"""정답셋 기준 추출 평가 리포트.

    uv run python eval/extract_eval.py eval/runs/baseline-gpt-5-mini-medium \
        eval/runs/v3-gpt-5-mini-medium
    # → eval/reports/eval-baseline-gpt-5-mini-medium-vs-v3-gpt-5-mini-medium.md

정답셋(`eval/gold/`)에 있는 글만 본다. 계산만으로 정해지는 지표(분류 일치율, 항목 수, 기술명)는
항상 나오고, 항목 대응이 필요한 지표(문제 유형·도메인, 버린 대안, 완결성, 충실성 등)는
judge.py 채점 결과가 최신인 글에서만 계산한다. 비용은 run 전체 글 기준이다.
"""

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 pipeline을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from eval.compare_runs import Run  # noqa: E402
from eval.gold import GoldPost, load_gold  # noqa: E402
from eval.inspect_run import REPORTS, TOTAL_POSTS, _table, cost, load_pricing  # noqa: E402
from eval.judge import (  # noqa: E402
    COVERAGE_SCORE,
    JudgeRecord,
    input_hash,
    is_current,
    load_judgements,
)
from eval.judge import prompt_version as judge_prompt_version  # noqa: E402
from pipeline.extract.schema import Entry, PostRecord, Usage  # noqa: E402
from techblog_mcp import taxonomy  # noqa: E402


def tech_key(name: str) -> str:
    """기술명 비교 키: 사전에 있으면 표준 이름, 없으면 대소문자·구분자를 무시한 원래 이름."""
    standard = taxonomy.normalize_technology(name) or name
    return re.sub(r"[\s\-_.·]", "", standard).casefold()


@dataclass
class Counts:
    """정밀도·재현율 집계 (글 단위 집합 비교를 글 전체에 합산)."""

    hit_pred: int = 0  # 예측 중 정답에 있는 것
    pred: int = 0
    hit_gold: int = 0  # 정답 중 예측에 있는 것
    gold: int = 0

    def add(self, other: "Counts") -> None:
        self.hit_pred += other.hit_pred
        self.pred += other.pred
        self.hit_gold += other.hit_gold
        self.gold += other.gold

    def precision(self) -> float | None:
        return self.hit_pred / self.pred if self.pred else None

    def recall(self) -> float | None:
        return self.hit_gold / self.gold if self.gold else None


def set_counts(pred: set[str], gold: set[str]) -> Counts:
    hit = len(pred & gold)
    return Counts(hit, len(pred), hit, len(gold))


def technology_counts(gold: GoldPost, entries: list[Entry]) -> Counts:
    pred = {tech_key(n) for e in entries for n in e.technologies_raw}
    expected = {tech_key(n) for g in gold.entries for n in g.technologies}
    return set_counts(pred, expected)


def kind_ok(gold: GoldPost, record: PostRecord) -> bool:
    return record.kind == gold.kind or record.kind in gold.kind_alternatives


@dataclass
class PostEval:
    """정답 글 하나의 평가 결과. judge 값은 채점 결과가 최신일 때만 채운다."""

    gold: GoldPost
    record: PostRecord
    entries: list[Entry]
    judged: bool = False
    # 정답 key_facts 포함률. 담김 1, 일부 0.5, 없음 0 (정답 항목이 없으면 None)
    completeness: float | None = None
    faithfulness: list[int] = field(default_factory=list)
    card_summary: list[int] = field(default_factory=list)
    split_score: int | None = None
    # 대응된 (정답, 추출) 쌍마다 집합 비교.
    # 정밀도는 꼭 들어갈 값 + 허용 값, 재현율은 꼭 들어갈 값 기준
    types: Counts = field(default_factory=Counts)
    domains: Counts = field(default_factory=Counts)
    pairs: int = 0
    rejected: Counts = field(default_factory=Counts)
    rejected_unmatched: int = 0  # 정답에 없는 버린 대안
    rejected_unsupported: int = 0  # 그중 원문에 버린 이유가 없는 것
    unsupported_claims: list[str] = field(default_factory=list)

    @property
    def both_extracted(self) -> bool:
        return bool(self.gold.entries) and bool(self.entries)


def label_counts(pred: list[str], core: list[str], acceptable: list[str]) -> Counts:
    """다중 선택 분류 비교.

    예측 중 허용 범위(꼭 들어갈 값 + 허용 값)에 드는 수와, 꼭 들어갈 값 중 맞힌 수를 센다.
    """
    predicted, required = set(pred), set(core)
    return Counts(
        hit_pred=len(predicted & (required | set(acceptable))),
        pred=len(predicted),
        hit_gold=len(predicted & required),
        gold=len(required),
    )


_REJECTED_KIND_SUFFIX = re.compile(r"\s*\((기술|설계 방식)\)\s*$")


def gold_rejected_name(name: str) -> str:
    """정답 대안 이름에서 유형 표시를 뗀다.

    채점 모델은 정답 대안을 "이름 (유형)" 형식으로 보므로 그대로 돌려줄 때가 있다.
    """
    return _REJECTED_KIND_SUFFIX.sub("", name.strip())


def _clamp(score: int) -> int:
    return min(5, max(1, score))


def evaluate_post(
    gold: GoldPost, record: PostRecord, entries: list[Entry], judge: JudgeRecord | None
) -> PostEval:
    ev = PostEval(gold, record, entries)
    if judge is None:
        return ev
    ev.judged = True
    if judge.output is None:  # 추출 항목이 없는 글: 정답 항목이 있으면 아무것도 담지 못한 것
        if gold.entries:
            ev.completeness = 0.0
            ev.rejected = Counts(gold=sum(len(g.rejected_alternatives) for g in gold.entries))
        return ev

    out = judge.output
    by_id = {e.id: e for e in entries}
    facts_total = sum(len(g.key_facts) for g in gold.entries)
    facts_hit = 0
    for m in out.matches:
        if not 1 <= m.gold_index <= len(gold.entries):
            continue
        g = gold.entries[m.gold_index - 1]
        matched = [by_id[i] for i in m.extracted_ids if i in by_id]
        if matched:
            facts_hit += sum(COVERAGE_SCORE[c] for c in m.key_facts_coverage[: len(g.key_facts)])
        for e in matched:
            ev.pairs += 1
            ev.types.add(label_counts(e.problem_types, g.problem_types, g.acceptable_problem_types))
            ev.domains.add(label_counts(e.domains, g.domains, g.acceptable_domains))
    if facts_total:
        ev.completeness = facts_hit / facts_total

    for s in out.entries:
        if s.entry_id in by_id:
            ev.faithfulness.append(_clamp(s.faithfulness))
            ev.card_summary.append(_clamp(s.card_summary))
            ev.unsupported_claims += [f"{s.entry_id}: {c}" for c in s.unsupported_claims]
    ev.split_score = _clamp(out.split_score)

    # 버린 대안: 이름이 정답의 어느 대안과 같은지는 채점 모델이 판정한다
    gold_names = {r.name for g in gold.entries for r in g.rejected_alternatives}
    judged = [r for r in out.rejected if r.entry_id in by_id]
    matched = [gold_rejected_name(r.gold_name) for r in judged]
    ev.rejected = Counts(
        hit_pred=sum(name in gold_names for name in matched),
        pred=len(judged),
        hit_gold=len(gold_names & set(matched)),
        gold=len(gold_names),
    )
    unmatched = [r for r, name in zip(judged, matched, strict=True) if name not in gold_names]
    ev.rejected_unmatched = len(unmatched)
    ev.rejected_unsupported = sum(not r.supported for r in unmatched)
    return ev


def evaluate_run(
    run: Run, golds: dict[tuple[str, str], GoldPost], judgements: dict[tuple[str, str], JudgeRecord]
) -> list[PostEval]:
    by_key = {(p.source, p.post_id): p for p in run.posts}
    by_url: dict[str, list[Entry]] = {}
    for e in run.entries:
        by_url.setdefault(e.post_url, []).append(e)
    version = judge_prompt_version()
    evals = []
    for key, gold in sorted(golds.items()):
        record = by_key.get(key)
        if record is None:
            continue
        entries = by_url.get(record.url, [])
        judge = judgements.get(key)
        current = judge and is_current(
            judge, judge.judge_model, judge.judge_effort, version, input_hash(gold, entries)
        )
        evals.append(evaluate_post(gold, record, entries, judge if current else None))
    return evals


def _rate(hit: int, total: int) -> str:
    return f"{hit / total:.0%} ({hit}/{total})" if total else "-"


def _ratio(value: float | None) -> str:
    return f"{value:.0%}" if value is not None else "-"


def _kept(total: int, dropped: int) -> float | None:
    return (total - dropped) / total if total else None


def _pr(c: Counts) -> str:
    return (
        f"{_ratio(c.precision())} / {_ratio(c.recall())}"
        f" ({c.hit_pred}/{c.pred}, {c.hit_gold}/{c.gold})"
    )


def _mean(values: list[float]) -> str:
    return f"{sum(values) / len(values):.2f}" if values else "-"


def run_metrics(run: Run, evals: list[PostEval], judgements: dict, pricing: dict) -> dict[str, str]:
    n = len(evals)
    judged = [e for e in evals if e.judged]
    both = [e for e in evals if e.both_extracted]
    extracted = [e for e in evals if e.gold.kind == "추출" and e.record.kind == "추출"]
    diffs = Counter(len(e.entries) - len(e.gold.entries) for e in extracted)

    tech = Counts()
    for e in both:
        tech.add(technology_counts(e.gold, e.entries))
    rejected = Counts()
    for e in judged:
        if e.both_extracted or e.gold.entries:
            rejected.add(e.rejected)
    completeness = [e.completeness for e in judged if e.completeness is not None]
    types, domains = Counts(), Counts()
    for e in judged:
        types.add(e.types)
        domains.add(e.domains)

    gold_ev = sum(e.record.evidence_total for e in evals)
    gold_dropped = sum(e.record.dropped_evidence for e in evals)
    all_ev = sum(p.evidence_total for p in run.posts)
    all_dropped = sum(p.dropped_evidence for p in run.posts)

    usage = Usage()
    for p in run.posts:
        usage.add(p.usage)
    price = pricing.get(run.posts[0].model) if run.posts else None
    run_cost = cost(usage, price) if price else None
    judge_usage = Usage()
    judge_models = set()
    for key in {(e.gold.source, e.gold.post_id) for e in judged}:
        judge_usage.add(judgements[key].usage)
        judge_models.add(judgements[key].judge_model)
    judge_price = pricing.get(next(iter(judge_models))) if len(judge_models) == 1 else None

    def per_post_cost() -> str:
        if run_cost is None or not run.posts:
            return "-"
        per = run_cost / len(run.posts)
        return f"${per:.4f} (전체 {TOTAL_POSTS:,}편 ${per * TOTAL_POSTS:.1f})"

    return {
        "모델 (effort)": f"{run.posts[0].model} ({run.posts[0].reasoning_effort or '?'})"
        if run.posts
        else "-",
        "프롬프트 버전": ", ".join(sorted({p.prompt_version for p in run.posts})),
        "정답 글 / 채점된 글": f"{n} / {len(judged)}",
        "추출 여부 일치 (허용 답 포함)": _rate(sum(kind_ok(e.gold, e.record) for e in evals), n),
        "추출 여부 정확 일치": _rate(sum(e.record.kind == e.gold.kind for e in evals), n),
        "글 유형 일치": _rate(sum(e.record.post_type == e.gold.post_type for e in evals), n),
        "항목 수 차이 (추출 − 정답)": ", ".join(f"{d:+d}: {diffs[d]}편" for d in sorted(diffs))
        or "-",
        "기술 정밀도 / 재현율": _pr(tech),
        "문제 유형 정밀도 / 재현율 (대응 쌍)": _pr(types),
        "도메인 정밀도 / 재현율 (대응 쌍)": _pr(domains),
        "버린 대안 정밀도 / 재현율": _pr(rejected),
        "정답에 없는 버린 대안 중 원문 근거 없음": _rate(
            sum(e.rejected_unsupported for e in judged), sum(e.rejected_unmatched for e in judged)
        ),
        "완결성 (key_facts 포함률, 글 평균)": _ratio(
            sum(completeness) / len(completeness) if completeness else None
        ),
        "충실성 (1~5, 항목 평균)": _mean([s for e in judged for s in e.faithfulness]),
        "카드 요약 적합성 (1~5)": _mean([s for e in judged for s in e.card_summary]),
        "분할 적절성 (1~5, 글 평균)": _mean(
            [e.split_score for e in judged if e.split_score is not None]
        ),
        "원문 근거 없는 주장": str(sum(len(e.unsupported_claims) for e in judged)),
        "발췌 원문 존재율 (정답 글 / 전체)": f"{_ratio(_kept(gold_ev, gold_dropped))}"
        f" / {_ratio(_kept(all_ev, all_dropped))}",
        "추출 비용 (편당 / 전체 추정)": per_post_cost(),
        "채점 비용": f"${cost(judge_usage, judge_price):.2f} ({', '.join(sorted(judge_models))})"
        if judge_price
        else "-",
    }


def _post_cell(e: PostEval) -> str:
    cell = f"{e.record.kind} {len(e.entries)}개"
    if not kind_ok(e.gold, e.record):
        cell = f"**{cell}**"
    if e.completeness is not None:
        cell += f" · 완결 {e.completeness:.0%}"
    if e.faithfulness:
        cell += f" · 충실 {min(e.faithfulness)}"
    return cell


def build_report(names: list[str], metrics: list[dict], evals: list[list[PostEval]]) -> str:
    lines = [f"# 정답셋 평가: {' vs '.join(names)}", ""]
    lines += _table(["지표", *names], [[k, *(m[k] for m in metrics)] for k in metrics[0]])
    lines += [
        "",
        "- 기술 정밀도·재현율은 정답과 추출 모두 항목이 있는 글에서 글 단위 집합으로 비교한다"
        " (사전에 있으면 표준 이름, 없으면 대소문자·구분자 무시).",
        "- 문제 유형·도메인 일치, 버린 대안, 완결성, 충실성은 judge.py 채점 결과가"
        " 최신인 글만 센다. 문제 유형·도메인은 다중 선택이라 집합으로 비교한다:"
        " 정밀도는 추출한 값 중 정답(꼭 들어갈 값 + 허용 값)에 드는 비율,"
        " 재현율은 꼭 들어갈 값 중 추출에 들어간 비율.",
        "- 완결성은 추출에서 빠진 정답 글(추출 결과가 제외)도 0%로 넣는다.",
        "",
        "## 글별 결과",
        "",
        "굵게 표시한 것은 추출 여부가 정답과 다른 글. 완결은 key_facts 포함률,"
        " 충실은 그 글 항목 중 가장 낮은 충실성 점수.",
        "",
    ]
    by_key = [{(e.gold.source, e.gold.post_id): e for e in run} for run in evals]
    keys = sorted(set().union(*by_key))
    rows = []
    for key in keys:
        gold = next(b[key].gold for b in by_key if key in b)
        alt = f" (허용 {', '.join(gold.kind_alternatives)})" if gold.kind_alternatives else ""
        rows.append(
            [
                f"{key[0]}/{key[1]}",
                f"{gold.kind} {len(gold.entries)}개{alt}",
                *(_post_cell(b[key]) if key in b else "-" for b in by_key),
            ]
        )
    lines += _table(["글", "정답", *names], rows)
    lines.append("")

    for name, run in zip(names, evals, strict=True):
        claims = [(e, c) for e in run for c in e.unsupported_claims]
        if claims:
            lines += [f"## {name}: 원문 근거 없는 주장 {len(claims)}개", ""]
            lines += [f"- `{e.gold.source}/{e.gold.post_id}` {c}" for e, c in claims]
            lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="정답셋 기준 추출 평가 리포트")
    parser.add_argument("run_dirs", type=Path, nargs="+")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    golds = load_gold()
    pricing = load_pricing()
    names, metrics, evals = [], [], []
    for run_dir in args.run_dirs:
        run = Run.load(run_dir)
        judgements = load_judgements(run_dir)
        run_evals = evaluate_run(run, golds, judgements)
        names.append(run.name)
        evals.append(run_evals)
        metrics.append(run_metrics(run, run_evals, judgements, pricing))
    out = args.out or REPORTS / f"eval-{'-vs-'.join(names)}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_report(names, metrics, evals), encoding="utf-8")
    print(f"리포트 저장: {out}")


if __name__ == "__main__":
    main()
