from datetime import UTC, date, datetime

import httpx

from pipeline.collect import raw
from pipeline.collect.common import ParseError, collect_each, parse_sitemap, save_feed_posts

SITEMAP = b"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://example.com/posts/2</loc><lastmod>2024-01-02T10:00:00+09:00</lastmod></url>
  <url><loc>https://example.com/posts/1</loc></url>
</urlset>"""


def test_parse_sitemap():
    entries = parse_sitemap(SITEMAP)
    assert [(e.loc, e.lastmod) for e in entries] == [
        ("https://example.com/posts/2", date(2024, 1, 2)),
        ("https://example.com/posts/1", None),
    ]


def _post(post_id: str, published_at: datetime) -> raw.RawPost:
    return raw.RawPost(
        source="test",
        post_id=post_id,
        url=f"https://example.com/{post_id}",
        title=post_id,
        published_at=published_at,
        content_html="<p>본문</p>",
        collected_at=datetime(2026, 9, 30, tzinfo=UTC),
    )


def test_collect_each_skips_cached_and_records_failures(tmp_path):
    raw.save(_post("cached", datetime(2024, 1, 1, tzinfo=UTC)), tmp_path)
    requested = []

    def fetch_one(post_id, url):
        requested.append(post_id)
        if post_id == "http-error":
            raise httpx.ConnectError("연결 실패")
        if post_id == "broken":
            raise ParseError("본문 없음")
        if post_id == "old":
            return _post(post_id, datetime(2023, 8, 31, tzinfo=UTC))
        return _post(post_id, datetime(2024, 5, 1, tzinfo=UTC))

    targets = [(pid, f"https://example.com/{pid}") for pid in
               ["cached", "new", "http-error", "broken", "old"]]  # fmt: skip
    result = collect_each("test", targets, fetch_one, tmp_path)

    assert requested == ["new", "http-error", "broken", "old"]
    assert [p.post_id for p in result.saved] == ["new"]
    assert result.skipped == 1
    assert result.out_of_period == 1
    assert [url for url, _ in result.failures] == [
        "https://example.com/http-error",
        "https://example.com/broken",
    ]
    assert raw.exists("test", "new", tmp_path)
    assert not raw.exists("test", "old", tmp_path)


def test_collect_each_refresh_refetches_cached(tmp_path):
    raw.save(_post("cached", datetime(2024, 1, 1, tzinfo=UTC)), tmp_path)
    result = collect_each(
        "test",
        [("cached", "https://example.com/cached")],
        lambda pid, url: _post(pid, datetime(2024, 2, 1, tzinfo=UTC)),
        tmp_path,
        refresh=True,
    )
    assert [p.published_at.month for p in result.saved] == [2]


def test_collect_period_is_judged_in_kst():
    # 한국 시간 2023-09-01 00:00 = UTC 2023-08-31 15:00
    assert raw.in_collect_period(datetime(2023, 8, 31, 15, 0, tzinfo=UTC))
    assert not raw.in_collect_period(datetime(2023, 8, 31, 14, 59, tzinfo=UTC))


def test_collect_each_skips_known_without_cache(tmp_path):
    # 원문 캐시가 없는 환경에서도 추출 기록이 있는 글은 다시 받지 않는다
    requested = []

    def fetch_one(post_id, url):
        requested.append(post_id)
        return _post(post_id, datetime(2024, 5, 1, tzinfo=UTC))

    targets = [(pid, f"https://example.com/{pid}") for pid in ["known", "new"]]
    result = collect_each("test", targets, fetch_one, tmp_path, known={"known"})
    assert requested == ["new"]
    assert result.skipped == 1
    # 목록에 없는 추출 기록("gone")은 세지 않는다
    assert (
        collect_each("test", targets, fetch_one, tmp_path, known={"known", "gone"}).listed_known
        == 1
    )

    requested.clear()
    result = collect_each("test", targets, fetch_one, tmp_path, refresh=True, known={"known"})
    assert requested == ["known", "new"]
    assert result.listed_known == 1


def test_save_feed_posts_skips_known_and_out_of_period(tmp_path):
    posts = [
        _post("known", datetime(2024, 1, 1, tzinfo=UTC)),
        _post("new", datetime(2024, 1, 2, tzinfo=UTC)),
        _post("old", datetime(2023, 8, 1, tzinfo=UTC)),
    ]
    result = save_feed_posts(posts, tmp_path, known={"known", "old", "gone"})
    assert [p.post_id for p in result.saved] == ["new"]
    assert result.skipped == 1
    assert result.listed_known == 1  # 기간 밖 글과 목록에 없는 글은 세지 않는다
    assert not raw.exists("test", "known", tmp_path)
