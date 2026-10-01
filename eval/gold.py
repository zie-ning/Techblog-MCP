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

GOLD_DIR = ROOT / "eval" / "gold"


class GoldRejected(BaseModel):
    name: str  # 기술이면 기술 사전의 표준 이름(없으면 원래 이름), 설계 방식이면 짧은 명사구
    kind: RejectedKind


class GoldEntry(BaseModel):
    summary: str = Field(
        description="이 항목의 문제와 해법(또는 핵심 내용) 한 줄. 사례 대응에 쓴다"
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
        default=[], description="경계 글에서 이 구조화 유형도 맞다고 볼 때"
    )
    entries: list[GoldEntry]
    notes: str = Field(description="판단 근거, 특히 경계 글의 이유")
    reviewed: bool = False  # 사람이 원문과 대조해 검수했는지

    @model_validator(mode="after")
    def _entries_match_kind(self) -> "GoldPost":
        if self.kind == "제외" and self.entries:
            raise ValueError("제외 글에는 항목이 없어야 합니다")
        if self.kind == "인사이트" and len(self.entries) != 1:
            raise ValueError("인사이트 글은 항목이 1개여야 합니다")
        if self.kind == "사례" and not self.entries:
            raise ValueError("사례 글에는 항목이 1개 이상 있어야 합니다")
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
            f"- 구조화 유형: **{g.kind}**{alt}",
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


if __name__ == "__main__":
    if sys.argv[1:] == ["review"]:
        out = GOLD_DIR / "REVIEW.md"
        out.write_text(render_review(load_gold()), encoding="utf-8")
        print(f"검수표 저장: {out}")
    else:
        sys.exit("사용법: uv run python eval/gold.py review")
