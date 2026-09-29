"""MCP 도구 응답 형식 테스트. 실제 MCP 호출 경로(call_tool)로 부른다."""

import asyncio

import pytest
from mcp.server.mcpserver.exceptions import ToolError

from techblog_mcp import db, server


@pytest.fixture(autouse=True)
def use_sample_db(sample_db, monkeypatch):
    monkeypatch.setenv(db.DB_PATH_ENV, str(sample_db))
    server._connection.cache_clear()
    yield
    server._connection.cache_clear()


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
    text = call("search", query="선착순 쿠폰 동시성", limit=1)
    assert "[사례 case_0001] 올리브영 · 2025-03-12 · 동시성·락 / 커머스·주문·재고" in text
    assert "문제 상황: 선착순 쿠폰 발급 시 한도 초과 발급 발생 (초당 최대 3만 요청)" in text
    assert "기술: Redis, Spring Boot" in text
    assert "버린 대안: DB 비관적 락" in text
    assert "원문: https://example.com/coupon" in text
    assert "근거:" not in text  # 카드에는 발췌를 넣지 않는다


def test_search_insight_card():
    text = call("search", query="AI 에이전트", kind="인사이트")
    assert "[인사이트 case_0004]" in text
    assert "핵심 내용: AI 코딩 에이전트의 완료 조건을 측정 가능하게 설계" in text


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
    assert "[사례 case_0001] 선착순 쿠폰 발급 개선기" in text
    assert "## 해결 방법" in text
    assert '근거: "Redis 원자 연산으로 발급 수량 관리"' in text
    assert "## 버린 대안\n- DB 비관적 락: 처리량 부족" in text
    assert "같은 글의 다른 항목: case_0002" in text
    assert "없는 ID: case_0404" in text


def test_get_details_limits_to_three():
    text = call("get_details", ids=["case_0001", "case_0002", "case_0003", "case_0004"])
    assert "제외된 ID: case_0004" in text


def test_aggregate_format():
    text = call("aggregate", group_by="technology", kind="사례")
    assert "조건: 유형 = 사례 → 사례 3건 · 인사이트 0건 / 2개사" in text
    assert "Kafka  사례 1건 · 인사이트 0건 · 1개사 (토스)  예시: case_0003" in text


def test_prompt():
    result = asyncio.run(server.server.get_prompt("techblog", {"topic": "선착순 쿠폰"}))
    text = result.messages[0].content.text
    assert "선착순 쿠폰" in text and "get_details" in text
