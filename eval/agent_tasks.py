"""M7 에이전트 평가 과제셋(eval/agent/tasks.toml)을 읽고 검증한다.

    uv run python eval/agent_tasks.py  # 과제 목록과 관련 사례 수 출력

형식과 기준은 eval/agent/README.md.
과제의 관련 사례는 검색 평가셋(eval/search/queries.toml)의 라벨을 search_refs로 가져와 쓴다.
"""

import sys
import tomllib
from pathlib import Path
from typing import Literal

from pydantic import BaseModel

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 eval 모듈을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from eval.search_eval import EvalQuery, load_queries  # noqa: E402

TASKS_PATH = ROOT / "eval" / "agent" / "tasks.toml"

Category = Literal["design", "few", "noise", "aggregate", "absent", "no_call", "concept"]
ExpectCall = Literal["required", "forbidden", "optional"]
Tool = Literal["search", "get_details", "aggregate"]

# 분류마다 기대하는 호출 여부. 과제마다 따로 정하지 않고 분류로 고정해 채점 기준을 맞춘다
EXPECT_CALL_BY_CATEGORY: dict[str, ExpectCall] = {
    "design": "required",
    "few": "required",
    "noise": "required",
    "aggregate": "required",
    "absent": "optional",
    "no_call": "forbidden",
    "concept": "optional",
}

# 같은 사례가 여러 질의에서 다른 등급을 받으면 높은 쪽을 쓴다
GRADE_RANK = {"관련": 2, "일부 관련": 1}


class Task(BaseModel):
    id: str
    category: Category
    prompt: str
    expect_call: ExpectCall
    expect_tool: Tool | None = None
    search_refs: list[str] = []
    source: str = ""
    check: str = ""


def load_tasks(path: Path = TASKS_PATH, queries: list[EvalQuery] | None = None) -> list[Task]:
    """과제셋을 읽고 검증한다. 문제가 있으면 모두 모아 ValueError로 알린다."""
    raw = tomllib.loads(path.read_text(encoding="utf-8"))
    tasks = [Task(**t) for t in raw.get("tasks", [])]
    by_query = {q.id: q for q in (load_queries() if queries is None else queries)}
    errors = validate(tasks, by_query)
    if errors:
        raise ValueError("과제셋 오류:\n" + "\n".join(f"- {e}" for e in errors))
    return tasks


def validate(tasks: list[Task], queries: dict[str, EvalQuery]) -> list[str]:
    errors = []
    seen: set[str] = set()
    for t in tasks:
        if t.id in seen:
            errors.append(f"{t.id}: id 중복")
        seen.add(t.id)
        expected = EXPECT_CALL_BY_CATEGORY[t.category]
        if t.expect_call != expected:
            errors.append(f"{t.id}: {t.category} 과제의 expect_call은 {expected}여야 함")
        missing = [r for r in t.search_refs if r not in queries]
        if missing:
            errors.append(f"{t.id}: 검색 평가셋에 없는 질의 {missing}")
        if t.category == "absent":
            graded = relevant_ids(t, queries)
            if any(g == "관련" for g in graded.values()):
                errors.append(f"{t.id}: 없는 주제인데 '관련' 사례가 있음")
    return errors


def relevant_ids(task: Task, queries: dict[str, EvalQuery]) -> dict[str, str]:
    """과제에 연결된 질의 라벨을 합친 {사례 ID: 등급}. '무관'은 넣지 않는다."""
    merged: dict[str, str] = {}
    for ref in task.search_refs:
        q = queries.get(ref)
        if q is None:
            continue
        for case_id, label in q.labels.items():
            if label.grade not in GRADE_RANK:
                continue
            prev = merged.get(case_id)
            if prev is None or GRADE_RANK[label.grade] > GRADE_RANK[prev]:
                merged[case_id] = label.grade
    return merged


def main() -> None:
    queries = {q.id: q for q in load_queries()}
    tasks = load_tasks(queries=list(queries.values()))
    for t in tasks:
        graded = relevant_ids(t, queries)
        full = sum(g == "관련" for g in graded.values())
        counts = f"관련 {full:>2} · 일부 {len(graded) - full:>2}"
        print(f"{t.id}  {t.category:<9} {t.expect_call:<9} {counts}  {t.prompt[:40]}")
    print(f"\n과제 {len(tasks)}개")


if __name__ == "__main__":
    main()
