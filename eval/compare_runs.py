"""추출 run 비교 리포트.

정답셋 없이 볼 수 있는 지표를 run별로 나란히 놓고, 글별 분류 변화를 보여 준다.

    uv run python eval/compare_runs.py eval/runs/baseline-gpt-5-mini-medium \
        eval/runs/v2-gpt-5-mini-medium
    # → eval/reports/compare-baseline-gpt-5-mini-medium-vs-v2-gpt-5-mini-medium.md

정답과 비교하는 지표(분류 일치율, 기술명 정밀도·재현율 등)는 정답셋을 만든 뒤
extract_eval.py에서 본다.
"""

import argparse
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 pipeline을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from eval.inspect_run import (  # noqa: E402
    REPORTS,
    SHORT_TEXT,
    TOTAL_POSTS,
    _table,
    cost,
    load_pricing,
    text_lengths,
)
from pipeline.extract.schema import Entry, PostRecord, Usage  # noqa: E402
from pipeline.extract.store import Store  # noqa: E402
from pipeline.normalize import renormalize  # noqa: E402


@dataclass
class Run:
    name: str
    posts: list[PostRecord]
    entries: list[Entry]

    @classmethod
    def load(cls, run_dir: Path) -> "Run":
        store = Store.in_dir(run_dir)
        # 기술 사전이 바뀌었을 수 있으므로 현재 사전으로 다시 정규화해 비교한다
        entries = [renormalize(e)[0] for e in store.entries]
        return cls(run_dir.name, list(store.posts.values()), entries)


def _pct(n: int, total: int) -> str:
    return f"{n} ({n / total:.0%})" if total else "-"


def run_metrics(run: Run, lengths: dict[str, int], pricing: dict) -> dict[str, str]:
    """run 하나의 요약 지표 (표의 한 열)."""
    posts, entries = run.posts, run.entries
    kinds = Counter(p.kind for p in posts)
    cases = [e for e in entries if e.kind == "사례"]
    extracted = [p for p in posts if p.kind != "제외"]
    total_ev = sum(p.evidence_total for p in posts)
    dropped_ev = sum(p.dropped_evidence for p in posts)
    missing = Counter(name for e in entries for name in renormalize(e)[1])
    rejected = [r for e in cases for r in e.rejected_alternatives]
    short = [p for p in posts if lengths.get(p.url, SHORT_TEXT) < SHORT_TEXT]
    primary = Counter(e.primary_problem_type for e in entries).most_common(1)
    domain = Counter(e.domain for e in entries).most_common(1)

    usage = Usage()
    for p in posts:
        usage.add(p.usage)
    price = pricing.get(posts[0].model) if posts else None
    run_cost = cost(usage, price) if price else None

    evidence = "-"
    if total_ev:
        evidence = f"{(total_ev - dropped_ev) / total_ev:.1%} ({dropped_ev}/{total_ev} 탈락)"
    unregistered = "-"
    if entries:
        unregistered = f"{len(missing)} / {sum(missing.values()) / len(entries):.2f}"
    return {
        "모델 (effort)": f"{posts[0].model} ({posts[0].reasoning_effort or '?'})" if posts else "-",
        "프롬프트 버전": ", ".join(sorted({p.prompt_version for p in posts})),
        "글 수": str(len(posts)),
        "사례 글": _pct(kinds["사례"], len(posts)),
        "인사이트 글": _pct(kinds["인사이트"], len(posts)),
        "제외 글": _pct(kinds["제외"], len(posts)),
        "항목 수 (사례/인사이트)": f"{len(entries)} ({len(cases)}/{len(entries) - len(cases)})",
        "글당 항목 수 (제외 빼고)": f"{len(entries) / len(extracted):.2f}" if extracted else "-",
        f"짧은 글(<{SHORT_TEXT:,}자)에서 항목 만든 글": f"{sum(p.kind != '제외' for p in short)}"
        f" / {len(short)}",
        "발췌 원문 존재율": evidence,
        "재시도한 글": str(sum(1 for p in posts if p.usage.calls > 2)),
        "사전에 없는 기술명 (종류 / 항목당)": unregistered,
        "버린 대안 (기술/설계 방식)": f"{len(rejected)} ({sum(r.kind == '기술' for r in rejected)}"
        f"/{sum(r.kind == '설계 방식' for r in rejected)})",
        "가장 많은 주 문제 유형": f"{primary[0][0]} {primary[0][1] / len(entries):.0%}"
        if primary
        else "-",
        "가장 많은 도메인": f"{domain[0][0]} {domain[0][1] / len(entries):.0%}" if domain else "-",
        "비용 (편당 / 전체 추정)": f"${run_cost:.2f} (${run_cost / len(posts):.4f}"
        f" / ${run_cost / len(posts) * TOTAL_POSTS:.1f})"
        if run_cost is not None and posts
        else "-",
    }


def kind_changes(runs: list[Run]) -> list[list[str]]:
    """run마다 구조화 유형이나 항목 수가 달라진 글."""
    by_run = [{(p.source, p.post_id): p for p in r.posts} for r in runs]
    counts = [Counter(e.post_url for e in r.entries) for r in runs]
    keys = sorted(set().union(*by_run))
    rows = []
    for key in keys:
        records = [b.get(key) for b in by_run]
        cells = [
            f"{rec.kind} {counts[i][rec.url]}개" if rec else "-" for i, rec in enumerate(records)
        ]
        if len(set(cells)) > 1:
            title = next(r.title for r in records if r)
            rows.append([f"{key[0]}/{key[1]}", *cells, title[:40]])
    return rows


def build_report(runs: list[Run], lengths: dict[str, int], pricing: dict) -> str:
    names = [r.name for r in runs]
    metrics = [run_metrics(r, lengths, pricing) for r in runs]
    lines = [f"# 추출 run 비교: {' vs '.join(names)}", ""]
    lines += _table(["지표", *names], [[k, *(m[k] for m in metrics)] for k in metrics[0]])
    lines += [
        "",
        "- 사전에 없는 기술명은 현재 기술 사전으로 다시 정규화해 센다.",
        "- 버린 대안 유형이 없는 이전 run은 사전에 있으면 기술, 없으면 설계 방식으로 추정한다.",
        "",
    ]
    changes = kind_changes(runs)
    lines += [f"## 구조화 유형·항목 수가 달라진 글 {len(changes)}편", ""]
    lines += _table(["글", *names, "제목"], changes)
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="추출 run 비교 리포트를 만든다.")
    parser.add_argument("run_dirs", type=Path, nargs="+")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    runs = [Run.load(d) for d in args.run_dirs]
    lengths = text_lengths([p for r in runs for p in r.posts])
    report = build_report(runs, lengths, load_pricing())
    out = args.out or REPORTS / f"compare-{'-vs-'.join(r.name for r in runs)}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")
    print(f"리포트 저장: {out}")


if __name__ == "__main__":
    main()
