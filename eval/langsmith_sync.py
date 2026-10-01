"""LangSmith Dataset·Experiment 등록.

    uv run python eval/langsmith_sync.py dataset          # 파일럿 80편 Dataset 생성·보충
    uv run python eval/langsmith_sync.py dataset --gold   # 정답셋 24편 Dataset 생성·갱신
    uv run python eval/langsmith_sync.py experiment eval/runs/baseline-gpt-5-mini-medium
    uv run python eval/langsmith_sync.py experiment eval/runs/v3-gpt-5-mini-medium --gold

- dataset: `eval/pilot_posts.txt`의 글을 Dataset `techblog-pilot-80`으로 올린다.
  입력은 글 식별 정보와 평문 원문이다(비공개 워크스페이스, docs/기획.md "원문 정책").
  이미 있는 글은 건너뛴다. `--gold`면 정답셋 글을 `techblog-gold-24`로 올리고 정답을
  reference output으로 넣는다. 정답이 바뀐 글은 reference output을 갱신한다.
- experiment: 이미 추출한 run 디렉터리를 LLM 재호출 없이 Experiment로 등록한다.
  target은 run 파일에서 그 글의 결과를 읽어 돌려주고, 정답셋 없이 볼 수 있는 점검 지표를 단다.
  `--gold`면 정답셋 Dataset에 등록하고 extract_eval.py의 정답 비교 지표를 단다.
  LLM 채점 점수는 run의 judge.jsonl 캐시에서 읽는다(judge.py를 먼저 실행).
  기준 데이터는 저장소의 run 파일이고 LangSmith는 비교·검수 화면이다(트레이스 보존 14일).
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 pipeline을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv  # noqa: E402

from eval.compare_runs import Run  # noqa: E402
from eval.extract_eval import PostEval, evaluate_run, kind_ok, technology_counts  # noqa: E402
from eval.gold import GoldPost, load_gold  # noqa: E402
from eval.inspect_run import SHORT_TEXT, cost, load_pricing  # noqa: E402
from eval.judge import load_judgements  # noqa: E402
from pipeline.collect import raw  # noqa: E402
from pipeline.extract.__main__ import parse_post_ids  # noqa: E402
from pipeline.extract.schema import PostRecord, Usage  # noqa: E402
from pipeline.extract.store import Store  # noqa: E402
from pipeline.extract.text import html_to_text  # noqa: E402
from pipeline.normalize import renormalize  # noqa: E402

PILOT_POSTS = ROOT / "eval" / "pilot_posts.txt"
PILOT_DATASET = "techblog-pilot-80"
GOLD_DATASET = "techblog-gold-24"


def post_example(source: str, post_id: str) -> dict:
    """Dataset 예시: 입력은 글 식별 정보와 평문, 메타데이터는 필터용."""
    post = raw.RawPost.from_json(raw.raw_path(source, post_id).read_text(encoding="utf-8"))
    text = html_to_text(post.content_html)
    return {
        "inputs": {
            "source": source,
            "post_id": post_id,
            "url": post.url,
            "title": post.title,
            "text": text,
        },
        "metadata": {"source": source, "text_length": len(text), "short": len(text) < SHORT_TEXT},
    }


def pilot_examples(path: Path = PILOT_POSTS) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [post_example(source, post_id) for source, post_id in parse_post_ids(lines, "all")]


def gold_reference(gold: GoldPost) -> dict:
    """정답을 reference output으로. 검수 여부는 화면에서 거를 수 있게 메타데이터에도 넣는다."""
    return gold.model_dump(exclude={"source", "post_id", "url", "title"})


def gold_examples(golds: dict[tuple[str, str], GoldPost]) -> list[dict]:
    examples = []
    for (source, post_id), gold in sorted(golds.items()):
        example = post_example(source, post_id)
        example["outputs"] = gold_reference(gold)
        example["metadata"] |= {"gold_kind": gold.kind, "reviewed": gold.reviewed}
        examples.append(example)
    return examples


def run_output(record: PostRecord | None, entries: list, price: dict | None) -> dict:
    """run 파일에 저장된 글 한 편의 결과를 Experiment 출력 형태로 만든다."""
    if record is None:
        return {"missing": True}
    return {
        "kind": record.kind,
        "post_type": record.post_type,
        "reason": record.reason,
        "evidence_total": record.evidence_total,
        "dropped_evidences": record.dropped_evidences,
        "usage": record.usage.model_dump(),
        "cost_usd": cost(record.usage, price) if price else None,
        "unregistered_technologies": sorted({n for e in entries for n in renormalize(e)[1]}),
        "entries": [e.model_dump() for e in entries],
    }


def post_checks(inputs: dict, outputs: dict) -> dict:
    """정답셋 없이 볼 수 있는 글 단위 점검 지표 (LangSmith evaluator)."""
    if outputs.get("missing"):
        return {"results": [{"key": "missing", "score": 1}]}
    total = outputs["evidence_total"]
    dropped = len(outputs["dropped_evidences"])
    extracted = outputs["kind"] != "제외"
    short = len(inputs.get("text", "")) < SHORT_TEXT
    results = [
        {"key": "excluded", "score": int(not extracted)},
        {"key": "entries", "score": len(outputs["entries"])},
        # 발췌가 없으면(제외 글) 존재율을 매기지 않는다
        {"key": "evidence_rate", "score": (total - dropped) / total if total else None},
        {"key": "unregistered_technologies", "score": len(outputs["unregistered_technologies"])},
        # 짧은 글에서 항목을 만든 경우: 목차·요약만으로 지어냈는지 확인할 대상
        {"key": "short_post_extracted", "score": int(short and extracted)},
    ]
    if outputs.get("cost_usd") is not None:
        results.append({"key": "cost_usd", "score": outputs["cost_usd"]})
    return {"results": results}


def gold_checks(evals: dict[tuple[str, str], PostEval]):
    """정답 비교 지표 evaluator. 계산은 extract_eval.py와 같고, 채점 점수는 judge.jsonl에서 온다."""

    def evaluator(inputs: dict, outputs: dict) -> dict:
        e = evals.get((inputs["source"], inputs["post_id"]))
        if e is None:
            return {"results": [{"key": "missing", "score": 1}]}
        results = [
            {"key": "kind_ok", "score": int(kind_ok(e.gold, e.record))},
            {"key": "kind_exact", "score": int(e.record.kind == e.gold.kind)},
            {"key": "post_type_ok", "score": int(e.record.post_type == e.gold.post_type)},
            {"key": "entry_count_diff", "score": len(e.entries) - len(e.gold.entries)},
        ]
        if e.both_extracted:
            tech = technology_counts(e.gold, e.entries)
            results += [
                {"key": "tech_precision", "score": tech.precision()},
                {"key": "tech_recall", "score": tech.recall()},
            ]
        if e.judged:
            mean = lambda xs: sum(xs) / len(xs) if xs else None  # noqa: E731
            results += [
                {"key": "completeness", "score": e.completeness},
                {"key": "faithfulness", "score": mean(e.faithfulness)},
                {"key": "card_summary", "score": mean(e.card_summary)},
                {"key": "split", "score": e.split_score},
                {"key": "problem_type_ok", "score": e.type_hits / e.pairs if e.pairs else None},
                {"key": "domain_ok", "score": e.domain_hits / e.pairs if e.pairs else None},
                {"key": "rejected_precision", "score": e.rejected.precision()},
                {"key": "rejected_recall", "score": e.rejected.recall()},
                {
                    "key": "unsupported_claims",
                    "score": len(e.unsupported_claims),
                    "comment": "\n".join(e.unsupported_claims) or None,
                },
            ]
        return {"results": [r for r in results if r["score"] is not None]}

    return evaluator


def sync_gold_dataset(client, name: str = GOLD_DATASET) -> None:
    """정답셋 Dataset을 만들거나, 있으면 새 글은 추가하고 정답이 바뀐 글은 갱신한다."""
    examples = gold_examples(load_gold())
    if not client.has_dataset(dataset_name=name):
        dataset = client.create_dataset(
            name, description="M3 추출 정답셋 (블로그당 3편, eval/gold/). 출력이 정답"
        )
        client.create_examples(dataset_id=dataset.id, examples=examples)
        print(f"Dataset {name}: {len(examples)}편 생성")
        return
    dataset = client.read_dataset(dataset_name=name)
    have = {
        (e.inputs["source"], e.inputs["post_id"]): e
        for e in client.list_examples(dataset_id=dataset.id)
    }
    new, updated = [], 0
    for ex in examples:
        current = have.get((ex["inputs"]["source"], ex["inputs"]["post_id"]))
        if current is None:
            new.append(ex)
        elif current.outputs != ex["outputs"] or current.metadata != ex["metadata"]:
            client.update_example(current.id, outputs=ex["outputs"], metadata=ex["metadata"])
            updated += 1
    if new:
        client.create_examples(dataset_id=dataset.id, examples=new)
    print(f"Dataset {name}: {len(new)}편 추가, {updated}편 갱신")


def sync_dataset(client, name: str = PILOT_DATASET) -> None:
    examples = pilot_examples()
    if client.has_dataset(dataset_name=name):
        dataset = client.read_dataset(dataset_name=name)
        have = {
            (e.inputs["source"], e.inputs["post_id"])
            for e in client.list_examples(dataset_id=dataset.id)
        }
        examples = [
            e for e in examples if (e["inputs"]["source"], e["inputs"]["post_id"]) not in have
        ]
    else:
        dataset = client.create_dataset(
            name, description="M3 파일럿 80편 (블로그당 10편, eval/pilot_posts.txt)"
        )
    if examples:
        client.create_examples(dataset_id=dataset.id, examples=examples)
    print(f"Dataset {name}: {len(examples)}편 추가")


def register_experiment(client, run_dir: Path, gold: bool = False) -> None:
    from langsmith import evaluate

    store = Store.in_dir(run_dir)
    by_key = {(p.source, p.post_id): p for p in store.posts.values()}
    entries_by_url: dict[str, list] = {}
    for e in store.entries:
        entries_by_url.setdefault(e.post_url, []).append(e)
    records = list(store.posts.values())
    model = records[0].model if records else ""
    price = load_pricing().get(model)

    def target(inputs: dict) -> dict:
        record = by_key.get((inputs["source"], inputs["post_id"]))
        entries = entries_by_url.get(record.url, []) if record else []
        return run_output(record, entries, price)

    usage = Usage()
    for r in records:
        usage.add(r.usage)
    evaluators = [post_checks]
    name = PILOT_DATASET
    if gold:
        name = GOLD_DATASET
        evals = evaluate_run(Run.load(run_dir), load_gold(), load_judgements(run_dir))
        evaluators.append(gold_checks({(e.gold.source, e.gold.post_id): e for e in evals}))
        print(f"채점 결과가 최신인 글: {sum(e.judged for e in evals)} / {len(evals)}")
    evaluate(
        target,
        data=name,
        evaluators=evaluators,
        experiment_prefix=run_dir.name,
        description=f"{run_dir.as_posix()}의 저장된 추출 결과 (LLM 재호출 없음)",
        metadata={
            "run": run_dir.name,
            "model": model,
            "reasoning_effort": records[0].reasoning_effort if records else "",
            "prompt_version": ", ".join(sorted({r.prompt_version for r in records})),
            "total_cost_usd": round(cost(usage, price), 4) if price else None,
        },
        max_concurrency=4,
        client=client,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="LangSmith Dataset·Experiment 등록")
    sub = parser.add_subparsers(dest="command", required=True)
    ds = sub.add_parser("dataset", help="파일럿 80편 Dataset 생성·보충")
    ds.add_argument("--gold", action="store_true", help="정답셋 24편 Dataset")
    exp = sub.add_parser("experiment", help="추출 run을 Experiment로 등록")
    exp.add_argument("run_dir", type=Path)
    exp.add_argument("--gold", action="store_true", help="정답셋 Dataset에 정답 비교 지표로 등록")
    args = parser.parse_args()

    load_dotenv(ROOT / ".env")
    from langsmith import Client

    client = Client()
    if args.command == "dataset":
        sync_gold_dataset(client) if args.gold else sync_dataset(client)
    else:
        register_experiment(client, args.run_dir, gold=args.gold)


if __name__ == "__main__":
    main()
