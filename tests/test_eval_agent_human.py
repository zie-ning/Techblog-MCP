from collections import Counter

from eval.agent_human import (
    build_sample,
    compare,
    human_side,
    page_items,
    render_page,
    sample_pairs,
)
from eval.agent_judge import (
    JUDGE_EFFORT,
    JUDGE_MODEL,
    JudgeOutput,
    JudgeRecord,
    Pair,
    input_hash,
    prompt_version,
)
from eval.agent_run import RunRecord
from eval.agent_tasks import Task
from pipeline.extract.schema import Usage


def _pair(tid: str, right: str, rep: int = 1) -> Pair:
    task = Task(id=tid, category="design", prompt=f"{tid} 질문", expect_call="required")

    def rec(condition: str) -> RunRecord:
        return RunRecord(
            key=f"{tid}__{condition}__r{rep}",
            task_id=tid,
            condition=condition,
            rep=rep,
            answer=f"{condition} 답변",
            result_subtype="success",
        )

    return Pair(task, rec("mcp"), rec(right))


def test_sample_pairs_balances_kinds_and_uses_each_task_once():
    pairs = [
        _pair(f"t{i:02d}", right, rep)
        for i in range(12)
        for right in ("none", "web", "web-ask")
        for rep in (1, 2)
    ]
    chosen = sample_pairs(pairs, 9, seed=1)
    assert Counter(p.right.condition for p in chosen) == {"none": 3, "web": 3, "web-ask": 3}
    assert len({p.task.id for p in chosen}) == 9
    assert [p.key for p in sample_pairs(pairs, 9, seed=1)] == [p.key for p in chosen]


def test_page_hides_conditions_and_pair_keys():
    items = build_sample([_pair("t01", "none"), _pair("t02", "web-ask")], seed=3)
    html = render_page(page_items(items))
    assert "t01__mcp" not in html and "left_is_a" not in html
    for it, view in zip(items, page_items(items), strict=True):
        mcp_text = view["a"] if it["left_is_a"] else view["b"]
        assert mcp_text == "mcp 답변"


def test_human_side():
    assert human_side("A", left_is_a=True) == "left"
    assert human_side("A", left_is_a=False) == "right"
    assert human_side("B", left_is_a=False) == "left"
    assert human_side("tie", left_is_a=True) == "tie"


def test_compare_counts_agreement_with_llm():
    pair = _pair("t01", "none")

    def judged(order: str, overall: str) -> JudgeRecord:
        base = {k: "tie" for k in ("accuracy", "practicality", "reasoning", "fit", "clarity")}
        return JudgeRecord(
            pair=pair.key,
            order=order,
            output=JudgeOutput(**base, overall=overall, reason="r"),
            judge_model=JUDGE_MODEL,
            judge_effort=JUDGE_EFFORT,
            prompt_version=prompt_version(),
            input_hash=input_hash(pair),
            usage=Usage(),
        )

    llm = {
        (pair.key, "left_first"): judged("left_first", "A"),
        (pair.key, "right_first"): judged("right_first", "B"),
    }
    items = [{"item": "q01", "pair": pair.key, "left_is_a": False}]
    rows = compare(items, {"q01": {"choice": "B"}}, llm, {pair.key: pair})
    assert "사람 left" in rows[0] and "LLM left" in rows[0]
    assert "일치 1쌍 (100%)" in rows[-2]
