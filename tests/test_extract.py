from datetime import UTC, datetime

from pipeline.collect.raw import RawPost
from pipeline.extract import prompt_version
from pipeline.extract.extractor import ExtractResult, extract_post
from pipeline.extract.schema import (
    CaseDraft,
    CaseExtraction,
    Classification,
    InsightDraft,
    InsightExtraction,
    Point,
    RejectedAlternativeDraft,
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

    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def parse(self, instructions, messages, schema):
        self.calls.append((schema, messages))
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
