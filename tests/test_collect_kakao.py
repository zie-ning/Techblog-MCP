from datetime import UTC, datetime
from pathlib import Path

import pytest

from pipeline.collect import kakao
from pipeline.collect.common import ParseError
from pipeline.collect.raw import KST

FIXTURES = Path(__file__).parent / "fixtures"
COLLECTED_AT = datetime(2026, 9, 30, tzinfo=UTC)


def test_parse_targets_filters_posts_by_lastmod():
    targets = kakao.parse_targets((FIXTURES / "kakao_sitemap.xml").read_bytes())
    # lastmod 2023-08-31은 여유 기간 안이라 받아 본 뒤 발행일로 판단한다
    assert targets == [
        ("837", "https://tech.kakao.com/posts/837"),
        ("600", "https://tech.kakao.com/posts/600"),
    ]


def test_parse_post_reads_nuxt_payload():
    html = (FIXTURES / "kakao_post.html").read_text(encoding="utf-8")
    post = kakao.parse_post(html, "https://tech.kakao.com/posts/837", COLLECTED_AT)

    assert post.post_id == "837"
    assert post.title == "랭킹 모델 개발기"
    assert post.published_at == datetime(2025, 3, 12, 10, 1, tzinfo=KST)
    assert "<pre><code>model.fit()" in post.content_html


def test_parse_post_without_payload_fails():
    with pytest.raises(ParseError):
        kakao.parse_post("<html><body></body></html>", "u", COLLECTED_AT)


def test_resolve_unwraps_reactive():
    payload = [["Ref", 1], "값"]
    assert kakao._resolve(payload, 0) == "값"
