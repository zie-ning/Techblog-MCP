"""정답셋 기준 LLM 채점.

    uv run python eval/judge.py eval/runs/v3-gpt-5-mini-medium --dry-run   # 예상 비용만
    uv run python eval/judge.py eval/runs/v3-gpt-5-mini-medium --workers 4 [--trace]

정답셋(`eval/gold/`)에 있는 글마다 원문 평문, 추출 결과, 정답 항목을 채점 모델에 주고
구조화 출력으로 다음을 받는다.

- 항목 대응표: 정답 항목마다 대응하는 추출 항목과 핵심 사실(`key_facts`) 포함 여부 → 완결성
- 추출 항목별 점수(1~5): 충실성(원문에 근거), 카드 요약 적합성
- 버린 대안 판정: 정답의 어느 대안과 같은지, 원문에 버린 이유가 명시돼 있는지
- 글 단위 분할 적절성(1~5)

결과는 `{run}/judge.jsonl`에 캐시한다. 채점 프롬프트·모델·입력(추출 결과와 정답)이 같으면
다시 부르지 않으므로, 정답을 검수해 고친 글만 다시 채점된다.
지표 계산과 리포트는 extract_eval.py가 한다.
"""

import argparse
import hashlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 pipeline을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from eval.compare_runs import Run  # noqa: E402
from eval.gold import GoldPost, load_gold  # noqa: E402
from eval.inspect_run import cost, load_pricing  # noqa: E402
from pipeline.collect import raw  # noqa: E402
from pipeline.extract.schema import Entry, PostRecord, Usage  # noqa: E402
from pipeline.extract.text import html_to_text  # noqa: E402

# 채점 모델은 추출 후보보다 상위 모델로 고정한다. 바꾸면 이전 채점 결과와 직접 비교하지 않는다.
JUDGE_MODEL = "gpt-5.4"
JUDGE_EFFORT = "medium"
JUDGE_FILE = "judge.jsonl"

INSTRUCTIONS = """\
너는 기술 블로그 글에서 구조화 데이터를 뽑는 추출기의 결과를 채점한다.
입력은 원문 평문, 사람이 만든 정답, 추출 결과 세 부분이다.

## 대응표 (matches)
정답 항목마다 하나씩 쓴다.
- extracted_ids: 같은 문제-해법을 다룬 추출 항목 id.
  정답 하나가 추출 여러 개로 나뉘었으면 모두 넣고,
  대응하는 추출 항목이 없으면 빈 목록.
- key_facts_covered: 정답의 key_facts 순서대로, 대응한 추출 항목들의 내용에 그 사실이 담겼는지.
  표현이 달라도 같은 뜻이고 수치가 맞으면 true. 수치가 빠지거나 틀리면 false.
  대응 항목이 없으면 모두 false.

## 추출 항목 점수 (entries)
추출 항목마다 하나씩 쓴다. 점수는 1~5 정수.
- faithfulness (충실성): 항목의 모든 문장이 원문에 근거하는가.
  5 = 전부 원문에 있음, 3 = 일부 과장·추측·다른 맥락의 내용이 섞임, 1 = 핵심 내용이 원문과 다름.
  원문에 없는 주장은 unsupported_claims에 그대로 옮긴다.
- card_summary (카드 요약 적합성): 검색 카드에 보이는 첫 줄만 읽고 이 항목을 고를 수 있는가.
  카드에는 "문제 상황"(있으면), "해결 방법", "성능·운영 포인트"(있으면)의 첫 줄이 보인다.
  5 = 첫 줄들이 문제와 최종 해결책(팁·활용 경험 글은 글의 요지)을 구체적으로 담음,
  3 = 맞지만 막연하거나 최종 해결책이 아닌 중간 단계·배경을 담음,
  1 = 첫 줄로는 무엇을 했는지 알 수 없음.

## 버린 대안 (rejected)
추출 결과의 버린 대안마다 하나씩 쓴다.
- gold_name: 같은 대안을 가리키는 정답의 버린 대안 이름. 없으면 빈 문자열.
- supported: 원문에 "검토했거나 기존에 쓰다가 이런 이유로 쓰지 않았다"는 내용이 명시돼 있으면 true.
  원문에 언급만 되거나 추출기가 추측한 대안이면 false.

## 분할 (split_score)
글 전체에서 추출 항목을 나눈 방식이 적절한가. 1~5 정수.
독립적인 문제-해법 쌍마다 항목 하나, 같은 문제의 단계적 해결은 한 항목,
팁 모음·도구 활용 경험 글은 항목 하나가 기준이다.
정답의 항목 수와 달라도 이 기준에 맞으면 높은 점수를 준다.
5 = 기준에 맞음, 3 = 곁가지·팁을 항목으로 만들거나 독립된 문제를 합침,
1 = 글의 핵심 내용이 빠지거나 뒤섞임.
정답이 제외 글이면(정답 항목 없음) 추출한 것 자체가 잘못이므로 1점.

reason 필드는 한국어 한두 문장으로 쓴다.
"""


class EntryMatch(BaseModel):
    gold_index: int = Field(description="정답 항목 번호 (1부터)")
    extracted_ids: list[str] = Field(description="대응하는 추출 항목 id. 없으면 빈 목록")
    key_facts_covered: list[bool] = Field(description="정답 key_facts 순서대로 담겼는지")
    reason: str


class EntryScore(BaseModel):
    entry_id: str
    faithfulness: int = Field(description="1~5")
    card_summary: int = Field(description="1~5")
    unsupported_claims: list[str] = Field(description="원문에 근거 없는 주장. 없으면 빈 목록")
    reason: str


class RejectedJudgement(BaseModel):
    entry_id: str
    name: str = Field(description="추출 결과의 버린 대안 이름")
    gold_name: str = Field(description="같은 대안을 가리키는 정답 이름. 없으면 빈 문자열")
    supported: bool = Field(description="원문에 버린 이유가 명시돼 있는지")
    reason: str


class JudgeOutput(BaseModel):
    matches: list[EntryMatch]
    entries: list[EntryScore]
    rejected: list[RejectedJudgement]
    split_score: int = Field(description="1~5")
    split_reason: str


class JudgeRecord(BaseModel):
    """judge.jsonl 한 줄."""

    source: str
    post_id: str
    judge_model: str
    judge_effort: str
    judge_prompt_version: str
    input_hash: str  # 추출 결과 + 정답. 둘 중 하나가 바뀌면 다시 채점한다
    output: JudgeOutput | None  # 채점할 것이 없는 글(양쪽 다 항목 없음)은 None
    usage: Usage = Usage()


def prompt_version() -> str:
    schema = json.dumps(JudgeOutput.model_json_schema(), ensure_ascii=False, sort_keys=True)
    return hashlib.sha256((INSTRUCTIONS + schema).encode("utf-8")).hexdigest()[:12]


def _points(points: list) -> list[str]:
    return [p.text for p in points]


def entry_view(e: Entry) -> dict:
    """채점 모델에 보여 줄 추출 항목. 발췌는 이미 원문 대조를 통과했으므로 요약 문장만 넣는다."""
    view: dict = {
        "id": e.id,
        "problem_types": e.problem_types,
        "domains": e.domains,
        "technologies": e.technologies_raw,
    }
    view |= {
        "문제 상황": _points(e.problem_situation),
        "해결 방법": _points(e.solution),
        "성능·운영 포인트": _points(e.performance_ops),
        "버린 대안": [
            {"name": r.name, "kind": r.kind, "reason": r.reason} for r in e.rejected_alternatives
        ],
    }
    return view


def gold_view(gold: GoldPost) -> dict:
    return {
        "kind": gold.kind,
        "entries": [
            {
                "index": i,
                "summary": g.summary,
                "key_facts": g.key_facts,
                "버린 대안": [f"{r.name} ({r.kind})" for r in g.rejected_alternatives],
            }
            for i, g in enumerate(gold.entries, 1)
        ],
    }


def input_hash(gold: GoldPost, entries: list[Entry]) -> str:
    payload = json.dumps(
        {"gold": gold_view(gold), "entries": [entry_view(e) for e in entries]},
        ensure_ascii=False,
        sort_keys=True,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def needs_llm(gold: GoldPost, entries: list[Entry]) -> bool:
    """추출 항목이 없으면 점수는 계산만으로 정해진다(완결성 0 또는 채점 대상 없음)."""
    return bool(entries)


def judge_message(title: str, text: str, gold: GoldPost, entries: list[Entry]) -> str:
    dump = lambda v: json.dumps(v, ensure_ascii=False, indent=1)  # noqa: E731
    return (
        f"# 원문\n제목: {title}\n\n{text}\n\n"
        f"# 정답\n{dump(gold_view(gold))}\n\n"
        f"# 추출 결과\n{dump([entry_view(e) for e in entries])}\n"
    )


def judge_post(
    llm, title: str, text: str, gold: GoldPost, entries: list[Entry], version: str
) -> JudgeRecord:
    usage = Usage()
    output = None
    if needs_llm(gold, entries):
        messages = [{"role": "user", "content": judge_message(title, text, gold, entries)}]
        output = llm.parse(INSTRUCTIONS, messages, JudgeOutput, usage, "채점")
    return JudgeRecord(
        source=gold.source,
        post_id=gold.post_id,
        judge_model=llm.model,
        judge_effort=llm.reasoning_effort,
        judge_prompt_version=version,
        input_hash=input_hash(gold, entries),
        output=output,
        usage=usage,
    )


def load_judgements(run_dir: Path) -> dict[tuple[str, str], JudgeRecord]:
    """글별 최신 채점 결과. 같은 글이 여러 번 있으면 나중 줄이 이긴다."""
    path = run_dir / JUDGE_FILE
    if not path.exists():
        return {}
    records = [
        JudgeRecord.model_validate_json(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    return {(r.source, r.post_id): r for r in records}


def is_current(record: JudgeRecord | None, model: str, effort: str, version: str, h: str) -> bool:
    return (
        record is not None
        and record.judge_model == model
        and record.judge_effort == effort
        and record.judge_prompt_version == version
        and record.input_hash == h
    )


def run_entries(run_dir: Path) -> tuple[dict[tuple[str, str], PostRecord], dict[str, list[Entry]]]:
    # extract_eval.py와 같은 입력 해시가 나오도록 같은 방식(현재 사전으로 재정규화)으로 읽는다
    run = Run.load(run_dir)
    by_key = {(p.source, p.post_id): p for p in run.posts}
    by_url: dict[str, list[Entry]] = {}
    for e in run.entries:
        by_url.setdefault(e.post_url, []).append(e)
    return by_key, by_url


def pending(
    run_dir: Path, golds: dict[tuple[str, str], GoldPost], model: str, effort: str
) -> list[tuple[GoldPost, PostRecord, list[Entry]]]:
    """채점이 필요한 글 (캐시와 입력이 다른 글)."""
    by_key, by_url = run_entries(run_dir)
    cached = load_judgements(run_dir)
    version = prompt_version()
    todo = []
    for key, gold in sorted(golds.items()):
        record = by_key.get(key)
        if record is None:
            continue
        entries = by_url.get(record.url, [])
        if not is_current(cached.get(key), model, effort, version, input_hash(gold, entries)):
            todo.append((gold, record, entries))
    return todo


def estimate_tokens(text: str) -> int:
    """한국어가 섞인 글의 대략적인 토큰 수 (글자 수 기준 보수적 추정)."""
    return len(text)


def main() -> None:
    parser = argparse.ArgumentParser(description="정답셋 기준 LLM 채점")
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--model", default=JUDGE_MODEL)
    parser.add_argument("--effort", default=JUDGE_EFFORT)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--dry-run", action="store_true", help="채점할 글 수와 예상 비용만 출력")
    parser.add_argument("--trace", action="store_true", help="LangSmith 트레이스 전송")
    args = parser.parse_args()

    golds = load_gold()
    todo = pending(args.run_dir, golds, args.model, args.effort)
    texts = {}
    for gold, _, _ in todo:
        post = raw.RawPost.from_json(
            raw.raw_path(gold.source, gold.post_id).read_text(encoding="utf-8")
        )
        texts[(gold.source, gold.post_id)] = (post.title, html_to_text(post.content_html))
    llm_todo = [t for t in todo if needs_llm(t[0], t[2])]
    price = load_pricing().get(args.model)
    est_in = sum(
        estimate_tokens(judge_message(*texts[(g.source, g.post_id)], g, es)) + len(INSTRUCTIONS)
        for g, _, es in llm_todo
    )
    est_out = 4000 * len(llm_todo)  # reasoning 포함 대략치
    est = cost(Usage(input_tokens=est_in, output_tokens=est_out), price) if price else None
    print(
        f"채점 대상 {len(todo)}편 (LLM 호출 {len(llm_todo)}편), 모델 {args.model} ({args.effort}), "
        f"추정 입력 {est_in:,} / 출력 {est_out:,} 토큰"
        + (f", 예상 비용 ${est:.2f}" if est is not None else "")
    )
    if args.dry_run or not todo:
        return

    from dotenv import load_dotenv

    from pipeline.extract import tracing
    from pipeline.extract.extractor import OpenAILLM

    load_dotenv(ROOT / ".env")
    if args.trace:
        print(f"LangSmith 프로젝트: {tracing.enable()}")
    llm = OpenAILLM(args.model, args.effort)
    version = prompt_version()
    out = args.run_dir / JUDGE_FILE
    total = Usage()
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {
            pool.submit(judge_post, llm, *texts[(g.source, g.post_id)], g, es, version): g
            for g, _, es in todo
        }
        with out.open("a", encoding="utf-8") as f:
            for n, future in enumerate(as_completed(futures), 1):
                gold = futures[future]
                try:
                    record = future.result()
                except Exception as e:  # 한 글 실패로 전체를 멈추지 않는다
                    print(f"[{n}/{len(todo)}] {gold.source}/{gold.post_id} 실패: {e}")
                    continue
                f.write(record.model_dump_json() + "\n")
                f.flush()
                total.add(record.usage)
                print(f"[{n}/{len(todo)}] {gold.source}/{gold.post_id}")
    spent = f", 비용 ${cost(total, price):.2f}" if price else ""
    print(
        f"완료: 호출 {total.calls}회, 입력 {total.input_tokens:,}, 출력 {total.output_tokens:,}"
        f"{spent} → {out}"
    )


if __name__ == "__main__":
    main()
