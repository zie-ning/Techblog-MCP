import json
from datetime import UTC, datetime

import pytest

from pipeline.collect.raw import RawPost
from pipeline.extract import prompt_version
from pipeline.extract.__main__ import parse_post_ids
from pipeline.extract.extractor import ExtractResult, extract_post
from pipeline.extract.schema import (
    CaseDraft,
    CaseExtraction,
    Classification,
    InsightDraft,
    InsightExtraction,
    Point,
    RejectedAlternativeDraft,
    Usage,
)
from pipeline.extract.store import Store

POST = RawPost(
    source="oliveyoung",
    post_id="2025-03-12_coupon",
    url="https://oliveyoung.tech/2025-03-12/coupon/",
    title="쿠폰 발급 개선기",
    published_at=datetime(2025, 3, 12, tzinfo=UTC),
    content_html=(
        "<p>세일 기간에 쿠폰이 한도를 넘어 발급되는 문제가 있었습니다.</p>"
        "<p>Redis의 원자 연산으로 발급 수량을 관리했습니다.</p>"
        "<p>Kafka도 검토했지만 파티션을 줄일 수 없어 제외했습니다.</p>"
        "<p>초과 발급이 더 이상 발생하지 않았습니다.</p>"
    ),
    collected_at=datetime(2026, 9, 28, tzinfo=UTC),
)


class FakeLLM:
    """스키마별로 미리 정한 응답을 순서대로 돌려준다."""

    model = "fake-model"
    reasoning_effort = "medium"

    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []
        self.steps = []

    def parse(self, instructions, messages, schema, usage, step):
        self.calls.append((schema, messages))
        self.steps.append(step)
        usage.add(Usage(calls=1, input_tokens=100, output_tokens=10))
        response = self.responses.pop(0)
        assert isinstance(response, schema)
        return response


def case(**overrides) -> CaseDraft:
    base = dict(
        primary_problem_type="동시성·락",
        secondary_problem_types=["동시성·락", "트래픽 급증 대응", "캐싱", "비용 절감"],
        domain="커머스·주문·재고",
        technologies=["레디스", "spring-boot", "사내 발급기", "레디스"],
        tags=["쿠폰"],
        problem_situation=[
            Point(text="한도 초과 발급", evidence="쿠폰이 한도를 넘어 발급되는 문제가 있었습니다.")
        ],
        solution=[
            Point(
                text="Redis 원자 연산", evidence="Redis의 원자 연산으로 발급 수량을 관리했습니다."
            )
        ],
        performance_ops=[
            Point(text="초과 발급 해소", evidence="초과 발급이 더 이상 발생하지 않았습니다."),
            Point(text="지어낸 수치", evidence="처리량이 10배 늘었습니다."),
        ],
        rejected_alternatives=[
            RejectedAlternativeDraft(
                name="카프카",
                reason="파티션 축소 불가",
                evidence="Kafka도 검토했지만 파티션을 줄일 수 없어 제외했습니다.",
            )
        ],
    )
    base.update(overrides)
    return CaseDraft(**base)


CLASSIFIED_CASE = Classification(post_type="문제 해결형", kind="사례", reason="문제 해결")


def test_extract_case_verifies_and_normalizes():
    # 첫 결과에 지어낸 발췌가 있으면 한 번 다시 요청하고, 그래도 남은 항목은 버린다
    llm = FakeLLM([CLASSIFIED_CASE, CaseExtraction(cases=[case()]), CaseExtraction(cases=[case()])])
    result = extract_post(POST, llm)

    assert [c[0] for c in llm.calls] == [Classification, CaseExtraction, CaseExtraction]
    assert llm.steps == ["분류", "구조화", "재시도"]
    assert "처리량이 10배" in llm.calls[2][1][-1]["content"]  # 재요청에 실패 발췌를 알려 줌

    assert result.record.kind == "사례"
    assert result.record.prompt_version == prompt_version.version()
    assert result.record.dropped_evidence == 1
    [entry] = result.entries
    assert entry.company == "올리브영"
    assert entry.published_at == "2025-03-12"
    assert [p.text for p in entry.performance_ops] == ["초과 발급 해소"]
    # 보조 유형: 주 유형 제거, 중복 제거, 최대 2개
    assert entry.secondary_problem_types == ["트래픽 급증 대응", "캐싱"]
    # 기술명: 사전으로 정규화하고 사전에 없는 이름은 raw에만 남긴다
    assert entry.technologies == ["Redis", "Spring Boot"]
    assert entry.technologies_raw == ["레디스", "spring-boot", "사내 발급기"]
    assert entry.rejected_alternatives[0].name == "Kafka"
    assert entry.rejected_alternatives[0].name_raw == "카프카"


def test_rejected_alternative_keeps_raw_name_when_same_as_used_technology():
    # "Claude 3 Haiku"를 버리고 "Claude 3.5 Sonnet"을 썼다면 "Claude를 버렸다"로 기록하지 않는다
    drafted = case(
        technologies=["Claude 3.5 Sonnet"],
        rejected_alternatives=[
            RejectedAlternativeDraft(
                name="Claude 3 Haiku",
                reason="정확도 부족",
                evidence="Kafka도 검토했지만 파티션을 줄일 수 없어 제외했습니다.",
            )
        ],
        performance_ops=[],
    )
    llm = FakeLLM([CLASSIFIED_CASE, CaseExtraction(cases=[drafted])])
    [entry] = extract_post(POST, llm).entries
    assert entry.technologies == ["Claude"]
    assert entry.rejected_alternatives[0].name == "Claude 3 Haiku"


def test_extract_drops_case_without_required_fields():
    bad = case(solution=[Point(text="지어냄", evidence="원문에 없는 해결 방법입니다.")])
    good = case(performance_ops=[])
    llm = FakeLLM(
        [CLASSIFIED_CASE, CaseExtraction(cases=[bad, good]), CaseExtraction(cases=[bad, good])]
    )
    result = extract_post(POST, llm)
    assert len(result.entries) == 1


def test_keeps_better_attempt_when_retry_is_worse():
    first = case()  # 지어낸 발췌 1개만 탈락
    worse = case(solution=[Point(text="지어냄", evidence="원문에 없는 해결 방법입니다.")])
    llm = FakeLLM([CLASSIFIED_CASE, CaseExtraction(cases=[first]), CaseExtraction(cases=[worse])])
    result = extract_post(POST, llm)
    assert len(result.entries) == 1
    assert result.record.dropped_evidences == ["처리량이 10배 늘었습니다."]


def test_no_retry_when_all_evidence_found():
    llm = FakeLLM([CLASSIFIED_CASE, CaseExtraction(cases=[case(performance_ops=[])])])
    result = extract_post(POST, llm)
    assert len(llm.calls) == 2
    assert result.record.dropped_evidence == 0


def test_excluded_post_has_no_entries():
    llm = FakeLLM([Classification(post_type="회고·문화·행사", kind="제외", reason="회고")])
    result = extract_post(POST, llm)
    assert result.record.kind == "제외"
    assert result.entries == []


def test_extract_insight():
    insight = InsightDraft(
        primary_problem_type="개발 생산성",
        secondary_problem_types=[],
        domain="범용",
        technologies=[],
        tags=[],
        key_points=[Point(text="원자 연산", evidence="Redis의 원자 연산으로")],
        takeaways=[],
    )
    llm = FakeLLM(
        [
            Classification(post_type="실험·활용기", kind="인사이트", reason="팁"),
            InsightExtraction(insight=insight),
        ]
    )
    [entry] = extract_post(POST, llm).entries
    assert entry.kind == "인사이트"
    assert entry.key_points[0].text == "원자 연산"


def _result(n_entries: int) -> ExtractResult:
    llm = FakeLLM([CLASSIFIED_CASE, CaseExtraction(cases=[case(performance_ops=[])] * n_entries)])
    return extract_post(POST, llm)


def test_store_assigns_stable_ids(tmp_path):
    store = Store(tmp_path / "posts.jsonl", tmp_path / "entries.jsonl")
    assert store.add(_result(2)) == ["case_0001", "case_0002"]
    store.save()

    # 다시 추출하면 옛 항목을 지우고 번호를 재사용하지 않는다
    reloaded = Store(tmp_path / "posts.jsonl", tmp_path / "entries.jsonl")
    assert [e.id for e in reloaded.entries] == ["case_0001", "case_0002"]
    assert reloaded.add(_result(1)) == ["case_0003"]
    reloaded.save()

    final = Store(tmp_path / "posts.jsonl", tmp_path / "entries.jsonl")
    assert [e.id for e in final.entries] == ["case_0003"]
    assert final.record_for(POST.url).entry_ids == ["case_0003"]


def test_record_keeps_usage_and_evidence_total():
    # 첫 시도 발췌 5개(1개 탈락) → 재시도도 같아서 첫 시도를 쓴다. 호출 3회의 사용량 합계
    llm = FakeLLM([CLASSIFIED_CASE, CaseExtraction(cases=[case()]), CaseExtraction(cases=[case()])])
    result = extract_post(POST, llm)
    assert result.record.evidence_total == 5
    assert result.record.reasoning_effort == "medium"
    assert result.record.usage == Usage(calls=3, input_tokens=300, output_tokens=30)
    # 검증 전 출력은 재시도까지 모두 남긴다
    assert result.raw_outputs["classification"]["kind"] == "사례"
    assert len(result.raw_outputs["attempts"]) == 2


def test_store_in_dir_saves_drafts(tmp_path):
    store = Store.in_dir(tmp_path / "run", save_drafts=True)
    store.add(_result(1))
    store.save()
    [line] = (tmp_path / "run" / "drafts.jsonl").read_text(encoding="utf-8").splitlines()
    draft = json.loads(line)
    assert (draft["source"], draft["post_id"]) == ("oliveyoung", "2025-03-12_coupon")
    assert len(draft["attempts"]) == 1
    assert (tmp_path / "run" / "posts.jsonl").exists()

    # drafts를 끄면 파일을 만들지 않는다
    plain = Store.in_dir(tmp_path / "plain")
    plain.add(_result(1))
    plain.save()
    assert not (tmp_path / "plain" / "drafts.jsonl").exists()


def test_old_post_record_without_new_fields_loads():
    old = {
        "source": "oliveyoung",
        "post_id": "x",
        "url": "u",
        "title": "t",
        "published_at": "2025-01-01",
        "post_type": "문제 해결형",
        "kind": "사례",
        "reason": "r",
        "content_hash": "h",
        "model": "gpt-5-mini",
        "prompt_version": "v",
        "extracted_at": "2026-09-28T00:00:00+00:00",
        "entry_ids": [],
        "dropped_evidence": 0,
    }
    from pipeline.extract.schema import PostRecord

    record = PostRecord.model_validate_json(json.dumps(old))
    assert record.usage == Usage() and record.evidence_total == 0


def test_parse_post_ids():
    lines = ["# 주석", "kakao/599  # 제목", "", "2023-09-18_coupon"]
    assert parse_post_ids(lines, "oliveyoung") == [
        ("kakao", "599"),
        ("oliveyoung", "2023-09-18_coupon"),
    ]
    assert parse_post_ids(["d2/0004394"], "all") == [("d2", "0004394")]
    with pytest.raises(ValueError):
        parse_post_ids(["599"], "all")
