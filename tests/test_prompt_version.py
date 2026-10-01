from datetime import UTC, datetime

from pipeline.collect.raw import RawPost
from pipeline.extract import prompt_version, prompts
from pipeline.extract.extractor import content_hash, extraction_reason
from pipeline.extract.schema import PostRecord

POST = RawPost(
    source="oliveyoung",
    post_id="p",
    url="https://example.com/p",
    title="제목",
    published_at=datetime(2025, 1, 1, tzinfo=UTC),
    content_html="<p>본문</p>",
    collected_at=datetime(2026, 9, 28, tzinfo=UTC),
)


def test_version_is_stable():
    assert prompt_version.version() == prompt_version.version()
    assert len(prompt_version.version()) == 12


def test_version_changes_when_instructions_change(monkeypatch):
    before = prompt_version.version()
    monkeypatch.setattr(prompts, "CLASSIFY", prompts.CLASSIFY + "\n추가 지시")
    assert prompt_version.version() != before


def test_version_covers_output_schema_descriptions(monkeypatch):
    # 스키마의 필드 설명도 LLM이 보는 지시이므로 바뀌면 버전이 바뀌어야 한다
    from pipeline.extract.schema import Classification

    before = prompt_version.version()
    field = Classification.model_fields["reason"]
    monkeypatch.setattr(field, "description", "바뀐 설명")
    Classification.model_rebuild(force=True)
    try:
        assert prompt_version.version() != before
    finally:
        monkeypatch.undo()
        Classification.model_rebuild(force=True)


def test_save_snapshot_writes_once(tmp_path):
    version = prompt_version.save_snapshot(tmp_path)
    path = tmp_path / f"{version}.md"
    text = path.read_text(encoding="utf-8")
    assert f"# 프롬프트 버전 {version}" in text
    assert prompts.CLASSIFY.strip() in text
    assert "출력 스키마: Extraction" in text

    # 이미 있으면 덮어쓰지 않는다
    path.write_text("기존 내용", encoding="utf-8")
    assert prompt_version.save_snapshot(tmp_path) == version
    assert path.read_text(encoding="utf-8") == "기존 내용"


def record(**overrides) -> PostRecord:
    base = dict(
        source="oliveyoung",
        post_id="p",
        url=POST.url,
        title="제목",
        published_at="2025-01-01",
        post_type="문제 해결형",
        kind="추출",
        reason="",
        content_hash=content_hash(POST),
        model="gpt-5-mini",
        prompt_version="v1",
        extracted_at="2026-09-28T00:00:00+00:00",
        entry_ids=[],
        dropped_evidence=0,
    )
    base.update(overrides)
    return PostRecord(**base)


def test_extraction_reason():
    def reason(previous, outdated=False, model="gpt-5-mini", version="v1"):
        return extraction_reason(previous, POST, model, version, outdated)

    assert reason(None) == "신규"
    assert reason(record(content_hash="changed")) == "원문 변경"
    # 기본 실행에서는 프롬프트·모델이 바뀌어도 건너뛴다 (비용 때문에 명시적으로 켠다)
    assert reason(record(), version="v2") is None
    assert reason(record(), model="gpt-5") is None
    assert reason(record()) is None
    # --outdated
    assert reason(record(), outdated=True, version="v2") == "프롬프트 변경 v1 → v2"
    assert reason(record(), outdated=True, model="gpt-5") == "모델 변경 gpt-5-mini → gpt-5"
    assert reason(record(), outdated=True) is None
