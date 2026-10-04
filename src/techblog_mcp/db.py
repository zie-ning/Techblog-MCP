"""검색 DB 경로 로딩. DB 위치를 아는 곳은 여기 하나뿐이다.

DB는 다음 순서로 찾는다.
1. 환경 변수 `TECHBLOG_MCP_DB`로 지정한 경로
2. 저장소의 `data/techblog.sqlite` (개발용, pipeline.build_index로 생성)
3. GitHub Release에서 내려받아 사용자 캐시 폴더에 둔 DB (`uvx` 설치 사용자)

내려받을 Release 태그와 체크섬은 `db_release.json`에 고정한다 (M6 결정). 같은 코드면 항상
같은 데이터를 쓰고, 받은 파일이 그 파일인지 체크섬으로 확인한다. 이 파일은
`pipeline.release_db`가 만든다.
"""

import hashlib
import json
import os
import sqlite3
import sys
import tempfile
import time
import urllib.request
from dataclasses import dataclass
from pathlib import Path

from techblog_mcp.search.schema import SCHEMA_VERSION

DB_PATH_ENV = "TECHBLOG_MCP_DB"
CACHE_DIR_ENV = "TECHBLOG_MCP_CACHE_DIR"
DEFAULT_DB_PATH = Path(__file__).resolve().parents[2] / "data" / "techblog.sqlite"
RELEASE_MANIFEST_PATH = Path(__file__).with_name("db_release.json")

REPO_URL = "https://github.com/zie-ning/Techblog-Search-MCP"
ASSET_NAME = "techblog.sqlite"
DOWNLOAD_TIMEOUT = 30  # 초. 연결·읽기 각각의 대기 시간
CHUNK_SIZE = 1 << 16
STALE_DOWNLOAD_SECONDS = 600


class DatabaseNotFound(Exception):
    pass


@dataclass(frozen=True)
class Release:
    tag: str
    sha256: str
    size: int
    schema_version: str

    @property
    def url(self) -> str:
        return f"{REPO_URL}/releases/download/{self.tag}/{ASSET_NAME}"

    @property
    def filename(self) -> str:
        # 버전마다 파일 이름이 달라 새 버전을 받는 동안 이전 파일을 덮어쓰지 않는다
        return f"techblog-{self.sha256[:16]}.sqlite"


def load_release(path: Path = RELEASE_MANIFEST_PATH) -> Release | None:
    if not path.exists():
        return None
    return Release(**json.loads(path.read_text(encoding="utf-8")))


def cache_dir() -> Path:
    if custom := os.environ.get(CACHE_DIR_ENV):
        return Path(custom)
    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA") or Path.home() / "AppData" / "Local")
    elif sys.platform == "darwin":
        base = Path.home() / "Library" / "Caches"
    else:
        base = Path(os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache")
    return base / "techblog-mcp"


def db_path() -> Path:
    if custom := os.environ.get(DB_PATH_ENV):
        return Path(custom)
    if DEFAULT_DB_PATH.exists():
        return DEFAULT_DB_PATH
    return ensure_downloaded()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()


def ensure_downloaded(release: Release | None = None, directory: Path | None = None) -> Path:
    """고정된 Release의 DB를 캐시에 두고 경로를 돌려준다. 이미 있으면 내려받지 않는다."""
    release = release or load_release()
    if release is None:
        raise DatabaseNotFound(
            "내려받을 검색 DB 정보(db_release.json)가 없습니다. "
            f"{DB_PATH_ENV} 환경 변수로 DB 경로를 지정하세요."
        )
    if release.schema_version != SCHEMA_VERSION:
        # 스키마를 바꾸고 새 DB를 배포하지 않은 경우. 받아도 열 수 없다
        raise DatabaseNotFound(
            f"배포된 검색 DB({release.tag})의 스키마 버전 {release.schema_version}이 "
            f"서버({SCHEMA_VERSION})와 맞지 않습니다."
        )
    directory = directory or cache_dir()
    target = directory / release.filename
    if target.exists() and file_sha256(target) == release.sha256:
        return target

    directory.mkdir(parents=True, exist_ok=True)
    _download(release, directory, target)
    _remove_old_versions(directory, keep=target)
    return target


def _download(release: Release, directory: Path, target: Path) -> None:
    # 같은 폴더의 임시 파일에 받은 뒤 검증하고 이름을 바꾼다. 중간에 끊겨도 깨진 DB가 남지 않는다
    fd, tmp_name = tempfile.mkstemp(prefix=".download-", suffix=".tmp", dir=directory)
    tmp = Path(tmp_name)
    try:
        digest = hashlib.sha256()
        with os.fdopen(fd, "wb") as out:
            try:
                with urllib.request.urlopen(release.url, timeout=DOWNLOAD_TIMEOUT) as response:
                    while chunk := response.read(CHUNK_SIZE):
                        digest.update(chunk)
                        out.write(chunk)
            except OSError as e:
                raise DatabaseNotFound(
                    f"검색 DB를 내려받지 못했습니다: {release.url}\n"
                    f"원인: {e}\n네트워크 연결을 확인하고 다시 시도하세요."
                ) from e
        if digest.hexdigest() != release.sha256:
            raise DatabaseNotFound(
                f"내려받은 검색 DB의 체크섬이 맞지 않습니다 ({release.url}). 다시 시도하세요."
            )
        try:
            os.replace(tmp, target)
        except PermissionError:
            # Windows에서 다른 서버 프로세스가 같은 파일을 먼저 받아 열고 있는 경우
            if not (target.exists() and file_sha256(target) == release.sha256):
                raise
    finally:
        tmp.unlink(missing_ok=True)


def _remove_old_versions(directory: Path, keep: Path) -> None:
    # 서버가 다운로드 도중 종료되면 임시 파일이 남는다.
    # 다른 프로세스가 받는 중일 수 있어 오래된 것만 지운다
    stale_before = time.time() - STALE_DOWNLOAD_SECONDS
    stale = [p for p in directory.glob(".download-*.tmp") if p.stat().st_mtime < stale_before]
    for old in [*directory.glob("techblog-*.sqlite"), *stale]:
        if old != keep:
            try:
                old.unlink()
            except OSError:
                pass  # 다른 서버 프로세스가 아직 쓰고 있으면 다음 기회에 지운다


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
