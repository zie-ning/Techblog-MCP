"""M4 분류 목록 검토용 표본: 블로그당 25편.

    uv run python eval/sample_m4.py            # eval/m4_sample_posts.txt 생성

M3 파일럿 10편(eval/pilot_posts.txt)을 그대로 넣고, 나머지를 같은 방식의 무작위 표본으로 채운다.
올리브영 M1 20편은 따로 재추출하므로 표본에서 뺀다.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 pipeline을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from eval.sample_pilot import M1_POSTS, SHORT_TEXT, read_ids, sample_posts  # noqa: E402
from pipeline.collect import COMPANY_NAMES, raw  # noqa: E402
from pipeline.extract.text import html_to_text  # noqa: E402

SEED = 20261002
PER_SOURCE = 25
PILOT_POSTS = ROOT / "eval" / "pilot_posts.txt"
OUT = ROOT / "eval" / "m4_sample_posts.txt"


def main() -> None:
    pilot = read_ids(PILOT_POSTS)
    m1 = read_ids(M1_POSTS)
    lines = [
        f"# M4 표본: 블로그당 {PER_SOURCE}편, M3 파일럿 + 시드 {SEED} 무작위 (eval/sample_m4.py)",
        "# 형식: source/post_id  # 발행일 | 평문 길이 | 제목 ([짧음] 짧은 글, [파일럿] M3 파일럿)",
    ]
    total = short = 0
    for source in COMPANY_NAMES:
        posts = raw.load_all(source)
        in_pilot = [p for p in posts if f"{source}/{p.post_id}" in pilot]
        exclude = {p.post_id for p in in_pilot} | (m1 if source == "oliveyoung" else set())
        extra = sample_posts(posts, source, PER_SOURCE - len(in_pilot), seed=SEED, exclude=exclude)
        lines.append(f"\n# {source}")
        for p in sorted(in_pilot + extra, key=lambda p: p.published_at):
            length = len(html_to_text(p.content_html))
            marks = " [짧음]" if length < SHORT_TEXT else ""
            marks += " [파일럿]" if p in in_pilot else ""
            short += length < SHORT_TEXT
            total += 1
            date = p.published_at.date().isoformat()
            lines.append(f"{source}/{p.post_id}  # {date} | {length:,}자{marks} | {p.title}")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)} 저장: {total}편, 짧은 글(<{SHORT_TEXT}자) {short}편 포함")


if __name__ == "__main__":
    main()
