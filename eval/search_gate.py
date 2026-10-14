"""M10 4단계 R4: 판정 방식 확정을 위한 분석 (voyage-4-large 후보 + Voyage rerank-3).

    uv run python eval/search_gate.py        # 리포트: eval/reports/m10-r4-gate.md

2단 판정(1위 리랭커 점수로 결과 있음/없음을 정하고, 보여 줄 항목은 따로 고른다)의 두 부분을 본다.

1. 결과 유무 기준선: 기준선별로 정답 있는 질문·없는 주제를 몇 개 맞히는지, 그리고 같은 평가셋으로
   고른 기준선이 새 질문에도 통하는지(질문 하나를 빼고 나머지로 기준선을 골라 뺀 질문을 맞히는지)
2. 항목 고르기: 절대 기준선, 1위 대비 비율, 1위와의 점수 차 중 무엇이 재현율과 무관 카드를
   잘 절충하는지

검색 한 번의 응답 시간(검색어 임베딩 + 리랭커 호출)도 잰다. 설계는 docs/milestones/M10.md.
"""

import statistics
import sys
import time
from collections.abc import Callable
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eval.search_embed import MODELS, EmbeddingIndex, make_embedder  # noqa: E402
from eval.search_eval import (  # noqa: E402
    MAX_RESULTS,
    REPORTS,
    EvalQuery,
    Ranked,
    System,
    load_queries,
    summarize,
)
from eval.search_experiments import Context, run_rows  # noqa: E402
from eval.search_rerank import (  # noqa: E402
    RERANKERS,
    Reranker,
    Scored,
    _fmt,
    _load_env,
    entry_texts,
    score_all,
    tag_of,
)
from techblog_mcp import db  # noqa: E402

EMBEDDING = "voyage-4-large"
RERANKER = "voyage-3"
GATES = [round(0.50 + 0.02 * i, 2) for i in range(16)]  # 결과 유무 기준선 후보 0.50~0.80
LATENCY_SAMPLES = 10


def is_absent(x: EvalQuery) -> bool:
    return x.source == "없는 주제"


def gate_correct(s: Scored, gate: float) -> bool:
    """정답 있는 질문은 결과를 돌려줘야 맞고, 없는 주제는 결과 없음이어야 맞다."""
    passed = s.top1(RERANKER) >= gate
    return not passed if is_absent(s.query) else passed


def best_gate(scored: list[Scored]) -> float:
    """두 종류를 함께 가장 많이 맞히는 기준선. 같은 성적이 여럿이면 그 구간의 가운데 값."""
    tops = sorted({s.top1(RERANKER) for s in scored})
    cuts = [(a + b) / 2 for a, b in zip(tops, tops[1:], strict=False)]
    score = {c: sum(gate_correct(s, c) for s in scored) for c in cuts}
    top = max(score.values())
    best = [c for c in cuts if score[c] == top]
    return statistics.median(best)


def gate_section(scored: list[Scored]) -> tuple[list[str], float]:
    answerable = [s for s in scored if s.query.relevant]
    absent = [s for s in scored if is_absent(s.query)]
    lines = [
        "## 결과 유무 기준선",
        "",
        f"정답 있는 질문 {len(answerable)}개, 없는 주제 {len(absent)}개.",
        "1위 리랭커 점수가 기준선 이상이면 결과 있음.",
        "",
        "| 기준선 | 결과 돌려줌 (정답 있는 질문) | 결과 없음 (없는 주제) | 틀린 질문 |",
        "| --- | --- | --- | --- |",
    ]
    for g in GATES:
        answered = sum(gate_correct(s, g) for s in answerable)
        empty = sum(gate_correct(s, g) for s in absent)
        wrong = [s.query.id for s in scored if not gate_correct(s, g)]
        lines.append(
            f"| {g:.2f} | {answered}/{len(answerable)} | {empty}/{len(absent)}"
            f" | {', '.join(wrong)} |"
        )

    # 질문 하나를 빼고 나머지로 기준선을 골라 뺀 질문을 맞히는지 (leave-one-out)
    held = []
    for n, s in enumerate(scored):
        if not (s.query.relevant or is_absent(s.query)):
            continue
        gate = best_gate(scored[:n] + scored[n + 1 :])
        held.append((s, gate, gate_correct(s, gate)))
    gates = [g for _, g, _ in held]
    ok_ans = sum(ok for s, _, ok in held if s.query.relevant)
    ok_abs = sum(ok for s, _, ok in held if is_absent(s.query))
    wrong = [s.query.id for s, _, ok in held if not ok]
    chosen = best_gate(scored)
    lines += [
        "",
        f"전체로 고른 기준선: {chosen:.3f}",
        "",
        "질문 하나를 빼고 나머지로 고른 기준선으로 뺀 질문을 판정했을 때(leave-one-out):",
        f"정답 있는 질문 {ok_ans}/{len(answerable)}, 없는 주제 {ok_abs}/{len(absent)} 맞힘."
        f" 고른 기준선 범위 {min(gates):.3f}~{max(gates):.3f}. 틀린 질문: {', '.join(wrong)}",
    ]
    return lines, chosen


def item_systems(scored: dict[str, Scored], gate: float) -> list[tuple[str, System]]:
    """결과가 있을 때 항목을 고르는 방식들."""

    def make(name: str, keep: Callable[[float, float], bool]) -> tuple[str, System]:
        def rank(x: EvalQuery) -> list[Ranked]:
            s = scored[x.id]
            top = s.top1(RERANKER)
            if top < gate:
                return []
            return [r for r in s.ranked(RERANKER) if keep(r.score, top)][:MAX_RESULTS]

        return name, System(name, rank, cutoff=True)

    out = [make("상위 10건 그대로", lambda s, t: True)]
    out += [make(f"점수 ≥ {a:.2f}", lambda s, t, a=a: s >= a) for a in (0.4, 0.5, 0.55, 0.6)]
    out += [make(f"점수 ≥ 1위 × {r:.2f}", lambda s, t, r=r: s >= t * r) for r in (0.7, 0.8, 0.9)]
    out += [make(f"점수 ≥ 1위 − {d:.2f}", lambda s, t, d=d: s >= t - d) for d in (0.1, 0.15, 0.2)]
    return out


def item_section(ctx: Context, scored: dict[str, Scored], gate: float) -> list[str]:
    lines = [
        "## 항목 고르기",
        "",
        f"결과 유무 기준선 {gate:.3f}로 결과 있음이 된 질문에서 보여 줄 항목을 고르는 방식별 지표.",
        "",
        "| 방식 | Recall@5 | MRR | Recall@10 | 결과 없음 | 평균 결과 수 | 무관 비율"
        " | 일부 관련 유지 | 미판정 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for name, system in item_systems(scored, gate):
        (row,) = run_rows(ctx, [system])
        m = summarize(row.results)
        lines.append(
            f"| {name} | {_fmt(m.recall5)} | {_fmt(m.mrr)} | {_fmt(m.recall10)}"
            f" | {m.no_result_rate:.0%} | {m.avg_returned:.1f} | {_fmt(m.noise_rate, 2)}"
            f" | {_fmt(m.partial_kept, 2)} | {m.unjudged} |"
        )
    return lines


def tag_section(ctx: Context, scored: dict[str, Scored], gate: float) -> list[str]:
    from eval.search_eval import evaluate_query
    from eval.search_rerank import TAG_GROUPS

    chosen = [s for name, s in item_systems(scored, gate) if name in ("점수 ≥ 0.50", "점수 ≥ 0.55")]
    lines = [
        "## 질문 성격별",
        "",
        "칸은 정답 있는 질문의 Recall@5 / MRR · 무관 비율, 없는 주제의 결과 없음 비율이다.",
        "",
        "| 방식 | " + " | ".join(TAG_GROUPS) + " |",
        "| --- |" + " --- |" * len(TAG_GROUPS),
    ]
    for system in chosen:
        cells = []
        for tag in TAG_GROUPS:
            group = [x for x in ctx.queries if tag_of(x) == tag]
            m = summarize([evaluate_query(x, system.rank(x), ctx.post_of) for x in group])
            parts = []
            if m.recall5 is not None:
                parts.append(f"{m.recall5:.3f} / {m.mrr:.3f} · 무관 {_fmt(m.noise_rate, 2)}")
            if m.no_result_rate is not None:
                parts.append(f"결과 없음 {m.no_result_rate:.0%}")
            cells.append(" · ".join(parts))
        lines.append(f"| {system.name} | " + " | ".join(cells) + " |")
    return lines


def latency_section(ctx: Context, scored: list[Scored]) -> list[str]:
    """검색 한 번: 검색어 임베딩 호출 + 후보 50건 리랭커 호출 (캐시 없이)."""
    embedder = make_embedder(MODELS[EMBEDDING])
    reranker = Reranker(next(s for s in RERANKERS if s.key == RERANKER))
    texts = entry_texts(ctx)
    embed_times, rerank_times = [], []
    for s in scored[:LATENCY_SAMPLES]:
        start = time.perf_counter()
        embedder.queries([s.query.query])
        embed_times.append(time.perf_counter() - start)
        start = time.perf_counter()
        reranker._call(s.query.query, [texts[i] for i in s.ids])
        rerank_times.append(time.perf_counter() - start)
    total = [a + b for a, b in zip(embed_times, rerank_times, strict=True)]
    return [
        "## 응답 시간",
        "",
        f"질문 {LATENCY_SAMPLES}개, 캐시 없이 API를 직접 불러 잰 값(네트워크 포함, 초).",
        "BM25·코사인 계산과 결과 렌더링은 수십 ms 이하라 뺐다.",
        "",
        "| 단계 | 평균 | 최대 |",
        "| --- | --- | --- |",
        f"| 검색어 임베딩 ({EMBEDDING}) | {statistics.mean(embed_times):.2f}"
        f" | {max(embed_times):.2f} |",
        f"| 리랭커 ({RERANKER}, 후보 50건) | {statistics.mean(rerank_times):.2f}"
        f" | {max(rerank_times):.2f} |",
        f"| 합계 | {statistics.mean(total):.2f} | {max(total):.2f} |",
    ]


def main() -> None:
    _load_env()
    ctx = Context(db.connect(ROOT / "data" / "techblog.sqlite"), load_queries())
    EmbeddingIndex(MODELS[EMBEDDING]).build(ctx.conn)
    reranker = Reranker(next(s for s in RERANKERS if s.key == RERANKER))
    scored_list = score_all(ctx, [reranker], EMBEDDING)
    scored = {s.query.id: s for s in scored_list}

    gate_lines, gate = gate_section(scored_list)
    sections = [
        gate_lines,
        item_section(ctx, scored, gate),
        tag_section(ctx, scored, gate),
        latency_section(ctx, scored_list),
    ]
    head = [
        "# M10 R4: 판정 방식 (voyage-4-large 후보 + Voyage rerank-3)",
        "",
        "후보는 BM25와 voyage-4-large 상위 50건씩을 RRF로 합친 상위 50건이다.",
        f"평가셋 질문 {len(ctx.queries)}개. 지표 정의는 eval/search/README.md.",
        "",
        "",
    ]
    text = "\n".join(head) + "\n\n".join("\n".join(s) for s in sections) + "\n"
    path = REPORTS / "m10-r4-gate.md"
    path.write_text(text, encoding="utf-8")
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
