"""LY Corporation 기술블로그(한국어) 수집기.

다국어 사이트라 사이트맵(`/sitemap-0.xml`)에서 `/ko/{slug}` 한 단계 경로만 글로 본다
(`/ko/page/N`, `/ko/tag/...`는 목록 페이지). 한국어 블로그가 2023-10에 시작해 대부분 기간 안이지만
최종 판단은 페이지의 발행일로 한다.
"""

import re
from datetime import UTC, datetime
from pathlib import Path

from bs4 import BeautifulSoup

from pipeline.collect import raw
from pipeline.collect.common import CollectResult, ParseError, collect_each, parse_sitemap
from pipeline.collect.http import PoliteClient

SOURCE = "ly"
SITEMAP_URL = "https://techblog.lycorp.co.jp/sitemap-0.xml"

_POST_URL = re.compile(r"^https://techblog\.lycorp\.co\.jp/ko/([^/]+)$")


def parse_targets(sitemap: bytes) -> list[tuple[str, str]]:
    targets = []
    for entry in parse_sitemap(sitemap):
        match = _POST_URL.match(entry.loc)
        if match:
            targets.append((match.group(1), entry.loc))
    return targets


def parse_post(html: str, post_id: str, url: str, collected_at: datetime) -> raw.RawPost:
    soup = BeautifulSoup(html, "html.parser")
    title = soup.select_one("article h1.title")
    published = soup.find("meta", property="article:published_time")
    # 본문 앞뒤의 번역 안내·공유 버튼(header), 작성자 소개(footer)는 제외한다
    body = soup.select_one("article .post_content_wrap")
    if title is None or published is None or body is None:
        raise ParseError("제목(h1.title)·발행일(article:published_time)·본문 중 없음")
    return raw.RawPost(
        source=SOURCE,
        post_id=post_id,
        url=url,
        title=title.get_text().strip(),
        published_at=datetime.fromisoformat(published["content"].replace("Z", "+00:00")),
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
