"""검색 DB 경로 로딩. DB 위치를 아는 곳은 여기 하나뿐이다.

DB는 다음 순서로 찾는다.
1. 환경 변수 `SONBAE_DB`로 지정한 경로
2. 저장소의 `data/techblog.sqlite` (개발용, pipeline.build_index로 생성)
3. GitHub Release에서 내려받아 사용자 캐시 폴더에 둔 DB (git 주소로 설치한 사용자)

캐시 DB는 최신 Release를 따라간다 (M8 결정, docs/기획.md "자동 갱신"). Release마다 DB와 함께
버전 정보 파일(`db_release.json`: 태그·sha256·크기·스키마 버전)을 올리고, 서버는 하루 한 번
`releases/latest/download/db_release.json`으로 최신 버전을 확인한다. 스키마가 맞는 새 버전이면
백그라운드로 받아 체크섬을 확인해 두고 다음 기동부터 쓴다. 한 세션 안에서는 DB가 바뀌지 않는다.
확인에 실패하면(오프라인 등) 받아 둔 DB를 그대로 쓰고, 받아 둔 DB가 없으면 패키지에 고정된
`db_release.json` 버전을 받는다. 이 파일은 `pipeline.release_db`가 만든다.
"""

import hashlib
import json
import os
import re
import sqlite3
import sys
import tempfile
import time
import urllib.request
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from pathlib import Path

from sonbae.search.schema import SCHEMA_VERSION

DB_PATH_ENV = "SONBAE_DB"
CACHE_DIR_ENV = "SONBAE_CACHE_DIR"
DEFAULT_DB_PATH = Path(__file__).resolve().parents[2] / "data" / "techblog.sqlite"
RELEASE_MANIFEST_PATH = Path(__file__).with_name("db_release.json")

REPO_URL = "https://github.com/zie-ning/sonbae"
ASSET_NAME = "techblog.sqlite"
MANIFEST_ASSET_NAME = RELEASE_MANIFEST_PATH.name  # Release에 함께 올리는 버전 정보 파일
STATE_FILE_NAME = "state.json"  # 캐시 폴더에 두는 마지막 확인 시각과 받아 둔 최신 버전
CHECK_INTERVAL_SECONDS = 24 * 60 * 60
CHECK_TIMEOUT = 10  # 초. 최신 버전 확인 요청의 대기 시간
DOWNLOAD_TIMEOUT = 30  # 초. 연결·읽기 각각의 대기 시간
CHUNK_SIZE = 1 << 16
STALE_DOWNLOAD_SECONDS = 600
KEEP_RECENT_VERSIONS = 3  # 새 버전을 받을 때 지우지 않고 남기는 최근 버전 수 (이슈 #22)


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
    return base / "sonbae"


def db_path() -> Path:
    if custom := os.environ.get(DB_PATH_ENV):
        return Path(custom)
    if DEFAULT_DB_PATH.exists():
        return DEFAULT_DB_PATH
    return cached_db()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()


def ensure_downloaded(
    release: Release | None = None, directory: Path | None = None, keep: Iterable[Path] = ()
) -> Path:
    """Release의 DB(기본은 고정 버전)를 캐시에 두고 경로를 돌려준다. 이미 있으면 내려받지 않는다.

    새로 받으면 `keep`(쓰고 있는 DB 등)을 뺀 다른 버전은 지운다.
    """
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
    _remove_old_versions(directory, keep={target, *keep})
    return target


def latest_manifest_url() -> str:
    return f"{REPO_URL}/releases/latest/download/{MANIFEST_ASSET_NAME}"


def fetch_latest_release() -> Release:
    """최신 Release의 버전 정보. GitHub API가 아니라 다운로드 주소라 요청 한도가 없다."""
    with urllib.request.urlopen(latest_manifest_url(), timeout=CHECK_TIMEOUT) as response:
        return Release(**json.loads(response.read()))


@dataclass
class _State:
    checked_at: float = 0.0
    current: Release | None = None  # 받아 둔 최신 버전 (다음 기동부터 쓸 DB)


def _load_state(directory: Path) -> _State:
    try:
        data = json.loads((directory / STATE_FILE_NAME).read_text(encoding="utf-8"))
        current = Release(**data["current"]) if data.get("current") else None
        return _State(float(data.get("checked_at", 0)), current)
    except (OSError, ValueError, TypeError, KeyError):
        return _State()  # 없거나 깨졌으면 처음부터 확인한다


def _save_state(directory: Path, state: _State) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    data = {
        "checked_at": state.checked_at,
        "current": asdict(state.current) if state.current else None,
    }
    fd, tmp_name = tempfile.mkstemp(prefix=".state-", suffix=".tmp", dir=directory)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp_name, directory / STATE_FILE_NAME)


def _compatible(release: Release | None) -> bool:
    return release is not None and release.schema_version == SCHEMA_VERSION


def _tag_key(tag: str) -> tuple[int, ...]:
    """`db-2026.10.12.2` → (2026, 10, 12, 2). 태그끼리 새 버전 순서로 비교한다."""
    return tuple(int(n) for n in re.findall(r"\d+", tag))


def cached_db(directory: Path | None = None) -> Path:
    """사용자 캐시의 DB 경로. 받아 둔 버전 중 가장 새 것을 쓰고, 없으면 내려받는다.

    받아 둔 최신 버전과 패키지에 고정된 버전 중 스키마가 맞는 새 것을 고른다(코드를 업데이트해
    고정 버전이 더 새로울 수 있다). 하나도 없으면(첫 실행) 최신 버전을 확인해 받고, 확인이나
    다운로드에 실패하면 고정 버전을 받는다.
    """
    directory = directory or cache_dir()
    pinned = load_release()
    state = _load_state(directory)
    candidates = [r for r in (state.current, pinned) if _compatible(r)]
    for release in sorted(candidates, key=lambda r: _tag_key(r.tag), reverse=True):
        target = directory / release.filename
        if target.exists() and file_sha256(target) == release.sha256:
            return target

    try:
        latest = fetch_latest_release()
    except (OSError, ValueError, TypeError):
        latest = None
    if _compatible(latest) and latest != pinned:
        try:
            path = ensure_downloaded(latest, directory)
        except DatabaseNotFound:
            pass  # 최신을 못 받으면 고정 버전으로 시작한다
        else:
            _save_state(directory, _State(time.time(), latest))
            return path
    path = ensure_downloaded(pinned, directory)
    if latest is not None:
        _save_state(directory, _State(time.time(), state.current))
    return path


def check_for_update(directory: Path | None = None, now: float | None = None) -> Release | None:
    """하루 한 번 최신 Release를 확인해, 새 버전이면 받아 두고 돌려준다. 다음 기동부터 쓴다.

    환경 변수나 저장소 DB를 쓰는 경우와 확인·다운로드 실패는 조용히 넘어간다(다음 기동에서
    다시 확인). 받는 동안 지금 쓰는 DB는 지우지 않는다.
    """
    if os.environ.get(DB_PATH_ENV) or DEFAULT_DB_PATH.exists():
        return None
    directory = directory or cache_dir()
    now = time.time() if now is None else now
    state = _load_state(directory)
    if now - state.checked_at < CHECK_INTERVAL_SECONDS:
        return None
    try:
        latest = fetch_latest_release()
    except (OSError, ValueError, TypeError):
        return None
    pinned = load_release()
    in_use = state.current or pinned
    if not _compatible(latest) or latest == in_use:
        _save_state(directory, _State(now, state.current))
        return None
    keep = {directory / r.filename for r in (state.current, pinned) if r is not None}
    try:
        ensure_downloaded(latest, directory, keep=keep)
    except DatabaseNotFound:
        return None
    _save_state(directory, _State(now, latest))
    return latest


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


def _remove_old_versions(directory: Path, keep: set[Path]) -> None:
    # 서버가 다운로드 도중 종료되면 임시 파일이 남는다.
    # 다른 프로세스가 받는 중일 수 있어 오래된 것만 지운다
    stale_before = time.time() - STALE_DOWNLOAD_SECONDS
    stale = [p for p in directory.glob(".download-*.tmp") if p.stat().st_mtime < stale_before]
    # 먼저 기동해 계속 켜져 있는 서버 프로세스는 받아 둔 최신보다 이전 버전을 쓰고 있을 수 있다
    # (새 DB는 다음 기동부터 쓰므로). 최근에 받은 버전 몇 개는 남겨 그 서버가 계속 열 수 있게 한다
    versions = sorted(directory.glob("techblog-*.sqlite"), key=lambda p: p.stat().st_mtime)
    keep = keep | set(versions[-KEEP_RECENT_VERSIONS:])
    for old in [*versions, *stale]:
        if old not in keep:
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
