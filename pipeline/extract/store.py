"""추출 결과 저장소: `data/posts.jsonl`(글별 기록)과 `data/entries.jsonl`(항목).

둘 다 git에 커밋한다. 원문 전체는 들어 있지 않다(요약과 짧은 발췌, 원문 링크만).
항목 ID(`case_0001`)는 한 번 붙으면 바뀌지 않는다. 글을 다시 추출하면 그 글의 옛 항목은 지우고
새 항목에 새 번호를 붙인다.
"""

import re
from pathlib import Path

from pipeline.extract.extractor import ExtractResult
from pipeline.extract.schema import Entry, PostRecord

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
POSTS_PATH = DATA_DIR / "posts.jsonl"
ENTRIES_PATH = DATA_DIR / "entries.jsonl"

_ID_PREFIX = "case_"


class Store:
    def __init__(self, posts_path: Path = POSTS_PATH, entries_path: Path = ENTRIES_PATH):
        self.posts_path = posts_path
        self.entries_path = entries_path
        self.posts: dict[str, PostRecord] = {
            p.url: p for p in _read(posts_path, PostRecord.model_validate_json)
        }
        self.entries: list[Entry] = _read(entries_path, Entry.model_validate_json)

    def record_for(self, url: str) -> PostRecord | None:
        return self.posts.get(url)

    def add(self, result: ExtractResult) -> list[str]:
        """추출 결과를 반영하고 새 항목 ID를 돌려준다. 파일 저장은 `save()`로 한다."""
        url = result.record.url
        self.entries = [e for e in self.entries if e.post_url != url]
        next_no = self._max_id_no() + 1
        ids = []
        for offset, entry in enumerate(result.entries):
            entry_id = f"{_ID_PREFIX}{next_no + offset:04d}"
            self.entries.append(entry.model_copy(update={"id": entry_id}))
            ids.append(entry_id)
        self.posts[url] = result.record.model_copy(update={"entry_ids": ids})
        return ids

    def save(self) -> None:
        posts = sorted(self.posts.values(), key=lambda p: (p.source, p.published_at, p.url))
        _write(self.posts_path, [p.model_dump_json() for p in posts])
        entries = sorted(self.entries, key=lambda e: e.id)
        _write(self.entries_path, [e.model_dump_json() for e in entries])

    def _max_id_no(self) -> int:
        # 지운 항목의 번호를 재사용하지 않도록 글 기록에 남은 ID까지 함께 본다
        ids = [e.id for e in self.entries] + [i for p in self.posts.values() for i in p.entry_ids]
        numbers = [int(m.group(1)) for i in ids if (m := re.fullmatch(r"case_(\d+)", i))]
        return max(numbers, default=0)


def _read(path: Path, parse):
    if not path.exists():
        return []
    return [parse(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(f"{line}\n" for line in lines), encoding="utf-8")
