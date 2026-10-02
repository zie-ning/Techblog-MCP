"""발췌 검증 완화 실험 (M3 6단계): 지금 규칙(줄 단위)과 문장 단위 검증 비교.

    uv run python eval/evidence_relax.py eval/runs/baseline-gpt-5-mini-medium \
        eval/runs/v4-gpt-5-mini-medium
    # → eval/reports/evidence-relax.md

run의 drafts.jsonl(검증 전 LLM 출력)을 다시 검증하므로 LLM을 다시 부르지 않는다.
첫 구조화 시도 기준으로 센다(재시도 여부가 첫 시도의 탈락으로 정해지므로).

- 되살아난 발췌: 지금 규칙으로는 탈락, 문장 단위로는 통과
- 재시도가 필요 없어지는 글: 첫 시도의 탈락이 모두 되살아나는 글
되살아난 발췌가 떨어진 문장을 섞어 뜻이 바뀌었는지는 리포트 목록을 보고 판단한다.
"""

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 pipeline을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from eval.inspect_run import REPORTS, _table  # noqa: E402
from pipeline.collect import raw  # noqa: E402
from pipeline.extract.evidence import SourceText  # noqa: E402
from pipeline.extract.text import html_to_text  # noqa: E402


def evidences(node) -> list[str]:
    """구조화 출력 JSON에서 evidence 값을 모두 모은다 (사례·인사이트 시절 형식도 그대로 읽는다)."""
    found: list[str] = []
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "evidence" and isinstance(value, str):
                found.append(value)
            else:
                found += evidences(value)
    elif isinstance(node, list):
        for item in node:
            found += evidences(item)
    return found


@dataclass
class RunResult:
    name: str
    total: int = 0
    failed: int = 0
    recovered: list[tuple[str, str]] = field(default_factory=list)  # (글, 발췌)
    retried_posts: int = 0
    retry_avoided: int = 0


def evaluate(run_dir: Path) -> RunResult:
    result = RunResult(run_dir.name)
    texts: dict[tuple[str, str], SourceText] = {}
    for line in (run_dir / "drafts.jsonl").read_text(encoding="utf-8").splitlines():
        draft = json.loads(line)
        if not draft["attempts"]:
            continue
        key = (draft["source"], draft["post_id"])
        if key not in texts:
            post = raw.RawPost.from_json(raw.raw_path(*key).read_text(encoding="utf-8"))
            texts[key] = SourceText(html_to_text(post.content_html))
        source = texts[key]
        first = evidences(draft["attempts"][0])
        failed = [e for e in first if not source.contains(e)]
        recovered = [e for e in failed if source.contains(e, by_sentence=True)]
        result.total += len(first)
        result.failed += len(failed)
        result.recovered += [(f"{key[0]}/{key[1]}", e) for e in recovered]
        if failed:
            result.retried_posts += 1
            result.retry_avoided += len(recovered) == len(failed)
    return result


def build_report(results: list[RunResult]) -> str:
    lines = ["# 발췌 검증 완화 실험: 줄 단위(현행) vs 문장 단위", ""]
    rows = []
    for r in results:
        n = len(r.recovered)
        rows.append(
            [
                r.name,
                r.total,
                f"{r.failed} ({r.failed / r.total:.1%})" if r.total else "-",
                f"{n} ({n / r.failed:.0%})" if r.failed else "0",
                f"{r.retry_avoided} / {r.retried_posts}",
            ]
        )
    lines += _table(
        ["run", "첫 시도 발췌", "현행 탈락", "문장 단위로 되살아남", "재시도가 필요 없어지는 글"],
        rows,
    )
    lines += [
        "",
        "- 첫 구조화 시도 기준. 탈락 발췌가 있으면 재시도하므로,"
        " 재시도가 필요 없어지는 글은 비용 절감분이다.",
        "- 아래 목록은 되살아난 발췌. 떨어진 문장을 이어 붙여 뜻이 바뀌었는지 확인하는 대상이다.",
        "",
    ]
    for r in results:
        lines += [f"## {r.name}: 되살아난 발췌 {len(r.recovered)}개", ""]
        lines += [f"- `{post}` {evidence}" for post, evidence in r.recovered]
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="발췌 검증 완화 실험")
    parser.add_argument("run_dirs", type=Path, nargs="+")
    parser.add_argument("--out", type=Path, default=REPORTS / "evidence-relax.md")
    args = parser.parse_args()
    report = build_report([evaluate(d) for d in args.run_dirs])
    args.out.write_text(report, encoding="utf-8")
    print(f"리포트 저장: {args.out}")


if __name__ == "__main__":
    main()
