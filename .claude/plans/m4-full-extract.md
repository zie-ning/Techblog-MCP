# M4 전체 추출 실행 계획

## Context

M3에서 추출 모델(`gpt-5.6-luna` medium)과 프롬프트 v4가 확정됐고 PR #5가 `main`에 병합됐다. `data/`에는 아직 M1 올리브영 20편(gpt-5-mini, 옛 프롬프트)만 있다. M4 목표는 1,262편 전체를 추출해 `entries.jsonl`을 완성하고, 기술 사전을 보강하고, M3에서 넘어온 분류 목록 검토를 마치는 것.

사용자 결정:
- 추출은 Batch API를 구현하지 않고 **기존 동기 CLI + `--workers`**로 돌린다 (추정 $5~6).
- 분류 목록은 **표본을 먼저 추출해 보고 결정**한 뒤 나머지를 추출한다 (목록이 바뀌면 표본만 재추출).

## 0. 브랜치

- 최신 `main`에서 `feat/m4-full-extract` 생성. M4.md 상태를 🔄 진행 중으로, 허브 README "지금 할 일"에서 병합 완료된 M3 PR 줄 제거 (첫 커밋 `docs:`).

## 1. 표본 추출 (약 200편)

- 블로그별 시드 고정 무작위 25편(kurly는 25편, 합 200편). M3 파일럿 80편을 포함해 기존 평가와 비교 가능하게 함. `eval/sample_pilot.py`의 표본 추출 로직을 재사용(필요하면 인자만 추가) → `eval/m4_sample_posts.txt`
- `uv run python -m pipeline.extract all --post-ids-file eval/m4_sample_posts.txt --outdated --workers 6` → `data/`에 바로 저장 (올리브영 M1 20편도 `--outdated`로 별도 재추출)
- 실패 글은 같은 명령 재실행으로 회수
- `uv run python eval/inspect_run.py data`로 분류 분포·쏠림·발췌 탈락·미등록 기술명·비용 확인

## 2. 분류 목록 검토 (사용자 결정 지점)

- 문제 유형·도메인 분포, 공백 후보 2개(JVM·GC 튜닝, 검색 품질)에 해당하는 글이 표본에 몇 편인지, "LLM·AI"·"사내 플랫폼·개발 도구" 도메인에 들어간 글의 성격을 정리해 보고
- 사용자가 결정하면 `src/techblog_mcp/taxonomy/problem_types.toml`·`domains.toml`과 `docs/기획.md` 반영 → 프롬프트 해시가 바뀌므로 표본만 `--outdated`로 재추출 (~$1)

## 3. 전체 추출

- `uv run python -m pipeline.extract all --workers 6` (이미 처리된 글은 건너뜀, 진행분은 글마다 저장). 연결 실패 글은 재실행으로 회수, 최종 실패 0편 확인
- `inspect_run.py data`로 전체 리포트를 `eval/reports/m4-full.md`로 저장. `inspect_run.py`의 고정 상수 `TOTAL_POSTS` 기반 전체 추정은 전체 run에서 의미 없으므로 표시만 정리

## 4. 기술 사전 보강

- `uv run python -m pipeline.normalize`로 미등록 이름 빈도 리포트 → 빈도 높은 이름부터 `src/techblog_mcp/taxonomy/technologies.toml`에 표준 이름·별칭·종류·상위 기술 추가 (일회성 언급·브라우저 API 등 사전에 넣지 않을 이름의 기준은 첫 리포트를 보고 사용자와 맞춤)
- `--apply`로 `entries.jsonl` 재정규화 (LLM 재호출 없음)

## 5. 마무리

- `uv run python -m pipeline.build_index`로 검색 DB 빌드, MCP 서버로 M1 시나리오 몇 개(선착순 쿠폰 등) 직접 검색해 확인
- 발췌 검증 실패 처리 현황(`dropped_evidences`, 항목 통째 탈락 수) 집계해 완료 기준 기록
- 완결성·항목 분할·경계 글 관찰 결과는 M5로 넘길 항목으로 정리
- M4.md 진행 기록·상태, 허브 README, 필요 시 기획.md 갱신. 커밋은 단계별 원자적으로(데이터 / 사전 / 문서 분리). push·PR은 사용자 지시 후

## 수정·생성 파일

- `data/posts.jsonl`, `data/entries.jsonl`, `data/prompt_versions/` (추출 산출물)
- `src/techblog_mcp/taxonomy/technologies.toml` (+ 분류 변경 시 `problem_types.toml`·`domains.toml`)
- `eval/m4_sample_posts.txt`, `eval/reports/m4-*.md`, 필요 시 `eval/sample_pilot.py`·`eval/inspect_run.py` 소폭 수정
- `docs/milestones/M4.md`, `docs/README.md`, `docs/기획.md`

## 검증

- 단계마다 `uv run pytest`, `uv run ruff check`, `uv run ruff format --check`
- 추출 후: `posts.jsonl` 1,262줄, 실패 0편, `inspect_run.py` 리포트의 발췌 존재율이 M3 luna run(99%대)과 비슷한지
- 사전 보강 후: normalize 리포트의 미등록 이름 수 감소 확인
- 색인 빌드 후 MCP `search`·`aggregate`로 실제 조회
