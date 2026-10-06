"""M7 사람 검증: 답변 비교 쌍 일부를 사람이 조건을 모른 채 판정하고 LLM 채점기와 대조한다.

    uv run python eval/agent_human.py sample     # 표본을 뽑고 검증 화면(review.html)을 만든다
    uv run python eval/agent_human.py compare    # 사람 판정(answers.json)과 LLM 판정을 대조한다

표본은 LLM 판정 결과를 보기 전에 고정 시드로 뽑는다. 비교 종류(mcp 대 none·web·web-ask)를 고르게
나누고, 같은 과제가 몰리지 않게 한다. 화면에는 답변 A·B만 보이고, 어느 쪽이 어떤 조건인지는
sample.json에만 둔다. 화면에서 고른 결과를 내려받아 eval/agent/human/answers.json으로 저장한다.
"""

import argparse
import json
import random
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:  # 스크립트로 실행할 때도 eval 모듈을 import할 수 있게 한다
    sys.path.insert(0, str(ROOT))

from eval.agent_judge import (  # noqa: E402
    COMPARISONS,
    JUDGE_FILE,
    Pair,
    build_pairs,
    load_judgements,
    pair_result,  # noqa: E402
)
from eval.agent_run import RUNS_DIR, RunRecord  # noqa: E402
from eval.agent_tasks import load_tasks  # noqa: E402

HUMAN_DIR = ROOT / "eval" / "agent" / "human"
TEMPLATE = (
    ROOT / "eval" / "agent" / "human_review.html"
)  # 검증 화면 틀. __DATA__ 자리에 항목을 넣는다
SAMPLE_SIZE = 21  # 비교 종류 3개 × 7쌍
SEED = 20261006


def sample_pairs(pairs: list[Pair], size: int, seed: int) -> list[Pair]:
    """비교 종류마다 같은 수를 뽑되, 한 과제는 전체 표본에서 한 번만 쓴다."""
    rng = random.Random(seed)
    per_kind = size // len(COMPARISONS)
    by_kind = {right: [p for p in pairs if p.right.condition == right] for _, right in COMPARISONS}
    used_tasks: set[str] = set()
    chosen: list[Pair] = []
    for kind in by_kind.values():
        candidates = kind[:]
        rng.shuffle(candidates)
        picked = 0
        for pair in candidates:
            if picked == per_kind:
                break
            if pair.task.id in used_tasks:
                continue
            chosen.append(pair)
            used_tasks.add(pair.task.id)
            picked += 1
    rng.shuffle(chosen)
    return chosen


def build_sample(chosen: list[Pair], seed: int) -> list[dict]:
    """화면 항목과 정답 키. left_is_a가 True면 화면의 A가 mcp 답변이다."""
    rng = random.Random(seed + 1)
    items = []
    for i, pair in enumerate(chosen, 1):
        items.append(
            {
                "item": f"q{i:02d}",
                "pair": pair.key,
                "left_is_a": rng.random() < 0.5,
                "question": pair.task.prompt,
                "left": pair.left.answer,
                "right": pair.right.answer,
            }
        )
    return items


def page_items(items: list[dict]) -> list[dict]:
    """화면에 넣을 내용. 조건과 쌍 이름은 넣지 않는다."""
    view = []
    for it in items:
        a, b = (it["left"], it["right"]) if it["left_is_a"] else (it["right"], it["left"])
        view.append({"item": it["item"], "question": it["question"], "a": a, "b": b})
    return view


def render_page(view: list[dict]) -> str:
    data = json.dumps(view, ensure_ascii=False).replace("</", "<\\/")
    return TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", data)


def human_side(choice: str, left_is_a: bool) -> str:
    """사람이 고른 A/B/tie를 left(mcp)/right/tie로 바꾼다."""
    if choice == "tie":
        return "tie"
    return "left" if (choice == "A") == left_is_a else "right"


def compare(items: list[dict], answers: dict, judged: dict, pairs: dict[str, Pair]) -> list[str]:
    rows = []
    agree = Counter()
    for it in items:
        choice = answers.get(it["item"], {}).get("choice")
        if choice is None:
            continue
        human = human_side(choice, it["left_is_a"])
        records = [
            judged[(it["pair"], o)]
            for o in ("left_first", "right_first")
            if (it["pair"], o) in judged
        ]
        llm = (pair_result(records) or {}).get("overall")
        kind = f"mcp vs {pairs[it['pair']].right.condition}"
        agree["판정함"] += 1
        agree["일치"] += human == llm
        agree[f"사람 {human}"] += 1
        rows.append(f"{it['item']} {it['pair']:<32} {kind:<16} 사람 {human:<5} LLM {llm}")
    n = agree["판정함"]
    if n:
        rows.append(f"\n사람 판정 {n}쌍, LLM과 일치 {agree['일치']}쌍 ({agree['일치'] / n:.0%})")
        rows.append(
            f"사람: mcp 승 {agree['사람 left']} · 무 {agree['사람 tie']} · 패 {agree['사람 right']}"
        )
    return rows


def load_records(name: str) -> list[RunRecord]:
    path = RUNS_DIR / name / "records.jsonl"
    return [
        RunRecord.model_validate_json(x) for x in path.read_text(encoding="utf-8").splitlines() if x
    ]


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("command", choices=["sample", "compare"])
    parser.add_argument("--name", default="m7-sonnet")
    args = parser.parse_args()

    pairs = build_pairs(load_tasks(), load_records(args.name))
    sample_path = HUMAN_DIR / "sample.json"
    if args.command == "sample":
        if sample_path.exists():
            sys.exit(f"이미 표본이 있습니다: {sample_path} (다시 뽑으려면 지우고 실행)")
        items = build_sample(sample_pairs(pairs, SAMPLE_SIZE, SEED), SEED)
        HUMAN_DIR.mkdir(parents=True, exist_ok=True)
        key = {
            "seed": SEED,
            "items": [{k: it[k] for k in ("item", "pair", "left_is_a")} for it in items],
        }
        sample_path.write_text(
            json.dumps(key, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        (HUMAN_DIR / "review.html").write_text(render_page(page_items(items)), encoding="utf-8")
        kinds = Counter(p.split("__")[1] for p in (it["pair"] for it in items))
        print(f"표본 {len(items)}쌍 {dict(kinds)} → {HUMAN_DIR / 'review.html'}")
        return

    key = json.loads(sample_path.read_text(encoding="utf-8"))
    by_key = {p.key: p for p in pairs}
    items = [
        {**it, "question": by_key[it["pair"]].task.prompt}
        for it in key["items"]
        if it["pair"] in by_key
    ]
    answers = json.loads((HUMAN_DIR / "answers.json").read_text(encoding="utf-8"))
    judged = load_judgements(RUNS_DIR / args.name / JUDGE_FILE)
    print("\n".join(compare(items, answers, judged, by_key)))


if __name__ == "__main__":
    main()
