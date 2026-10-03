import numpy as np
import pytest

from eval.search_embed import MODELS, EmbeddingIndex, embedding_text
from eval.search_eval import EvalQuery, candidate_pool, embedding_system, pool_report, pool_systems
from techblog_mcp import db


class FakeEmbedder:
    """텍스트에 든 단어 수로 만드는 결정적 벡터. 호출 횟수를 센다."""

    WORDS = ["쿠폰", "kafka", "정산", "에이전트"]

    def __init__(self):
        self.calls = 0

    def _vector(self, text: str) -> list[float]:
        lowered = text.casefold()
        return [lowered.count(w) + 0.01 for w in self.WORDS]

    def documents(self, texts):
        self.calls += len(texts)
        return np.array([self._vector(t) for t in texts])

    queries = documents


@pytest.fixture
def conn(sample_db):
    connection = db.connect(sample_db)
    yield connection
    connection.close()


def test_embedding_text_uses_summaries_not_evidence():
    entry = {
        "post_title": "제목",
        "problem_situation": [{"text": "문제 요약", "evidence": "원문 발췌"}],
        "solution": [{"text": "해결 요약", "evidence": "원문 발췌"}],
        "performance_ops": [],
        "technologies": ["Redis"],
    }
    text = embedding_text(entry)
    assert "문제: 문제 요약" in text and "해결: 해결 요약" in text and "기술: Redis" in text
    assert "원문 발췌" not in text and "성능·운영" not in text


def test_index_caches_unchanged_entries(conn, tmp_path):
    fake = FakeEmbedder()
    index = EmbeddingIndex(MODELS["minilm"], cache_dir=tmp_path, embedder=fake)
    assert index.build(conn) == 4
    # 다시 만들면 캐시에서 읽어 새로 계산하지 않는다
    again = EmbeddingIndex(MODELS["minilm"], cache_dir=tmp_path, embedder=fake)
    assert again.build(conn) == 0
    assert fake.calls == 4
    np.testing.assert_allclose(np.linalg.norm(again.vectors, axis=1), 1.0)


def test_rank_and_query_cache(conn, tmp_path):
    fake = FakeEmbedder()
    index = EmbeddingIndex(MODELS["minilm"], cache_dir=tmp_path, embedder=fake)
    index.build(conn)
    ranked = index.rank("카프카 kafka 정산", None, depth=2)
    assert ranked[0][0] == "case_0003"
    assert len(ranked) == 2
    calls = fake.calls
    index.rank("카프카 kafka 정산", None, depth=2)
    assert fake.calls == calls  # 검색어 임베딩도 캐시한다
    # allowed로 필터 결과만 남긴다
    assert [i for i, _ in index.rank("kafka", {"case_0004"}, depth=5)] == ["case_0004"]


def test_embedding_system_applies_filters(conn, tmp_path):
    index = EmbeddingIndex(MODELS["minilm"], cache_dir=tmp_path, embedder=FakeEmbedder())
    index.build(conn)
    system = embedding_system(conn, index)
    x = EvalQuery(id="q", query="쿠폰", source="M1", domain="결제·금융")
    assert [r.id for r in system.rank(x)] == ["case_0003"]


def test_candidate_pool_also_searches_without_filters(conn, tmp_path):
    index = EmbeddingIndex(MODELS["minilm"], cache_dir=tmp_path, embedder=FakeEmbedder())
    index.build(conn)
    systems = pool_systems(conn, [index])
    x = EvalQuery(id="q", query="쿠폰 발급", source="M1", domain="결제·금융")
    found = candidate_pool(x, systems)
    # 필터에 걸리지 않는 쿠폰 글도 필터 없는 검색으로 후보에 들어온다
    assert "case_0001" in found
    assert any("(필터 없음)" in hit for hit in found["case_0001"])
    report = pool_report(conn, [x], systems)
    assert "## q [M1] 쿠폰 발급 (도메인 = 결제·금융)" in report
    assert "case_0001 [미판정]" in report
