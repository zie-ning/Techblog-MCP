# 추출 정답셋 검수표

`uv run python eval/gold.py review`로 생성한다. 기준 데이터는 같은 폴더의 JSON이고 이 파일은 보기용이다. 원문과 대조해 고칠 점이 있으면 JSON을 고치고, 검수를 마친 글은 JSON의 `reviewed`를 `true`로 바꾼다.

## d2/1155434 — 검수 전

[C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가](https://d2.naver.com/helloworld/1155434)

- 글 유형: 개념·튜토리얼
- 구조화 유형: **인사이트** (허용: 제외)
- 판단 근거: 팀이 코드 리뷰에서 겪은 문제로 시작하지만 본문 대부분이 언어 기능 의미론 설명이고 적용 결과가 없음. 실무 판단 기준을 주므로 인사이트, 개념 설명으로 보고 제외해도 맞다고 봄. 사례로 보기는 어려움(해결 결정과 결과가 없음)

### 항목 1. 바이트 패턴을 해석할 때 값 재해석은 std::bit_cast, 포인터 변환·바이트 접근·포인터↔정수 변환은 reinterpret_cast를 쓰는 기준

- 주 문제 유형: 개발 생산성
- 도메인: 범용 (허용: 사내 플랫폼·개발 도구)
- 기술: C++
- 핵심 사실:
  - 분산 DB(Dot) 스토리지 계층을 개발하며 바이트 패턴을 타입으로 해석하는 일이 잦음
  - 포인터에 std::bit_cast를 쓰면 const가 경고 없이 제거되고 역참조 시 엄격한 앨리어싱 규칙 위반
  - 타입 퍼닝은 memcpy·std::bit_cast가 표준상 안전하고 reinterpret_cast·union 역참조는 UB
  - 포인터↔정수 왕복 변환은 reinterpret_cast만 표준이 보장

## d2/6512234 — 검수 전

[스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기](https://d2.naver.com/helloworld/6512234)

- 글 유형: 기술 선택·도입형
- 구조화 유형: **사례**
- 판단 근거: 하나의 마이그레이션을 단계적으로 푼 글이라 사례 1개. 이중 쓰기 / 성능·정합성 검증 / 트러블슈팅으로 2~3개로 나눠도 무방. 정량 결과는 Oracle 세션·메모리 감소와 API 지연 개선(수치 없음)

### 항목 1. 여러 파트가 공유하던 Oracle을 회원 파트 MySQL로 양방향 이중 쓰기를 써서 무중단·즉시 롤백 가능하게 전환

- 주 문제 유형: DB 마이그레이션·샤딩 (허용: 비용 절감, 데이터 정합성·트랜잭션)
- 도메인: 커머스·주문·재고
- 기술: MySQL, JPA, MyBatis, datasource-proxy, Kafka, Apache Airflow, Apache Hive, Spring Batch, HikariCP
- 버린 대안: ChainedTransactionManager·분산 트랜잭션(설계 방식), Oracle·MySQL MyBatis 인터페이스 분리 호출(설계 방식), HTTP 트래픽 복사·Kafka 토픽 복제 부하 검증(설계 방식)
- 핵심 사실:
  - 공용 Oracle의 리소스 경합으로 성능이 불안정하고 확장하면 라이선스 비용이 커서 MySQL로 이전
  - 타 부서 시스템과 연계돼 무중단과 즉시 롤백이 필수 → 전환 전에는 Oracle 주·MySQL 보조, 전환 후에는 반대 방향으로 이중 쓰기
  - JPA는 datasource-proxy로 트랜잭션 중 쿼리를 모았다가 커밋 후 MySQL에 실행하고 실패는 무시 (MySQL이 검증되기 전이라 ChainedTransactionManager로 묶지 않음)
  - MyBatis는 MySQL 문법 XML을 한 벌 더 만들고 SqlSessionFactory 프록시로 비즈니스 코드 수정 없이 양쪽에 쓰기
  - Read 호출의 메서드·파라미터를 Kafka로 보내 MySQL에서 재실행해 성능 검증(HTTP 트래픽 복사는 타 부서 중복 호출 위험)
  - Airflow·Hive로 두 DB를 주기 비교하며 약 6개월간 불일치를 제거하고 약 3개월 QA
  - MySQL이 최적화하지 못하는 OR 조건(Index Merge)과 다중 PK 페이징 쿼리는 UNION으로 튜닝

## d2/8992409 — 검수 전

[DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기](https://d2.naver.com/helloworld/8992409)

- 글 유형: 회고·문화·행사
- 구조화 유형: **제외**
- 판단 근거: NAVER ENGINEERING DAY 발표 영상 소개 글. 본문은 발표 내용 3줄·발표 대상·목차뿐이고 해결 근거(수치, 비교, 설계 결정 이유)가 없음. 글 유형은 발표 주제로는 기술 선택·도입형이지만 본문이 행사 발표 소개라 회고·문화·행사로 봄. gpt-5-mini가 v2·v3에서 계속 사례로 만든 글

## kakao/762 — 검수 전

[생산성 혁신의 실험: AI 마일리지 프로그램](https://tech.kakao.com/posts/762)

- 글 유형: 실험·활용기
- 구조화 유형: **인사이트** (허용: 사례)
- 판단 근거: AI 도구 도입 경험이 주제라 제외는 아님. 설문 수치는 많지만 기술적 선택과 그 결과(문제-해법 쌍)는 약하고 활용 패턴·교훈 위주라 인사이트, 근거 있는 실험·활용기로 보고 사례도 허용

### 항목 1. 개발자 100여 명에게 3개월간 상용 AI 개발 도구 크레딧을 지원해 업무 단계별 효과와 효과를 가르는 실패 패턴을 확인한 시범 운영

- 주 문제 유형: 개발 생산성
- 도메인: 사내 플랫폼·개발 도구 (허용: LLM·AI)
- 기술: Cursor, GitHub Copilot, Claude Code, OpenAI API, Gemini
- 핵심 사실:
  - 약 3개월, 30여 개 조직의 개발자 100여 명이 40여 개 과제에서 월 마일리지 안에서 도구를 자유롭게 사용
  - 인당 평균 3~4개 도구를 조합했고 Claude Code 사용자는 마지막 달에 처음보다 약 2배
  - 3개월 차에 시간이 단축됐다고 답한 비율: 코드 작성 98.0%, 디버깅·테스트 86.3%, 설계 84.2%(1개월 차 대비 21.2%p 상승), 릴리즈 43.1%
  - 68.4%가 이제 AI 도구 없이 개발하기 어렵다고 응답
  - 효과를 떨어뜨린 패턴: 컨텍스트 부족, 사내 플랫폼과의 연동 부족, 러닝 커브, 검증 비용 증가, 이미 자동화된 영역

## kakao/785 — 검수 전

[if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며](https://tech.kakao.com/posts/785)

- 글 유형: 회고·문화·행사
- 구조화 유형: **제외**
- 판단 근거: 사내 행사 패널 토크를 Q&A로 정리한 글. AI 코딩 도구 토큰 절약 팁이 일부 있지만 행사 후기 형식이라 제외(기획.md 대상 글 기준: 행사·토크 후기는 실무 팁이 섞여 있어도 제외)

## kakao/822 — 검수 전

[메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분](https://tech.kakao.com/posts/822)

- 글 유형: 실험·활용기
- 구조화 유형: **인사이트** (허용: 사례)
- 판단 근거: 스트레스 테스트 방법론과 AI 도구 활용 노하우가 중심이고 구체적인 문제-결정-결과 쌍(수치로 확인된 개선)은 약해 인사이트. 스킬 자동화 부분을 사례로 볼 수도 있어 사례 허용

### 항목 1. 카카오톡 메시징 서버의 상시 스트레스 테스트 환경 구성·지표 분석 순서·의사결정 원칙과, 반복되는 테스트 라운드를 Claude Code 스킬·서브에이전트로 자동화한 경험

- 주 문제 유형: 테스트 자동화 (허용: 트래픽 급증 대응, 개발 생산성)
- 도메인: 채팅·메시징 서비스 (허용: 사내 플랫폼·개발 도구)
- 기술: Locust, Claude Code, Grafana, Netty
- 핵심 사실:
  - 테스트 서버는 운영과 같은 스펙으로 두고 Locust 워커를 수백 파드로 늘려 클라이언트 병목을 없앰
  - 평시 정오와 신년 자정의 프로토콜 비율이 달라(메시지 전송 52% → 61%) 시나리오를 나눠 테스트
  - endpoint 지표 → 시스템 자원 → JVM 런타임 → 객체 수준(heap dump, 프로파일링) 순으로 내려가며 분석, heap 점유 → GC → CPU → executor 큐 → readTimeout으로 이어진 병목 사례
  - 한 실험에 한 변수만 바꾸고 대당 RPS 기준으로 비교
  - 한 라운드 약 50분을 10번 넘게 반복하던 배포·부하·지표 캡처·보고서 작업을 스킬로 묶고 지표 수집을 서브에이전트로 병렬화
  - 배포 스킬이 이미지 캐시 때문에 새 이미지를 올리지 못했는데 AI 보고서는 '아주 좋음'으로 판정 → 성공·검증 기준을 사람이 명시해야 함

## kakaopay/katfun-joy-kotlin — 검수 전

[코틀린, 저는 이렇게 쓰고 있습니다](https://tech.kakaopay.com/post/katfun-joy-kotlin/)

- 글 유형: 실험·활용기
- 구조화 유형: **인사이트**
- 판단 근거: 서로 독립된 코틀린 활용 팁 4개를 소개하는 글이라 기획.md 기준에 따라 인사이트 1개. gpt-5-mini가 같은 프롬프트에서도 사례 4개/인사이트 1개를 오가는 글

### 항목 1. 보험 서비스 백엔드에서 value class·invoke 팩토리, 불변성·스마트 캐스트, 확장 함수 라이브러리, data class copy()로 안정성과 테스트 가독성을 높이는 코틀린 활용법

- 주 문제 유형: 개발 생산성 (허용: 테스트 자동화)
- 도메인: 결제·금융 (허용: 범용)
- 기술: Kotlin, Jackson
- 버린 대안: 검증 로직 별도 클래스 분리(설계 방식)
- 핵심 사실:
  - value class에 private 생성자와 invoke 연산자 오버로딩을 써서 생성 시 검증을 강제 (검증 로직을 별도 클래스로 두면 호출 누락 위험)
  - @JsonCreator로 역직렬화 때도 검증하는 팩토리 메서드를 거치게 함
  - val 불변성과 requireNotNull 뒤 스마트 캐스트로 null이 아님을 보장
  - 확장 함수와 object declaration으로 공통 유틸 라이브러리를 만들어 프로젝트 간 중복 코드 감소
  - data class copy()로 테스트 대상 필드만 바꿔 테스트 의도를 드러냄

## kakaopay/pallas-v2-log-platform — 검수 전

[일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트](https://tech.kakaopay.com/post/pallas-v2-log-platform/)

- 글 유형: 기술 선택·도입형
- 구조화 유형: **사례**
- 판단 근거: 수집·큐·처리·저장·아카이빙·장기 조회·UI 7단계지만 하나의 문제(로그 플랫폼 확장)를 단계적으로 푼 것이라 사례 1개. 단계별로 2~4개 사례로 나눠도 무방. 기존에 쓰다 교체한 기술(Filebeat, Fluentd, OpenSearch, Athena)도 글에 버린 이유가 명시돼 버린 대안으로 봄. 사내 도구(ssak3)는 technologies에서 뺌

### 항목 1. 하루 41TB로 늘어난 로그의 유입 지연·조회 지연·비용 문제를 수집부터 조회까지 ClickStack(OpenTelemetry + ClickHouse + HyperDX)으로 다시 설계해 해결

- 주 문제 유형: 모니터링·관측성 (허용: 비용 절감, 데이터 파이프라인)
- 도메인: 사내 플랫폼·개발 도구 (허용: 결제·금융)
- 기술: ClickHouse, OpenTelemetry, HyperDX, Kafka, Amazon S3, Grafana
- 버린 대안: OpenSearch(기술), Grafana Loki(기술), Signoz(기술), Amazon Athena(기술), Fluentd(기술), Filebeat(기술), 파티션 수와 컨슈머 수 일치(설계 방식)
- 핵심 사실:
  - 3년 사이 로그가 하루 약 100GB에서 41TB·200억 건으로 늘고(410배) 조회 5분 이상·유입 지연, OpenSearch 비용은 8배 이상 증가
  - Filebeat → OpenTelemetry(OTLP Proto, 배치 전송)로 처리량 16.5MB/s → 300MB/s, Kafka CPU 2배 이상 감소
  - Kafka 토픽 약 300개 → 18개, 파티션 150개에 컨슈머 15·30·50개(평시 20% 자원 손실을 감수하고 09:00·23:30 증권 트래픽 스파이크 때 컨슈머만 늘려 대응)
  - Fluentd 1,000여 개 Pod → OpenTelemetry 150개, 코어당 150건/초 → 4,000건/초, Fast/Common/Debug 레벨별 Pool로 우선순위 처리
  - 조회의 90% 이상이 시간 범위+필드 조건 검색이라 전문 검색이 약해도 컬럼형 ClickHouse 선택 (OpenSearch는 비용·집계, Loki는 라벨 제약·집계 부족으로 제외)
  - IDC ClickHouse는 9일 보관, 이후 자체 도구로 S3 Parquet+ZSTD 아카이빙, 장기 조회는 필요할 때만 띄우는 AWS ClickHouse가 S3를 직접 조회
  - 결과: 로그 지연 20초 이내, 초당 83만 건 처리, 전체 비용 85.6% 절감(저장소 78%, 처리기 96%)

## kakaopay/tech-strategy-tpm — 검수 전

[카카오페이 TPM은 어떤 일을 하나요?](https://tech.kakaopay.com/post/tech-strategy-tpm/)

- 글 유형: 회고·문화·행사
- 구조화 유형: **제외**
- 판단 근거: TPM 직무 소개 인터뷰. 방화벽 작업·안정화 프로젝트 언급은 있으나 기술적 해결 내용이 없음

## kurly/access-block-2 — 검수 전

[nginx 설정 없이 우아하게 서비스 점검하기 (下)](https://helloworld.kurly.com/blog/access-block-2/)

- 글 유형: 기술 선택·도입형
- 구조화 유형: **사례**
- 판단 근거: 물류센터 업무 시스템(클러스터·창고·PDA)이라 도메인은 배달·물류, 사내 운영 도구로도 볼 수 있음. 주 문제 유형은 정확히 맞는 분류가 없어 운영 자동화로 둠

### 항목 1. 서비스 점검 때 nginx 설정 없이 경로·클러스터·권한 단위로 화면과 API 접근을 막는 기능을 구글 시트·BigQuery 메타데이터와 Redis 캐시, Spring AOP로 구현

- 주 문제 유형: 업무·운영 자동화 (허용: 장애 대응·복구, API 설계·외부 연동)
- 도메인: 배달·물류 (허용: 사내 플랫폼·개발 도구)
- 기술: Redis, BigQuery, Google Sheets, Spring AOP, Vue.js
- 버린 대안: nginx 설정으로 접근 차단(설계 방식), BigQuery 직접 조회(설계 방식), 호출 횟수 기반 동기화(설계 방식)
- 핵심 사실:
  - nginx가 앞단 리버스 프록시가 아니고 게이트웨이도 없으며 nginx 설정은 인프라팀이 도커 베이스 이미지로 관리해 nginx 차단이 맞지 않음
  - 개발자가 아닌 기획자·QA·운영 담당자도 차단을 설정할 수 있어야 하고 업무 RDBMS에 종속되면 안 됨
  - 메타데이터는 구글 시트 → BigQuery에 두고 3분마다 배치로 Redis에 동기화 (BigQuery는 작은 쿼리도 수백 ms라 직접 조회하지 않음)
  - 실행데이터는 API로 Redis에 바로 등록·삭제하고 클러스터·창고·제외 권한 단위로 차단
  - 화면은 VueRouter beforeEach, API는 Spring AOP로 모든 요청을 가로채 차단

## kurly/claude-code-redesign-my-day — 검수 전

[클로드 코드로 개발 팀장의 하루를 재설계한 이야기](https://helloworld.kurly.com/blog/claude-code-redesign-my-day/)

- 글 유형: 실험·활용기
- 구조화 유형: **사례** (허용: 인사이트)
- 판단 근거: AI 도구 활용 경험 글이지만 문제-결정-결과(MCP 직접 조회의 비용 문제 → 수집 스크립트 분리)와 수치가 있어 사례. 근거가 대부분 정성적이라 인사이트도 허용. 라운드테이블(페르소나 토론)은 기술적 결정이 약해 항목으로 만들지 않음. 항목 1~3개 모두 무방

### 항목 1. 여러 시스템을 돌며 정리하던 데일리 브리핑을 클로드 코드로 자동화하면서, MCP 직접 조회의 토큰 비용 문제를 수집 스크립트 분리로 해결

- 주 문제 유형: 개발 생산성 (허용: 업무·운영 자동화, 비용 절감)
- 도메인: 사내 플랫폼·개발 도구 (허용: LLM·AI)
- 기술: Claude Code, Slack, Jira, Confluence
- 버린 대안: AI가 MCP로 외부 시스템 직접 조회(설계 방식)
- 핵심 사실:
  - 첫 버전은 MCP로 슬랙·Jira·Confluence를 매번 직접 조회해 2~3일치만 수집해도 토큰 비용과 속도가 급격히 나빠짐
  - 수집은 스크립트로 파일에 저장하고 AI는 요약·판단·페이지 생성만 맡겨 수집 단계 토큰을 거의 안 쓰고 속도와 결과 일관성이 올라감
  - 브리핑 생성을 수집 → 사람·과제별 요약 → 페이지 생성 → 업로드 4단계로 나눠 세션마다 결과가 달라지는 문제를 해결
  - 브리핑은 15분이면 읽는 분량이고 하루 1시간 가까이를 확보

### 항목 2. 10개 넘는 클로드 코드 워크플로에 같은 교정을 반복하던 문제를 공통 규칙 프로젝트와 세션 마무리 자기개선 루프로 해결

- 주 문제 유형: 개발 생산성
- 도메인: 사내 플랫폼·개발 도구 (허용: LLM·AI)
- 기술: Claude Code
- 핵심 사실:
  - 워크플로가 10개 넘게 늘면서 같은 교정을 워크플로마다 반복해야 했음
  - 각 프로젝트 CLAUDE.md 맨 위에 공통 규칙·보조 규칙을 import로 걸어 공통 규칙을 고치면 다음 세션부터 모든 워크플로에 반영
  - 세션 마무리마다 규칙 위반·재발·사용자 교정·환경 이슈를 점검해 규칙을 제안하고 승인된 것만 반영
  - 개별 워크플로는 공통 규칙을 직접 고치지 않고 제안함에 올리며, 둘 이상에서 반복되는 것 등을 공통 규칙으로 승격

## kurly/commit-mvcc-set-autocommit — 검수 전

[데이터가 있었는데요, 아니 없어요](https://helloworld.kurly.com/blog/commit-mvcc-set-autocommit/)

- 글 유형: 문제 해결형
- 구조화 유형: **사례**
- 판단 근거: 성능 개선(auto-commit false)은 글 끝 Q&A에 나오지만 독립된 결정과 수치가 있어 별도 항목으로 둠. 한 사례로 합쳐도 무방. 회원마케팅서비스의 멤버십 조회라 도메인은 커머스로 봄

### 항목 1. auto-commit을 끈 커넥션에서 COMMIT이 없어 MVCC 스냅샷이 갱신되지 않아 이미 있는 회원이 간헐적으로 조회되지 않던 문제를 바깥 메서드에 읽기 전용 트랜잭션을 걸어 해결

- 주 문제 유형: 데이터 정합성·트랜잭션 (허용: 장애 대응·복구)
- 도메인: 커머스·주문·재고 (허용: 광고·마케팅, 범용)
- 기술: Amazon Aurora, HikariCP, JPA, MariaDB Connector/J
- 버린 대안: READ COMMITTED 격리 수준(설계 방식), 잠금 읽기(LOCK IN SHARE MODE)(설계 방식)
- 핵심 사실:
  - Aurora MySQL 5.7, REPEATABLE READ, hikari auto-commit false, open-in-view true 환경
  - @Transactional이 없는 JPA 쿼리 메서드는 COMMIT이 없어 Consistent Nonlocking Read 스냅샷이 갱신되지 않고 다른 세션이 넣은 회원을 못 봄(재요청하면 조회됨)
  - open-in-view로 커넥션이 API 끝까지 유지되고 하위 읽기 전용 트랜잭션의 COMMIT 때문에 ROLLBACK도 일어나지 않아 옛 스냅샷이 남음
  - READ COMMITTED는 Phantom Read로 기존 로직에 영향, 잠금 읽기는 락 경합·데드락 우려로 배제
  - 바깥 메서드에 @Transactional(readOnly = true)를 붙여 메서드 종료 COMMIT으로 스냅샷 갱신

### 항목 2. HikariCP auto-commit을 꺼서 트랜잭션 전후의 set autocommit 쿼리를 없애 API 응답을 40% 개선

- 주 문제 유형: DB 성능·쿼리 최적화
- 도메인: 커머스·주문·재고 (허용: 광고·마케팅, 범용)
- 기술: HikariCP, JPA
- 핵심 사실:
  - auto-commit true면 Hibernate가 @Transactional 전후로 set autocommit 쿼리를 추가로 실행
  - auto-commit false로 API 응답 시간을 1.5ms 줄여 약 40% 향상
  - 대신 쿼리 종료 시점에 COMMIT이 실행되는지 직접 확인해야 함(이 글의 장애 원인)

## ly/how-to-evaluate-ai-generated-images-1 — 검수 전

[AI로 생성한 이미지는 어떻게 평가할까요? (기본편)](https://techblog.lycorp.co.jp/ko/how-to-evaluate-ai-generated-images-1)

- 글 유형: 개념·튜토리얼
- 구조화 유형: **제외**
- 판단 근거: 이미지 생성 모델 평가 지표(PSNR, SSIM, IS, FID, CLIP Score 등)를 정리한 개념 글. 팀이 적용한 경험·결과는 후속 편에 있고 이 글에는 없음

## ly/improving-kubernetes-relay-api-server-performance-with-informer — 검수 전

[Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기](https://techblog.lycorp.co.jp/ko/improving-kubernetes-relay-api-server-performance-with-informer)

- 글 유형: 문제 해결형
- 구조화 유형: **사례**
- 판단 근거: 주 문제 유형은 쿠버네티스 운영 성능이라 인프라·컨테이너, Informer 캐시를 쓴 점에서 캐싱도 허용

### 항목 1. 모든 파드 조회 권한 없이 노드별 스케줄링 가능 리소스를 보여 주는 중계 API 서버를 Go 클라이언트의 Informer 캐시로 재구현해 응답 10초를 0.2초로 단축

- 주 문제 유형: 인프라·컨테이너 (허용: 캐싱, 인증·보안, API 설계·외부 연동)
- 도메인: 사내 플랫폼·개발 도구
- 기술: Kubernetes, Go
- 버린 대안: 사용자에게 모든 파드 조회 권한 부여(설계 방식), Kubernetes Python 클라이언트(기술), 다중 스레드 비동기 조회(설계 방식)
- 핵심 사실:
  - 약 800대 노드의 멀티 테넌트 클러스터, 사용자 약 200명, RBAC로 네임스페이스 권한만 부여
  - kubectl describe node는 클러스터 전체 파드 조회 권한이 필요해 최소 권한 원칙상 별도 중계 API 서버를 둠
  - Python 클라이언트로 매번 전체 파드를 조회하면 스레드로 우회해도 리소스 계산에 10초가 걸리고 kube-apiserver·etcd에 부하
  - Python 클라이언트는 Informer를 지원하지 않아(관련 이슈가 4년째 정체) Go로 재구현하고 노드·파드 Informer 캐시에서 조회
  - 800개 노드 계산 시간 10초 → 약 0.2초

## ly/japanese-search-kuromoji-to-sudachi — 검수 전

[일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로](https://techblog.lycorp.co.jp/ko/japanese-search-kuromoji-to-sudachi)

- 글 유형: 기술 선택·도입형
- 구조화 유형: **사례**
- 판단 근거: 분석기 교체와 Multi-field 설계는 문제가 달라 사례 2개로 나눔(1~3개 모두 무방). 적용 후 정량 결과는 없음(검색 로그로 확인 예정). 검색 품질을 다루는 문제 유형이 없어 DB 성능·쿼리 최적화로 둠(분류 목록 공백 후보, M4에서 검토)

### 항목 1. 오래된 IPADIC 사전과 복합어 과분해로 상품명이 검색되지 않던 문제를 Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 바꿔 해결

- 주 문제 유형: DB 성능·쿼리 최적화 (허용: DB 마이그레이션·샤딩)
- 도메인: 검색·추천 (허용: 커머스·주문·재고)
- 기술: OpenSearch, Sudachi
- 버린 대안: Kuromoji 사용자 사전 등록(설계 방식), mecab-ipadic-neologd(기술), Elasticsearch 8.x 업그레이드(설계 방식)
- 핵심 사실:
  - IPADIC 사전은 2007년 이후 업데이트가 멈춰 신조어·고유명사(예: 2001년 등록 쌀 품종명)를 인식하지 못함
  - Kuromoji 기본 설정은 상품명 복합어를 잘게 쪼개 의도와 다른 상품이 검색됨
  - 단어가 보고될 때마다 사용자 사전에 추가하던 방식은 신조어·복합어·모델명 변형을 감당하지 못함
  - 사내 검색 플랫폼은 Elasticsearch 7.10.2에서 일몰하고 OpenSearch 2.4.1/2.15.0을 지원해 Sudachi 플러그인(2.6 이상)을 쓸 수 있는 2.15.0 선택
  - Sudachi 기본 C 모드로 복합어·고유명사를 한 토큰으로 유지해 동의어 확장도 안정적으로 동작

### 항목 2. 형태소 분석으로 풀 수 없는 모델 번호·구분자 표기 차이와 자동완성을 인덱스 규모에 맞춘 Multi-field(compact, edge n-gram) 설계로 해결

- 주 문제 유형: DB 성능·쿼리 최적화
- 도메인: 검색·추천 (허용: 커머스·주문·재고)
- 기술: OpenSearch
- 버린 대안: 상품 인덱스에 Edge N-gram 적용(설계 방식)
- 핵심 사실:
  - 상품 인덱스 약 8억 건, 카탈로그 인덱스 약 1억 건
  - 모델 번호(AW-10DP3, aw10dp3 등)는 구분자를 공백으로 바꾸고 whitespace tokenizer로 자르는 compact 서브 필드로 같은 토큰에 수렴
  - 짧은 일본어 검색어에 compact 필드를 쓰면 노이즈가 생겨 영숫자가 들어간 3자 초과 검색어에만 사용
  - Edge N-gram 자동완성은 정제된 카탈로그 인덱스에만 두고, 8억 건 비정형 상품 인덱스는 인덱스 크기·색인 비용·Kafka 처리 지연 우려로 제외
  - 자동완성 쿼리는 constant_score로 스코어 계산을 생략

## oliveyoung/2023-09-27_oliveyoung-favorite-snack — 검수 전

[올리브영 개발자가 좋아하는 과자는?](https://oliveyoung.tech/2023-09-27/oliveyoung-favorite-snack/)

- 글 유형: 회고·문화·행사
- 구조화 유형: **제외**
- 판단 근거: 사내 간식 설문 결과를 공유하는 조직 문화 글. 기술 내용 없음

## oliveyoung/2024-12-17_catalog-mongo-transaction-2 — 검수 전

[Spring Boot MongoDB 트랜잭션 도입 실전 가이드](https://oliveyoung.tech/2024-12-17/catalog-mongo-transaction-2/)

- 글 유형: 문제 해결형
- 구조화 유형: **사례**
- 판단 근거: 글 앞부분의 MongoDB 트랜잭션 개념 설명(격리 수준, Write Concern 옵션 표)은 항목으로 만들지 않음

### 항목 1. 복제 지연 때문에 트랜잭션 안에서 방금 쓴 데이터를 Secondary에서 못 읽는 문제를 트랜잭션에서만 Primary에서 읽도록 해 해결

- 주 문제 유형: 데이터 정합성·트랜잭션 (허용: DB 성능·쿼리 최적화)
- 도메인: 커머스·주문·재고
- 기술: MongoDB, Spring Boot, Spring Data MongoDB
- 버린 대안: WriteConcern MAJORITY(설계 방식), 전역 ReadPreference PRIMARY(설계 방식)
- 핵심 사실:
  - WriteConcern ACKNOWLEDGED와 ReadPreference secondaryPreferred 조합에서 복제 지연으로 트랜잭션 중 재조회가 Not Found
  - WriteConcern MAJORITY는 모든 요청에서 과반수 응답을 기다려 성능 부담
  - 전역 PRIMARY 읽기는 Secondary 자원을 놀림
  - MongoTransactionManager의 TransactionOptions에만 readPreference primary를 설정

### 항목 2. 트랜잭션 커밋 전에 SQS 메시지가 나가 컨슈머가 데이터를 못 찾는 문제를 커밋 후 이벤트 발행(@TransactionalEventListener)으로 해결

- 주 문제 유형: 데이터 정합성·트랜잭션 (허용: 메시징·비동기 처리)
- 도메인: 커머스·주문·재고
- 기술: Amazon SQS, Spring Framework
- 버린 대안: SQS 메시지 지연 전송(설계 방식), Outbox 패턴(설계 방식)
- 핵심 사실:
  - @Transactional 안에서 SQS로 발행해 커밋 전에 메시지가 나가 컨슈머 조회가 Not Found
  - 지연 전송은 지연이 짧으면 문제가 남는 임시방편, Outbox·로그 테일링은 당장은 설계·구현 비용이 큼
  - ApplicationEventPublisher와 @TransactionalEventListener(AFTER_COMMIT) + @Async로 커밋 후 비동기 발행

## oliveyoung/2025-04-25_web-worker-for-image-processing — 검수 전

[Web Worker로 이미지 처리 최적화하기](https://oliveyoung.tech/2025-04-25/web-worker-for-image-processing/)

- 글 유형: 문제 해결형
- 구조화 유형: **사례**
- 판단 근거: Web Worker·OffscreenCanvas는 제품이 아니라 브라우저 API지만 사례의 핵심 기술이라 technologies에 Web Worker만 넣음. 버린 대안 중 Shared/Service Worker는 기술, 나머지는 설계 방식

### 항목 1. 모바일 고해상도 이미지 업로드 때 메인 스레드 블로킹과 강제 새로고침을 이미지 변환·리사이징을 Dedicated Web Worker로 옮겨 해결

- 주 문제 유형: 클라이언트 성능(웹·앱)
- 도메인: 콘텐츠·미디어 (허용: 커머스·주문·재고)
- 기술: Web Worker
- 버린 대안: WebP 포맷 변환(설계 방식), 메인 스레드 Canvas 리사이징(설계 방식), Shared Worker(기술), Service Worker(기술)
- 핵심 사실:
  - 게시물에 이미지 최대 10장·최대 40MB 업로드, LTE 약 28초·불안정한 네트워크 약 64초 예상
  - 모바일 대용량 이미지는 4MB·4000px 이상이 흔하고 iOS 메모리 제한으로 브라우저 강제 새로고침이 발생
  - WebP 변환은 복잡한 이미지에서 압축 효율이 낮고, Canvas 리사이징은 메인 스레드를 점유해 클릭이 무시됨
  - Shared·Service Worker는 이미지 처리에 불필요한 기능이 많아 Dedicated Worker 선택
  - 2.31MB Base64 변환 기준 처리 시간 388ms → 137ms, 메인 스레드 블로킹 350ms → 8ms

## toss/firesidechat_frontend_4 — 검수 전

[오픈소스에 기여하고 토스에 합격한.ssul | EP.4 모닥불](https://toss.tech/article/firesidechat_frontend_4)

- 글 유형: 회고·문화·행사
- 구조화 유형: **제외**
- 판단 근거: 영상 인터뷰 소개 글. 본문은 소개 문구·라이브러리 링크·타임스탬프뿐이고 기술적 해결 내용이 없음

## toss/toss-frontend-ai-docs — 검수 전

[토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유](https://toss.tech/article/toss-frontend-ai-docs)

- 글 유형: 문제 해결형
- 구조화 유형: **사례** (허용: 인사이트)
- 판단 근거: 문제-해법 쌍과 선택 이유(문서 개선 대신 질문 방식 존중)는 분명하지만 정량 근거가 없어 인사이트도 허용. 박씨·실록봇을 사례 2개로 나눠도 무방(실록봇은 박씨의 지식 기반 확보 수단)

### 항목 1. 문서를 찾느라 개발 흐름이 끊기는 문제를 RAG 챗봇(박씨)과 대화 자동 문서화 봇(실록봇)으로 해결

- 주 문제 유형: 개발 생산성 (허용: 업무·운영 자동화)
- 도메인: 사내 플랫폼·개발 도구 (허용: LLM·AI)
- 기술: RAG
- 버린 대안: 문서를 더 잘 써서 방문 유도(설계 방식)
- 핵심 사실:
  - 관찰·인터뷰 결과 개발자는 문서 검색보다 동료·메신저에 질문하는 방식으로 지식을 얻음
  - RAG 기반 챗봇이 문서를 근거로 답하고 출처를 제공하며 IDE와 사내 메신저에서 쓸 수 있음
  - 메신저 대화 스레드를 AI가 요약해 문서 저장소에 PR을 올리는 봇으로 문서 양을 늘림
  - 특정 팀원에 지식이 몰리거나 같은 질문이 반복되는 문제가 줄었다고 함 (정량 수치 없음)

## toss/toss-securities-gpu-mig — 검수 전

[GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기](https://toss.tech/article/toss-securities-gpu-mig)

- 글 유형: 기술 선택·도입형
- 구조화 유형: **사례**
- 판단 근거: 도입 후 성능·비용 결과는 후속 글로 미뤄져 없음. 클라우드·혼합 GPU는 장단점을 비교한 뒤 자기 조건에 맞지 않아 택하지 않은 대안이라 버린 대안으로 봄

### 항목 1. 작은 ML 워크로드가 고성능 GPU를 낭비하는 문제를 클라우드·혼합 GPU 대신 MIG GPU 가상화로 해결하고 Kubernetes 스케줄링·모니터링을 맞춤

- 주 문제 유형: 비용 절감 (허용: 인프라·컨테이너)
- 도메인: LLM·AI (허용: 사내 플랫폼·개발 도구)
- 기술: NVIDIA MIG, Kubernetes, nvidia-device-plugin, dcgm-exporter, Prometheus, Grafana
- 버린 대안: 클라우드 GPU 활용(설계 방식), 혼합 GPU 운영(설계 방식), MPS(기술)
- 핵심 사실:
  - 전체 워크로드의 약 1/3이 GPU 자원의 1/4도 쓰지 않음
  - H100 하루 대여 약 38만 원, 1/4만 쓰면 월 약 855만 원 낭비(8장 서버 기준 월 6,840만 원)
  - 단일 아키텍처 운용, 추론 속도 일관성, 유연한 자원 전환이 선택 기준이고 클러스터가 대부분 H100/H200이라 MIG 사용 가능
  - MPS는 자원 격리가 어렵고 관리 부담이 커서 하드웨어 격리되는 MIG 선택
  - Kubernetes는 nvidia-device-plugin을 MIG 전략 mixed로 재배포하고 dcgm-exporter로 인스턴스별 SM 사용률을 수집

## woowahan/14671 — 검수 전

[요즘 협업 잘하는 팀은 이렇게 일합니다.](https://techblog.woowahan.com/14671/)

- 글 유형: 회고·문화·행사
- 구조화 유형: **제외**
- 판단 근거: 온보딩·지식 공유·이슈 처리 프로세스 등 팀 협업 방식 글. 슬랙 워크플로·지라 티켓 자동 생성이 나오지만 업무 프로세스 개선이 주제라 제외

## woowahan/17386 — 검수 전

[우리 팀은 카프카를 어떻게 사용하고 있을까](https://techblog.woowahan.com/17386/)

- 글 유형: 기술 선택·도입형
- 구조화 유형: **사례** (허용: 인사이트)
- 판단 근거: 2년 차 개발자가 팀의 카프카 활용을 넓게 소개하는 글이라 인사이트로 볼 수도 있지만, 활용 방식마다 구체적인 문제·결정·이유가 있어 사례 3개로 봄

### 항목 1. 주문·배달 이벤트의 순서와 누락을 키 기반 파티셔닝과 Debezium을 이용한 Transactional Outbox 패턴으로 보장

- 주 문제 유형: 데이터 정합성·트랜잭션 (허용: 메시징·비동기 처리)
- 도메인: 배달·물류
- 기술: Kafka, Debezium, MySQL, Kafka Connect
- 핵심 사실:
  - 하루 100만 건 이상 생성되는 배민배달을 여러 배달 서비스로 분배·중계
  - 주문·배달 식별자를 메시지 키로 써서 같은 파티션·같은 컨슈머가 처리하게 해 순서를 보장
  - DB 저장과 이벤트 발행을 한 트랜잭션으로 묶으려고 outbox 테이블을 binlog CDC(Debezium MySQL source connector)로 발행
  - source connector가 태스크 하나만 써서 처리량이 부족해 토픽별·식별자 기반 N개 outbox 테이블로 분산

### 항목 2. 배달 서버군이 인메모리로 가진 분배 규칙 변경을 카프카 이벤트 버스(Spring Cloud Bus)로 모든 서버에 반영

- 주 문제 유형: 메시징·비동기 처리
- 도메인: 배달·물류
- 기술: Kafka, Spring Cloud Bus
- 핵심 사실:
  - 운영자가 분배 규칙을 바꾸면 이벤트를 소비한 서버만 바뀌고 나머지는 옛 규칙을 유지하는 문제
  - RemoteApplicationEvent로 목적 서버군에 이벤트를 보내고 각 서버가 규칙을 다시 읽음
  - 높은 처리량이 필요 없어 이벤트 버스 토픽은 파티션 1개, 서버마다 다른 컨슈머 그룹으로 모두 수신

### 항목 3. 배달 이벤트를 카프카 스트림즈로 실시간 집계하고 배달 건별 통합 이벤트를 S3·Athena로 분석용 제공

- 주 문제 유형: 데이터 파이프라인 (허용: 모니터링·관측성)
- 도메인: 배달·물류
- 기술: Kafka Streams, Redis, Kafka Connect, Amazon S3, Amazon Athena, Grafana
- 버린 대안: 배치 기반 분석 데이터 제공(설계 방식)
- 핵심 사실:
  - 배치는 실시간 데이터를 반영하기 어려워 카프카 스트림즈 상태 저장소로 배달 상태별 건수 등을 실시간 집계해 그라파나로 시각화
  - 배달 한 건의 여러 이벤트를 Redis에 임시로 모았다가 완료 시 통합 이벤트로 분석 토픽에 발행
  - S3 싱크 커넥터로 분석 토픽을 S3에 영구 저장하고 Athena로 서비스 DB 부하 없이 조회
  - 서비스 토픽과 분석 토픽·서버를 분리해 장애 영향 범위를 나눔

## woowahan/20763 — 검수 전

[이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기](https://techblog.woowahan.com/20763/)

- 글 유형: 기술 선택·도입형
- 구조화 유형: **사례**
- 판단 근거: 언어 전환과 전환 뒤 GC 개선은 문제가 달라 사례 2개로 나눔(한 사례로 묶어도 무방). 주 문제 유형: 전환의 목적은 유지보수성·사내 표준화라 개발 생산성. GC 개선은 JVM 성능 튜닝인데 맞는 문제 유형이 없음(분류 목록 공백 후보, M4에서 검토)

### 항목 1. 배달 주소의 행정동을 판별하는 C++ 서버를 성능을 유지하면서 Java·Spring Boot로 전환하고 Canary 배포를 여러 번 반복해 무장애로 배포

- 주 문제 유형: 개발 생산성 (허용: 배포·CI/CD, MSA)
- 도메인: 배달·물류
- 기술: Java, Spring Boot, S2 Geometry, nGrinder, AWS ALB
- 버린 대안: 캐시 레이어 도입(설계 방식), Blue/Green 배포(설계 방식)
- 핵심 사실:
  - 피크 시간 전체 서버 기준 1분에 80만 건 이상, C++ 서버는 대당 2000TPS 이상을 10ms 이하로 응답
  - C++는 작은 메모리 실수로 서버가 멈출 위험이 있고 팀의 C++ 전문성이 낮으며 사내 배포·모니터링을 적용하기 어려웠음
  - 기존 서버가 싱글스레드 이벤트 루프라 Java 멀티스레드로 성능을 맞출 수 있다고 보고 nGrinder 부하 테스트에서 최대 3500TPS 확인
  - 약 180MB 데이터를 메모리에 올리는 구조는 유지 (캐시 레이어는 비용과 작업량 때문에 보류)
  - 1%·5% Canary와 일시 전면 배포 후 롤백을 반복하고 ALB에 두 TargetGroup을 걸어 1분 안에 롤백할 수 있게 함
  - 결과: 더 적은 비용의 서버로 같은 트래픽 처리, 평균 응답은 1ms 수준으로 소폭 증가

### 항목 2. Java 전환 뒤 힙에 올린 대용량 데이터 때문에 생긴 major GC와 CPU 급증을 fastutil primitive 컬렉션으로 해결

- 주 문제 유형: 인프라·컨테이너 (허용: 장애 대응·복구, 트래픽 급증 대응, 비용 절감)
- 도메인: 배달·물류
- 기술: Java, fastutil
- 버린 대안: Hazelcast(기술), Chronicle Map(기술), HPPC(기술), Trove(기술), Koloboke(기술), GC 파라미터(IHOP) 튜닝(설계 방식)
- 핵심 사실:
  - 전체 데이터가 힙 old 영역에 있어 major GC가 잦고 STW 구간(Remark)이 30~40ms, 주기적 CPU 급증
  - Ramp-up 방식 부하 테스트로는 중간 트래픽을 오래 유지할 때의 CPU 급증을 찾지 못함
  - Hazelcast·Chronicle Map은 단순 조회에 비해 기능이 과하고 진입 장벽이 높아 제외
  - fastutil로 primitive 저장 전환 후 최고 3500 → 3700TPS, 힙 하단 2GB → 1.13GB, 1500TPS 유지 시 major GC 미발생

