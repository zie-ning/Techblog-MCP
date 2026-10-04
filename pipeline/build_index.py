"""검색 DB 빌드: data/entries.jsonl → SQLite FTS5.

    uv run python -m pipeline.build_index [--out 경로]

항목 텍스트와 문서 확장(data/expansions.jsonl, pipeline/expand.py)을 서버와 같은 형태소
분석기(techblog_mcp.search.analyzer)로 분석해 색인한다.
DB는 빌드 산출물이라 git에 넣지 않는다.
"""

import argparse
import json
import sqlite3
from datetime import UTC, datetime
from pathlib import Path

from pipeline import expand
from pipeline.extract.schema import Entry
from pipeline.extract.store import ENTRIES_PATH, Store
from techblog_mcp import db
from techblog_mcp.search import schema
from techblog_mcp.search.analyzer import analyze


def has_metrics(entry: Entry) -> bool:
    """성능·운영 포인트에 숫자가 있는 항목 (M5 결정: 정량 결과가 있는 사례를 구분하는 표시).

    "47초 → 1.3초"는 있고 "같은 질문의 반복이 줄었다"는 없다. 글에 수치가 없는 항목이
    절반 가까이라 모든 항목에 붙던 이전 표시(96%)보다 근거가 강한 사례를 가려 준다.
    """
    return any(any(c.isdigit() for c in p.text) for p in entry.performance_ops)


def _join(*parts: object) -> str:
    return "\n".join(str(p) for p in parts if p)


def fts_fields(entry: Entry, expansion: str = "") -> dict[str, str]:
    """FTS 열별 원문 텍스트 (형태소 분석 전). 발췌(evidence)도 넣어 원문 표현으로도 찾히게 한다.

    expansion은 그 항목의 문서 확장 텍스트(expand.expansion_text)다.
    """

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
        "expansion": expansion,
    }
    assert fields.keys() == schema.FTS_COLUMNS.keys()
    return fields


def build(entries: list[Entry], out: Path, expansions: dict[str, str] | None = None) -> None:
    """expansions: 항목 ID → 문서 확장 텍스트. 없는 항목은 확장 열이 빈다."""
    expansions = expansions or {}
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
            _insert(conn, rowid, entry, expansions.get(entry.id, ""))
        conn.commit()
    finally:
        conn.close()
    # 서버가 읽는 도중 반쯤 만들어진 DB를 보지 않도록 다 만든 뒤 바꿔치기한다
    tmp.replace(out)


def _insert(conn: sqlite3.Connection, rowid: int, e: Entry, expansion: str) -> None:
    conn.execute(
        "INSERT INTO entries VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            rowid,
            e.id,
            int(has_metrics(e)),
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
    fields = fts_fields(e, expansion)
    columns = ", ".join(fields)
    placeholders = ", ".join("?" * len(fields))
    conn.execute(
        f"INSERT INTO entries_fts (rowid, {columns}) VALUES (?, {placeholders})",
        (rowid, *(analyze(v) for v in fields.values())),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="entries.jsonl로 검색 DB를 만든다.")
    parser.add_argument("--entries", type=Path, default=ENTRIES_PATH)
    parser.add_argument("--expansions", type=Path, default=expand.EXPANSIONS_PATH)
    parser.add_argument("--out", type=Path, default=db.DEFAULT_DB_PATH)
    args = parser.parse_args()

    entries = Store(entries_path=args.entries).entries
    records = expand.load(args.expansions)
    missing = expand.outdated(entries, records)
    if missing:
        # 확장이 없거나 오래돼도 빌드는 한다. 그 항목은 다른 표현으로 찾히기 어려울 뿐이다
        print(f"경고: 확장이 없거나 오래된 항목 {len(missing)}개. pipeline.expand를 실행하세요.")
    texts = {i: expand.expansion_text(r) for i, r in records.items()}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    build(entries, args.out, texts)
    print(f"{len(entries)}개 항목으로 {args.out}를 만들었습니다.")


if __name__ == "__main__":
    main()
