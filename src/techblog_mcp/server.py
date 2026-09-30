"""MCP 서버 진입점: 도구 search, get_details, aggregate와 prompt techblog.

도구 입력 스키마의 문제 유형·도메인 enum은 taxonomy에서 만들어 추출에 쓴 값과 항상 같다.
"""

import sqlite3
from functools import cache
from typing import Annotated, Literal

from mcp.server.mcpserver import MCPServer
from mcp.types import ToolAnnotations
from pydantic import Field

from techblog_mcp import db, render, taxonomy
from techblog_mcp.search import query as q

ProblemType = Literal[taxonomy.problem_type_names()]  # type: ignore[valid-type]
Domain = Literal[taxonomy.domain_names()]  # type: ignore[valid-type]

MAX_DETAIL_IDS = 5  # search 기본 결과 수와 같게 두어 기본 검색 결과를 한 번에 열 수 있게 함

# 세 도구 모두 검색 DB를 읽기만 하고 외부와 통신하지 않는다
READ_ONLY = ToolAnnotations(
    read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=False
)

COMPANIES = "토스, 우아한형제들, 카카오, 카카오페이, 네이버, LY, 컬리, 올리브영"

INSTRUCTIONS = f"""\
국내 IT 기업({COMPANIES}) 기술 블로그의 2023-09 이후 글에서 뽑은 실제 해결 사례와 실무 인사이트를
검색·집계한다. 동시성, 캐싱, 메시징, DB, 장애 대응, LLM 활용처럼 선택지가 있는 설계를 시작하기 전에
search로 비슷한 사례를 확인하고, 필요하면 get_details로 근거를, aggregate로 회사별 채택 현황을 본다.
결과를 인용할 때는 회사명과 원문 링크를 밝히고, 결과에 없는 사례는 지어내지 않는다.
{render.REFERENCE_PRINCIPLE}"""

SEARCH_DESCRIPTION = f"""\
국내 IT 기업 기술 블로그({COMPANIES})에서
실제 해결 사례와 실무 인사이트를 검색한다. (2023-09 이후 글)

동시성, 캐싱, 메시징, DB 마이그레이션, 장애 대응, LLM 활용 등
선택지가 있는 설계를 시작하기 전에 호출해 국내 기업이 비슷한 문제를
어떻게 풀었는지 확인할 것. 단순 CRUD, 버그 수정, 리팩터링에는 호출하지 않는다.

결과는 관련도 순 요약 카드([사례]/[인사이트])이고 근거 발췌는 get_details로 본다.
답변에 소개할 사례는 모두 get_details로 열어 확인한 뒤 인용하고,
카드에 없는 내용을 추측으로 채우지 말 것.
같은 문제에 다른 선택을 한 사례가 있으면 비교 자료로 함께 소개할 가치가 있다.
결과를 인용할 때는 회사명과 원문 링크를 함께 밝히고,
결과에 없는 사례를 지어내지 말 것. 결과가 없거나 적으면 그렇다고 말할 것.
{render.REFERENCE_PRINCIPLE}"""

GET_DETAILS_DESCRIPTION = f"""\
search나 aggregate 결과의 항목 ID(case_0001 형식)로 전체 내용을 조회한다.
한 번에 최대 {MAX_DETAIL_IDS}건.

문제 상황·해결 방법·성능/운영 포인트·버린 대안(사례) 또는 핵심 내용·적용해볼 점(인사이트)을
필드마다 원문 근거 발췌와 함께 돌려주고, 원문 제목·링크와 같은 글의 다른 항목 ID도 알려 준다.
답변에 소개할 사례는 모두 이 도구로 열어 확인할 것. 소개하지 않을 사례까지 열 필요는 없다."""

AGGREGATE_DESCRIPTION = """\
조건에 맞는 사례·인사이트를 기술, 문제 유형, 도메인, 회사, 버린 대안별로 센다.
"Kafka를 쓰는 국내 회사는 몇 곳?", "메시징 문제에 어떤 기술을 많이 쓰나?"처럼
여러 회사의 선택을 비교할 때 호출한다.

모수(전체 건수·회사 수)와 항목별 건수(사례/인사이트 구분)·회사 이름·예시 ID를 돌려준다.
예시 ID는 get_details로 이어서 볼 수 있다. 결과에 없는 수치를 지어내지 말 것."""

server = MCPServer(name="techblog", instructions=INSTRUCTIONS)

QueryArg = Annotated[
    str, Field(description="찾는 문제 상황이나 주제 (자연어). 예: 선착순 쿠폰 발급 동시성")
]
ProblemTypeArg = Annotated[
    ProblemType | None, Field(description="문제 유형 필터. 주 유형과 보조 유형 모두 매칭")
]
DomainArg = Annotated[Domain | None, Field(description="도메인 필터")]
TechnologiesArg = Annotated[
    list[str] | None,
    Field(description="기술 필터 (자유 입력, 예: 카프카 → Kafka). 하나라도 쓴 항목을 찾는다"),
]
KindArg = Annotated[
    Literal["사례", "인사이트", "전체"], Field(description="사례=문제-해결 쌍, 인사이트=실무 팁")
]


@cache
def _connection() -> sqlite3.Connection:
    return db.connect()


def _filters(
    problem_type: str | None, domain: str | None, technologies: list[str] | None, kind: str
) -> tuple[q.Filters, list[str]]:
    resolution = q.resolve_technologies(technologies or [])
    filters = q.Filters(
        problem_type=problem_type,
        domain=domain,
        technologies=resolution.normalized,
        kind=kind,  # type: ignore[arg-type]
    )
    return filters, render.unknown_technologies(resolution)


@server.tool(description=SEARCH_DESCRIPTION, structured_output=False, annotations=READ_ONLY)
def search(
    query: QueryArg,
    problem_type: ProblemTypeArg = None,
    domain: DomainArg = None,
    technologies: TechnologiesArg = None,
    kind: KindArg = "전체",
    limit: Annotated[
        int, Field(ge=1, le=q.MAX_LIMIT, description=f"결과 수 (최대 {q.MAX_LIMIT})")
    ] = q.DEFAULT_LIMIT,
) -> str:
    filters, notes = _filters(problem_type, domain, technologies, kind)
    result = q.search(_connection(), query, filters, limit)
    return render.search_result(query, filters, limit, result, notes)


@server.tool(description=GET_DETAILS_DESCRIPTION, structured_output=False, annotations=READ_ONLY)
def get_details(
    ids: Annotated[
        list[str], Field(min_length=1, description=f"항목 ID 목록. 최대 {MAX_DETAIL_IDS}건")
    ],
) -> str:
    ids = list(dict.fromkeys(i.strip() for i in ids if i.strip()))
    wanted, dropped = ids[:MAX_DETAIL_IDS], ids[MAX_DETAIL_IDS:]
    details, missing = q.get_details(_connection(), wanted)
    return render.details_result(details, missing, dropped, MAX_DETAIL_IDS)


@server.tool(description=AGGREGATE_DESCRIPTION, structured_output=False, annotations=READ_ONLY)
def aggregate(
    group_by: Annotated[q.GroupBy, Field(description="집계 기준")],
    problem_type: ProblemTypeArg = None,
    domain: DomainArg = None,
    technologies: TechnologiesArg = None,
    kind: KindArg = "전체",
    top_n: Annotated[int, Field(ge=1, le=50, description="상위 몇 개까지 보여 줄지")] = 10,
) -> str:
    filters, notes = _filters(problem_type, domain, technologies, kind)
    result = q.aggregate(_connection(), group_by, filters, top_n)
    return render.aggregate_result(group_by, filters, result, notes)


@server.prompt(
    name="techblog",
    description="주제에 대한 국내 기업 사례를 참고 자료로 소개하고, 현재 작업에 맞는 선택지를 "
    "따로 제안한다.",
)
def techblog(topic: Annotated[str, Field(description="찾아볼 설계 주제나 현재 작업")]) -> str:
    return f"""\
다음 주제에 대해 techblog MCP 도구로 국내 기업 사례를 찾아 참고 자료로 소개해 줘: {topic}

1. search로 관련 사례를 찾는다. 결과가 적으면 검색어를 바꾸거나 필터를 빼서 한 번 더 찾는다.
2. 소개할 사례는 모두 get_details로 열어 근거 발췌를 확인한다. 같은 문제에 다른 선택을 한 사례가
   있으면 비교 자료로 함께 연다.
3. 회사별 접근 방식(문제 상황, 해결 방법, 성능·운영 포인트, 버린 대안)을 출처와 함께 소개한다.
4. 각 사례의 조건(규모, 제약, 기존 인프라)이 지금 작업과 어떻게 다른지 짚는다.
5. 사례에 얽매이지 않고, 지금 작업에 맞는 선택지를 트레이드오프와 함께 제안한다.

답변은 "참고 사례"와 "제안"을 나눠서 쓴다. 사례를 그대로 적용하라고 권하지 않는다.
사례를 인용할 때는 회사명과 원문 링크를 밝히고, 도구 결과에 없는 사례는 지어내지 않는다.
찾은 사례가 없거나 적으면 그렇다고 분명히 말한다."""


def main() -> None:
    server.run()
