from datetime import UTC, datetime
from pathlib import Path

from pipeline.collect import d2, raw

FIXTURES = Path(__file__).parent / "fixtures"
COLLECTED_AT = datetime(2026, 9, 30, tzinfo=UTC)


def test_parse_list():
    items, has_next = d2.parse_list((FIXTURES / "d2_list_0.json").read_bytes())

    assert has_next
    assert [(i.post_id, i.category) for i in items] == [
        ("1000003", "helloworld"),
        ("1000002", "news"),
        ("1000001", "helloworld"),
    ]
    assert items[0].url == "https://d2.naver.com/helloworld/1000003"
    assert items[0].published_at == datetime(2025, 3, 12, tzinfo=UTC)
    # 1693494000000 = 한국 시간 2023-09-01 00:00
    assert raw.in_collect_period(items[2].published_at)


def test_parse_detail():
    post = d2.parse_detail((FIXTURES / "d2_detail.json").read_bytes(), COLLECTED_AT)

    assert post.post_id == "1000003"
    assert post.url == "https://d2.naver.com/helloworld/1000003"
    assert post.title == "추천 시스템 개선기"
    assert post.published_at == datetime(2025, 3, 12, tzinfo=UTC)
    assert "후보 생성 단계" in post.content_html


def test_collect_skips_news_and_stops_at_period_end(tmp_path, fake_client):
    detail = (FIXTURES / "d2_detail.json").read_bytes()
    client = fake_client(
        {
            d2.list_url(0): (FIXTURES / "d2_list_0.json").read_bytes(),
            d2.list_url(1): (FIXTURES / "d2_list_1.json").read_bytes(),
            d2.detail_url("1000003"): detail,
            d2.detail_url("1000001"): detail.replace(b"1741737600000", b"1693494000000").replace(
                b"1000003", b"1000001"
            ),
        }
    )
    result = d2.collect(client, tmp_path)

    assert d2.detail_url("1000002") not in client.requested  # news 제외
    assert [p.post_id for p in result.saved] == ["1000003", "1000001"]
    assert not result.failures
