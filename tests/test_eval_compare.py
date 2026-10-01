from conftest import ev, make_entry
from test_eval_inspect import PRICE, _record

from eval.compare_runs import Run, build_report, kind_changes


def _run(name: str, kind: str, n_entries: int) -> Run:
    posts = [_record("1", kind, "https://e/1"), _record("2", "제외", "https://e/2")]
    entries = [
        make_entry(
            f"case_{i:04d}",
            source="kakao",
            post_url="https://e/1",
            problem_situation=[ev("문제")],
            solution=[ev("해결")],
        )
        for i in range(n_entries)
    ]
    return Run(name, posts, entries)


def test_compare_report_lists_metrics_and_changes():
    a, b = _run("a", "사례", 3), _run("b", "인사이트", 1)
    rows = kind_changes([a, b])
    assert rows == [["kakao/1", "사례 3개", "인사이트 1개", "제목 1"]]

    report = build_report([a, b], {"https://e/1": 5000, "https://e/2": 300}, {"m": PRICE})
    assert "| 인사이트 글 | 0 (0%) | 1 (50%) |" in report
    assert "구조화 유형·항목 수가 달라진 글 1편" in report


def test_kind_changes_ignores_posts_missing_from_a_run():
    a, b = _run("a", "사례", 1), _run("b", "사례", 1)
    b.posts = b.posts[:1]  # b에는 글 2가 없다
    assert kind_changes([a, b]) == []
