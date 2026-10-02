"""M3 파일럿 표본 추출: 블로그마다 시드를 고정해 무작위로 N편을 뽑는다.

    uv run python eval/sample_pilot.py            # eval/pilot_posts.txt 생성

올리브영은 M1에서 이미 추출한 20편(eval/m1_posts.txt)을 빼고 뽑는다.
각 줄 주석에 제목과 평문 길이를 남겨 짧은 글이 몇 편 들어갔는지 바로 보이게 한다.
"""

import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 pipeline을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from pipeline.collect import COMPANY_NAMES, raw  # noqa: E402
from pipeline.extract.text import html_to_text  # noqa: E402

SEED = 20260930
PER_SOURCE = 10
SHORT_TEXT = 1500  # M2에서 넘어온 "본문이 짧은 글" 기준 (평문 글자 수)
M1_POSTS = ROOT / "eval" / "m1_posts.txt"
OUT = ROOT / "eval" / "pilot_posts.txt"


def read_ids(path: Path) -> set[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return {s for line in lines if (s := line.split("#")[0].strip())}


def sample_posts(
    posts: list[raw.RawPost], source: str, n: int, seed: int = SEED, exclude: set[str] = frozenset()
) -> list[raw.RawPost]:
    """시드와 블로그 이름으로 정해지는 무작위 표본. 결과는 발행일 순으로 정렬한다."""
    candidates = sorted((p for p in posts if p.post_id not in exclude), key=lambda p: p.post_id)
    picked = random.Random(f"{seed}:{source}").sample(candidates, min(n, len(candidates)))
    return sorted(picked, key=lambda p: p.published_at)


def main() -> None:
    m1 = read_ids(M1_POSTS)
    lines = [
        f"# M3 파일럿 표본: 블로그당 {PER_SOURCE}편, 시드 {SEED} (eval/sample_pilot.py로 생성)",
        "# 형식: source/post_id  # 발행일 | 평문 길이 | 제목 (짧은 글은 [짧음] 표시)",
    ]
    short = 0
    for source in COMPANY_NAMES:
        exclude = m1 if source == "oliveyoung" else set()
        picked = sample_posts(raw.load_all(source), source, PER_SOURCE, exclude=exclude)
        lines.append(f"\n# {source}")
        for p in picked:
            length = len(html_to_text(p.content_html))
            mark = " [짧음]" if length < SHORT_TEXT else ""
            short += bool(mark)
            date = p.published_at.date().isoformat()
            lines.append(f"{source}/{p.post_id}  # {date} | {length:,}자{mark} | {p.title}")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)} 저장: 짧은 글(<{SHORT_TEXT}자) {short}편 포함")


if __name__ == "__main__":
    main()
