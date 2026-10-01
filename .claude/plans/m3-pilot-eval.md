# M3. 파일럿과 추출 평가 — 실행 계획

## Context

M2까지 8개 블로그 1,262편의 원문을 `data/raw/`에 확보했다. M4에서 이 글을 모두 추출하기 전에 M3에서 다음을 정해야 한다.

- 추출 모델 (현재 `gpt-5-mini` medium은 M1 임시값)
- 분류 목록(문제 유형 20 / 도메인 10) 확정
- 추출 프롬프트 보강: M1에서 넘어온 6개 항목, M2에서 넘어온 1개 항목
- 발췌 검증 완화 여부 (M4 시작 전 결정)

지금 코드의 한계는 세 가지다.

- 추출 결과 경로가 `data/`로 고정돼 있고 글 URL로 덮어쓴다. 그래서 모델·프롬프트별 결과를 나란히 둘 수 없다.
- 토큰 사용량과 reasoning effort를 기록하지 않는다.
- 평가 스크립트와 정답셋이 없다 (`eval/`에는 `m1_posts.txt`만 있음).

**완료 기준**: 추출 모델 결정, 분류 목록 확정, 평가 결과 기록, 발췌 검증 완화 여부 결정.

### 확정한 진행 방식 (사용자 답변)

| 항목 | 방식 |
| --- | --- |
| 정답셋 초안 | Claude Code 세션에서 원문을 읽고 작성 → 사용자가 원문과 대조해 검수 |
| LLM 채점 | `eval/` 아래 OpenAI API 채점 스크립트. 채점 기준(rubric)은 프롬프트로 고정하고, 일부는 직접 검수 |
| 모델 후보 | 가성비 중심: 기준 `gpt-5-mini`(medium), nano급, mini의 effort 변형(low/high), 상위 모델 1개. 정확한 이름은 실행 시점의 모델 목록으로 확정 |
| 파일럿 표본 | 블로그마다 시드를 고정해 무작위 10편. 올리브영은 M1의 20편을 뺀 나머지에서 뽑음 |

## 0. 사전 정리 (작업 시작 시 바로)

- **플랜 파일 저장 위치**
  - 프로젝트 `.claude/settings.json`에 `"plansDirectory": ".claude/plans"`를 추가한다. 적용 전에 `update-config` 스킬로 키 이름을 확인한다.
  - 이 플랜 파일을 `.claude/plans/`로 복사해 커밋한다.
- **브랜치 규칙 변경**
  - `.claude/rules/commit.md` 브랜치 절에서 다음 두 문장을 지운다.
    - "브랜치는 작업 단위로 만든다"
    - "마일스톤 전체를 한 브랜치에 몰지 않는다"
  - 대신 "마일스톤 하나를 한 브랜치로 진행해도 된다"는 문장을 넣는다.
  - 이 저장소의 `CLAUDE.md` 작업 방식 절도 같은 방향으로 맞춘다. 지금 문구는 "작업 단위 브랜치 → PR"이다.

## 브랜치 구성

M3 전체를 **브랜치 하나 `feat/m3-pilot-eval`** 에서 진행한다.

- 최신 `main`에서 딴다.
- 아래 1~7 단계는 커밋 단위로 나누고, 커밋은 원자적으로 유지한다.
- PR은 마일스톤이 끝날 때 하나로 올린다.
- push·PR·병합은 사용자가 지시할 때만 한다.

| # | 단계 | 내용 |
| --- | --- | --- |
| 1 | 평가 기반 도구 | 추출 CLI 확장, 사용량 기록, 파일럿 표본 추출 |
| 2 | 파일럿 baseline | 현재 프롬프트로 파일럿 80편 추출, 점검 리포트 |
| 2.5 | LangSmith 도입 | 추출 트레이싱(원문 포함), 파일럿 Dataset, baseline을 Experiment로 등록 |
| 3 | 프롬프트 v2 | 점검 결과를 반영한 프롬프트·스키마·분류 목록 수정 |
| 4 | 정답셋 | 정답셋 24편 초안 작성과 검수 |
| 5 | 평가 지표 | 자동 지표와 LLM 채점 스크립트 |
| 6 | 발췌 검증 실험 | 발췌 검증 완화 실험과 결정 |
| 7 | 모델 결정 | 모델 비교 실행, 결정, 문서 마감 |

---

## 1. 평가 기반 도구

**추출 CLI 확장** (`pipeline/extract/__main__.py`)

- `--out-dir DIR`
  - `posts.jsonl`·`entries.jsonl`을 저장할 디렉터리. 기본값은 `data/`.
  - `Store(posts_path, entries_path)`가 이미 경로 인자를 받으므로 CLI에서 넘기기만 하면 된다 (`pipeline/extract/store.py`).
  - 평가용 실행은 `eval/runs/{run_name}/`에 저장한다. 그러면 `data/entries.jsonl`(M1 올리브영 20편)은 건드리지 않는다.
- `source`에 `all` 허용
  - 이때 `--post-ids-file`의 줄은 `source/post_id` 형식이다. 블로그마다 숫자 ID가 겹칠 수 있어서다.
  - 기존 `eval/m1_posts.txt`처럼 `/`가 없는 줄은 지정한 source의 ID로 본다. 기존 형식을 그대로 쓸 수 있다.
- `--workers N`
  - `ThreadPoolExecutor`로 글 단위 병렬 추출을 한다.
  - 저장(`store.add`/`save`)은 메인 스레드에서만 해서 스레드 안전성을 지킨다.
  - 모델 후보마다 80편을 돌려야 해서 넣는다. 기본값은 1.

**사용량 기록**

- `PostRecord`(`pipeline/extract/schema.py`)에 필드를 추가한다.
  - `reasoning_effort`
  - `usage`: 입력·캐시·출력·reasoning 토큰, 호출 수 (분류 + 구조화 + 재시도 합계)
  - `evidence_total`: 검증 전 발췌 수. 발췌 원문 존재율의 분모다.
- 새 필드는 기본값을 두어 기존 `posts.jsonl`도 읽히게 한다.
  - 이 필드들은 LLM 출력 스키마가 아니다. 그래서 프롬프트 버전 해시는 바뀌지 않는다.
- `OpenAILLM.parse`(`pipeline/extract/extractor.py:52`)에서 `response.usage`를 누적한다. `LLM` Protocol에는 선택적 사용량 조회를 추가한다. 테스트용 `FakeLLM`은 0을 돌려준다.

**파일럿 표본**

- `eval/sample_pilot.py`
  - `raw.load_all(source)`로 블로그별 글 목록을 읽는다.
  - `random.Random(시드)`로 블로그마다 10편을 뽑는다. 올리브영은 `eval/m1_posts.txt`의 글을 뺀다.
  - 결과를 `eval/pilot_posts.txt`(`source/post_id` 줄)로 저장한다.
  - 각 줄 주석에 제목과 평문 길이를 남겨, 짧은 글이 몇 편 들어갔는지 바로 보이게 한다.

**가격표**

- `eval/pricing.toml`: 모델별 100만 토큰당 단가. 실행 시점 공식 가격을 사용자와 확인해 채운다.
- 이후 평가 리포트가 이 단가로 run 비용과 1,262편 전체 비용을 추정한다.

**테스트** (`tests/test_extract.py`에 추가)

- `--out-dir` 경로
- `source/post_id` 파싱
- 사용량 누적
- 표본 추출의 결정성 (같은 시드 → 같은 결과)

**문서**: M3 상태를 🔄로 바꾼다 (`docs/milestones/M3.md` 상태 줄 + `docs/README.md` 현황 표).

## 2. 현재 프롬프트로 파일럿

**실행**

```
uv run python -m pipeline.extract all --post-ids-file eval/pilot_posts.txt --out-dir eval/runs/baseline-gpt-5-mini-medium --workers 4
```

- `OPENAI_API_KEY`가 필요하다 (`.env`).
- 실행 전에 예상 비용을 알린다.

**점검 스크립트** `eval/inspect_run.py`

run 디렉터리를 읽어 마크다운 리포트 `eval/reports/{run}.md`를 만든다. 리포트에 넣을 내용:

- kind·post_type 분포 (블로그별)
- 평문 1,500자 미만 글의 분류 결과
- 문제 유형·도메인 분포와 쏠림. 한 분류에 30% 넘게 몰리는지, 한 번도 안 쓰인 분류가 있는지.
- 글당 항목 수
- 발췌 탈락률과 탈락 발췌 목록
- 기술 사전에 없는 이름: `pipeline.normalize`의 `renormalize` 재사용
- 버린 대안 수
- 토큰·비용

**직접 점검 (M3 넘어온 항목별)**

리포트와 결과를 보며 항목마다 해당 사례를 골라 `docs/milestones/M3.md`의 "진행 기록"에 적는다.

| 넘어온 항목 | 확인할 것 |
| --- | --- |
| 분류 편향 | 인사이트 비율, 팁 모음 글이 사례로 쪼개지는지 |
| 주 문제 유형 오분류 | 오분류 사례 목록 |
| 조건 정보 누락 | 원문에 규모 수치가 있는데 문제 상황에 빠진 사례 비율 (샘플 20건) |
| technologies 품질 | 개념·클래스명이 섞였는지, 버린 대안이 technologies에 들어갔는지 |
| 발췌 검증 | 탈락 발췌 중 "떨어진 문장 이어 붙이기" 유형이 몇 건인지 |
| 기술 사전 구조 | 집계 시 섞이는 기술 종류, 상하 관계 후보 (Kafka/MSK 등) |
| 짧은 글 (M2) | 영상 소개·공지 글이 제외되는지, 목차만으로 사례를 지어내지 않는지 |

**결과물**: `eval/runs/baseline-*/`(커밋), `eval/reports/baseline-*.md`, M3 진행 기록.

## 2.5 LangSmith 도입 (2026-09-30 결정 추가)

결정과 근거는 `docs/기획.md` "평가·관측 도구" 행. 원문을 트레이스에 올리는 방향으로 확정했다.

- **트레이싱**: `extract_post`를 `@traceable`로 감싸고 OpenAI 클라이언트를 `wrap_openai`로 감싼다.
  - 글 하나가 트레이스 하나이고, 분류 → 구조화 → 재시도 호출이 하위 단계로 보인다.
  - 메타데이터: source/post_id, URL, 모델, effort, 프롬프트 버전, run 이름
  - `LANGSMITH_TRACING` 환경 변수로 켜고 기본은 끈다. 키가 없으면 지금과 똑같이 동작한다.
  - `langsmith`는 `pipeline` 의존성 그룹에 넣는다. 서버 의존성에는 넣지 않는다.
- **Dataset**
  - `techblog-pilot-80`: 입력은 글 ID·제목·평문
  - 정답셋(4단계)은 정답 출력을 포함한 별도 Dataset으로 둔다.
  - 실패 사례 회귀셋은 3단계에서 트레이스를 보며 추가한다.
- **Experiment**: baseline run을 API 재호출 없이 `evaluate()`로 등록한다. target은 run 파일을 읽어 돌려주는 함수다.
- **사용자 준비물**: LangSmith 계정과 `LANGSMITH_API_KEY`(`.env`). 계정 생성과 키 입력은 사용자가 직접 한다.
- **테스트**: 트레이싱을 끈 상태에서 기존 동작이 같은지, 메타데이터 구성 함수

## 3. 프롬프트·스키마·분류 목록 수정

2의 점검 결과를 근거로 고친다. 선택지가 있는 결정은 그때 데이터를 보여 주고 사용자에게 묻는다. 결정되면 `docs/기획.md`에 반영한다.

**질문할 결정**

- 문제 유형·도메인 목록 조정: 합치기·나누기·이름 바꾸기, LLM·AI 도메인 세분화 여부
  - 이 결정으로 기획.md 미결정 사항 "분류 목록 조정 기준"도 함께 정한다.
- 조건 정보: 프롬프트로 "원문의 규모·제약 수치를 문제 상황에 반드시 포함"만 요구할지, 별도 필드(`conditions`)를 둘지
  - 별도 필드를 두면 서버 렌더링, DB 스키마, `SCHEMA_VERSION`까지 바뀐다.
- 기술 사전 구조: 기술에 분류(메시지 브로커·DB·모니터링 등)를 붙일지, 상하 관계(`parent`)를 둘지
  - 붙이면 `technologies.toml` 형식, `taxonomy/__init__.py`, `aggregate`에 영향이 간다.
- **짧은 글 처리 방식**: 영상 소개·행사·공지·너무 짧은 글
  - 현재 설계
    - 수집 단계에서 미리 거르는 글은 토스 Design·외부 링크 글과 D2 news뿐이다.
    - 나머지 글은 `data/raw/`에 저장된다.
    - 추출 단계의 분류 호출에서 `kind=제외`가 되면 `posts.jsonl`에 기록만 남는다. 항목(`entries.jsonl`)은 만들지 않으므로 검색 DB에도 들어가지 않는다.
  - baseline에서 짧은 글이 실제로 잘 제외되는지 보고 두 가지 중 고른다.
    - ① 지금처럼 LLM 분류에만 맡기고 프롬프트를 보강한다.
    - ② 평문 길이 등 규칙으로 LLM 호출 전에 제외해 비용을 줄인다. 짧지만 가치 있는 글을 놓칠 위험이 있다.

**예상 수정** (`pipeline/extract/prompts.py`, `schema.py`의 Field 설명)

- `CLASSIFY` 보강
  - 인사이트 기준을 구체화한다. 팁 모음, 도구 사용기, 여러 곁가지로 구성된 글이 여기에 해당한다.
  - 발표 영상 소개·목차뿐인 글, 행사·공지 글은 제외한다는 규칙을 넣는다.
- `structure_case` 보강
  - 주 문제 유형 선택 기준을 넣는다 (예: "비용이 동기면 비용 절감").
  - technologies에서 개념·클래스·메서드명과 버린 대안을 뺀다는 규칙을 넣는다.
  - 떨어진 문장은 각각 따로 인용한다는 규칙을 넣는다.
- 분류 목록을 바꾸면 함께 고칠 곳
  - `src/techblog_mcp/taxonomy/*.toml`
  - 기존 `data/entries.jsonl`의 해당 값
  - `tests/test_taxonomy.py`의 개수
  - 서버 enum은 자동으로 따라간다.
- 프롬프트 버전 해시는 자동으로 바뀐다. 스냅샷은 실행할 때 생긴다.

**검증**

- `pytest`, `ruff`
- 파일럿 80편 재추출 → `eval/runs/v2-gpt-5-mini-medium/` → `inspect_run`으로 baseline과 비교한다.
- 비교 대상: 분포 변화, 짧은 글 제외, technologies 품질.
- 필요하면 한 번 더 반복한다.

## 4. 정답셋 24편

**표본**

- 파일럿 80편에서 블로그당 3편, 모두 24편을 고른다.
- 제외·인사이트·여러 사례 글, 짧은 글이 골고루 들어가게 한다.
- 목록은 `eval/gold_posts.txt`에 둔다.

**형식** `eval/gold/{source}__{post_id}.json`

분류 목록이 확정된 v2 기준으로 작성한다.

```
{ "source", "post_id", "url", "title",
  "post_type", "kind", "kind_alternatives": [],       # 경계 글은 허용 답 추가
  "entries": [
    { "summary": "이 사례의 문제-해법 한 줄",
      "primary_problem_type", "acceptable_problem_types": [], "domain",
      "technologies": [...],                          # 정규화된 표준 이름
      "rejected_alternatives": [...],                 # 글에 명시된 것만
      "key_facts": ["초당 3만 요청", ...] }            # 반드시 담겨야 할 조건·수치·결과
  ],
  "notes": "경계 판단 근거", "reviewed": false }
```

- 원문 전문은 넣지 않는다. 요약과 짧은 수치만 넣어 배포 원칙을 지킨다.

**절차**

1. 이 세션에서 원문(`data/raw`)을 읽고 초안을 쓴다.
2. 사용자가 원문과 대조해 검수하고 `reviewed: true`로 바꾼다.
3. `eval/gold/README.md`에 라벨링 기준을 적는다: 경계 글 판단, 사례 분할 기준, key_facts 선정 기준.
4. 스키마 검증 테스트를 둔다 (분류 값이 taxonomy에 있는지).

## 5. 자동 지표와 LLM 채점

> 2026-10-01 변경: 정답 검수 중 사례·인사이트 구분을 없앴다(추출/제외만 판단, 항목 구조 하나). 아래 "분류 일치율"은 추출 여부 일치율, "사례 수"는 항목 수로 읽는다. 결정과 근거는 docs/기획.md "사례·인사이트 구분 폐지".

**`eval/extract_eval.py`**: run 디렉터리와 정답셋을 받아 지표를 계산한다.

| 지표 | 계산 방식 |
| --- | --- |
| 분류 일치율 | kind, post_type (`kind_alternatives` 허용) |
| 항목 수 차이 | 글별 사례 수 − 정답 사례 수 분포 |
| 문제 유형·도메인 일치율 | 사례를 정답과 대응시킨 뒤 계산. 대응은 채점기 결과를 쓴다 |
| technologies 정밀도·재현율 | 글 단위 집합 비교 |
| 버린 대안 정밀도·재현율 | 정답과 비교 |
| 원문에 없는 버린 대안 비율 | 정답에 없는 버린 대안 중 원문에서도 확인되지 않는 비율 |
| 발췌 원문 존재율 | `1 - dropped_evidence / evidence_total` (전체 80편에서도 계산 가능) |
| 비용 | 편당 토큰·비용, 1,262편 추정 비용 |

**`eval/judge.py`**: OpenAI API 채점 (LangSmith `evaluate()`의 evaluator로도 등록)

- 입력: 원문 평문 + 추출 결과 + 정답 항목
- 출력: structured output으로 받는다.
  - 사례 대응표
  - 항목별 점수 1~5: 충실성(원문에 근거), 완결성(`key_facts` 포함률), 카드 요약 적합성(첫 줄이 최종 해결책인지), 분할 적절성
  - 이유
- 채점 모델과 기준 프롬프트는 파일 상단에 고정하고, 채점 결과에 채점 프롬프트 해시를 남긴다.
- 원문 추출용 평문화는 `pipeline.extract.text.html_to_text`, 구조화 출력 호출 패턴은 `OpenAILLM`을 재사용한다.
- 채점 결과는 `eval/runs/{run}/judge.jsonl`에 캐시한다. 같은 run과 채점 프롬프트면 다시 부르지 않는다.

**채점 신뢰도 확인**

- ~~채점 10건을 뽑아 사용자가 LangSmith Annotation queue에서 원문을 보며 직접 점수를 매긴다.~~
  2026-10-01 변경: 사람이 채점 결과를 검수하지 않는다. Claude Code 세션이 채점 결과를 원문·추출 결과와 대조한다.
- 채점기와의 일치 정도를 `docs/milestones/M3.md`에 기록한다.

**비교 리포트** `eval/compare.py`

- 여러 run의 지표를 한 표로 모아 `eval/reports/comparison.md`에 쓴다.

**테스트**: 지표 계산 함수 단위 테스트 (가짜 run·정답셋).

## 6. 발췌 검증 완화 실험

- `pipeline/extract/evidence.py`에 문장 단위 검증 모드를 선택지로 추가한다.
  - 발췌를 문장으로 쪼개 문장마다 원문에 있으면 통과한다.
  - 기본값은 지금 규칙을 유지한다.
- 비교할 세 가지:
  - ① 현재 규칙
  - ② 문장 단위 완화
  - ③ 현재 규칙 + 프롬프트 보강 ("떨어진 문장은 따로 인용", 3에서 반영)
- 기존 run의 원래 LLM 출력으로 재검증할 수 있어야 한다.
  - 그래서 추출 시 검증 전 원본을 `eval/runs/{run}/drafts.jsonl`에 남기는 옵션(`--save-drafts`)을 1이나 이 브랜치에 넣는다.
  - 이렇게 하면 ②는 LLM 재호출 없이 계산된다.
- 측정
  - 재현율: 완화로 되살아나는 발췌 수
  - 정밀도 손실: 되살아난 발췌 중 떨어진 문장을 섞어 뜻이 바뀐 비율. 전수를 LLM으로 채점하고, 샘플은 직접 검수한다.
- 결정은 사용자에게 물어 `docs/기획.md`의 "발췌 검증 실패 처리" 행을 갱신한다. M4 문서의 선결 조건도 해소 표시한다.

## 7. 모델 비교와 마감

**후보 확정**

- `openai` SDK의 `models.list()`로 사용 가능한 모델을 확인한다.
- 그 결과로 후보 4~5개를 사용자와 확정한다: 기준 mini/medium, mini/low, mini/high, nano급, 상위 1개.
- 단가는 `eval/pricing.toml`에 채운다.

**실행**

- 후보마다 최종 프롬프트(v2)로 파일럿 80편을 `eval/runs/{model}-{effort}/`에 추출한다.
- 정답셋 지표는 24편으로, 발췌 존재율·분포·비용은 80편으로 본다.
- 실행 전 run별 예상 비용을 알린다.

**결정**

- `comparison.md`와 비용 추정을 보고 사용자와 결정한다.
- 결정되면 반영할 곳:
  - `DEFAULT_MODEL`과 reasoning effort 기본값 (`pipeline/extract/__main__.py:26`)
  - `docs/기획.md` "M1 임시 모델" 행을 확정 결정으로 교체
  - 분류 목록 확정 표시 (`taxonomy/*.toml` 헤더 주석, 기획.md "초안" 섹션을 확정 섹션으로 이동)

**마감 문서**

- `docs/milestones/M3.md`: 평가 결과 요약 표, 결정과 근거 링크, 상태 ✅
- `docs/README.md`: 현황과 "지금 할 일" → M4
- `docs/milestones/M4.md`의 "넘어온 항목"
  - 기본 모델, 예상 비용, Batch API 검토 여부
  - 기존 M1 20편을 새 프롬프트로 다시 추출해야 한다는 점
- 검색 관련 관찰이 있으면 `docs/milestones/M5.md`의 관찰 기록에 쌓는다.
- `CLAUDE.md` 명령어 절에 평가 명령(`eval/*.py`, `--out-dir`, `all`)을 추가한다.

## 재사용할 기존 코드

| 코드 | 쓰는 곳 |
| --- | --- |
| `pipeline/extract/store.py` `Store(posts_path, entries_path)` | run별 저장 |
| `pipeline/extract/extractor.py` `extract_post`, `OpenAILLM`, `LLM` Protocol | 추출 실행, 채점기 호출 패턴 |
| `pipeline/extract/evidence.py` `SourceText`, `normalize` | 완화 모드 구현, 버린 대안 원문 확인 |
| `pipeline/extract/text.py` `html_to_text` | 평문 길이, 채점 입력 |
| `pipeline/collect/raw.py` `load_all` | 표본 추출 |
| `pipeline/normalize` `renormalize` | 미등록 기술 리포트, 정답 기술명 정규화 |
| `techblog_mcp.taxonomy` | 정답셋 값 검증 |

## 검증 (전 과정 공통)

- 브랜치마다 `uv run ruff check`, `uv run ruff format --check`, `uv run pytest`를 통과시킨다.
- `--python 3.11` 격리 테스트도 CI 기준에 맞춘다.
- 추출 도구 변경 확인
  - M1 20편에 `--out-dir`로 소량 실행(`--limit 2`)해 run 디렉터리 구조, 사용량 기록, 기존 `data/` 불변을 확인한다.
  - API 호출이 드는 실행은 매번 예상 비용을 먼저 알린다.
- 평가 스크립트는 가짜 run·정답셋 단위 테스트 뒤, baseline run으로 리포트가 생성되는지 확인한다.
- 마감 전: 결정된 모델로 만든 파일럿 결과를 `pipeline.build_index --entries`로 색인하고 MCP 서버로 검색해 본다. 서버 enum과 분류 목록이 맞는지도 `tests/test_taxonomy.py`로 확인한다.

## 이번 세션 바로 다음 단계

1. `main` 최신 확인 후 `feat/m3-pilot-eval` 브랜치 생성
2. 0번 사전 정리를 커밋: plansDirectory 설정, 플랜 파일 복사, commit.md·CLAUDE.md 브랜치 규칙
3. 1번 작업 구현과 테스트, 커밋 (push는 지시가 있을 때만)
