"""추출 스키마.

- LLM 출력 스키마(`Classification`, `Extraction`):
  OpenAI structured output에 그대로 넘긴다.
  문제 유형·도메인 선택지는 taxonomy에서 만들어 서버의 enum과 항상 같다.
- 저장 스키마(`Entry`, `PostRecord`): 검증·정규화를 거쳐 `data/*.jsonl`에 한 줄씩 저장한다.
"""

from typing import Literal

from pydantic import BaseModel, Field, model_validator

from techblog_mcp import taxonomy

ProblemType = Literal[taxonomy.problem_type_names()]  # type: ignore[valid-type]
Domain = Literal[taxonomy.domain_names()]  # type: ignore[valid-type]

PostType = Literal[
    "문제 해결형", "기술 선택·도입형", "실험·활용기", "개념·튜토리얼", "회고·문화·행사"
]
# 추출 여부. M3에서 사례·인사이트 구분을 없애고 추출/제외만 판단하기로 했다 (docs/기획.md)
PostKind = Literal["추출", "제외"]
LEGACY_POST_KINDS = ("사례", "인사이트")  # M3 이전 기록의 값. 읽을 때 "추출"로 바꾼다
# 버린 대안 유형: 기술은 집계 대상, 설계 방식은 상세에서만 보여 준다
RejectedKind = Literal["기술", "설계 방식"]

MAX_SECONDARY_PROBLEM_TYPES = 2


# ---- LLM 출력 스키마 ----


class Classification(BaseModel):
    post_type: PostType
    kind: PostKind
    reason: str = Field(description="이 유형으로 분류한 이유 한두 문장")


class Point(BaseModel):
    text: str = Field(description="요약 문장. 원문에 근거한 내용만 쓴다")
    evidence: str = Field(
        description="text의 근거가 되는 원문 문장 1~2개를 글자 그대로 복사. "
        "원문의 한 곳에서 이어지는 문장만, 앞뒤 따옴표 없이"
    )


class RejectedAlternativeDraft(BaseModel):
    name: str = Field(
        description="검토했지만 채택하지 않은 대안의 짧은 이름 (명사구. 예: Kafka, DB 비관적 락)"
    )
    kind: RejectedKind = Field(
        description="기술: 제품·라이브러리·서비스 (예: Kafka, Redis). "
        "설계 방식: 아키텍처·패턴·구현 방식·설정 변경·버전 업그레이드 "
        "(예: Outbox 패턴, DB 비관적 락, nginx 설정으로 차단)"
    )
    reason: str = Field(description="채택하지 않은 이유")
    evidence: str = Field(description="버린 이유가 드러나는 원문 문장을 글자 그대로 복사")


class _Classified(BaseModel):
    primary_problem_type: ProblemType
    secondary_problem_types: list[ProblemType] = Field(
        description=f"보조 문제 유형. 최대 {MAX_SECONDARY_PROBLEM_TYPES}개, 없으면 빈 목록"
    )
    domain: Domain
    technologies: list[str] = Field(
        description="이 항목에서 실제로 쓴 제품·라이브러리·프레임워크·서비스 이름. "
        "클래스·메서드명, 일반 개념, 사내 시스템 이름, 버전 표기는 넣지 않음"
    )
    tags: list[str] = Field(description="검색에 도움이 되는 자유 키워드 3~6개 (한국어 가능)")


class EntryDraft(_Classified):
    problem_situation: list[Point] = Field(
        description="문제 상황. 첫 항목은 문제를 한 줄로 요약. 원문에 나온 트래픽·데이터 규모, "
        "지연·가용성 요구, 기존 인프라·팀 제약은 원문 표현대로 반드시 포함. "
        "특정 문제 없이 팁·활용 경험을 소개하는 글이면 그 배경만 쓰거나 빈 목록"
    )
    solution: list[Point] = Field(
        description="해결 방법. 최종 채택한 방법만 쓰고 첫 항목은 그 해결책을 한 줄로 요약. "
        "팁·활용 경험 글이면 첫 항목은 글의 요지, 이어서 중요한 팁·적용 방법. "
        "검토만 하고 버린 방법은 rejected_alternatives에 넣는다"
    )
    performance_ops: list[Point] = Field(
        description="성능·운영 포인트: 적용 후 확인한 결과(수치 포함)를 먼저, 이어서 운영 주의점. "
        "원문에 없으면 빈 목록"
    )
    rejected_alternatives: list[RejectedAlternativeDraft] = Field(
        description="글에 명시적으로 검토 후 버렸다고 나온 대안만. 없으면 빈 목록"
    )


class Extraction(BaseModel):
    entries: list[EntryDraft]


# ---- 저장 스키마 ----


class Evidenced(BaseModel):
    text: str
    evidence: str


class RejectedAlternative(BaseModel):
    name: str  # 기술이고 기술 사전에 있으면 표준 이름, 아니면 원래 이름
    name_raw: str
    # M3 이전 추출에는 없어 비어 있을 수 있다. 정규화(pipeline.normalize)에서 채운다
    kind: str = ""
    reason: str
    evidence: str


class Entry(BaseModel):
    id: str
    source: str
    company: str
    post_url: str
    post_title: str
    published_at: str  # YYYY-MM-DD
    primary_problem_type: str
    secondary_problem_types: list[str]
    domain: str
    technologies: list[str]  # 기술 사전의 표준 이름
    technologies_raw: list[str]  # 사전에 없는 이름도 포함한 원래 이름 (사전 보강 후 재정규화용)
    tags: list[str]
    problem_situation: list[Evidenced] = []  # 팁·활용 경험 글은 비어 있을 수 있다
    solution: list[Evidenced] = []  # 추출 때 비어 있으면 항목을 버린다 (extractor.verify_draft)
    performance_ops: list[Evidenced] = []
    rejected_alternatives: list[RejectedAlternative] = []

    @model_validator(mode="before")
    @classmethod
    def _from_legacy(cls, data):
        """M3 이전 기록을 읽는다: 사례/인사이트 `kind`를 버리고, 인사이트의 핵심 내용과
        적용해볼 점은 해결 방법으로 옮긴다."""
        if isinstance(data, dict) and "kind" in data:
            data = dict(data)
            del data["kind"]
            key_points, takeaways = data.pop("key_points", []), data.pop("takeaways", [])
            if key_points or takeaways:
                data["solution"] = [*data.get("solution", []), *key_points, *takeaways]
        return data


class Usage(BaseModel):
    """글 한 편을 추출하는 데 쓴 LLM 호출 수와 토큰 (분류 + 구조화 + 재시도 합계)."""

    calls: int = 0
    input_tokens: int = 0
    cached_input_tokens: int = 0
    output_tokens: int = 0
    reasoning_tokens: int = 0  # output_tokens에 포함된 값

    def add(self, other: "Usage") -> None:
        for name in type(self).model_fields:
            setattr(self, name, getattr(self, name) + getattr(other, name))


class PostRecord(BaseModel):
    """추출을 거친 글 한 편의 기록. 제외된 글도 남겨 다시 추출하지 않게 한다."""

    source: str
    post_id: str
    url: str
    title: str
    published_at: str
    post_type: PostType
    kind: PostKind
    reason: str
    content_hash: str
    model: str
    prompt_version: str  # 전문은 data/prompt_versions/{prompt_version}.md
    extracted_at: str
    entry_ids: list[str]
    dropped_evidence: int  # 발췌 검증에 실패해 버린 항목 수
    dropped_evidences: list[str] = []  # 버린 발췌 (검증 기준 점검용)
    # 아래는 M3 평가용으로 추가. M1 기록에는 없어 기본값을 둔다
    reasoning_effort: str = ""
    evidence_total: int = 0  # 채택한 시도의 검증 전 발췌 수 (발췌 원문 존재율의 분모)
    usage: Usage = Usage()

    @model_validator(mode="before")
    @classmethod
    def _from_legacy(cls, data):
        if isinstance(data, dict) and data.get("kind") in LEGACY_POST_KINDS:
            data = {**data, "kind": "추출"}
        return data
