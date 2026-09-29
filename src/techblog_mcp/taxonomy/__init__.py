"""분류 정의(문제 유형·도메인)와 기술 사전.

추출 파이프라인과 MCP 서버가 함께 쓴다. 추출 프롬프트의 선택지와 도구 입력 스키마의 enum이
모두 이 모듈에서 나오므로 두 곳의 값이 항상 같다.
"""

import re
import tomllib
from dataclasses import dataclass
from functools import cache
from pathlib import Path

_DIR = Path(__file__).parent


@dataclass(frozen=True)
class Category:
    name: str
    description: str


@dataclass(frozen=True)
class Technology:
    name: str
    aliases: tuple[str, ...]


def _load(filename: str) -> dict:
    return tomllib.loads((_DIR / filename).read_text(encoding="utf-8"))


@cache
def problem_types() -> tuple[Category, ...]:
    return tuple(Category(**c) for c in _load("problem_types.toml")["problem_type"])


@cache
def domains() -> tuple[Category, ...]:
    return tuple(Category(**c) for c in _load("domains.toml")["domain"])


@cache
def technologies() -> tuple[Technology, ...]:
    return tuple(
        Technology(name=t["name"], aliases=tuple(t.get("aliases", [])))
        for t in _load("technologies.toml")["technology"]
    )


def problem_type_names() -> tuple[str, ...]:
    return tuple(c.name for c in problem_types())


def domain_names() -> tuple[str, ...]:
    return tuple(c.name for c in domains())


def _key(name: str) -> str:
    """비교용 키: 대소문자, 공백, '-', '_', '.' 차이를 무시한다."""
    return re.sub(r"[\s\-_.]", "", name).casefold()


@cache
def _alias_index() -> dict[str, str]:
    index: dict[str, str] = {}
    for tech in technologies():
        for alias in (tech.name, *tech.aliases):
            key = _key(alias)
            if key in index and index[key] != tech.name:
                raise ValueError(f"기술 사전의 별칭 '{alias}'이 여러 기술에 걸려 있습니다")
            index[key] = tech.name
    return index


_PARENTHESIZED = re.compile(r"\s*\([^)]*\)\s*")
_TRAILING_VERSION = re.compile(r"\s*v?\d+(?:\.\d+)*\s*$", re.IGNORECASE)


def normalize_technology(name: str) -> str | None:
    """기술 이름을 사전의 표준 이름으로 바꾼다. 사전에 없으면 None.

    그대로 없으면 괄호 설명("OGG(Oracle GoldenGate)"는 괄호 안도 후보)과
    끝의 버전 번호("RabbitMQ 3.12.14")를 떼고 다시 찾는다.
    """
    index = _alias_index()
    candidates = [name, _PARENTHESIZED.sub(" ", name), *re.findall(r"\(([^)]*)\)", name)]
    for candidate in candidates:
        for form in (candidate, _TRAILING_VERSION.sub("", candidate)):
            if form.strip() and (found := index.get(_key(form))):
                return found
    return None


def similar_technologies(name: str, n: int = 3) -> list[str]:
    """사전에 없는 이름과 비슷한 표준 이름을 찾는다 (사용자에게 대안을 알려 주는 용도)."""
    import difflib

    index = _alias_index()
    matches = difflib.get_close_matches(_key(name), index.keys(), n=n * 3, cutoff=0.6)
    result: list[str] = []
    for key in matches:
        if index[key] not in result:
            result.append(index[key])
    return result[:n]
