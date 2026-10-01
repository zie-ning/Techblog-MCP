import pytest
from pydantic import ValidationError

from eval.gold import GOLD_DIR, GoldEntry, GoldPost, load_gold, render_reference
from techblog_mcp import taxonomy


def _post(**overrides) -> dict:
    base = dict(
        source="kakao",
        post_id="1",
        url="https://e/1",
        title="제목",
        post_type="문제 해결형",
        kind="추출",
        entries=[
            GoldEntry(
                summary="요약",
                primary_problem_type="캐싱",
                domain="범용",
                technologies=["Redis"],
                key_facts=["초당 3만 요청"],
            )
        ],
        notes="",
    )
    base.update(overrides)
    return base


def test_gold_post_checks_entries_against_kind():
    GoldPost(**_post())
    with pytest.raises(ValidationError):
        GoldPost(**_post(kind="제외"))  # 제외 글에 항목이 있음
    with pytest.raises(ValidationError):
        GoldPost(**_post(entries=[]))  # 추출 글에 항목이 없음
    with pytest.raises(ValidationError):
        GoldPost(**_post(kind="인사이트"))  # 없앤 값


def test_gold_rejects_unknown_category():
    with pytest.raises(ValidationError):
        GoldEntry(
            summary="s",
            primary_problem_type="없는 유형",
            domain="범용",
            technologies=[],
            key_facts=[],
        )


def test_saved_gold_files_are_valid():
    # 저장된 정답 파일이 모두 형식을 지키고, 기술명이 사전에 있으면 표준 이름을 쓰는지
    for gold in load_gold().values():
        for entry in gold.entries:
            for name in entry.technologies:
                normalized = taxonomy.normalize_technology(name)
                assert normalized in (None, name), f"{gold.post_id}: {name} → {normalized}"


def test_reference_covers_every_value_and_is_up_to_date():
    reference = render_reference()
    for name in (*taxonomy.problem_type_names(), *taxonomy.domain_names()):
        assert f"| {name} |" in reference
    # 분류 목록·정의를 바꾸고 다시 생성하지 않으면 실패한다
    assert (GOLD_DIR / "REFERENCE.md").read_text(encoding="utf-8") == reference
