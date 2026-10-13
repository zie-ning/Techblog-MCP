"""M10 검색 개편 실험 R1: 리랭커로 "관련 / 결과 없음"을 판정할 수 있는지 확인한다.

    uv run python eval/search_rerank.py            # 리포트: eval/reports/m10-r1-rerank.md

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


RERANKERS = [
    RerankerSpec("cohere-v4-pro", "cohere", "rerank-v4.0-pro"),
    RerankerSpec("cohere-v4-fast", "cohere", "rerank-v4.0-fast"),
    RerankerSpec("voyage-3", "voyage", "rerank-3"),
]


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


def score_all(ctx: Context, rerankers: list[Reranker]) -> list[Scored]:
    index = EmbeddingIndex(MODELS["openai-large"])
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
        scored.append(s)
        print(f"{x.id} 후보 {len(ids)}건")
    return scored


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
        "최적 기준선은 두 종류를 함께 가장 많이 맞히는 값이다 (같은 30개로 고른 값이라 낙관적).",
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
    args = parser.parse_args()
    chosen = args.models.split(",")

    _load_env()
    conn = db.connect(ROOT / "data" / "techblog.sqlite")
    ctx = Context(conn, load_queries())
    rerankers = [Reranker(spec) for spec in RERANKERS if spec.key in chosen]
    scored_list = score_all(ctx, rerankers)
    scored = {s.query.id: s for s in scored_list}
    keys = ["cosine", *(r.spec.key for r in rerankers)]

    systems = [server_system(ctx, "server", None, False), rrf_system(scored)]
    systems[0].description = "현재 서버 search (BM25 + IDF 일치 50%)"
    for k in keys:
        systems.append(gated_system(scored, k, None))
    for k in keys:
        systems.append(gated_system(scored, k, best_separation(scored_list, k).threshold))
    rows = run_rows(ctx, systems)

    text = comparison(
        "M10 R1: 리랭커 판정 가능성",
        [
            f"후보: 질문마다 BM25(서버 가중치)와 OpenAI large 임베딩 상위 {CANDIDATES}건씩을",
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
        tradeoff_section(ctx, scored, keys),
        latency_section(rerankers, scored_list, entry_texts(ctx)),
        per_query(rows),
    ]
    text += "\n" + "\n\n".join("\n".join(s) for s in sections) + "\n"
    REPORTS.mkdir(parents=True, exist_ok=True)
    path = REPORTS / "m10-r1-rerank.md"
    path.write_text(text, encoding="utf-8")
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
