from datetime import UTC, datetime
from pathlib import Path

import pytest

from pipeline.collect import kakaopay, raw
from pipeline.collect.common import ParseError
from pipeline.collect.raw import KST

FIXTURES = Path(__file__).parent / "fixtures"
COLLECTED_AT = datetime(2026, 9, 30, tzinfo=UTC)
URL = "https://tech.kakaopay.com/post/payment-retry/"


def test_parse_targets_keeps_only_posts():
    targets = kakaopay.parse_targets((FIXTURES / "kakaopay_sitemap.xml").read_bytes())
    assert targets == [
        ("payment-retry", URL),
        ("2023-jan-festival", "https://tech.kakaopay.com/post/2023-jan-festival/"),
    ]


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("2023. 2. 3", datetime(2023, 2, 3, tzinfo=KST)),
        (" 2025. 12. 31 ", datetime(2025, 12, 31, tzinfo=KST)),
    ],
)
def test_parse_date(text, expected):
    assert kakaopay.parse_date(text) == expected


def test_parse_date_invalid():
    with pytest.raises(ParseError):
        kakaopay.parse_date("어제")


def test_parse_post():
    html = (FIXTURES / "kakaopay_post.html").read_text(encoding="utf-8")
    post = kakaopay.parse_post(html, "payment-retry", URL, COLLECTED_AT)

    assert post.title == "결제 재시도 설계"
    assert post.published_at == datetime(2025, 3, 12, tzinfo=KST)
    assert "<pre><code>retry(3)" in post.content_html
    assert "링크 복사" not in post.content_html
    assert "<article" not in post.content_html


def test_collect_drops_posts_outside_period(tmp_path, fake_client):
    html = (FIXTURES / "kakaopay_post.html").read_bytes()
    client = fake_client(
        {
            kakaopay.SITEMAP_URL: (FIXTURES / "kakaopay_sitemap.xml").read_bytes(),
            URL: html,
            "https://tech.kakaopay.com/post/2023-jan-festival/": html.replace(
                b"2025. 3. 12", b"2023. 8. 31"
            ),
        }
    )
    result = kakaopay.collect(client, tmp_path)

    assert [p.post_id for p in result.saved] == ["payment-retry"]
    assert result.out_of_period == 1
    assert not raw.exists("kakaopay", "2023-jan-festival", tmp_path)
