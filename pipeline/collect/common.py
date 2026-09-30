"""여러 수집기가 함께 쓰는 사이트맵 파싱, 글별 수집 루프, 결과 형식."""

import sys
import xml.etree.ElementTree as ET
from collections.abc import Callable
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
    skipped: int = 0  # 이미 캐시돼 요청하지 않은 글
    out_of_period: int = 0  # 받아 보니 수집 기간 밖이라 저장하지 않은 글
    failures: list[tuple[str, str]] = field(default_factory=list)  # (URL, 이유)


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
) -> CollectResult:
    """(post_id, URL) 목록을 한 편씩 `fetch_one(post_id, url)`으로 받아 저장한다.

    이미 캐시된 글은 건너뛰어 중단 후 다시 실행하면 이어받는다.
    한 편이 실패해도 멈추지 않고 실패 목록에 모아 돌려준다.
    """
    result = CollectResult()
    for i, (post_id, url) in enumerate(targets, 1):
        if i % 20 == 0:
            print(f"  {source}: {i}/{len(targets)}", file=sys.stderr)
        if not refresh and raw.exists(source, post_id, raw_dir):
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
