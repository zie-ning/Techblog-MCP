import pytest
from conftest import ev, make_entry

from eval.inspect_run import build_report, cost
from pipeline.extract.schema import PostRecord, RejectedAlternative, Usage

PRICE = {
    "input": 1.0,
    "cached_input": 0.1,
    "output": 10.0,
    "batch": {"input": 0.5, "cached_input": 0.05, "output": 5.0},
}


def _record(post_id: str, kind: str, url: str, **overrides) -> PostRecord:
    base = dict(
        source="kakao",
        post_id=post_id,
        url=url,
        title=f"제목 {post_id}",
        published_at="2025-01-01",
        post_type="문제 해결형" if kind != "제외" else "회고·문화·행사",
        kind=kind,
        reason="이유",
        content_hash="h",
        model="m",
        reasoning_effort="medium",
        prompt_version="v1",
        extracted_at="2026-09-30T00:00:00+00:00",
        entry_ids=[],
        dropped_evidence=0,
        evidence_total=4,
        usage=Usage(calls=2, input_tokens=1000, cached_input_tokens=200, output_tokens=100),
    )
    base.update(overrides)
    return PostRecord(**base)


def test_cost_counts_cached_input_separately():
    usage = Usage(input_tokens=1_000_000, cached_input_tokens=400_000, output_tokens=100_000)
    assert cost(usage, PRICE) == pytest.approx(0.6 + 0.04 + 1.0)


def test_build_report_sections():
    posts = [
        _record("1", "추출", "https://e/1", dropped_evidence=1, dropped_evidences=["지어낸 문장"]),
        _record("2", "제외", "https://e/2", evidence_total=0),
    ]
    entry = make_entry(
        "case_0001",
        source="kakao",
        post_url="https://e/1",
        technologies=["Kafka"],
        technologies_raw=["Kafka", "kafkaTemplate"],
        problem_situation=[ev("문제")],
        solution=[ev("해결")],
        rejected_alternatives=[
            RejectedAlternative(name="Kafka", name_raw="카프카", reason="이유", evidence="e")
        ],
    )
    report = build_report(
        "run-a", posts, [entry], {"https://e/1": 5000, "https://e/2": 300}, {"m": PRICE}
    )
    assert "추출 1, 제외 1" in report
    assert "## 짧은 글 (평문 1,500자 미만) 1편" in report
    assert "kafkaTemplate (1)" in report
    assert "(technologies에도 있음)" in report
    assert "탈락 1개" in report and "지어낸 문장" in report
    assert "쏠림" in report  # 항목 1개라 한 분류가 100%
    assert "전체 1,262편 추정" in report
