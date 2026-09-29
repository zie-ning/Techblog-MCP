"""본문 HTML을 LLM 입력과 발췌 검증에 쓸 평문으로 바꾼다.

추출 입력과 발췌 검증이 같은 평문을 써야 LLM이 본 문장을 그대로 검증할 수 있다.
"""

import re

from bs4 import BeautifulSoup, NavigableString

# 내용이 없거나 텍스트로 옮길 수 없는 태그
_DROP_TAGS = ["script", "style", "svg", "picture", "source", "img", "iframe", "video", "noscript"]
# 앞뒤로 줄을 바꾸는 블록 태그
_BLOCK_TAGS = [
    "p", "div", "section", "article", "blockquote", "figure", "figcaption", "ul", "ol",
    "table", "thead", "tbody", "tr", "details", "summary", "center", "hr",
]  # fmt: skip
_FENCE = "```"


def html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup.find_all(_DROP_TAGS):
        tag.decompose()
    # 제목 옆 앵커 링크(#)는 본문이 아니다
    for tag in soup.select("a.anchor"):
        tag.decompose()

    # 코드 블록은 들여쓰기를 보존해야 하므로 펜스로 감싸고 줄 정리에서 제외한다
    for pre in soup.find_all("pre"):
        code = pre.get_text().strip("\n")
        pre.replace_with(NavigableString(f"\n{_FENCE}\n{code}\n{_FENCE}\n"))

    for br in soup.find_all("br"):
        br.replace_with(NavigableString("\n"))
    for level in range(1, 7):
        for h in soup.find_all(f"h{level}"):
            h.insert_before(NavigableString(f"\n\n{'#' * level} "))
            h.insert_after(NavigableString("\n\n"))
    for li in soup.find_all("li"):
        li.insert_before(NavigableString("\n- "))
        li.insert_after(NavigableString("\n"))
    for cell in soup.find_all(["td", "th"]):
        cell.insert_after(NavigableString(" | "))
    for tag in soup.find_all(_BLOCK_TAGS):
        tag.insert_before(NavigableString("\n"))
        tag.insert_after(NavigableString("\n"))

    return _tidy(soup.get_text())


def _tidy(text: str) -> str:
    """코드 블록 밖의 공백을 정리하고 빈 줄은 하나로 줄인다."""
    lines: list[str] = []
    in_code = False
    for line in text.split("\n"):
        if line.strip() == _FENCE:
            in_code = not in_code
            lines.append(_FENCE)
            continue
        if in_code:
            lines.append(line.rstrip())
            continue
        line = re.sub(r"[ \t ​]+", " ", line).strip()
        if line in ("-", "|"):
            continue
        lines.append(line)

    out: list[str] = []
    for line in lines:
        if line == "" and (not out or out[-1] == ""):
            continue
        out.append(line)
    return "\n".join(out).strip()
