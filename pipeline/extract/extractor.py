"""글 한 편 추출: 글 유형 분류 → 구조화 → 발췌 검증 → 기술명 정규화.

발췌 검증에 실패한 항목이 있으면 실패 목록을 알려 주고 한 번 다시 구조화한 뒤,
두 시도 중 검증을 통과한 내용이 더 많은 쪽을 쓴다. 그래도 실패한 항목은 버리고,
해결 방법이 비는 항목은 통째로 버린다. 버린 발췌는 글별 기록에 남긴다.
"""

import hashlib
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Protocol, TypeVar

from langsmith import traceable
from pydantic import BaseModel

from pipeline.collect import COMPANY_NAMES
from pipeline.collect.raw import RawPost
from pipeline.extract import prompt_version, prompts, tracing
from pipeline.extract.evidence import SourceText
from pipeline.extract.schema import (
    GENERIC_DOMAIN,
    MAX_DOMAINS,
    MAX_PROBLEM_TYPES,
    Classification,
    Entry,
    EntryDraft,
    Evidenced,
    Extraction,
    FailedEvidence,
    Point,
    PostRecord,
    QuarantineRecord,
    RejectedAlternative,
    Usage,
)
from pipeline.extract.text import html_to_text
from pipeline.normalize import renormalize

T = TypeVar("T", bound=BaseModel)


class LLM(Protocol):
    model: str
    reasoning_effort: str

    def parse(
        self, instructions: str, messages: list[dict], schema: type[T], usage: Usage, step: str
    ) -> T:
        """구조화 출력을 받고 이번 호출의 사용량을 `usage`에 더한다. `step`은 트레이스 단계 이름."""
        ...


class OpenAILLM:
    def __init__(self, model: str, reasoning_effort: str = "medium"):
        from langsmith.wrappers import wrap_openai
        from openai import OpenAI

        self.model = model
        self.reasoning_effort = reasoning_effort
        # 트레이싱이 꺼져 있으면 감싸도 아무것도 보내지 않는다
        # 일시적인 연결 오류로 글이 통째로 실패하지 않게 기본(2회)보다 넉넉히 재시도한다
        self._client = wrap_openai(OpenAI(max_retries=6))

    def parse(
        self, instructions: str, messages: list[dict], schema: type[T], usage: Usage, step: str
    ) -> T:
        response = self._client.responses.parse(
            model=self.model,
            instructions=instructions,
            input=messages,
            text_format=schema,
            reasoning={"effort": self.reasoning_effort},
            langsmith_extra={"name": step},
        )
        usage.add(_usage_of(response))
        if response.output_parsed is None:
            raise RuntimeError(f"구조화 출력을 받지 못했습니다: {response.output_text[:200]}")
        return response.output_parsed


def _usage_of(response) -> Usage:
    u = response.usage
    if u is None:
        return Usage(calls=1)
    input_details = getattr(u, "input_tokens_details", None)
    output_details = getattr(u, "output_tokens_details", None)
    return Usage(
        calls=1,
        input_tokens=u.input_tokens,
        cached_input_tokens=getattr(input_details, "cached_tokens", 0) or 0,
        output_tokens=u.output_tokens,
        reasoning_tokens=getattr(output_details, "reasoning_tokens", 0) or 0,
    )


@dataclass
class ExtractResult:
    record: PostRecord  # entry_ids는 저장 시 채운다
    entries: list[Entry]  # id는 저장 시 채운다
    # 검증 전 LLM 출력(분류, 구조화 시도들). 발췌 검증 기준을 LLM 재호출 없이 비교하는 데 쓴다
    raw_outputs: dict
    # 발췌 검증에 실패한 내용이 있는 항목 (채택한 시도 기준). data/quarantine.jsonl에 보관한다
    quarantined: list[QuarantineRecord] = field(default_factory=list)


def content_hash(post: RawPost) -> str:
    return hashlib.sha256(post.content_html.encode("utf-8")).hexdigest()[:16]


def extraction_reason(
    previous: PostRecord | None,
    post: RawPost,
    model: str,
    current_prompt_version: str,
    outdated: bool,
) -> str | None:
    """이 글을 (다시) 추출해야 하는 이유. 건너뛸 글이면 None.

    기본은 새 글과 원문이 바뀐 글만 추출한다. `outdated`면 다른 프롬프트·모델로 추출한 글도
    다시 추출한다. 프롬프트를 고칠 때마다 자동으로 전체를 다시 돌리면 비용이 크므로 명시적으로 켠다.
    """
    if previous is None:
        return "신규"
    if previous.content_hash != content_hash(post):
        return "원문 변경"
    if outdated and previous.prompt_version != current_prompt_version:
        return f"프롬프트 변경 {previous.prompt_version} → {current_prompt_version}"
    if outdated and previous.model != model:
        return f"모델 변경 {previous.model} → {model}"
    return None


@traceable(
    name="extract_post",
    run_type="chain",
    process_inputs=tracing.root_inputs,
    process_outputs=tracing.root_outputs,
)
def extract_post(post: RawPost, llm: LLM) -> ExtractResult:
    text = html_to_text(post.content_html)
    source = SourceText(text)
    user_input = [{"role": "user", "content": prompts.post_input(post.title, text)}]

    usage = Usage()
    classification = llm.parse(prompts.CLASSIFY, user_input, Classification, usage, "분류")
    raw_outputs: dict = {"classification": classification.model_dump(), "attempts": []}

    chosen = _Attempt(results=[])
    first: _Attempt | None = None
    if classification.kind == "추출":
        instructions, schema = prompts.structure(), Extraction
        result = llm.parse(instructions, user_input, schema, usage, "구조화")
        raw_outputs["attempts"].append(result.model_dump())
        chosen = first = _verify_all(result, source)
        if chosen.dropped:
            retry_input = [
                *user_input,
                {"role": "assistant", "content": result.model_dump_json()},
                {"role": "user", "content": prompts.evidence_retry(chosen.dropped)},
            ]
            retry_result = llm.parse(instructions, retry_input, schema, usage, "재시도")
            raw_outputs["attempts"].append(retry_result.model_dump())
            retry = _verify_all(retry_result, source)
            # 재시도가 항상 낫지는 않으므로 검증을 통과한 내용이 더 많은 쪽을 쓴다
            if retry.score() > chosen.score():
                chosen = retry
    dropped = chosen.dropped
    version = prompt_version.version()
    extracted_at = datetime.now(UTC).isoformat(timespec="seconds")

    record = PostRecord(
        source=post.source,
        post_id=post.post_id,
        url=post.url,
        title=post.title,
        published_at=post.published_at.date().isoformat(),
        post_type=classification.post_type,
        kind=classification.kind,
        reason=classification.reason,
        content_hash=content_hash(post),
        model=llm.model,
        reasoning_effort=llm.reasoning_effort,
        prompt_version=version,
        extracted_at=extracted_at,
        entry_ids=[],
        dropped_evidence=len(dropped),
        dropped_evidences=dropped,
        evidence_total=chosen.total,
        usage=usage,
        first_attempt_total=first.total if first else None,
        first_attempt_dropped=len(first.dropped) if first else None,
    )
    quarantined = [
        QuarantineRecord(
            source=post.source,
            post_id=post.post_id,
            post_url=post.url,
            post_title=post.title,
            model=llm.model,
            prompt_version=version,
            extracted_at=extracted_at,
            entry_dropped=verified is None,
            failed=failed,
            draft=draft,
        )
        for draft, verified, failed in chosen.results
        if failed
    ]
    return ExtractResult(
        record=record,
        entries=[to_entry(d, post) for d in chosen.drafts],
        raw_outputs=raw_outputs,
        quarantined=quarantined,
    )


@dataclass
class _Attempt:
    """구조화 시도 한 번의 검증 결과."""

    # 항목별 (검증 전 항목, 검증을 통과한 항목 또는 버렸으면 None, 실패한 발췌)
    results: list[tuple[EntryDraft, EntryDraft | None, list[FailedEvidence]]]

    @property
    def drafts(self) -> list[EntryDraft]:
        """검증을 통과한 항목들"""
        return [verified for _, verified, _ in self.results if verified is not None]

    @property
    def dropped(self) -> list[str]:
        """버린 발췌"""
        return [f.evidence for _, _, failed in self.results for f in failed]

    @property
    def total(self) -> int:
        """검증 전 발췌 수"""
        return sum(len(_evidences(draft)) for draft, _, _ in self.results)

    def score(self) -> tuple[int, int, int]:
        """남은 항목 수 → 남은 발췌 수 → 버린 발췌가 적은 순으로 비교한다."""
        kept = sum(len(_evidences(d)) for d in self.drafts)
        return len(self.drafts), kept, -len(self.dropped)


def _verify_all(result: Extraction, source: SourceText) -> _Attempt:
    return _Attempt(results=[(d, *verify_draft(d, source)) for d in result.entries])


def _evidences(draft: EntryDraft) -> list[str]:
    points = [*draft.problem_situation, *draft.solution, *draft.performance_ops]
    return [p.evidence for p in points] + [r.evidence for r in draft.rejected_alternatives]


def verify_draft(
    draft: EntryDraft, source: SourceText
) -> tuple[EntryDraft | None, list[FailedEvidence]]:
    """발췌가 원문에 없는 포인트를 버린다. 해결 방법이 비면 None. (결과, 실패한 발췌 목록)"""
    failed: list[FailedEvidence] = []

    def keep(field_name: str, points: list[Point]) -> list[Point]:
        kept = []
        for p in points:
            if source.contains(p.evidence):
                kept.append(p)
            else:
                failed.append(FailedEvidence(field=field_name, text=p.text, evidence=p.evidence))
        return kept

    rejected = []
    for r in draft.rejected_alternatives:
        if source.contains(r.evidence):
            rejected.append(r)
        else:
            text = f"{r.name}: {r.reason}"
            failed.append(
                FailedEvidence(field="rejected_alternatives", text=text, evidence=r.evidence)
            )
    verified = draft.model_copy(
        update={
            "problem_situation": keep("problem_situation", draft.problem_situation),
            "solution": keep("solution", draft.solution),
            "performance_ops": keep("performance_ops", draft.performance_ops),
            "rejected_alternatives": rejected,
        }
    )
    # 문제 상황은 팁·활용 경험 글에서 비어 있을 수 있어 해결 방법만 필수로 본다
    return (verified if verified.solution else None), failed


def _dedupe(items: list[str]) -> list[str]:
    return list(dict.fromkeys(i.strip() for i in items if i.strip()))


def _domains(names: list[str]) -> list[str]:
    """중복 제거, 범용은 다른 도메인이 있으면 뺀다, 최대 개수."""
    domains = _dedupe(names)
    if len(domains) > 1:
        domains = [d for d in domains if d != GENERIC_DOMAIN]
    return domains[:MAX_DOMAINS]


def to_entry(draft: EntryDraft, post: RawPost) -> Entry:

    def evidenced(points: list[Point]) -> list[Evidenced]:
        return [Evidenced(text=p.text, evidence=p.evidence) for p in points]

    entry = Entry(
        id="",
        source=post.source,
        company=COMPANY_NAMES[post.source],
        post_url=post.url,
        post_title=post.title,
        published_at=post.published_at.date().isoformat(),
        problem_types=_dedupe(draft.problem_types)[:MAX_PROBLEM_TYPES],
        domains=_domains(draft.domains),
        technologies=[],  # 아래 renormalize에서 채운다
        technologies_raw=_dedupe(draft.technologies),
        tags=_dedupe(draft.tags),
        problem_situation=evidenced(draft.problem_situation),
        solution=evidenced(draft.solution),
        performance_ops=evidenced(draft.performance_ops),
        rejected_alternatives=[
            RejectedAlternative(
                name=r.name.strip(),  # 아래 renormalize에서 정규화한다
                name_raw=r.name.strip(),
                kind=r.kind,
                reason=r.reason,
                evidence=r.evidence,
            )
            for r in draft.rejected_alternatives
        ],
    )
    # 기술명 정규화 규칙은 사전 보강 후 재정규화(pipeline.normalize)와 같은 함수 하나로 적용한다
    return renormalize(entry)[0]
