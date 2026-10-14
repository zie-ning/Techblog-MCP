"""여러 수집기가 함께 쓰는 사이트맵 파싱, 글별 수집 루프, 결과 형식."""

import sys
import xml.etree.ElementTree as ET
from collections.abc import Callable, Collection
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import httpx

from pipeline.collect import raw
from pipeline.collect.http import DisallowedByRobots

_SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


class ParseError(ValueError):
    """응답에서 기대한 구조(본문, 발행일 등)를 찾지 못했을 때 발생한다."""


@dataclass
class CollectResult:
    saved: list[raw.RawPost] = field(default_factory=list)
    skipped: int = 0  # 이미 캐시됐거나 추출 기록이 있어 요청하지 않은 글
    out_of_period: int = 0  # 받아 보니 수집 기간 밖이라 저장하지 않은 글
    failures: list[tuple[str, str]] = field(default_factory=list)  # (URL, 이유)
    # 목록에서 본 글 중 `known`(추출 기록)에 있는 글 수. 목록 형식이 바뀌어 파싱이 깨지면
    # 기존 글도 함께 안 보여 이 값이 줄어든다 (pipeline/update.py가 판단)
    listed_known: int = 0


@dataclass
class SitemapEntry:
    loc: str
    lastmod: date | None


def parse_sitemap(xml: bytes) -> list[SitemapEntry]:
    root = ET.fromstring(xml)
    entries = []
    for url in root.iter(f"{_SITEMAP_NS}url"):
        lastmod = url.findtext(f"{_SITEMAP_NS}lastmod")
        entries.append(
            SitemapEntry(
                loc=url.findtext(f"{_SITEMAP_NS}loc", "").strip(),
                lastmod=date.fromisoformat(lastmod.strip()[:10]) if lastmod else None,
            )
        )
    return entries


def collect_each(
    source: str,
    targets: list[tuple[str, str]],
    fetch_one: Callable[[str, str], raw.RawPost],
    raw_dir: Path = raw.RAW_DIR,
    refresh: bool = False,
    known: Collection[str] = frozenset(),
) -> CollectResult:
    """(post_id, URL) 목록을 한 편씩 `fetch_one(post_id, url)`으로 받아 저장한다.

    이미 캐시된 글과 `known`(이미 추출한 글의 post_id)은 건너뛰어 중단 후 다시 실행하면
    이어받고, 원문 캐시가 없는 환경에서도 새 글만 받는다. `refresh`면 둘 다 무시한다.
    한 편이 실패해도 멈추지 않고 실패 목록에 모아 돌려준다.
    """
    result = CollectResult(listed_known=len({post_id for post_id, _ in targets} & set(known)))
    for i, (post_id, url) in enumerate(targets, 1):
        if i % 20 == 0:
            print(f"  {source}: {i}/{len(targets)}", file=sys.stderr)
        if not refresh and (post_id in known or raw.exists(source, post_id, raw_dir)):
            result.skipped += 1
            continue
        try:
            post = fetch_one(post_id, url)
        except (httpx.HTTPError, DisallowedByRobots, ValueError, KeyError) as e:
            result.failures.append((url, f"{type(e).__name__}: {e}"))
            continue
        if not raw.in_collect_period(post.published_at):
            result.out_of_period += 1
            continue
        raw.save(post, raw_dir)
        result.saved.append(post)
    return result


def save_feed_posts(
    posts: list[raw.RawPost],
    raw_dir: Path = raw.RAW_DIR,
    refresh: bool = False,
    known: Collection[str] = frozenset(),
) -> CollectResult:
    """목록 응답에 본문까지 들어 있는 블로그용: 기간 안의 글을 저장한다.

    본문을 이미 받았으므로 캐시와 관계없이 덮어쓰되, `known`(이미 추출한 글)은
    `collect_each`와 같은 기준으로 건너뛴다.
    """
    in_period = [p for p in posts if raw.in_collect_period(p.published_at)]
    result = CollectResult(listed_known=len({p.post_id for p in in_period} & set(known)))
    for post in in_period:
        if not refresh and post.post_id in known:
            result.skipped += 1
            continue
        raw.save(post, raw_dir)
        result.saved.append(post)
    return result
