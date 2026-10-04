"""검색 평가용 항목 임베딩: 계산, 캐시, 코사인 순위.

M5 하이브리드 검색 실험에서만 쓴다. OpenAI 임베딩(.env의 OPENAI_API_KEY)을 쓴다.
로컬 임베딩 모델(fastembed MiniLM)은 M5에서 재 본 뒤 도입하지 않기로 해 지웠다
(docs/기획.md "임베딩").
항목 임베딩은 eval/search/embeddings/(git 제외)에 캐시해 텍스트가 바뀐 항목만 다시 계산한다.
"""

import hashlib
import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / "eval" / "search" / "embeddings"


@dataclass(frozen=True)
class ModelSpec:
    key: str  # 캐시 파일·리포트에 쓰는 짧은 이름
    provider: str  # openai
    name: str  # 공급자의 모델 이름


# 사용자 키로 쓰는 선택 기능 후보 (docs/기획.md "임베딩")
MODELS: dict[str, ModelSpec] = {
    spec.key: spec
    for spec in [
        ModelSpec("openai-small", "openai", "text-embedding-3-small"),
        ModelSpec("openai-large", "openai", "text-embedding-3-large"),
    ]
}


def embedding_text(entry: dict) -> str:
    """항목에서 임베딩할 텍스트: 제목 + 요약 필드 + 기술 (M5 사용자 결정).

    발췌(evidence)는 요약과 뜻이 같고 작은 모델의 입력 길이 제한(512 토큰)을 넘기기 쉬워 뺀다.
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


def _hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


class Embedder(Protocol):
    def documents(self, texts: list[str]) -> np.ndarray: ...
    def queries(self, texts: list[str]) -> np.ndarray: ...


class OpenAIEmbedder:
    BATCH = 100

    def __init__(self, name: str):
        from dotenv import load_dotenv
        from openai import OpenAI

        load_dotenv(ROOT / ".env")
        self._client = OpenAI(max_retries=6)
        self._name = name
        self.tokens = 0  # 비용 확인용 누적 토큰

    def documents(self, texts: list[str]) -> np.ndarray:
        vectors = []
        for start in range(0, len(texts), self.BATCH):
            response = self._client.embeddings.create(
                model=self._name, input=texts[start : start + self.BATCH]
            )
            self.tokens += response.usage.total_tokens
            vectors.extend(d.embedding for d in response.data)
        return np.array(vectors)

    queries = documents  # OpenAI 임베딩은 검색어와 문서를 구분하지 않는다


def make_embedder(spec: ModelSpec) -> Embedder:
    return OpenAIEmbedder(spec.name)


def _normalize(vectors: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    return vectors / np.where(norms == 0, 1, norms)


class EmbeddingIndex:
    """한 모델의 항목 임베딩과 검색어 임베딩 캐시."""

    def __init__(self, spec: ModelSpec, cache_dir: Path = CACHE_DIR, embedder=None):
        self.spec = spec
        self._cache_dir = cache_dir
        self._embedder = embedder
        self.ids: list[str] = []
        self.vectors = np.zeros((0, 0))
        self._query_cache: dict[str, list[float]] = {}

    @property
    def embedder(self) -> Embedder:
        if self._embedder is None:
            self._embedder = make_embedder(self.spec)
        return self._embedder

    @property
    def _doc_path(self) -> Path:
        return self._cache_dir / f"{self.spec.key}.npz"

    @property
    def _query_path(self) -> Path:
        return self._cache_dir / f"{self.spec.key}.queries.json"

    def build(self, conn: sqlite3.Connection) -> int:
        """DB의 항목을 임베딩하고 새로 계산한 수를 돌려준다.

        캐시와 텍스트가 같은 항목은 다시 계산하지 않는다.
        """
        rows = conn.execute("SELECT id, data FROM entries ORDER BY rowid").fetchall()
        ids = [r[0] for r in rows]
        texts = [embedding_text(json.loads(r[1])) for r in rows]
        hashes = [_hash(t) for t in texts]

        cached: dict[str, np.ndarray] = {}
        if self._doc_path.exists():
            data = np.load(self._doc_path)
            for i, h, v in zip(data["ids"], data["hashes"], data["vectors"], strict=True):
                cached[f"{i}:{h}"] = v
        keys = [f"{i}:{h}" for i, h in zip(ids, hashes, strict=True)]
        todo = [n for n, key in enumerate(keys) if key not in cached]
        if todo:
            fresh = self.embedder.documents([texts[n] for n in todo])
            for n, vector in zip(todo, fresh, strict=True):
                cached[keys[n]] = vector

        self.ids = ids
        self.vectors = _normalize(np.array([cached[key] for key in keys]))
        self._cache_dir.mkdir(parents=True, exist_ok=True)
        np.savez(self._doc_path, ids=ids, hashes=hashes, vectors=self.vectors)
        if self._query_path.exists():
            self._query_cache = json.loads(self._query_path.read_text(encoding="utf-8"))
        return len(todo)

    def query_vector(self, text: str) -> np.ndarray:
        if text not in self._query_cache:
            self._query_cache[text] = self.embedder.queries([text])[0].tolist()
            self._query_path.write_text(json.dumps(self._query_cache), encoding="utf-8")
        return _normalize(np.array([self._query_cache[text]]))[0]

    def rank(self, text: str, allowed: set[str] | None, depth: int) -> list[tuple[str, float]]:
        """코사인 유사도 순 (항목 ID, 점수). allowed가 있으면 그 항목만 (필터 결과)."""
        scores = self.vectors @ self.query_vector(text)
        order = np.argsort(-scores)
        ranked = []
        for n in order:
            if allowed is None or self.ids[n] in allowed:
                ranked.append((self.ids[n], float(scores[n])))
                if len(ranked) == depth:
                    break
        return ranked
