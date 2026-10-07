import pytest

from eval.agent_tasks import Task, load_tasks, relevant_ids, validate
from eval.search_eval import EvalQuery


def _query(qid: str, labels: dict[str, str]) -> EvalQuery:
    return EvalQuery(
        id=qid,
        query="q",
        source="데이터",
        judged=list(labels),
        labels={k: {"grade": g, "reason": "r"} for k, g in labels.items()},
    )


def test_shipped_tasks_are_valid():
    tasks = load_tasks()
    assert 30 <= len(tasks) <= 40
    # 호출해야 하는 과제, 하지 말아야 하는 과제, 없는 주제를 모두 포함한다 (M7 넘어온 항목)
    categories = {t.category for t in tasks}
    assert {"design", "no_call", "absent"} <= categories


def test_relevant_ids_merges_refs_with_higher_grade():
    queries = {
        "a": _query("a", {"c1": "일부 관련", "c2": "관련", "c3": "무관"}),
        "b": _query("b", {"c1": "관련"}),
    }
    task = Task(
        id="t", category="design", prompt="p", expect_call="required", search_refs=["a", "b"]
    )
    assert relevant_ids(task, queries) == {"c1": "관련", "c2": "관련"}


def test_validate_reports_problems():
    queries = {"a": _query("a", {"c1": "관련"})}
    tasks = [
        Task(id="t1", category="no_call", prompt="p", expect_call="required"),
        Task(id="t1", category="design", prompt="p", expect_call="required", search_refs=["zz"]),
        Task(id="t3", category="absent", prompt="p", expect_call="optional", search_refs=["a"]),
    ]
    errors = validate(tasks, queries)
    assert any("expect_call은 forbidden" in e for e in errors)
    assert any("id 중복" in e for e in errors)
    assert any("없는 질의" in e for e in errors)
    assert any("'관련' 사례가 있음" in e for e in errors)


def test_load_tasks_raises_on_invalid(tmp_path):
    path = tmp_path / "tasks.toml"
    path.write_text(
        '[[tasks]]\nid = "t1"\ncategory = "design"\nprompt = "p"\nexpect_call = "optional"\n',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="expect_call"):
        load_tasks(path, queries=[])
