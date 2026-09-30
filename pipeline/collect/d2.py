"""네이버 D2 수집기.

공개 JSON API를 쓴다. 목록(`/api/v1/contents?page=N`)은 최신순이고 본문이 256자로 잘려 있어
발행일로 기간을 거른 뒤 글마다 상세(`/api/v1/contents/{id}`)를 받는다.
행사·공지 글인 news 카테고리는 수집하지 않는다 (docs/기획.md "데이터 수집").
"""

import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from pipeline.collect import raw
from pipeline.collect.common import CollectResult, collect_each
from pipeline.collect.http import PoliteClient

SOURCE = "d2"
BASE_URL = "https://d2.naver.com"
EXCLUDED_CATEGORIES = {"news"}


@dataclass
class ListItem:
    post_id: str
    url: str
    category: str  # URL 첫 경로 (helloworld, news)
    published_at: datetime


def list_url(page: int) -> str:
    return f"{BASE_URL}/api/v1/contents?page={page}"


def detail_url(post_id: str) -> str:
    return f"{BASE_URL}/api/v1/contents/{post_id}"


def _published_at(epoch_ms: str | int) -> datetime:
    return datetime.fromtimestamp(int(epoch_ms) / 1000, tz=UTC)


def parse_list(body: bytes) -> tuple[list[ListItem], bool]:
    """목록 한 페이지를 파싱해 (글 목록, 다음 페이지 존재 여부)를 돌려준다."""
    data = json.loads(body)
    items = []
    for item in data["content"]:
        path = item["url"]  # 예: /helloworld/8118359
        category, post_id = path.strip("/").split("/")
        items.append(
            ListItem(
                post_id=post_id,
                url=BASE_URL + path,
                category=category,
                published_at=_published_at(item["postPublishedAt"]),
            )
        )
    page = data["page"]
    return items, page["number"] + 1 < page["totalPages"]


def parse_detail(body: bytes, collected_at: datetime) -> raw.RawPost:
    item = json.loads(body)
    path = item["url"]
    return raw.RawPost(
        source=SOURCE,
        post_id=path.strip("/").split("/")[-1],
        url=BASE_URL + path,
        title=item["postTitle"].strip(),
        published_at=_published_at(item["postPublishedAt"]),
        content_html=item["postHtml"],
        collected_at=collected_at,
    )


def collect(
    client: PoliteClient, raw_dir: Path = raw.RAW_DIR, refresh: bool = False
) -> CollectResult:
    targets: list[ListItem] = []
    page, has_next = 0, True
    while has_next:
        items, has_next = parse_list(client.get(list_url(page)).content)
        in_period = [i for i in items if raw.in_collect_period(i.published_at)]
        targets.extend(i for i in in_period if i.category not in EXCLUDED_CATEGORIES)
        # 최신순이므로 한 페이지가 모두 기간 밖이면 그 뒤 페이지는 볼 필요가 없다
        if not in_period:
            break
        page += 1

    collected_at = datetime.now(UTC)
    return collect_each(
        SOURCE,
        [(t.post_id, t.url) for t in targets],
        lambda post_id, url: parse_detail(client.get(detail_url(post_id)).content, collected_at),
        raw_dir,
        refresh,
    )
