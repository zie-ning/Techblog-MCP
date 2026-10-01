"""기술 사전 기반 기술명 정규화.

정규화 규칙 자체는 서버와 공유하는 `techblog_mcp.taxonomy`에 있다.
여기서는 저장된 항목을 현재 사전으로 다시 정규화한다.
"""

from pipeline.extract.schema import Entry, RejectedAlternative
from techblog_mcp import taxonomy


def rejected_alternative_name(name_raw: str, technologies: list[str]) -> str:
    """버린 대안의 집계용 이름.

    사전으로 정규화하되, 정규화 결과가 그 사례에서 쓴 기술과 같으면 원래 이름을 둔다.
    예: "Claude 3 Haiku"를 버리고 "Claude 3.5 Sonnet"을 쓴 경우 둘 다 "Claude"가 되어
    "Claude를 버렸다"는 모순된 기록이 되는 것을 막는다.
    """
    name_raw = name_raw.strip()
    normalized = taxonomy.normalize_technology(name_raw)
    if normalized is None or normalized in technologies:
        return name_raw
    return normalized


def rejected_alternative_kind(r: RejectedAlternative) -> str:
    """버린 대안 유형.

    유형이 없는 M3 이전 추출은 기술 사전에 있으면 기술, 없으면 설계 방식으로 본다.
    """
    if r.kind:
        return r.kind
    return "기술" if taxonomy.normalize_technology(r.name_raw) else "설계 방식"


def renormalize(entry: Entry) -> tuple[Entry, list[str]]:
    """(다시 정규화한 항목, 사전에 없는 원래 이름 목록)"""
    technologies: list[str] = []
    missing: list[str] = []
    for name in entry.technologies_raw:
        normalized = taxonomy.normalize_technology(name)
        if normalized is None:
            missing.append(name)
        elif normalized not in technologies:
            technologies.append(normalized)

    rejected = []
    for r in entry.rejected_alternatives:
        kind = rejected_alternative_kind(r)
        # 설계 방식은 기술 사전과 무관하므로 원래 이름을 그대로 쓴다
        name = rejected_alternative_name(r.name_raw, technologies) if kind == "기술" else r.name_raw
        rejected.append(r.model_copy(update={"name": name.strip(), "kind": kind}))
    updated = entry.model_copy(
        update={"technologies": technologies, "rejected_alternatives": rejected}
    )
    return updated, missing
