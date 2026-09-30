"""추출 실행.

    uv run python -m pipeline.extract oliveyoung --limit 20
    uv run python -m pipeline.extract oliveyoung --post-id 2023-09-18_oliveyoung-coupon-rabbit
    uv run python -m pipeline.extract oliveyoung --post-ids-file eval/m1_posts.txt

    uv run python -m pipeline.extract oliveyoung --outdated   # 프롬프트·모델이 바뀐 글도 재추출

    # 평가용: 여러 블로그의 글을 run 디렉터리에 따로 저장 (data/는 건드리지 않음)
    uv run python -m pipeline.extract all --post-ids-file eval/pilot_posts.txt \\
        --out-dir eval/runs/baseline-gpt-5-mini-medium --workers 4 --save-drafts

OPENAI_API_KEY는 환경 변수나 저장소 루트의 `.env`로 설정한다.
이미 추출했고 원문이 바뀌지 않은 글은 건너뛴다(`--outdated`, `--force`로 다시 추출).
실행할 때마다 현재 프롬프트의 스냅샷을 data/prompt_versions/에 남긴다.
글 ID 목록 파일의 줄은 `post_id` 또는 `source/post_id` 형식이다. source가 `all`이면 뒤쪽만 쓴다.
"""

import argparse
import os
import sys
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from dotenv import load_dotenv

from pipeline.collect import COMPANY_NAMES, raw
from pipeline.extract import prompt_version
from pipeline.extract.extractor import OpenAILLM, extract_post, extraction_reason
from pipeline.extract.schema import Usage
from pipeline.extract.store import DATA_DIR, Store

DEFAULT_MODEL = "gpt-5-mini"  # M1 임시 모델. M3 평가 후 확정한다
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
    store = Store.in_dir(args.out_dir, save_drafts=args.save_drafts)
    llm = OpenAILLM(args.model, args.reasoning_effort)
    # 기록되는 모든 버전에 스냅샷이 있도록 추출 전에 저장한다
    current_version = prompt_version.save_snapshot()
    print(f"프롬프트 버전: {current_version}, 저장 위치: {args.out_dir}")

    todo = []
    for post in posts:
        if args.limit is not None and len(todo) >= args.limit:
            break
        previous = store.record_for(post.url)
        reason = extraction_reason(previous, post, llm.model, current_version, args.outdated)
        if args.force and reason is None:
            reason = "강제"
        if reason is not None:
            todo.append((post, reason))

    done = 0
    total_usage = Usage()
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {pool.submit(extract_post, post, llm): (post, reason) for post, reason in todo}
        # 저장은 메인 스레드에서만 한다
        for n, future in enumerate(as_completed(futures), 1):
            post, reason = futures[future]
            label = f"[{n}/{len(todo)}] {post.source}/{post.post_id} ({reason})"
            try:
                result = future.result()
            except Exception as e:  # 한 편이 실패해도 나머지는 계속한다
                print(f"{label} 실패: {e}")
                continue
            ids = store.add(result)
            store.save()  # 중간에 멈춰도 진행분을 잃지 않도록 매번 저장
            done += 1
            r = result.record
            total_usage.add(r.usage)
            print(
                f"{label} {r.kind}/{r.post_type} 항목 {len(ids)}개, "
                f"발췌 탈락 {r.dropped_evidence}/{r.evidence_total}개"
            )

    u = total_usage
    print(
        f"완료: {done}/{len(todo)}편 추출. 호출 {u.calls}회, 입력 {u.input_tokens:,}"
        f"(캐시 {u.cached_input_tokens:,}) / 출력 {u.output_tokens:,}"
        f"(reasoning {u.reasoning_tokens:,}) 토큰"
    )


if __name__ == "__main__":
    main()
