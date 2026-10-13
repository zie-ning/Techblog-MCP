"""검색 DB 찾기와 GitHub Release 다운로드 테스트. 다운로드는 file:// 주소로 흉내 낸다."""

import shutil
from pathlib import Path

import pytest

from pipeline import release_db
from techblog_mcp import db
from techblog_mcp.search.schema import SCHEMA_VERSION


@pytest.fixture
def published(sample_db, tmp_path, monkeypatch) -> db.Release:
    """sample_db를 Release에 올린 것처럼 tmp_path 아래 file:// 주소에 둔다."""
    monkeypatch.setattr(db, "REPO_URL", (tmp_path / "repo").as_uri())
    release = release_db.make_release(sample_db, "db-test")
    asset = tmp_path / "repo" / "releases" / "download" / release.tag / db.ASSET_NAME
    asset.parent.mkdir(parents=True)
    shutil.copy(sample_db, asset)
    return release


def asset_path(release: db.Release, tmp_path: Path) -> Path:
    return tmp_path / "repo" / "releases" / "download" / release.tag / db.ASSET_NAME


def test_download_verifies_and_caches(published, tmp_path):
    cache = tmp_path / "cache"
    path = db.ensure_downloaded(published, cache)
    assert path == cache / published.filename
    db.connect(path).close()

    # 캐시에 있으면 다시 받지 않는다
    asset_path(published, tmp_path).unlink()
    assert db.ensure_downloaded(published, cache) == path
    assert [p.name for p in cache.iterdir()] == [published.filename]


def test_checksum_mismatch_rejected(published, tmp_path):
    wrong = db.Release(**{**published.__dict__, "sha256": "0" * 64})
    cache = tmp_path / "cache"
    with pytest.raises(db.DatabaseNotFound, match="체크섬"):
        db.ensure_downloaded(wrong, cache)
    assert list(cache.iterdir()) == []  # 깨진 파일이나 임시 파일을 남기지 않는다


def test_download_failure_reported(published, tmp_path):
    asset_path(published, tmp_path).unlink()
    with pytest.raises(db.DatabaseNotFound, match="내려받지 못했습니다"):
        db.ensure_downloaded(published, tmp_path / "cache")


def test_schema_mismatch_not_downloaded(published, tmp_path):
    old = db.Release(**{**published.__dict__, "schema_version": "0"})
    with pytest.raises(db.DatabaseNotFound, match="스키마 버전"):
        db.ensure_downloaded(old, tmp_path / "cache")
    assert not (tmp_path / "cache").exists()


def test_old_versions_removed(published, tmp_path):
    cache = tmp_path / "cache"
    cache.mkdir()
    (cache / "techblog-0123456789abcdef.sqlite").write_bytes(b"old")
    path = db.ensure_downloaded(published, cache)
    assert list(cache.iterdir()) == [path]


def test_corrupt_cache_downloaded_again(published, tmp_path):
    cache = tmp_path / "cache"
    cache.mkdir()
    (cache / published.filename).write_bytes(b"broken")
    path = db.ensure_downloaded(published, cache)
    assert db.file_sha256(path) == published.sha256


def test_manifest_round_trip(published, tmp_path):
    manifest = tmp_path / "db_release.json"
    release_db.write_manifest(published, manifest)
    assert db.load_release(manifest) == published
    assert db.load_release(tmp_path / "none.json") is None


def test_env_path_takes_priority(tmp_path, monkeypatch):
    monkeypatch.setenv(db.DB_PATH_ENV, str(tmp_path / "custom.sqlite"))
    assert db.db_path() == tmp_path / "custom.sqlite"


def test_downloads_when_no_local_db(published, tmp_path, monkeypatch):
    monkeypatch.delenv(db.DB_PATH_ENV, raising=False)
    monkeypatch.setattr(db, "DEFAULT_DB_PATH", tmp_path / "none.sqlite")
    monkeypatch.setattr(db, "load_release", lambda: published)
    monkeypatch.setenv(db.CACHE_DIR_ENV, str(tmp_path / "cache"))
    assert db.db_path() == tmp_path / "cache" / published.filename


def test_shipped_manifest_matches_schema():
    # 스키마를 바꾸면 새 DB를 배포하고 db_release.json을 갱신해야 설치 사용자가 쓸 수 있다
    release = db.load_release()
    assert release is not None, "pipeline.release_db --upload로 DB를 배포하세요"
    assert release.schema_version == SCHEMA_VERSION


def test_unique_tag_adds_suffix_when_released_same_day():
    existing = {"db-2026.10.12", "db-2026.10.12.2"}
    assert release_db.unique_tag("db-2026.10.13", existing.__contains__) == "db-2026.10.13"
    assert release_db.unique_tag("db-2026.10.12", existing.__contains__) == "db-2026.10.12.3"


# ---- 최신 Release 자동 확인 (M8) ----


@pytest.fixture
def newer(published, tmp_path) -> db.Release:
    """published보다 새 Release. 내용이 달라 체크섬이 다르다."""
    from conftest import SAMPLE_ENTRIES

    from pipeline.build_index import build

    path = tmp_path / "newer" / db.ASSET_NAME
    path.parent.mkdir()
    build(SAMPLE_ENTRIES[:2], path)
    release = release_db.make_release(path, "db-2026.10.19")
    asset = asset_path(release, tmp_path)
    asset.parent.mkdir(parents=True)
    shutil.copy(path, asset)
    return release


def mark_latest(release: db.Release, tmp_path: Path) -> None:
    """`releases/latest/download/db_release.json`이 이 Release를 가리키게 한다."""
    manifest = tmp_path / "repo" / "releases" / "latest" / "download" / db.MANIFEST_ASSET_NAME
    manifest.parent.mkdir(parents=True, exist_ok=True)
    release_db.write_manifest(release, manifest)


@pytest.fixture
def installed(published, tmp_path, monkeypatch) -> Path:
    """저장소 DB 없이 설치한 사용자 환경. 고정 버전은 published. 캐시 폴더를 돌려준다."""
    monkeypatch.delenv(db.DB_PATH_ENV, raising=False)
    monkeypatch.setattr(db, "DEFAULT_DB_PATH", tmp_path / "none.sqlite")
    monkeypatch.setattr(db, "load_release", lambda: published)
    cache = tmp_path / "cache"
    monkeypatch.setenv(db.CACHE_DIR_ENV, str(cache))
    return cache


def test_first_run_downloads_latest(installed, newer, tmp_path):
    mark_latest(newer, tmp_path)
    assert db.db_path() == installed / newer.filename
    # 첫 실행에서 이미 확인했으므로 백그라운드 확인은 하루 동안 다시 하지 않는다
    assert db.check_for_update() is None


def test_update_is_downloaded_for_next_start(installed, published, newer, tmp_path):
    assert db.db_path() == installed / published.filename  # 최신 정보가 없으면 고정 버전

    mark_latest(newer, tmp_path)
    assert db.check_for_update() == newer
    # 지금 쓰는 DB는 지우지 않고, 다음 기동부터 새 DB를 쓴다
    assert (installed / published.filename).exists()
    assert db.db_path() == installed / newer.filename


def test_update_checked_once_a_day(installed, published, newer, tmp_path):
    mark_latest(published, tmp_path)
    now = 1_000_000.0
    assert db.check_for_update(now=now) is None  # 이미 최신
    mark_latest(newer, tmp_path)
    assert db.check_for_update(now=now + 60 * 60) is None  # 하루가 안 지남
    assert db.check_for_update(now=now + db.CHECK_INTERVAL_SECONDS) == newer


def test_incompatible_latest_is_ignored(installed, published, newer, tmp_path):
    db.db_path()
    mark_latest(db.Release(**{**newer.__dict__, "schema_version": "999"}), tmp_path)
    assert db.check_for_update() is None
    assert db.db_path() == installed / published.filename


def test_offline_check_keeps_current_db(installed, published, tmp_path):
    db.db_path()
    assert db.check_for_update() is None  # 최신 정보를 받지 못함
    assert db.db_path() == installed / published.filename


def test_newer_pinned_version_wins_after_code_upgrade(installed, newer, tmp_path, monkeypatch):
    from conftest import SAMPLE_ENTRIES

    from pipeline.build_index import build

    mark_latest(newer, tmp_path)
    db.db_path()  # newer(db-2026.10.19)를 받아 둠
    # 코드를 업데이트해 고정 버전이 받아 둔 것보다 새로워진 경우 (이미 캐시에 있다고 둔다)
    path = tmp_path / "upgraded.sqlite"
    build(SAMPLE_ENTRIES[:1], path)
    upgraded = release_db.make_release(path, "db-2026.10.26")
    shutil.copy(path, installed / upgraded.filename)
    monkeypatch.setattr(db, "load_release", lambda: upgraded)
    assert db.db_path() == installed / upgraded.filename


def test_no_update_check_with_repo_or_env_db(tmp_path, monkeypatch, sample_db):
    monkeypatch.setenv(db.DB_PATH_ENV, str(sample_db))
    monkeypatch.setenv(db.CACHE_DIR_ENV, str(tmp_path / "cache"))
    assert db.check_for_update() is None
    assert not (tmp_path / "cache").exists()
