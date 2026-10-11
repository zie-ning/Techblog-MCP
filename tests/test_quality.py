from pipeline.extract import quality
from pipeline.extract.schema import PostRecord


def record(url: str, dropped: int, total: int, first: tuple[int, int] | None = None) -> PostRecord:
    return PostRecord(
        source="oliveyoung",
        post_id=url,
        url=url,
        title="t",
        published_at="2026-10-01",
        post_type="문제 해결형",
        kind="추출",
        reason="r",
        content_hash="h",
        model="m",
        prompt_version="v",
        extracted_at="2026-10-11T00:00:00+00:00",
        entry_ids=[],
        dropped_evidence=dropped,
        evidence_total=total,
        first_attempt_dropped=first[0] if first else None,
        first_attempt_total=first[1] if first else None,
    )


# 누적 기준: 최종 1%(10/1000), 재시도 전 기록은 없음 (M8 이전 기록)
HISTORY = [record(f"old{i}", 1, 100) for i in range(10)]


def test_small_run_is_not_judged():
    [final, first] = quality.check_run([record("new", 10, 40, (20, 40))], HISTORY)
    assert final.threshold is None and not final.spike
    assert first.threshold is None


def test_final_rate_uses_ratio_and_floor():
    # 기준 1%의 3배는 3%, 하한도 3%라 3% 이상이면 급등
    [normal, _] = quality.check_run([record("new", 2, 100)], HISTORY)
    [spike, _] = quality.check_run([record("new", 3, 100)], HISTORY)
    assert normal.threshold == spike.threshold == quality.FINAL_FLOOR
    assert not normal.spike and spike.spike

    # 기준값이 높으면 3배가 판단 기준이 된다
    noisy = [record(f"old{i}", 2, 100) for i in range(10)]
    [check, _] = quality.check_run([record("new", 5, 100)], noisy)
    assert abs(check.threshold - 0.06) < 1e-9 and not check.spike


def test_first_attempt_without_history_uses_floor_only():
    [_, first] = quality.check_run([record("new", 0, 100, (10, 100))], HISTORY)
    assert first.baseline.total == 0
    assert first.threshold == quality.FIRST_ATTEMPT_FLOOR and first.spike


def test_reextracted_post_is_excluded_from_baseline():
    history = [*HISTORY, record("same", 50, 100)]
    [final, _] = quality.check_run([record("same", 0, 100)], history)
    assert final.baseline == quality.Rate(10, 1000)
