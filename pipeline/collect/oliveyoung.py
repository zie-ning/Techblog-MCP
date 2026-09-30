"""올리브영 테크블로그 수집기.

RSS 피드(`/rss.xml`)에 2020년부터의 전체 글이 본문과 함께 들어 있어 피드 요청 한 번으로 수집한다.
"""

import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlsplit

from pipeline.collect import raw
from pipeline.collect.common import CollectResult
from pipeline.collect.http import PoliteClient

SOURCE = "oliveyoung"
FEED_URL = "https://oliveyoung.tech/rss.xml"

_CONTENT_TAG = "{http://purl.org/rss/1.0/modules/content/}encoded"


def post_id_from_url(url: str) -> str:
    """`https://oliveyoung.tech/2026-09-23/order-cancellation/` → `2026-09-23_order-cancellation`"""
    path = urlsplit(url).path.strip("/")
    return path.replace("/", "_")


def parse_feed(xml: bytes, collected_at: datetime) -> list[raw.RawPost]:
    """피드의 모든 글을 RawPost로 변환한다. 기간 필터는 적용하지 않는다."""
    root = ET.fromstring(xml)
    posts = []
    for item in root.iter("item"):
        url = item.findtext("link", "").strip()
        posts.append(
            raw.RawPost(
                source=SOURCE,
                post_id=post_id_from_url(url),
                url=url,
                title=item.findtext("title", "").strip(),
                published_at=parsedate_to_datetime(item.findtext("pubDate", "")),
                content_html=item.findtext(_CONTENT_TAG, ""),
                collected_at=collected_at,
            )
        )
    return posts


def collect(
    client: PoliteClient, raw_dir: Path = raw.RAW_DIR, refresh: bool = False
) -> CollectResult:
    """피드를 받아 수집 기간 안의 글을 저장한다.

    피드에 본문이 있어 `refresh`와 관계없이 항상 덮어쓴다.
    """
    response = client.get(FEED_URL)
    posts = parse_feed(response.content, collected_at=datetime.now(UTC))
    posts = [p for p in posts if raw.in_collect_period(p.published_at)]
    for post in posts:
        raw.save(post, raw_dir)
    return CollectResult(saved=posts)
