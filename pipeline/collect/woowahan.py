"""우아한형제들 기술블로그 수집기.

WordPress 공식 REST API(`/wp-json/wp/v2/posts`)가 발행일과 본문 HTML을 함께 주므로
목록 요청만으로 수집한다. 사이트맵의 lastmod는 수정일이라 쓰지 않는다.

사이트의 WAF가 Python TLS 클라이언트(httpx)의 요청을 robots.txt까지 403으로 막는다.
운영 측 허락을 받아(2026-09-30) 이 호스트만 시스템 curl로 요청한다 (`http.CURL_HOSTS`).
"""

import html
import json
from datetime import UTC, datetime
from pathlib import Path

from pipeline.collect import raw
from pipeline.collect.common import CollectResult
from pipeline.collect.http import PoliteClient

SOURCE = "woowahan"
API_URL = "https://techblog.woowahan.com/wp-json/wp/v2/posts"
_FIELDS = "id,date_gmt,link,title,content"


def page_url(page: int) -> str:
    since = f"{raw.COLLECT_SINCE.isoformat()}T00:00:00"
    return f"{API_URL}?per_page=100&page={page}&after={since}&_fields={_FIELDS}"


def parse_posts(body: bytes, collected_at: datetime) -> list[raw.RawPost]:
    """API 응답 한 페이지를 RawPost로 변환한다. 기간 필터는 적용하지 않는다."""
    return [
        raw.RawPost(
            source=SOURCE,
            post_id=str(item["id"]),
            url=item["link"],
            title=html.unescape(item["title"]["rendered"]).strip(),
            published_at=datetime.fromisoformat(item["date_gmt"]).replace(tzinfo=UTC),
            content_html=item["content"]["rendered"],
            collected_at=collected_at,
        )
        for item in json.loads(body)
    ]


def collect(
    client: PoliteClient, raw_dir: Path = raw.RAW_DIR, refresh: bool = False
) -> CollectResult:
    """API 목록을 끝까지 받아 저장한다. 목록에 본문이 있어 항상 덮어쓴다."""
    collected_at = datetime.now(UTC)
    posts: list[raw.RawPost] = []
    page, total_pages = 1, 1
    while page <= total_pages:
        response = client.get(page_url(page))
        total_pages = int(response.headers.get("X-WP-TotalPages", "1"))
        posts.extend(parse_posts(response.content, collected_at))
        page += 1

    posts = [p for p in posts if raw.in_collect_period(p.published_at)]
    for post in posts:
        raw.save(post, raw_dir)
    return CollectResult(saved=posts)
