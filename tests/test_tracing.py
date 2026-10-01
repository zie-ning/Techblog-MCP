import pytest
from test_extract import POST, FakeLLM

from pipeline.extract import tracing
from pipeline.extract.extractor import extract_post
from pipeline.extract.schema import Classification


def test_enable_requires_key(monkeypatch):
    monkeypatch.delenv("LANGSMITH_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        tracing.enable()


def test_enable_sets_default_project(monkeypatch):
    monkeypatch.setenv("LANGSMITH_API_KEY", "test-key")
    monkeypatch.delenv("LANGSMITH_PROJECT", raising=False)
    monkeypatch.delenv("LANGSMITH_TRACING", raising=False)
    assert tracing.enable() == "techblog-mcp"
    # 사용자가 정한 프로젝트가 있으면 그대로 쓴다
    monkeypatch.setenv("LANGSMITH_PROJECT", "mine")
    assert tracing.enable() == "mine"
    monkeypatch.delenv("LANGSMITH_TRACING")


def test_post_extra_and_root_io():
    extra = tracing.post_extra(POST, "run-a", "gpt-5-mini", "medium", "abc123")
    assert extra["name"] == f"extract oliveyoung/{POST.post_id}"
    assert extra["metadata"]["prompt_version"] == "abc123"
    assert "run-a" in extra["tags"]
    # 루트 입력에는 HTML 원문을 넣지 않는다
    inputs = tracing.root_inputs({"post": POST, "llm": object()})
    assert "content_html" not in inputs and inputs["url"] == POST.url


def test_extract_post_accepts_langsmith_extra_when_tracing_off(monkeypatch):
    monkeypatch.delenv("LANGSMITH_TRACING", raising=False)
    llm = FakeLLM([Classification(post_type="회고·문화·행사", kind="제외", reason="회고")])
    extra = tracing.post_extra(POST, "run-a", "fake", "medium", "v")
    result = extract_post(POST, llm, langsmith_extra=extra)
    assert result.record.kind == "제외"
    assert tracing.root_outputs(result)["entries"] == []
