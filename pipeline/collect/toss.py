"""토스 기술블로그 수집기.

목록·발행일·카테고리는 공개 JSON API에서 받는다. API의 `fullDescription`은 평문이라
코드 블록과 제목 구조가 사라지므로, 본문은 글 페이지(`/article/{key}`)의 서버 렌더링 HTML에서
가져온다.
UX 디자인 글인 Design 카테고리는 수집하지 않는다 (docs/기획.md "데이터 수집").
"""

import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from bs4 import BeautifulSoup

from pipeline.collect import raw
from pipeline.collect.common import CollectResult, ParseError, collect_each
from pipeline.collect.http import PoliteClient

SOURCE = "toss"
API_URL = "https://api-public.toss.im/api-public/v3/ipd-thor/api/v1/workspaces/15/posts"
ARTICLE_URL = "https://toss.tech/article/"
EXCLUDED_CATEGORIES = {"Design"}


@dataclass
class ListItem:
    key: str
    title: str
    category: str
    published_at: datetime

    @property
    def url(self) -> str:
        return ARTICLE_URL + self.key


def list_url(page: int) -> str:
    return f"{API_URL}?page={page}&size=20"


def parse_list(body: bytes) -> tuple[list[ListItem], bool]:
    """목록 한 페이지를 파싱해 (공개된 글 목록, 다음 페이지 존재 여부)를 돌려준다.

    본문이 빈 글은 외부 페이지(SLASH 발표 영상 등)로 넘어가는 링크 글이라 제외한다.
    """
    data = json.loads(body)["success"]
    items = [
        ListItem(
            key=item["key"],
            title=item["title"].strip(),
            category=item["category"],
            published_at=datetime.fromisoformat(item["publishedTime"]),
        )
        for item in data["results"]
        if item["isPublished"] and item["fullDescription"].strip()
    ]
    return items, data["next"] is not None


def parse_article(html: str) -> str:
    """글 페이지에서 본문 HTML만 꺼낸다.

    `<article>` 안에 제목·작성자·날짜 머리(header), 본문 div, 공유 버튼이 있다.
    클래스 이름은 빌드마다 바뀌는 해시라 쓰지 않고 구조로 찾는다.
    """
    article = BeautifulSoup(html, "html.parser").find("article")
    if article is None:
        raise ParseError("<article> 없음")
    bodies = article.find_all("div", recursive=False)
    if not bodies:
        raise ParseError("<article> 안에 본문 div 없음")
    return str(max(bodies, key=lambda div: len(div.get_text())))


def collect(
    client: PoliteClient, raw_dir: Path = raw.RAW_DIR, refresh: bool = False
) -> CollectResult:
    targets: dict[str, ListItem] = {}
    page, has_next = 1, True
    while has_next:
        items, has_next = parse_list(client.get(list_url(page)).content)
        in_period = [i for i in items if raw.in_collect_period(i.published_at)]
        for item in in_period:
            if item.category not in EXCLUDED_CATEGORIES:
                targets[item.key] = item
        # 최신순이므로 한 페이지가 모두 기간 밖이면 그 뒤 페이지는 볼 필요가 없다
        if not in_period:
            break
        page += 1

    collected_at = datetime.now(UTC)

    def fetch_one(key: str, url: str) -> raw.RawPost:
        item = targets[key]
        return raw.RawPost(
            source=SOURCE,
            post_id=key,
            url=url,
            title=item.title,
            published_at=item.published_at,
            content_html=parse_article(client.get(url).text),
            collected_at=collected_at,
        )

    return collect_each(
        SOURCE, [(key, item.url) for key, item in targets.items()], fetch_one, raw_dir, refresh
    )
