"""컬리 기술블로그 수집기.

RSS 피드(`/rss.xml`)에 2019년부터의 전체 글 목록과 발행일이 있지만 본문은 요약뿐이라,
피드로 기간을 거른 뒤 글 페이지에서 본문을 받는다.
"""

import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlsplit

from bs4 import BeautifulSoup

from pipeline.collect import raw
from pipeline.collect.common import CollectResult, ParseError, collect_each
from pipeline.collect.http import PoliteClient

SOURCE = "kurly"
FEED_URL = "https://helloworld.kurly.com/rss.xml"


@dataclass
class FeedItem:
    post_id: str
    url: str
    title: str
    published_at: datetime


def post_id_from_url(url: str) -> str:
    """`https://helloworld.kurly.com/blog/2026-delivery-domain-rag/` → `2026-delivery-domain-rag`"""
    return urlsplit(url).path.strip("/").split("/")[-1]


def parse_feed(xml: bytes) -> list[FeedItem]:
    """피드의 모든 글을 돌려준다. 기간 필터는 적용하지 않는다."""
    items = []
    for item in ET.fromstring(xml).iter("item"):
        url = item.findtext("link", "").strip()
        items.append(
            FeedItem(
                post_id=post_id_from_url(url),
                url=url,
                title=item.findtext("title", "").strip(),
                published_at=parsedate_to_datetime(item.findtext("pubDate", "")),
            )
        )
    return items


def parse_article(html: str) -> str:
    """글 페이지에서 본문 HTML만 꺼낸다. 관련 글 카드도 `<article>`이라 본문 section으로 찾는다."""
    body = BeautifulSoup(html, "html.parser").select_one("main article section.prose")
    if body is None:
        raise ParseError("본문(article section.prose) 없음")
    return body.decode_contents()


def collect(
    client: PoliteClient, raw_dir: Path = raw.RAW_DIR, refresh: bool = False
) -> CollectResult:
    items = parse_feed(client.get(FEED_URL).content)
    targets = {i.post_id: i for i in items if raw.in_collect_period(i.published_at)}
    collected_at = datetime.now(UTC)

    def fetch_one(post_id: str, url: str) -> raw.RawPost:
        item = targets[post_id]
        return raw.RawPost(
            source=SOURCE,
            post_id=post_id,
            url=url,
            title=item.title,
            published_at=item.published_at,
            content_html=parse_article(client.get(url).text),
            collected_at=collected_at,
        )

    return collect_each(
        SOURCE, [(i.post_id, i.url) for i in targets.values()], fetch_one, raw_dir, refresh
    )
