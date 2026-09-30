from datetime import UTC, datetime
from pathlib import Path

import pytest

from pipeline.collect import ly
from pipeline.collect.common import ParseError

FIXTURES = Path(__file__).parent / "fixtures"
COLLECTED_AT = datetime(2026, 9, 30, tzinfo=UTC)
URL = "https://techblog.lycorp.co.jp/ko/rundeck-automation"


def test_parse_targets_keeps_only_korean_posts():
    targets = ly.parse_targets((FIXTURES / "ly_sitemap.xml").read_bytes())
    assert targets == [
        ("rundeck-automation", URL),
        ("20231001a", "https://techblog.lycorp.co.jp/ko/20231001a"),
    ]


def test_parse_post_keeps_only_body():
    html = (FIXTURES / "ly_post.html").read_text(encoding="utf-8")
    post = ly.parse_post(html, "rundeck-automation", URL, COLLECTED_AT)

    assert post.title == "서버 작업 자동화"
    assert post.published_at == datetime(2023, 10, 6, 2, 30, tzinfo=UTC)
    assert "<pre><code>ansible-playbook" in post.content_html
    for noise in ["also available", "Share on", "작성자"]:
        assert noise not in post.content_html


def test_parse_post_without_body_fails():
    with pytest.raises(ParseError):
        ly.parse_post("<html><body><article></article></body></html>", "x", URL, COLLECTED_AT)
