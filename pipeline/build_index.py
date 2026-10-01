"""검색 DB 빌드: data/entries.jsonl → SQLite FTS5.

    uv run python -m pipeline.build_index [--out 경로]

항목 텍스트를 서버와 같은 형태소 분석기(techblog_mcp.search.analyzer)로 분석해 색인한다.
DB는 빌드 산출물이라 git에 넣지 않는다.
"""

import argparse
import json
import sqlite3
from datetime import UTC, datetime
from pathlib import Path

from pipeline.extract.schema import Entry
from pipeline.extract.store import ENTRIES_PATH, Store
from techblog_mcp import db
from techblog_mcp.search import schema
from techblog_mcp.search.analyzer import analyze


def _join(*parts: object) -> str:
    return "\n".join(str(p) for p in parts if p)


def fts_fields(entry: Entry) -> dict[str, str]:
    """FTS 열별 원문 텍스트 (형태소 분석 전). 발췌(evidence)도 넣어 원문 표현으로도 찾히게 한다."""

    def points(items) -> str:
        return _join(*(f"{p.text}\n{p.evidence}" for p in items))

    fields = {
        "title": entry.post_title,
        "problem": points(entry.problem_situation),
        "solution": points(entry.solution),
        "ops": points(entry.performance_ops),
        "rejected": _join(*(f"{r.name} {r.reason}" for r in entry.rejected_alternatives)),
        "keywords": _join(
            " ".join(entry.technologies),
            " ".join(entry.technologies_raw),
            " ".join(entry.tags),
            entry.company,
            " ".join(entry.problem_types),
            " ".join(entry.domains),
        ),
    }
    assert fields.keys() == schema.FTS_COLUMNS.keys()
    return fields


def build(entries: list[Entry], out: Path) -> None:
    tmp = out.with_name(out.name + ".tmp")
    tmp.unlink(missing_ok=True)
    conn = sqlite3.connect(tmp)
    try:
        conn.executescript(schema.DDL)
        meta = {
            "schema_version": schema.SCHEMA_VERSION,
            "built_at": datetime.now(UTC).isoformat(timespec="seconds"),
            "entry_count": str(len(entries)),
        }
        conn.executemany("INSERT INTO meta VALUES (?, ?)", meta.items())
        for rowid, entry in enumerate(entries, start=1):
            _insert(conn, rowid, entry)
        conn.commit()
    finally:
        conn.close()
    # 서버가 읽는 도중 반쯤 만들어진 DB를 보지 않도록 다 만든 뒤 바꿔치기한다
    tmp.replace(out)


def _insert(conn: sqlite3.Connection, rowid: int, e: Entry) -> None:
    conn.execute(
        "INSERT INTO entries VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            rowid,
            e.id,
            int(bool(e.performance_ops)),
            e.company,
            e.post_url,
            e.published_at,
            json.dumps(e.model_dump(), ensure_ascii=False),
        ),
    )
    conn.executemany(
        "INSERT INTO entry_problem_types VALUES (?, ?)", [(e.id, t) for t in e.problem_types]
    )
    conn.executemany("INSERT INTO entry_domains VALUES (?, ?)", [(e.id, d) for d in e.domains])
    conn.executemany(
        "INSERT INTO entry_technologies VALUES (?, ?)", [(e.id, t) for t in e.technologies]
    )
    conn.executemany(
        "INSERT INTO entry_rejected_alternatives VALUES (?, ?, ?)",
        [(e.id, r.name, r.kind) for r in e.rejected_alternatives],
    )
    fields = fts_fields(e)
    columns = ", ".join(fields)
    placeholders = ", ".join("?" * len(fields))
    conn.execute(
        f"INSERT INTO entries_fts (rowid, {columns}) VALUES (?, {placeholders})",
        (rowid, *(analyze(v) for v in fields.values())),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="entries.jsonl로 검색 DB를 만든다.")
    parser.add_argument("--entries", type=Path, default=ENTRIES_PATH)
    parser.add_argument("--out", type=Path, default=db.DEFAULT_DB_PATH)
    args = parser.parse_args()

    entries = Store(entries_path=args.entries).entries
    args.out.parent.mkdir(parents=True, exist_ok=True)
    build(entries, args.out)
    print(f"{len(entries)}개 항목으로 {args.out}를 만들었습니다.")


if __name__ == "__main__":
    main()
