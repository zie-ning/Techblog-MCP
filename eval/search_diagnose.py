"""M10 진단 R0: 현재 서버 search가 정답(관련 라벨)을 놓치는 이유를 나눈다.

    uv run python eval/search_diagnose.py     # 리포트: eval/reports/m10-r0-diagnosis.md

정답 항목마다 서버 결과(최대 10건)에 들었는지 보고, 빠졌으면 이유를 셋으로 나눈다.

- A: 검색어 토큰이 하나도 없어 BM25 후보에도 오르지 못함
- B: 후보에는 올랐지만 관련도 기준(IDF 일치 50%)에서 잘림
- C: 기준은 넘었지만 10위 밖

빠진 정답의 OpenAI large 임베딩 순위와, 기준에서 잘린 정답에 빠진 검색어 단위도 함께 적는다.
질문별 임베딩 1위 코사인으로 "결과 없음"을 가를 수 있는지도 본다. 설계는 docs/milestones/M10.md.
"""

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eval.search_embed import MODELS, EmbeddingIndex  # noqa: E402
from eval.search_eval import REPORTS, filtered_ids, load_queries  # noqa: E402
from techblog_mcp import db  # noqa: E402
from techblog_mcp.search import query as q  # noqa: E402
from techblog_mcp.search.schema import FTS_COLUMNS  # noqa: E402

REASONS = {
    "A": "검색어 토큰이 하나도 없음",
    "B": "IDF 일치 기준에서 잘림",
    "C": "기준 통과, 10위 밖",
}


def lexical_candidates(conn, x) -> dict[str, tuple[int, float, int]]:
    """항목 ID → (BM25 순위, IDF 일치 비율, rowid). 기준을 적용하기 전 후보 전체."""
    filters = x.filters()
    units = q.query_units(x.query)
    tokens = list(dict.fromkeys(t for u in units for t in u))
    where, params = filters.sql()
    weights = ", ".join(str(w) for w in FTS_COLUMNS.values())
    rows = conn.execute(
        "SELECT e.id, e.rowid FROM entries_fts f JOIN entries e ON e.rowid = f.rowid"
        f" WHERE entries_fts MATCH ? AND {where} ORDER BY bm25(entries_fts, {weights})",
        [" OR ".join(f'"{t}"' for t in tokens), *params],
    ).fetchall()
    coverage = q._idf_coverage(conn, q._without_filter_terms(units, filters))
    return {r[0]: (n, coverage(r[1]), r[1]) for n, r in enumerate(rows, start=1)}


def missing_units(conn, query: str, rowid: int) -> list[str]:
    """항목에 없는 검색어 단위 (대체 토큰은 '/'로 잇는다)."""
    out = []
    for unit in q.query_units(query):
        hit = any(
            conn.execute(
                "SELECT 1 FROM entries_fts WHERE entries_fts MATCH ? AND rowid = ?",
                [f'"{t}"', rowid],
            ).fetchone()
            for t in unit
        )
        if not hit:
            out.append("/".join(unit))
    return out


def main() -> None:
    conn = db.connect(ROOT / "data" / "techblog.sqlite")
    queries = load_queries()
    index = EmbeddingIndex(MODELS["openai-large"])
    index.build(conn)
    titles = {
        r[0]: json.loads(r[1])["post_title"] for r in conn.execute("SELECT id, data FROM entries")
    }

    counts: Counter[str] = Counter()
    found = 0
    emb_buckets: dict[str, Counter[str]] = {k: Counter() for k in REASONS}
    detail = [
        "## 빠진 정답",
        "",
        "| 질문 | 항목 | 이유 | BM25 순위 | IDF 일치 | 임베딩 순위 | 빠진 검색어 단위 | 제목 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    tops = []
    for x in queries:
        ranked = index.rank(x.query, filtered_ids(conn, x.filters()), len(index.ids))
        emb_rank = {entry_id: n for n, (entry_id, _) in enumerate(ranked, start=1)}
        tops.append((x, ranked[0][1]))
        if not x.relevant:
            continue
        served = {e["id"] for e in q.search(conn, x.query, x.filters()).entries}
        lexical = lexical_candidates(conn, x)
        for entry_id in sorted(x.relevant):
            if entry_id in served:
                found += 1
                continue
            if entry_id not in lexical:
                reason, lex = "A", None
            else:
                lex = lexical[entry_id]
                reason = "B" if lex[1] < q.MIN_IDF_COVERAGE else "C"
            counts[reason] += 1
            er = emb_rank.get(entry_id)
            bucket = "10위 안" if er and er <= 10 else "30위 안" if er and er <= 30 else "그 밖"
            emb_buckets[reason][bucket] += 1
            miss = ", ".join(missing_units(conn, x.query, lex[2])) if lex else "-"
            detail.append(
                f"| {x.id} | {entry_id} | {reason} | {lex[0] if lex else '-'}"
                f" | {f'{lex[1]:.2f}' if lex else '-'} | {er or '-'} | {miss}"
                f" | {titles[entry_id][:40]} |"
            )

    total = found + sum(counts.values())
    lines = [
        "# M10 R0: 현재 search가 정답을 놓치는 이유",
        "",
        "서버 search 결과(관련도 기준 적용, 최대 10건)에 정답(`관련` 라벨)이 들었는지 본다.",
        "임베딩 순위는 필터를 건 뒤 OpenAI text-embedding-3-large 코사인 순위다.",
        "",
        "| 결과 | 정답 수 | 비율 | 임베딩 10위 안 | 30위 안 | 그 밖 |",
        "| --- | --- | --- | --- | --- | --- |",
        f"| 서버 결과에 듦 | {found} | {found / total:.0%} | | | |",
    ]
    for k, name in REASONS.items():
        b = emb_buckets[k]
        lines.append(
            f"| {k}. {name} | {counts[k]} | {counts[k] / total:.0%}"
            f" | {b['10위 안']} | {b['30위 안']} | {b['그 밖']} |"
        )
    lines += [
        "",
        "## 질문별 임베딩 1위 코사인",
        "",
        "✅ 정답 있는 질문, ❌ 없는 주제 질문.",
        "둘이 섞이면 코사인 기준선 하나로 결과 없음을 가를 수 없다.",
        "",
        "| 질문 | 구분 | 1위 코사인 |",
        "| --- | --- | --- |",
    ]
    for x, top in sorted(tops, key=lambda t: -t[1]):
        mark = "❌" if x.source == "없는 주제" else "✅"
        lines.append(f"| {x.id} {x.query[:30]} | {mark} | {top:.3f} |")
    text = "\n".join(lines + [""] + detail) + "\n"
    REPORTS.mkdir(parents=True, exist_ok=True)
    path = REPORTS / "m10-r0-diagnosis.md"
    path.write_text(text, encoding="utf-8")
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
