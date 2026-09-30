from datetime import datetime
from pathlib import Path

import pytest

from pipeline.collect import raw, toss
from pipeline.collect.common import ParseError
from pipeline.collect.raw import KST

FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_list():
    items, has_next = toss.parse_list((FIXTURES / "toss_list_1.json").read_bytes())

    assert has_next
    assert [(i.key, i.category) for i in items] == [
        ("smoke-test", "Engineering"),
        ("savings-character", "Design"),
        ("boundary", "프로덕트"),
    ]
    assert items[0].title == "스모크 테스트 자동화"
    assert items[0].url == "https://toss.tech/article/smoke-test"
    assert items[0].published_at == datetime(2025, 3, 12, 10, tzinfo=KST)


def test_parse_list_drops_unpublished():
    items, has_next = toss.parse_list((FIXTURES / "toss_list_2.json").read_bytes())
    assert not has_next
    assert [i.key for i in items] == ["old-post"]


def test_parse_article_keeps_only_body():
    body = toss.parse_article((FIXTURES / "toss_article.html").read_text(encoding="utf-8"))

    assert "매주 빌드를 손으로 확인했습니다." in body
    assert "<pre><code>run_smoke()" in body
    assert "작성자" not in body
    assert "공유하기" not in body


def test_parse_article_without_article_fails():
    with pytest.raises(ParseError):
        toss.parse_article("<html><body><p>빈 페이지</p></body></html>")


def test_collect_excludes_design(tmp_path, fake_client):
    article = (FIXTURES / "toss_article.html").read_bytes()
    client = fake_client(
        {
            toss.list_url(1): (FIXTURES / "toss_list_1.json").read_bytes(),
            toss.list_url(2): (FIXTURES / "toss_list_2.json").read_bytes(),
            "https://toss.tech/article/smoke-test": article,
            "https://toss.tech/article/boundary": article,
        }
    )
    result = toss.collect(client, tmp_path)

    assert "https://toss.tech/article/savings-character" not in client.requested
    assert [p.post_id for p in result.saved] == ["smoke-test", "boundary"]
    assert result.saved[0].title == "스모크 테스트 자동화"
    assert raw.exists("toss", "boundary", tmp_path)
