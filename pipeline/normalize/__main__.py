"""기술명 재정규화와 미등록 이름 리포트.

    uv run python -m pipeline.normalize          # 리포트만
    uv run python -m pipeline.normalize --apply  # 현재 사전으로 entries.jsonl 다시 정규화

기술 사전(`src/techblog_mcp/taxonomy/technologies.toml`)을 보강한 뒤 --apply로 반영하면
LLM을 다시 호출하지 않고 정규화 결과를 갱신할 수 있다.
"""

import argparse
from collections import Counter

from pipeline.extract.store import Store
from pipeline.normalize import renormalize


def main() -> None:
    parser = argparse.ArgumentParser(description="기술 사전에 없는 기술 이름을 집계한다.")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    store = Store()
    unknown: Counter[str] = Counter()
    for i, entry in enumerate(store.entries):
        store.entries[i], missing = renormalize(entry)
        unknown.update(missing)

    if args.apply:
        store.save()
        print(f"{len(store.entries)}개 항목을 다시 정규화했습니다.")

    print(f"사전에 없는 기술 이름 {len(unknown)}종:")
    for name, count in unknown.most_common():
        print(f"  {count:3d}  {name}")


if __name__ == "__main__":
    main()
