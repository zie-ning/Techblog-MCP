"""항목 임베딩 단계(pipeline.embed) 테스트: 바뀐 항목만 다시 계산하고 색인에 넣는다."""

import numpy as np
from conftest import SAMPLE_ENTRIES, ev

from pipeline import embed
from pipeline.build_index import build
from sonbae import db
from sonbae.search import semantic


class FakeDocuments:
    """문서마다 길이 1인 2차원 벡터를 돌려주고, 받은 텍스트를 기록한다."""

    def __init__(self):
        self.calls: list[list[str]] = []

    def embed(self, texts: list[str], input_type: str) -> np.ndarray:
        assert input_type == "document"
        self.calls.append(texts)
        return semantic.normalize(np.array([[len(t), 1.0] for t in texts], dtype=np.float32))


def test_run_embeds_only_new_and_changed(tmp_path):
    stored = embed.Embeddings(semantic.EMBEDDING_MODEL, {})
    client = FakeDocuments()
    assert embed.run(SAMPLE_ENTRIES, stored, client) == len(SAMPLE_ENTRIES)
    assert embed.outdated(SAMPLE_ENTRIES, stored) == []

    changed = SAMPLE_ENTRIES[0].model_copy(update={"solution": [ev("Lua 스크립트로 차감")]})
    entries = [changed, *SAMPLE_ENTRIES[1:3]]  # case_0004는 사라짐
    assert embed.run(entries, stored, client) == 1
    assert client.calls[-1] == [embed.embedding_input(changed)]
    assert set(stored.vectors) == {e.id for e in entries}


def test_model_change_recomputes_everything():
    stored = embed.Embeddings("old-model", {})
    embed.run(SAMPLE_ENTRIES, stored, FakeDocuments())
    stored.model = "old-model"
    assert len(embed.outdated(SAMPLE_ENTRIES, stored)) == len(SAMPLE_ENTRIES)


def test_save_load_round_trip(tmp_path):
    path = tmp_path / "embeddings.npz"
    stored = embed.Embeddings(semantic.EMBEDDING_MODEL, {})
    embed.run(SAMPLE_ENTRIES, stored, FakeDocuments())
    embed.save(stored, path)
    loaded = embed.load(path)
    assert loaded.model == semantic.EMBEDDING_MODEL
    assert loaded.vectors.keys() == stored.vectors.keys()
    for key, (digest, vector) in stored.vectors.items():
        assert loaded.vectors[key][0] == digest
        assert np.allclose(loaded.vectors[key][1], vector)


def test_build_index_stores_current_vectors(tmp_path):
    stored = embed.Embeddings(semantic.EMBEDDING_MODEL, {})
    embed.run(SAMPLE_ENTRIES, stored, FakeDocuments())
    changed = SAMPLE_ENTRIES[0].model_copy(update={"post_title": "다른 제목"})
    entries = [changed, *SAMPLE_ENTRIES[1:]]
    vectors = embed.current(entries, stored)
    assert changed.id not in vectors  # 입력이 바뀐 항목은 오래된 벡터를 넣지 않는다

    path = tmp_path / "techblog.sqlite"
    build(entries, path, embeddings=vectors)
    conn = db.connect(path)
    loaded = semantic.load_vectors(conn)
    assert loaded is not None
    assert len(loaded.rowids) == len(entries) - 1
    assert np.allclose(np.linalg.norm(loaded.matrix, axis=1), 1.0)
    conn.close()
