"""M7 에이전트 평가 실행기: 과제셋을 조건별로 Claude Code 헤드리스 모드에 풀게 하고 기록을 남긴다.

    uv run python eval/agent_run.py --dry-run               # 실행 계획만 출력
    uv run python eval/agent_run.py --tasks t01 --reps 1    # 일부만 실행
    uv run python eval/agent_run.py                         # 전체 (이미 끝난 실행은 건너뜀)
    uv run python eval/agent_run.py --rebuild               # 원본 로그로 records.jsonl 재생성

조건(mcp·none·web·web-ask)과 실행 옵션의 근거는 docs/기획.md "에이전트 평가 (M7)"와
docs/milestones/M7.md 진행 기록. 결과는 eval/runs/agent/<name>/에 둔다.
- raw/<과제>__<조건>__r<회차>.jsonl: stream-json 원본 (git 제외)
- records.jsonl: 실행마다 도구 호출·결과·답변을 뽑은 기록 (채점 입력, 커밋)
- meta.json: 실행 환경 (Claude Code 버전, 모델, 커밋, DB 체크섬)
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

from pydantic import BaseModel

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 eval 모듈을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from eval.agent_tasks import Task, load_tasks  # noqa: E402

RUNS_DIR = ROOT / "eval" / "runs" / "agent"
DB_PATH = ROOT / "data" / "techblog.sqlite"
MCP_PREFIX = "mcp__techblog__"
MCP_TOOLS = [f"{MCP_PREFIX}{name}" for name in ("search", "get_details", "aggregate")]
WEB_TOOLS = ["WebSearch", "WebFetch"]
# 이 접두어의 환경 변수는 실행 중인 Claude Code 세션(데스크톱 앱 등)에서 물려받은 것이라 뺀다.
# MCP_CONNECTION_NONBLOCKING처럼 결과를 바꿀 수 있는 값이 섞여 있고, 빼도 저장된 로그인은 유지된다
INHERITED_ENV_PREFIXES = ("CLAUDE", "ANTHROPIC", "MCP_")


@dataclass(frozen=True)
class Condition:
    name: str
    mcp: bool
    allowed_tools: tuple[str, ...]
    append_system_prompt: str | None = None


# web 조건에서 에이전트가 웹 검색을 스스로 쓰지 않아(M7 진행 기록), 사례가 필요하면 웹 검색을 쓰라고
# 지시한 조건을 따로 둔다 (사용자 결정). 사용자가 CLAUDE.md에 넣는 지시문과 같은 수준으로만 쓴다
WEB_ASK_PROMPT = (
    "설계처럼 선택지가 있는 작업에서는 답하기 전에 WebSearch로 국내 기업 기술 블로그의 실제 사례를 "
    "찾아본다. 사례를 인용할 때는 회사명과 원문 링크를 밝히고, 찾지 못한 사례는 만들어내지 않는다."
)

CONDITIONS = {
    "mcp": Condition("mcp", mcp=True, allowed_tools=tuple(MCP_TOOLS)),
    "none": Condition("none", mcp=False, allowed_tools=()),
    "web": Condition("web", mcp=False, allowed_tools=tuple(WEB_TOOLS)),
    "web-ask": Condition(
        "web-ask", mcp=False, allowed_tools=tuple(WEB_TOOLS), append_system_prompt=WEB_ASK_PROMPT
    ),
}
# 호출 금지 과제는 techblog 도구가 있을 때만 의미가 있어 mcp 조건만 돌린다 (사용자 결정)
MCP_ONLY_CATEGORIES = {"no_call"}


@dataclass(frozen=True)
class RunSpec:
    task: Task
    condition: Condition
    rep: int

    @property
    def key(self) -> str:
        return f"{self.task.id}__{self.condition.name}__r{self.rep}"


def plan_runs(tasks: list[Task], conditions: list[str], reps: int) -> list[RunSpec]:
    specs = []
    for task in tasks:
        for name in conditions:
            if task.category in MCP_ONLY_CATEGORIES and name != "mcp":
                continue
            for rep in range(1, reps + 1):
                specs.append(RunSpec(task, CONDITIONS[name], rep))
    return specs


# ---------- 실행 ----------


def mcp_config(with_server: bool) -> dict:
    if not with_server:
        return {"mcpServers": {}}
    server = {
        "type": "stdio",
        "command": "uv",
        "args": ["run", "--directory", str(ROOT), "techblog-mcp"],
        # 저장소 DB로 고정한다. 사용자 캐시의 다른 버전 DB를 쓰지 않게 한다
        "env": {"TECHBLOG_MCP_DB": str(DB_PATH)},
    }
    return {"mcpServers": {"techblog": server}}


def build_command(claude: str, spec: RunSpec, model: str, config_path: Path) -> list[str]:
    command = [
        claude,
        "-p",
        spec.task.prompt,
        "--output-format",
        "stream-json",
        "--verbose",
        "--model",
        model,
        "--strict-mcp-config",
        "--mcp-config",
        str(config_path),
        "--setting-sources",
        "project",
        "--settings",
        json.dumps({"autoMemoryEnabled": False}),
        "--permission-mode",
        "dontAsk",
        "--no-session-persistence",
    ]
    if spec.condition.allowed_tools:
        command += ["--allowedTools", " ".join(spec.condition.allowed_tools)]
    if spec.condition.append_system_prompt:
        command += ["--append-system-prompt", spec.condition.append_system_prompt]
    return command


def clean_env(env: dict[str, str]) -> dict[str, str]:
    return {k: v for k, v in env.items() if not k.upper().startswith(INHERITED_ENV_PREFIXES)}


def is_complete(path: Path) -> bool:
    """원본 로그에 최종 result 이벤트가 있으면 끝난 실행으로 본다."""
    if not path.exists():
        return False
    return any(
        _event(line).get("type") == "result"
        for line in path.read_text(encoding="utf-8").splitlines()
    )


def run_one(spec: RunSpec, out_dir: Path, claude: str, model: str, timeout: int) -> Path:
    raw = out_dir / "raw" / f"{spec.key}.jsonl"
    config_path = out_dir / f"mcp_{spec.condition.name}.json"
    command = build_command(claude, spec, model, config_path)
    # 실행마다 새 빈 폴더에서 돌려 이전 실행이 남긴 파일·프로젝트 맥락이 섞이지 않게 한다
    with tempfile.TemporaryDirectory(prefix="techblog-agent-") as workspace:
        try:
            proc = subprocess.run(
                command,
                cwd=workspace,
                env=clean_env(dict(os.environ)),
                stdin=subprocess.DEVNULL,
                capture_output=True,
                timeout=timeout,
            )
            stdout, stderr = proc.stdout, proc.stderr
        except subprocess.TimeoutExpired as e:
            stdout, stderr = e.stdout or b"", (e.stderr or b"") + b"\n[timeout]"
    partial = raw.with_suffix(".part")
    partial.write_bytes(stdout)
    if stderr.strip():
        raw.with_suffix(".err").write_bytes(stderr)
    partial.replace(raw)
    return raw


# ---------- 기록 추출 ----------


class ToolCall(BaseModel):
    id: str
    name: str  # techblog 도구는 접두어를 뗀 이름(search 등)
    input: dict
    result: str | None = None
    is_error: bool = False


class RunRecord(BaseModel):
    key: str
    task_id: str
    condition: str
    rep: int
    model: str | None = None
    mcp_status: str | None = None  # techblog 서버 연결 상태 (mcp 조건만)
    tool_calls: list[ToolCall] = []
    denied: list[str] = []  # 권한 모드에서 거부된 도구 이름 (web 차단 확인용)
    answer: str = ""
    result_subtype: str | None = None
    is_error: bool = False
    num_turns: int | None = None
    cost_usd: float | None = None
    duration_ms: int | None = None


def _event(line: str) -> dict:
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        return {}


def _text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(c.get("text", "") for c in content if isinstance(c, dict))
    return ""


def parse_stream(lines: Iterable[str], spec_key: str) -> RunRecord:
    task_id, condition, rep = spec_key.split("__")
    record = RunRecord(key=spec_key, task_id=task_id, condition=condition, rep=int(rep[1:]))
    calls: dict[str, ToolCall] = {}
    for line in lines:
        event = _event(line)
        kind = event.get("type")
        if kind == "system" and event.get("subtype") == "init":
            record.model = event.get("model")
            for server in event.get("mcp_servers") or []:
                if server.get("name") == "techblog":
                    record.mcp_status = server.get("status")
        elif kind == "assistant":
            for block in event.get("message", {}).get("content", []):
                if block.get("type") == "tool_use":
                    name = block["name"].removeprefix(MCP_PREFIX)
                    call = ToolCall(id=block["id"], name=name, input=block.get("input") or {})
                    calls[call.id] = call
                    record.tool_calls.append(call)
        elif kind == "user":
            content = event.get("message", {}).get("content")
            for block in content if isinstance(content, list) else []:
                if block.get("type") == "tool_result" and block.get("tool_use_id") in calls:
                    call = calls[block["tool_use_id"]]
                    call.result = _text(block.get("content"))
                    call.is_error = bool(block.get("is_error"))
        elif kind == "result":
            record.answer = event.get("result") or ""
            record.result_subtype = event.get("subtype")
            record.is_error = bool(event.get("is_error"))
            record.num_turns = event.get("num_turns")
            record.cost_usd = event.get("total_cost_usd")
            record.duration_ms = event.get("duration_ms")
            record.denied = [d.get("tool_name", "") for d in event.get("permission_denials") or []]
    if record.result_subtype is None:  # 시간 초과 등으로 result 이벤트가 없음
        record.is_error = True
    return record


def rebuild_records(out_dir: Path) -> list[RunRecord]:
    records = []
    for raw in sorted((out_dir / "raw").glob("*.jsonl")):
        lines = raw.read_text(encoding="utf-8").splitlines()
        records.append(parse_stream(lines, raw.stem))
    with (out_dir / "records.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for r in records:
            f.write(r.model_dump_json() + "\n")
    return records


# ---------- 실행 환경 기록 ----------


def _output(command: list[str]) -> str:
    try:
        return subprocess.run(command, capture_output=True, text=True, cwd=ROOT).stdout.strip()
    except OSError:
        return ""


def write_meta(out_dir: Path, claude: str, model: str, reps: int) -> None:
    meta_path = out_dir / "meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    meta.update(
        {
            "claude_code_version": _output([claude, "--version"]),
            "model": model,
            "reps": reps,
            "git_commit": _output(["git", "rev-parse", "HEAD"]),
            "git_dirty": bool(_output(["git", "status", "--porcelain", "--", "src"])),
            "db_sha256": hashlib.sha256(DB_PATH.read_bytes()).hexdigest(),
        }
    )
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ---------- CLI ----------


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--name", default="m7-sonnet", help="실행 묶음 이름 (eval/runs/agent/<name>)"
    )
    parser.add_argument("--model", default="sonnet")
    parser.add_argument("--reps", type=int, default=3)
    parser.add_argument("--jobs", type=int, default=3, help="동시에 띄울 claude 프로세스 수")
    parser.add_argument("--timeout", type=int, default=900, help="실행 1회의 제한 시간(초)")
    parser.add_argument("--tasks", help="쉼표로 구분한 과제 id (기본: 전체)")
    parser.add_argument("--conditions", default="mcp,none,web,web-ask")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--rebuild", action="store_true", help="실행하지 않고 records.jsonl만 다시 만듦"
    )
    args = parser.parse_args()

    out_dir = RUNS_DIR / args.name
    if args.rebuild:
        print(f"기록 {len(rebuild_records(out_dir))}건 → {out_dir / 'records.jsonl'}")
        return

    tasks = load_tasks()
    if args.tasks:
        wanted = set(args.tasks.split(","))
        tasks = [t for t in tasks if t.id in wanted]
    conditions = args.conditions.split(",")
    unknown = [c for c in conditions if c not in CONDITIONS]
    if unknown:
        parser.error(f"알 수 없는 조건: {unknown}")
    specs = plan_runs(tasks, conditions, args.reps)
    todo = [s for s in specs if not is_complete(out_dir / "raw" / f"{s.key}.jsonl")]
    print(f"계획 {len(specs)}회, 남은 실행 {len(todo)}회 → {out_dir}")
    if args.dry_run or not todo:
        return

    claude = shutil.which("claude")
    if claude is None:
        sys.exit("claude 명령을 찾을 수 없습니다")
    (out_dir / "raw").mkdir(parents=True, exist_ok=True)
    for condition in CONDITIONS.values():
        config = json.dumps(mcp_config(condition.mcp), indent=2)
        (out_dir / f"mcp_{condition.name}.json").write_text(config, encoding="utf-8")
    write_meta(out_dir, claude, args.model, args.reps)

    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {
            pool.submit(run_one, s, out_dir, claude, args.model, args.timeout): s for s in todo
        }
        for i, future in enumerate(as_completed(futures), 1):
            spec = futures[future]
            raw = future.result()
            record = parse_stream(raw.read_text(encoding="utf-8").splitlines(), spec.key)
            tools = ",".join(c.name for c in record.tool_calls) or "-"
            status = "오류" if record.is_error else "완료"
            print(
                f"[{i}/{len(todo)}] {spec.key} {status} · 도구 {tools} · {record.duration_ms}ms",
                flush=True,
            )

    records = rebuild_records(out_dir)
    print(f"기록 {len(records)}건 → {out_dir / 'records.jsonl'}")


if __name__ == "__main__":
    main()
