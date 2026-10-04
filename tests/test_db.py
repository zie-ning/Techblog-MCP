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
