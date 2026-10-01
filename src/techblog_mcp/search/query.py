"""검색·상세 조회·집계. 결과는 데이터로 돌려주고, 텍스트로 옮기는 일은 render 모듈이 한다."""

import json
import sqlite3
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Literal

from techblog_mcp import taxonomy
from techblog_mcp.search.analyzer import tokenize
from techblog_mcp.search.schema import FTS_COLUMNS

GroupBy = Literal["technology", "problem_type", "domain", "company", "rejected_alternative"]

DEFAULT_LIMIT = 5
MAX_LIMIT = 10
EXAMPLES_PER_GROUP = 2


@dataclass
class Filters:
    problem_type: str | None = None
    domain: str | None = None
    technologies: list[str] = field(default_factory=list)  # 정규화된 표준 이름

    def describe(self) -> list[str]:
        parts = []
        if self.problem_type:
            parts.append(f"문제 유형 = {self.problem_type}")
        if self.domain:
            parts.append(f"도메인 = {self.domain}")
        if self.technologies:
            parts.append(f"기술 ∋ {' 또는 '.join(self.technologies)}")
        return parts

    def sql(self) -> tuple[str, list]:
        """entries 테이블(별칭 e)에 거는 WHERE 조건."""
        clauses, params = ["1=1"], []
        if self.domain:
            clauses.append("e.domain = ?")
            params.append(self.domain)
        if self.problem_type:
            # 검색 필터는 주·보조 유형 모두 매칭 (docs/기획.md "분류 개수")
            clauses.append(
                "EXISTS (SELECT 1 FROM entry_problem_types p"
                " WHERE p.entry_id = e.id AND p.problem_type = ?)"
            )
            params.append(self.problem_type)
        if self.technologies:
            # 여러 기술을 주면 하나라도 쓴 항목을 찾는다
            marks = ", ".join("?" * len(self.technologies))
            clauses.append(
                "EXISTS (SELECT 1 FROM entry_technologies t"
                f" WHERE t.entry_id = e.id AND t.technology IN ({marks}))"
            )
            params.extend(self.technologies)
        return " AND ".join(clauses), params


@dataclass
class TechnologyResolution:
    normalized: list[str]
    unknown: dict[str, list[str]]  # 사전에 없는 입력 → 비슷한 표준 이름


def resolve_technologies(names: list[str]) -> TechnologyResolution:
    normalized: list[str] = []
    unknown: dict[str, list[str]] = {}
    for name in names:
        if not name.strip():
            continue
        tech = taxonomy.normalize_technology(name)
        if tech is None:
            unknown[name] = taxonomy.similar_technologies(name)
        elif tech not in normalized:
            normalized.append(tech)
    return TechnologyResolution(normalized, unknown)


def _entry(row: sqlite3.Row) -> dict:
    return json.loads(row["data"])


def _match_expression(query: str) -> str | None:
    tokens = tokenize(query)
    # "카프카"처럼 별칭으로 물어도 색인된 표준 이름("kafka")으로 찾히게 한다
    for word in query.split():
        if tech := taxonomy.normalize_technology(word):
            tokens.extend(tokenize(tech))
    unique = list(dict.fromkeys(t.replace('"', "") for t in tokens))
    unique = [t for t in unique if t]
    if not unique:
        return None
    return " OR ".join(f'"{t}"' for t in unique)


@dataclass
class SearchResult:
    entries: list[dict]
    total: int  # 검색어·필터에 걸린 전체 건수 (limit 전)


def search(conn: sqlite3.Connection, query: str, filters: Filters, limit: int) -> SearchResult:
    limit = max(1, min(limit, MAX_LIMIT))
    where, params = filters.sql()
    match = _match_expression(query)
    if match is None:
        # 검색어에서 뽑을 토큰이 없으면 필터만으로 최신순
        base = f"FROM entries e WHERE {where}"
        total = conn.execute(f"SELECT COUNT(*) {base}", params).fetchone()[0]
        rows = conn.execute(
            f"SELECT e.data {base} ORDER BY e.published_at DESC LIMIT ?", [*params, limit]
        ).fetchall()
        return SearchResult([_entry(r) for r in rows], total)

    weights = ", ".join(str(w) for w in FTS_COLUMNS.values())
    base = (
        "FROM entries_fts f JOIN entries e ON e.rowid = f.rowid"
        f" WHERE entries_fts MATCH ? AND {where}"
    )
    total = conn.execute(f"SELECT COUNT(*) {base}", [match, *params]).fetchone()[0]
    rows = conn.execute(
        f"SELECT e.data {base} ORDER BY bm25(entries_fts, {weights}) LIMIT ?",
        [match, *params, limit],
    ).fetchall()
    return SearchResult([_entry(r) for r in rows], total)


@dataclass
class Detail:
    entry: dict
    siblings: list[str]  # 같은 글에서 나온 다른 항목 ID


def get_details(conn: sqlite3.Connection, ids: list[str]) -> tuple[list[Detail], list[str]]:
    """(찾은 항목, 없는 ID)"""
    details, missing = [], []
    for entry_id in ids:
        row = conn.execute("SELECT data, post_url FROM entries WHERE id = ?", [entry_id]).fetchone()
        if row is None:
            missing.append(entry_id)
            continue
        siblings = [
            r[0]
            for r in conn.execute(
                "SELECT id FROM entries WHERE post_url = ? AND id != ? ORDER BY id",
                [row["post_url"], entry_id],
            )
        ]
        details.append(Detail(_entry(row), siblings))
    return details, missing


@dataclass
class Group:
    key: str
    total: int = 0
    with_results: int = 0  # 그중 성능·운영 포인트(적용 결과 등)가 있는 항목
    companies: list[str] = field(default_factory=list)
    examples: list[str] = field(default_factory=list)


@dataclass
class AggregateResult:
    total: int  # 모수: 조건에 맞는 항목 수
    with_results: int  # 모수 중 성능·운영 포인트가 있는 항목 수
    companies: int  # 모수: 조건에 맞는 항목을 낸 회사 수
    groups: list[Group]  # 상위 top_n개
    group_count: int  # 전체 그룹 수


_GROUP_KEY_SQL: dict[str, str] = {
    "technology": "SELECT technology FROM entry_technologies WHERE entry_id = ?",
    "rejected_alternative": (
        "SELECT name FROM entry_rejected_alternatives WHERE entry_id = ? AND kind = '기술'"
    ),
}


def aggregate(
    conn: sqlite3.Connection, group_by: GroupBy, filters: Filters, top_n: int
) -> AggregateResult:
    where, params = filters.sql()
    if group_by == "rejected_alternative":
        # 버린 대안 집계는 기술 대안이 있는 항목만 대상 (설계 방식은 get_details에서만 보여 준다)
        where += (
            " AND EXISTS (SELECT 1 FROM entry_rejected_alternatives r"
            " WHERE r.entry_id = e.id AND r.kind = '기술')"
        )
    rows = conn.execute(
        "SELECT e.id, e.has_results, e.company, e.primary_problem_type, e.domain"
        f" FROM entries e WHERE {where} ORDER BY e.published_at DESC, e.id DESC",
        params,
    ).fetchall()

    groups: dict[str, Group] = {}
    companies_by_group: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        for key in _group_keys(conn, group_by, row):
            group = groups.setdefault(key, Group(key))
            group.total += 1
            group.with_results += row["has_results"]
            if row["company"] not in companies_by_group[key]:
                companies_by_group[key].add(row["company"])
                group.companies.append(row["company"])
            if len(group.examples) < EXAMPLES_PER_GROUP:
                group.examples.append(row["id"])

    ranked = sorted(groups.values(), key=lambda g: (-g.total, -len(g.companies), g.key))
    return AggregateResult(
        total=len(rows),
        with_results=sum(r["has_results"] for r in rows),
        companies=len({r["company"] for r in rows}),
        groups=ranked[: max(1, top_n)],
        group_count=len(ranked),
    )


def _group_keys(conn: sqlite3.Connection, group_by: GroupBy, row: sqlite3.Row) -> list[str]:
    if group_by == "problem_type":
        return [row["primary_problem_type"]]  # 주 유형 기준으로 중복 없이 센다
    if group_by == "domain":
        return [row["domain"]]
    if group_by == "company":
        return [row["company"]]
    # 한 항목이 같은 키를 두 번 세지 않도록 중복 제거
    return list(dict.fromkeys(r[0] for r in conn.execute(_GROUP_KEY_SQL[group_by], [row["id"]])))
