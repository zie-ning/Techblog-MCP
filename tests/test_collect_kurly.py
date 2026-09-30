from datetime import UTC, datetime
from pathlib import Path

import pytest

from pipeline.collect import kurly, raw
from pipeline.collect.common import ParseError

FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_feed():
    items = kurly.parse_feed((FIXTURES / "kurly_feed.xml").read_bytes())

    assert [i.post_id for i in items] == ["delivery-rag", "boundary", "old-post"]
    assert items[0].url == "https://helloworld.kurly.com/blog/delivery-rag/"
    assert items[0].title == "배송 도메인 RAG 적용기"
    assert items[0].published_at == datetime(2025, 3, 11, 15, tzinfo=UTC)
    kept = [i.post_id for i in items if raw.in_collect_period(i.published_at)]
    assert kept == ["delivery-rag", "boundary"]


def test_parse_article_keeps_only_body():
    body = kurly.parse_article((FIXTURES / "kurly_post.html").read_text(encoding="utf-8"))

    assert "임베딩 검색과 FTS를 섞었습니다." in body
    assert "<pre><code>search(q)" in body
    for noise in ["공유하기", "같은 카테고리", "다른 글", "2025년 03월 12일"]:
        assert noise not in body


def test_parse_article_without_body_fails():
    with pytest.raises(ParseError):
        kurly.parse_article("<html><body><main><article></article></main></body></html>")


def test_collect_fetches_only_posts_in_period(tmp_path, fake_client):
    page = (FIXTURES / "kurly_post.html").read_bytes()
    client = fake_client(
        {
            kurly.FEED_URL: (FIXTURES / "kurly_feed.xml").read_bytes(),
            "https://helloworld.kurly.com/blog/delivery-rag/": page,
            "https://helloworld.kurly.com/blog/boundary/": page,
        }
    )
    result = kurly.collect(client, tmp_path)

    assert "https://helloworld.kurly.com/blog/old-post/" not in client.requested
    assert [p.post_id for p in result.saved] == ["delivery-rag", "boundary"]
    assert result.saved[1].title == "경계일 글"
