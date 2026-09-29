"""형태소 분석기. 색인 빌드(pipeline/build_index.py)와 검색이 반드시 이 함수 하나를 같이 쓴다.

한쪽만 바꾸면 색인된 토큰과 검색어 토큰이 달라져 검색이 깨진다.
"""

from functools import cache

# 검색어로 의미 있는 품사: 명사, 외국어, 한자, 숫자, 어근, 동사·형용사 어간
_KEEP_TAGS = {"NNG", "NNP", "NR", "SL", "SH", "SN", "XR", "VV", "VA"}


@cache
def _kiwi():
    from kiwipiepy import Kiwi  # 불러오는 데 1~2초 걸려 처음 쓸 때 연다

    return Kiwi()


def tokenize(text: str) -> list[str]:
    tokens = []
    for token in _kiwi().tokenize(text):
        # 불규칙 활용 표시(VV-R, VA-I 등)는 떼고 본다
        if token.tag.split("-")[0] in _KEEP_TAGS:
            tokens.append(token.form.casefold())
    return tokens


def analyze(text: str) -> str:
    """FTS5 색인에 넣을 형태: 토큰을 공백으로 이은 문자열."""
    return " ".join(tokenize(text))
