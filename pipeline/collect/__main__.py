"""수집 실행: `uv run python -m pipeline.collect oliveyoung`"""

import argparse

from pipeline.collect import oliveyoung
from pipeline.collect.http import PoliteClient

COLLECTORS = {
    oliveyoung.SOURCE: oliveyoung.collect,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="기술 블로그 원문을 data/raw/에 수집한다.")
    parser.add_argument("sources", nargs="+", choices=sorted(COLLECTORS))
    args = parser.parse_args()

    with PoliteClient() as client:
        for source in args.sources:
            posts = COLLECTORS[source](client)
            oldest = min((p.published_at for p in posts), default=None)
            print(f"{source}: {len(posts)}편 저장 (가장 오래된 글: {oldest:%Y-%m-%d})")


if __name__ == "__main__":
    main()
