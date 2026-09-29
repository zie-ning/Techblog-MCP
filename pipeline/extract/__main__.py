"""추출 실행.

    uv run python -m pipeline.extract oliveyoung --limit 20
    uv run python -m pipeline.extract oliveyoung --post-id 2023-09-18_oliveyoung-coupon-rabbit
    uv run python -m pipeline.extract oliveyoung --post-ids-file eval/m1_posts.txt

    uv run python -m pipeline.extract oliveyoung --outdated   # 프롬프트·모델이 바뀐 글도 재추출

OPENAI_API_KEY는 환경 변수나 저장소 루트의 `.env`로 설정한다.
이미 추출했고 원문이 바뀌지 않은 글은 건너뛴다(`--outdated`, `--force`로 다시 추출).
실행할 때마다 현재 프롬프트의 스냅샷을 data/prompt_versions/에 남긴다.
"""

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from pipeline.collect import raw
from pipeline.extract import prompt_version
from pipeline.extract.extractor import OpenAILLM, extract_post, extraction_reason
from pipeline.extract.store import Store

DEFAULT_MODEL = "gpt-5-mini"  # M1 임시 모델. M3 평가 후 확정한다


def main() -> None:
    parser = argparse.ArgumentParser(
        description="수집한 원문을 구조화해 data/entries.jsonl에 저장한다."
    )
    parser.add_argument("source")
    parser.add_argument(
        "--post-id", action="append", default=[], help="특정 글만 (여러 번 지정 가능)"
    )
    parser.add_argument(
        "--post-ids-file", type=Path, help="글 ID 목록 파일 (한 줄에 하나, # 주석 가능)"
    )
    parser.add_argument("--limit", type=int, help="최신 글부터 N편 (건너뛴 글은 세지 않음)")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--reasoning-effort", default="medium")
    parser.add_argument(
        "--outdated", action="store_true", help="다른 프롬프트·모델로 추출한 글도 다시 추출"
    )
    parser.add_argument("--force", action="store_true", help="이미 추출한 글도 모두 다시 추출")
    args = parser.parse_args()

    load_dotenv()
    posts = raw.load_all(args.source)
    wanted_ids = list(args.post_id)
    if args.post_ids_file:
        lines = args.post_ids_file.read_text(encoding="utf-8").splitlines()
        wanted_ids += [s for line in lines if (s := line.split("#")[0].strip())]
    if wanted_ids:
        wanted = set(wanted_ids)
        posts = [p for p in posts if p.post_id in wanted]
        if missing := wanted - {p.post_id for p in posts}:
            sys.exit(f"수집되지 않은 글: {', '.join(sorted(missing))}")

    if not os.environ.get("OPENAI_API_KEY"):
        sys.exit("OPENAI_API_KEY가 없습니다. 환경 변수나 저장소 루트의 .env에 설정하세요.")
    store = Store()
    llm = OpenAILLM(args.model, args.reasoning_effort)
    # 기록되는 모든 버전에 스냅샷이 있도록 추출 전에 저장한다
    current_version = prompt_version.save_snapshot()
    print(f"프롬프트 버전: {current_version}")
    done = 0
    for post in posts:
        if args.limit is not None and done >= args.limit:
            break
        previous = store.record_for(post.url)
        reason = extraction_reason(previous, post, llm.model, current_version, args.outdated)
        if args.force and reason is None:
            reason = "강제"
        if reason is None:
            continue
        print(f"[{done + 1}] {post.post_id} ({reason}) ... ", end="", flush=True)
        try:
            result = extract_post(post, llm)
        except Exception as e:  # 한 편이 실패해도 나머지는 계속한다
            print(f"실패: {e}")
            continue
        ids = store.add(result)
        store.save()  # 중간에 멈춰도 진행분을 잃지 않도록 매번 저장
        done += 1
        r = result.record
        print(f"{r.kind}/{r.post_type} 항목 {len(ids)}개, 발췌 탈락 {r.dropped_evidence}개")

    print(f"완료: {done}편 추출")


if __name__ == "__main__":
    main()
