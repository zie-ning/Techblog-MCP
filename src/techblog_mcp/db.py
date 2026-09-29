"""검색 DB 경로 로딩. DB 위치를 아는 곳은 여기 하나뿐이다.

MVP는 저장소의 `data/techblog.sqlite`(pipeline.build_index로 생성)를 쓴다.
나중에 GitHub Release에서 DB를 내려받는 방식으로 바꿀 때 이 모듈만 고친다.
"""

import os
import sqlite3
from pathlib import Path

from techblog_mcp.search.schema import SCHEMA_VERSION

DB_PATH_ENV = "TECHBLOG_MCP_DB"
DEFAULT_DB_PATH = Path(__file__).resolve().parents[2] / "data" / "techblog.sqlite"


class DatabaseNotFound(Exception):
    pass


def db_path() -> Path:
    return Path(os.environ.get(DB_PATH_ENV) or DEFAULT_DB_PATH)


def connect(path: Path | None = None) -> sqlite3.Connection:
    path = path or db_path()
    if not path.exists():
        raise DatabaseNotFound(
            f"검색 DB가 없습니다: {path}\n"
            "저장소 루트에서 `uv run python -m pipeline.build_index`로 만들거나 "
            f"{DB_PATH_ENV} 환경 변수로 경로를 지정하세요."
        )
    # 서버는 읽기만 한다
    conn = sqlite3.connect(f"{path.resolve().as_uri()}?mode=ro", uri=True, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    version = conn.execute("SELECT value FROM meta WHERE key = 'schema_version'").fetchone()
    if version is None or version[0] != SCHEMA_VERSION:
        conn.close()
        raise DatabaseNotFound(
            f"검색 DB 스키마 버전이 맞지 않습니다 "
            f"(DB {version and version[0]}, 서버 {SCHEMA_VERSION}). "
            "`uv run python -m pipeline.build_index`로 다시 만드세요."
        )
    return conn
