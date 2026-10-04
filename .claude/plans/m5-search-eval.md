# M5 검색 평가와 튜닝 실행 계획

## Context

M4에서 1,262편을 추출해 항목 1,315개(`data/entries.jsonl`)가 완성됐고 PR #6이 `main`에 병합됐다. 지금 `search`는 검색어 형태소를 OR로 묶은 BM25라서 흔한 단어 하나만 맞아도 후보가 되고, `limit`까지 채우느라 무관한 카드가 섞인다. DB에 없는 주제를 물어도 "결과 없음"이라고 하지 않는다. M1~M4 관찰 기록 12건으로 기준 후보는 좁혀 뒀지만 모두 32개 항목 기준이라 새 데이터로 다시 재야 한다.

M5의 목표는 다음과 같다.
- 검색 평가셋을 만들어 수치로 비교한다.
- 그 수치로 관련도 기준, 필드 가중치, 형태소 처리, 하이브리드 검색 도입 여부를 결정한다.
- `limit`를 없애고 "관련도 기준을 넘는 항목만 최대 10건"을 반환하도록 구현한다.

### 사용자 결정 (이번 계획 단계)

| 항목 | 결정 |
| --- | --- |
| 질문 구성 | 30개를 다음처럼 섞는다: M1 시나리오·관찰 기록 검색어 약 10개, 데이터 분포에서 뽑은 질문 약 15개(문제 유형 21개가 고르게), DB에 없는 주제 약 5개 |
| 정답 판정 | Claude가 판정하고 판정 이유를 파일에 남긴다. 사용자 검수 없이 진행하고 애매한 질문만 보고한다 |
| 단위 | 라벨은 항목 단위로 붙인다. 지표는 항목 단위와 글 단위(같은 글은 하나로 봄)를 둘 다 계산한다 |
| 임베딩 후보 | 로컬 경량 ONNX 모델(fastembed)이 실제 도입 후보다. OpenAI 임베딩은 품질 기준점으로만 잰다 |
| aggregate 넘어온 항목 | M5 마지막에 처리한다 (성능·운영 표시 기준, parent 묶음 집계) |
| 경계 글 | 평가에서 잡음으로 나오면 M5 안에서 분류 프롬프트를 보강하고 해당 글만 재추출한다 |
| 평가 기록 | 저장소의 스크립트와 리포트(`eval/`)만 쓴다. LangSmith는 쓰지 않는다 |
| 브랜치 | `feat/m5-search-eval` |

## 0. 브랜치와 문서 시작

> 상태: **완료** (역사 기록으로 남김). 브랜치 생성과 문서 갱신은 [M5.md](../../docs/milestones/M5.md)의 진행 기록을 참조한다.

- 최신 `main`에서 `feat/m5-search-eval`을 만든다. 계획 모드라 아직 만들지 않았고, 승인 직후 첫 작업으로 한다.
- M5.md 상태를 🔄 진행 중으로 바꾸고 "진행 방식" 표에 위 결정을 적는다. 허브 README의 "지금 할 일"에서 병합이 끝난 M4 PR 줄을 지우고 M5 상태를 갱신한다. 이 계획 파일은 `.claude/plans/m5-search-eval.md`로 저장소에 둔다(M4와 같은 방식). 첫 커밋은 `docs:`.

## 1. 평가 도구

- **`eval/search_eval.py`** (새로 작성): 평가셋을 읽어 검색 설정별로 상위 N건을 뽑고 지표를 계산해 `eval/reports/m5-*.md`에 저장한다.
  - 지표: Recall@5와 MRR(기획.md에서 정한 지표)을 항목 단위와 글 단위로 계산한다. 서버가 최대 10건을 돌려주게 되므로 Recall@10을 보조로 넣는다.
  - 관련도 기준을 평가할 때는 세 가지를 더 본다: 기준을 통과한 결과 수, 통과 결과 중 무관한 항목 비율, 없는 주제 질문에서 "결과 없음"으로 판정한 비율.
  - 검색은 `techblog_mcp.search.query`를 직접 부른다. 실험용 설정(가중치, 기준, 형태소, 임베딩 결합)은 인자로 바꿀 수 있게 하되 서버 코드는 결정된 뒤에만 고친다.
- **평가셋 파일**: `eval/search/queries.toml`. 질문, 출처(M1 시나리오 / 데이터 / 없는 주제), 필터(있으면), 항목별 라벨(관련 / 일부 관련 / 무관)과 판정 이유를 담는다. 형식과 판정 기준은 `eval/search/README.md`에 적는다(`eval/gold/README.md`와 같은 방식).
- 실험용 의존성(fastembed)은 기본 동기화에 넣지 않는 별도 의존성 그룹에 둔다. CI와 서버 의존성은 바뀌지 않는다. OpenAI 임베딩은 기존 `pipeline` 그룹의 `openai`를 쓴다.

## 2. 임베딩 준비와 정답 후보 모으기

- 항목 임베딩을 미리 계산해 `eval/search/embeddings/`(git 제외)에 캐시한다.
  - fastembed 다국어 소형 모델 2~3개. 후보는 multilingual-e5-small, paraphrase-multilingual-MiniLM 계열이고, fastembed 지원 목록에서 크기를 보고 고른다.
  - OpenAI `text-embedding-3-small`/`large` 기준점. 1,315개 항목 기준 수 센트.
- 질문 30개를 작성한다.
- 정답 후보 풀: BM25(현재 설정과 가중치 변형) 상위 20, 임베딩 모델별 상위 20, 필터를 건 검색 결과를 합친다. 임베딩 후보까지 넣는 것은 하이브리드가 라벨에서 불리해지지 않게 하기 위해서다.
- Claude가 풀의 항목을 제목·요약과 대조해 라벨을 붙이고 이유를 적는다. 애매한 질문은 모아서 보고한다.

## 3. 기준선과 실험

모든 실험은 같은 평가셋으로 돌리고, 결과는 실험마다 리포트로 남긴다.

| 실험 | 내용 |
| --- | --- |
| E1 기준선 | 현재 BM25(가중치 그대로, OR 매칭). 1,315개 항목에서 관찰 기록 12건 검색어의 점수 분포도 다시 재서 M5.md 관찰 기록에 추가한다 |
| E2 필드 가중치 | `FTS_COLUMNS` 가중치를 몇 가지 조합으로 비교한다(제목·문제 상황·키워드 비중 등). 기획.md 미결정 "검색 대상 필드와 가중치"를 정리하는 근거 |
| E3 형태소 | Kiwi 사용자 사전(기술 사전의 표준 이름·별칭, "시그널링", "아웃박스", "동시성" 같은 잘못 잘리는 단어)을 넣고 비교한다. `analyzer.py` 한 곳만 고치므로 색인과 검색이 같이 바뀐다 |
| E4 글 묶기 | 같은 글의 항목이 여러 개 걸리면 글 단위로 점수를 합치거나 최고점으로 올리는 방식을 비교한다(M1 시나리오 2, Kafka 중복·유실 글 문제) |
| E5 관련도 기준 | 후보 ① 1위 대비 상대 점수 ② 검색어 형태소 일치 비율 ③ 희소 단어(IDF 높은 단어) 일치 여부 ④ BM25 절대 점수. 단독과 조합으로 비교한다. "비교 대상이 되는 사례"(M1 시나리오 5의 case_0030 같은 일부 관련 항목)를 잘라내는지도 따로 확인한다 |
| E6 하이브리드 | BM25와 임베딩을 RRF(순위 역수 합)로 결합해 BM25 단독과 비교한다. 하이브리드에서 쓸 관련도 기준도 함께 본다. 로컬 모델은 설치 크기(패키지 + 모델 파일), 서버 기동 시간 증가, 검색어 임베딩 지연 시간을 잰다. 단어는 겹치지만 뜻이 다른 글(선착순 동시성 vs 멤버십 대량 발급)을 구분하는지 확인한다 |

- **경계 글**: E1에서 블로그 글 모음·행사 참관기 등이 잡음으로 자주 나오면 해당 글 목록과 근거를 보고한다. 분류 프롬프트(`pipeline/extract/`의 분류 지시문)를 보강한 뒤 그 글만 `--post-ids-file`로 재추출하고, 색인을 다시 빌드한다.
  - 재추출하면 항목 ID가 새로 붙는다. 평가셋 라벨에서 사라진 ID는 정리하고 E1을 다시 잰다.
  - 프롬프트 해시가 바뀌어 다른 글은 `--outdated` 대상이 되지만, 전체 재추출은 하지 않는다.

**사용자 결정 지점**: 실험이 끝나면 수치를 정리해 보고하고 아래 네 가지를 각각 질문한다.
1. 가중치·형태소 변경 채택 여부
2. 글 묶기 방식
3. 관련도 기준과 임계값
4. 하이브리드 도입 여부

결정되면 기획.md "검색"·"결과 수 결정"·미결정 사항에 반영한다.

## 4. 결정 반영 구현

- `src/techblog_mcp/search/query.py`: `DEFAULT_LIMIT`과 `limit` 인자를 제거하고 관련도 기준을 넘는 항목만 최대 10건 돌려준다. `SearchResult.total`은 "검색어가 하나라도 걸린 건수"가 아니라 "기준을 통과한 건수"로 바꾼다.
- `src/techblog_mcp/server.py`: `search`의 `limit` 파라미터를 제거한다. `MAX_DETAIL_IDS`(5)는 "search 기본 결과 수와 같게"라는 근거가 사라지므로 값을 유지할지 결정 지점 보고 때 함께 질문한다.
- `src/techblog_mcp/render.py`: "N건뿐" 안내를 관련도 기준 통과 건수 기준으로 바꾼다. 없는 주제에서는 "결과 없음" 문구가 나오게 한다.
- 가중치·형태소를 채택하면 `schema.py`의 `FTS_COLUMNS`와 `analyzer.py`를 고치고 `SCHEMA_VERSION`을 올린다. 하이브리드를 채택하면 임베딩 열·`build_index`·서버 의존성을 바꾸고 `SCHEMA_VERSION`을 올린다.
- 테스트: `tests/test_search.py`, `tests/test_server.py`에 관련도 기준(무관 항목 제외, 없는 주제 0건, 일부 관련 항목 유지)과 `limit` 제거를 반영한다.

## 5. aggregate 넘어온 항목 (M5 마지막)

- "성능·운영 포인트 있음" 표시 기준(유지 / 수치가 있는 경우만 / 제거)과 parent 묶음 집계 방식(예: Kafka 아래에 Amazon MSK 합산 표시)의 선택지를 데이터 수치와 함께 보고하고 질문한 뒤 구현한다. 관련 파일은 `query.aggregate`, `render.aggregate_result`, `build_index`(`has_results`), `taxonomy`.

## 6. 마무리

- 검색 DB를 다시 빌드하고 MCP 도구로 M1 시나리오(선착순 쿠폰, WebRTC 없는 주제, Kafka 중복 등)를 직접 확인한다.
- M5.md에 진행 기록, 결정 근거, 완료 기준을 적고 넘길 항목은 M6 등 받는 쪽에 적는다. 허브 README, 기획.md, CLAUDE.md(`limit` 관련 문구)도 갱신한다.
- 커밋은 원자적으로 나눈다: 평가 도구 / 평가셋 / 실험 리포트 / 검색 변경 / aggregate / 문서. push와 PR은 사용자 지시 후에 한다.

## 수정·생성 파일

- 새로 만듦: `eval/search_eval.py`, `eval/search/queries.toml`, `eval/search/README.md`, `eval/reports/m5-*.md`, `.claude/plans/m5-search-eval.md`
- 수정: `src/techblog_mcp/search/{query,schema,analyzer}.py`, `src/techblog_mcp/{server,render}.py`, `pipeline/build_index.py`, `pyproject.toml`·`uv.lock`(실험 그룹), `.gitignore`(임베딩 캐시), `tests/test_search.py`·`tests/test_server.py`
- 경계 글 재추출 시: 분류 프롬프트 파일, `data/posts.jsonl`·`data/entries.jsonl`·`data/prompt_versions/`
- 문서: `docs/milestones/M5.md`, `docs/README.md`, `docs/기획.md`, `CLAUDE.md`

## 검증

- 단계마다 `uv run pytest`, `uv run ruff check`, `uv run ruff format --check`. 의존성을 바꾸면 `uv sync --locked`도 확인한다.
- `uv run python eval/search_eval.py`가 기준선과 최종 설정의 수치를 재현하는지 확인한다(최종 리포트에 기준선 대비 Recall@5·MRR·없는 주제 판정률을 비교).
- `uv run python -m pipeline.build_index` 후 `uv run techblog-mcp`로 MCP `search`를 실제 호출해 다음을 확인한다.
  - `limit` 없이 결과 수가 달라지는지
  - 없는 주제에서 "결과 없음"이 나오는지
  - 관련 주제에서 무관 카드가 줄었는지
