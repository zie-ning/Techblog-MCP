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
    category: str  # 종류 (technologies.toml의 categories 중 하나)
    parent: str | None = None  # 같은 계열로 묶어 셀 상위 기술 (예: Amazon MSK → Kafka)


def _load(filename: str) -> dict:
    return tomllib.loads((_DIR / filename).read_text(encoding="utf-8"))


@cache
def problem_types() -> tuple[Category, ...]:
    return tuple(Category(**c) for c in _load("problem_types.toml")["problem_type"])


@cache
def domains() -> tuple[Category, ...]:
    return tuple(Category(**c) for c in _load("domains.toml")["domain"])


@cache
def technology_categories() -> tuple[str, ...]:
    return tuple(_load("technologies.toml")["categories"])


@cache
def technologies() -> tuple[Technology, ...]:
    techs = tuple(
        Technology(
            name=t["name"],
            aliases=tuple(t.get("aliases", [])),
            category=t["category"],
            parent=t.get("parent"),
        )
        for t in _load("technologies.toml")["technology"]
    )
    _validate(techs)
    return techs


def _validate(techs: tuple[Technology, ...]) -> None:
    """종류는 정해진 목록 안에서, 상위 기술은 사전에 있는 기술로 한 단계만 둔다."""
    categories = set(technology_categories())
    parents = {t.name: t.parent for t in techs}
    for t in techs:
        if t.category not in categories:
            raise ValueError(f"기술 '{t.name}'의 종류 '{t.category}'가 categories에 없습니다")
        if t.parent is None:
            continue
        if t.parent not in parents or t.parent == t.name:
            raise ValueError(f"기술 '{t.name}'의 상위 기술 '{t.parent}'가 사전에 없습니다")
        if parents[t.parent] is not None:
            raise ValueError(f"상위 기술 '{t.parent}'에 다시 상위 기술이 있습니다 (한 단계만 허용)")


def technology(name: str) -> Technology | None:
    """표준 이름으로 사전 항목을 찾는다."""
    return _by_name().get(name)


@cache
def _by_name() -> dict[str, Technology]:
    return {t.name: t for t in technologies()}


def technology_family(name: str) -> str:
    """같은 계열로 묶어 셀 이름: 상위 기술이 있으면 상위 기술, 없으면 자기 자신."""
    tech = technology(name)
    return tech.parent if tech and tech.parent else name


def technology_members(name: str) -> tuple[str, ...]:
    """필터에서 펼칠 이름: 자기 자신 + 하위 기술 (예: Kafka → Kafka, Amazon MSK, …).

    하위 기술로 찾으면 그 기술만 찾는다 (M6 결정, docs/기획.md).
    """
    return (name, *_children().get(name, ()))


@cache
def _children() -> dict[str, tuple[str, ...]]:
    children: dict[str, list[str]] = {}
    for t in technologies():
        if t.parent:
            children.setdefault(t.parent, []).append(t.name)
    return {parent: tuple(names) for parent, names in children.items()}


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
