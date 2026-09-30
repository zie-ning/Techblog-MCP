from datetime import UTC, datetime
from pathlib import Path

import httpx

from pipeline.collect import raw, woowahan

FIXTURES = Path(__file__).parent / "fixtures"
COLLECTED_AT = datetime(2026, 9, 30, tzinfo=UTC)


def test_parse_posts():
    posts = woowahan.parse_posts((FIXTURES / "woowahan_posts.json").read_bytes(), COLLECTED_AT)

    assert [p.post_id for p in posts] == ["27678", "13000", "12999"]
    first = posts[0]
    assert first.title == "주문 ‘자동승인’ 개선기"
    assert first.url == "https://techblog.woowahan.com/27678/"
    assert first.published_at == datetime(2025, 3, 12, 6, 40, 18, tzinfo=UTC)
    assert "<pre><code>SELECT 1;" in first.content_html


def test_collect_period_uses_kst():
    posts = woowahan.parse_posts((FIXTURES / "woowahan_posts.json").read_bytes(), COLLECTED_AT)
    kept = [p.post_id for p in posts if raw.in_collect_period(p.published_at)]
    assert kept == ["27678", "13000"]


def test_collect_follows_total_pages(tmp_path, fake_client):
    body = (FIXTURES / "woowahan_posts.json").read_bytes()
    headers = {"X-WP-TotalPages": "2"}
    client = fake_client(
        {
            woowahan.page_url(1): httpx.Response(200, content=body, headers=headers),
            woowahan.page_url(2): httpx.Response(200, content=b"[]", headers=headers),
        }
    )
    result = woowahan.collect(client, tmp_path)

    assert len(client.requested) == 2
    assert [p.post_id for p in result.saved] == ["27678", "13000"]
    assert raw.exists("woowahan", "27678", tmp_path)
