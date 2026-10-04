"""검색 실험용 LLM 생성물: 문서 확장(E7)과 질의 재작성(E8).

- 문서 확장: 항목마다 "이 사례를 찾을 사람이 넣을 검색어"와 "본문에 없는 다른 표기·동의어"를
  만들어 별도 FTS 열로 색인한다(doc2query 방식). 빌드 때 한 번만 드는 비용이다.
- 질의 재작성: 코딩 에이전트가 검색어를 짧게 나눠 여러 번 검색하는 상황을 LLM으로 흉내 낸다.
  실제 서비스에서는 에이전트가 하므로 서버 비용은 없다. 재작성 모델은 실제 에이전트보다 작다.

생성물은 eval/search/llm_cache/(git 제외)에 캐시해 입력이 바뀐 것만 다시 만든다.
"""

import hashlib
import json
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / "eval" / "search" / "llm_cache"
DEFAULT_MODEL = "gpt-5.6-luna"  # 추출에 쓰는 모델
WORKERS = 8

EXPANSION_INSTRUCTIONS = """\
국내 IT 기업 기술 블로그의 해결 사례 하나가 주어진다. 코딩 에이전트가 설계를 시작하기 전에
이 사례를 검색으로 찾을 수 있도록 검색 보조 정보를 만든다.

- queries: 이 사례가 답이 될 만한 검색어 5개. 개발자가 검색창에 넣을 법한 짧은 한국어 문장이나
  명사구로, 사례의 핵심 문제와 해결을 서로 다른 표현으로 쓴다.
- terms: 사례 본문에 없지만 같은 개념을 가리키는 용어 최대 10개. 한국어↔영어 표기
  (예: 제로트러스트 ↔ Zero Trust), 약어와 원래 이름, 흔히 쓰는 동의어, 바로 위 상위 개념.

사례에 없는 다른 주제나 기술을 지어내지 않는다. 사례가 다루지 않는 문제를 검색어로 만들지 않는다.
"""

REWRITE_INSTRUCTIONS = """\
너는 코딩 에이전트다. 국내 IT 기업 기술 블로그 사례 검색 도구 search를 쓰려고 한다.
search는 검색어를 형태소로 나눠 단어가 많이 겹치는 항목을 찾는 키워드 검색이다(뜻으로 찾지 않는다).
검색어가 길면 핵심이 아닌 단어 때문에 엉뚱한 항목이 섞이고, 표기가 다르면(한국어/영어) 못 찾는다.

주어진 원래 검색 의도를 보고 search에 넣을 검색어를 1~4개 만든다.
- 각 검색어는 2~5단어의 짧은 명사구로, 한 가지 하위 주제만 담는다.
- 의도가 여러 하위 주제를 묶고 있으면 나눈다. 하나뿐이면 1~2개면 된다.
- 핵심 기술·개념은 한국어와 영어 표기 중 사례에 더 쓰일 법한 것을 쓰고,
  필요하면 다른 표기로 한 개 더 만든다.
- 원래 의도에 없는 주제를 더하지 않는다.
"""


class Expansion(BaseModel):
    queries: list[str] = Field(description="이 사례를 찾을 검색어 5개")
    terms: list[str] = Field(description="본문에 없는 다른 표기·동의어·상위 개념, 최대 10개")


class Rewrite(BaseModel):
    queries: list[str] = Field(description="search에 넣을 짧은 검색어 1~4개")


def _hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


class LLMCache:
    """{key: {"hash": 입력 해시, "output": 생성 결과}}를 jsonl 한 파일에 둔다."""

    def __init__(self, path: Path):
        self.path = path
        self.items: dict[str, dict] = {}
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                item = json.loads(line)
                self.items[item["key"]] = item

    def get(self, key: str, text: str) -> dict | None:
        item = self.items.get(key)
        return item["output"] if item and item["hash"] == _hash(text) else None

    def put(self, key: str, text: str, output: dict) -> None:
        self.items[key] = {"key": key, "hash": _hash(text), "output": output}

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        lines = [json.dumps(i, ensure_ascii=False) for i in self.items.values()]
        self.path.write_text("\n".join(lines) + "\n", encoding="utf-8")


class OpenAIGenerator:
    def __init__(self, model: str = DEFAULT_MODEL, reasoning_effort: str = "low"):
        from dotenv import load_dotenv
        from openai import OpenAI

        load_dotenv(ROOT / ".env")
        self._client = OpenAI(max_retries=6)
        self.model = model
        self.reasoning_effort = reasoning_effort
        self.input_tokens = 0
        self.output_tokens = 0

    def __call__(self, instructions: str, text: str, schema: type[BaseModel]) -> dict:
        response = self._client.responses.parse(
            model=self.model,
            instructions=instructions,
            input=[{"role": "user", "content": text}],
            text_format=schema,
            reasoning={"effort": self.reasoning_effort},
        )
        if response.usage:
            self.input_tokens += response.usage.input_tokens
            self.output_tokens += response.usage.output_tokens
        if response.output_parsed is None:
            raise RuntimeError(f"구조화 출력을 받지 못했습니다: {response.output_text[:200]}")
        return response.output_parsed.model_dump()


Generate = Callable[[str, str, type[BaseModel]], dict]


def _generate_all(
    cache: LLMCache,
    inputs: dict[str, str],
    instructions: str,
    schema: type[BaseModel],
    generate: Generate,
) -> dict[str, dict]:
    todo = {k: t for k, t in inputs.items() if cache.get(k, t) is None}
    if todo:
        print(f"{cache.path.name}: {len(todo)}건 생성")
        with ThreadPoolExecutor(WORKERS) as pool:
            outputs = pool.map(lambda kt: generate(instructions, kt[1], schema), todo.items())
            for (key, text), output in zip(todo.items(), outputs, strict=True):
                cache.put(key, text, output)
        cache.save()
    return {k: cache.get(k, t) for k, t in inputs.items()}


def expansions(
    entries: dict[str, str], model: str = DEFAULT_MODEL, generate: Generate | None = None
) -> dict[str, Expansion]:
    """항목 ID → 확장. entries는 항목 ID → 임베딩과 같은 입력 텍스트(제목 + 요약 + 기술)."""
    cache = LLMCache(CACHE_DIR / f"expansion-{model}.jsonl")
    generate = generate or OpenAIGenerator(model)
    out = _generate_all(cache, entries, EXPANSION_INSTRUCTIONS, Expansion, generate)
    return {k: Expansion.model_validate(v) for k, v in out.items()}


def rewrites(
    queries: dict[str, str], model: str = DEFAULT_MODEL, generate: Generate | None = None
) -> dict[str, list[str]]:
    """질문 ID → 재작성 검색어 목록."""
    cache = LLMCache(CACHE_DIR / f"rewrite-{model}.jsonl")
    generate = generate or OpenAIGenerator(model)
    out = _generate_all(cache, queries, REWRITE_INSTRUCTIONS, Rewrite, generate)
    return {k: Rewrite.model_validate(v).queries for k, v in out.items()}
