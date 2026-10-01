"""추출 run 점검 리포트: 분류 분포, 짧은 글 처리, 발췌 탈락, 미등록 기술명, 비용.

    uv run python eval/inspect_run.py eval/runs/baseline-gpt-5-mini-medium
    # → eval/reports/baseline-gpt-5-mini-medium.md

정답셋 없이 run 결과만으로 볼 수 있는 것을 모은다.
정답셋과 비교하는 지표는 extract_eval.py에서 본다.
"""

import argparse
import sys
import tomllib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 pipeline을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from pipeline.collect import raw  # noqa: E402
from pipeline.extract.schema import Entry, PostRecord, Usage  # noqa: E402
from pipeline.extract.store import Store  # noqa: E402
from pipeline.extract.text import html_to_text  # noqa: E402
from pipeline.normalize import renormalize  # noqa: E402
from techblog_mcp import taxonomy  # noqa: E402

PRICING = ROOT / "eval" / "pricing.toml"
REPORTS = ROOT / "eval" / "reports"
SHORT_TEXT = 1500  # M2에서 넘어온 "본문이 짧은 글" 기준 (평문 글자 수)
SKEW = 0.3  # 한 분류에 이 비율 넘게 몰리면 쏠림으로 표시
TOTAL_POSTS = 1262  # M2에서 수집한 전체 글 수 (전체 추출 비용 추정용)


def load_pricing(path: Path = PRICING) -> dict:
    return tomllib.loads(path.read_text(encoding="utf-8"))["models"]


def cost(usage: Usage, price: dict) -> float:
    """USD. reasoning 토큰은 출력 토큰에 포함되어 있다."""
    fresh = usage.input_tokens - usage.cached_input_tokens
    return (
        fresh * price["input"]
        + usage.cached_input_tokens * price["cached_input"]
        + usage.output_tokens * price["output"]
    ) / 1_000_000


def text_lengths(posts: list[PostRecord]) -> dict[str, int]:
    """글 URL → 평문 길이. 원문 캐시가 없는 글은 빠진다."""
    lengths = {}
    for p in posts:
        path = raw.raw_path(p.source, p.post_id)
        if path.exists():
            post = raw.RawPost.from_json(path.read_text(encoding="utf-8"))
            lengths[p.url] = len(html_to_text(post.content_html))
    return lengths


def _pct(n: int, total: int) -> str:
    return f"{n / total:.0%}" if total else "-"


def _table(header: list[str], rows: list[list]) -> list[str]:
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    lines += ["| " + " | ".join(str(c).replace("|", "\\|") for c in row) + " |" for row in rows]
    return lines


def _distribution(title: str, counts: Counter, names: tuple[str, ...], total: int) -> list[str]:
    lines = [f"## {title}", ""]
    rows = [[name, n, _pct(n, total)] for name, n in counts.most_common()]
    lines += _table(["분류", "항목 수", "비율"], rows)
    skewed = [name for name, n in counts.items() if total and n / total > SKEW]
    unused = [name for name in names if name not in counts]
    lines.append("")
    if skewed:
        lines.append(f"- 쏠림({SKEW:.0%} 초과): {', '.join(skewed)}")
    lines.append(f"- 한 번도 안 쓰인 분류 ({len(unused)}개): {', '.join(unused) or '없음'}")
    return [*lines, ""]


def build_report(
    run_name: str,
    posts: list[PostRecord],
    entries: list[Entry],
    lengths: dict[str, int],
    pricing: dict,
) -> str:
    entries_by_url: dict[str, list[Entry]] = {}
    for e in entries:
        entries_by_url.setdefault(e.post_url, []).append(e)
    models = sorted({(p.model, p.reasoning_effort) for p in posts})
    kinds = Counter(p.kind for p in posts)

    # 비용
    usage = Usage()
    for p in posts:
        usage.add(p.usage)
    model = posts[0].model if posts else ""
    price = pricing.get(model)
    model_names = ", ".join(f"{m} ({e or '?'})" for m, e in models)
    lines = [f"# 추출 점검 리포트: {run_name}", ""]
    lines += [
        f"- 모델: {model_names}",
        f"- 프롬프트 버전: {', '.join(sorted({p.prompt_version for p in posts}))}",
        f"- 글 {len(posts)}편: " + ", ".join(f"{k} {kinds[k]}" for k in ("추출", "제외")),
        f"- 항목 {len(entries)}개",
        f"- 토큰: 호출 {usage.calls}회, 입력 {usage.input_tokens:,}"
        f" (캐시 {usage.cached_input_tokens:,}),"
        f" 출력 {usage.output_tokens:,} (reasoning {usage.reasoning_tokens:,})",
    ]
    if price and posts:
        std = cost(usage, price)
        batch = cost(usage, price["batch"]) if "batch" in price else None
        per_post = std / len(posts)
        line = (
            f"- 비용: ${std:.3f} (편당 ${per_post:.4f}),"
            f" 전체 {TOTAL_POSTS:,}편 추정 ${per_post * TOTAL_POSTS:.1f}"
        )
        if batch is not None:
            line += f" / Batch ${batch / len(posts) * TOTAL_POSTS:.1f}"
        lines.append(line)
    else:
        lines.append(f"- 비용: `eval/pricing.toml`에 {model} 단가가 없음")
    lines.append("")

    # 블로그별 분포
    lines += ["## 블로그별 추출 여부", ""]
    sources = sorted({p.source for p in posts})
    rows = []
    for s in sources:
        c = Counter(p.kind for p in posts if p.source == s)
        n_entries = sum(len(entries_by_url.get(p.url, [])) for p in posts if p.source == s)
        rows.append([s, c["추출"], c["제외"], n_entries])
    lines += _table(["블로그", "추출", "제외", "항목 수"], rows)
    lines.append("")

    lines += ["## 글 유형 × 추출 여부", ""]
    pt = Counter((p.post_type, p.kind) for p in posts)
    post_types = sorted({p.post_type for p in posts})
    lines += _table(
        ["글 유형", "추출", "제외"],
        [[t, pt[(t, "추출")], pt[(t, "제외")]] for t in post_types],
    )
    lines.append("")

    # 짧은 글
    short = [p for p in posts if lengths.get(p.url, SHORT_TEXT) < SHORT_TEXT]
    lines += [f"## 짧은 글 (평문 {SHORT_TEXT:,}자 미만) {len(short)}편", ""]
    lines += _table(
        ["글", "길이", "결과", "항목", "분류 이유"],
        [
            [
                f"{p.source}/{p.post_id}",
                f"{lengths[p.url]:,}",
                f"{p.kind}/{p.post_type}",
                len(entries_by_url.get(p.url, [])),
                p.reason,
            ]
            for p in short
        ],
    )
    lines.append("")

    # 글당 항목 수
    per_post = Counter(len(entries_by_url.get(p.url, [])) for p in posts if p.kind != "제외")
    lines += ["## 글당 항목 수 (제외 글 빼고)", ""]
    lines += _table(["항목 수", "글 수"], [[k, per_post[k]] for k in sorted(per_post)])
    lines.append("")

    # 분류 분포 (항목 기준)
    lines += _distribution(
        "주 문제 유형 분포",
        Counter(e.primary_problem_type for e in entries),
        taxonomy.problem_type_names(),
        len(entries),
    )
    lines += _distribution(
        "도메인 분포", Counter(e.domain for e in entries), taxonomy.domain_names(), len(entries)
    )

    # 발췌
    total_ev = sum(p.evidence_total for p in posts)
    dropped_ev = sum(p.dropped_evidence for p in posts)
    lines += [
        "## 발췌 검증",
        "",
        f"- 채택한 시도 기준 발췌 {total_ev}개 중 탈락 {dropped_ev}개"
        f" (원문 존재율 {_pct(total_ev - dropped_ev, total_ev)})",
        f"- 재시도한 글 {sum(1 for p in posts if p.usage.calls > 2)}편",
        "",
    ]
    for p in posts:
        for ev in p.dropped_evidences:
            lines.append(f"- `{p.source}/{p.post_id}`: {ev}")
    lines.append("")

    # 기술명
    missing = Counter()
    for e in entries:
        missing.update(renormalize(e)[1])
    lines += [f"## 기술 사전에 없는 이름 {len(missing)}종", ""]
    lines += [f"- {name} ({n})" for name, n in missing.most_common()]
    lines.append("")

    # 버린 대안
    rejected = [(e, r) for e in entries for r in e.rejected_alternatives]
    lines += [f"## 버린 대안 {len(rejected)}개 (항목 {len(entries)}개 중)", ""]
    for e, r in rejected:
        both = " **(technologies에도 있음)**" if r.name in e.technologies else ""
        raw_name = f" ← {r.name_raw}" if r.name_raw != r.name else ""
        lines.append(f"- `{e.id}` {r.name}{raw_name}: {r.reason}{both}")
    lines.append("")

    # 전체 글 목록
    lines += ["## 글 목록", ""]
    rows = []
    for p in posts:
        es = entries_by_url.get(p.url, [])
        rows.append(
            [
                f"{p.source}/{p.post_id}",
                f"{lengths.get(p.url, 0):,}",
                f"{p.kind}/{p.post_type}",
                ", ".join(e.id for e in es) or "-",
                f"{p.dropped_evidence}/{p.evidence_total}",
                p.title,
            ]
        )
    lines += _table(["글", "길이", "결과", "항목", "발췌 탈락", "제목"], rows)
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="추출 run 점검 리포트를 만든다.")
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--out", type=Path, help="기본: eval/reports/{run 이름}.md")
    args = parser.parse_args()

    store = Store.in_dir(args.run_dir)
    posts = list(store.posts.values())
    report = build_report(
        args.run_dir.name, posts, store.entries, text_lengths(posts), load_pricing()
    )
    out = args.out or REPORTS / f"{args.run_dir.name}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")
    print(f"리포트 저장: {out}")


if __name__ == "__main__":
    main()
