from datetime import UTC, datetime

import httpx
import numpy as np
import pytest

from pipeline import expand, update
from pipeline.collect import raw
from pipeline.collect.common import save_feed_posts
from pipeline.extract import quality
from pipeline.extract.schema import Classification, EntryDraft, Extraction, Point
from pipeline.extract.store import Store
from techblog_mcp import db
from techblog_mcp.search import semantic

EVIDENCE = "Redis의 원자 연산으로 발급 수량을 관리했습니다."
# 본문 길이 하한(update.MIN_BODY_CHARS)을 넘기기 위한 문단
FILLER = "<p>" + "선착순 쿠폰 발급 과정을 정리했습니다. " * 20 + "</p>"


def make_post(source: str, post_id: str) -> raw.RawPost:
    return raw.RawPost(
        source=source,
        post_id=post_id,
        url=f"https://example.com/{source}/{post_id}",
        title=f"{post_id} 제목",
        published_at=datetime(2026, 10, 1, tzinfo=UTC),
        content_html=f"<p>{post_id} 문제가 있었습니다.</p><p>{EVIDENCE}</p>{FILLER}",
        collected_at=datetime(2026, 10, 2, tzinfo=UTC),
    )


class FakeBlog:
    """목록에 본문까지 들어 있는 블로그 대역. 받은 known을 기록한다."""

    def __init__(self, source: str, post_ids: list[str]):
        self.source = source
        self.posts = [make_post(source, i) for i in post_ids]
        self.error: Exception | None = None
        self.known_seen: set[str] = set()

    def collect(self, client, raw_dir, refresh=False, known=frozenset()):
        if self.error:
            raise self.error
        self.known_seen = set(known)
        return save_feed_posts(self.posts, raw_dir, refresh, known)


class FakeLLM:
    """분류·구조화·확장에 정해 둔 응답을 돌려준다. `fail_on`이 든 글은 구조화에서 실패한다."""

    model = "fake-model"
    reasoning_effort = "medium"

    def __init__(self, fail_on: str | None = None, made_up: bool = False):
        self.fail_on = fail_on
        self.made_up = made_up  # 원문에 없는 발췌를 섞는다
        self.steps: list[str] = []

    def parse(self, instructions, messages, schema, usage, step):
        self.steps.append(step)
        usage.calls += 1
        if schema is Classification:
            return Classification(post_type="문제 해결형", kind="추출", reason="문제 해결")
        if schema is Extraction:
            if self.fail_on and self.fail_on in messages[0]["content"]:
                raise RuntimeError("일시적 오류")
            draft = EntryDraft(
                problem_types=["동시성·락"],
                domains=["커머스·주문·재고"],
                technologies=["Redis"],
                tags=["쿠폰"],
                problem_situation=[],
                solution=[Point(text="Redis 원자 연산", evidence=EVIDENCE)],
                performance_ops=(
                    [Point(text="지어낸 수치", evidence="처리량이 10배 늘었습니다.")]
                    if self.made_up
                    else []
                ),
                rejected_alternatives=[],
            )
            return Extraction(entries=[draft])
        assert schema is expand.Expansion
        return expand.Expansion(queries=["선착순 쿠폰"], terms=["원자적 증가"])


@pytest.fixture
def paths(tmp_path):
    return update.Paths(
        raw_dir=tmp_path / "raw", data_dir=tmp_path / "data", db=tmp_path / "techblog.sqlite"
    )


def run(blogs: list[FakeBlog], llm: FakeLLM | None, paths, **kwargs) -> update.UpdateReport:
    def make_llm(model, effort):
        if llm is None:
            raise AssertionError("LLM을 호출하면 안 됩니다")
        return llm

    collectors = {b.source: b.collect for b in blogs}
    return update.update(
        [b.source for b in blogs],
        client=None,
        make_llm=make_llm,
        paths=paths,
        workers=1,
        collectors=collectors,
        **kwargs,
    )


def test_update_runs_all_steps_and_is_idempotent(paths):
    olive = FakeBlog("oliveyoung", ["a", "b"])
    toss = FakeBlog("toss", ["c"])
    toss.error = httpx.ConnectError("연결 실패")

    report = run([olive, toss], FakeLLM(), paths)
    # 한 블로그 수집이 실패해도 나머지는 반영하고 일부 실패로 끝낸다
    assert report.collect.source_failures.keys() == {"toss"}
    assert report.extract.done == 2
    assert report.expanded == 2
    assert report.entry_count == 2
    assert report.exit_code == update.EXIT_PARTIAL
    conn = db.connect(paths.db)
    assert conn.execute("SELECT count(*) FROM entries").fetchone()[0] == 2
    conn.close()

    # 원문 캐시가 없어도 추출 기록이 있는 글은 다시 받지 않고, LLM도 호출하지 않는다
    files = {p: p.read_bytes() for p in paths.data_dir.glob("*.jsonl")}
    raw_dir = paths.raw_dir
    for f in raw_dir.rglob("*.json"):
        f.unlink()
    toss.error = None
    toss.posts = []
    report = run([olive, toss], None, paths)
    assert olive.known_seen == {"a", "b"}
    assert report.collect.results["oliveyoung"].skipped == 2
    assert report.extract.done == 0
    assert report.exit_code == update.EXIT_OK
    assert {p: p.read_bytes() for p in paths.data_dir.glob("*.jsonl")} == files


def test_new_post_is_added_without_touching_existing(paths):
    olive = FakeBlog("oliveyoung", ["a"])
    run([olive], FakeLLM(), paths)
    olive.posts.append(make_post("oliveyoung", "b"))
    llm = FakeLLM()

    report = run([olive], llm, paths)
    assert report.planned == {"oliveyoung": 1}
    assert llm.steps == ["분류", "구조화", "expand"]
    store = Store.in_dir(paths.data_dir)
    assert [e.id for e in store.entries] == ["case_0001", "case_0002"]
    assert set(expand.load(paths.expansions)) == {"case_0001", "case_0002"}


def test_failed_post_is_retried_next_run(paths):
    olive = FakeBlog("oliveyoung", ["a", "broken"])
    report = run([olive], FakeLLM(fail_on="broken 제목"), paths)
    assert report.extract.done == 1
    assert [p.post_id for p, _ in report.extract.failures] == ["broken"]
    assert report.exit_code == update.EXIT_PARTIAL
    assert report.entry_count == 1

    # 실패한 글은 기록이 없어 다음 실행에서 다시 받고 추출한다
    report = run([olive], FakeLLM(), paths)
    assert olive.known_seen == {"a"}
    assert report.planned == {"oliveyoung": 1}
    assert report.exit_code == update.EXIT_OK
    assert report.entry_count == 2


def test_source_over_limit_is_held(paths):
    olive = FakeBlog("oliveyoung", ["a", "b", "c"])
    toss = FakeBlog("toss", ["d"])

    report = run([olive, toss], FakeLLM(), paths, max_new=2)
    assert report.held == {"oliveyoung": 3}
    assert report.extract.done == 1  # toss만 추출
    assert report.exit_code == update.EXIT_PARTIAL

    # 확인한 뒤 상한을 올리면 보류했던 글을 추출한다
    report = run([olive, toss], FakeLLM(), paths, max_new=10)
    assert report.held == {}
    assert report.extract.done == 3


def test_shrunk_listing_is_reported(paths):
    olive = FakeBlog("oliveyoung", ["a", "b"])
    run([olive], FakeLLM(), paths)

    # 새 글이 없어도 기존 글이 목록에 그대로 보이면 정상이다
    report = run([olive], None, paths)
    assert report.shrunk == {}
    assert report.exit_code == update.EXIT_OK

    # 목록 형식이 바뀌어 기존 글이 안 보이면 새 글 0편이어도 알린다
    olive.posts = olive.posts[:1]
    report = run([olive], None, paths)
    assert report.shrunk == {"oliveyoung": (1, 2)}
    assert report.exit_code == update.EXIT_PARTIAL
    assert "목록 감소 oliveyoung: 목록에서 본 기존 글 1편, 추출 기록 2편" in update.summary(report)


def test_short_body_is_held(paths):
    olive = FakeBlog("oliveyoung", ["a", "b"])
    olive.posts[1].content_html = "<p>관련 글</p>"

    report = run([olive], FakeLLM(), paths)
    assert [(p.post_id, n) for p, n in report.short] == [("b", 4)]
    assert report.extract.done == 1
    assert report.exit_code == update.EXIT_PARTIAL
    assert "본문 짧음 oliveyoung [b 제목]" in update.summary(report)
    # 캐시를 지워 다음 실행에서 원문을 다시 받게 한다
    assert not raw.exists("oliveyoung", "b", paths.raw_dir)
    assert raw.exists("oliveyoung", "a", paths.raw_dir)

    # 기록을 남기지 않아 수집기를 고친 뒤 다음 실행에서 추출한다
    olive.posts[1] = make_post("oliveyoung", "b")
    report = run([olive], FakeLLM(), paths)
    assert report.short == []
    assert report.extract.done == 1
    assert report.exit_code == update.EXIT_OK


def test_dry_run_does_not_call_llm_or_build(paths):
    olive = FakeBlog("oliveyoung", ["a"])
    report = run([olive], None, paths, dry_run=True)
    assert report.planned == {"oliveyoung": 1}
    assert report.entry_count is None
    assert not paths.db.exists()
    assert not (paths.data_dir / "posts.jsonl").exists()


def test_evidence_spike_is_reported_but_deployed(paths, monkeypatch):
    monkeypatch.setattr(quality, "MIN_EVIDENCE", 1)
    olive = FakeBlog("oliveyoung", ["a"])
    report = run([olive], FakeLLM(made_up=True), paths)

    # 지어낸 발췌는 걸러 격리하고, 급등을 알리되 DB는 만든다
    assert [c.spike for c in report.checks] == [True, True]
    assert report.exit_code == update.EXIT_PARTIAL
    assert report.entry_count == 1
    [q] = Store.in_dir(paths.data_dir).quarantine
    assert q.failed[0].evidence == "처리량이 10배 늘었습니다."


def test_summary_lists_new_posts_and_problems(paths):
    olive = FakeBlog("oliveyoung", ["a"])
    toss = FakeBlog("toss", [])
    toss.error = httpx.ConnectError("연결 실패")
    text = update.summary(run([olive, toss], FakeLLM(), paths))

    assert text.startswith("## 자동 갱신 결과: 일부 실패·보류·이상")
    assert "- 올리브영 [a 제목](https://example.com/oliveyoung/a): 항목 1개" in text
    assert "- 수집 실패 toss: ConnectError: 연결 실패" in text


def test_select_sources_skips_blogs():
    assert "woowahan" not in update.select_sources([], ["woowahan"])
    assert len(update.select_sources(["all"], ["woowahan"])) == 7
    assert update.select_sources(["kakao", "toss"], ["toss"]) == ["kakao"]


class FakeEmbedder:
    def __init__(self):
        self.texts: list[str] = []

    def embed(self, texts, input_type):
        self.texts += texts
        return np.ones((len(texts), 4), dtype=np.float32) / 2


def test_update_embeds_new_entries_for_semantic_search(paths):
    embedder = FakeEmbedder()
    blog = FakeBlog("oliveyoung", ["a", "b"])
    report = run([blog], FakeLLM(), paths, make_embedder=lambda: embedder)
    assert report.embedded == 2 and report.embed_error is None
    assert report.exit_code == update.EXIT_OK
    conn = db.connect(paths.db)
    assert semantic.load_vectors(conn).matrix.shape == (2, 4)
    conn.close()

    # 다시 실행하면 바뀐 항목이 없어 임베딩 클라이언트를 만들지 않는다
    def must_not_embed():
        raise AssertionError("임베딩을 다시 만들면 안 됩니다")

    report = run([FakeBlog("oliveyoung", ["a", "b"])], None, paths, make_embedder=must_not_embed)
    assert report.embedded == 0 and report.exit_code == update.EXIT_OK


def test_update_reports_embedding_failure_but_builds(paths):
    def no_key():
        raise RuntimeError("VOYAGE_API_KEY가 없습니다")

    report = run([FakeBlog("oliveyoung", ["a"])], FakeLLM(), paths, make_embedder=no_key)
    assert report.embed_error == "RuntimeError: VOYAGE_API_KEY가 없습니다"
    assert report.exit_code == update.EXIT_PARTIAL
    assert report.entry_count == 1  # 임베딩 없이도 빌드한다
    assert "임베딩 실패: RuntimeError: VOYAGE_API_KEY가 없습니다" in update.summary(report)
