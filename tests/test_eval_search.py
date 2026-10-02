import pytest

from eval.search_eval import (
    EvalQuery,
    Ranked,
    bm25_ranking,
    bm25_system,
    build_report,
    dedupe_posts,
    evaluate_query,
    load_queries,
    parse_weights,
    post_map,
    recall_at,
    reciprocal_rank,
    run,
    summarize,
)
from techblog_mcp import db
from techblog_mcp.search import query as q
from techblog_mcp.search.schema import FTS_COLUMNS


@pytest.fixture
def conn(sample_db):
    connection = db.connect(sample_db)
    yield connection
    connection.close()


def _query(**overrides) -> EvalQuery:
    base = dict(id="q01", query="선착순 쿠폰 동시성", source="M1")
    return EvalQuery.model_validate(base | overrides)


def test_recall_denominator_is_capped_at_k():
    relevant = {f"c{i}" for i in range(8)}
    # 정답이 8개여도 상위 5건이 모두 정답이면 1.0
    assert recall_at(["c0", "c1", "c2", "c3", "c4"], relevant, 5) == 1.0
    assert recall_at(["c0", "x", "c1"], {"c0", "c1", "c9"}, 5) == pytest.approx(2 / 3)


def test_reciprocal_rank():
    assert reciprocal_rank(["x", "y", "a"], {"a"}) == pytest.approx(1 / 3)
    assert reciprocal_rank(["x"], {"a"}) == 0.0


def test_dedupe_posts_keeps_first_rank():
    post_of = {"a1": "A", "a2": "A", "b1": "B"}
    assert dedupe_posts(["a1", "b1", "a2"], post_of) == ["A", "B"]


def test_load_queries_validates(tmp_path):
    path = tmp_path / "queries.toml"
    path.write_text(
        """
[[queries]]
id = "q01"
query = "선착순 쿠폰"
source = "M1"
judged = ["case_0001", "case_0003"]

[queries.labels]
case_0001 = { grade = "관련", reason = "선착순 쿠폰" }
""",
        encoding="utf-8",
    )
    (x,) = load_queries(path)
    assert x.relevant == {"case_0001"}
    assert x.grade("case_0003") == "무관"  # 판정했지만 라벨 없음
    assert x.grade("case_0004") is None  # 미판정

    with pytest.raises(ValueError, match="judged에 없는"):
        _query(labels={"case_0001": {"grade": "관련", "reason": "-"}})
    with pytest.raises(ValueError, match="없는 주제"):
        _query(
            source="없는 주제",
            judged=["case_0001"],
            labels={"case_0001": {"grade": "관련", "reason": "-"}},
        )


def test_bm25_ranking_matches_server_order(conn):
    ranked = bm25_ranking(conn, "선착순 쿠폰 동시성", q.Filters(), dict(FTS_COLUMNS))
    server = q.search(conn, "선착순 쿠폰 동시성", q.Filters(), 10)
    assert [r.id for r in ranked] == [e["id"] for e in server.entries]
    scores = [r.score for r in ranked]
    assert scores == sorted(scores, reverse=True)  # 클수록 관련 있게 부호를 바꿈
    # 필터도 서버와 같다
    filtered = bm25_ranking(conn, "적재", q.Filters(domain="결제·금융"), dict(FTS_COLUMNS))
    assert [r.id for r in filtered] == ["case_0003"]


def test_evaluate_query_item_and_post_metrics():
    post_of = {"a1": "A", "a2": "A", "b1": "B", "c1": "C"}
    x = _query(
        judged=["a1", "a2", "b1"],
        labels={
            "a2": {"grade": "관련", "reason": "-"},
            "b1": {"grade": "관련", "reason": "-"},
        },
    )
    ranked = [Ranked(i, 1.0) for i in ["a1", "a2", "c1", "b1"]]
    r = evaluate_query(x, ranked, post_of)
    assert r.rr == 0.5  # 항목 단위 첫 정답은 2위
    assert r.post_rr == 1.0  # 글 단위로는 A가 1위
    assert r.recall5 == 1.0
    assert r.grades == {"무관": 1, "관련": 2, "미판정": 1}


def test_summarize_absent_topics_and_noise():
    post_of = {"a": "A", "b": "B"}
    answerable = _query(judged=["a", "b"], labels={"a": {"grade": "관련", "reason": "-"}})
    absent_empty = _query(id="q02", source="없는 주제")
    absent_noisy = _query(id="q03", source="없는 주제", judged=["b"])
    results = [
        evaluate_query(answerable, [Ranked("a", 2), Ranked("b", 1)], post_of),
        evaluate_query(absent_empty, [], post_of),
        evaluate_query(absent_noisy, [Ranked("b", 1)], post_of),
    ]
    s = summarize(results)
    assert s.answerable == 1
    assert s.mrr == 1.0
    assert s.no_result_rate == 0.5
    assert s.noise_rate == pytest.approx(2 / 3)  # 판정된 결과 3건 중 무관 2건
    assert s.unjudged == 0


def test_run_and_report(conn):
    x = _query(judged=["case_0001"], labels={"case_0001": {"grade": "관련", "reason": "-"}})
    system = bm25_system(conn, "baseline")
    results = run(system, [x], post_map(conn))
    assert results[0].rr == 1.0
    report = build_report(system, results, {"entry_count": "4"}, "테스트")
    assert "| baseline | 1.000 | 1.000 |" in report
    assert "| q01 | M1 |" in report


def test_parse_weights():
    assert parse_weights("title=3, problem=2.5") == {"title": 3.0, "problem": 2.5}
    assert parse_weights(None) == {}
    with pytest.raises(ValueError, match="없는 열"):
        parse_weights("body=1")
