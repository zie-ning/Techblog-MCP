import pytest
from conftest import ev, make_entry

from pipeline.build_index import build, has_metrics
from techblog_mcp import db
from techblog_mcp.search import analyzer
from techblog_mcp.search import query as q


@pytest.fixture
def conn(sample_db):
    connection = db.connect(sample_db)
    yield connection
    connection.close()


def test_analyzer_keeps_content_morphemes():
    tokens = analyzer.tokenize("선착순 쿠폰 발급을 Redis로 해결했습니다")
    assert {"선착순", "쿠폰", "발급", "redis", "해결"} <= set(tokens)
    assert "을" not in tokens and "로" not in tokens


def test_analyzer_user_words_split_consistently():
    # 사용자 사전 단어는 문장 안에서도 단독으로 쓸 때와 같게 잘린다 (M5 E3)
    for word in ["동시성", "제로트러스트", "시그널링"]:
        assert analyzer.tokenize(word) == [word]
        assert word in analyzer.tokenize(f"사내 {word} 문제를 해결했다")


def ids(result: q.SearchResult) -> list[str]:
    return [e["id"] for e in result.entries]


def test_search_ranks_relevant_first(conn):
    result = q.search(conn, "선착순 쿠폰 동시성", q.Filters())
    assert ids(result)[0] == "case_0001"


def test_search_by_korean_alias_finds_english_name(conn):
    # "카프카"는 색인된 "Kafka"로도 찾는다
    result = q.search(conn, "카프카 정산", q.Filters())
    assert ids(result)[0] == "case_0003"


def test_search_filters(conn):
    assert ids(q.search(conn, "에이전트 완료 조건", q.Filters()))[0] == "case_0004"
    # 보조 문제 유형으로도 매칭
    assert ids(q.search(conn, "쿠폰", q.Filters(problem_type="트래픽 급증 대응"))) == ["case_0001"]
    assert ids(q.search(conn, "적재", q.Filters(domain="결제·금융"))) == ["case_0003"]
    # 기술 필터는 하나라도 쓴 항목
    tech = q.Filters(technologies=["RabbitMQ", "Kafka"])
    assert ids(q.search(conn, "쿠폰 발급", tech)) == ["case_0002"]
    assert ids(q.search(conn, "적재", tech)) == ["case_0003"]


def test_search_relevance_cutoff(conn):
    # case_0002는 흔한 단어 '쿠폰'만 맞고 주제를 정하는 '비관'·'락'이 없어 걸러진다
    result = q.search(conn, "쿠폰 비관 락", q.Filters())
    assert (ids(result), result.total) == (["case_0001"], 1)
    # DB에 없는 주제는 0건
    assert q.search(conn, "블록체인 가스비", q.Filters()).entries == []


def test_search_caps_results(conn, monkeypatch):
    monkeypatch.setattr(q, "MAX_RESULTS", 1)
    result = q.search(conn, "쿠폰 발급", q.Filters())
    assert len(result.entries) == 1
    assert result.total == 2  # 기준을 넘은 건수는 그대로 알려 준다


def test_search_without_tokens_falls_back_to_filters(conn):
    result = q.search(conn, "!!!", q.Filters(domain="LLM·AI"))
    assert ids(result) == ["case_0004"]
    # 두 번째 도메인으로도 찾는다
    assert ids(q.search(conn, "!!!", q.Filters(domain="사내 플랫폼·개발 도구"))) == ["case_0004"]


def test_resolve_technologies():
    resolution = q.resolve_technologies(["카프카", "Kafka", "Kafak", " "])
    assert resolution.normalized == ["Kafka"]
    assert list(resolution.unknown) == ["Kafak"]
    assert "Kafka" in resolution.unknown["Kafak"]


def test_get_details_with_siblings(conn):
    details, missing = q.get_details(conn, ["case_0001", "case_9999"])
    assert missing == ["case_9999"]
    assert details[0].entry["id"] == "case_0001"
    assert details[0].siblings == ["case_0002"]


def test_aggregate_by_technology(conn):
    result = q.aggregate(conn, "technology", q.Filters(), 10)
    assert (result.total, result.with_metrics, result.companies) == (4, 1, 2)
    groups = {g.key: g for g in result.groups}
    assert groups["Kafka"].companies == ["토스"]
    assert (groups["Redis"].total, groups["Redis"].with_metrics) == (1, 1)
    assert (groups["Claude Code"].total, groups["Claude Code"].with_metrics) == (1, 0)


def test_aggregate_technology_merges_families(tmp_path):
    entries = [
        make_entry("case_0001", technologies=["Kafka"]),
        make_entry("case_0002", technologies=["Amazon MSK"]),
        # 같은 계열을 두 개 써도 계열로는 한 번만 센다
        make_entry("case_0003", technologies=["Kafka", "Amazon MSK", "Kafka Connect"]),
        make_entry("case_0004", technologies=["Redis"]),
    ]
    path = tmp_path / "families.sqlite"
    build(entries, path)
    conn = db.connect(path)
    try:
        result = q.aggregate(conn, "technology", q.Filters(), 10)
    finally:
        conn.close()
    groups = {g.key: g for g in result.groups}
    assert set(groups) == {"Kafka", "Redis"}
    assert groups["Kafka"].total == 3
    assert groups["Kafka"].members == {"Amazon MSK": 2, "Kafka Connect": 1}
    assert groups["Redis"].members == {}


def test_has_metrics_requires_a_number():
    assert has_metrics(make_entry("a", performance_ops=[ev("첫 화면이 47초에서 1.3초로 줄었다")]))
    assert not has_metrics(make_entry("a", performance_ops=[ev("같은 질문의 반복이 줄었다")]))
    assert not has_metrics(make_entry("a"))


def test_aggregate_counts_every_problem_type_and_domain(conn):
    # 다중 선택: 한 항목이 여러 그룹에 들어가므로 건수의 합이 전체보다 클 수 있다
    result = q.aggregate(conn, "problem_type", q.Filters(), 10)
    groups = {g.key: g.total for g in result.groups}
    assert groups["동시성·락"] == 1 and groups["트래픽 급증 대응"] == 1
    assert result.total == 4 and sum(groups.values()) == 5

    domains = {g.key: g.total for g in q.aggregate(conn, "domain", q.Filters(), 10).groups}
    assert domains["LLM·AI"] == 1 and domains["사내 플랫폼·개발 도구"] == 1


def test_aggregate_rejected_alternatives_only_cases_with_them(conn):
    result = q.aggregate(conn, "rejected_alternative", q.Filters(), 10)
    # 설계 방식 대안(DB 비관적 락)은 세지 않고 기술 대안이 있는 항목만 모수로 센다
    assert result.total == 1
    assert {g.key for g in result.groups} == {"Kafka"}


def test_aggregate_top_n_and_examples(conn):
    result = q.aggregate(conn, "company", q.Filters(), 1)
    assert result.group_count == 2
    [top] = result.groups
    assert top.key == "올리브영" and top.total == 3
    assert len(top.examples) == q.EXAMPLES_PER_GROUP


def test_filter_terms_in_query_do_not_inflate_relevance(tmp_path):
    # 필터 이름을 되풀이한 검색어 단위는 후보마다 자동으로 맞으므로 관련도 기준에서 뺀다 (M6)
    surge = ["트래픽 급증 대응"]
    entries = [
        make_entry(
            "case_0001",
            problem_types=surge,
            solution=[ev("주문서 진입 요청을 대기열로 순차 처리")],
        ),
        make_entry(
            "case_0002",
            problem_types=surge,
            problem_situation=[ev("세일 기간 계산대 대기 이탈 증가")],
            solution=[ev("셀프계산대 도입")],
        ),
        *[make_entry(f"case_01{i:02d}", solution=[ev(f"무관한 해결 {i}")]) for i in range(6)],
    ]
    path = tmp_path / "filter.sqlite"
    build(entries, path)
    conn = db.connect(path)
    try:
        filters = q.Filters(problem_type="트래픽 급증 대응")
        result = q.search(conn, "트래픽 급증 대기열", filters)
        assert ids(result) == ["case_0001"]
        # 검색어가 필터 이름뿐이면 원래 단위로 잰다 (결과를 비우지 않음)
        assert q.search(conn, "트래픽 급증", filters).total == 2
    finally:
        conn.close()


def test_connect_missing_db(tmp_path):
    with pytest.raises(db.DatabaseNotFound):
        db.connect(tmp_path / "none.sqlite")
