from datetime import UTC, datetime, timedelta

from eval.sample_pilot import sample_posts
from pipeline.collect.raw import RawPost


def _posts(n: int) -> list[RawPost]:
    base = datetime(2024, 1, 1, tzinfo=UTC)
    return [
        RawPost(
            source="kakao",
            post_id=str(i),
            url=f"https://example.com/{i}",
            title=f"글 {i}",
            published_at=base + timedelta(days=i),
            content_html="<p>본문</p>",
            collected_at=base,
        )
        for i in range(n)
    ]


def test_sample_is_deterministic_and_excludes():
    posts = _posts(30)
    first = sample_posts(posts, "kakao", 10, seed=1, exclude={"3", "4"})
    # 입력 순서가 달라도 같은 시드면 같은 표본
    again = sample_posts(list(reversed(posts)), "kakao", 10, seed=1, exclude={"3", "4"})
    assert [p.post_id for p in first] == [p.post_id for p in again]
    assert len(first) == 10
    assert not {"3", "4"} & {p.post_id for p in first}
    # 발행일 순으로 정렬
    assert first == sorted(first, key=lambda p: p.published_at)
    # 블로그 이름이 다르면 다른 표본
    other = sample_posts(posts, "toss", 10, seed=1, exclude={"3", "4"})
    assert {p.post_id for p in other} != {p.post_id for p in first}


def test_sample_smaller_than_n():
    assert len(sample_posts(_posts(3), "kakao", 10)) == 3
