"""추출 정답셋 형식과 불러오기.

정답 파일은 `eval/gold/{source}__{post_id}.json` 하나에 글 한 편이다.
라벨링 기준은 eval/gold/README.md.
원문 전체는 넣지 않고 요약과 짧은 수치만 넣는다(docs/기획.md "원문 정책").
"""

import json
import sys
from pathlib import Path

from pydantic import BaseModel, Field, model_validator

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 pipeline을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from pipeline.extract.schema import (  # noqa: E402
    Domain,
    PostKind,
    PostType,
    ProblemType,
    RejectedKind,
)
from techblog_mcp import taxonomy  # noqa: E402

GOLD_DIR = ROOT / "eval" / "gold"


class GoldRejected(BaseModel):
    name: str  # 기술이면 기술 사전의 표준 이름(없으면 원래 이름), 설계 방식이면 짧은 명사구
    kind: RejectedKind


class GoldEntry(BaseModel):
    summary: str = Field(
        description="이 항목의 문제와 해법(팁·활용 경험 글은 요지) 한 줄. 항목 대응에 쓴다"
    )
    primary_problem_type: ProblemType
    acceptable_problem_types: list[ProblemType] = Field(
        default=[], description="주 문제 유형으로 이것을 골라도 맞다고 볼 다른 유형"
    )
    domain: Domain
    acceptable_domains: list[Domain] = []
    technologies: list[str] = Field(description="실제로 쓴 기술. 사전에 있으면 표준 이름")
    rejected_alternatives: list[GoldRejected] = []
    key_facts: list[str] = Field(
        description="추출 결과에 반드시 담겨야 할 조건·수치·결과 (완결성 채점 기준)"
    )


class GoldPost(BaseModel):
    source: str
    post_id: str
    url: str
    title: str
    post_type: PostType
    kind: PostKind
    kind_alternatives: list[PostKind] = Field(
        default=[], description="경계 글에서 이 추출 여부도 맞다고 볼 때"
    )
    entries: list[GoldEntry]
    notes: str = Field(description="판단 근거, 특히 경계 글의 이유")
    reviewed: bool = False  # 사람이 원문과 대조해 검수했는지

    @model_validator(mode="after")
    def _entries_match_kind(self) -> "GoldPost":
        if self.kind == "제외" and self.entries:
            raise ValueError("제외 글에는 항목이 없어야 합니다")
        if self.kind == "추출" and not self.entries:
            raise ValueError("추출 글에는 항목이 1개 이상 있어야 합니다")
        return self


def gold_path(source: str, post_id: str, gold_dir: Path = GOLD_DIR) -> Path:
    return gold_dir / f"{source}__{post_id}.json"


def load_gold(gold_dir: Path = GOLD_DIR) -> dict[tuple[str, str], GoldPost]:
    posts = [
        GoldPost.model_validate_json(p.read_text(encoding="utf-8"))
        for p in sorted(gold_dir.glob("*.json"))
    ]
    return {(g.source, g.post_id): g for g in posts}


def save_gold(post: GoldPost, gold_dir: Path = GOLD_DIR) -> Path:
    path = gold_path(post.source, post.post_id, gold_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = post.model_dump()
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def _allowed(values: list[str]) -> str:
    return f" (허용: {', '.join(values)})" if values else ""


def render_review(golds: dict[tuple[str, str], GoldPost]) -> str:
    """검수용 마크다운: 글마다 원문 링크와 정답을 한눈에 보이게 정리한다. 기준은 JSON 파일이다."""
    lines = [
        "# 추출 정답셋 검수표",
        "",
        "`uv run python eval/gold.py review`로 생성한다. 기준 데이터는 같은 폴더의 JSON이고 "
        "이 파일은 보기용이다. 원문과 대조해 고칠 점이 있으면 JSON을 고치고, 검수를 마친 글은 "
        "JSON의 `reviewed`를 `true`로 바꾼다.",
        "",
    ]
    for (source, post_id), g in sorted(golds.items()):
        mark = "검수 완료" if g.reviewed else "검수 전"
        alt = f" (허용: {', '.join(g.kind_alternatives)})" if g.kind_alternatives else ""
        lines += [
            f"## {source}/{post_id} — {mark}",
            "",
            f"[{g.title}]({g.url})",
            "",
            f"- 글 유형: {g.post_type}",
            f"- 추출 여부: **{g.kind}**{alt}",
            f"- 판단 근거: {g.notes}",
        ]
        for i, e in enumerate(g.entries, 1):
            types = e.primary_problem_type + _allowed(e.acceptable_problem_types)
            domains = e.domain + _allowed(e.acceptable_domains)
            lines += [
                "",
                f"### 항목 {i}. {e.summary}",
                "",
                f"- 주 문제 유형: {types}",
                f"- 도메인: {domains}",
                f"- 기술: {', '.join(e.technologies) or '-'}",
            ]
            if e.rejected_alternatives:
                rejected = ", ".join(f"{r.name}({r.kind})" for r in e.rejected_alternatives)
                lines.append(f"- 버린 대안: {rejected}")
            lines.append("- 핵심 사실:")
            lines += [f"  - {fact}" for fact in e.key_facts]
        lines.append("")
    return "\n".join(lines) + "\n"


# 글 유형·구조화 유형 정의는 추출 프롬프트(pipeline/extract/prompts.py CLASSIFY)와 같은 문구를 쓴다.
# 값 목록은 스키마의 Literal에서 읽으므로, 값을 바꾸면 여기 정의가 없다는 테스트가 실패한다.
POST_TYPE_DEFINITIONS = {
    "문제 해결형": "겪은 기술 문제와 그 해결 과정을 다룸",
    "기술 선택·도입형": "기술·구조를 검토해 도입하거나 바꾼 경험과 근거를 다룸",
    "실험·활용기": "도구·기술을 실제 업무에 써 본 경험, 설계 팁, 적용 결과",
    "개념·튜토리얼": "교과서적인 개념 설명, 입문 튜토리얼, 문법·API 소개",
    "회고·문화·행사": "회고, 조직 문화, 협업 방식, 직무·팀 소개, 컨퍼런스·행사, 채용, 온보딩",
}
KIND_DEFINITIONS = {
    "추출": "다른 팀이 설계·구현 판단에 참고할 기술적 실무 내용이 있는 글. 겪은 기술 문제와 해결, "
    "기술 선택·도입의 근거, 도구·기술을 실제 업무에 적용한 경험과 팁",
    "제외": "개념·튜토리얼, 회고·문화·행사, 그 밖에 기술적 실무 적용점이 없는 글",
}
REJECTED_KIND_DEFINITIONS = {
    "기술": "제품·라이브러리·서비스 자체 (예: OpenSearch, Hazelcast, MPS). 기술별 집계에 들어감",
    "설계 방식": "패턴, 구현·설정·운영 방법 (예: Outbox 패턴, READ COMMITTED 격리 수준). "
    "상세 보기에서만 보임",
}


def _literal_values(literal) -> tuple[str, ...]:
    return literal.__args__


def _definition_table(values: tuple[str, ...], definitions: dict[str, str]) -> list[str]:
    lines = ["| 값 | 정의 |", "| --- | --- |"]
    return lines + [f"| {v} | {definitions[v]} |" for v in values]


def render_reference() -> str:
    """검수 참고표: 정답 필드별 선택지와 정의. 분류 목록과 스키마에서 만든다."""
    lines = [
        "# 정답셋 검수 참고표",
        "",
        "`uv run python eval/gold.py reference`로 생성한다. 문제 유형·도메인·기술 사전은 "
        "`src/techblog_mcp/taxonomy/`, 글 유형·구조화 유형은 추출 스키마와 프롬프트가 기준이다. "
        "분류 목록이 바뀌면 다시 생성한다. 라벨링 기준은 [README.md](README.md).",
        "",
        '정답의 "(허용: …)"는 추출 결과가 그 값이어도 맞다고 보는 다른 답이다.',
        "",
        f"## 글 유형 (`post_type`, {len(_literal_values(PostType))}개)",
        "",
        *_definition_table(_literal_values(PostType), POST_TYPE_DEFINITIONS),
        "",
        f"## 추출 여부 (`kind`, {len(_literal_values(PostKind))}개)",
        "",
        *_definition_table(_literal_values(PostKind), KIND_DEFINITIONS),
        "",
        "- 행사·문화·협업 글은 AI 도구나 실무 팁이 섞여 있어도 제외.",
        "- 발표 소개 글은 본문에 해결 근거(수치, 비교, 설계 결정과 이유)가 없으면 제외. "
        "목차는 근거가 아니다.",
        "- 언어 기능·개념 설명 글은 팀이 겪은 문제나 적용 결과가 없으면 제외.",
        "",
        "항목 나누기: 독립된 문제-해법 쌍마다 항목 하나, 같은 문제의 단계적 해결은 한 항목, "
        "팁 모음·도구 활용 경험 글은 항목 하나.",
        "",
        f"## 주 문제 유형 (`primary_problem_type`, {len(taxonomy.problem_types())}개)",
        "",
        "무엇을 풀었는지(해결의 목적) 기준으로 고른다. 쓴 기술 기준이 아니다.",
        "",
        *_definition_table(
            taxonomy.problem_type_names(),
            {c.name: c.description for c in taxonomy.problem_types()},
        ),
        "",
        f"## 도메인 (`domain`, {len(taxonomy.domains())}개)",
        "",
        "그 시스템이 속한 서비스 영역. 애매하면 범용.",
        "",
        *_definition_table(
            taxonomy.domain_names(), {c.name: c.description for c in taxonomy.domains()}
        ),
        "",
        "## 버린 대안 유형 (`rejected_alternatives[].kind`, 2개)",
        "",
        *_definition_table(_literal_values(RejectedKind), REJECTED_KIND_DEFINITIONS),
        "",
        f"## 기술 사전 ({len(taxonomy.technologies())}개)",
        "",
        "`technologies`는 정해진 목록이 아니라 자유 입력이다. "
        "사전에 있는 기술은 아래 표준 이름으로 "
        "쓰고, 사전에 없는 기술도 넣을 수 있다. 괄호는 같은 계열로 묶어 세는 상위 기술.",
        "",
        "| 종류 | 기술 |",
        "| --- | --- |",
    ]
    for category in taxonomy.technology_categories():
        names = [
            f"{t.name} (→ {t.parent})" if t.parent else t.name
            for t in taxonomy.technologies()
            if t.category == category
        ]
        lines.append(f"| {category} | {', '.join(names)} |")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    if sys.argv[1:] == ["review"]:
        out = GOLD_DIR / "REVIEW.md"
        out.write_text(render_review(load_gold()), encoding="utf-8")
        print(f"검수표 저장: {out}")
    elif sys.argv[1:] == ["reference"]:
        out = GOLD_DIR / "REFERENCE.md"
        out.write_text(render_reference(), encoding="utf-8")
        print(f"검수 참고표 저장: {out}")
    else:
        sys.exit("사용법: uv run python eval/gold.py review|reference")
