"""형태소 분석기. 색인 빌드(pipeline/build_index.py)와 검색이 반드시 이 함수 하나를 같이 쓴다.

한쪽만 바꾸면 색인된 토큰과 검색어 토큰이 달라져 검색이 깨진다.
"""

from functools import cache

# 검색어로 의미 있는 품사: 명사, 외국어, 한자, 숫자, 어근, 동사·형용사 어간
_KEEP_TAGS = {"NNG", "NNP", "NR", "SL", "SH", "SN", "XR", "VV", "VA"}

# 사용자 사전 (M5 실험 E3). 외래어 기술 용어가 뜻 없는 조각으로 잘리거나(시그널링 → 시그널 + 링),
# 같은 단어가 문장 안과 단독 검색어에서 다르게 잘리는 것(동시성 → 동시, 제로트러스트 → 제로 +
# 트러스트)을 막는다. 합성어(데이터센터 → 데이터 + 센터)처럼 조각에 뜻이 남는 것은 넣지 않는다.
# 단어를 바꾸면 색인도 다시 빌드해야 하므로 SCHEMA_VERSION을 올린다.
USER_WORDS = [
    "동시성",
    "시그널링",
    "아웃박스",
    "서킷브레이커",
    "온콜",
    "리랭킹",
    "멀티플레이",
    "디비지움",
    "커스텀",
    "메트릭",
    "시맨틱",
    "핫픽스",
    "모노리포",
    "스냅샷",
    "스냅숏",
    "워크플로",
    "워크플로우",
    "멀티모달",
    "런타임",
    "오케스트레이션",
    "프라이빗",
    "타임아웃",
    "미러링",
    "타겟팅",
    "스케줄링",
    "페이징",
    "미들웨어",
    "폴리필",
    "샌드박스",
    "헥사고날",
    "핸들링",
    "라벨링",
    "브로드캐스트",
    "롤아웃",
    "컴파일",
    "오토스케일링",
    "프론트엔드",
    "프런트엔드",
    "백오피스",
    "메타데이터",
    "데이터셋",
    "오픈소스",
    "워크로드",
    "헬스체크",
    "크론잡",
    "제로트러스트",
]


@cache
def _kiwi():
    from kiwipiepy import Kiwi  # 불러오는 데 1~2초 걸려 처음 쓸 때 연다

    kiwi = Kiwi()
    for word in USER_WORDS:
        kiwi.add_user_word(word, "NNP", 0)
    return kiwi


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
