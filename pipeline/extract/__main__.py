"""추출 실행.

    uv run python -m pipeline.extract oliveyoung --limit 20
    uv run python -m pipeline.extract oliveyoung --post-id 2023-09-18_oliveyoung-coupon-rabbit
    uv run python -m pipeline.extract oliveyoung --post-ids-file eval/m1_posts.txt

    uv run python -m pipeline.extract oliveyoung --outdated   # 프롬프트·모델이 바뀐 글도 재추출

    # 평가용: 여러 블로그의 글을 run 디렉터리에 따로 저장 (data/는 건드리지 않음)
    uv run python -m pipeline.extract all --post-ids-file eval/pilot_posts.txt \\
        --out-dir eval/runs/baseline-gpt-5-mini-medium --workers 4 --save-drafts --trace

OPENAI_API_KEY는 환경 변수나 저장소 루트의 `.env`로 설정한다.
이미 추출했고 원문이 바뀌지 않은 글은 건너뛴다(`--outdated`, `--force`로 다시 추출).
실행할 때마다 현재 프롬프트의 스냅샷을 data/prompt_versions/에 남긴다.
글 ID 목록 파일의 줄은 `post_id` 또는 `source/post_id` 형식이다. source가 `all`이면 뒤쪽만 쓴다.
`--trace`를 주면 LangSmith에 글별 트레이스를 남긴다(LANGSMITH_API_KEY 필요, 원문 포함).
"""

import argparse
import os
import sys
from collections.abc import Iterable
from pathlib import Path

from dotenv import load_dotenv

from pipeline.collect import COMPANY_NAMES, raw
from pipeline.extract import prompt_version, tracing
from pipeline.extract.extractor import OpenAILLM
from pipeline.extract.run import DEFAULT_MODEL, extract_all, plan, usage_summary
from pipeline.extract.store import DATA_DIR, Store

ALL = "all"


def parse_post_ids(lines: Iterable[str], default_source: str) -> list[tuple[str, str]]:
    """글 ID 목록을 (source, post_id)로 읽는다. `#` 뒤는 주석이다."""
    ids = []
    for line in lines:
        text = line.split("#")[0].strip()
        if not text:
            continue
        if "/" in text:
            source, post_id = text.split("/", 1)
        elif default_source == ALL:
            raise ValueError(f"source가 all이면 'source/post_id' 형식이어야 합니다: {text}")
        else:
            source, post_id = default_source, text
        ids.append((source, post_id))
    return ids


def select_posts(source: str, wanted: list[tuple[str, str]]) -> list[raw.RawPost]:
    """추출 대상 글. 지정한 글이 없으면 해당 블로그 전체를 최신순으로 돌려준다."""
    sources = list(COMPANY_NAMES) if source == ALL else [source]
    if wanted:
        if others := {s for s, _ in wanted} - set(sources):
            sys.exit(f"지정한 source({source})와 다른 블로그의 글이 있습니다: {sorted(others)}")
        sources = [s for s in sources if any(ws == s for ws, _ in wanted)]
    posts = [p for s in sources for p in raw.load_all(s)]
    if wanted:
        keys = set(wanted)
        posts = [p for p in posts if (p.source, p.post_id) in keys]
        if missing := keys - {(p.source, p.post_id) for p in posts}:
            sys.exit(f"수집되지 않은 글: {', '.join(f'{s}/{i}' for s, i in sorted(missing))}")
    return posts


def main() -> None:
    parser = argparse.ArgumentParser(
        description="수집한 원문을 구조화해 data/entries.jsonl(또는 --out-dir)에 저장한다."
    )
    parser.add_argument("source", choices=[*COMPANY_NAMES, ALL])
    parser.add_argument(
        "--post-id", action="append", default=[], help="특정 글만 (여러 번 지정 가능)"
    )
    parser.add_argument(
        "--post-ids-file",
        type=Path,
        help="글 ID 목록 파일 (한 줄에 post_id 또는 source/post_id, # 주석 가능)",
    )
    parser.add_argument("--limit", type=int, help="추출할 글 수 (건너뛴 글은 세지 않음)")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--reasoning-effort", default="medium")
    parser.add_argument(
        "--outdated", action="store_true", help="다른 프롬프트·모델로 추출한 글도 다시 추출"
    )
    parser.add_argument("--force", action="store_true", help="이미 추출한 글도 모두 다시 추출")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=DATA_DIR,
        help="posts.jsonl·entries.jsonl을 저장할 디렉터리 (기본 data/, 평가는 eval/runs/{run}/)",
    )
    parser.add_argument(
        "--save-drafts", action="store_true", help="검증 전 LLM 출력을 drafts.jsonl에 저장"
    )
    parser.add_argument("--workers", type=int, default=1, help="동시에 추출할 글 수")
    parser.add_argument(
        "--trace", action="store_true", help="LangSmith에 글별 트레이스를 남긴다 (원문 포함)"
    )
    args = parser.parse_args()

    load_dotenv()
    lines = []
    if args.post_ids_file:
        lines = args.post_ids_file.read_text(encoding="utf-8").splitlines()
    try:
        wanted = parse_post_ids([*args.post_id, *lines], args.source)
    except ValueError as e:
        sys.exit(str(e))
    posts = select_posts(args.source, wanted)

    if not os.environ.get("OPENAI_API_KEY"):
        sys.exit("OPENAI_API_KEY가 없습니다. 환경 변수나 저장소 루트의 .env에 설정하세요.")
    if args.trace:
        try:
            project = tracing.enable()
        except RuntimeError as e:
            sys.exit(str(e))
        print(f"LangSmith 트레이싱: 프로젝트 {project}")
    store = Store.in_dir(args.out_dir, save_drafts=args.save_drafts)
    llm = OpenAILLM(args.model, args.reasoning_effort)
    # 기록되는 모든 버전에 스냅샷이 있도록 추출 전에 저장한다
    current_version = prompt_version.save_snapshot()
    print(f"프롬프트 버전: {current_version}, 저장 위치: {args.out_dir}")

    todo = plan(posts, store, llm.model, current_version, args.outdated, args.force, args.limit)
    report = extract_all(
        todo, store, llm, current_version, args.workers, run_name=args.out_dir.name
    )
    print(f"완료: {report.done}/{len(todo)}편 추출. {usage_summary(report.usage)}")


if __name__ == "__main__":
    main()
