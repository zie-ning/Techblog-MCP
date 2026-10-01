from conftest import ev, make_entry
from test_eval_inspect import PRICE, _record

from eval.langsmith_sync import post_checks, run_output
from pipeline.extract.schema import Usage


def _scores(result: dict) -> dict:
    return {r["key"]: r["score"] for r in result["results"]}


def test_run_output_and_checks_for_case():
    record = _record("1", "추출", "https://e/1", dropped_evidence=1, dropped_evidences=["x"])
    entry = make_entry(
        "case_0001",
        post_url="https://e/1",
        technologies_raw=["Kafka", "kafkaTemplate"],
        problem_situation=[ev("문제")],
        solution=[ev("해결")],
    )
    out = run_output(record, [entry], PRICE)
    assert out["unregistered_technologies"] == ["kafkaTemplate"]
    assert out["cost_usd"] > 0

    scores = _scores(post_checks({"text": "가" * 3000}, out))
    assert scores["evidence_rate"] == 0.75  # 발췌 4개 중 1개 탈락
    assert scores["entries"] == 1
    assert scores["excluded"] == 0
    assert scores["short_post_extracted"] == 0
    assert scores["unregistered_technologies"] == 1


def test_checks_for_short_excluded_and_missing():
    record = _record("2", "제외", "https://e/2", evidence_total=0, usage=Usage())
    scores = _scores(post_checks({"text": "짧은 글"}, run_output(record, [], None)))
    assert scores["excluded"] == 1
    assert scores["evidence_rate"] is None
    assert scores["short_post_extracted"] == 0
    assert "cost_usd" not in scores

    assert _scores(post_checks({}, run_output(None, [], None))) == {"missing": 1}


def test_gold_checks_reports_judge_scores_only_when_judged():
    from test_eval_judge import _entries, _gold, _judge_record, _output

    from eval.extract_eval import evaluate_post
    from eval.langsmith_sync import gold_checks, gold_reference

    gold, entries = _gold(), _entries()
    record = _record("1", "추출", "https://e/1")
    inputs = {"source": "kakao", "post_id": "1"}

    unjudged = gold_checks({("kakao", "1"): evaluate_post(gold, record, entries, None)})
    scores = _scores(unjudged(inputs, {}))
    assert scores["kind_ok"] == 1 and scores["entry_count_diff"] == 0
    assert scores["tech_recall"] == 2 / 3
    assert "completeness" not in scores

    judged = evaluate_post(gold, record, entries, _judge_record(gold, entries, _output()))
    scores = _scores(gold_checks({("kakao", "1"): judged})(inputs, {}))
    assert scores["completeness"] == 1.5 / 3
    assert scores["faithfulness"] == 5
    assert scores["unsupported_claims"] == 1
    assert gold_checks({})(inputs, {}) == {"results": [{"key": "missing", "score": 1}]}

    assert "source" not in gold_reference(gold) and gold_reference(gold)["kind"] == "추출"
