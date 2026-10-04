from conftest import SAMPLE_ENTRIES, ev, make_entry

from pipeline import expand
from pipeline.build_index import build
from techblog_mcp import db
from techblog_mcp.search import query as q


class FakeLLM:
    model = "fake-model"

    def __init__(self):
        self.inputs: list[str] = []

    def parse(self, instructions, messages, schema, usage, step):
        self.inputs.append(messages[0]["content"])
        usage.calls += 1
        return schema(queries=["사내 접근 제어"], terms=["제로트러스트", "ZTNA"])


def test_expansion_input_uses_summaries_not_evidence():
    entry = make_entry(
        "case_0001",
        post_title="제목",
        problem_situation=[ev("문제 요약", "원문 발췌")],
        solution=[ev("해결 요약", "원문 발췌")],
        technologies=["Redis"],
    )
    text = expand.expansion_input(entry)
    assert text == "제목\n문제: 문제 요약\n해결: 해결 요약\n기술: Redis"


def test_run_creates_only_outdated_and_drops_removed(tmp_path):
    a = make_entry("case_0001", solution=[ev("해결 A")])
    b = make_entry("case_0002", solution=[ev("해결 B")])
    llm = FakeLLM()
    records: dict[str, expand.ExpansionRecord] = {}
    usage = expand.run([a, b], records, llm)
    assert (usage.calls, sorted(records)) == (2, ["case_0001", "case_0002"])

    path = tmp_path / "expansions.jsonl"
    expand.save(records, path)
    records = expand.load(path)
    assert records["case_0001"].terms == ["제로트러스트", "ZTNA"]

    # 내용이 바뀐 항목만 다시 만들고, 사라진 항목의 확장은 지운다
    changed = a.model_copy(update={"solution": [ev("해결 A 수정")]})
    llm.inputs.clear()
    expand.run([changed], records, llm)
    assert len(llm.inputs) == 1 and "해결 A 수정" in llm.inputs[0]
    assert list(records) == ["case_0001"]


def test_prompt_change_marks_outdated(monkeypatch):
    entry = make_entry("case_0001", solution=[ev("해결")])
    records: dict[str, expand.ExpansionRecord] = {}
    expand.run([entry], records, FakeLLM())
    assert expand.outdated([entry], records) == []
    monkeypatch.setattr(expand, "INSTRUCTIONS", expand.INSTRUCTIONS + "추가 지시")
    assert expand.outdated([entry], records) == [entry]


def test_expansion_is_indexed_and_searchable(tmp_path):
    path = tmp_path / "expanded.sqlite"
    texts = {"case_0004": "사내 접근 제어\n제로트러스트 ZTNA"}
    build(SAMPLE_ENTRIES, path, texts)
    conn = db.connect(path)
    try:
        # 본문에 없는 표현도 확장 열로 찾는다
        result = q.search(conn, "제로트러스트 접근 제어", q.Filters())
        assert [e["id"] for e in result.entries] == ["case_0004"]
    finally:
        conn.close()
