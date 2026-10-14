"""자동 갱신: 새 글만 수집 → 추출 → 문서 확장 → 항목 임베딩 → 검색 DB 빌드를 한 번에 실행한다.

    uv run python -m pipeline.update                 # 8곳 모두
    uv run python -m pipeline.update kakao toss      # 일부 블로그만
    uv run python -m pipeline.update --skip woowahan # 일부 블로그 빼고 (GitHub Actions)
    uv run python -m pipeline.update --dry-run       # 수집과 추출 대상 확인까지만 (LLM 호출 없음)
    uv run python -m pipeline.update --max-new 200   # 상한을 넘어 보류된 블로그를 확인한 뒤 풀 때

새 글 판단은 원문 캐시가 아니라 추출 기록(data/posts.jsonl) 기준이라 캐시가 없는 환경에서도
새 글만 받는다. 이미 추출한 글의 수정은 반영하지 않는다(필요하면 수집 --refresh 후 추출).
여러 번 실행해도 결과가 같다(멱등). 실패한 글은 기록을 남기지 않아 다음 실행에서 다시 시도한다.
한 블로그의 추출 대상이 상한(--max-new)을 넘으면 URL·ID 체계 변경 등으로 기존 글이 새 글로
보이는 경우일 수 있어 그 블로그는 추출하지 않고 보류한다 (docs/기획.md "자동 갱신").
발췌 검증에 실패한 내용은 data/quarantine.jsonl에 격리하고, 이번 실행의 발췌 탈락률이
급등하면 알린다(pipeline/extract/quality.py). 탈락한 내용은 이미 걸러졌으므로 배포는 막지 않는다.

블로그 형식이 바뀌어 수집기가 오류 없이 빈 결과를 내는 조용한 고장도 알린다.
- 목록: 이번 목록에서 본 기존 글이 추출 기록보다 크게 적으면 목록 파싱이 깨진 것으로 본다.
  새 글이 없는 것과 달리 형식 변경은 기존 글도 함께 안 보이게 한다.
- 본문: 새 글 본문이 너무 짧으면 본문 위치가 바뀌어 엉뚱한 요소를 가져온 것으로 보고 추출하지
  않고 보류한다. 그대로 추출하면 "제외"로 기록돼 다음 실행에서 다시 받지 않기 때문이다.

종료 코드: 0 정상, 2 일부 실패·보류·탈락률 급등·수집 이상(성공한 부분은 반영), 1 실행 불가.
OPENAI_API_KEY(추출·확장)와 VOYAGE_API_KEY(항목 임베딩, M10)는 환경 변수나 저장소 루트의
`.env`로 설정한다. 임베딩이 실패하면 그 항목은 의미 검색의 임베딩 후보에서만 빠지므로 빌드는
하고 일부 실패로 알린다(다음 실행에서 다시 만든다).
"""

import argparse
import os
import sys
from collections import Counter
from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

from pipeline import embed, expand
from pipeline.build_index import build
from pipeline.collect import COMPANY_NAMES, raw
from pipeline.collect.http import PoliteClient
from pipeline.collect.run import COLLECTORS, Collector, CollectReport, collect_sources
from pipeline.extract import prompt_version, quality
from pipeline.extract.extractor import LLM
from pipeline.extract.run import DEFAULT_MODEL, ExtractReport, extract_all, plan, usage_summary
from pipeline.extract.store import DATA_DIR, Store
from pipeline.extract.text import html_to_text
from techblog_mcp import db
from techblog_mcp.search import semantic

# 블로그별 한 번에 추출할 글 수 상한. 평소 8곳 합쳐 주 10편 안팎이다
DEFAULT_MAX_NEW = 30
WORKERS = 4
# 이번 목록에서 본 기존 글이 추출 기록의 이 비율보다 적으면 목록 형식 변경을 의심한다.
# 블로그가 글 몇 편을 지운 정도는 넘기고, 0편이나 첫 페이지만 보이는 고장은 잡는다
MIN_LISTED_RATIO = 0.9
# 본문 평문 길이 하한. 2023-09 이후 1,268편 중 300자 미만은 5편(모두 공지·행사로 제외)이고
# 추출된 글은 최소 1,201자였다. 본문 위치가 바뀌어 엉뚱한 요소를 가져오면 이보다 짧아진다
MIN_BODY_CHARS = 300

EXIT_OK = 0
EXIT_FATAL = 1
EXIT_PARTIAL = 2

MakeLLM = Callable[[str, str], LLM]  # (모델, 추론 강도) → LLM
MakeEmbedder = Callable[
    [], object
]  # 항목 임베딩 클라이언트 (semantic.VoyageClient처럼 embed를 가짐)


@dataclass
class Paths:
    raw_dir: Path = raw.RAW_DIR
    # posts.jsonl, entries.jsonl, expansions.jsonl, prompt_versions/
    data_dir: Path = DATA_DIR
    db: Path = db.DEFAULT_DB_PATH

    @property
    def expansions(self) -> Path:
        return self.data_dir / expand.EXPANSIONS_PATH.name

    @property
    def embeddings(self) -> Path:
        return self.data_dir / embed.EMBEDDINGS_PATH.name

    @property
    def prompt_versions(self) -> Path:
        return self.data_dir / prompt_version.SNAPSHOT_DIR.name


@dataclass
class UpdateReport:
    collect: CollectReport
    planned: dict[str, int] = field(default_factory=dict)  # 블로그 → 추출 대상 수
    held: dict[str, int] = field(default_factory=dict)  # 상한을 넘어 보류한 블로그 → 대상 수
    # 목록이 줄어든 블로그 → (목록에서 본 기존 글 수, 추출 기록 수)
    shrunk: dict[str, tuple[int, int]] = field(default_factory=dict)
    # 본문이 짧아 추출하지 않고 보류한 글과 평문 길이
    short: list[tuple[raw.RawPost, int]] = field(default_factory=list)
    extract: ExtractReport = field(default_factory=ExtractReport)
    expanded: int = 0  # 새로 만든 확장 수
    expand_error: str | None = None
    embedded: int = 0  # 새로 만든 항목 임베딩 수
    embed_error: str | None = None
    checks: list[quality.Check] = field(default_factory=list)  # 발췌 탈락률 판단
    entry_count: int | None = None  # 빌드한 DB의 항목 수. 빌드하지 않았으면 None

    @property
    def partial(self) -> bool:
        return bool(
            self.collect.failed
            or self.held
            or self.shrunk
            or self.short
            or self.extract.failures
            or self.expand_error
            or self.embed_error
            or self.spikes
        )

    @property
    def spikes(self) -> list[quality.Check]:
        return [c for c in self.checks if c.spike]

    @property
    def exit_code(self) -> int:
        return EXIT_PARTIAL if self.partial else EXIT_OK


def known_post_ids(store: Store) -> dict[str, set[str]]:
    """블로그 → 추출 기록이 있는 글의 post_id. 수집에서 다시 받지 않을 글이다."""
    known: dict[str, set[str]] = {}
    for record in store.posts.values():
        known.setdefault(record.source, set()).add(record.post_id)
    return known


def shrunk_listings(
    collect: CollectReport, known: Mapping[str, set[str]]
) -> dict[str, tuple[int, int]]:
    """목록에서 본 기존 글이 추출 기록의 `MIN_LISTED_RATIO`보다 적은 블로그."""
    return {
        source: (result.listed_known, len(known[source]))
        for source, result in collect.results.items()
        if known.get(source) and result.listed_known < MIN_LISTED_RATIO * len(known[source])
    }


def update(
    sources: list[str],
    client: PoliteClient,
    make_llm: MakeLLM,
    paths: Paths | None = None,
    max_new: int = DEFAULT_MAX_NEW,
    workers: int = WORKERS,
    dry_run: bool = False,
    collectors: Mapping[str, Collector] = COLLECTORS,
    make_embedder: MakeEmbedder | None = None,
) -> UpdateReport:
    """make_embedder가 없으면 항목 임베딩을 새로 만들지 않고 저장된 것만 색인에 넣는다."""
    paths = paths or Paths()
    store = Store.in_dir(paths.data_dir)

    print("== 수집")
    known = known_post_ids(store)
    report = UpdateReport(
        collect_sources(client, sources, paths.raw_dir, known=known, collectors=collectors)
    )
    report.shrunk = shrunk_listings(report.collect, known)
    for source, (listed, total) in report.shrunk.items():
        print(
            f"{source}: 목록에서 본 기존 글이 {listed}편으로 추출 기록 {total}편보다 크게 "
            "적습니다. 목록 형식이 바뀌지 않았는지 수집기를 확인하세요.",
            file=sys.stderr,
        )

    print("== 추출")
    current_version = prompt_version.version()
    posts = [p for s in sources for p in raw.load_all(s, paths.raw_dir)]
    todo = plan(posts, store, DEFAULT_MODEL, current_version)
    report.planned = dict(Counter(t.post.source for t in todo))
    report.held = {s: n for s, n in report.planned.items() if n > max_new}
    for source, n in report.held.items():
        print(
            f"{source}: 추출 대상 {n}편이 상한 {max_new}편을 넘어 보류합니다. "
            "URL·ID 체계가 바뀌지 않았는지 확인한 뒤 --max-new로 상한을 올려 실행하세요.",
            file=sys.stderr,
        )
    todo = [t for t in todo if t.post.source not in report.held]
    lengths = {t.post.url: len(html_to_text(t.post.content_html)) for t in todo}
    report.short = [
        (t.post, lengths[t.post.url]) for t in todo if lengths[t.post.url] < MIN_BODY_CHARS
    ]
    for post, n in report.short:
        # 캐시가 남으면 수집기를 고쳐도 다음 실행에서 다시 받지 않으므로 지운다
        raw.raw_path(post.source, post.post_id, paths.raw_dir).unlink(missing_ok=True)
        print(
            f"{post.source}/{post.post_id}: 본문이 {n}자로 {MIN_BODY_CHARS}자보다 짧아 보류합니다. "
            "본문 위치가 바뀌지 않았는지 수집기를 확인하세요. 실제로 짧은 글이면 "
            "pipeline.collect로 다시 받은 뒤 pipeline.extract로 직접 추출하세요.",
            file=sys.stderr,
        )
    todo = [t for t in todo if lengths[t.post.url] >= MIN_BODY_CHARS]
    for t in todo:
        print(f"  {t.post.source}/{t.post.post_id} ({t.reason}) {t.post.title}")
    print(f"추출 대상 {len(todo)}편")
    if dry_run:
        return report
    if todo:
        prompt_version.save_snapshot(paths.prompt_versions)
        llm = make_llm(DEFAULT_MODEL, "medium")
        previous = list(store.posts.values())
        report.extract = extract_all(todo, store, llm, current_version, workers, "update")
        print(f"추출 {report.extract.done}/{len(todo)}편. {usage_summary(report.extract.usage)}")
        report.checks = quality.check_run(report.extract.records, previous)
        for c in report.checks:
            print(c)

    print("== 문서 확장")
    records = expand.load(paths.expansions)
    expand_todo = expand.outdated(store.entries, records)
    print(f"확장을 새로 만들 항목 {len(expand_todo)}개")
    try:
        llm = make_llm(expand.DEFAULT_MODEL, expand.REASONING_EFFORT) if expand_todo else None
        expand.run(store.entries, records, llm)
        report.expanded = len(expand_todo)
    except Exception as e:  # 확장이 없어도 빌드는 한다. 다음 실행에서 다시 만든다
        report.expand_error = f"{type(e).__name__}: {e}"
        print(f"확장 실패: {report.expand_error}", file=sys.stderr)
    finally:
        expand.save(records, paths.expansions)

    print("== 항목 임베딩")
    stored = embed.load(paths.embeddings)
    embed_todo = embed.outdated(store.entries, stored)
    print(f"임베딩을 새로 만들 항목 {len(embed_todo)}개")
    if make_embedder is not None:
        try:  # 임베딩이 없어도 빌드는 한다. 그 항목은 BM25 후보로만 찾힌다
            client = make_embedder() if embed_todo else None
            report.embedded = embed.run(store.entries, stored, client)
        except Exception as e:
            report.embed_error = f"{type(e).__name__}: {e}"
            print(f"임베딩 실패: {report.embed_error}", file=sys.stderr)
        finally:
            embed.save(stored, paths.embeddings)

    print("== 검색 DB 빌드")
    texts = {i: expand.expansion_text(r) for i, r in records.items()}
    paths.db.parent.mkdir(parents=True, exist_ok=True)
    build(store.entries, paths.db, texts, embed.current(store.entries, stored))
    report.entry_count = len(store.entries)
    print(f"{report.entry_count}개 항목으로 {paths.db}를 만들었습니다.")
    return report


def summary(report: UpdateReport) -> str:
    """실행 요약 (마크다운). 터미널에 출력하고, 워크플로는 PR 본문과 알림 이슈에 쓴다."""
    problems = [
        *(f"수집 실패 {s}: {e}" for s, e in report.collect.source_failures.items()),
        *(
            f"수집 실패 {s} {url}: {reason}"
            for s, r in report.collect.results.items()
            for url, reason in r.failures
        ),
        *(f"보류 {s}: 추출 대상 {n}편이 상한 초과 (--max-new)" for s, n in report.held.items()),
        *(
            f"목록 감소 {s}: 목록에서 본 기존 글 {listed}편, 추출 기록 {total}편 "
            "(목록 형식 변경 의심)"
            for s, (listed, total) in report.shrunk.items()
        ),
        *(
            f"본문 짧음 {p.source} [{p.title}]({p.url}): {n}자, 추출 보류 (본문 위치 변경 의심)"
            for p, n in report.short
        ),
        *(f"추출 실패 {p.source}/{p.post_id}: {e}" for p, e in report.extract.failures),
        *([f"확장 실패: {report.expand_error}"] if report.expand_error else []),
        *([f"임베딩 실패: {report.embed_error}"] if report.embed_error else []),
        *(f"발췌 탈락률 급등: {c} (격리분은 data/quarantine.jsonl)" for c in report.spikes),
    ]
    built = f"DB 항목 {report.entry_count}개" if report.entry_count is not None else "빌드 안 함"
    lines = [
        f"## 자동 갱신 결과: {'일부 실패·보류·이상' if report.partial else '정상'}",
        "",
        f"- 추출 {report.extract.done}편, 확장 {report.expanded}개,"
        f" 임베딩 {report.embedded}개, {built}",
        *(f"- {c}" for c in report.checks),
    ]
    if report.extract.records:
        lines += ["", "### 새로 반영한 글", ""]
        for r in sorted(report.extract.records, key=lambda r: (r.source, r.post_id)):
            result = f"항목 {len(r.entry_ids)}개" if r.kind == "추출" else "제외"
            lines.append(f"- {COMPANY_NAMES[r.source]} [{r.title}]({r.url}): {result}")
    if problems:
        lines += ["", "### 문제", "", *(f"- {p}" for p in problems)]
    return "\n".join(lines) + "\n"


def select_sources(requested: list[str], skip: list[str]) -> list[str]:
    """지정한 블로그(없거나 all이면 전체)에서 skip을 뺀다."""
    sources = sorted(COLLECTORS) if not requested or "all" in requested else requested
    return [s for s in sources if s not in skip]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="새 글만 수집·추출하고 문서 확장, 항목 임베딩, 검색 DB 빌드까지 실행한다."
    )
    parser.add_argument("sources", nargs="*", choices=["all", *sorted(COLLECTORS)])
    parser.add_argument(
        "--skip",
        action="append",
        default=[],
        choices=sorted(COLLECTORS),
        help="뺄 블로그 (여러 번 지정 가능, 워크플로는 우아한형제들을 뺀다)",
    )
    parser.add_argument(
        "--max-new",
        type=int,
        default=DEFAULT_MAX_NEW,
        help=f"블로그별 추출 대상 상한. 넘으면 그 블로그는 보류 (기본 {DEFAULT_MAX_NEW})",
    )
    parser.add_argument("--workers", type=int, default=WORKERS, help="동시에 추출할 글 수")
    parser.add_argument(
        "--dry-run", action="store_true", help="수집과 추출 대상 확인까지만 한다 (LLM 호출 없음)"
    )
    parser.add_argument("--summary-file", type=Path, help="실행 요약(마크다운)을 저장할 파일")
    args = parser.parse_args()
    sources = select_sources(args.sources, args.skip)

    load_dotenv()

    def make_llm(model: str, reasoning_effort: str) -> LLM:
        if not os.environ.get("OPENAI_API_KEY"):
            print("OPENAI_API_KEY가 없습니다. 환경 변수나 .env에 설정하세요.", file=sys.stderr)
            sys.exit(EXIT_FATAL)
        from pipeline.extract.extractor import OpenAILLM

        return OpenAILLM(model, reasoning_effort)

    def make_embedder() -> semantic.VoyageClient:
        key = os.environ.get(semantic.API_KEY_ENV, "").strip()
        if not key:
            raise RuntimeError(f"{semantic.API_KEY_ENV}가 없습니다. 환경 변수나 .env에 설정하세요.")
        # 문서 64개 묶음은 검색어 하나보다 오래 걸려 대기 시간을 넉넉히 둔다
        return semantic.VoyageClient(key, timeout=120)

    with PoliteClient() as client:
        report = update(
            sources,
            client,
            make_llm,
            None,
            args.max_new,
            args.workers,
            args.dry_run,
            make_embedder=make_embedder,
        )
    text = summary(report)
    print(text)
    if args.summary_file:
        args.summary_file.write_text(text, encoding="utf-8")
    sys.exit(report.exit_code)


if __name__ == "__main__":
    main()
