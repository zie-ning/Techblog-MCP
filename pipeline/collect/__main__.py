"""수집 실행.

uv run python -m pipeline.collect oliveyoung
uv run python -m pipeline.collect all             # 8곳 모두
uv run python -m pipeline.collect kakao --refresh # 캐시된 글도 다시 받기
"""

import argparse
import sys

from pipeline.collect.http import PoliteClient
from pipeline.collect.run import COLLECTORS, collect_sources


def main() -> None:
    parser = argparse.ArgumentParser(description="기술 블로그 원문을 data/raw/에 수집한다.")
    parser.add_argument("sources", nargs="+", choices=["all", *sorted(COLLECTORS)])
    parser.add_argument(
        "--refresh", action="store_true", help="이미 캐시된 글도 다시 받아 덮어쓴다"
    )
    args = parser.parse_args()
    sources = sorted(COLLECTORS) if "all" in args.sources else args.sources

    with PoliteClient() as client:
        report = collect_sources(client, sources, refresh=args.refresh)
    if report.failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
