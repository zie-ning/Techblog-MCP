"""MCP 도구 응답 형식 테스트. 실제 MCP 호출 경로(call_tool)로 부른다."""

import asyncio

import pytest
from mcp.server.mcpserver.exceptions import ToolError

from techblog_mcp import db, server


@pytest.fixture(autouse=True)
def use_sample_db(sample_db, monkeypatch):
    monkeypatch.setenv(db.DB_PATH_ENV, str(sample_db))
    server._open_connection.cache_clear()
    yield
    server._open_connection.cache_clear()


def call(name: str, **arguments) -> str:
    result = asyncio.run(server.server.call_tool(name, arguments))
    assert not result.is_error, result
    [content] = result.content
    return content.text


def test_tools_and_prompt_registered():
    tools = asyncio.run(server.server.list_tools())
    assert {t.name for t in tools} == {"search", "get_details", "aggregate"}
    prompts = asyncio.run(server.server.list_prompts())
    assert [p.name for p in prompts] == ["techblog"]


def test_search_card_format():
    text = call("search", query="선착순 쿠폰 동시성")
    assert (
        "[case_0001] 올리브영 · 2025-03-12 · 동시성·락, 트래픽 급증 대응 / 커머스·주문·재고\n"
        "제목: 선착순 쿠폰 발급 개선기\n"
        "문제 상황:"
    ) in text
    assert "문제 상황: 선착순 쿠폰 발급 시 한도 초과 발급 발생 (초당 최대 3만 요청)" in text
    assert "성능·운영: 초과 발급이 0건으로 줄었다" in text
    assert "기술: Redis, Spring Boot" in text
    assert "버린 대안: DB 비관적 락" in text
    assert "원문: https://example.com/coupon" in text
    assert "근거:" not in text  # 카드에는 발췌를 넣지 않는다


def test_search_tip_card_omits_empty_fields():
    text = call("search", query="AI 에이전트 완료 조건")
    assert "[case_0004]" in text
    assert "제목: AI 코딩 에이전트 활용 팁" in text
    assert "해결 방법: AI 코딩 에이전트의 완료 조건을 측정 가능하게 설계" in text
    # 문제 상황·성능·운영 포인트가 없는 항목은 그 줄을 빼서 근거가 약하다는 것이 보인다
    assert "문제 상황:" not in text and "성능·운영:" not in text


def test_search_reports_few_and_empty_results():
    few = call("search", query="정산 적재")
    assert "1건뿐" in few
    empty = call("search", query="쿠폰", domain="배달·물류")
    assert "결과 없음" in empty and "지어내지" in empty


def test_search_unknown_technology_note():
    text = call("search", query="쿠폰", technologies=["Kafak", "레디스"])
    assert "'Kafak'은(는) 기술 사전에 없어" in text
    assert "기술 ∋ Redis" in text


def test_search_rejects_invalid_enum():
    arguments = {"query": "쿠폰", "domain": "없는 도메인"}
    with pytest.raises(ToolError, match="Input should be"):
        asyncio.run(server.server.call_tool("search", arguments))


def test_get_details_format():
    text = call("get_details", ids=["case_0001", "case_0404"])
    assert "[case_0001] 선착순 쿠폰 발급 개선기" in text
    assert "## 해결 방법" in text
    assert '근거: "Redis 원자 연산으로 발급 수량 관리"' in text
    assert "## 버린 대안\n- DB 비관적 락 (설계 방식): 처리량 부족" in text
    assert "같은 글의 다른 항목: case_0002" in text
    assert "없는 ID: case_0404" in text


def test_get_details_limits_to_five():
    ids = ["case_0001", "case_0002", "case_0003", "case_0004", "case_0404", "case_0405"]
    text = call("get_details", ids=ids)
    assert "[case_0003]" in text and "[case_0004]" in text
    assert "없는 ID: case_0404" in text
    assert "한 번에 5건까지만 조회합니다. 제외된 ID: case_0405" in text


def test_aggregate_format():
    text = call("aggregate", group_by="technology")
    assert "조건: 조건 없음 → 4건 (수치 있는 성능·운영 포인트 1) / 2개사" in text
    assert "Kafka  1건 (수치 있는 성능·운영 포인트 0) · 1개사 (토스)  예시: case_0003" in text


def test_aggregate_by_company_omits_redundant_company_list():
    text = call("aggregate", group_by="company")
    assert "1. 올리브영  3건 (수치 있는 성능·운영 포인트 1)  예시:" in text
    assert "개사 (올리브영)" not in text


def test_tools_are_marked_read_only():
    for tool in asyncio.run(server.server.list_tools()):
        assert tool.annotations.read_only_hint is True
        assert tool.annotations.destructive_hint is False


def test_descriptions_ask_to_open_every_cited_case():
    tools = {t.name: t for t in asyncio.run(server.server.list_tools())}
    assert "소개할 사례는 모두 get_details로 열어" in tools["search"].description
    assert "다른 선택을 한 사례" in tools["search"].description
    assert "최대 5건" in tools["get_details"].description


def test_prompt():
    result = asyncio.run(server.server.get_prompt("techblog", {"topic": "선착순 쿠폰"}))
    text = result.messages[0].content.text
    assert "선착순 쿠폰" in text and "get_details" in text


def test_reference_principle_is_communicated():
    # 사례는 참고 자료라는 원칙이 서버 안내·search 설명·결과·prompt에 모두 들어 있어야 한다
    from techblog_mcp import render

    assert render.REFERENCE_PRINCIPLE in server.INSTRUCTIONS
    tools = {t.name: t for t in asyncio.run(server.server.list_tools())}
    assert render.REFERENCE_PRINCIPLE in tools["search"].description
    assert "설계 판단의 근거로" not in tools["get_details"].description

    assert render.REFERENCE_RULE in call("search", query="선착순 쿠폰")
    assert render.REFERENCE_RULE in call("get_details", ids=["case_0001"])

    prompt = asyncio.run(server.server.get_prompt("techblog", {"topic": "쿠폰"}))
    text = prompt.messages[0].content.text
    assert '"참고 사례"와 "제안"을 나눠서' in text
    assert "그대로 적용하라고 권하지 않는다" in text


@pytest.fixture
def family_db(tmp_path, monkeypatch):
    from conftest import make_entry

    from pipeline.build_index import build

    path = tmp_path / "families.sqlite"
    build(
        [
            make_entry("case_0001", technologies=["Kafka"]),
            make_entry("case_0002", technologies=["Amazon MSK"]),
        ],
        path,
    )
    monkeypatch.setenv(db.DB_PATH_ENV, str(path))
    server._open_connection.cache_clear()


def test_aggregate_technology_shows_family_members(family_db):
    text = call("aggregate", group_by="technology")
    assert "1. Kafka  2건" in text and "포함: Amazon MSK 1" in text
    assert "Amazon MSK는 Kafka 계열" in text


def test_technology_filter_expands_family(family_db):
    # 상위 기술 필터는 계열 전체를 찾아 집계의 계열 합산과 숫자가 맞는다 (M6 결정)
    text = call("aggregate", group_by="company", technologies=["카프카"])
    assert "기술 ∋ Kafka 계열 → 2건" in text
    # 하위 기술로 거르면 그 기술만
    text = call("aggregate", group_by="company", technologies=["Amazon MSK"])
    assert "기술 ∋ Amazon MSK → 1건" in text


def test_prepare_survives_missing_db(tmp_path, monkeypatch):
    # 기동 때 백그라운드 준비가 실패해도 서버가 죽지 않고, 도구 호출에서 이유를 알린다
    monkeypatch.setenv(db.DB_PATH_ENV, str(tmp_path / "none.sqlite"))
    server._open_connection.cache_clear()
    for thread in server._prepare():
        thread.join()
    with pytest.raises(ToolError, match="검색 DB가 없습니다"):
        asyncio.run(server.server.call_tool("search", {"query": "쿠폰"}))
