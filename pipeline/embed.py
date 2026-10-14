"""항목 임베딩: 의미 검색(M10)에 쓰는 항목별 벡터를 Voyage voyage-4-large로 만든다.

    uv run python -m pipeline.embed          # 새 항목·내용이 바뀐 항목만 계산
    uv run python -m pipeline.embed --dry-run

결과는 data/embeddings.npz(커밋)에 두고, build_index가 검색 DB의 entry_embeddings 테이블에 넣는다.
입력은 서버 리랭커와 같은 텍스트(sonbae.search.semantic.entry_text)다. 저장소에 두는 이유는
키 없이도 같은 검색 DB를 빌드하고, 바뀐 항목만 다시 계산하기 위함이다(M10 사용자 결정).
VOYAGE_API_KEY는 환경 변수나 저장소 루트의 `.env`로 설정한다.
"""

import argparse
import hashlib
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from dotenv import load_dotenv

from pipeline.extract.schema import Entry
from pipeline.extract.store import DATA_DIR, ENTRIES_PATH, Store
from sonbae.search import semantic

EMBEDDINGS_PATH = DATA_DIR / "embeddings.npz"
BATCH = 64  # 요청당 토큰 한도 안에 들도록 (항목당 평균 약 535토큰)
RETRIES = 6


def embedding_input(entry: Entry) -> str:
    return semantic.entry_text(entry.model_dump())


def _hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


@dataclass
class Embeddings:
    model: str
    vectors: dict[str, tuple[str, np.ndarray]]  # 항목 ID → (입력 해시, float32 벡터)


def load(path: Path = EMBEDDINGS_PATH) -> Embeddings:
    if not path.exists():
        return Embeddings(semantic.EMBEDDING_MODEL, {})
    data = np.load(path)
    vectors = {
        str(i): (str(h), v.astype(np.float32))
        for i, h, v in zip(data["ids"], data["hashes"], data["vectors"], strict=True)
    }
    return Embeddings(str(data["model"]), vectors)


def save(embeddings: Embeddings, path: Path = EMBEDDINGS_PATH) -> None:
    ids = sorted(embeddings.vectors)
    vectors = [embeddings.vectors[i][1] for i in ids]
    np.savez_compressed(
        path,
        model=np.array(embeddings.model),
        ids=np.array(ids, dtype=str),
        hashes=np.array([embeddings.vectors[i][0] for i in ids], dtype=str),
        vectors=np.vstack(vectors).astype(np.float32) if vectors else np.zeros((0, 0), np.float32),
    )


def outdated(entries: list[Entry], embeddings: Embeddings) -> list[Entry]:
    """임베딩이 없거나 입력이 바뀐 항목. 모델이 다르면 모두 다시 만든다."""
    if embeddings.model != semantic.EMBEDDING_MODEL:
        return list(entries)
    return [
        e
        for e in entries
        if (v := embeddings.vectors.get(e.id)) is None or v[0] != _hash(embedding_input(e))
    ]


def current(entries: list[Entry], embeddings: Embeddings) -> dict[str, np.ndarray]:
    """입력이 최신인 항목의 벡터 (build_index가 넣는 것)."""
    stale = {e.id for e in outdated(entries, embeddings)}
    return {e.id: embeddings.vectors[e.id][1] for e in entries if e.id not in stale}


def _embed_documents(client: semantic.VoyageClient, texts: list[str]) -> np.ndarray:
    for attempt in range(RETRIES):
        try:
            return client.embed(texts, "document")
        except semantic.SemanticUnavailable as e:
            if attempt == RETRIES - 1:
                raise
            print(f"재시도: {e}")
            time.sleep(10 * (attempt + 1))
    raise AssertionError("unreachable")


def run(entries: list[Entry], embeddings: Embeddings, client) -> int:
    """오래된 임베딩을 새로 만들고, 사라진 항목의 임베딩은 지운다. embeddings를 고쳐 쓴다."""
    if embeddings.model != semantic.EMBEDDING_MODEL:
        embeddings.vectors.clear()
        embeddings.model = semantic.EMBEDDING_MODEL
    for entry_id in set(embeddings.vectors) - {e.id for e in entries}:
        del embeddings.vectors[entry_id]
    todo = outdated(entries, embeddings)
    for start in range(0, len(todo), BATCH):
        batch = todo[start : start + BATCH]
        texts = [embedding_input(e) for e in batch]
        vectors = _embed_documents(client, texts)
        for entry, text, vector in zip(batch, texts, vectors, strict=True):
            embeddings.vectors[entry.id] = (_hash(text), vector)
    return len(todo)


def main() -> None:
    parser = argparse.ArgumentParser(description="항목 임베딩(의미 검색용)을 만든다.")
    parser.add_argument("--entries", type=Path, default=ENTRIES_PATH)
    parser.add_argument("--out", type=Path, default=EMBEDDINGS_PATH)
    parser.add_argument("--dry-run", action="store_true", help="만들 항목 수만 보여 준다")
    args = parser.parse_args()

    entries = Store(entries_path=args.entries).entries
    embeddings = load(args.out)
    todo = outdated(entries, embeddings)
    print(f"항목 {len(entries)}개 중 임베딩을 새로 만들 항목 {len(todo)}개")
    removed = set(embeddings.vectors) - {e.id for e in entries}
    if args.dry_run or not todo and not removed:
        return

    load_dotenv()
    key = os.environ.get(semantic.API_KEY_ENV, "").strip()
    if not key:
        sys.exit(f"{semantic.API_KEY_ENV}를 설정하세요 (환경 변수나 .env).")
    # 문서 64개 묶음은 검색어 하나보다 오래 걸려 대기 시간을 넉넉히 둔다
    client = semantic.VoyageClient(key, timeout=120)
    try:
        count = run(entries, embeddings, client)
    finally:
        save(embeddings, args.out)
    print(f"{args.out}에 저장했습니다. 새로 만든 항목 {count}개")


if __name__ == "__main__":
    sys.exit(main())
