"""검색 DB 스키마. 색인 빌드(pipeline/build_index.py)가 만들고 서버가 읽는다."""

SCHEMA_VERSION = "4"

# FTS5 열과 bm25() 가중치. 순서가 곧 bm25() 인자 순서다. 가중치는 M5 검색 평가에서 조정한다.
FTS_COLUMNS: dict[str, float] = {
    "title": 1.5,  # 원문 제목
    "problem": 3.0,  # 문제 상황
    "solution": 2.0,  # 해결 방법
    "ops": 1.0,  # 성능·운영 포인트
    "rejected": 1.0,  # 버린 대안과 이유
    "keywords": 2.0,  # 기술, 태그, 회사, 분류 이름
}

DDL = f"""
CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);

CREATE TABLE entries (
    rowid INTEGER PRIMARY KEY,
    id TEXT NOT NULL UNIQUE,
    has_results INTEGER NOT NULL,  -- 성능·운영 포인트(적용 결과 등)가 있는 항목
    company TEXT NOT NULL,
    post_url TEXT NOT NULL,
    published_at TEXT NOT NULL,
    data TEXT NOT NULL  -- data/entries.jsonl의 한 줄 (JSON)
);
CREATE INDEX entries_post_url ON entries(post_url);

-- 문제 유형·도메인은 항목마다 여러 개 (주·보조 구분 없음)
CREATE TABLE entry_problem_types (entry_id TEXT NOT NULL, problem_type TEXT NOT NULL);
CREATE INDEX entry_problem_types_type ON entry_problem_types(problem_type);

CREATE TABLE entry_domains (entry_id TEXT NOT NULL, domain TEXT NOT NULL);
CREATE INDEX entry_domains_domain ON entry_domains(domain);

CREATE TABLE entry_technologies (entry_id TEXT NOT NULL, technology TEXT NOT NULL);
CREATE INDEX entry_technologies_tech ON entry_technologies(technology);

-- kind: 기술 / 설계 방식. 버린 대안 집계는 기술만 센다
CREATE TABLE entry_rejected_alternatives (
    entry_id TEXT NOT NULL,
    name TEXT NOT NULL,
    kind TEXT NOT NULL
);

-- 형태소 분석한 텍스트만 색인하고 원문은 entries.data에서 읽으므로 내용 없는(contentless) 테이블
CREATE VIRTUAL TABLE entries_fts USING fts5(
    {", ".join(FTS_COLUMNS)}, content='', tokenize='unicode61 remove_diacritics 0'
);
"""
