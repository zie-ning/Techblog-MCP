"""추출 스키마.

- LLM 출력 스키마(`Classification`, `CaseExtraction`, `InsightExtraction`):
  OpenAI structured output에 그대로 넘긴다.
  문제 유형·도메인 선택지는 taxonomy에서 만들어 서버의 enum과 항상 같다.
- 저장 스키마(`Entry`, `PostRecord`): 검증·정규화를 거쳐 `data/*.jsonl`에 한 줄씩 저장한다.
"""

from typing import Literal

from pydantic import BaseModel, Field

from techblog_mcp import taxonomy

ProblemType = Literal[taxonomy.problem_type_names()]  # type: ignore[valid-type]
Domain = Literal[taxonomy.domain_names()]  # type: ignore[valid-type]

PostType = Literal[
    "문제 해결형", "기술 선택·도입형", "실험·활용기", "개념·튜토리얼", "회고·문화·행사"
]
PostKind = Literal["사례", "인사이트", "제외"]
EntryKind = Literal["사례", "인사이트"]

MAX_SECONDARY_PROBLEM_TYPES = 2


# ---- LLM 출력 스키마 ----


class Classification(BaseModel):
    post_type: PostType
    kind: PostKind
    reason: str = Field(description="이 유형으로 분류한 이유 한두 문장")


class Point(BaseModel):
    text: str = Field(description="요약 문장. 원문에 근거한 내용만 쓴다")
    evidence: str = Field(description="text의 근거가 되는 원문 문장 1~2개를 글자 그대로 복사")


class RejectedAlternativeDraft(BaseModel):
    name: str = Field(description="검토했지만 채택하지 않은 기술·방식 이름")
    reason: str = Field(description="채택하지 않은 이유")
    evidence: str = Field(description="버린 이유가 드러나는 원문 문장을 글자 그대로 복사")


class _Classified(BaseModel):
    primary_problem_type: ProblemType
    secondary_problem_types: list[ProblemType] = Field(
        description=f"보조 문제 유형. 최대 {MAX_SECONDARY_PROBLEM_TYPES}개, 없으면 빈 목록"
    )
    domain: Domain
    technologies: list[str] = Field(description="이 항목에서 실제로 쓰거나 다룬 기술·제품 이름")
    tags: list[str] = Field(description="검색에 도움이 되는 자유 키워드 3~6개 (한국어 가능)")


class CaseDraft(_Classified):
    problem_situation: list[Point] = Field(
        description="문제 상황. 첫 항목은 문제를 한 줄로 요약. 트래픽·데이터 규모는 원문 표현대로"
    )
    solution: list[Point] = Field(
        description="해결 방법. 최종 채택한 방법만 쓰고 첫 항목은 그 해결책을 한 줄로 요약. "
        "검토만 하고 버린 방법은 rejected_alternatives에 넣는다"
    )
    performance_ops: list[Point] = Field(
        description="성능·운영 포인트: 적용 후 결과(수치 포함)와 운영 주의점. 없으면 빈 목록"
    )
    rejected_alternatives: list[RejectedAlternativeDraft] = Field(
        description="글에 명시적으로 검토 후 버렸다고 나온 대안만. 없으면 빈 목록"
    )


class CaseExtraction(BaseModel):
    cases: list[CaseDraft]


class InsightDraft(_Classified):
    key_points: list[Point] = Field(description="핵심 내용. 첫 항목은 글의 요지를 한 줄로 요약")
    takeaways: list[Point] = Field(description="다른 팀이 적용해볼 점")


class InsightExtraction(BaseModel):
    insight: InsightDraft


# ---- 저장 스키마 ----


class Evidenced(BaseModel):
    text: str
    evidence: str


class RejectedAlternative(BaseModel):
    name: str  # 기술 사전에 있으면 표준 이름, 없으면 원문 이름
    name_raw: str
    reason: str
    evidence: str


class Entry(BaseModel):
    id: str
    kind: EntryKind
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
    # 사례형
    problem_situation: list[Evidenced] = []
    solution: list[Evidenced] = []
    performance_ops: list[Evidenced] = []
    rejected_alternatives: list[RejectedAlternative] = []
    # 인사이트형
    key_points: list[Evidenced] = []
    takeaways: list[Evidenced] = []


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
