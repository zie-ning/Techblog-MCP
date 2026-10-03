import pytest

from eval.search_eval import EvalQuery, Ranked
from eval.search_experiments import (
    Context,
    absolute,
    both,
    group_by_post,
    idf_coverage,
    match_ratio,
    query_tokens,
    rare_match,
    relative,
    rrf,
)
from techblog_mcp import db


@pytest.fixture
def ctx(sample_db):
    connection = db.connect(sample_db)
    x = EvalQuery(id="q", query="쿠폰 비관 락", source="M1")
    yield Context(connection, [x])
    connection.close()


def _ids(ranked: list[Ranked]) -> list[str]:
    return [e.id for e in ranked]


def test_query_tokens_match_server_expression():
    assert query_tokens("카프카 정산") == ["카프카", "정산", "kafka"]
    assert query_tokens("!!!") == []


def test_context_matches_full_bm25_and_tokens(ctx):
    x = ctx.queries[0]
    ranked = ctx.bm25(x)
    assert _ids(ranked)[0] == "case_0001"
    assert {"쿠폰", "비관", "락"} <= ctx.tokens["case_0001"]
    # 희소한 단어일수록 IDF가 크다 (정산은 1개 항목, 쿠폰은 2개 항목에 있음)
    assert ctx.idf("정산") > ctx.idf("쿠폰")


def test_score_cutoffs():
    ranked = [Ranked("a", 10), Ranked("b", 6), Ranked("c", 3)]
    x = EvalQuery(id="q", query="-", source="M1")
    assert _ids(relative(0.5)(None, x, ranked)) == ["a", "b"]
    assert _ids(absolute(5)(None, x, ranked)) == ["a", "b"]
    assert _ids(both(relative(0.5), absolute(7))(None, x, ranked)) == ["a"]
    assert relative(0.5)(None, x, []) == []


def test_token_cutoffs(ctx):
    x = ctx.queries[0]
    ranked = ctx.bm25(x)
    assert set(_ids(ranked)) == {"case_0001", "case_0002"}
    # case_0002는 흔한 단어 '쿠폰'만 맞는다
    assert _ids(match_ratio(0.9)(ctx, x, ranked)) == ["case_0001"]
    assert _ids(match_ratio(0.3)(ctx, x, ranked)) == ["case_0001", "case_0002"]
    assert _ids(idf_coverage(0.5)(ctx, x, ranked)) == ["case_0001"]
    # 희소 단어 기준: 문서 빈도 30% 이하인 단어(비관, 락)가 하나라도 맞아야 한다
    assert _ids(rare_match(0.3)(ctx, x, ranked)) == ["case_0001"]


def test_group_by_post_lifts_siblings(ctx):
    # case_0001·0002는 같은 글. 글 점수로 묶으면 0002가 다른 글의 0003보다 앞선다
    ranked = [Ranked("case_0001", 10), Ranked("case_0003", 8), Ranked("case_0002", 2)]
    assert _ids(group_by_post(ctx, ranked, "max")) == ["case_0001", "case_0002", "case_0003"]
    # sum2는 상위 2개 합이라 한 항목만 강한 글보다 여러 항목이 걸린 글이 앞설 수 있다
    ranked = [Ranked("case_0003", 10), Ranked("case_0001", 6), Ranked("case_0002", 5)]
    assert _ids(group_by_post(ctx, ranked, "sum2"))[0] == "case_0001"


def test_rrf_combines_ranks():
    a = [Ranked("x", 0), Ranked("y", 0), Ranked("z", 0)]
    b = [Ranked("y", 0), Ranked("w", 0)]
    assert _ids(rrf([a, b]))[0] == "y"  # 양쪽에 있는 항목이 앞선다
    assert set(_ids(rrf([a, b]))) == {"x", "y", "z", "w"}
