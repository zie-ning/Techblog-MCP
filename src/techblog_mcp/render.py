"""도구 결과를 에이전트가 읽기 쉬운 텍스트로 만든다 (JSON보다 토큰이 적고 인용하기 쉽다)."""

from techblog_mcp.search.query import (
    AggregateResult,
    Detail,
    Filters,
    GroupBy,
    SearchResult,
    TechnologyResolution,
)

CITATION_RULE = (
    "인용할 때는 회사명과 원문 링크를 함께 밝히고, 위 결과에 없는 사례는 지어내지 마세요."
)
# 사례는 설계 정답이 아니라 참고 자료라는 원칙 (docs/기획.md "호출 유도"의 사례 활용 원칙).
# 도구 설명·서버 안내·prompt에는 전문을, 결과마다 붙는 안내에는 짧은 버전을 쓴다.
REFERENCE_PRINCIPLE = (
    "사례는 해당 회사의 규모·조직·기존 인프라에서 내린 선택이다. "
    "사용자에게 참고 사례로 출처와 함께 소개하되 그대로 적용하라고 권하지 말고, "
    "사용자 상황과 다른 점을 함께 짚는다. 사례 소개와 자신의 제안은 구분해서 제시한다."
)
REFERENCE_RULE = "사례는 참고용으로 소개하고, 사용자 상황과의 차이를 짚어 자신의 제안과 구분하세요."
_MAX_COMPANY_NAMES = 5

GROUP_BY_LABELS: dict[str, str] = {
    "technology": "기술",
    "problem_type": "문제 유형(주 유형 기준)",
    "domain": "도메인",
    "company": "회사",
    "rejected_alternative": "버린 대안",
}


def _header(entry: dict) -> str:
    return (
        f"[{entry['kind']} {entry['id']}] {entry['company']} · {entry['published_at']}"
        f" · {entry['primary_problem_type']} / {entry['domain']}"
    )


def _first(points: list[dict]) -> str:
    return points[0]["text"] if points else "-"


def card(entry: dict) -> str:
    lines = [_header(entry)]
    if entry["kind"] == "사례":
        lines.append(f"문제 상황: {_first(entry['problem_situation'])}")
        lines.append(f"해결 방법: {_first(entry['solution'])}")
    else:
        lines.append(f"핵심 내용: {_first(entry['key_points'])}")
    if entry["technologies"]:
        lines.append(f"기술: {', '.join(entry['technologies'])}")
    rejected = list(dict.fromkeys(r["name"] for r in entry.get("rejected_alternatives", [])))
    if rejected:
        lines.append(f"버린 대안: {', '.join(rejected)}")
    lines.append(f"원문: {entry['post_url']}")
    return "\n".join(lines)


def _condition(query: str | None, filters: Filters) -> str:
    parts = [f'검색어 "{query}"'] if query else []
    parts += filters.describe()
    return ", ".join(parts) if parts else "조건 없음"


def unknown_technologies(resolution: TechnologyResolution) -> list[str]:
    lines = []
    for name, similar in resolution.unknown.items():
        hint = f" 비슷한 기술: {', '.join(similar)}" if similar else ""
        lines.append(f"※ '{name}'은(는) 기술 사전에 없어 기술 필터에서 뺐습니다.{hint}")
    return lines


def search_result(
    query: str, filters: Filters, limit: int, result: SearchResult, notes: list[str]
) -> str:
    lines = [f"조건: {_condition(query, filters)}", *notes]
    if not result.entries:
        lines.append(
            "\n결과 없음: 이 조건에 맞는 국내 기업 사례·인사이트가 DB에 없습니다. "
            "사례를 지어내지 말고, 참고할 국내 사례를 찾지 못했다고 답하세요. "
            "검색어를 바꾸거나 필터를 빼서 다시 검색해 볼 수 있습니다."
        )
        return "\n".join(lines)

    shown = len(result.entries)
    if result.total < limit:
        lines.append(
            f"결과: {result.total}건뿐입니다. 이 주제의 사례가 적다는 점을 답변에 밝히세요."
        )
    else:
        lines.append(
            f"결과: 관련도 순 상위 {shown}건 (검색어가 하나라도 걸린 항목 {result.total}건)"
        )
    lines.append("")
    lines.append("\n\n".join(card(e) for e in result.entries))
    lines.append("")
    lines.append("근거 발췌와 전체 내용은 get_details(ids)로 확인하세요. " + CITATION_RULE)
    lines.append(REFERENCE_RULE)
    return "\n".join(lines)


def _points(title: str, points: list[dict]) -> list[str]:
    if not points:
        return []
    lines = ["", f"## {title}"]
    for p in points:
        lines.append(f"- {p['text']}")
        lines.append(f'  근거: "{p["evidence"]}"')
    return lines


def detail(d: Detail) -> str:
    e = d.entry
    secondary = e["secondary_problem_types"]
    lines = [
        f"[{e['kind']} {e['id']}] {e['post_title']}",
        f"회사: {e['company']} · 발행일: {e['published_at']}",
        f"원문: {e['post_url']}",
        f"문제 유형: {e['primary_problem_type']}"
        + (f" (보조: {', '.join(secondary)})" if secondary else "")
        + f" · 도메인: {e['domain']}",
    ]
    if e["technologies"]:
        lines.append(f"기술: {', '.join(e['technologies'])}")
    if e["tags"]:
        lines.append(f"태그: {', '.join(e['tags'])}")

    if e["kind"] == "사례":
        lines += _points("문제 상황", e["problem_situation"])
        lines += _points("해결 방법", e["solution"])
        lines += _points("성능·운영 포인트", e["performance_ops"])
        if e["rejected_alternatives"]:
            lines += ["", "## 버린 대안"]
            for r in e["rejected_alternatives"]:
                lines.append(f"- {r['name']}: {r['reason']}")
                lines.append(f'  근거: "{r["evidence"]}"')
    else:
        lines += _points("핵심 내용", e["key_points"])
        lines += _points("적용해볼 점", e["takeaways"])

    if d.siblings:
        lines += ["", f"같은 글의 다른 항목: {', '.join(d.siblings)}"]
    return "\n".join(lines)


def details_result(details: list[Detail], missing: list[str], dropped: list[str]) -> str:
    parts = [detail(d) for d in details]
    notes = []
    if missing:
        notes.append(f"※ 없는 ID: {', '.join(missing)} (search 결과의 ID를 쓰세요)")
    if dropped:
        notes.append(f"※ 한 번에 3건까지만 조회합니다. 제외된 ID: {', '.join(dropped)}")
    if parts:
        notes.append(CITATION_RULE)
        notes.append(REFERENCE_RULE)
    return "\n\n---\n\n".join(parts + ["\n".join(notes)] if notes else parts)


def _count(cases: int, insights: int) -> str:
    return f"사례 {cases}건 · 인사이트 {insights}건"


def aggregate_result(
    group_by: GroupBy, filters: Filters, result: AggregateResult, notes: list[str]
) -> str:
    label = GROUP_BY_LABELS[group_by]
    lines = [
        f"조건: {_condition(None, filters)} → {_count(result.cases, result.insights)}"
        f" / {result.companies}개사",
        f"기준: {label} (상위 {len(result.groups)}개 / 전체 {result.group_count}개)",
        *notes,
    ]
    if group_by == "rejected_alternative":
        lines.append("※ 버린 대안이 글에 명시된 사례만 셉니다.")
    if result.cases + result.insights == 0:
        lines.append("\n결과 없음: 이 조건에 맞는 항목이 DB에 없습니다. 수치를 지어내지 마세요.")
        return "\n".join(lines)

    lines.append("")
    for rank, g in enumerate(result.groups, start=1):
        names = ", ".join(g.companies[:_MAX_COMPANY_NAMES])
        if len(g.companies) > _MAX_COMPANY_NAMES:
            names += ", …"
        lines.append(
            f"{rank}. {g.key}  {_count(g.cases, g.insights)} · {len(g.companies)}개사 ({names})"
            f"  예시: {', '.join(g.examples)}"
        )
    lines.append("")
    lines.append(
        "인사이트는 실제 운영 사례가 아닐 수 있으니 사례 건수를 우선 보세요. "
        "예시 ID는 get_details로 확인할 수 있습니다."
    )
    return "\n".join(lines)
