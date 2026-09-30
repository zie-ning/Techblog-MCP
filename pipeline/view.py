"""JSONL을 사람이 보기 좋은 JSON 배열로 변환한다 (보기 전용 산출물).

    uv run python -m pipeline.view                        # entries.jsonl, posts.jsonl 모두
    uv run python -m pipeline.view data/entries.jsonl     # 지정한 파일만

결과는 `data/.view/<이름>.pretty.json`에 쓰며 git에서 제외된다.
원본은 건드리지 않으므로 VS Code에서 이 파일을 열어 접고 펼치며 보면 된다.
"""

import argparse
import json
from pathlib import Path

from pipeline.extract.store import DATA_DIR, ENTRIES_PATH, POSTS_PATH

VIEW_DIR = DATA_DIR / ".view"


def convert(src: Path) -> Path:
    """`src`의 각 줄을 JSON으로 읽어 들여쓴 배열로 저장하고 결과 경로를 돌려준다."""
    records = [
        json.loads(line) for line in src.read_text(encoding="utf-8").splitlines() if line.strip()
    ]
    VIEW_DIR.mkdir(exist_ok=True)
    dst = VIEW_DIR / f"{src.stem}.pretty.json"
    dst.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return dst


def main() -> None:
    parser = argparse.ArgumentParser(description="JSONL을 보기 좋은 JSON으로 변환한다.")
    parser.add_argument("paths", nargs="*", type=Path, help="변환할 JSONL 파일 (생략 시 전체)")
    args = parser.parse_args()

    for src in args.paths or [ENTRIES_PATH, POSTS_PATH]:
        if not src.exists():
            print(f"건너뜀: {src} 없음")
            continue
        print(f"{src} → {convert(src)}")


if __name__ == "__main__":
    main()
