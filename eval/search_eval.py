"""검색 평가: 평가셋(eval/search/queries.toml)으로 검색 설정별 Recall·MRR 등을 잰다.

    uv run python eval/search_eval.py  # 현재 설정(기준선) → eval/reports/m5-baseline.md
    uv run python eval/search_eval.py --name w-title3 --weights title=3

평가셋 형식과 판정 기준은 eval/search/README.md.
서버 코드는 결정이 난 뒤에만 고치므로, 실험 설정(가중치 등)은 이 스크립트에서 바꿔 가며 잰다.
"""

import argparse
import json
import sqlite3
import sys
import tomllib
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, model_validator

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 techblog_mcp를 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from techblog_mcp import db  # noqa: E402
from techblog_mcp.search import query as q  # noqa: E402
from techblog_mcp.search.schema import FTS_COLUMNS  # noqa: E402

QUERIES_PATH = ROOT / "eval" / "search" / "queries.toml"
REPORTS = ROOT / "eval" / "reports"
MAX_RESULTS = 10  # 서버가 돌려줄 최대 건수 (docs/기획.md "결과 수 결정")
DEPTH = 50  # 순위를 볼 깊이. 관련도 기준이 없는 설정은 상위 MAX_RESULTS건을 결과로 본다

Grade = Literal["관련", "일부 관련", "무관"]
Source = Literal["M1", "데이터", "없는 주제"]


# ---------- 평가셋 ----------


class Label(BaseModel):
    grade: Grade
    reason: str


class EvalQuery(BaseModel):
    id: str
    query: str
    source: Source
    note: str = ""
    problem_type: str | None = None
    domain: str | None = None
    technologies: list[str] = []
    # 판정한 후보 전체. 여기 있고 labels에 없으면 무관, 여기 없으면 미판정
    judged: list[str] = []
    labels: dict[str, Label] = {}

    @model_validator(mode="after")
    def _labels_are_judged(self) -> "EvalQuery":
        missing = set(self.labels) - set(self.judged)
        if missing:
            raise ValueError(f"{self.id}: judged에 없는 라벨 {sorted(missing)}")
        if self.source == "없는 주제" and self.relevant:
            raise ValueError(f"{self.id}: 없는 주제 질문에 '관련' 라벨이 있습니다")
        return self

    @property
    def relevant(self) -> set[str]:
        return {i for i, label in self.labels.items() if label.grade == "관련"}

    @property
    def partial(self) -> set[str]:
        return {i for i, label in self.labels.items() if label.grade == "일부 관련"}

    def grade(self, entry_id: str) -> Grade | None:
        """None이면 미판정."""
        if entry_id in self.labels:
            return self.labels[entry_id].grade
        return "무관" if entry_id in self.judged else None

    def filters(self) -> q.Filters:
        return q.Filters(
            problem_type=self.problem_type,
            domain=self.domain,
            technologies=q.resolve_technologies(self.technologies).normalized,
        )


def load_queries(path: Path = QUERIES_PATH) -> list[EvalQuery]:
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    queries = [EvalQuery.model_validate(item) for item in data.get("queries", [])]
    ids = [x.id for x in queries]
    if len(ids) != len(set(ids)):
        raise ValueError("질문 ID가 중복됩니다")
    return queries


# ---------- 검색 설정 ----------


@dataclass
class Ranked:
    id: str
    score: float


@dataclass
class System:
    """검색 설정 하나. rank는 질문 → 순위 목록.

    cutoff가 있으면 관련도 기준을 통과한 것만 돌려준다.
    """

    name: str
    rank: Callable[[EvalQuery], list[Ranked]]
    cutoff: bool = False
    description: str = ""


def bm25_ranking(
    conn: sqlite3.Connection,
    query: str,
    filters: q.Filters,
    weights: dict[str, float],
    depth: int = DEPTH,
) -> list[Ranked]:
    """서버 검색(query.search)과 같은 MATCH 식·필터로 bm25 점수까지 돌려준다.

    bm25()는 낮을수록(더 음수일수록) 관련도가 높다. 여기서는 부호를 바꿔 클수록 관련 있게 한다.
    """
    match = q._match_expression(query)
    if match is None:
        return []
    where, params = filters.sql()
    args = ", ".join(str(weights[c]) for c in FTS_COLUMNS)
    rows = conn.execute(
        f"SELECT e.id, bm25(entries_fts, {args}) AS score"
        " FROM entries_fts f JOIN entries e ON e.rowid = f.rowid"
        f" WHERE entries_fts MATCH ? AND {where} ORDER BY score LIMIT ?",
        [match, *params, depth],
    ).fetchall()
    return [Ranked(r[0], -r[1]) for r in rows]


def bm25_system(
    conn: sqlite3.Connection, name: str, weights: dict[str, float] | None = None
) -> System:
    weights = {**FTS_COLUMNS, **(weights or {})}
    desc = ", ".join(f"{c}={w:g}" for c, w in weights.items())
    return System(
        name,
        lambda x: bm25_ranking(conn, x.query, x.filters(), weights),
        description=f"BM25 가중치 {desc}",
    )


def filtered_ids(conn: sqlite3.Connection, filters: q.Filters) -> set[str] | None:
    """필터에 맞는 항목 ID. 필터가 없으면 None(전체)."""
    if not filters.describe():
        return None
    where, params = filters.sql()
    return {r[0] for r in conn.execute(f"SELECT e.id FROM entries e WHERE {where}", params)}


def embedding_system(conn: sqlite3.Connection, index) -> System:
    """임베딩 코사인 순위. index는 search_embed.EmbeddingIndex (build를 마친 것)."""
    return System(
        f"emb-{index.spec.key}",
        lambda x: [
            Ranked(i, s) for i, s in index.rank(x.query, filtered_ids(conn, x.filters()), DEPTH)
        ],
        description=f"임베딩 {index.spec.name} (코사인)",
    )


# ---------- 지표 ----------


def dedupe_posts(ids: list[str], post_of: dict[str, str]) -> list[str]:
    """순위 목록을 글 단위로 바꾼다. 같은 글은 처음 나온 순위 하나로 본다."""
    return list(dict.fromkeys(post_of[i] for i in ids))


def recall_at(ranked: list[str], relevant: set[str], k: int) -> float:
    """분모는 min(정답 수, k): 정답이 k개보다 많은 넓은 주제도 상위 k건이 모두 정답이면 1.0."""
    hits = len(set(ranked[:k]) & relevant)
    return hits / min(len(relevant), k)


def reciprocal_rank(ranked: list[str], relevant: set[str]) -> float:
    for rank, item in enumerate(ranked, start=1):
        if item in relevant:
            return 1 / rank
    return 0.0


@dataclass
class QueryResult:
    query: EvalQuery
    returned: list[str]  # 결과로 보여 줄 항목 (최대 MAX_RESULTS건, 관련도 기준 적용 후)
    candidates: int  # 기준 적용 전 순위 목록 길이 (DEPTH까지)
    recall5: float | None = None  # 관련 항목이 없는 질문은 None
    recall10: float | None = None
    rr: float | None = None
    post_recall5: float | None = None
    post_recall10: float | None = None
    post_rr: float | None = None
    grades: dict[str, int] = field(default_factory=dict)  # 결과의 라벨별 건수 (미판정 포함)


def evaluate_query(x: EvalQuery, ranked: list[Ranked], post_of: dict[str, str]) -> QueryResult:
    returned = [r.id for r in ranked][:MAX_RESULTS]
    result = QueryResult(x, returned, len(ranked))
    for entry_id in returned:
        key = x.grade(entry_id) or "미판정"
        result.grades[key] = result.grades.get(key, 0) + 1

    relevant = x.relevant
    if relevant:
        result.recall5 = recall_at(returned, relevant, 5)
        result.recall10 = recall_at(returned, relevant, 10)
        result.rr = reciprocal_rank(returned, relevant)
        posts = dedupe_posts(returned, post_of)
        relevant_posts = {post_of[i] for i in relevant}
        result.post_recall5 = recall_at(posts, relevant_posts, 5)
        result.post_recall10 = recall_at(posts, relevant_posts, 10)
        result.post_rr = reciprocal_rank(posts, relevant_posts)
    return result


def _mean(values: list[float | None]) -> float | None:
    present = [v for v in values if v is not None]
    return sum(present) / len(present) if present else None


@dataclass
class Summary:
    answerable: int  # 관련 항목이 있는 질문 수
    recall5: float | None
    recall10: float | None
    mrr: float | None
    post_recall5: float | None
    post_recall10: float | None
    post_mrr: float | None
    no_result_rate: float | None  # 없는 주제 질문 중 결과 0건으로 돌려준 비율
    avg_returned: float  # 질문당 결과 수
    noise_rate: float | None  # 결과 중 무관 비율 (판정된 결과만 분모)
    partial_kept: float | None  # '일부 관련' 라벨 중 결과에 남은 비율
    unjudged: int  # 결과 중 미판정 건수 (평가셋 판정 보강 필요)


def summarize(results: list[QueryResult]) -> Summary:
    absent = [r for r in results if r.query.source == "없는 주제"]
    grades = _sum_grades(results)
    judged = sum(n for g, n in grades.items() if g != "미판정")
    partial_total = sum(len(r.query.partial) for r in results)
    partial_kept = sum(len(set(r.returned) & r.query.partial) for r in results)
    return Summary(
        answerable=sum(1 for r in results if r.recall5 is not None),
        recall5=_mean([r.recall5 for r in results]),
        recall10=_mean([r.recall10 for r in results]),
        mrr=_mean([r.rr for r in results]),
        post_recall5=_mean([r.post_recall5 for r in results]),
        post_recall10=_mean([r.post_recall10 for r in results]),
        post_mrr=_mean([r.post_rr for r in results]),
        no_result_rate=(sum(1 for r in absent if not r.returned) / len(absent) if absent else None),
        avg_returned=sum(len(r.returned) for r in results) / len(results) if results else 0.0,
        noise_rate=grades.get("무관", 0) / judged if judged else None,
        partial_kept=partial_kept / partial_total if partial_total else None,
        unjudged=grades.get("미판정", 0),
    )


def _sum_grades(results: list[QueryResult]) -> dict[str, int]:
    total: dict[str, int] = {}
    for r in results:
        for g, n in r.grades.items():
            total[g] = total.get(g, 0) + n
    return total


def run(system: System, queries: list[EvalQuery], post_of: dict[str, str]) -> list[QueryResult]:
    return [evaluate_query(x, system.rank(x), post_of) for x in queries]


# ---------- 정답 후보 풀 ----------

POOL_DEPTH = 20
# 후보를 넓게 모으기 위한 BM25 변형 (가중치 실험의 후보와는 별개)
POOL_WEIGHTS: dict[str, dict[str, float]] = {
    "bm25": {},
    "bm25-title": {"title": 4.0},
    "bm25-flat": dict.fromkeys(FTS_COLUMNS, 1.0),
    "bm25-keywords": {"keywords": 5.0},
}


def pool_systems(conn: sqlite3.Connection, indexes: list) -> list[System]:
    systems = [bm25_system(conn, name, w) for name, w in POOL_WEIGHTS.items()]
    return systems + [embedding_system(conn, index) for index in indexes]


def candidate_pool(x: EvalQuery, systems: list[System]) -> dict[str, list[str]]:
    """후보 항목 ID → 찾은 설정과 순위(예: "bm25#3"). 필터가 있는 질문은 필터 없이도 모은다."""
    variants = [("", x)]
    if x.filters().describe():
        bare = x.model_copy(update={"problem_type": None, "domain": None, "technologies": []})
        variants.append(("(필터 없음)", bare))
    found: dict[str, list[str]] = {}
    for suffix, variant in variants:
        for system in systems:
            for rank, r in enumerate(system.rank(variant)[:POOL_DEPTH], start=1):
                found.setdefault(r.id, []).append(f"{system.name}{suffix}#{rank}")
    return found


def _best_rank(hits: list[str]) -> int:
    return min(int(h.rsplit("#", 1)[1]) for h in hits)


def _short(text: str, limit: int = 110) -> str:
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def pool_report(conn: sqlite3.Connection, queries: list[EvalQuery], systems: list[System]) -> str:
    """판정용 후보 목록. 항목마다 제목과 문제 상황·해결 방법 첫 줄을 보여 준다."""
    entries = {r[0]: json.loads(r[1]) for r in conn.execute("SELECT id, data FROM entries")}
    lines = [f"# 정답 후보 풀 (설정 {', '.join(s.name for s in systems)}, 상위 {POOL_DEPTH})"]
    for x in queries:
        found = candidate_pool(x, systems)
        unjudged = [i for i in found if x.grade(i) is None]
        filters = ", ".join(x.filters().describe())
        lines += [
            "",
            f"## {x.id} [{x.source}] {x.query}" + (f" ({filters})" if filters else ""),
            f"후보 {len(found)}개, 미판정 {len(unjudged)}개",
        ]
        for entry_id in sorted(found, key=lambda i: (_best_rank(found[i]), i)):
            e = entries[entry_id]
            mark = x.grade(entry_id) or "미판정"
            problem = e["problem_situation"][0]["text"] if e["problem_situation"] else "-"
            lines += [
                f"- {entry_id} [{mark}] {e['company']} · {_short(e['post_title'], 60)}"
                f" · 최고 {_best_rank(found[entry_id])}위 ({len(found[entry_id])}회)",
                f"  문제: {_short(problem)}",
                f"  해결: {_short(e['solution'][0]['text'])}",
            ]
    return "\n".join(lines) + "\n"


# ---------- 리포트 ----------


def _fmt(value: float | None, percent: bool = False) -> str:
    if value is None:
        return "-"
    return f"{value:.0%}" if percent else f"{value:.3f}"


def summary_rows(name: str, s: Summary) -> str:
    return (
        f"| {name} | {_fmt(s.recall5)} | {_fmt(s.mrr)} | {_fmt(s.recall10)}"
        f" | {_fmt(s.post_recall5)} | {_fmt(s.post_mrr)}"
        f" | {_fmt(s.no_result_rate, True)} | {s.avg_returned:.1f}"
        f" | {_fmt(s.noise_rate, True)} | {_fmt(s.partial_kept, True)} | {s.unjudged} |"
    )


SUMMARY_HEADER = (
    "| 설정 | Recall@5 | MRR | Recall@10 | 글 Recall@5 | 글 MRR"
    " | 없는 주제 결과 없음 | 평균 결과 수 | 무관 비율 | 일부 관련 유지 | 미판정 |\n"
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"
)


def build_report(
    system: System, results: list[QueryResult], db_meta: dict[str, str], title: str
) -> str:
    s = summarize(results)
    lines = [
        f"# {title}",
        "",
        f"- 설정: {system.description or system.name}"
        + (" (관련도 기준 적용)" if system.cutoff else ""),
        f"- 검색 DB: 항목 {db_meta.get('entry_count', '?')}개,"
        f" 빌드 {db_meta.get('built_at', '?')}, 스키마 {db_meta.get('schema_version', '?')}",
        f"- 평가셋: 질문 {len(results)}개 (관련 항목이 있는 질문 {s.answerable}개)",
        "- 정답은 '관련' 라벨만. Recall@k의 분모는 min(정답 수, k)",
        "- 글 단위 지표는 같은 글의 항목을 하나로 본다",
        "- 무관 비율의 분모는 판정된 결과만. '일부 관련'은 무관으로 세지 않는다",
        "",
        "## 요약",
        "",
        SUMMARY_HEADER,
        summary_rows(system.name, s),
        "",
        "## 질문별",
        "",
        "| ID | 출처 | 질문 | 정답 수 | R@5 | RR | 글 R@5 | 후보 | 결과 라벨 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in results:
        grades = ", ".join(f"{g} {n}" for g, n in sorted(r.grades.items())) or "결과 없음"
        lines.append(
            f"| {r.query.id} | {r.query.source} | {r.query.query} | {len(r.query.relevant)}"
            f" | {_fmt(r.recall5)} | {_fmt(r.rr)} | {_fmt(r.post_recall5)}"
            f" | {r.candidates} | {grades} |"
        )
    return "\n".join(lines) + "\n"


# ---------- 실행 ----------


def post_map(conn: sqlite3.Connection) -> dict[str, str]:
    return {r[0]: r[1] for r in conn.execute("SELECT id, post_url FROM entries")}


def db_meta(conn: sqlite3.Connection) -> dict[str, str]:
    return {r[0]: r[1] for r in conn.execute("SELECT key, value FROM meta")}


def parse_weights(text: str | None) -> dict[str, float]:
    """ "title=3,problem=2" → {"title": 3.0, "problem": 2.0}"""
    if not text:
        return {}
    weights = {}
    for part in text.split(","):
        column, _, value = part.partition("=")
        column = column.strip()
        if column not in FTS_COLUMNS:
            raise ValueError(f"없는 열: {column} (가능: {', '.join(FTS_COLUMNS)})")
        weights[column] = float(value)
    return weights


def main() -> None:
    parser = argparse.ArgumentParser(description="검색 평가셋으로 검색 설정을 잰다.")
    parser.add_argument("--name", default="baseline", help="리포트 이름 (m5-{name}.md)")
    parser.add_argument("--weights", help="bm25 가중치 변경, 예: title=3,problem=2")
    parser.add_argument("--db", type=Path, help="검색 DB 경로 (기본: 서버와 같은 경로)")
    parser.add_argument("--queries", type=Path, default=QUERIES_PATH)
    parser.add_argument(
        "--embedding",
        action="append",
        default=[],
        help="임베딩 모델 키 (search_embed.MODELS). 평가에서는 첫 모델로 순위를 매기고,"
        " --pool에서는 모든 모델을 후보 풀에 넣는다",
    )
    parser.add_argument("--pool", type=Path, help="평가 대신 판정용 후보 풀을 이 경로에 쓴다")
    args = parser.parse_args()

    conn = db.connect(args.db)
    queries = load_queries(args.queries)
    indexes = []
    for key in args.embedding:
        from eval.search_embed import MODELS, EmbeddingIndex  # numpy 외 의존성은 쓸 때만

        index = EmbeddingIndex(MODELS[key])
        fresh = index.build(conn)
        print(f"임베딩 {key}: 항목 {len(index.ids)}개 (새로 계산 {fresh}개)")
        indexes.append(index)

    if args.pool:
        args.pool.write_text(
            pool_report(conn, queries, pool_systems(conn, indexes)), encoding="utf-8"
        )
        print(f"후보 풀: {args.pool}")
        return

    if indexes:
        system = embedding_system(conn, indexes[0])
        system.name = args.name
    else:
        system = bm25_system(conn, args.name, parse_weights(args.weights))
    results = run(system, queries, post_map(conn))
    report = build_report(system, results, db_meta(conn), f"M5 검색 평가: {args.name}")
    REPORTS.mkdir(parents=True, exist_ok=True)
    out = REPORTS / f"m5-{args.name}.md"
    out.write_text(report, encoding="utf-8")
    s = summarize(results)
    print(
        f"{out.relative_to(ROOT)}: Recall@5 {_fmt(s.recall5)}, MRR {_fmt(s.mrr)},"
        f" 미판정 결과 {s.unjudged}건"
    )


if __name__ == "__main__":
    main()
