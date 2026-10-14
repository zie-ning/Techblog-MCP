"""의미 검색 (M10): BM25 + 임베딩 후보를 리랭커로 정렬하고 2단 판정으로 거른다.

1. 검색어 임베딩(Voyage voyage-4-large)과 항목 임베딩의 코사인 상위 50건, BM25 상위 50건을
   RRF로 합쳐 후보 50건을 만든다
2. Voyage rerank-3로 후보마다 "검색어에 답이 되는 정도"를 0~1 점수로 매긴다
3. 1위 점수가 GATE 이상이면 결과 있음, 그때 점수가 ITEM_MIN 이상인 항목을 최대 10건 돌려준다

설정값과 근거는 docs/기획.md "검색", 실험은 docs/milestones/M10.md(eval/search_gate.py).
API 키(VOYAGE_API_KEY)가 없거나 호출이 실패하면 SemanticUnavailable을 던지고,
호출한 쪽(query.search)이 단어 일치 검색으로 대체한다.
"""

import os
import sqlite3
import threading
from collections.abc import Callable
from dataclasses import dataclass
from typing import Protocol

import httpx
import numpy as np

API_KEY_ENV = "VOYAGE_API_KEY"
API_URL = "https://api.voyageai.com/v1"
EMBEDDING_MODEL = "voyage-4-large"
RERANK_MODEL = "rerank-3"
CANDIDATES = 50  # 리랭커에 넘기는 후보 수 (BM25·임베딩 각 상위 50건을 RRF로 합친 상위)
RRF_K = 60
# 2단 판정 기준선 (M10 4단계 사용자 결정). 1위 점수가 GATE 미만이면 "결과 없음"이다.
# GATE는 DB에 없는 주제에서 1위로 올라오는 "비슷하지만 다른 글"을 거르는 값이라 높고,
# ITEM_MIN은 결과가 있을 때 무관한 꼬리만 자르는 값이라 낮다 (정답 항목의 48%가 GATE 미만)
GATE = 0.654
ITEM_MIN = 0.50
# 초. 호출 하나가 이보다 늦으면 단어 일치 검색으로 대체한다. 정상 응답은 1~2초인데 드물게
# 수십 초 멈추는 호출이 있었다(M10 R5 최대 33초)
TIMEOUT = 8.0


class SemanticUnavailable(Exception):
    """의미 검색을 쓸 수 없다. 메시지는 결과에 붙이는 대체 이유다."""


class Client(Protocol):
    def embed_query(self, text: str) -> np.ndarray: ...
    def rerank(self, query: str, documents: list[str]) -> list[float]: ...


def entry_text(entry: dict) -> str:
    """항목 임베딩·리랭커 입력: 제목 + 요약 필드 + 기술 (M5·M10 실험과 같은 텍스트).

    발췌(evidence)는 요약과 뜻이 같아 넣지 않는다. 파이프라인(pipeline.embed)과 서버가 이 함수
    하나를 같이 써야 항목 임베딩과 리랭커가 같은 텍스트를 본다.
    """

    def texts(points: list[dict]) -> str:
        return " ".join(p["text"] for p in points)

    parts = [entry["post_title"]]
    if entry["problem_situation"]:
        parts.append(f"문제: {texts(entry['problem_situation'])}")
    parts.append(f"해결: {texts(entry['solution'])}")
    if entry["performance_ops"]:
        parts.append(f"성능·운영: {texts(entry['performance_ops'])}")
    if entry["technologies"]:
        parts.append(f"기술: {', '.join(entry['technologies'])}")
    return "\n".join(parts)


def normalize(vectors: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(vectors, axis=-1, keepdims=True)
    return vectors / np.where(norms == 0, 1, norms)


class VoyageClient:
    def __init__(self, api_key: str, timeout: float = TIMEOUT):
        self._headers = {"Authorization": f"Bearer {api_key}"}
        self._timeout = timeout

    def _post(self, path: str, body: dict) -> dict:
        try:
            response = httpx.post(
                f"{API_URL}/{path}", headers=self._headers, json=body, timeout=self._timeout
            )
        except httpx.HTTPError as e:
            reason = f"Voyage API에 연결하지 못했습니다({type(e).__name__})"
            raise SemanticUnavailable(reason) from e
        if response.status_code != 200:
            reason = f"Voyage API가 오류를 돌려줬습니다(HTTP {response.status_code})"
            raise SemanticUnavailable(reason)
        return response.json()

    def embed(self, texts: list[str], input_type: str) -> np.ndarray:
        """input_type: 검색어는 query, 항목은 document. 길이 1로 맞춘 float32 벡터."""
        data = self._post(
            "embeddings", {"model": EMBEDDING_MODEL, "input": texts, "input_type": input_type}
        )
        rows = sorted(data["data"], key=lambda d: d["index"])
        return normalize(np.asarray([r["embedding"] for r in rows], dtype=np.float32))

    def embed_query(self, text: str) -> np.ndarray:
        return self.embed([text], "query")[0]

    def rerank(self, query: str, documents: list[str]) -> list[float]:
        data = self._post("rerank", {"model": RERANK_MODEL, "query": query, "documents": documents})
        scores = [0.0] * len(documents)
        for r in data["data"]:
            scores[r["index"]] = r["relevance_score"]
        return scores


def client_from_env() -> VoyageClient | None:
    key = os.environ.get(API_KEY_ENV, "").strip()
    return VoyageClient(key) if key else None


@dataclass(frozen=True)
class EntryVectors:
    rowids: np.ndarray  # entries.rowid
    matrix: np.ndarray  # (항목 수, 차원) float32, 길이 1


_vectors: dict[tuple[str, str], EntryVectors | None] = {}
_vectors_lock = threading.Lock()


def load_vectors(conn: sqlite3.Connection) -> EntryVectors | None:
    """DB의 항목 임베딩. 임베딩이 없거나 모델이 다르면 None (의미 검색을 쓸 수 없음).

    DB 파일과 빌드 시각별로 한 번만 읽는다(항목 1,315개 × 1024차원 약 5MB).
    """
    path = conn.execute("PRAGMA database_list").fetchone()[2]
    meta = dict(conn.execute("SELECT key, value FROM meta").fetchall())
    key = (path, meta.get("built_at", ""))
    with _vectors_lock:
        if key not in _vectors:
            _vectors[key] = _read_vectors(conn, meta)
        return _vectors[key]


def _read_vectors(conn: sqlite3.Connection, meta: dict[str, str]) -> EntryVectors | None:
    if meta.get("embedding_model") != EMBEDDING_MODEL:
        return None
    rows = conn.execute("SELECT rowid, vector FROM entry_embeddings ORDER BY rowid").fetchall()
    if not rows:
        return None
    rowids = np.array([r[0] for r in rows])
    matrix = np.vstack([np.frombuffer(r[1], dtype=np.float32) for r in rows])
    return EntryVectors(rowids, matrix)


def _rrf(lists: list[list[int]]) -> list[int]:
    """순위 목록들을 RRF로 합친다. 점수가 같으면 먼저 나온 목록(BM25)의 순서를 따른다."""
    score: dict[int, float] = {}
    for ranked in lists:
        for rank, rowid in enumerate(ranked, start=1):
            score[rowid] = score.get(rowid, 0.0) + 1 / (RRF_K + rank)
    return sorted(score, key=lambda r: -score[r])


@dataclass
class Ranked:
    rowids: list[int]  # 판정을 넘은 항목, 리랭커 점수 순 (ITEM_MIN 이상 전부)
    top_score: float  # 1위 리랭커 점수 (결과 없음 판정 근거)


def rank(
    query: str,
    vectors: EntryVectors,
    lexical: list[int],
    allowed: set[int] | None,
    texts_of: Callable[[list[int]], list[str]],
    client: Client,
) -> Ranked:
    """lexical: 필터를 건 BM25 상위 rowid. allowed: 필터에 맞는 rowid (필터가 없으면 None)."""
    scores = vectors.matrix @ client.embed_query(query)
    order = np.argsort(-scores, kind="stable")
    semantic = []
    for n in order:
        rowid = int(vectors.rowids[n])
        if allowed is None or rowid in allowed:
            semantic.append(rowid)
            if len(semantic) == CANDIDATES:
                break
    candidates = _rrf([lexical[:CANDIDATES], semantic])[:CANDIDATES]
    if not candidates:
        return Ranked([], 0.0)
    relevance = client.rerank(query, texts_of(candidates))
    ranked = sorted(zip(candidates, relevance, strict=True), key=lambda p: -p[1])
    top = ranked[0][1]
    if top < GATE:
        return Ranked([], top)
    return Ranked([rowid for rowid, score in ranked if score >= ITEM_MIN], top)
