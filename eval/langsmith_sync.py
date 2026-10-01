"""LangSmith Dataset·Experiment 등록.

    uv run python eval/langsmith_sync.py dataset   # 파일럿 80편 Dataset 생성·보충
    uv run python eval/langsmith_sync.py experiment eval/runs/baseline-gpt-5-mini-medium

- dataset: `eval/pilot_posts.txt`의 글을 Dataset `techblog-pilot-80`으로 올린다.
  입력은 글 식별 정보와 평문 원문이다(비공개 워크스페이스, docs/기획.md "원문 정책").
  이미 있는 글은 건너뛴다.
- experiment: 이미 추출한 run 디렉터리를 LLM 재호출 없이 Experiment로 등록한다.
  target은 run 파일에서 그 글의 결과를 읽어 돌려주고, 정답셋 없이 볼 수 있는 점검 지표를 단다.
  기준 데이터는 저장소의 run 파일이고 LangSmith는 비교·검수 화면이다(트레이스 보존 14일).
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 pipeline을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv  # noqa: E402

from eval.inspect_run import SHORT_TEXT, cost, load_pricing  # noqa: E402
from pipeline.collect import raw  # noqa: E402
from pipeline.extract.__main__ import parse_post_ids  # noqa: E402
from pipeline.extract.schema import PostRecord, Usage  # noqa: E402
from pipeline.extract.store import Store  # noqa: E402
from pipeline.extract.text import html_to_text  # noqa: E402
from pipeline.normalize import renormalize  # noqa: E402

PILOT_POSTS = ROOT / "eval" / "pilot_posts.txt"
PILOT_DATASET = "techblog-pilot-80"


def pilot_examples(path: Path = PILOT_POSTS) -> list[dict]:
    """Dataset 예시: 입력은 글 식별 정보와 평문, 메타데이터는 필터용."""
    lines = path.read_text(encoding="utf-8").splitlines()
    examples = []
    for source, post_id in parse_post_ids(lines, "all"):
        post = raw.RawPost.from_json(raw.raw_path(source, post_id).read_text(encoding="utf-8"))
        text = html_to_text(post.content_html)
        examples.append(
            {
                "inputs": {
                    "source": source,
                    "post_id": post_id,
                    "url": post.url,
                    "title": post.title,
                    "text": text,
                },
                "metadata": {
                    "source": source,
                    "text_length": len(text),
                    "short": len(text) < SHORT_TEXT,
                },
            }
        )
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
        {"key": "insight", "score": int(outputs["kind"] == "인사이트")},
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


def register_experiment(client, run_dir: Path, name: str = PILOT_DATASET) -> None:
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
    evaluate(
        target,
        data=name,
        evaluators=[post_checks],
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
    sub.add_parser("dataset", help="파일럿 80편 Dataset 생성·보충")
    exp = sub.add_parser("experiment", help="추출 run을 Experiment로 등록")
    exp.add_argument("run_dir", type=Path)
    args = parser.parse_args()

    load_dotenv(ROOT / ".env")
    from langsmith import Client

    client = Client()
    if args.command == "dataset":
        sync_dataset(client)
    else:
        register_experiment(client, args.run_dir)


if __name__ == "__main__":
    main()
