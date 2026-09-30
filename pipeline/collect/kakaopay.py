"""카카오페이 기술블로그 수집기.

피드(`/rss.xml`)가 비어 있어 사이트맵(`/sitemap-0.xml`)의 `/post/{slug}/` 목록으로 글을 찾는다.
사이트맵에 날짜가 없어 모든 글 페이지를 받은 뒤 페이지의 발행일로 기간을 거른다.
"""

import re
from datetime import UTC, datetime
from pathlib import Path

from bs4 import BeautifulSoup

from pipeline.collect import raw
from pipeline.collect.common import CollectResult, ParseError, collect_each, parse_sitemap
from pipeline.collect.http import PoliteClient

SOURCE = "kakaopay"
SITEMAP_URL = "https://tech.kakaopay.com/sitemap-0.xml"

_POST_URL = re.compile(r"^https://tech\.kakaopay\.com/post/([^/]+)/$")
_DATE = re.compile(r"(\d{4})\.\s*(\d{1,2})\.\s*(\d{1,2})")


def parse_targets(sitemap: bytes) -> list[tuple[str, str]]:
    targets = []
    for entry in parse_sitemap(sitemap):
        match = _POST_URL.match(entry.loc)
        if match:
            targets.append((match.group(1), entry.loc))
    return targets


def parse_date(text: str) -> datetime:
    """`2023. 2. 3` 형식의 날짜를 한국 시간 자정으로 바꾼다."""
    match = _DATE.search(text)
    if match is None:
        raise ParseError(f"날짜 형식이 아님: {text!r}")
    year, month, day = map(int, match.groups())
    return datetime(year, month, day, tzinfo=raw.KST)


def parse_post(html: str, post_id: str, url: str, collected_at: datetime) -> raw.RawPost:
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find("h1")
    published = soup.select_one(".header-post-info time")
    body = soup.select_one("article.markdown")
    if title is None or published is None or body is None:
        raise ParseError("제목(h1)·발행일(.header-post-info time)·본문(article.markdown) 중 없음")
    return raw.RawPost(
        source=SOURCE,
        post_id=post_id,
        url=url,
        title=title.get_text().strip(),
        published_at=parse_date(published.get_text()),
        content_html=body.decode_contents(),
        collected_at=collected_at,
    )


def collect(
    client: PoliteClient, raw_dir: Path = raw.RAW_DIR, refresh: bool = False
) -> CollectResult:
    targets = parse_targets(client.get(SITEMAP_URL).content)
    collected_at = datetime.now(UTC)
    return collect_each(
        SOURCE,
        targets,
        lambda post_id, url: parse_post(client.get(url).text, post_id, url, collected_at),
        raw_dir,
        refresh,
    )
