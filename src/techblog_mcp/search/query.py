"""검색·상세 조회·집계. 결과는 데이터로 돌려주고, 텍스트로 옮기는 일은 render 모듈이 한다."""

import json
import math
import sqlite3
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Literal

from techblog_mcp import taxonomy
from techblog_mcp.search.analyzer import tokenize
from techblog_mcp.search.schema import FTS_COLUMNS

GroupBy = Literal["technology", "problem_type", "domain", "company", "rejected_alternative"]

MAX_RESULTS = 10
# 관련도 기준 (M5 실험 E5·E7): 검색어 토큰의 IDF 합 중 항목에 있는 토큰의 IDF 합이 이 비율 이상인
# 항목만 돌려준다. 드문 단어(주제를 정하는 단어)가 빠지고 흔한 단어만 맞은 항목을 거르고,
# DB에 없는 주제에는 0건을 돌려주기 위함이다
MIN_IDF_COVERAGE = 0.5
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
            names = [
                f"{t} 계열" if len(taxonomy.technology_members(t)) > 1 else t
                for t in self.technologies
            ]
            parts.append(f"기술 ∋ {' 또는 '.join(names)}")
        return parts

    def technology_names(self) -> list[str]:
        """필터에 거는 이름. 상위 기술은 하위 기술까지 펼쳐 aggregate의 계열 합산과 맞춘다."""
        names = [m for t in self.technologies for m in taxonomy.technology_members(t)]
        return list(dict.fromkeys(names))

    def sql(self) -> tuple[str, list]:
        """entries 테이블(별칭 e)에 거는 WHERE 조건."""
        clauses, params = ["1=1"], []
        if self.domain:
            # 문제 유형·도메인 필터는 항목의 값 중 하나라도 맞으면 찾는다
            clauses.append(
                "EXISTS (SELECT 1 FROM entry_domains d WHERE d.entry_id = e.id AND d.domain = ?)"
            )
            params.append(self.domain)
        if self.problem_type:
            clauses.append(
                "EXISTS (SELECT 1 FROM entry_problem_types p"
                " WHERE p.entry_id = e.id AND p.problem_type = ?)"
            )
            params.append(self.problem_type)
        if self.technologies:
            # 여러 기술을 주면 하나라도 쓴 항목을 찾는다
            names = self.technology_names()
            marks = ", ".join("?" * len(names))
            clauses.append(
                "EXISTS (SELECT 1 FROM entry_technologies t"
                f" WHERE t.entry_id = e.id AND t.technology IN ({marks}))"
            )
            params.extend(names)
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


def _clean(tokens: list[str]) -> list[str]:
    return [t for t in dict.fromkeys(t.replace('"', "") for t in tokens) if t]


def query_units(query: str) -> list[tuple[str, ...]]:
    """관련도 기준을 재는 검색어 단위. 단위마다 대체 토큰 묶음이다.

    보통은 토큰 하나가 한 단위다. 기술 별칭("카프카")은 색인된 표준 이름("kafka")과 한 단위로
    묶어 둘 중 하나만 있어도 맞은 것으로 본다. 따로 세면 글에 거의 쓰이지 않는 한글 별칭이
    드문 단어로 계산돼 정답이 관련도 기준에서 잘린다.
    """
    units = [(t,) for t in _clean(tokenize(query))]
    for word in query.split():
        if tech := taxonomy.normalize_technology(word):
            alternatives = tuple(_clean(tokenize(word) + tokenize(tech)))
            units = [u for u in units if not (len(u) == 1 and u[0] in alternatives)]
            units.append(alternatives)
    return list(dict.fromkeys(u for u in units if u))


def query_tokens(query: str) -> list[str]:
    """검색어 토큰 (중복 제거). 기술 별칭이 있으면 표준 이름의 토큰도 더한다."""
    return list(dict.fromkeys(t for unit in query_units(query) for t in unit))


def _phrase(token: str) -> str:
    return f'"{token}"'


@dataclass
class SearchResult:
    entries: list[dict]  # 관련도 순 최대 MAX_RESULTS건
    total: int  # 관련도 기준을 넘은 건수 (검색어가 없으면 필터에 맞는 건수)


def search(conn: sqlite3.Connection, query: str, filters: Filters) -> SearchResult:
    where, params = filters.sql()
    units = query_units(query)
    tokens = list(dict.fromkeys(t for unit in units for t in unit))
    if not tokens:
        # 검색어에서 뽑을 토큰이 없으면 필터만으로 최신순
        base = f"FROM entries e WHERE {where}"
        total = conn.execute(f"SELECT COUNT(*) {base}", params).fetchone()[0]
        rows = conn.execute(
            f"SELECT e.data {base} ORDER BY e.published_at DESC LIMIT ?", [*params, MAX_RESULTS]
        ).fetchall()
        return SearchResult([_entry(r) for r in rows], total)

    # 검색어 토큰이 하나라도 걸린 항목을 BM25 순으로 모은 뒤 관련도 기준으로 거른다
    weights = ", ".join(str(w) for w in FTS_COLUMNS.values())
    ranked = conn.execute(
        "SELECT e.rowid FROM entries_fts f JOIN entries e ON e.rowid = f.rowid"
        f" WHERE entries_fts MATCH ? AND {where} ORDER BY bm25(entries_fts, {weights})",
        [" OR ".join(map(_phrase, tokens)), *params],
    ).fetchall()
    coverage = _idf_coverage(conn, _without_filter_terms(units, filters))
    passed = [r[0] for r in ranked if coverage(r[0]) >= MIN_IDF_COVERAGE]
    shown = passed[:MAX_RESULTS]
    data = dict(
        conn.execute(
            f"SELECT rowid, data FROM entries WHERE rowid IN ({', '.join('?' * len(shown))})",
            shown,
        ).fetchall()
    )
    return SearchResult([json.loads(data[i]) for i in shown], len(passed))


def _without_filter_terms(units: list[tuple[str, ...]], filters: Filters) -> list[tuple[str, ...]]:
    """관련도 기준에서 필터 이름과 겹치는 검색어 단위를 뺀다 (M6).

    색인의 keywords 열에는 분류·기술 이름이 들어 있어, 필터를 건 후보는 모두 필터 이름의 토큰을
    가진다. 검색어가 필터 이름을 되풀이하면(문제 유형 "트래픽 급증 대응" + 검색어 "트래픽 급증
    대기열") 그 단위가 후보마다 자동으로 맞아 주제 단어("대기열")가 없는 항목도 기준을 넘는다.
    다 빠지면(검색어가 필터 이름뿐이면) 원래 단위로 잰다.
    """
    names = [filters.problem_type, filters.domain, *filters.technology_names()]
    filter_tokens = {t for name in names if name for t in tokenize(name)}
    if not filter_tokens:
        return units
    remaining = [u for u in units if not any(t in filter_tokens for t in u)]
    return remaining or units


def _idf_coverage(conn: sqlite3.Connection, units: list[tuple[str, ...]]):
    """rowid → 그 항목에 있는 검색어 단위의 IDF 합 ÷ 검색어 전체 단위의 IDF 합.

    IDF는 BM25와 같은 식으로 DB 전체 항목 기준(필터와 무관)으로 계산한다. 대체 토큰이 여러 개인
    단위는 DB에 있는 토큰 중 가장 큰 IDF를 쓴다.
    """
    n = conn.execute("SELECT COUNT(*) FROM entries").fetchone()[0]
    holders = {
        t: {
            r[0]
            for r in conn.execute(
                "SELECT rowid FROM entries_fts WHERE entries_fts MATCH ?", [_phrase(t)]
            )
        }
        for unit in units
        for t in unit
    }

    def idf(t: str) -> float:
        df = len(holders[t])
        return math.log((n - df + 0.5) / (df + 0.5) + 1)

    weights = []
    for unit in units:
        present = [t for t in unit if holders[t]] or list(unit)
        weights.append(max(idf(t) for t in present))
    total = sum(weights)

    def coverage(rowid: int) -> float:
        hit = sum(
            w
            for unit, w in zip(units, weights, strict=True)
            if any(rowid in holders[t] for t in unit)
        )
        return hit / total

    return coverage


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
    with_metrics: int = 0  # 그중 성능·운영 포인트에 수치가 있는 항목
    companies: list[str] = field(default_factory=list)
    examples: list[str] = field(default_factory=list)
    # 기술 집계에서 계열로 합쳐진 하위 기술별 항목 수 (예: Kafka 아래 Amazon MSK)
    members: dict[str, int] = field(default_factory=dict)


@dataclass
class AggregateResult:
    total: int  # 모수: 조건에 맞는 항목 수
    with_metrics: int  # 모수 중 성능·운영 포인트에 수치가 있는 항목 수
    companies: int  # 모수: 조건에 맞는 항목을 낸 회사 수
    groups: list[Group]  # 상위 top_n개
    group_count: int  # 전체 그룹 수


_GROUP_KEY_SQL: dict[str, str] = {
    "problem_type": "SELECT problem_type FROM entry_problem_types WHERE entry_id = ?",
    "domain": "SELECT domain FROM entry_domains WHERE entry_id = ?",
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
        "SELECT e.id, e.has_metrics, e.company"
        f" FROM entries e WHERE {where} ORDER BY e.published_at DESC, e.id DESC",
        params,
    ).fetchall()

    groups: dict[str, Group] = {}
    companies_by_group: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        for key, member in _group_keys(conn, group_by, row):
            group = groups.setdefault(key, Group(key))
            group.total += 1
            group.with_metrics += row["has_metrics"]
            for name in member:
                group.members[name] = group.members.get(name, 0) + 1
            if row["company"] not in companies_by_group[key]:
                companies_by_group[key].add(row["company"])
                group.companies.append(row["company"])
            if len(group.examples) < EXAMPLES_PER_GROUP:
                group.examples.append(row["id"])

    ranked = sorted(groups.values(), key=lambda g: (-g.total, -len(g.companies), g.key))
    return AggregateResult(
        total=len(rows),
        with_metrics=sum(r["has_metrics"] for r in rows),
        companies=len({r["company"] for r in rows}),
        groups=ranked[: max(1, top_n)],
        group_count=len(ranked),
    )


def _group_keys(
    conn: sqlite3.Connection, group_by: GroupBy, row: sqlite3.Row
) -> list[tuple[str, list[str]]]:
    """(그룹 이름, 그 그룹에 합쳐진 하위 기술들). 하위 기술은 기술 집계에서만 있다."""
    if group_by == "company":
        return [(row["company"], [])]
    if group_by == "technology":
        return _technology_families(conn, row["id"])
    # 한 항목은 여러 그룹에 들어갈 수 있다(문제 유형·도메인). 같은 그룹에는 한 번만 센다
    keys = dict.fromkeys(r[0] for r in conn.execute(_GROUP_KEY_SQL[group_by], [row["id"]]))
    return [(key, []) for key in keys]


def _technology_families(conn: sqlite3.Connection, entry_id: str) -> list[tuple[str, list[str]]]:
    """항목의 기술을 계열(상위 기술)로 합친다. 같은 계열의 제품을 여러 개 써도 한 번만 센다.

    예: Kafka와 Amazon MSK를 함께 쓴 항목은 Kafka 계열 1건이고 하위 기술은 [Amazon MSK].
    """
    families: dict[str, list[str]] = {}
    for (name,) in conn.execute(
        "SELECT technology FROM entry_technologies WHERE entry_id = ?", [entry_id]
    ):
        family = taxonomy.technology_family(name)
        members = families.setdefault(family, [])
        if family != name:
            members.append(name)
    return list(families.items())
