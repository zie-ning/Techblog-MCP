from conftest import ev, make_entry
from test_eval_inspect import PRICE, _record

from eval.compare_runs import Run
from eval.extract_eval import (
    build_report,
    evaluate_post,
    evaluate_run,
    run_metrics,
    tech_key,
    technology_counts,
)
from eval.gold import GoldEntry, GoldPost, GoldRejected
from eval.judge import (
    EntryMatch,
    EntryScore,
    JudgeOutput,
    JudgeRecord,
    RejectedJudgement,
    input_hash,
    is_current,
    judge_post,
    load_judgements,
    prompt_version,
)
from pipeline.extract.schema import RejectedAlternative, Usage


class FakeJudge:
    model = "judge-model"
    reasoning_effort = "medium"

    def __init__(self, output: JudgeOutput):
        self.output = output
        self.messages = []

    def parse(self, instructions, messages, schema, usage, step):
        self.messages.append(messages)
        usage.add(Usage(calls=1, input_tokens=1000, output_tokens=100))
        return self.output


def _gold(kind: str = "추출", **overrides) -> GoldPost:
    entries = [
        GoldEntry(
            summary="쿠폰 초과 발급을 Redis 원자 연산으로 해결",
            problem_types=["동시성·락"],
            acceptable_problem_types=["트래픽 급증 대응"],
            domains=["커머스·주문·재고"],
            technologies=["Redis", "Spring Boot"],
            rejected_alternatives=[GoldRejected(name="DB 비관적 락", kind="설계 방식")],
            key_facts=["초당 3만 요청", "초과 발급 0건"],
        ),
        GoldEntry(
            summary="발급 이력을 Kafka로 비동기 적재",
            problem_types=["메시징·비동기 처리"],
            domains=["커머스·주문·재고"],
            technologies=["Kafka"],
            key_facts=["적재 지연 1초 이내"],
        ),
    ]
    base = dict(
        source="kakao",
        post_id="1",
        url="https://e/1",
        title="제목 1",
        post_type="문제 해결형",
        kind=kind,
        entries=entries if kind == "추출" else [],
        notes="",
    )
    base.update(overrides)
    return GoldPost(**base)


def _entries() -> list:
    return [
        make_entry(
            "case_0001",
            source="kakao",
            post_url="https://e/1",
            # 허용 답 하나와 정답에 없는 값 하나. 꼭 들어갈 값(동시성·락)은 빠짐
            problem_types=["트래픽 급증 대응", "캐싱"],
            technologies=["Redis"],
            technologies_raw=["redis", "spring-boot", "Lua"],
            problem_situation=[ev("초당 3만 요청에서 초과 발급")],
            solution=[ev("Redis 원자 연산")],
            rejected_alternatives=[
                RejectedAlternative(
                    name="DB 락", name_raw="DB 락", kind="설계 방식", reason="느림", evidence="e"
                ),
                RejectedAlternative(
                    name="Memcached", name_raw="Memcached", kind="기술", reason="?", evidence="e"
                ),
            ],
        ),
        make_entry(
            "case_0002",
            source="kakao",
            post_url="https://e/1",
            problem_types=["캐싱"],
            domains=["범용"],
            problem_situation=[ev("부가 문제")],
            solution=[ev("부가 해결")],
        ),
    ]


def _output() -> JudgeOutput:
    return JudgeOutput(
        matches=[
            EntryMatch(
                gold_index=1,
                extracted_ids=["case_0001"],
                key_facts_covered=[True, False],
                reason="",
            ),
            EntryMatch(gold_index=2, extracted_ids=[], key_facts_covered=[True], reason=""),
            EntryMatch(gold_index=9, extracted_ids=["case_0002"], key_facts_covered=[], reason=""),
        ],
        entries=[
            EntryScore(
                entry_id="case_0001",
                faithfulness=5,
                card_summary=4,
                unsupported_claims=[],
                reason="",
            ),
            EntryScore(
                entry_id="case_0002",
                faithfulness=7,  # 범위 밖 점수는 1~5로 자른다
                card_summary=2,
                unsupported_claims=["지어낸 수치"],
                reason="",
            ),
        ],
        rejected=[
            RejectedJudgement(
                entry_id="case_0001",
                name="DB 락",
                gold_name="DB 비관적 락",
                supported=True,
                reason="",
            ),
            RejectedJudgement(
                entry_id="case_0001", name="Memcached", gold_name="", supported=False, reason=""
            ),
        ],
        split_score=4,
        split_reason="",
    )


def _judge_record(gold: GoldPost, entries: list, output: JudgeOutput | None) -> JudgeRecord:
    return JudgeRecord(
        source=gold.source,
        post_id=gold.post_id,
        judge_model="judge-model",
        judge_effort="medium",
        judge_prompt_version=prompt_version(),
        input_hash=input_hash(gold, entries),
        output=output,
        usage=Usage(calls=1, input_tokens=1_000_000, output_tokens=100_000),
    )


def test_tech_key_uses_dictionary_and_ignores_separators():
    assert tech_key("spring-boot") == tech_key("Spring Boot")
    assert tech_key("레디스") == tech_key("Redis")
    assert tech_key("data-source proxy") == tech_key("datasource-proxy")  # 사전에 없는 이름


def test_technology_counts_compares_post_level_sets():
    counts = technology_counts(_gold(), _entries())
    # 예측 {redis, springboot, lua}, 정답 {redis, springboot, kafka}
    assert (counts.hit_pred, counts.pred, counts.hit_gold, counts.gold) == (2, 3, 2, 3)


def test_evaluate_post_uses_judge_matches():
    gold, entries = _gold(), _entries()
    result = evaluate_post(
        gold, _record("1", "추출", "https://e/1"), entries, _judge_record(gold, entries, _output())
    )
    assert result.judged
    # 정답 key_facts 3개 중 항목 1의 첫 사실만 담김. 대응 없는 항목 2는 true라도 세지 않는다
    assert result.completeness == 1 / 3
    # 범위 밖 정답 번호(9)는 무시하고, 대응 쌍은 (1, case_0001) 하나
    assert result.pairs == 1
    t, d = result.types, result.domains
    assert (t.hit_pred, t.pred, t.hit_gold, t.gold) == (1, 2, 0, 1)
    assert (d.hit_pred, d.pred, d.hit_gold, d.gold) == (1, 1, 1, 1)
    assert result.faithfulness == [5, 5]
    assert result.card_summary == [4, 2]
    assert result.split_score == 4
    assert result.unsupported_claims == ["case_0002: 지어낸 수치"]
    r = result.rejected
    assert (r.hit_pred, r.pred, r.hit_gold, r.gold) == (1, 2, 1, 1)
    assert (result.rejected_unmatched, result.rejected_unsupported) == (1, 1)


def test_missing_extraction_counts_as_zero_completeness():
    gold = _gold()
    result = evaluate_post(
        gold, _record("1", "제외", "https://e/1"), [], _judge_record(gold, [], None)
    )
    assert result.completeness == 0.0
    assert result.rejected.gold == 1


def test_judge_post_skips_llm_without_entries():
    gold = _gold()
    llm = FakeJudge(_output())
    record = judge_post(llm, "제목", "본문", gold, [], prompt_version())
    assert record.output is None and llm.messages == []

    record = judge_post(llm, "제목", "본문", gold, _entries(), prompt_version())
    assert record.output == _output()
    assert record.usage.calls == 1
    content = llm.messages[0][0]["content"]
    assert "본문" in content and "초당 3만 요청" in content and "case_0001" in content


def test_cache_is_invalidated_when_gold_changes(tmp_path):
    gold, entries = _gold(), _entries()
    record = _judge_record(gold, entries, _output())
    h = input_hash(gold, entries)
    assert is_current(record, "judge-model", "medium", prompt_version(), h)

    changed = _gold(entries=[gold.entries[0].model_copy(update={"key_facts": ["다른 사실"]})])
    assert not is_current(
        record, "judge-model", "medium", prompt_version(), input_hash(changed, entries)
    )
    assert not is_current(record, "other-model", "medium", prompt_version(), h)

    path = tmp_path / "judge.jsonl"
    newer = record.model_copy(update={"input_hash": "new"})
    path.write_text(record.model_dump_json() + "\n" + newer.model_dump_json() + "\n", "utf-8")
    assert load_judgements(tmp_path)[("kakao", "1")].input_hash == "new"


def test_evaluate_run_ignores_stale_judgements_and_builds_report():
    gold = _gold()
    entries = _entries()
    posts = [_record("1", "추출", "https://e/1"), _record("2", "제외", "https://e/2")]
    run = Run("r", posts, entries)
    golds = {("kakao", "1"): gold, ("kakao", "2"): _gold("제외", post_id="2", url="https://e/2")}

    stale = _judge_record(gold, entries, _output()).model_copy(update={"input_hash": "old"})
    evals = evaluate_run(run, golds, {("kakao", "1"): stale})
    assert [e.judged for e in evals] == [False, False]

    judgements = {("kakao", "1"): _judge_record(gold, entries, _output())}
    evals = evaluate_run(run, golds, judgements)
    metrics = run_metrics(run, evals, judgements, {"m": PRICE, "judge-model": PRICE})
    assert metrics["정답 글 / 채점된 글"] == "2 / 1"
    assert metrics["추출 여부 일치 (허용 답 포함)"] == "100% (2/2)"
    assert metrics["항목 수 차이 (추출 − 정답)"] == "+0: 1편"
    assert metrics["문제 유형 정밀도 / 재현율 (대응 쌍)"] == "50% / 0% (1/2, 0/1)"
    assert metrics["완결성 (key_facts 포함률, 글 평균)"] == "33%"
    assert metrics["채점 비용"] == "$2.00 (judge-model)"

    report = build_report(["r"], [metrics], [evals])
    assert "| kakao/1 | 추출 2개 | 추출 2개 · 완결 33% · 충실 5 |" in report
    assert "`kakao/1` case_0002: 지어낸 수치" in report
