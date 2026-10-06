import json
from pathlib import Path

from eval.agent_run import (
    CONDITIONS,
    RunSpec,
    build_command,
    clean_env,
    is_complete,
    mcp_config,
    parse_stream,
    plan_runs,
    rebuild_records,
)
from eval.agent_tasks import Task


def _task(tid: str, category: str = "design", expect_call: str = "required") -> Task:
    return Task(id=tid, category=category, prompt="설계해줘", expect_call=expect_call)


def _lines(*events: dict) -> list[str]:
    return [json.dumps(e, ensure_ascii=False) for e in events]


STREAM = _lines(
    {
        "type": "system",
        "subtype": "init",
        "model": "claude-sonnet-5-5",
        "mcp_servers": [{"name": "techblog", "status": "connected"}],
    },
    {
        "type": "assistant",
        "message": {
            "content": [
                {"type": "text", "text": "사례를 찾겠습니다."},
                {
                    "type": "tool_use",
                    "id": "tu1",
                    "name": "mcp__techblog__search",
                    "input": {"query": "선착순 쿠폰"},
                },
                {"type": "tool_use", "id": "tu2", "name": "WebSearch", "input": {"query": "x"}},
            ]
        },
    },
    {
        "type": "user",
        "message": {
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": "tu1",
                    "content": [{"type": "text", "text": "결과 1건"}],
                },
                {
                    "type": "tool_result",
                    "tool_use_id": "tu2",
                    "content": "denied",
                    "is_error": True,
                },
            ]
        },
    },
    {
        "type": "result",
        "subtype": "success",
        "is_error": False,
        "result": "답변",
        "num_turns": 2,
        "total_cost_usd": 0.1,
        "duration_ms": 1000,
        "permission_denials": [{"tool_name": "WebSearch", "tool_use_id": "tu2"}],
    },
)


def test_plan_runs_limits_no_call_to_mcp():
    tasks = [_task("t01"), _task("t25", "no_call", "forbidden")]
    specs = plan_runs(tasks, ["mcp", "none", "web"], reps=3)
    assert len(specs) == 3 * 3 + 3
    assert {s.condition.name for s in specs if s.task.id == "t25"} == {"mcp"}
    assert specs[0].key == "t01__mcp__r1"


def test_build_command_allows_only_condition_tools(tmp_path: Path):
    config = tmp_path / "mcp.json"
    mcp = build_command("claude", RunSpec(_task("t01"), CONDITIONS["mcp"], 1), "sonnet", config)
    allowed = mcp[mcp.index("--allowedTools") + 1].split()
    assert allowed == [
        "mcp__techblog__search",
        "mcp__techblog__get_details",
        "mcp__techblog__aggregate",
    ]
    assert {"--strict-mcp-config", "--no-session-persistence"} <= set(mcp)
    assert mcp[mcp.index("--permission-mode") + 1] == "dontAsk"

    none = build_command("claude", RunSpec(_task("t01"), CONDITIONS["none"], 1), "sonnet", config)
    assert "--allowedTools" not in none
    web = build_command("claude", RunSpec(_task("t01"), CONDITIONS["web"], 1), "sonnet", config)
    assert web[web.index("--allowedTools") + 1] == "WebSearch WebFetch"


def test_mcp_config_pins_repository_db():
    server = mcp_config(True)["mcpServers"]["techblog"]
    assert server["env"]["TECHBLOG_MCP_DB"].endswith("techblog.sqlite")
    assert mcp_config(False) == {"mcpServers": {}}


def test_clean_env_drops_inherited_session_vars():
    env = {
        "PATH": "p",
        "CLAUDECODE": "1",
        "MCP_CONNECTION_NONBLOCKING": "1",
        "anthropic_base_url": "u",
    }
    assert clean_env(env) == {"PATH": "p"}


def test_parse_stream_extracts_calls_results_and_answer():
    record = parse_stream(STREAM, "t01__mcp__r2")
    assert (record.task_id, record.condition, record.rep) == ("t01", "mcp", 2)
    assert record.model == "claude-sonnet-5-5"
    assert record.mcp_status == "connected"
    assert [c.name for c in record.tool_calls] == ["search", "WebSearch"]
    assert record.tool_calls[0].input == {"query": "선착순 쿠폰"}
    assert record.tool_calls[0].result == "결과 1건"
    assert record.tool_calls[1].is_error
    assert record.denied == ["WebSearch"]
    assert record.answer == "답변"
    assert not record.is_error


def test_parse_stream_without_result_is_error():
    record = parse_stream(STREAM[:2] + ["not json"], "t01__none__r1")
    assert record.is_error
    assert record.result_subtype is None


def test_is_complete_and_rebuild(tmp_path: Path):
    raw = tmp_path / "raw"
    raw.mkdir()
    (raw / "t01__mcp__r1.jsonl").write_text("\n".join(STREAM), encoding="utf-8")
    (raw / "t01__none__r1.jsonl").write_text("\n".join(STREAM[:1]), encoding="utf-8")
    assert is_complete(raw / "t01__mcp__r1.jsonl")
    assert not is_complete(raw / "t01__none__r1.jsonl")
    assert not is_complete(raw / "missing.jsonl")

    records = rebuild_records(tmp_path)
    assert [r.key for r in records] == ["t01__mcp__r1", "t01__none__r1"]
    lines = (tmp_path / "records.jsonl").read_text(encoding="utf-8").splitlines()
    assert json.loads(lines[0])["answer"] == "답변"
