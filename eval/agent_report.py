"""M7 에이전트 평가 리포트: 답변 비교 판정과 실행 진단 지표를 한 문서로 정리한다.

    uv run python eval/agent_report.py   # → eval/reports/m7-agent.md

핵심 결과는 답변 비교 판정(eval/agent_judge.py)이다. 도구 호출률·검색어·비용 같은 진단 지표는
결과가 왜 그렇게 나왔는지 설명하는 데만 쓴다 (docs/기획.md "에이전트 평가 (M7)").
"""

import argparse
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 eval 모듈을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from eval.agent_judge import (  # noqa: E402
    COMPARISONS,
    CRITERIA,
    JUDGE_FILE,
    JudgeRecord,
    Pair,
    build_pairs,
    load_judgements,
    pair_result,
    to_side,
)
from eval.agent_run import RUNS_DIR, RunRecord  # noqa: E402
from eval.agent_tasks import Task, load_tasks  # noqa: E402
from eval.inspect_run import cost, load_pricing  # noqa: E402
from pipeline.extract.schema import Usage  # noqa: E402

REPORTS = ROOT / "eval" / "reports"
TECHBLOG_TOOLS = {"search", "get_details", "aggregate"}
CRITERIA_NAMES = {
    "accuracy": "정확성",
    "practicality": "실무 고려",
    "reasoning": "판단 근거",
    "fit": "상황 적합성",
    "clarity": "전달",
    "overall": "종합",
}
CATEGORY_NAMES = {
    "design": "설계",
    "few": "사례 적음",
    "noise": "검색 잡음",
    "aggregate": "집계",
    "absent": "없는 주제",
    "concept": "개념",
    "open": "DB와 무관한 과제",
    "no_call": "호출 금지",
}
ORDERS = ("left_first", "right_first")


def _results(pairs: list[Pair], judged: dict) -> list[tuple[Pair, dict]]:
    out = []
    for pair in pairs:
        result = pair_result([judged[(pair.key, o)] for o in ORDERS if (pair.key, o) in judged])
        if result is not None:
            out.append((pair, result))
    return out


def _wtl(counter: Counter) -> str:
    """승·무·패와 승률(무승부 제외 없이 전체 대비)."""
    total = sum(counter.values()) or 1
    w, t, lo = counter["left"], counter["tie"], counter["right"]
    return f"{w} / {t} / {lo} | {w / total:.0%} / {lo / total:.0%}"


def overall_table(results: list[tuple[Pair, dict]]) -> list[str]:
    lines = ["| 비교 | 쌍 | MCP 승 / 무 / 패 | 승률 / 패율 |", "| --- | --- | --- | --- |"]
    for _, right in COMPARISONS:
        c = Counter(r["overall"] for p, r in results if p.right.condition == right)
        lines.append(f"| mcp vs {right} | {sum(c.values())} | {_wtl(c)} |")
    return lines


def criteria_table(results: list[tuple[Pair, dict]]) -> list[str]:
    heads = [f"mcp vs {right}" for _, right in COMPARISONS]
    lines = ["| 기준 | " + " | ".join(heads) + " |", "| --- |" + " --- |" * len(heads)]
    for name in (*CRITERIA, "overall"):
        cells = []
        for _, right in COMPARISONS:
            c = Counter(r[name] for p, r in results if p.right.condition == right)
            cells.append(f"{c['left']} / {c['tie']} / {c['right']}")
        lines.append(f"| {CRITERIA_NAMES[name]} | " + " | ".join(cells) + " |")
    return lines


def category_table(results: list[tuple[Pair, dict]]) -> list[str]:
    heads = [f"mcp vs {right}" for _, right in COMPARISONS]
    lines = ["| 분류 | " + " | ".join(heads) + " |", "| --- |" + " --- |" * len(heads)]
    by: dict[tuple[str, str], Counter] = defaultdict(Counter)
    categories = []
    for pair, r in results:
        if pair.task.category not in categories:
            categories.append(pair.task.category)
        by[(pair.task.category, pair.right.condition)][r["overall"]] += 1
    for cat in categories:
        cells = []
        for _, right in COMPARISONS:
            c = by[(cat, right)]
            cells.append(f"{c['left']} / {c['tie']} / {c['right']}")
        lines.append(f"| {CATEGORY_NAMES.get(cat, cat)} | " + " | ".join(cells) + " |")
    return lines


def order_consistency(pairs: list[Pair], judged: dict) -> tuple[int, int]:
    """두 순서의 종합 판정이 같은 쪽을 고른 쌍 수 / 판정이 끝난 쌍 수."""
    same = total = 0
    for pair in pairs:
        records = [judged.get((pair.key, o)) for o in ORDERS]
        if None in records:
            continue
        total += 1
        sides = [to_side(r.output.overall, r.order) for r in records]
        same += sides[0] == sides[1]
    return same, total


def _median(values: list[float]) -> float:
    return statistics.median(values) if values else 0


def diagnostics(records: list[RunRecord], tasks: dict[str, Task]) -> list[str]:
    """조건별 진단 지표. 호출 금지 과제는 mcp만 돌렸으므로 비교를 위해 뺀다."""
    lines = [
        "| 조건 | 실행 | 답변 길이 중앙값 | 턴 중앙값 | 시간 중앙값 | 비용 합계 | "
        "techblog 호출 | search 횟수 중앙값 | get_details까지 | 웹 검색 | 원문 가져오기 |",
        "| --- |" + " --- |" * 10,
    ]
    by_condition: dict[str, list[RunRecord]] = defaultdict(list)
    for r in records:
        if tasks[r.task_id].category != "no_call":
            by_condition[r.condition].append(r)
    for condition in ("mcp", "none", "web", "web-ask"):
        runs = by_condition.get(condition, [])
        if not runs:
            continue
        names = [[c.name for c in r.tool_calls] for r in runs]
        n = len(runs)
        lines.append(
            f"| {condition} | {n} | {_median([len(r.answer) for r in runs]):.0f}자 "
            f"| {_median([r.num_turns or 0 for r in runs]):.0f} "
            f"| {_median([(r.duration_ms or 0) / 1000 for r in runs]):.0f}초 "
            f"| ${sum(r.cost_usd or 0 for r in runs):.1f} "
            f"| {sum(any(x in TECHBLOG_TOOLS for x in ns) for ns in names)}/{n} "
            f"| {_median([ns.count('search') for ns in names]):.0f} "
            f"| {sum('get_details' in ns for ns in names)}/{n} "
            f"| {sum('WebSearch' in ns for ns in names)}/{n} "
            f"| {sum('WebFetch' in ns for ns in names)}/{n} |"
        )
    return lines


def search_queries(records: list[RunRecord]) -> list[str]:
    """mcp 조건에서 에이전트가 만든 검색어의 모양 (M5 질의 재작성 안내의 효과 확인용)."""
    queries = [
        c.input for r in records if r.condition == "mcp" for c in r.tool_calls if c.name == "search"
    ]
    if not queries:
        return []
    lengths = [len(str(q.get("query", ""))) for q in queries]
    filters = Counter(
        k for q in queries for k in ("problem_type", "domain", "technologies") if q.get(k)
    )
    empty = sum(
        1
        for r in records
        if r.condition == "mcp"
        for c in r.tool_calls
        if c.name == "search" and c.result and "결과 없음" in c.result[:300]
    )
    n = len(queries)
    return [
        f"- 검색 {n}회, 검색어 길이 중앙값 {_median(lengths):.0f}자 (최대 {max(lengths)}자)",
        f"- 필터 사용: 문제 유형 {filters['problem_type']}회, 도메인 {filters['domain']}회, "
        f"기술 {filters['technologies']}회",
        f"- 결과 없음 {empty}회",
    ]


def call_rates(records: list[RunRecord], tasks: dict[str, Task]) -> list[str]:
    lines = ["| 분류 | 기대 | techblog 호출 |", "| --- | --- | --- |"]
    by: dict[str, list[RunRecord]] = defaultdict(list)
    for r in records:
        if r.condition == "mcp":
            by[tasks[r.task_id].category].append(r)
    for cat, runs in by.items():
        called = sum(any(c.name in TECHBLOG_TOOLS for c in r.tool_calls) for r in runs)
        expect = tasks[runs[0].task_id].expect_call
        lines.append(f"| {CATEGORY_NAMES.get(cat, cat)} | {expect} | {called}/{len(runs)} |")
    return lines


def judge_cost(judged: dict[tuple[str, str], JudgeRecord]) -> str:
    total = Usage()
    models = Counter()
    for r in judged.values():
        total.add(r.usage)
        models[f"{r.judge_model} {r.judge_effort}"] += 1
    price = load_pricing().get(next(iter(judged.values())).judge_model) if judged else None
    spent = f"${cost(total, price):.2f}" if price else "단가 없음"
    return f"판정 {len(judged)}회 ({', '.join(models)}), 비용 {spent}"


def build_report(
    records: list[RunRecord],
    tasks: list[Task],
    judged: dict[tuple[str, str], JudgeRecord],
    meta: dict,
) -> str:
    by_id = {t.id: t for t in tasks}
    pairs = build_pairs(tasks, records)
    results = _results(pairs, judged)
    same, total = order_consistency(pairs, judged)
    lines = [
        "# M7 에이전트 평가 결과",
        "",
        "같은 과제를 네 조건으로 풀게 하고, 같은 과제·같은 회차의 mcp 답변과",
        "다른 조건 답변을 나란히 놓고 질문한 개발자에게 어느 쪽이 더 도움이 되는지",
        "LLM으로 판정했다.",
        '채점 방향과 조건 정의는 docs/기획.md "에이전트 평가 (M7)".',
        "",
        f"- 에이전트: Claude Code {meta.get('claude_code_version', '?')}, "
        f"모델 {meta.get('model', '?')}, 조건별 {meta.get('reps', '?')}회",
        f"- 서버 커밋 {meta.get('git_commit', '?')[:7]}, "
        f"DB sha256 {meta.get('db_sha256', '?')[:12]}",
        f"- 과제 {len(tasks)}개, 실행 {len(records)}회, 비교 쌍 {len(results)}개",
        f"- {judge_cost(judged)}",
        f"- 순서 일관성: 두 순서의 종합 판정이 같은 쪽을 고른 쌍 {same}/{total}"
        f" ({same / (total or 1):.0%}). 엇갈린 쌍은 무승부로 셌다",
        "",
        "## 종합 판정",
        "",
        *overall_table(results),
        "",
        "## 기준별 판정 (MCP 승 / 무 / 패)",
        "",
        *criteria_table(results),
        "",
        "## 과제 분류별 종합 판정 (MCP 승 / 무 / 패)",
        "",
        *category_table(results),
        "",
        "## 진단: 조건별 실행",
        "",
        "호출 금지 과제(mcp만 실행)는 뺐다. 비용은 Claude Code가 표시한 값이다.",
        "",
        *diagnostics(records, by_id),
        "",
        "## 진단: mcp 조건의 호출",
        "",
        *call_rates(records, by_id),
        "",
        *search_queries(records),
        "",
        "## 한계",
        "",
        "- 판정은 채점기 하나(OpenAI)의 판단이다. 사람 검증은 하지 않았다 (사용자 결정)",
        "- mcp 답변은 출처를 스스로 밝히는 경우가 많아 채점기가 조건을 짐작할 수 있다",
        '- 채점 지시문의 "질문과 맞지 않는 사례로 핵심을 흐리면 낮게 본다"는 문장이',
        "  사례를 많이 든 답에 불리하게 작용했을 수 있다",
        "- 에이전트 모델은 sonnet 하나, 과제당 조건별 3회다",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--name", default="m7-sonnet", help="실행 묶음 이름 (eval/runs/agent/<name>)"
    )
    args = parser.parse_args()

    run_dir = RUNS_DIR / args.name
    records = [
        RunRecord.model_validate_json(line)
        for line in (run_dir / "records.jsonl").read_text(encoding="utf-8").splitlines()
        if line
    ]
    meta = json.loads((run_dir / "meta.json").read_text(encoding="utf-8"))
    report = build_report(records, load_tasks(), load_judgements(run_dir / JUDGE_FILE), meta)
    out = REPORTS / "m7-agent.md"
    out.write_text(report, encoding="utf-8", newline="\n")
    print(f"리포트 → {out}")


if __name__ == "__main__":
    main()
