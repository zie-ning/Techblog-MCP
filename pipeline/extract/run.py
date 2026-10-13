"""추출 대상 고르기와 여러 글 추출.

추출 명령(`pipeline.extract`)과 자동 갱신(`pipeline.update`)이 함께 쓴다.
"""

from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field

from pipeline.collect.raw import RawPost
from pipeline.extract import tracing
from pipeline.extract.extractor import LLM, extract_post, extraction_reason
from pipeline.extract.schema import PostRecord, Usage
from pipeline.extract.store import Store

# M3 모델 비교로 확정 (docs/기획.md "추출 LLM"). effort 기본값 medium
DEFAULT_MODEL = "gpt-5.6-luna"


@dataclass
class Todo:
    post: RawPost
    reason: str  # 신규, 원문 변경, 프롬프트 변경 등


def plan(
    posts: Iterable[RawPost],
    store: Store,
    model: str,
    current_version: str,
    outdated: bool = False,
    force: bool = False,
    limit: int | None = None,
) -> list[Todo]:
    """(다시) 추출할 글. 건너뛸 글은 빼고, `limit`은 추출할 글만 센다."""
    todo = []
    for post in posts:
        if limit is not None and len(todo) >= limit:
            break
        previous = store.record_for(post.url)
        reason = extraction_reason(previous, post, model, current_version, outdated)
        if force and reason is None:
            reason = "강제"
        if reason is not None:
            todo.append(Todo(post, reason))
    return todo


@dataclass
class ExtractReport:
    done: int = 0
    records: list[PostRecord] = field(default_factory=list)  # 이번에 추출한 글의 기록
    failures: list[tuple[RawPost, str]] = field(default_factory=list)
    usage: Usage = field(default_factory=Usage)


def extract_all(
    todo: list[Todo],
    store: Store,
    llm: LLM,
    current_version: str,
    workers: int = 1,
    run_name: str = "",
) -> ExtractReport:
    """글마다 추출해 저장소에 반영한다. 한 편이 실패해도 나머지는 계속한다.

    실패한 글은 기록을 남기지 않으므로 다음 실행에서 다시 추출 대상이 된다.
    `run_name`은 트레이스에 붙일 실행 이름이다.
    """
    report = ExtractReport()
    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        futures = {
            pool.submit(
                extract_post,
                t.post,
                llm,
                langsmith_extra=tracing.post_extra(
                    t.post, run_name, llm.model, llm.reasoning_effort, current_version
                ),
            ): t
            for t in todo
        }
        # 저장은 메인 스레드에서만 한다
        for n, future in enumerate(as_completed(futures), 1):
            t = futures[future]
            label = f"[{n}/{len(todo)}] {t.post.source}/{t.post.post_id} ({t.reason})"
            try:
                result = future.result()
            except Exception as e:  # 한 편이 실패해도 나머지는 계속한다
                report.failures.append((t.post, f"{type(e).__name__}: {e}"))
                print(f"{label} 실패: {e}")
                continue
            ids = store.add(result)
            store.save()  # 중간에 멈춰도 진행분을 잃지 않도록 매번 저장
            report.done += 1
            r = result.record
            report.records.append(store.posts[r.url])  # 항목 ID가 채워진 저장본
            report.usage.add(r.usage)
            print(
                f"{label} {r.kind}/{r.post_type} 항목 {len(ids)}개, "
                f"발췌 탈락 {r.dropped_evidence}/{r.evidence_total}개"
            )
    return report


def usage_summary(u: Usage) -> str:
    return (
        f"호출 {u.calls}회, 입력 {u.input_tokens:,}(캐시 {u.cached_input_tokens:,}) / "
        f"출력 {u.output_tokens:,}(reasoning {u.reasoning_tokens:,}) 토큰"
    )
