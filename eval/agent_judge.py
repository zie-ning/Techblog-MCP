"""M7 답변 비교 채점: 같은 과제의 두 조건 답변을 나란히 놓고 어느 쪽이 더 도움이 되는지 판정한다.

    uv run python eval/agent_judge.py --dry-run              # 판정 대상 수와 예상 비용만
    uv run python eval/agent_judge.py --limit 6              # 일부만 판정 (채점기 확인용)
    uv run python eval/agent_judge.py --workers 4            # 전체 (이미 판정한 쌍은 건너뜀)

채점 방향은 docs/기획.md "에이전트 평가 (M7)". 사례 인용은 MCP 서버의 목적 자체라 채점 기준에
넣으면 MCP에 유리해진다. 그래서 질문한 개발자에게 답변이 실제로 더 도움이 되는지만 본다.
- 같은 과제·같은 회차의 두 답변을 비교한다 (mcp 대 none, mcp 대 web, mcp 대 web-ask)
- 조건 이름은 채점기에 주지 않는다
- 순서 편향을 막으려고 두 순서로 한 번씩 판정하고, 두 판정이 같을 때만 승패로 본다
결과는 eval/runs/agent/<name>/judge.jsonl에 캐시한다.
지시문·모델·두 답변이 같으면 다시 부르지 않는다.
"""

import argparse
import hashlib
import json
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 eval·pipeline을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from eval.agent_run import RUNS_DIR, RunRecord  # noqa: E402
from eval.agent_tasks import Task, load_tasks  # noqa: E402
from eval.inspect_run import cost, load_pricing  # noqa: E402
from pipeline.extract.schema import Usage  # noqa: E402

JUDGE_MODEL = (
    "gpt-5.5"  # 추출 평가 채점과 같은 모델 (M3 사용자 결정). Claude 답변을 다른 계열이 채점
)
JUDGE_EFFORT = "medium"
JUDGE_FILE = "judge.jsonl"
COMPARISONS = [("mcp", "none"), ("mcp", "web"), ("mcp", "web-ask")]
# 답변 품질을 비교할 수 없는 분류. 호출 금지 과제는 mcp 조건만 돌렸다
SKIP_CATEGORIES = {"no_call"}

Verdict = Literal["A", "B", "tie"]
CRITERIA = ("accuracy", "practicality", "reasoning", "fit", "clarity")

INSTRUCTIONS = """\
너는 시니어 소프트웨어 엔지니어다.
한 개발자가 코딩 에이전트에게 질문했고, 서로 다른 두 답변(A, B)이 있다.
질문한 개발자에게 어느 답변이 실제로 더 도움이 되는지 판정한다.

## 기준
- accuracy (정확성): 기술적으로 틀리거나 위험한 내용이 없는가.
  구체적인 주장(어떤 회사가 무엇을 했다, 어떤 수치가 나왔다)은 네 지식으로 판단하고,
  맞는지 판단할 수 없으면 점수에 반영하지 않는다.
- practicality (실무 고려): 실제로 만들고 운영할 때 부딪히는 문제
  (장애, 운영, 규모, 비용, 마이그레이션)를 다루는가.
- reasoning (판단 근거): 선택지 사이의 트레이드오프와 왜 그 선택을 권하는지가 드러나는가.
- fit (상황 적합성): 질문에 적힌 조건(규모, 제약, 기존 환경)에 맞춘 답인가.
  묻지 않은 쪽으로 흐르지 않는가.
- clarity (전달): 핵심이 잘 보이게 구성됐는가. 길이가 길다고 더 좋은 답이 아니다.

## 주의
- 출처 링크나 다른 회사 사례가 붙어 있다는 사실만으로 점수를 주지 않는다. 사례가 답의 판단을 실제로
  더 좋게 만들었을 때만 그 효과를 위 기준에 반영한다. 반대로 질문과 맞지 않는 사례를 늘어놓아
  핵심을 흐리면 fit·clarity에서 낮게 본다.
- 답변이 도구 사용, 검색 여부, 권한을 언급해도 그 자체는 평가하지 않는다. 개발자가 받은 내용만 본다.
- 두 답변의 순서는 무작위다. 순서에 영향받지 않는다.
- 차이가 작거나 장단점이 맞서면 tie로 한다.

각 기준과 overall(종합)에 A, B, tie 중 하나를 쓰고, reason에 판정 이유를 두세 문장으로 쓴다.
"""


class JudgeOutput(BaseModel):
    accuracy: Verdict
    practicality: Verdict
    reasoning: Verdict
    fit: Verdict
    clarity: Verdict
    overall: Verdict
    reason: str = Field(description="판정 이유 두세 문장")


@dataclass(frozen=True)
class Pair:
    task: Task
    left: RunRecord  # mcp 쪽
    right: RunRecord  # 비교 대상

    @property
    def key(self) -> str:
        return f"{self.task.id}__{self.left.condition}-vs-{self.right.condition}__r{self.left.rep}"


class JudgeRecord(BaseModel):
    pair: str
    order: Literal["left_first", "right_first"]
    output: JudgeOutput
    judge_model: str
    judge_effort: str
    prompt_version: str
    input_hash: str
    usage: Usage


def prompt_version() -> str:
    schema = json.dumps(JudgeOutput.model_json_schema(), ensure_ascii=False, sort_keys=True)
    return hashlib.sha256((INSTRUCTIONS + schema).encode("utf-8")).hexdigest()[:12]


def input_hash(pair: Pair) -> str:
    text = "\x00".join([pair.task.prompt, pair.left.answer, pair.right.answer])
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def build_pairs(tasks: list[Task], records: list[RunRecord]) -> list[Pair]:
    by_key = {(r.task_id, r.condition, r.rep): r for r in records}
    pairs = []
    for task in tasks:
        if task.category in SKIP_CATEGORIES:
            continue
        for left, right in COMPARISONS:
            for rep in sorted({r for (t, c, r) in by_key if t == task.id and c == left}):
                a, b = by_key.get((task.id, left, rep)), by_key.get((task.id, right, rep))
                # 답변이 없는 실행(시간 초과 등)은 비교하지 않는다
                if a and b and not a.is_error and not b.is_error:
                    pairs.append(Pair(task, a, b))
    return pairs


def judge_message(task: Task, first: str, second: str) -> str:
    return f"## 질문\n{task.prompt}\n\n## 답변 A\n{first}\n\n## 답변 B\n{second}"


def to_side(verdict: Verdict, order: str) -> str:
    """A/B 판정을 left/right/tie로 바꾼다."""
    if verdict == "tie":
        return "tie"
    left_is_a = order == "left_first"
    return "left" if (verdict == "A") == left_is_a else "right"


def combine(first: str, second: str) -> str:
    """두 순서의 판정을 합친다. 같으면 그 판정, 다르면 tie (순서 편향 제거)."""
    return first if first == second else "tie"


def pair_result(records: list[JudgeRecord]) -> dict[str, str] | None:
    """두 순서가 모두 판정된 쌍의 기준별 결과 {기준: left/right/tie}."""
    by_order = {r.order: r for r in records}
    if set(by_order) != {"left_first", "right_first"}:
        return None
    result = {}
    for name in (*CRITERIA, "overall"):
        sides = [
            to_side(getattr(by_order[o].output, name), o) for o in ("left_first", "right_first")
        ]
        result[name] = combine(*sides)
    return result


# ---------- 캐시 ----------


def load_judgements(path: Path) -> dict[tuple[str, str], JudgeRecord]:
    if not path.exists():
        return {}
    records = [
        JudgeRecord.model_validate_json(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line
    ]
    return {(r.pair, r.order): r for r in records}


def pending(
    pairs: list[Pair], cached: dict[tuple[str, str], JudgeRecord], model: str, effort: str
) -> list[tuple[Pair, str]]:
    version = prompt_version()
    todo = []
    for pair in pairs:
        h = input_hash(pair)
        for order in ("left_first", "right_first"):
            r = cached.get((pair.key, order))
            current = (
                r is not None
                and r.judge_model == model
                and r.judge_effort == effort
                and r.prompt_version == version
                and r.input_hash == h
            )
            if not current:
                todo.append((pair, order))
    return todo


def judge_one(llm, pair: Pair, order: str) -> JudgeRecord:
    first, second = (pair.left, pair.right) if order == "left_first" else (pair.right, pair.left)
    usage = Usage()
    message = judge_message(pair.task, first.answer, second.answer)
    output = llm.parse(
        INSTRUCTIONS, [{"role": "user", "content": message}], JudgeOutput, usage, "agent_judge"
    )
    return JudgeRecord(
        pair=pair.key,
        order=order,
        output=output,
        judge_model=llm.model,
        judge_effort=llm.reasoning_effort,
        prompt_version=prompt_version(),
        input_hash=input_hash(pair),
        usage=usage,
    )


# ---------- 요약 ----------


def summarize(pairs: list[Pair], judged: dict[tuple[str, str], JudgeRecord]) -> list[str]:
    """비교 쌍별 overall 승·무·패 (mcp 기준)."""
    tally: dict[str, Counter] = {}
    for pair in pairs:
        records = [
            judged[(pair.key, o)] for o in ("left_first", "right_first") if (pair.key, o) in judged
        ]
        result = pair_result(records)
        if result is None:
            continue
        name = f"mcp vs {pair.right.condition}"
        tally.setdefault(name, Counter())[result["overall"]] += 1
    lines = []
    for name, c in tally.items():
        total = sum(c.values())
        lines.append(f"{name}: mcp 승 {c['left']} · 무 {c['tie']} · 패 {c['right']} (쌍 {total})")
    return lines


def estimate_cost(todo: list[tuple[Pair, str]], price: dict) -> float:
    # 한국어는 대략 2자당 1토큰. 출력은 reasoning 포함 대략치
    tokens_in = sum(
        (len(p.left.answer) + len(p.right.answer) + len(INSTRUCTIONS)) // 2 for p, _ in todo
    )
    usage = Usage(input_tokens=tokens_in, output_tokens=2000 * len(todo))
    return cost(usage, price)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--name", default="m7-sonnet", help="실행 묶음 이름 (eval/runs/agent/<name>)"
    )
    parser.add_argument("--model", default=JUDGE_MODEL)
    parser.add_argument("--effort", default=JUDGE_EFFORT)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--limit", type=int, help="앞에서부터 이 수만큼의 쌍만 판정")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_dir = RUNS_DIR / args.name
    records = [
        RunRecord.model_validate_json(line)
        for line in (run_dir / "records.jsonl").read_text(encoding="utf-8").splitlines()
        if line
    ]
    pairs = build_pairs(load_tasks(), records)
    if args.limit:
        pairs = pairs[: args.limit]
    judge_path = run_dir / JUDGE_FILE
    cached = load_judgements(judge_path)
    todo = pending(pairs, cached, args.model, args.effort)
    price = load_pricing().get(args.model)
    estimate = f"예상 비용 ${estimate_cost(todo, price):.2f}" if price else "단가 없음"
    print(
        f"비교 쌍 {len(pairs)}개, 남은 판정 {len(todo)}회 ({args.model} {args.effort}), {estimate}"
    )
    if args.dry_run or not todo:
        print("\n".join(summarize(pairs, cached)))
        return

    from dotenv import load_dotenv

    from pipeline.extract.extractor import OpenAILLM

    load_dotenv(ROOT / ".env")
    llm = OpenAILLM(args.model, args.effort)
    total = Usage()
    with (
        ThreadPoolExecutor(max_workers=args.workers) as pool,
        judge_path.open("a", encoding="utf-8") as f,
    ):
        futures = {pool.submit(judge_one, llm, p, o): (p, o) for p, o in todo}
        for i, future in enumerate(as_completed(futures), 1):
            pair, order = futures[future]
            try:
                record = future.result()
            except Exception as e:  # 한 쌍이 실패해도 나머지는 계속한다. 다시 돌리면 이어서 판정
                print(f"[{i}/{len(todo)}] {pair.key} {order} 실패: {e}", flush=True)
                continue
            f.write(record.model_dump_json() + "\n")
            f.flush()
            cached[(record.pair, record.order)] = record
            total.add(record.usage)
            print(f"[{i}/{len(todo)}] {pair.key} {order} → {record.output.overall}", flush=True)
    if price:
        print(f"실제 비용 ${cost(total, price):.2f}")
    print("\n".join(summarize(pairs, cached)))


if __name__ == "__main__":
    main()
