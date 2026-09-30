"""카카오 기술블로그 수집기.

사이트맵(`/sitemap.xml`)의 `/posts/N` 목록을 lastmod(발행일과 같음)로 먼저 거른 뒤
글 페이지를 받는다. 사이트가 Nuxt라 본문이 HTML 요소가 아니라
`<script id="__NUXT_DATA__">` 안의 직렬화된 데이터에 있다.
"""

import json
import re
from datetime import UTC, datetime, timedelta
from pathlib import Path

from bs4 import BeautifulSoup

from pipeline.collect import raw
from pipeline.collect.common import CollectResult, ParseError, collect_each, parse_sitemap
from pipeline.collect.http import PoliteClient

SOURCE = "kakao"
SITEMAP_URL = "https://tech.kakao.com/sitemap.xml"

_POST_URL = re.compile(r"^https://tech\.kakao\.com/posts/(\d+)$")
# lastmod와 실제 발행 시각(한국 시간)의 날짜 차이를 흡수하는 여유.
# 최종 판단은 페이지의 발행일로 한다
_LASTMOD_MARGIN = timedelta(days=2)
# Nuxt 직렬화(devalue)에서 반응형 값을 감싸는 표식
_WRAPPERS = {"Reactive", "ShallowReactive", "Ref", "ShallowRef"}
_POST_KEYS = {"id", "title", "content", "releaseDateTime"}


def parse_targets(sitemap: bytes) -> list[tuple[str, str]]:
    """사이트맵에서 수집 기간 근처의 글을 (post_id, URL)로 고른다."""
    since = raw.COLLECT_SINCE - _LASTMOD_MARGIN
    targets = []
    for entry in parse_sitemap(sitemap):
        match = _POST_URL.match(entry.loc)
        if match and (entry.lastmod is None or entry.lastmod >= since):
            targets.append((match.group(1), entry.loc))
    return targets


def _resolve(payload: list, value):
    """devalue 형식에서 인덱스 참조를 따라가 실제 값을 꺼낸다 (문자열·숫자 필드용)."""
    if isinstance(value, int) and not isinstance(value, bool):
        value = payload[value]
    if isinstance(value, list) and len(value) == 2 and value[0] in _WRAPPERS:
        return _resolve(payload, value[1])
    return value


def parse_post(html: str, url: str, collected_at: datetime) -> raw.RawPost:
    script = BeautifulSoup(html, "html.parser").find("script", id="__NUXT_DATA__")
    if script is None:
        raise ParseError("__NUXT_DATA__ 없음")
    payload = json.loads(script.get_text())
    post = next(
        (x for x in payload if isinstance(x, dict) and _POST_KEYS <= x.keys()),
        None,
    )
    if post is None:
        raise ParseError("글 데이터(id, title, content, releaseDateTime) 없음")

    released = _resolve(payload, post["releaseDateTime"])  # 예: "2026.09.23 10:01:00"
    return raw.RawPost(
        source=SOURCE,
        post_id=str(_resolve(payload, post["id"])),
        url=url,
        title=_resolve(payload, post["title"]).strip(),
        published_at=datetime.strptime(released, "%Y.%m.%d %H:%M:%S").replace(tzinfo=raw.KST),
        content_html=_resolve(payload, post["content"]),
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
        lambda post_id, url: parse_post(client.get(url).text, url, collected_at),
        raw_dir,
        refresh,
    )
