from eval.agent_judge import (
    JUDGE_EFFORT,
    JUDGE_MODEL,
    JudgeOutput,
    JudgeRecord,
    Pair,
    build_pairs,
    combine,
    input_hash,
    judge_message,
    pair_result,
    pending,
    prompt_version,
    summarize,
    to_side,
)
from eval.agent_run import RunRecord
from eval.agent_tasks import Task
from pipeline.extract.schema import Usage


def _task(tid: str, category: str = "design") -> Task:
    expect = {"no_call": "forbidden", "open": "optional"}.get(category, "required")
    return Task(id=tid, category=category, prompt=f"{tid} 질문", expect_call=expect)


def _record(
    tid: str, condition: str, rep: int, answer: str = "답", error: bool = False
) -> RunRecord:
    return RunRecord(
        key=f"{tid}__{condition}__r{rep}",
        task_id=tid,
        condition=condition,
        rep=rep,
        answer=answer,
        is_error=error,
        result_subtype="success",
    )


def _output(overall: str, **criteria: str) -> JudgeOutput:
    base = {name: "tie" for name in ("accuracy", "practicality", "reasoning", "fit", "clarity")}
    return JudgeOutput(**{**base, **criteria}, overall=overall, reason="이유")


def _judged(pair: Pair, order: str, output: JudgeOutput) -> JudgeRecord:
    return JudgeRecord(
        pair=pair.key,
        order=order,
        output=output,
        judge_model=JUDGE_MODEL,
        judge_effort=JUDGE_EFFORT,
        prompt_version=prompt_version(),
        input_hash=input_hash(pair),
        usage=Usage(),
    )


def test_build_pairs_matches_same_rep_and_skips_no_call_and_errors():
    tasks = [_task("t01"), _task("t25", "no_call")]
    records = [
        _record("t01", "mcp", 1),
        _record("t01", "none", 1),
        _record("t01", "web", 1, error=True),
        _record("t01", "web-ask", 1),
        _record("t01", "mcp", 2),
        _record("t25", "mcp", 1),
    ]
    keys = [p.key for p in build_pairs(tasks, records)]
    assert keys == ["t01__mcp-vs-none__r1", "t01__mcp-vs-web-ask__r1"]


def test_to_side_maps_letters_by_order():
    assert to_side("A", "left_first") == "left"
    assert to_side("A", "right_first") == "right"
    assert to_side("B", "right_first") == "left"
    assert to_side("tie", "left_first") == "tie"


def test_combine_counts_only_agreeing_orders():
    assert combine("left", "left") == "left"
    assert combine("left", "right") == "tie"
    assert combine("left", "tie") == "tie"


def test_pair_result_needs_both_orders_and_removes_position_bias():
    pair = Pair(_task("t01"), _record("t01", "mcp", 1), _record("t01", "none", 1))
    # 두 순서 모두 mcp 답을 고름: left_first에서 A, right_first에서 B
    agree = [
        _judged(pair, "left_first", _output("A", accuracy="A")),
        _judged(pair, "right_first", _output("B", accuracy="A")),
    ]
    result = pair_result(agree)
    assert result["overall"] == "left"
    assert result["accuracy"] == "tie"  # 두 순서 모두 첫 번째 답을 고름 = 순서 편향 → 무승부
    assert pair_result(agree[:1]) is None


def test_pending_skips_current_and_redoes_changed_answer():
    pair = Pair(_task("t01"), _record("t01", "mcp", 1), _record("t01", "none", 1))
    cached = {(pair.key, "left_first"): _judged(pair, "left_first", _output("A"))}
    assert [o for _, o in pending([pair], cached, JUDGE_MODEL, JUDGE_EFFORT)] == ["right_first"]

    changed = Pair(pair.task, pair.left, _record("t01", "none", 1, answer="바뀐 답"))
    assert len(pending([changed], cached, JUDGE_MODEL, JUDGE_EFFORT)) == 2
    assert len(pending([pair], cached, "other-model", JUDGE_EFFORT)) == 2


def test_judge_message_hides_conditions():
    message = judge_message(_task("t01"), "첫 답", "둘째 답")
    assert "mcp" not in message and "web" not in message
    assert message.index("첫 답") < message.index("둘째 답")


def test_summarize_counts_overall_from_mcp_side():
    pair = Pair(_task("t01"), _record("t01", "mcp", 1), _record("t01", "none", 1))
    judged = {
        (pair.key, "left_first"): _judged(pair, "left_first", _output("B")),
        (pair.key, "right_first"): _judged(pair, "right_first", _output("A")),
    }
    assert summarize([pair], judged) == ["mcp vs none: mcp 승 0 · 무 0 · 패 1 (쌍 1)"]
