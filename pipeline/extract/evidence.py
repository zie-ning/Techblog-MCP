"""발췌 검증: LLM이 낸 근거 발췌가 원문에 실제로 있는지 코드로 검사한다.

LLM이 지어낸 내용을 거르는 핵심 장치이므로 기준을 느슨하게 바꿀 때는 신중해야 한다.
허용하는 차이는 표기 차이뿐이다.
- 공백·줄바꿈 (HTML을 평문으로 바꾸며 달라질 수 있음)
- 유니코드 호환 문자, 따옴표 모양, 대소문자
- 마크다운 강조 기호 (`**`, `` ` ``)
- 중간 생략: "A ... B"는 A와 B가 원문에 이 순서로 있으면 통과
- 여러 줄: 줄마다 원문에 있으면 통과 (떨어진 문장을 줄바꿈으로 이어 붙인 경우)
"""

import re
import unicodedata

_QUOTES = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "`": "", "*": ""})
_ELLIPSIS = re.compile(r"\s*(?:\.{3,}|…|⋯)\s*")
# 생략으로 잘린 조각이 너무 짧으면 아무 데나 우연히 맞으므로 인정하지 않는다
_MIN_SEGMENT = 4


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).translate(_QUOTES)
    return re.sub(r"\s+", "", text).casefold()


class SourceText:
    """원문 한 편. 여러 발췌를 검사할 때 정규화를 한 번만 한다."""

    def __init__(self, text: str):
        self._normalized = normalize(text)

    def contains(self, evidence: str) -> bool:
        # 줄바꿈으로 이어 붙인 발췌는 떨어진 문장을 모은 것이므로 줄마다 따로 찾는다
        lines = [line for line in evidence.splitlines() if line.strip()]
        return bool(lines) and all(self._contains_line(line) for line in lines)

    def _contains_line(self, evidence: str) -> bool:
        segments = [normalize(s) for s in _ELLIPSIS.split(evidence)]
        segments = [s for s in segments if s]
        if not segments or any(len(s) < _MIN_SEGMENT for s in segments):
            return False
        pos = 0
        for segment in segments:
            found = self._normalized.find(segment, pos)
            if found < 0:
                return False
            pos = found + len(segment)
        return True
