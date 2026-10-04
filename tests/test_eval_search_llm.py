import pytest

from eval import search_llm
from eval.search_eval import EvalQuery
from eval.search_experiments import (
    EXPANSION_COLUMN,
    Context,
    build_expanded,
    idf_coverage,
    multi_query_system,
)
from techblog_mcp import db


class FakeGenerate:
    """입력 텍스트를 그대로 검색어로 돌려준다. 호출 횟수를 센다."""

    def __init__(self):
        self.calls = 0

    def __call__(self, instructions, text, schema):
        self.calls += 1
        if schema is search_llm.Rewrite:
            return {"queries": text.split(" / ")}
        return {"queries": [text], "terms": ["Zero Trust"]}


@pytest.fixture
def conn(sample_db):
    connection = db.connect(sample_db)
    yield connection
    connection.close()


def test_generated_outputs_are_cached(tmp_path, monkeypatch):
    monkeypatch.setattr(search_llm, "CACHE_DIR", tmp_path)
    fake = FakeGenerate()
    assert search_llm.rewrites({"q1": "쿠폰 / 정산"}, generate=fake) == {"q1": ["쿠폰", "정산"]}
    search_llm.rewrites({"q1": "쿠폰 / 정산"}, generate=fake)
    assert fake.calls == 1  # 같은 입력은 캐시에서 읽는다
    search_llm.rewrites({"q1": "쿠폰"}, generate=fake)
    assert fake.calls == 2  # 입력이 바뀌면 다시 만든다
    out = search_llm.expansions({"case_0001": "본문"}, generate=fake)
    assert out["case_0001"].terms == ["Zero Trust"]


def test_expansion_column_is_searchable(conn, tmp_path):
    path = tmp_path / "expanded.sqlite"
    texts = {"case_0004": "제로트러스트 접근 제어"}
    build_expanded(conn, texts, path)
    expanded = db.connect(path)
    try:
        x = EvalQuery(id="q", query="제로트러스트", source="M1")
        assert Context(conn, [x]).bm25(x) == []  # 원래 DB에는 없는 단어
        ectx = Context(expanded, [x], expansion=texts)
        assert [e.id for e in ectx.bm25(x)] == ["case_0004"]
        assert [e.id for e in ectx.bm25(x, {EXPANSION_COLUMN: 0.5})] == ["case_0004"]
        # 관련도 기준도 확장 열 토큰을 일치로 센다
        assert [e.id for e in idf_coverage(0.5)(ectx, x, ectx.bm25(x))] == ["case_0004"]
    finally:
        expanded.close()


def test_multi_query_merges_subqueries(conn):
    x = EvalQuery(id="q", query="쿠폰 비관 락 카프카 정산", source="M1")
    ctx = Context(conn, [x])
    system = multi_query_system(ctx, "rw", {"q": ["비관 락", "카프카 정산"]}, False, None, "")
    ids = [e.id for e in system.rank(x)]
    # 하위 검색어 각각의 1위가 모두 앞쪽에 온다
    assert set(ids[:2]) == {"case_0001", "case_0003"}
    cut = multi_query_system(ctx, "rw", {"q": ["비관 락"]}, False, idf_coverage(0.5), "")
    assert [e.id for e in cut.rank(x)] == ["case_0001"]
