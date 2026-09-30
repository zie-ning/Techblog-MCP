"""수집한 원문의 저장 형식과 로컬 캐시.

글 하나를 `data/raw/{source}/{post_id}.json` 파일 하나로 저장한다.
원문 전체가 들어 있으므로 이 디렉터리는 git과 배포에서 제외한다.
"""

import json
from dataclasses import asdict, dataclass
from datetime import date, datetime
from pathlib import Path

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"

# 수집 기간: 2023-09 이후 발행된 글 (docs/기획.md "수집 기간")
COLLECT_SINCE = date(2023, 9, 1)


@dataclass
class RawPost:
    source: str  # 블로그 식별자 (예: "oliveyoung")
    post_id: str  # 블로그 안에서 고유하고 파일 이름으로 쓸 수 있는 ID
    url: str
    title: str
    published_at: datetime  # 시간대 포함
    content_html: str  # 본문 HTML 원문
    collected_at: datetime

    def to_json(self) -> str:
        data = asdict(self)
        data["published_at"] = self.published_at.isoformat()
        data["collected_at"] = self.collected_at.isoformat()
        return json.dumps(data, ensure_ascii=False, indent=2)

    @classmethod
    def from_json(cls, text: str) -> "RawPost":
        data = json.loads(text)
        data["published_at"] = datetime.fromisoformat(data["published_at"])
        data["collected_at"] = datetime.fromisoformat(data["collected_at"])
        return cls(**data)


def in_collect_period(published_at: datetime) -> bool:
    return published_at.date() >= COLLECT_SINCE


def raw_path(source: str, post_id: str, raw_dir: Path = RAW_DIR) -> Path:
    return raw_dir / source / f"{post_id}.json"


def exists(source: str, post_id: str, raw_dir: Path = RAW_DIR) -> bool:
    return raw_path(source, post_id, raw_dir).exists()


def save(post: RawPost, raw_dir: Path = RAW_DIR) -> Path:
    path = raw_path(post.source, post.post_id, raw_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(post.to_json(), encoding="utf-8")
    return path


def load_all(source: str, raw_dir: Path = RAW_DIR) -> list[RawPost]:
    """저장된 글을 발행일 최신순으로 불러온다."""
    posts = [
        RawPost.from_json(p.read_text(encoding="utf-8")) for p in (raw_dir / source).glob("*.json")
    ]
    return sorted(posts, key=lambda p: p.published_at, reverse=True)
