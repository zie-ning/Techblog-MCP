from datetime import UTC, datetime
from pathlib import Path

from pipeline.collect import oliveyoung, raw

FIXTURES = Path(__file__).parent / "fixtures"

COLLECTED_AT = datetime(2026, 9, 28, tzinfo=UTC)


def test_parse_feed():
    posts = oliveyoung.parse_feed((FIXTURES / "oliveyoung_feed.xml").read_bytes(), COLLECTED_AT)

    assert [p.post_id for p in posts] == [
        "2025-03-12_coupon-issue",
        "2023-09-01_boundary",
        "2023-08-31_old-post",
    ]
    first = posts[0]
    assert first.title == "쿠폰 발급 개선기"
    assert first.url == "https://oliveyoung.tech/2025-03-12/coupon-issue/"
    assert first.published_at == datetime(2025, 3, 12, tzinfo=UTC)
    assert "Redis 원자 연산" in first.content_html


def test_collect_period_boundary():
    posts = oliveyoung.parse_feed((FIXTURES / "oliveyoung_feed.xml").read_bytes(), COLLECTED_AT)
    kept = [p.post_id for p in posts if raw.in_collect_period(p.published_at)]
    assert kept == ["2025-03-12_coupon-issue", "2023-09-01_boundary"]


def test_raw_roundtrip(tmp_path):
    post = oliveyoung.parse_feed((FIXTURES / "oliveyoung_feed.xml").read_bytes(), COLLECTED_AT)[0]
    raw.save(post, tmp_path)
    assert raw.load_all("oliveyoung", tmp_path) == [post]
