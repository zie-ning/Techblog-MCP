"""문서 확장: 항목마다 LLM이 예상 검색어와 본문에 없는 다른 표기·동의어를 만든다.

    uv run python -m pipeline.expand          # 새 항목·내용이 바뀐 항목·지시문이 바뀐 항목만 생성
    uv run python -m pipeline.expand --dry-run

결과는 data/expansions.jsonl(커밋)에 두고, build_index가 `expansion` FTS 열로 색인한다.
단어로 맞춰 찾는 검색에서 "제로트러스트"로 물었는데 글에는 "Zero Trust"만 있거나, 글과 다른 말로
물어 못 찾는 경우를 메운다 (M5 실험 E7, docs/기획.md "검색").
확장은 검색 보조 정보일 뿐이라 원문 발췌 검증 대상이 아니고, 카드·상세에는 보여 주지 않는다.
OPENAI_API_KEY는 환경 변수나 저장소 루트의 `.env`로 설정한다.
"""

import argparse
import hashlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, Field

from pipeline.extract.schema import Entry, Usage
from pipeline.extract.store import DATA_DIR, ENTRIES_PATH, Store

EXPANSIONS_PATH = DATA_DIR / "expansions.jsonl"
DEFAULT_MODEL = "gpt-5.6-luna"  # 추출과 같은 모델. 짧은 생성이라 추론 강도는 low
REASONING_EFFORT = "low"
WORKERS = 8

INSTRUCTIONS = """\
국내 IT 기업 기술 블로그의 해결 사례 하나가 주어진다. 코딩 에이전트가 설계를 시작하기 전에
이 사례를 검색으로 찾을 수 있도록 검색 보조 정보를 만든다.

- queries: 이 사례가 답이 될 만한 검색어 5개. 개발자가 검색창에 넣을 법한 짧은 한국어 문장이나
  명사구로, 사례의 핵심 문제와 해결을 서로 다른 표현으로 쓴다.
- terms: 사례 본문에 없지만 같은 개념을 가리키는 용어 최대 10개. 한국어↔영어 표기
  (예: 제로트러스트 ↔ Zero Trust), 약어와 원래 이름, 흔히 쓰는 동의어, 바로 위 상위 개념.

사례에 없는 다른 주제나 기술을 지어내지 않는다. 사례가 다루지 않는 문제를 검색어로 만들지 않는다.
"""


class Expansion(BaseModel):
    queries: list[str] = Field(description="이 사례를 찾을 검색어 5개")
    terms: list[str] = Field(description="본문에 없는 다른 표기·동의어·상위 개념, 최대 10개")


class ExpansionRecord(BaseModel):
    entry_id: str
    input_hash: str  # 입력 텍스트(expansion_input) 해시. 항목 내용이 바뀌면 다시 만든다
    prompt_hash: str  # 지시문·출력 스키마 해시. 지시문을 고치면 다시 만든다
    model: str
    queries: list[str]
    terms: list[str]


def _hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def prompt_hash() -> str:
    schema = json.dumps(Expansion.model_json_schema(), ensure_ascii=False, sort_keys=True)
    return _hash(INSTRUCTIONS + schema)


def expansion_input(entry: Entry) -> str:
    """LLM 입력: 제목 + 요약 필드 + 기술. 발췌는 요약과 뜻이 같아 넣지 않는다."""

    def texts(points) -> str:
        return " ".join(p.text for p in points)

    parts = [entry.post_title]
    if entry.problem_situation:
        parts.append(f"문제: {texts(entry.problem_situation)}")
    parts.append(f"해결: {texts(entry.solution)}")
    if entry.performance_ops:
        parts.append(f"성능·운영: {texts(entry.performance_ops)}")
    if entry.technologies:
        parts.append(f"기술: {', '.join(entry.technologies)}")
    return "\n".join(parts)


def expansion_text(record: ExpansionRecord) -> str:
    """색인할 텍스트: 예상 검색어 한 줄씩 + 다른 표기·동의어."""
    return "\n".join([*record.queries, " ".join(record.terms)])


def load(path: Path = EXPANSIONS_PATH) -> dict[str, ExpansionRecord]:
    if not path.exists():
        return {}
    records = (ExpansionRecord.model_validate_json(line) for line in path.open(encoding="utf-8"))
    return {r.entry_id: r for r in records}


def save(records: dict[str, ExpansionRecord], path: Path = EXPANSIONS_PATH) -> None:
    lines = [records[k].model_dump_json() for k in sorted(records)]
    path.write_text("".join(f"{line}\n" for line in lines), encoding="utf-8")


def outdated(entries: list[Entry], records: dict[str, ExpansionRecord]) -> list[Entry]:
    """확장이 없거나 입력·지시문이 바뀐 항목."""
    current = prompt_hash()
    return [
        e
        for e in entries
        if (r := records.get(e.id)) is None
        or r.input_hash != _hash(expansion_input(e))
        or r.prompt_hash != current
    ]


def expand(entry: Entry, llm, usage: Usage) -> ExpansionRecord:
    text = expansion_input(entry)
    result = llm.parse(
        INSTRUCTIONS, [{"role": "user", "content": text}], Expansion, usage, "expand"
    )
    return ExpansionRecord(
        entry_id=entry.id,
        input_hash=_hash(text),
        prompt_hash=prompt_hash(),
        model=llm.model,
        queries=result.queries,
        terms=result.terms,
    )


def run(entries: list[Entry], records: dict[str, ExpansionRecord], llm) -> Usage:
    """오래된 확장을 새로 만들고, 사라진 항목의 확장은 지운다. records를 고쳐 쓴다."""
    for entry_id in set(records) - {e.id for e in entries}:
        del records[entry_id]
    todo = outdated(entries, records)
    usages = [Usage() for _ in todo]
    with ThreadPoolExecutor(WORKERS) as pool:
        jobs = zip(todo, usages, strict=True)
        for record in pool.map(lambda job: expand(job[0], llm, job[1]), jobs):
            records[record.entry_id] = record
    total = Usage()
    for u in usages:
        total.add(u)
    return total


def main() -> None:
    parser = argparse.ArgumentParser(
        description="항목별 검색 확장(예상 검색어·다른 표기)을 만든다."
    )
    parser.add_argument("--entries", type=Path, default=ENTRIES_PATH)
    parser.add_argument("--out", type=Path, default=EXPANSIONS_PATH)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--dry-run", action="store_true", help="만들 항목 수만 보여 준다")
    args = parser.parse_args()

    entries = Store(entries_path=args.entries).entries
    records = load(args.out)
    todo = outdated(entries, records)
    print(f"항목 {len(entries)}개 중 확장을 새로 만들 항목 {len(todo)}개")
    if args.dry_run or not todo and set(records) <= {e.id for e in entries}:
        return

    from pipeline.extract.extractor import OpenAILLM

    load_dotenv()
    llm = OpenAILLM(args.model, REASONING_EFFORT)
    try:
        usage = run(entries, records, llm)
    finally:
        save(records, args.out)
    print(
        f"{args.out}에 저장했습니다. 호출 {usage.calls}회,"
        f" 입력 {usage.input_tokens:,} / 출력 {usage.output_tokens:,} 토큰"
    )


if __name__ == "__main__":
    sys.exit(main())
