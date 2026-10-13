"""M10 검색 개편 실험: 리랭커로 "관련 / 결과 없음"을 판정할 수 있는지 확인하고 모델을 비교한다.

    uv run python eval/search_rerank.py --models cohere-v4-pro,cohere-v4-fast,voyage-3 \
        --report m10-r1-rerank --latency                       # R1 (M5 평가셋 30개 때 실행)
    uv run python eval/search_rerank.py                        # R2: 리랭커 비교 (보강 평가셋)
    uv run python eval/search_rerank.py --embeddings           # R3: 임베딩 비교

후보는 질문마다 BM25(서버 가중치, 필터 적용)와 OpenAI large 임베딩의 상위 50건을 RRF로 합친
상위 50건이다. 리랭커 API(Cohere, Voyage)로 후보마다 점수를 매기고 세 가지를 본다.

1. 질문별 1위 점수: 정답이 있는 질문과 없는 주제 질문이 기준선 하나로 갈리는가
2. 후보별 점수와 판정 라벨의 일치(AUC): 관련 항목이 무관 항목보다 높은 점수를 받는가
3. 리랭커 순위 + 기준선을 서버 search로 쓴다고 보고 M5와 같은 지표

API 키는 환경 변수(COHERE_API_KEY, VOYAGE_API_KEY, OPENAI_API_KEY)나 저장소 .env에서 읽는다.
점수는 eval/search/rerank_cache/(git 제외)에 캐시해 같은 질문·항목 텍스트는 다시 부르지 않는다.
실험 설계와 결과 해석은 docs/milestones/M10.md.
"""

import hashlib
import json
import os
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eval.search_embed import MODELS, EmbeddingIndex, embedding_text  # noqa: E402
from eval.search_eval import (  # noqa: E402
    MAX_RESULTS,
    REPORTS,
    EvalQuery,
    Ranked,
    System,
    bm25_ranking,
    evaluate_query,
    filtered_ids,
    load_queries,
)
from eval.search_experiments import (  # noqa: E402
    Context,
    comparison,
    per_query,
    rrf,
    run_rows,
    server_system,
)
from techblog_mcp import db  # noqa: E402
from techblog_mcp.search.schema import FTS_COLUMNS  # noqa: E402

CANDIDATES = 50  # 리랭커에 넘기는 후보 수 (BM25·임베딩 각 50건을 RRF로 합친 상위)
CACHE_DIR = ROOT / "eval" / "search" / "rerank_cache"
LATENCY_SAMPLES = 5  # 응답 시간을 잴 때 다시 부르는 질문 수
THRESHOLDS = [round(0.05 * i, 2) for i in range(1, 20)]  # 기준선 후보 0.05~0.95


@dataclass(frozen=True)
class RerankerSpec:
    key: str  # 캐시 파일·리포트에 쓰는 짧은 이름
    provider: str  # cohere / voyage
    model: str
    instruction: str = ""  # 검색어 앞에 붙이는 지시문 (Voyage는 검색어로 지시를 받는다)


RERANKERS = [
    RerankerSpec("cohere-v4-pro", "cohere", "rerank-v4.0-pro"),
    RerankerSpec("cohere-v4-fast", "cohere", "rerank-v4.0-fast"),
    RerankerSpec("voyage-3", "voyage", "rerank-3"),
    RerankerSpec(
        "voyage-3-inst",
        "voyage",
        "rerank-3",
        "검색어의 모든 조건(대상 기술·시스템·문제)을 직접 다룬 글만 관련 있다."
        " 주제가 비슷해도 핵심 조건이 다르면 관련 없다.",
    ),
]
# 두 리랭커 점수의 평균. 서로 다른 질문에서 틀려(R1) 함께 쓰면 나아지는지 본다
COMBO = ("combo", "cohere-v4-pro", "voyage-3")
TAG_GROUPS = ["기존", "표현 차이", "짧은 검색어", "근접 주제"]


def _load_env() -> None:
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")


def _hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


class Reranker:
    """리랭커 API 호출과 점수 캐시. 캐시 키는 (검색어, 항목 텍스트)의 해시다."""

    def __init__(self, spec: RerankerSpec):
        self.spec = spec
        self._path = CACHE_DIR / f"{spec.key}.json"
        self._cache: dict[str, float] = (
            json.loads(self._path.read_text(encoding="utf-8")) if self._path.exists() else {}
        )
        self.latencies: list[float] = []  # 실제로 부른 호출의 응답 시간(초)

    def scores(self, query: str, texts: list[str]) -> list[float]:
        keys = [_hash(f"{query}\0{t}") for t in texts]
        todo = [i for i, k in enumerate(keys) if k not in self._cache]
        if todo:
            fresh = self._call(query, [texts[i] for i in todo])
            for i, score in zip(todo, fresh, strict=True):
                self._cache[keys[i]] = score
            CACHE_DIR.mkdir(parents=True, exist_ok=True)
            self._path.write_text(json.dumps(self._cache), encoding="utf-8")
        return [self._cache[k] for k in keys]

    def _call(self, query: str, texts: list[str]) -> list[float]:
        if self.spec.instruction:
            query = f"{self.spec.instruction}\n검색어: {query}"
        if self.spec.provider == "cohere":
            url = "https://api.cohere.com/v2/rerank"
            key = os.environ["COHERE_API_KEY"]
            body = {"model": self.spec.model, "query": query, "documents": texts}
        else:
            url = "https://api.voyageai.com/v1/rerank"
            key = os.environ["VOYAGE_API_KEY"]
            body = {"model": self.spec.model, "query": query, "documents": texts}
        for attempt in range(8):
            start = time.perf_counter()
            try:
                response = httpx.post(
                    url, headers={"Authorization": f"Bearer {key}"}, json=body, timeout=120
                )
            except httpx.TransportError:
                # 연결이 끊기는 일시적 오류. 잠시 뒤 다시 부른다
                time.sleep(5 * (attempt + 1))
                continue
            if response.status_code == 429 or response.status_code >= 500:
                # 체험 키의 분당 호출 제한. 기다렸다가 다시 부른다
                time.sleep(10 * (attempt + 1))
                continue
            response.raise_for_status()
            self.latencies.append(time.perf_counter() - start)
            data = response.json()
            results = data["results"] if self.spec.provider == "cohere" else data["data"]
            scores = [0.0] * len(texts)
            for r in results:
                scores[r["index"]] = r["relevance_score"]
            return scores
        raise RuntimeError(f"{self.spec.key}: 호출 제한·연결 오류로 계속 실패")


# ---------- 후보와 점수 ----------


@dataclass
class Scored:
    """한 질문의 후보(RRF 순)와 설정별 점수."""

    query: EvalQuery
    ids: list[str]
    scores: dict[str, list[float]] = field(default_factory=dict)  # 설정 → 후보별 점수

    def ranked(self, key: str) -> list[Ranked]:
        pairs = sorted(zip(self.ids, self.scores[key], strict=True), key=lambda p: -p[1])
        return [Ranked(i, s) for i, s in pairs]

    def top1(self, key: str) -> float:
        return max(self.scores[key]) if self.ids else 0.0


def candidates(ctx: Context, index: EmbeddingIndex, x: EvalQuery) -> tuple[list[str], dict]:
    """(RRF 상위 후보 ID, 후보별 코사인)."""
    lexical = bm25_ranking(ctx.conn, x.query, x.filters(), FTS_COLUMNS, depth=CANDIDATES)
    semantic = [
        Ranked(i, s)
        for i, s in index.rank(x.query, filtered_ids(ctx.conn, x.filters()), CANDIDATES)
    ]
    ids = [r.id for r in rrf([lexical, semantic])[:CANDIDATES]]
    query_vector = index.query_vector(x.query)
    row = {entry_id: n for n, entry_id in enumerate(index.ids)}
    cosine = {i: float(index.vectors[row[i]] @ query_vector) for i in ids}
    return ids, cosine


def entry_texts(ctx: Context) -> dict[str, str]:
    """항목 ID → 리랭커에 넣는 텍스트 (임베딩 입력과 같다)."""
    return {
        r[0]: embedding_text(json.loads(r[1]))
        for r in ctx.conn.execute("SELECT id, data FROM entries")
    }


def score_all(
    ctx: Context, rerankers: list[Reranker], embedding: str = "openai-large"
) -> list[Scored]:
    index = EmbeddingIndex(MODELS[embedding])
    fresh = index.build(ctx.conn)
    if fresh:
        print(f"임베딩 새로 계산: {fresh}건")
    texts = entry_texts(ctx)
    scored = []
    for x in ctx.queries:
        ids, cosine = candidates(ctx, index, x)
        s = Scored(x, ids, {"cosine": [cosine[i] for i in ids]})
        for reranker in rerankers:
            s.scores[reranker.spec.key] = reranker.scores(x.query, [texts[i] for i in ids])
        name, a, b = COMBO
        if a in s.scores and b in s.scores:
            s.scores[name] = [(u + v) / 2 for u, v in zip(s.scores[a], s.scores[b], strict=True)]
        scored.append(s)
        print(f"{x.id} 후보 {len(ids)}건")
    return scored


# ---------- 판정 풀 ----------

POOL_DEPTH = 15  # 판정 풀에 넣는 설정별 상위 건수


def judge_pool(ctx: Context, scored: list[Scored]) -> list[dict]:
    """판정할 후보: 질문마다 BM25·코사인·RRF·리랭커별 상위 POOL_DEPTH건 중 미판정 항목."""
    lists = {}
    for s in scored:
        x = s.query
        lexical = bm25_ranking(ctx.conn, x.query, x.filters(), FTS_COLUMNS, depth=POOL_DEPTH)
        lists[x.id] = [[r.id for r in lexical], s.ids[:POOL_DEPTH]]
        lists[x.id] += [[r.id for r in s.ranked(k)[:POOL_DEPTH]] for k in s.scores]
    return pool_items(ctx, lists)


def embedding_pool(ctx: Context) -> list[dict]:
    """임베딩 모델별 단독 순위와 BM25 + 임베딩 RRF 순위의 상위 POOL_DEPTH건 중 미판정 항목 (R3)."""
    lists: dict[str, list[list[str]]] = {x.id: [] for x in ctx.queries}
    for spec in MODELS.values():
        index = EmbeddingIndex(spec)
        index.build(ctx.conn)
        for x in ctx.queries:
            allowed = filtered_ids(ctx.conn, x.filters())
            emb = [Ranked(i, s) for i, s in index.rank(x.query, allowed, CANDIDATES)]
            lexical = bm25_ranking(ctx.conn, x.query, x.filters(), FTS_COLUMNS, depth=CANDIDATES)
            lists[x.id].append([r.id for r in emb[:POOL_DEPTH]])
            lists[x.id].append([r.id for r in rrf([lexical, emb])[:POOL_DEPTH]])
    return pool_items(ctx, lists)


def pool_items(ctx: Context, lists: dict[str, list[list[str]]]) -> list[dict]:
    """질문별 순위 목록들에서 미판정 항목을 모은다.

    판정하는 사람(Claude)이 읽을 수 있게 항목의 제목과 요약 필드를 함께 담는다.
    """
    data = {r[0]: json.loads(r[1]) for r in ctx.conn.execute("SELECT id, data FROM entries")}
    out = []
    for x in ctx.queries:
        ids = (i for ranked in lists.get(x.id, []) for i in ranked)
        found = [i for i in dict.fromkeys(ids) if x.grade(i) is None]
        if not found:
            continue
        items = []
        for entry_id in found:
            e = data[entry_id]
            items.append(
                {
                    "id": entry_id,
                    "company": e["company"],
                    "title": e["post_title"],
                    "problem": [p["text"] for p in e["problem_situation"]],
                    "solution": [p["text"] for p in e["solution"]],
                    "ops": [p["text"] for p in e["performance_ops"]],
                    "technologies": e["technologies"],
                }
            )
        out.append(
            {"id": x.id, "query": x.query, "source": x.source, "note": x.note, "items": items}
        )
    return out


# ---------- 분석 ----------


def auc(positive: list[float], negative: list[float]) -> float | None:
    """관련 항목 점수가 무관 항목 점수보다 높을 확률 (동점은 0.5)."""
    if not positive or not negative:
        return None
    wins = sum((p > n) + 0.5 * (p == n) for p in positive for n in negative)
    return wins / (len(positive) * len(negative))


def grade_scores(scored: list[Scored], key: str) -> dict[str, list[float]]:
    """판정 라벨별 후보 점수. 질문마다 그 질문의 라벨로 나눈다 (미판정은 뺀다)."""
    out: dict[str, list[float]] = {"관련": [], "일부 관련": [], "무관": []}
    for s in scored:
        for entry_id, score in zip(s.ids, s.scores[key], strict=True):
            grade = s.query.grade(entry_id)
            if grade is not None:
                out[grade].append(score)
    return out


@dataclass
class Separation:
    threshold: float  # 1위 점수가 이 값 이상이면 결과를 돌려준다
    answered: int  # 정답 있는 질문 중 결과를 돌려준 수
    absent_empty: int  # 없는 주제 질문 중 결과 없음으로 판정한 수


def separations(scored: list[Scored], key: str) -> list[Separation]:
    """1위 점수를 기준선으로 쓸 때, 후보 기준선마다 두 종류 질문을 얼마나 맞히는지.

    기준선 후보는 질문들의 1위 점수 사이 중간값이다 (점수 척도가 모델마다 달라서).
    """
    tops = sorted({s.top1(key) for s in scored})
    cuts = [tops[0] - 1e-9] + [(a + b) / 2 for a, b in zip(tops, tops[1:], strict=False)]
    cuts.append(tops[-1] + 1e-9)
    out = []
    for t in cuts:
        answered = sum(1 for s in scored if s.query.relevant and s.top1(key) >= t)
        empty = sum(1 for s in scored if s.query.source == "없는 주제" and s.top1(key) < t)
        out.append(Separation(t, answered, empty))
    return out


def best_separation(scored: list[Scored], key: str) -> Separation:
    return max(separations(scored, key), key=lambda s: (s.answered + s.absent_empty, -s.threshold))


def gated_system(scored: dict[str, Scored], key: str, threshold: float | None) -> System:
    """리랭커 순위로 정렬하고 점수가 기준선 이상인 후보만 최대 10건 돌려주는 서버 흉내."""

    def rank(x: EvalQuery) -> list[Ranked]:
        ranked = scored[x.id].ranked(key)
        if threshold is not None:
            ranked = [r for r in ranked if r.score >= threshold]
        return ranked[:MAX_RESULTS]

    name = key if threshold is None else f"{key}≥{threshold:.2f}"
    desc = f"후보 50건을 {key} 점수 순으로" + (
        "" if threshold is None else f", 점수 {threshold:.2f} 이상만"
    )
    return System(name, rank, cutoff=threshold is not None, description=desc)


def rrf_system(scored: dict[str, Scored]) -> System:
    return System(
        "rrf",
        lambda x: [Ranked(i, -n) for n, i in enumerate(scored[x.id].ids)][:MAX_RESULTS],
        description="BM25 + OpenAI large RRF 상위 10건, 기준 없음 (리랭커 입력 순서)",
    )


# ---------- 리포트 ----------


def _fmt(v: float | None, digits: int = 3) -> str:
    return "-" if v is None else f"{v:.{digits}f}"


def top1_table(scored: list[Scored], keys: list[str]) -> list[str]:
    lines = [
        "## 질문별 1위 점수",
        "",
        "✅ 정답 있는 질문, ❌ 없는 주제 질문.",
        "점수 척도는 모델마다 다르므로 열끼리 비교하지 않는다.",
        "",
        "| 질문 | 구분 | " + " | ".join(keys) + " |",
        "| --- | --- |" + " --- |" * len(keys),
    ]
    for s in scored:
        mark = "❌" if s.query.source == "없는 주제" else "✅"
        cells = " | ".join(f"{s.top1(k):.3f}" for k in keys)
        lines.append(f"| {s.query.id} {s.query.query[:26]} | {mark} | {cells} |")
    return lines


def overlap_section(scored: list[Scored], keys: list[str]) -> list[str]:
    answerable = [s for s in scored if s.query.relevant]
    absent = [s for s in scored if s.query.source == "없는 주제"]
    lines = [
        "## 1위 점수로 가르기",
        "",
        f"정답 있는 질문 {len(answerable)}개, 없는 주제 질문 {len(absent)}개.",
        "'겹침'은 없는 주제 질문의 1위 점수 중 가장 높은 값보다 낮은 정답 있는 질문 수다.",
        "최적 기준선은 두 종류를 함께 가장 많이 맞히는 값이다",
        "(같은 평가셋으로 고른 값이라 낙관적).",
        "",
        "| 설정 | 정답 있는 질문 최저 | 없는 주제 최고 | 겹침 | 최적 기준선"
        " | 결과 돌려줌 | 결과 없음 |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for k in keys:
        low = min(s.top1(k) for s in answerable)
        high = max(s.top1(k) for s in absent)
        overlap = sum(1 for s in answerable if s.top1(k) <= high)
        best = best_separation(scored, k)
        lines.append(
            f"| {k} | {low:.3f} | {high:.3f} | {overlap} | {best.threshold:.3f}"
            f" | {best.answered}/{len(answerable)} | {best.absent_empty}/{len(absent)} |"
        )
    return lines


def auc_section(scored: list[Scored], keys: list[str]) -> list[str]:
    lines = [
        "## 후보 점수와 판정 라벨",
        "",
        "모든 질문의 후보를 한데 모아 잰다 (기준선 하나가 질문을 가리지 않고 통하는지 보려고).",
        "AUC는 관련 항목이 무관 항목보다 높은 점수를 받을 확률이다 (0.5는 무작위, 1.0은 완벽).",
        "",
        "| 설정 | AUC 관련 vs 무관 | AUC 관련·일부 vs 무관 | 평균 관련 | 평균 일부 | 평균 무관 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for k in keys:
        g = grade_scores(scored, k)
        mean = {name: sum(v) / len(v) if v else None for name, v in g.items()}
        lines.append(
            f"| {k} | {_fmt(auc(g['관련'], g['무관']))}"
            f" | {_fmt(auc(g['관련'] + g['일부 관련'], g['무관']))}"
            f" | {_fmt(mean['관련'])} | {_fmt(mean['일부 관련'])} | {_fmt(mean['무관'])} |"
        )
    counts = grade_scores(scored, keys[0])
    unjudged = sum(len(s.ids) for s in scored) - sum(len(v) for v in counts.values())
    lines += [
        "",
        f"후보 {sum(len(s.ids) for s in scored)}건: 관련 {len(counts['관련'])}"
        f" · 일부 관련 {len(counts['일부 관련'])} · 무관 {len(counts['무관'])}"
        f" · 미판정 {unjudged}",
    ]
    return lines


def tradeoff_section(ctx: Context, scored: dict[str, Scored], keys: list[str]) -> list[str]:
    """기준선을 바꿔 가며 Recall@5와 결과 없음 판정의 맞교환을 본다."""
    from eval.search_eval import summarize

    lines = [
        "## 기준선별 맞교환",
        "",
        "리랭커 순위로 정렬하고 점수가 기준선 이상인 항목만 최대 10건 돌려줄 때.",
        "",
    ]
    for k in keys:
        lines += [
            f"### {k}",
            "",
            "| 기준선 | Recall@5 | MRR | 결과 없음 | 평균 결과 수 | 무관 비율 | 미판정 |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
        for t in THRESHOLDS:
            (row,) = run_rows(ctx, [gated_system(scored, k, t)])
            m = summarize(row.results)
            lines.append(
                f"| {t:.2f} | {_fmt(m.recall5)} | {_fmt(m.mrr)} | {m.no_result_rate:.0%}"
                f" | {m.avg_returned:.1f} | {_fmt(m.noise_rate, 2)} | {m.unjudged} |"
            )
        lines.append("")
    return lines


ITEM_THRESHOLDS = [0.1, 0.3, 0.5, 0.6, 0.7]  # 2단 판정의 항목 기준선 후보


def two_level_system(scored: dict[str, Scored], key: str, gate: float, item: float) -> System:
    """2단 판정: 1위 점수가 gate 이상이면 결과 있음, 그때 점수가 item 이상인 항목을 최대 10건."""

    def rank(x: EvalQuery) -> list[Ranked]:
        s = scored[x.id]
        if s.top1(key) < gate:
            return []
        return [r for r in s.ranked(key) if r.score >= item][:MAX_RESULTS]

    return System(
        f"{key} 1위≥{gate:.2f}·항목≥{item:.2f}",
        rank,
        cutoff=True,
        description=f"1위 점수 {gate:.2f} 이상이면 결과 있음, 점수 {item:.2f} 이상 항목만",
    )


def two_level_section(ctx: Context, scored: dict[str, Scored], keys: list[str]) -> list[str]:
    """1위 기준선은 '1위 점수로 가르기'의 최적값으로 고정하고 항목 기준선을 바꿔 본다."""
    from eval.search_eval import summarize

    scored_list = list(scored.values())
    lines = [
        "## 2단 판정",
        "",
        "항목마다 기준선을 적용하면 결과 없음 판정을 위해 기준선을 올릴 때",
        "정답 항목도 함께 잘린다.",
        "2단 판정은 1위 점수로 결과 있음/없음만 정하고(1위 기준선 = 최적 기준선),",
        "결과가 있으면 더 낮은 항목 기준선으로 보여 줄 항목을 고른다.",
        "",
        "| 설정 | 항목 기준선 | Recall@5 | MRR | 결과 없음 | 평균 결과 수 | 무관 비율 | 미판정 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for k in keys:
        if k == "cosine":
            continue
        gate = best_separation(scored_list, k).threshold
        for item in [t for t in ITEM_THRESHOLDS if t <= gate]:
            (row,) = run_rows(ctx, [two_level_system(scored, k, gate, item)])
            m = summarize(row.results)
            lines.append(
                f"| {k} (1위 ≥ {gate:.2f}) | {item:.2f} | {_fmt(m.recall5)} | {_fmt(m.mrr)}"
                f" | {m.no_result_rate:.0%} | {m.avg_returned:.1f} | {_fmt(m.noise_rate, 2)}"
                f" | {m.unjudged} |"
            )
    return lines


def tag_of(x: EvalQuery) -> str:
    return x.tags[0] if x.tags else "기존"


def tag_section(ctx: Context, systems: list[System]) -> list[str]:
    """질문 성격별 지표. 근접 주제는 결과 없음 판정만, 나머지는 Recall@5·MRR을 본다."""
    from eval.search_eval import summarize

    lines = [
        "## 질문 성격별",
        "",
        "기존은 M5 평가셋 30개(정답 있는 25개 + 없는 주제 5개), 나머지는 M10 보강 질문이다.",
        "칸은 정답 있는 질문의 Recall@5 / MRR, 없는 주제 질문의 결과 없음 비율이다.",
        "",
        "| 설정 | " + " | ".join(TAG_GROUPS) + " |",
        "| --- |" + " --- |" * len(TAG_GROUPS),
    ]
    for system in systems:
        cells = []
        for tag in TAG_GROUPS:
            group = [x for x in ctx.queries if tag_of(x) == tag]
            m = summarize([evaluate_query(x, system.rank(x), ctx.post_of) for x in group])
            parts = []
            if m.recall5 is not None:
                parts.append(f"{m.recall5:.3f} / {m.mrr:.3f}")
            if m.no_result_rate is not None:
                parts.append(f"결과 없음 {m.no_result_rate:.0%}")
            cells.append(" · ".join(parts))
        lines.append(f"| {system.name} | " + " | ".join(cells) + " |")
    return lines


def candidate_recall(ctx: Context, ids_of: dict[str, list[str]], depth: int) -> float:
    """정답 있는 질문에서 정답이 상위 depth건 후보 안에 든 비율의 평균 (리랭커가 볼 수 있는 상한)

    리랭커는 후보 밖의 정답을 올릴 수 없다.
    """
    values = []
    for x in ctx.queries:
        if x.relevant:
            found = len(set(ids_of[x.id][:depth]) & x.relevant)
            values.append(found / len(x.relevant))
    return sum(values) / len(values)


def embeddings_report(ctx: Context) -> str:
    """임베딩 모델별 후보 찾기 성능. 리랭커 없이 잰다 (R3)."""
    from eval.search_eval import summarize

    lines = [
        "# M10 R3: 임베딩 모델 비교 (후보 찾기)",
        "",
        "리랭커 없이 임베딩 단독 순위와 BM25 + 임베딩 RRF 순위를 잰다. 관련도 기준은 없다.",
        f"후보 재현율 @{CANDIDATES}은 RRF 상위 {CANDIDATES}건(리랭커에 넘기는 후보) 안에 든",
        "정답 비율의 평균으로, 리랭커가 아무리 좋아도 넘을 수 없는 상한이다.",
        "판정 풀은 OpenAI large 후보로 만들어 다른 모델이 올린 미판정 항목은 정답으로 세지 않는다.",
        "미판정은 결과 상위 10건 중 판정하지 않은 항목 수다(많을수록 그 모델이 불리하게 잰 값).",
        "",
        "| 모델 | 차원 | 단독 R@5 | 단독 MRR | RRF R@5 | RRF MRR | RRF R@10"
        f" | 후보 재현율 @{CANDIDATES} | 표현 차이 RRF R@5 | 짧은 검색어 RRF R@5"
        " | 미판정 (단독 · RRF) |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    bm25 = {
        x.id: bm25_ranking(ctx.conn, x.query, x.filters(), FTS_COLUMNS, depth=CANDIDATES)
        for x in ctx.queries
    }
    for key, spec in MODELS.items():
        index = EmbeddingIndex(spec)
        index.build(ctx.conn)
        emb = {
            x.id: [
                Ranked(i, s)
                for i, s in index.rank(x.query, filtered_ids(ctx.conn, x.filters()), CANDIDATES)
            ]
            for x in ctx.queries
        }
        fused = {qid: rrf([bm25[qid], emb[qid]])[:CANDIDATES] for qid in emb}
        alone = summarize([evaluate_query(x, emb[x.id], ctx.post_of) for x in ctx.queries])
        hybrid = summarize([evaluate_query(x, fused[x.id], ctx.post_of) for x in ctx.queries])
        by_tag = {}
        for tag in ("표현 차이", "짧은 검색어"):
            group = [x for x in ctx.queries if tag_of(x) == tag]
            by_tag[tag] = summarize([evaluate_query(x, fused[x.id], ctx.post_of) for x in group])
        ids_of = {q: [r.id for r in v] for q, v in fused.items()}
        recall = candidate_recall(ctx, ids_of, CANDIDATES)
        lines.append(
            f"| {key} ({spec.name}) | {index.vectors.shape[1]} | {_fmt(alone.recall5)}"
            f" | {_fmt(alone.mrr)} | {_fmt(hybrid.recall5)} | {_fmt(hybrid.mrr)}"
            f" | {_fmt(hybrid.recall10)} | {recall:.3f} | {_fmt(by_tag['표현 차이'].recall5)}"
            f" | {_fmt(by_tag['짧은 검색어'].recall5)} | {alone.unjudged} · {hybrid.unjudged} |"
        )
        print(key, flush=True)
    bm = summarize([evaluate_query(x, bm25[x.id], ctx.post_of) for x in ctx.queries])
    recall = candidate_recall(ctx, {q: [r.id for r in v] for q, v in bm25.items()}, CANDIDATES)
    lines.append(
        f"| BM25만 (비교) | - | {_fmt(bm.recall5)} | {_fmt(bm.mrr)}"
        f" | - | - | - | {recall:.3f} | - | - | {bm.unjudged} · - |"
    )
    return "\n".join(lines) + "\n"


def latency_section(rerankers: list[Reranker], scored: list[Scored], texts: dict) -> list[str]:
    """앞쪽 질문 LATENCY_SAMPLES개를 캐시 없이 다시 불러 응답 시간을 잰다 (후보 50건 한 번)."""
    lines = [
        "## 응답 시간",
        "",
        f"질문 {LATENCY_SAMPLES}개를 캐시 없이 다시 불러 잰 값이다"
        f" (후보 {CANDIDATES}건을 한 번에).",
        "네트워크 왕복이 포함되고 체험 키 기준이다.",
        "",
        "| 설정 | 평균(초) | 최대(초) |",
        "| --- | --- | --- |",
    ]
    for r in rerankers:
        r.latencies.clear()
        for s in scored[:LATENCY_SAMPLES]:
            r._call(s.query.query, [texts[i] for i in s.ids])
        avg = sum(r.latencies) / len(r.latencies)
        lines.append(f"| {r.spec.key} | {avg:.2f} | {max(r.latencies):.2f} |")
    return lines


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="M10 R1 리랭커 판정 가능성")
    parser.add_argument(
        "--models", default=",".join(s.key for s in RERANKERS), help="쉼표로 구분한 리랭커 키"
    )
    parser.add_argument("--pool", type=Path, help="평가 대신 판정할 후보 풀을 JSON으로 쓴다")
    parser.add_argument("--report", default="m10-r2-rerankers", help="리포트 파일 이름")
    parser.add_argument("--embedding", default="openai-large", help="후보를 찾는 임베딩 모델")
    parser.add_argument("--embeddings", action="store_true", help="임베딩 모델 비교 (R3)")
    parser.add_argument("--latency", action="store_true", help="응답 시간을 다시 잰다")
    args = parser.parse_args()
    chosen = args.models.split(",")

    _load_env()
    conn = db.connect(ROOT / "data" / "techblog.sqlite")
    ctx = Context(conn, load_queries())
    if args.embeddings and args.pool:
        pool = embedding_pool(ctx)
        args.pool.write_text(json.dumps(pool, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{args.pool}: 질문 {len(pool)}개, 항목 {sum(len(p['items']) for p in pool)}건")
        return
    if args.embeddings:
        path = REPORTS / "m10-r3-embeddings.md"
        path.write_text(embeddings_report(ctx), encoding="utf-8")
        print(path.relative_to(ROOT))
        return
    rerankers = [Reranker(spec) for spec in RERANKERS if spec.key in chosen]
    scored_list = score_all(ctx, rerankers, args.embedding)
    scored = {s.query.id: s for s in scored_list}
    keys = ["cosine", *(r.spec.key for r in rerankers)]
    if COMBO[0] in scored_list[0].scores:
        keys.append(COMBO[0])
    if args.pool:
        pool = judge_pool(ctx, scored_list)
        args.pool.write_text(json.dumps(pool, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{args.pool}: 질문 {len(pool)}개, 항목 {sum(len(p['items']) for p in pool)}건")
        return

    systems = [server_system(ctx, "server", None, False), rrf_system(scored)]
    systems[0].description = "현재 서버 search (BM25 + IDF 일치 50%)"
    for k in keys:
        systems.append(gated_system(scored, k, None))
    for k in keys:
        systems.append(gated_system(scored, k, best_separation(scored_list, k).threshold))
    rows = run_rows(ctx, systems)

    text = comparison(
        f"M10 리랭커 판정 ({args.report})",
        [
            f"후보: 질문마다 BM25(서버 가중치)와 {args.embedding} 임베딩 상위 {CANDIDATES}건씩을",
            f"RRF로 합친 상위 {CANDIDATES}건. 리랭커에는 항목의 제목 + 문제 상황 + 해결 방법",
            "+ 성능·운영 + 기술(임베딩 입력과 같은 텍스트)을 넣는다.",
            "'≥' 설정의 기준선은 아래 '1위 점수로 가르기'의 최적 기준선이다.",
        ],
        rows,
        ctx,
    )
    sections = [
        overlap_section(scored_list, keys),
        auc_section(scored_list, keys),
        top1_table(scored_list, keys),
        tag_section(ctx, systems),
        two_level_section(ctx, scored, keys),
        tradeoff_section(ctx, scored, keys),
        *([latency_section(rerankers, scored_list, entry_texts(ctx))] if args.latency else []),
        per_query(rows),
    ]
    text += "\n" + "\n\n".join("\n".join(s) for s in sections) + "\n"
    REPORTS.mkdir(parents=True, exist_ok=True)
    path = REPORTS / f"{args.report}.md"
    path.write_text(text, encoding="utf-8")
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
