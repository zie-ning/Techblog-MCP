import pytest

from pipeline.extract.evidence import SourceText
from pipeline.extract.text import html_to_text


def test_html_to_text_structure():
    html = (
        '<p>첫 문단입니다.</p><img src="a.png">'
        '<h2 id="x"><a href="#x" class="anchor before"><svg><path d="M0"></path></svg></a>'
        "소제목</h2>"
        "<ul><li>항목 <strong>하나</strong></li><li>항목 둘</li></ul>"
        "<p>줄<br>바꿈</p>"
        "<pre><code>def f():\n    return 1</code></pre>"
        "<table><tr><th>A</th><th>B</th></tr><tr><td>1</td><td>2</td></tr></table>"
    )
    text = html_to_text(html)
    assert text.splitlines() == [
        "첫 문단입니다.",
        "",
        "## 소제목",
        "",
        "- 항목 하나",
        "",
        "- 항목 둘",
        "",
        "줄",
        "바꿈",
        "",
        "```",
        "def f():",
        "    return 1",
        "```",
        "",
        "A | B |",
        "",
        "1 | 2 |",
    ]


SOURCE = SourceText(
    "세일 기간에는 초당 최대 3만 건의 요청이 들어왔습니다.\n"
    "그래서 “Redis”의 INCR 명령으로\n발급 수량을 원자적으로 관리했습니다."
)


@pytest.mark.parametrize(
    "evidence",
    [
        "초당 최대 3만 건의 요청이 들어왔습니다.",
        # 줄바꿈·공백 차이
        "그래서 “Redis”의 INCR 명령으로 발급 수량을 원자적으로 관리했습니다.",
        # 따옴표 모양, 마크다운 강조
        '그래서 "Redis"의 **INCR** 명령으로',
        # 중간 생략
        "세일 기간에는 ... 요청이 들어왔습니다.",
        "세일 기간에는…관리했습니다.",
        # 떨어진 문장을 줄바꿈으로 이어 붙임 (순서 무관)
        "발급 수량을 원자적으로 관리했습니다.\n\n초당 최대 3만 건의 요청이 들어왔습니다.",
    ],
)
def test_evidence_found(evidence):
    assert SOURCE.contains(evidence)


@pytest.mark.parametrize(
    "evidence",
    [
        "초당 최대 5만 건의 요청이 들어왔습니다.",  # 수치 변조
        "Redis의 DECR 명령으로 관리했습니다.",  # 지어낸 문장
        "관리했습니다. ... 세일 기간에는",  # 생략 조각의 순서가 원문과 다름
        "세일 ... 다",  # 생략 조각이 너무 짧음
        "초당 최대 3만 건의 요청이 들어왔습니다.\n지어낸 두 번째 문장입니다.",  # 한 줄이라도 없음
        "",
        "\n\n",
    ],
)
def test_evidence_not_found(evidence):
    assert not SOURCE.contains(evidence)


def test_sentence_mode_accepts_separate_sentences_on_one_line():
    # 떨어진 두 문장을 한 줄로 이어 붙인 발췌: 기본 규칙은 탈락, 문장 단위는 통과
    joined = "발급 수량을 원자적으로 관리했습니다. 초당 최대 3만 건의 요청이 들어왔습니다."
    assert not SOURCE.contains(joined)
    assert SOURCE.contains(joined, by_sentence=True)
    # 문장 단위여도 지어낸 문장이 있으면 탈락
    fake = "초당 최대 3만 건의 요청이 들어왔습니다. 지어낸 두 번째 문장입니다."
    assert not SOURCE.contains(fake, by_sentence=True)
