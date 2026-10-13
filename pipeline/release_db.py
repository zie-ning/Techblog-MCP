"""검색 DB를 GitHub Release로 배포하고 서버가 내려받을 버전(db_release.json)을 고정한다.

    uv run python -m pipeline.release_db             # 배포할 내용만 확인
    uv run python -m pipeline.release_db --upload    # Release 생성·업로드 후 db_release.json 갱신

업로드에는 GitHub CLI(`gh`) 로그인이 필요하다(Actions에서는 GH_TOKEN). 태그를 주지 않으면
`db-YYYY.MM.DD`를 쓰고, 같은 날 이미 배포했으면 `.2`, `.3`을 붙인다.
업로드가 끝난 뒤에만 db_release.json을 쓰므로 업로드에 실패해도 서버가 없는 파일을 받으려
하지 않는다. 갱신된 db_release.json은 커밋해야 설치 사용자에게 반영된다.
"""

import argparse
import dataclasses
import datetime
import json
import subprocess
from collections.abc import Callable
from pathlib import Path

from techblog_mcp import db
from techblog_mcp.search.schema import SCHEMA_VERSION


def make_release(path: Path, tag: str) -> db.Release:
    # 서버가 열 수 있는 DB인지(스키마 버전) 먼저 확인한다
    db.connect(path).close()
    return db.Release(
        tag=tag,
        sha256=db.file_sha256(path),
        size=path.stat().st_size,
        schema_version=SCHEMA_VERSION,
    )


def write_manifest(release: db.Release, path: Path = db.RELEASE_MANIFEST_PATH) -> None:
    text = json.dumps(dataclasses.asdict(release), ensure_ascii=False, indent=2)
    path.write_text(text + "\n", encoding="utf-8")


def tag_exists(tag: str) -> bool:
    result = subprocess.run(["gh", "release", "view", tag], capture_output=True)
    return result.returncode == 0


def unique_tag(base: str, exists: Callable[[str], bool] = tag_exists) -> str:
    """같은 이름의 Release가 있으면 `.2`, `.3`을 붙인다 (같은 날 다시 배포하는 경우)."""
    if not exists(base):
        return base
    n = 2
    while exists(f"{base}.{n}"):
        n += 1
    return f"{base}.{n}"


def upload(release: db.Release, path: Path) -> None:
    if path.name != db.ASSET_NAME:
        raise SystemExit(f"Release 파일 이름은 {db.ASSET_NAME}이어야 합니다: {path}")
    notes = (
        f"검색 DB (스키마 버전 {release.schema_version})\n\n"
        f"- sha256: `{release.sha256}`\n- 크기: {release.size:,} bytes"
    )
    subprocess.run(
        [
            "gh",
            "release",
            "create",
            release.tag,
            str(path),
            "--title",
            release.tag,
            "--notes",
            notes,
        ],
        check=True,
    )


def main() -> None:
    today = datetime.date.today().strftime("%Y.%m.%d")
    parser = argparse.ArgumentParser(description="검색 DB를 GitHub Release로 배포한다.")
    parser.add_argument("--db", type=Path, default=db.DEFAULT_DB_PATH)
    parser.add_argument("--tag", help=f"Release 태그 (기본 db-{today}, 이미 있으면 .2를 붙임)")
    parser.add_argument("--upload", action="store_true", help="Release를 만들고 파일을 올린다")
    args = parser.parse_args()

    tag = args.tag or f"db-{today}"
    if args.upload and not args.tag:
        tag = unique_tag(tag)
    release = make_release(args.db, tag)
    print(f"태그 {release.tag}, 스키마 {release.schema_version}, {release.size:,} bytes")
    print(f"sha256 {release.sha256}")
    if not args.upload:
        print("확인만 했습니다. 배포하려면 --upload를 붙이세요.")
        return
    upload(release, args.db)
    write_manifest(release)
    print(f"{db.RELEASE_MANIFEST_PATH}를 갱신했습니다. 커밋해야 사용자에게 반영됩니다.")


if __name__ == "__main__":
    main()
