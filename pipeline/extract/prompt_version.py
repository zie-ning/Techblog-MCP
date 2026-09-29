"""프롬프트 버전: LLM에 전달되는 지시 전체의 해시와 그 스냅샷.

추출 결과마다 어떤 프롬프트로 만들었는지 `data/posts.jsonl`의 `prompt_version`에 남기고,
버전별 프롬프트 전문은 `data/prompt_versions/{버전}.md`에 한 번씩 저장한다.
프롬프트를 고친 뒤 옛 버전으로 추출된 글만 골라 다시 추출하고(`--outdated`),
버전끼리 결과를 비교할 때 해시만으로 당시 프롬프트를 바로 열어 볼 수 있게 하기 위함이다.

해시에는 LLM이 보는 것을 모두 넣는다: 지시문, 입력 형식, 재시도 문구, 출력 스키마
(필드 설명과 문제 유형·도메인 선택지 포함). 모델 이름과 추론 강도는 따로 기록하므로 넣지 않는다.
"""

import hashlib
import json
from pathlib import Path

from pydantic import BaseModel

from pipeline.extract import prompts
from pipeline.extract.schema import CaseExtraction, Classification, InsightExtraction

SNAPSHOT_DIR = Path(__file__).resolve().parents[2] / "data" / "prompt_versions"

_VERSION_LENGTH = 12

# 스냅샷에서 자리표시자로 보여 줄 입력값
_TITLE = "{제목}"
_TEXT = "{본문 평문}"
_FAILED = "{원문에서 찾지 못한 evidence}"


def _schema(model: type[BaseModel]) -> str:
    return json.dumps(model.model_json_schema(), ensure_ascii=False, indent=2)


def bundle() -> str:
    """LLM에 전달되는 지시 전체를 사람이 읽을 수 있는 한 문서로 만든다. 해시의 입력이기도 하다."""
    sections = [
        ("1. 글 유형 분류 (instructions)", prompts.CLASSIFY),
        ("2-a. 사례 구조화 (instructions)", prompts.structure_case()),
        ("2-b. 인사이트 구조화 (instructions)", prompts.structure_insight()),
        ("입력 형식 (user)", prompts.post_input(_TITLE, _TEXT)),
        ("발췌 재시도 요청 (user)", prompts.evidence_retry([_FAILED])),
        ("출력 스키마: Classification", _schema(Classification)),
        ("출력 스키마: CaseExtraction", _schema(CaseExtraction)),
        ("출력 스키마: InsightExtraction", _schema(InsightExtraction)),
    ]
    return "\n\n".join(f"## {title}\n\n````\n{body}\n````" for title, body in sections) + "\n"


def version() -> str:
    return hashlib.sha256(bundle().encode("utf-8")).hexdigest()[:_VERSION_LENGTH]


def save_snapshot(snapshot_dir: Path = SNAPSHOT_DIR) -> str:
    """현재 프롬프트의 스냅샷을 저장하고 버전을 돌려준다. 이미 있으면 그대로 둔다."""
    current = version()
    path = snapshot_dir / f"{current}.md"
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        header = (
            f"# 프롬프트 버전 {current}\n\n"
            "`pipeline/extract/prompt_version.py`가 자동 생성한 스냅샷. 직접 고치지 않는다.\n"
            "이 버전으로 추출한 글은 `data/posts.jsonl`에서 "
            f'`"prompt_version": "{current}"`로 찾을 수 있다.\n\n'
        )
        path.write_text(header + bundle(), encoding="utf-8")
    return current
