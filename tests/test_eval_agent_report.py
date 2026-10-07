from eval.agent_judge import (
    JUDGE_EFFORT,
    JUDGE_MODEL,
    JudgeOutput,
    JudgeRecord,
    Pair,
    input_hash,
    prompt_version,
)
from eval.agent_report import build_report, order_consistency
from eval.agent_run import RunRecord, ToolCall
from eval.agent_tasks import Task
from pipeline.extract.schema import Usage

TASK = Task(id="t01", category="design", prompt="질문", expect_call="required")


def _record(condition: str, calls: list[str] = ()) -> RunRecord:
    return RunRecord(
        key=f"t01__{condition}__r1",
        task_id="t01",
        condition=condition,
        rep=1,
        answer=f"{condition} 답변",
        result_subtype="success",
        num_turns=2,
        duration_ms=1000,
        cost_usd=0.1,
        tool_calls=[
            ToolCall(id=f"c{i}", name=n, input={"query": "선착순 쿠폰"}, result="결과 1건")
            for i, n in enumerate(calls)
        ],
    )


def _judged(pair: Pair, order: str, overall: str) -> JudgeRecord:
    base = {k: "tie" for k in ("accuracy", "practicality", "reasoning", "fit", "clarity")}
    return JudgeRecord(
        pair=pair.key,
        order=order,
        output=JudgeOutput(**base, overall=overall, reason="r"),
        judge_model=JUDGE_MODEL,
        judge_effort=JUDGE_EFFORT,
        prompt_version=prompt_version(),
        input_hash=input_hash(pair),
        usage=Usage(input_tokens=1000, output_tokens=100),
    )


def test_build_report_counts_from_mcp_side():
    records = [_record("mcp", ["search", "get_details"]), _record("none"), _record("web-ask")]
    none_pair = Pair(TASK, records[0], records[1])
    ask_pair = Pair(TASK, records[0], records[2])
    judged = {
        # none 쌍: 두 순서 모두 none 답을 고름 → mcp 패
        (none_pair.key, "left_first"): _judged(none_pair, "left_first", "B"),
        (none_pair.key, "right_first"): _judged(none_pair, "right_first", "A"),
        # web-ask 쌍: 두 순서 모두 첫 번째 답을 고름 → 순서 편향, 무승부
        (ask_pair.key, "left_first"): _judged(ask_pair, "left_first", "A"),
        (ask_pair.key, "right_first"): _judged(ask_pair, "right_first", "A"),
    }
    report = build_report(records, [TASK], judged, {"git_commit": "abcdef0123"})
    assert "| mcp vs none | 1 | 0 / 0 / 1 | 0% / 100% |" in report
    assert "| mcp vs web-ask | 1 | 0 / 1 / 0 | 0% / 0% |" in report
    assert "| 설계 | 0 / 0 / 1 | 0 / 0 / 0 | 0 / 1 / 0 |" in report
    assert "같은 쪽을 고른 쌍 1/2 (50%)" in report
    assert "| 설계 | required | 1/1 |" in report
    assert "검색 1회, 검색어 길이 중앙값 6자" in report


def test_order_consistency_skips_unfinished_pairs():
    records = [_record("mcp"), _record("none")]
    pair = Pair(TASK, records[0], records[1])
    judged = {(pair.key, "left_first"): _judged(pair, "left_first", "A")}
    assert order_consistency([pair], judged) == (0, 0)
