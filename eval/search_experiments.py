"""M5 검색 실험 E1~E6. 실험마다 비교 리포트를 eval/reports/m5-{실험}.md로 쓴다.

    uv run python eval/search_experiments.py e1 e2 e4 e5
    uv run python eval/search_experiments.py e3  # 사용자 사전으로 임시 색인 빌드
    uv run python eval/search_experiments.py e6  # OpenAI 임베딩 (캐시 사용)
    uv run python eval/search_experiments.py e7 e8  # LLM 문서 확장·질의 재작성 (캐시 사용)
    uv run python eval/search_experiments.py e9  # 최종 서버 설정

서버 코드는 바꾸지 않는다. 관련도 기준·글 묶기·하이브리드·문서 확장·질의 재작성은
여기서 순위 목록을 가공해 흉내 내고, 결정이 나면 서버에 옮긴다.
실험 설계는 docs/milestones/M5.md, 지표는 eval/search/README.md.
"""

import argparse
import json
import math
import sqlite3
import sys
import tempfile
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass
from functools import cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eval.search_eval import (  # noqa: E402
    MAX_RESULTS,
    REPORTS,
    SUMMARY_HEADER,
    EvalQuery,
    QueryResult,
    Ranked,
    System,
    bm25_ranking,
    db_meta,
    evaluate_query,
    filtered_ids,
    load_queries,
    post_map,
    summarize,
    summary_rows,
)
from pipeline import expand  # noqa: E402
from pipeline.build_index import build, fts_fields  # noqa: E402
from pipeline.extract.schema import Entry  # noqa: E402
from techblog_mcp import db  # noqa: E402
from techblog_mcp.search import analyzer  # noqa: E402
from techblog_mcp.search import query as q  # noqa: E402
from techblog_mcp.search.schema import FTS_COLUMNS  # noqa: E402

ALL = 100_000  # 걸린 항목 전체를 보려고 쓰는 깊이
RRF_K = 60
EXPANSION_COLUMN = "expansion"  # E7 문서 확장 열

# ---------- 공통 준비물 ----------


class Context:
    """한 검색 DB에 대한 실험 준비물: 항목 토큰, 문서 빈도, 글 대응, 질문별 BM25 전체 순위."""

    def __init__(
        self,
        conn: sqlite3.Connection,
        queries: list[EvalQuery],
        expansion: dict[str, str] | None = None,
    ):
        """expansion: 이 DB를 빌드할 때 쓴 문서 확장 텍스트. 없으면 data/expansions.jsonl."""
        self.conn = conn
        self.queries = queries
        self.post_of = post_map(conn)
        if expansion is None:
            expansion = {i: expand.expansion_text(r) for i, r in expand.load().items()}
        self.expansion_text = expansion
        self.tokens = entry_tokens(conn, expansion)
        self.columns = dict(FTS_COLUMNS)
        self.df = Counter(t for ts in self.tokens.values() for t in ts)
        self.n = len(self.tokens)
        self._bm25: dict[tuple, list[Ranked]] = {}

    def idf(self, token: str) -> float:
        df = self.df.get(token, 0)
        return math.log((self.n - df + 0.5) / (df + 0.5) + 1)

    def bm25(self, x: EvalQuery, weights: dict[str, float] | None = None) -> list[Ranked]:
        w = {**self.columns, **(weights or {})}
        key = (x.id, x.query, tuple(w.values()))
        if key not in self._bm25:
            self._bm25[key] = bm25_ranking(self.conn, x.query, x.filters(), w, depth=ALL)
        return self._bm25[key]


def entry_tokens(conn: sqlite3.Connection, expansion: dict[str, str]) -> dict[str, set[str]]:
    """항목별로 색인된 토큰 집합. 색인과 같은 텍스트(fts_fields)를 같은 분석기로 자른다."""
    tokens = {}
    for entry_id, data in conn.execute("SELECT id, data FROM entries"):
        entry = Entry.model_validate(json.loads(data))
        fields = fts_fields(entry, expansion.get(entry_id, ""))
        tokens[entry_id] = {t for text in fields.values() for t in analyzer.tokenize(text)}
    return tokens


def query_tokens(query: str) -> list[str]:
    """서버 MATCH 식과 같은 검색어 토큰 (기술 별칭의 표준 이름 토큰 포함)."""
    return q.query_tokens(query)


# ---------- 순위 가공: 관련도 기준, 글 묶기 ----------

Cutoff = Callable[[Context, EvalQuery, list[Ranked]], list[Ranked]]


def relative(r: float) -> Cutoff:
    """① 1위 점수 대비 r 이상."""

    def cut(ctx, x, ranked):
        return [e for e in ranked if ranked and e.score >= r * ranked[0].score]

    return cut


def match_ratio(t: float) -> Cutoff:
    """② 검색어 토큰 중 항목에 있는 비율이 t 이상."""

    def cut(ctx, x, ranked):
        qt = set(query_tokens(x.query))
        if not qt:
            return ranked
        return [e for e in ranked if len(qt & ctx.tokens[e.id]) / len(qt) >= t]

    return cut


def idf_coverage(t: float, top: int | None = None) -> Cutoff:
    """③ IDF 가중 일치 비율: 항목에 있는 검색어 토큰의 IDF 합 ÷ 검색어 전체 IDF 합 ≥ t.

    드문 단어(주제를 정하는 단어)가 맞지 않고 흔한 단어만 맞은 항목을 거른다.
    top을 주면 검색어에서 IDF가 가장 큰 토큰 top개만으로 잰다. 검색어가 길수록 모든 단어를
    맞추기 어려워 비율이 낮아지는 문제(M5 E5에서 m10이 0건)를 보완하기 위함.
    """

    def cut(ctx, x, ranked):
        qt = set(query_tokens(x.query))
        if top:
            qt = set(sorted(qt, key=ctx.idf, reverse=True)[:top])
        total = sum(ctx.idf(tok) for tok in qt)
        if not total:
            return ranked
        return [
            e for e in ranked if sum(ctx.idf(tok) for tok in qt & ctx.tokens[e.id]) / total >= t
        ]

    return cut


def rare_match(p: float) -> Cutoff:
    """③' 희소 단어(문서 빈도 비율 ≤ p) 중 하나라도 맞아야 통과.

    검색어에 희소 단어가 없으면 그대로 둔다.
    """

    def cut(ctx, x, ranked):
        rare = {tok for tok in query_tokens(x.query) if ctx.df.get(tok, 0) / ctx.n <= p}
        if not rare:
            return ranked
        return [e for e in ranked if rare & ctx.tokens[e.id]]

    return cut


def absolute(s: float) -> Cutoff:
    """④ BM25 절대 점수 s 이상 (부호를 바꾼 값)."""

    def cut(ctx, x, ranked):
        return [e for e in ranked if e.score >= s]

    return cut


def both(*cutoffs: Cutoff) -> Cutoff:
    def cut(ctx, x, ranked):
        for c in cutoffs:
            ranked = c(ctx, x, ranked)
        return ranked

    return cut


def group_by_post(ctx: Context, ranked: list[Ranked], how: str) -> list[Ranked]:
    """같은 글의 항목을 글 점수로 묶어 올린다. 글 점수는 max(최고 항목) 또는 sum2(상위 2개 합)."""
    by_post: dict[str, list[float]] = {}
    for e in ranked:
        by_post.setdefault(ctx.post_of[e.id], []).append(e.score)
    post_score = {
        p: (max(s) if how == "max" else sum(sorted(s, reverse=True)[:2]))
        for p, s in by_post.items()
    }
    return sorted(ranked, key=lambda e: (-post_score[ctx.post_of[e.id]], -e.score))


# ---------- 실험 실행 ----------


@dataclass
class Row:
    system: System
    results: list[QueryResult]


def bm25_system(
    ctx: Context,
    name: str,
    weights: dict[str, float] | None = None,
    cutoff: Cutoff | None = None,
    group: str | None = None,
    description: str = "",
) -> System:
    def rank(x: EvalQuery) -> list[Ranked]:
        ranked = ctx.bm25(x, weights)
        if group:
            ranked = group_by_post(ctx, ranked, group)
        if cutoff:
            ranked = cutoff(ctx, x, ranked)
        return ranked

    return System(name, rank, cutoff=cutoff is not None, description=description)


def run_rows(ctx: Context, systems: list[System]) -> list[Row]:
    return [
        Row(s, [evaluate_query(x, s.rank(x), ctx.post_of) for x in ctx.queries]) for s in systems
    ]


def comparison(title: str, intro: list[str], rows: list[Row], ctx: Context) -> str:
    meta = db_meta(ctx.conn)
    lines = [
        f"# {title}",
        "",
        *intro,
        "",
        f"- 검색 DB: 항목 {meta.get('entry_count')}개, 스키마 {meta.get('schema_version')}",
        f"- 평가셋: 질문 {len(ctx.queries)}개. 지표 정의는 eval/search/README.md",
        f"- 관련도 기준이 없는 설정은 상위 {MAX_RESULTS}건을 결과로 본다",
        "",
        SUMMARY_HEADER,
        *(summary_rows(r.system.name, summarize(r.results)) for r in rows),
        "",
        "| 설정 | 설명 |",
        "| --- | --- |",
        *(f"| {r.system.name} | {r.system.description} |" for r in rows),
    ]
    return "\n".join(lines) + "\n"


def per_query(rows: list[Row]) -> list[str]:
    """설정별 질문 단위 R@5 / 결과 수 비교표."""
    names = [r.system.name for r in rows]
    lines = [
        "## 질문별 (R@5 · 결과 수)",
        "",
        "| 질문 | " + " | ".join(names) + " |",
        "| --- |" + " --- |" * len(names),
    ]
    for i, x in enumerate(rows[0].results):
        cells = []
        for r in rows:
            res = r.results[i]
            r5 = f"{res.recall5:.2f}" if res.recall5 is not None else "-"
            cells.append(f"{r5} · {len(res.returned)}")
        lines.append(f"| {x.query.id} {x.query.query[:24]} | " + " | ".join(cells) + " |")
    return lines


def write(name: str, text: str) -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    path = REPORTS / f"m5-{name}.md"
    path.write_text(text, encoding="utf-8")
    print(f"{path.relative_to(ROOT)}")


# ---------- E1 기준선 ----------

_MARK = {"관련": "✅", "일부 관련": "△", "무관": "✗", None: "?"}


def e1(ctx: Context) -> None:
    base = bm25_system(ctx, "baseline", description="현재 서버 설정 (BM25 OR 매칭, 상위 10건)")
    rows = run_rows(ctx, [base])
    lines = [
        comparison(
            "M5 E1: 기준선",
            ["현재 서버 검색 그대로. 이후 실험의 비교 기준이다."],
            rows,
            ctx,
        ),
        "## 질문별 상위 10건 점수 분포",
        "",
        "1위 점수 대비 비율과 라벨 (✅ 관련, △ 일부 관련, ✗ 무관).",
        "M1 관찰 기록을 1,315개 항목으로 다시 잰 것",
        "",
        "| 질문 | 걸린 항목 | 1위 점수 | 상위 10건 |",
        "| --- | --- | --- | --- |",
    ]
    for x in ctx.queries:
        ranked = ctx.bm25(x)
        top = ranked[0].score if ranked else 0
        dist = ", ".join(f"{e.score / top:.0%} {_MARK[x.grade(e.id)]}" for e in ranked[:10])
        lines.append(f"| {x.id} {x.query} | {len(ranked)} | {top:.1f} | {dist} |")
    lines += ["", *noise_section(ctx, rows[0])]
    write("e1-baseline", "\n".join(lines) + "\n")


def noise_section(ctx: Context, row: Row) -> list[str]:
    """여러 질문의 상위 10건에 무관으로 자주 나오는 항목 (경계 글 후보)."""
    counter: Counter[str] = Counter()
    for res in row.results:
        for entry_id in res.returned:
            if res.query.grade(entry_id) == "무관":
                counter[entry_id] += 1
    titles = {
        r[0]: json.loads(r[1])["post_title"]
        for r in ctx.conn.execute("SELECT id, data FROM entries")
    }
    lines = [
        "## 자주 나오는 잡음 항목",
        "",
        "상위 10건에 `무관`으로 3번 이상 나온 항목. 경계 글(블로그 글 모음, 행사 후기 등) 확인용",
        "",
        "| 항목 | 횟수 | 제목 |",
        "| --- | --- | --- |",
    ]
    for entry_id, n in counter.most_common():
        if n < 3:
            break
        lines.append(f"| {entry_id} | {n} | {titles[entry_id]} |")
    return lines


# ---------- E2 필드 가중치 ----------

E2_WEIGHTS: dict[str, dict[str, float]] = {
    "current": {},
    "flat": dict.fromkeys(FTS_COLUMNS, 1.0),
    "title3": {"title": 3.0},
    "keywords4": {"keywords": 4.0},
    "prob=sol": {"problem": 2.0, "solution": 2.0},
    "ops·rej0.5": {"ops": 0.5, "rejected": 0.5},
    "title3·kw3": {"title": 3.0, "keywords": 3.0},
    "title3·kw3·low": {"title": 3.0, "keywords": 3.0, "ops": 0.5, "rejected": 0.5},
    "sol3": {"solution": 3.0},
}


def _desc(weights: dict[str, float]) -> str:
    w = {**FTS_COLUMNS, **weights}
    return ", ".join(f"{c}={v:g}" for c, v in w.items())


def e2(ctx: Context) -> None:
    systems = [bm25_system(ctx, name, w, description=_desc(w)) for name, w in E2_WEIGHTS.items()]
    rows = run_rows(ctx, systems)
    text = comparison(
        "M5 E2: 필드 가중치",
        ["bm25() 열 가중치만 바꿔 비교한다. 관련도 기준 없이 상위 10건."],
        rows,
        ctx,
    )
    write("e2-weights", text + "\n" + "\n".join(per_query(rows)) + "\n")


# ---------- E4 글 묶기 ----------


def e4(ctx: Context) -> None:
    systems = [
        bm25_system(ctx, "item", description="항목 점수 순 (기준선)"),
        bm25_system(ctx, "post-max", group="max", description="글의 최고 항목 점수로 묶어 정렬"),
        bm25_system(
            ctx, "post-sum2", group="sum2", description="글의 상위 2개 항목 점수 합으로 묶어 정렬"
        ),
    ]
    rows = run_rows(ctx, systems)
    text = comparison(
        "M5 E4: 같은 글의 항목 묶기",
        [
            "같은 글의 항목을 글 점수 순으로 붙여 올린다. 글 안에서는 항목 점수 순.",
            "M1 시나리오 2(하위 문제별로 나뉜 항목이 검색어를 적게 맞춰 아래로 가는 문제) 확인용.",
        ],
        rows,
        ctx,
    )
    write("e4-grouping", text + "\n" + "\n".join(per_query(rows)) + "\n")


# ---------- E5 관련도 기준 ----------


def e5_cutoffs() -> dict[str, tuple[Cutoff, str]]:
    c: dict[str, tuple[Cutoff, str]] = {}
    for r in (0.3, 0.4, 0.5, 0.6):
        c[f"rel{r:g}"] = (relative(r), f"① 1위 대비 {r:.0%} 이상")
    for t in (0.3, 0.4, 0.5):
        c[f"match{t:g}"] = (match_ratio(t), f"② 검색어 토큰 일치 비율 {t:.0%} 이상")
    for t in (0.3, 0.4, 0.5, 0.6):
        c[f"idf{t:g}"] = (idf_coverage(t), f"③ IDF 가중 일치 비율 {t:.0%} 이상")
    for k in (3, 4):
        for t in (0.4, 0.5):
            c[f"idf{t:g}@top{k}"] = (
                idf_coverage(t, top=k),
                f"③ IDF가 큰 검색어 토큰 {k}개 기준 IDF 일치 비율 {t:.0%} 이상",
            )
    for p in (0.02, 0.05, 0.1):
        c[f"rare{p:g}"] = (rare_match(p), f"③' 문서 빈도 {p:.0%} 이하 희소 단어 1개 이상 일치")
    for s in (8, 10, 12, 15):
        c[f"abs{s}"] = (absolute(s), f"④ BM25 점수 {s} 이상")
    for t in (0.4, 0.5):
        for r in (0.3, 0.4):
            c[f"idf{t:g}+rel{r:g}"] = (
                both(idf_coverage(t), relative(r)),
                f"③ IDF 일치 {t:.0%} 이상 그리고 ① 1위 대비 {r:.0%} 이상",
            )
    for t in (0.4, 0.5):
        c[f"idf{t:g}+rare0.05"] = (
            both(idf_coverage(t), rare_match(0.05)),
            f"③ IDF 일치 {t:.0%} 이상 그리고 ③' 희소 단어(5%) 일치",
        )
    return c


def e5(ctx: Context, group: str | None = None) -> None:
    systems = [bm25_system(ctx, "none", group=group, description="기준 없음 (상위 10건)")]
    for name, (cutoff, desc) in e5_cutoffs().items():
        systems.append(bm25_system(ctx, name, cutoff=cutoff, group=group, description=desc))
    rows = run_rows(ctx, systems)
    text = comparison(
        "M5 E5: 관련도 기준",
        [
            "BM25 순위(현재 가중치)에 관련도 기준을 걸고 통과한 항목만 최대 10건 돌려준다.",
            "Recall은 기준이 정답을 잘라내면 내려가고,",
            "무관 비율과 '없는 주제 결과 없음'은 잡음을 거르면 좋아진다.",
            f"글 묶기: {group or '없음'}",
        ],
        rows,
        ctx,
    )
    selected = [r for r in rows if r.system.name in E5_DETAIL]
    write("e5-cutoff", text + "\n" + "\n".join(per_query(selected)) + "\n")


E5_DETAIL = {"none", "rel0.4", "idf0.4", "idf0.5", "idf0.5@top3", "idf0.5@top4", "abs10"}


# ---------- E3 형태소 사용자 사전 ----------

# E3에서 잰 사용자 사전. M5 결정으로 서버 분석기에 들어가 이제 기본값과 같다
USER_WORDS = analyzer.USER_WORDS


@cache
def _user_kiwi():
    from kiwipiepy import Kiwi

    kiwi = Kiwi()
    for word in USER_WORDS:
        kiwi.add_user_word(word, "NNP", 0)
    return kiwi


def e3(conn: sqlite3.Connection, queries: list[EvalQuery]) -> None:
    base_ctx = Context(conn, queries)
    rows = run_rows(base_ctx, e3_systems(base_ctx, "기본"))

    original = analyzer._kiwi
    analyzer._kiwi = _user_kiwi  # 색인과 검색이 같은 함수를 쓰므로 둘 다 바뀐다
    try:
        cursor = conn.execute("SELECT data FROM entries ORDER BY rowid")
        entries = [Entry.model_validate(json.loads(d)) for (d,) in cursor]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "user-dict.sqlite"
            build(entries, path)
            user_conn = db.connect(path)
            try:
                user_ctx = Context(user_conn, queries)
                rows += run_rows(user_ctx, e3_systems(user_ctx, "사용자 사전"))
                examples = [
                    f"- {w}: {original().tokenize(w)[0].form}… → {analyzer.tokenize(w)}"
                    for w in ["시그널링", "아웃박스", "동시성", "메트릭"]
                ]
            finally:
                user_conn.close()
    finally:
        analyzer._kiwi = original

    text = comparison(
        "M5 E3: 형태소 사용자 사전",
        [
            f"외래어 기술 용어 {len(USER_WORDS)}개를 Kiwi 사용자 사전(NNP)에 넣고",
            "색인을 다시 만들어 비교한다.",
            "단어 목록은 eval/search_experiments.py의 USER_WORDS.",
            *examples,
        ],
        rows,
        base_ctx,
    )
    write("e3-userdict", text + "\n" + "\n".join(per_query(rows)) + "\n")


def e3_systems(ctx: Context, label: str) -> list[System]:
    return [
        bm25_system(ctx, f"{label}", description=f"{label}, 기준 없음"),
        bm25_system(
            ctx, f"{label}+idf0.5", cutoff=idf_coverage(0.5), description=f"{label}, ③ IDF 일치 50%"
        ),
    ]


# ---------- E6 하이브리드 ----------


def rrf(lists: list[list[Ranked]]) -> list[Ranked]:
    score: dict[str, float] = {}
    for ranked in lists:
        for rank, e in enumerate(ranked, start=1):
            score[e.id] = score.get(e.id, 0) + 1 / (RRF_K + rank)
    return [Ranked(i, s) for i, s in sorted(score.items(), key=lambda kv: -kv[1])]


def e6(ctx: Context, models: list[str], lexical: float, cosines: list[float]) -> None:
    from eval.search_embed import MODELS, EmbeddingIndex

    systems = [
        bm25_system(ctx, "bm25", description="BM25, 기준 없음"),
        bm25_system(
            ctx,
            f"bm25+idf{lexical:g}",
            cutoff=idf_coverage(lexical),
            description=f"BM25, ③ IDF 일치 {lexical:.0%}",
        ),
    ]
    for key in models:
        index = EmbeddingIndex(MODELS[key])
        index.build(ctx.conn)
        systems += hybrid_systems(ctx, index, lexical, cosines)
    rows = run_rows(ctx, systems)
    text = comparison(
        "M5 E6: 하이브리드 검색",
        [
            f"BM25와 임베딩 순위를 RRF(k={RRF_K})로 결합한다. 임베딩 후보는 상위 100건.",
            f"하이브리드 관련도 기준: ③ IDF 일치 {lexical:.0%}를 통과하거나",
            "코사인 유사도가 c 이상인 항목만.",
            "로컬 모델(MiniLM) 결과는 M5에서 잰 기록이다.",
            "로컬 임베딩은 도입하지 않기로 해 코드에서 지웠다.",
        ],
        rows,
        ctx,
    )
    write("e6-hybrid", text + "\n" + "\n".join(per_query(rows)) + "\n")


def hybrid_systems(ctx: Context, index, lexical: float, cosines: list[float]) -> list[System]:
    key = index.spec.key
    lexical_cut = idf_coverage(lexical)

    def emb(x: EvalQuery) -> list[Ranked]:
        allowed = filtered_ids(ctx.conn, x.filters())
        return [Ranked(i, s) for i, s in index.rank(x.query, allowed, 100)]

    def hybrid(x: EvalQuery) -> list[Ranked]:
        return rrf([ctx.bm25(x), emb(x)])

    def hybrid_cut(c: float):
        def rank(x: EvalQuery) -> list[Ranked]:
            passed = {e.id for e in lexical_cut(ctx, x, ctx.bm25(x))}
            passed |= {e.id for e in emb(x) if e.score >= c}
            return [e for e in hybrid(x) if e.id in passed]

        return rank

    systems = [
        System(f"emb-{key}", emb, description=f"임베딩 {index.spec.name} 단독"),
        System(f"hyb-{key}", hybrid, description=f"BM25 + {key} RRF, 기준 없음"),
    ]
    for c in cosines:
        systems.append(
            System(
                f"hyb-{key}+cut{c:g}",
                hybrid_cut(c),
                cutoff=True,
                description=f"BM25 + {key} RRF, ③ IDF {lexical:.0%} 통과 또는 코사인 {c:g} 이상",
            )
        )
    return systems


# ---------- E7 문서 확장 ----------

# 확장 열에 넣을 내용. terms만 넣으면 표기 차이만 메우고, all은 예상 검색어 문장까지 넣는다
EXPANSION_VARIANTS = ("terms", "all")
E7_WEIGHTS = (0.5, 1.0, 2.0)


def expansion_texts(conn: sqlite3.Connection, model: str) -> dict[str, dict[str, str]]:
    """변형 → 항목 ID → 확장 열 텍스트. LLM 생성물은 캐시를 쓴다."""
    from eval.search_embed import embedding_text
    from eval.search_llm import expansions

    inputs = {
        i: embedding_text(json.loads(d)) for i, d in conn.execute("SELECT id, data FROM entries")
    }
    generated = expansions(inputs, model)
    return {
        "none": {},
        "terms": {i: " ".join(e.terms) for i, e in generated.items()},
        "all": {i: "\n".join([*e.queries, " ".join(e.terms)]) for i, e in generated.items()},
    }


def build_expanded(conn: sqlite3.Connection, texts: dict[str, str], path: Path) -> None:
    """확장 열 텍스트를 바꿔 검색 DB를 다시 만든다 (빈 dict면 확장 없음)."""
    cursor = conn.execute("SELECT data FROM entries ORDER BY rowid")
    build([Entry.model_validate(json.loads(d)) for (d,) in cursor], path, texts)


def expanded_contexts(
    conn: sqlite3.Connection, queries: list[EvalQuery], model: str
) -> dict[str, Context]:
    from eval.search_llm import CACHE_DIR

    contexts = {}
    for variant, texts in expansion_texts(conn, model).items():
        path = CACHE_DIR / f"expanded-{variant}.sqlite"
        build_expanded(conn, texts, path)
        contexts[variant] = Context(db.connect(path), queries, expansion=texts)
    return contexts


def e7(ctx: Context, expanded: dict[str, Context], model: str) -> None:
    cuts = {"": None, "+idf0.5": idf_coverage(0.5), "+idf0.4": idf_coverage(0.4)}
    base = expanded["none"]
    rows = run_rows(
        base,
        [
            bm25_system(base, f"base{s}", cutoff=c, description=f"확장 없음{_cut_desc(s)}")
            for s, c in cuts.items()
        ],
    )
    for variant in EXPANSION_VARIANTS:
        ectx = expanded[variant]
        for w in E7_WEIGHTS:
            rows += run_rows(
                ectx,
                [
                    bm25_system(
                        ectx,
                        f"{variant}-w{w:g}{s}",
                        weights={EXPANSION_COLUMN: w},
                        cutoff=c,
                        description=f"확장 {variant}, 가중치 {w:g}{_cut_desc(s)}",
                    )
                    for s, c in cuts.items()
                ],
            )
    text = comparison(
        "M5 E7: 문서 확장",
        [
            f"항목마다 LLM({model})이 만든 예상 검색어 5개와 본문에 없는 다른 표기·동의어를",
            f"`{EXPANSION_COLUMN}` FTS 열로 더해 색인하고 비교한다(doc2query 방식).",
            "LLM 입력은 임베딩과 같은 텍스트(제목 + 요약 + 기술). 발췌는 넣지 않았다.",
            "terms는 다른 표기·동의어만, all은 예상 검색어 문장까지 넣는다.",
            "다른 열 가중치는 현재 서버 그대로. 관련도 기준 ③은 확장 열 토큰도 일치로 센다.",
        ],
        rows,
        ctx,
    )
    selected = [
        r for r in rows if r.system.name in {"base", "base+idf0.5", "all-w2", "all-w2+idf0.5"}
    ]
    examples = _expansion_examples(ctx, expanded["all"])
    write("e7-expansion", text + "\n" + "\n".join(per_query(selected) + ["", *examples]) + "\n")


def _cut_desc(suffix: str) -> str:
    return {"": ", 기준 없음", "+idf0.5": ", ③ IDF 50%", "+idf0.4": ", ③ IDF 40%"}.get(suffix, "")


def _expansion_examples(ctx: Context, ectx: Context, n: int = 5) -> list[str]:
    """정답 항목 몇 개의 확장 결과 예시 (생성물이 엉뚱하지 않은지 눈으로 확인용)."""
    seen: list[str] = []
    for x in ctx.queries:
        for entry_id in sorted(x.relevant)[:1]:
            seen.append(entry_id)
    lines = ["## 확장 예시", "", "질문마다 정답 항목 하나의 확장 열 (앞 5개 질문)", ""]
    for entry_id in seen[:n]:
        row = ectx.conn.execute("SELECT data FROM entries WHERE id = ?", [entry_id]).fetchone()
        title = json.loads(row[0])["post_title"]
        lines.append(f"- {entry_id} {title}")
        lines += [f"  - {t}" for t in ectx.expansion_text.get(entry_id, "").splitlines()]
    return lines


# ---------- E8 질의 재작성 ----------

E8_EXPANSION_WEIGHT = 2.0  # E7에서 가장 나았던 확장 열 가중치


def multi_query_system(
    ctx: Context,
    name: str,
    subqueries: dict[str, list[str]],
    keep_original: bool,
    cutoff: Cutoff | None,
    description: str,
    weights: dict[str, float] | None = None,
) -> System:
    """검색어 여러 개로 각각 검색해 RRF로 합친다. 관련도 기준은 검색어마다 따로 건다."""

    def rank(x: EvalQuery) -> list[Ranked]:
        texts = ([x.query] if keep_original else []) + subqueries[x.id]
        lists = []
        for text in dict.fromkeys(texts):
            sub = x.model_copy(update={"query": text})
            ranked = ctx.bm25(sub, weights)
            lists.append(cutoff(ctx, sub, ranked) if cutoff else ranked)
        return rrf(lists)

    return System(name, rank, cutoff=cutoff is not None, description=description)


def e8(ctx: Context, expanded: Context | None, model: str) -> None:
    from eval.search_llm import rewrites

    rw = rewrites({x.id: x.query for x in ctx.queries}, model)
    cuts = {"": None, "+idf0.5": idf_coverage(0.5), "+idf0.4": idf_coverage(0.4)}
    targets = [("", ctx, None)]
    if expanded is not None:
        targets.append(("exp-", expanded, {EXPANSION_COLUMN: E8_EXPANSION_WEIGHT}))
    rows = []
    for prefix, c, w in targets:
        where = f"확장 all 가중치 {E8_EXPANSION_WEIGHT:g} DB" if prefix else "현재 DB"
        for s, cut in cuts.items():
            rows += run_rows(
                c,
                [
                    bm25_system(
                        c,
                        f"{prefix}orig{s}",
                        weights=w,
                        cutoff=cut,
                        description=f"{where}, 원래 검색어{_cut_desc(s)}",
                    ),
                    multi_query_system(
                        c,
                        f"{prefix}rw{s}",
                        rw,
                        False,
                        cut,
                        f"{where}, 재작성 검색어만 RRF{_cut_desc(s)}",
                        w,
                    ),
                    multi_query_system(
                        c,
                        f"{prefix}orig+rw{s}",
                        rw,
                        True,
                        cut,
                        f"{where}, 원래 + 재작성 검색어 RRF{_cut_desc(s)}",
                        w,
                    ),
                ],
            )
    text = comparison(
        "M5 E8: 질의 재작성",
        [
            "코딩 에이전트가 검색어를 짧게 나눠 여러 번 검색하는 상황을",
            f"LLM({model})으로 흉내 낸다.",
            "재작성 지시문은 eval/search_llm.py의 REWRITE_INSTRUCTIONS.",
            "실제 에이전트는 더 큰 모델이고 대화 맥락이 있어 결과가 다를 수 있다.",
            "검색어마다 BM25 순위(관련도 기준이 있으면 기준 통과분)를 RRF로 합쳐 상위 10건.",
        ],
        rows,
        ctx,
    )
    selected = [r for r in rows if r.system.name in {"orig+idf0.5", "rw+idf0.5", "orig+rw+idf0.5"}]
    listing = ["## 재작성 검색어", "", "| 질문 | 원래 | 재작성 |", "| --- | --- | --- |"]
    listing += [f"| {x.id} | {x.query} | {' / '.join(rw[x.id])} |" for x in ctx.queries]
    write("e8-rewrite", text + "\n" + "\n".join(per_query(selected) + ["", *listing]) + "\n")


# ---------- E9 최종 설정 ----------


def server_system(
    ctx: Context, name: str, rewritten: dict[str, list[str]] | None, keep_original: bool
) -> System:
    """서버 search 함수 그대로. 재작성 검색어가 있으면 검색어마다 서버 결과(최대 10건)를
    받아 RRF로 합친다. 에이전트가 검색을 여러 번 하고 결과를 모아 보는 상황이다."""

    def rank(x: EvalQuery) -> list[Ranked]:
        texts = [x.query] if rewritten is None else rewritten[x.id]
        if rewritten is not None and keep_original:
            texts = [x.query, *texts]
        lists = [
            [Ranked(e["id"], -i) for i, e in enumerate(q.search(ctx.conn, t, x.filters()).entries)]
            for t in dict.fromkeys(texts)
        ]
        return lists[0] if len(lists) == 1 else rrf(lists)

    return System(name, rank, cutoff=True, description="")


def e9(ctx: Context, model: str) -> None:
    from eval.search_llm import rewrites

    rw = rewrites({x.id: x.query for x in ctx.queries}, model)
    systems = [
        server_system(ctx, "server", None, False),
        server_system(ctx, "server+rw", rw, False),
        server_system(ctx, "server+orig+rw", rw, True),
    ]
    systems[0].description = "서버 search 그대로 (원래 검색어 한 번)"
    systems[1].description = "재작성 검색어마다 서버 search, 결과를 RRF로 합쳐 10건"
    systems[2].description = "원래 + 재작성 검색어마다 서버 search, RRF로 합쳐 10건"
    rows = run_rows(ctx, systems)
    text = comparison(
        "M5 E9: 최종 설정",
        [
            "M5 결정을 모두 반영한 서버 검색: 문서 확장(expansion 열, 가중치 2),",
            "형태소 사용자 사전, 관련도 기준(IDF 일치 50%, 기술 별칭은 표준 이름과 한 단위),",
            "최대 10건. 질의 재작성은 E8과 같은 재작성 검색어로",
            "에이전트의 여러 번 검색을 흉내 낸다.",
        ],
        rows,
        ctx,
    )
    write("e9-final", text + "\n" + "\n".join(per_query(rows)) + "\n")


# ---------- 실행 ----------


def main() -> None:
    parser = argparse.ArgumentParser(description="M5 검색 실험")
    parser.add_argument("experiments", nargs="+", choices=[f"e{i}" for i in range(1, 10)])
    parser.add_argument("--db", type=Path)
    parser.add_argument("--group", choices=["max", "sum2"], help="E5에서 글 묶기를 함께 적용")
    parser.add_argument("--models", default="openai-small,openai-large")
    parser.add_argument("--lexical", type=float, default=0.5, help="E6 하이브리드의 IDF 일치 기준")
    parser.add_argument("--cosines", default="0.5,0.6,0.7")
    parser.add_argument("--llm", default="gpt-5.6-luna", help="E7·E8 생성 모델")
    args = parser.parse_args()

    conn = db.connect(args.db)
    queries = load_queries()
    ctx = Context(conn, queries)
    for exp in args.experiments:
        if exp == "e1":
            e1(ctx)
        elif exp == "e2":
            e2(ctx)
        elif exp == "e3":
            e3(conn, queries)
        elif exp == "e4":
            e4(ctx)
        elif exp == "e5":
            e5(ctx, args.group)
        elif exp == "e6":
            e6(
                ctx,
                args.models.split(","),
                args.lexical,
                [float(c) for c in args.cosines.split(",")],
            )
    if "e9" in args.experiments:
        e9(ctx, args.llm)
    if {"e7", "e8"} & set(args.experiments):
        expanded = expanded_contexts(conn, queries, args.llm)
        if "e7" in args.experiments:
            e7(ctx, expanded, args.llm)
        if "e8" in args.experiments:
            e8(ctx, expanded["all"], args.llm)


if __name__ == "__main__":
    main()
