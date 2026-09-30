# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

국내 IT 기업 기술 블로그 8곳(토스, 우아한형제들, 카카오, 카카오페이, 네이버 D2, LY, 컬리, 올리브영)의 2023-09 이후 글을 수집해 LLM으로 구조화하고, 코딩 에이전트가 MCP 도구로 검색·집계하게 하는 로컬 stdio MCP 서버. 전체 문서와 마일스톤 현황은 허브 문서 [docs/README.md](docs/README.md)에서 시작한다. 결정 사항과 그 근거는 [docs/기획.md](docs/기획.md), 원칙·기술 선택·구조는 [docs/구현계획.md](docs/구현계획.md), 마일스톤별 작업과 진행 기록은 [docs/milestones/](docs/milestones/)에 있다. 설계를 바꾸는 작업은 기획.md와 구현계획.md를 먼저 읽고, 결정이 바뀌면 문서도 함께 고친다. 진행 상황이 바뀌면 해당 마일스톤 문서와 허브 문서를 함께 갱신한다.

## 작업 방식

- 기획·설계상 선택지가 있는 결정은 임의로 정하지 말고 사용자에게 질문한다. 결정되면 `docs/기획.md`에 반영한다.
- 커밋 메시지, 코드 주석, 문서는 한국어. 식별자는 영어.
- `main`에 직접 커밋하지 않고 작업 단위 브랜치 → PR → Merge commit으로 병합한다. 세부 규칙은 `.claude/rules/`의 커밋·PR 규칙을 따른다.

## 명령어

```bash
uv sync                                   # 의존성 설치 (dev 그룹 포함)
uv run pytest                             # 전체 테스트
uv run pytest tests/test_smoke.py::test_package_importable   # 단일 테스트
uv run ruff check                         # 린트
uv run ruff format                        # 포맷 (CI는 --check로 검사)
uv run --python 3.11 --isolated pytest    # 최소 지원 버전(3.11)에서 테스트

uv run python -m pipeline.collect oliveyoung                                   # 원문 수집
uv run python -m pipeline.extract oliveyoung --post-ids-file eval/m1_posts.txt # 추출 (OPENAI_API_KEY 필요, .env 가능)
uv run python -m pipeline.extract oliveyoung --outdated                        # 프롬프트·모델이 바뀐 글만 재추출
uv run python -m pipeline.normalize [--apply]                                  # 기술명 재정규화·미등록 리포트
uv run python -m pipeline.build_index                                          # 검색 DB 빌드
uv run techblog-mcp                                                            # MCP 서버 (stdio)
```

파이프라인 의존성은 `pipeline` 의존성 그룹에 있고 `[tool.uv] default-groups`로 기본 설치된다.

CI(`.github/workflows/ci.yml`)는 Python 3.11과 3.14에서 `uv sync --locked` → ruff check → ruff format --check → pytest를 실행한다. 의존성을 바꾸면 `uv.lock`도 커밋해야 한다.

## 아키텍처

두 부분으로 나뉘고, 의존성도 분리한다.

- **`src/techblog_mcp/`** — 사용자가 `uvx`로 설치하는 MCP 서버 패키지. 검색에 필요한 의존성만 `[project].dependencies`에 둔다.
- **`pipeline/`** — 수집·추출·색인 빌드. 배포 패키지에 포함되지 않는다. OpenAI SDK, 크롤링 라이브러리 등은 서버 의존성이 아니라 별도 의존성 그룹에 둔다. 테스트에서는 `pythonpath = ["."]` 설정으로 import한다.

데이터 흐름:

```
블로그 → pipeline/collect → data/raw/ (원문 캐시, git 제외)
       → pipeline/extract (글 유형 분류, 구조화, 발췌 검증) → data/entries.jsonl (커밋)
       → pipeline/build_index (kiwipiepy 형태소 분석 → SQLite FTS5) → 검색 DB (빌드 산출물, git 제외)
       → src/techblog_mcp (MCP 도구가 검색 DB 조회)
```

### 여러 파일에 걸친 규칙

- **구조화 유형 두 가지**: 사례형(문제 상황 / 해결 방법 / 성능·운영 포인트 + 글에 명시된 경우에만 버린 대안, 1글 = N개)과 인사이트형(핵심 내용 / 적용해볼 점, 1글 = 1개). 모든 항목 필드는 `{text, evidence}` 형태로 원문 발췌를 함께 가진다.
- **발췌 검증**: 추출된 `evidence`는 원문에 실제로 존재하는지 코드로 검사한다. LLM이 지어낸 내용을 거르는 핵심 장치이므로 우회하지 않는다.
- **프롬프트 버전**: 추출 프롬프트·출력 스키마를 고치면 `pipeline/extract/prompt_version.py`의 해시가 자동으로 바뀐다. `data/prompt_versions/`의 스냅샷은 자동 생성물이라 직접 고치지 않는다.
- **`src/techblog_mcp/taxonomy/`는 추출과 서버가 공유**한다 (설치 패키지에 포함돼야 해서 패키지 안에 둠). 문제 유형·도메인 정의에서 MCP 도구 입력 스키마의 `enum`을 자동 생성하므로 두 곳의 값이 항상 같아야 한다. 기술명은 기술 사전(표준 이름 + 별칭)으로 정규화한다.
- **형태소 분석은 색인과 검색에서 같은 방식**을 써야 한다 (kiwipiepy, `techblog_mcp.search.analyzer`). 한쪽만 바꾸면 검색이 깨진다. DB 스키마를 바꾸면 `search/schema.py`의 `SCHEMA_VERSION`을 올린다.
- **MCP SDK는 2.x**다. `FastMCP`가 아니라 `mcp.server.mcpserver.MCPServer`를 쓴다.
- **DB 경로 로딩은 `src/techblog_mcp/db.py` 한 곳**에 둔다. 나중에 GitHub Release에서 DB를 내려받는 방식으로 교체할 지점이다.

### MCP 도구 계약

- 도구는 `search`, `get_details`(ID 최대 5개), `aggregate` 세 개와 MCP prompt `techblog`.
- 세 도구 모두 읽기 전용 annotation(`readOnlyHint` 등)을 단다. DB에 쓰는 도구를 추가하면 annotation도 바꾼다.
- 결과는 JSON이 아니라 읽기 쉬운 텍스트로 반환한다. `search` 카드에는 근거 발췌를 넣지 않고 `[사례]`/`[인사이트]` 유형을 표시한다.
- `search` 필터는 문제 유형·도메인(enum), 기술(자유 입력 → 서버 정규화), `kind`, `limit`(기본 5, 최대 10). 회사·날짜 필터는 의도적으로 없다. `limit`은 M5에서 제거하고 서버가 관련도 기준으로 최대 10건을 돌려주도록 바꿀 예정이다.
- `aggregate`는 모수(전체 건수·회사 수)와 예시 ID를 함께 반환하고, 건수를 사례/인사이트로 나눠 표시한다. 문제 유형은 주 유형 기준으로 센다.
- 결과가 없거나 적으면 그 사실을 명시해 에이전트가 사례를 지어내지 않게 한다.

## 수집 규칙

- 정직한 User-Agent(예: `TechblogCaseBot/0.1 (+저장소 URL)`)를 쓰고 브라우저로 위장하지 않는다. robots.txt를 지키고, Cloudflare 등 봇 확인은 우회하지 않으며, 요청 사이에 간격을 둔다.
- 원문 전체는 `data/raw/`에만 두고 배포하지 않는다. 배포 데이터에는 요약, 짧은 발췌(필드당 1~2문장), 원문 링크만 넣는다.
- 블로그별 수집 경로(피드, 사이트맵, 공개 JSON API, WordPress REST API)와 주의점은 `docs/기획.md`의 "블로그 수집 조사 결과"에 정리되어 있다.
