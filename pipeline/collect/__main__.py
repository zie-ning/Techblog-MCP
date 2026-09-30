"""수집 실행.

uv run python -m pipeline.collect oliveyoung
uv run python -m pipeline.collect all             # 8곳 모두
uv run python -m pipeline.collect kakao --refresh # 캐시된 글도 다시 받기
"""

import argparse
import sys

import httpx

from pipeline.collect import d2, oliveyoung, raw, toss, woowahan
from pipeline.collect.http import DisallowedByRobots, PoliteClient

COLLECTORS = {
    d2.SOURCE: d2.collect,
    oliveyoung.SOURCE: oliveyoung.collect,
    toss.SOURCE: toss.collect,
    woowahan.SOURCE: woowahan.collect,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="기술 블로그 원문을 data/raw/에 수집한다.")
    parser.add_argument("sources", nargs="+", choices=["all", *sorted(COLLECTORS)])
    parser.add_argument(
        "--refresh", action="store_true", help="이미 캐시된 글도 다시 받아 덮어쓴다"
    )
    args = parser.parse_args()
    sources = sorted(COLLECTORS) if "all" in args.sources else args.sources

    failed = False
    with PoliteClient() as client:
        for source in sources:
            try:
                result = COLLECTORS[source](client, refresh=args.refresh)
            except (httpx.HTTPError, DisallowedByRobots, ValueError) as e:
                # 목록 요청 자체가 막히면 그 블로그만 실패로 두고 나머지는 계속 수집한다
                failed = True
                print(f"{source}: 수집 실패 ({type(e).__name__}: {e})", file=sys.stderr)
                continue
            oldest = min((p.published_at for p in result.saved), default=None)
            summary = f"{source}: {len(result.saved)}편 저장"
            if oldest:
                summary += f" (가장 오래된 글: {oldest.astimezone(raw.KST):%Y-%m-%d})"
            if result.skipped:
                summary += f", 캐시 {result.skipped}편 건너뜀"
            if result.out_of_period:
                summary += f", 기간 밖 {result.out_of_period}편"
            print(summary)
            for url, reason in result.failures:
                failed = True
                print(f"  실패 {url}: {reason}", file=sys.stderr)
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
