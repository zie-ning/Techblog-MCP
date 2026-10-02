"""LangSmith 트레이싱 (선택).

`--trace`로 켤 때만 트레이스를 보낸다. 글 한 편이 트레이스 하나이고, 그 아래에
분류 → 구조화 → (재시도) OpenAI 호출이 하위 단계로 남는다. OpenAI 호출 단계에는
LLM에 보낸 평문 원문이 그대로 들어간다(비공개 워크스페이스 전송은 허용, 공개 공유는 하지 않음.
docs/기획.md "원문 정책").

설정: `.env`의 `LANGSMITH_API_KEY`. 프로젝트는 `LANGSMITH_PROJECT`가 없으면 `techblog-mcp`.
"""

import os
from typing import Any

DEFAULT_PROJECT = "techblog-mcp"


def enable() -> str:
    """트레이싱을 켜고 프로젝트 이름을 돌려준다. 키가 없으면 RuntimeError."""
    if not os.environ.get("LANGSMITH_API_KEY"):
        raise RuntimeError("LANGSMITH_API_KEY가 없습니다. 저장소 루트의 .env에 설정하세요.")
    os.environ["LANGSMITH_TRACING"] = "true"
    return os.environ.setdefault("LANGSMITH_PROJECT", DEFAULT_PROJECT)


def post_extra(post: Any, run_name: str, model: str, reasoning_effort: str, prompt: str) -> dict:
    """`extract_post`에 넘기는 langsmith_extra: 트레이스 이름, 태그, 필터용 메타데이터."""
    return {
        "name": f"extract {post.source}/{post.post_id}",
        "tags": [run_name, model, f"prompt:{prompt}"],
        "metadata": {
            "run": run_name,
            "source": post.source,
            "post_id": post.post_id,
            "url": post.url,
            "model": model,
            "reasoning_effort": reasoning_effort,
            "prompt_version": prompt,
        },
    }


def root_inputs(inputs: dict) -> dict:
    """루트 단계 입력: HTML 원문과 LLM 객체 대신 글 식별 정보만 남긴다.

    평문 원문은 하위 OpenAI 호출 단계의 입력에 들어 있다.
    """
    post = inputs["post"]
    return {
        "source": post.source,
        "post_id": post.post_id,
        "url": post.url,
        "title": post.title,
        "published_at": post.published_at.date().isoformat(),
    }


def root_outputs(result: Any) -> dict:
    """루트 단계 출력: 글별 기록의 핵심 값과 검증을 통과한 항목들."""
    # 추출이 예외로 끝나면 결과가 없다 (오류는 트레이스에 따로 남음)
    if not hasattr(result, "record"):
        return {}
    r = result.record
    return {
        "kind": r.kind,
        "post_type": r.post_type,
        "reason": r.reason,
        "evidence_total": r.evidence_total,
        "dropped_evidences": r.dropped_evidences,
        "entries": [e.model_dump(exclude={"id"}) for e in result.entries],
    }
