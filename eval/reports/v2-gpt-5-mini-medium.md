# 추출 점검 리포트: v2-gpt-5-mini-medium

- 모델: gpt-5-mini (medium)
- 프롬프트 버전: 44b7d89476c5
- 글 80편: 사례 58, 인사이트 3, 제외 19
- 항목 83개: 사례 80, 인사이트 3
- 토큰: 호출 161회, 입력 1,249,619 (캐시 431,744), 출력 551,140 (reasoning 424,512)
- 비용: $1.318 (편당 $0.0165), 전체 1,262편 추정 $20.8 / Batch $10.4

## 블로그별 구조화 유형

| 블로그 | 사례 | 인사이트 | 제외 | 항목 수 |
| --- | --- | --- | --- | --- |
| d2 | 7 | 0 | 3 | 10 |
| kakao | 5 | 2 | 3 | 8 |
| kakaopay | 8 | 0 | 2 | 18 |
| kurly | 10 | 0 | 0 | 13 |
| ly | 8 | 1 | 1 | 10 |
| oliveyoung | 6 | 0 | 4 | 7 |
| toss | 6 | 0 | 4 | 6 |
| woowahan | 8 | 0 | 2 | 11 |

## 글 유형 × 구조화 유형

| 글 유형 | 사례 | 인사이트 | 제외 |
| --- | --- | --- | --- |
| 개념·튜토리얼 | 0 | 0 | 4 |
| 기술 선택·도입형 | 34 | 0 | 0 |
| 문제 해결형 | 15 | 0 | 0 |
| 실험·활용기 | 9 | 0 | 0 |
| 회고·문화·행사 | 0 | 3 | 15 |

## 짧은 글 (평문 1,500자 미만) 8편

| 글 | 길이 | 결과 | 항목 | 분류 이유 |
| --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | 0 | 발표 세션의 공개 안내 및 목차/요약 형태의 글입니다. 다뤄진 주제(알고리즘, 아키텍처, 비교 등)는 기술적이지만 본문에 구체적인 문제 해결 과정·설계 근거·수치적 결과나 적용 사례가 제시되어 있지 않아 실무에 바로 적용 가능한 사례나 인사이트로 분류하기 어렵습니다. 따라서 '제외'로 판단합니다. |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | 0 | 발표(세션) 형식으로 C++의 동시성 개념(데이터 레이스, happens-before, basic thread safety 등)을 정리·설명하는 교육·개념 설명 중심 글입니다. 특정 실무 사례, 도입 판단, 실험 결과나 수치적 근거가 제시되어 있지 않아 기술 사례 데이터베이스의 '사례'나 '인사이트'로 활용하기 어렵습니다. |
| d2/8992409 | 1,342 | 사례/기술 선택·도입형 | 1 | DBT와 Airflow를 도입해 Flow.er라는 on‑demand 데이터 계보 중심 파이프라인을 설계·구현한 경험을 다루며, 과거 파이프라인의 문제(백필·복구 비용 등), POC, 구성 요소, DBT/Airflow의 역할, CI/CD, 확장 및 개선사항(Partition Checker 등)을 구체적으로 설명합니다. 기술 선택과 구현 근거(설계·구성 요소·운영 개선)가 포함되어 있어 다른 팀의 설계 판단에 참고 가능한 사례입니다. |
| d2/9290861 | 796 | 제외/회고·문화·행사 | 0 | 발표 세션 소개와 목차 중심의 글로, VictoriaMetrics 내부 구조를 다루긴 하지만 구체적인 문제·해법, 구현 세부사항, 적용 결과나 수치가 제공되지 않아 실무에 바로 적용 가능한 기술 사례로 보기에 부족함. |
| kakao/624 | 787 | 제외/회고·문화·행사 | 0 | 발표 영상 공유 및 발표자 인터뷰 중심의 행사(테크밋) 소개글로, 구체적인 기술 문제·해결 과정이나 설계·적용 근거(수치·비교·코드 등)가 제공되지 않음. 실무 적용 가능한 기술 사례가 없어 제외로 분류함. |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | 0 | 사내 간식 설문 결과와 조직 문화 관련 공유 글입니다. 기술적 문제 해결·도입 판단·실무 적용 팁 등이 없어 기술 사례 데이터베이스에 포함할 실질적 내용이 없습니다. |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | 0 | 인터뷰 형식의 영상/에피소드 요약으로 오픈소스 기여 경험과 채용·성장 이야기를 중심으로 구성됨. 라이브러리 목록과 일반적 조언은 있으나 구체적 기술 문제·해결 과정, 설계 근거(수치·비교)나 실무 적용 팁이 부족해 기술 사례 데이터베이스로 활용할 만큼의 기술적 내용은 아님. |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | 0 | 인터뷰/대담 형식으로 개발자 리더십·조직 성장·피드백 등 문화·경험을 논의하는 내용입니다. 구체적 기술 문제 해결이나 도구·설계 적용 사례, 실무 적용 팁이 없으므로 기술 사례 데이터베이스의 대상(사례/인사이트)이 아닙니다. |

## 글당 항목 수 (제외 글 빼고)

| 항목 수 | 글 수 |
| --- | --- |
| 1 | 48 |
| 2 | 6 |
| 3 | 5 |
| 4 | 2 |

## 주 문제 유형 분포

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 개발 생산성 | 19 | 23% |
| 인증·보안 | 6 | 7% |
| 데이터 정합성·트랜잭션 | 6 | 7% |
| API 설계·외부 연동 | 6 | 7% |
| 배포·CI/CD | 6 | 7% |
| 클라이언트 성능(웹·앱) | 5 | 6% |
| 인프라·컨테이너 | 5 | 6% |
| 데이터 파이프라인 | 4 | 5% |
| 업무·운영 자동화 | 4 | 5% |
| 모니터링·관측성 | 4 | 5% |
| 비용 절감 | 3 | 4% |
| 트래픽 급증 대응 | 3 | 4% |
| 메시징·비동기 처리 | 3 | 4% |
| 장애 대응·복구 | 2 | 2% |
| MSA | 2 | 2% |
| 테스트 자동화 | 2 | 2% |
| DB 성능·쿼리 최적화 | 1 | 1% |
| 캐싱 | 1 | 1% |
| DB 마이그레이션·샤딩 | 1 | 1% |

- 한 번도 안 쓰인 분류 (1개): 동시성·락

## 도메인 분포

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 사내 플랫폼·개발 도구 | 32 | 39% |
| 범용 | 13 | 16% |
| 커머스·주문·재고 | 11 | 13% |
| LLM·AI | 8 | 10% |
| 검색·추천 | 5 | 6% |
| 결제·금융 | 4 | 5% |
| 배달·물류 | 4 | 5% |
| 콘텐츠·미디어 | 3 | 4% |
| 채팅·메시징 서비스 | 2 | 2% |
| 광고·마케팅 | 1 | 1% |

- 쏠림(30% 초과): 사내 플랫폼·개발 도구
- 한 번도 안 쓰인 분류 (0개): 없음

## 발췌 검증

- 채택한 시도 기준 발췌 887개 중 탈락 8개 (원문 존재율 99%)
- 재시도한 글 20편

- `kakao/770`: - Webpack에서만 지원되는 사내 Sentry 플러그인을 제거 및 cli로 변경
- `kurly/refine-address-internalization-2`: 제 기억에 이 때 까지는 외부 업체와의 계약 종료라는 목표는 뭔가 멀게만 느껴지는 목표였고, 일단 외부업체 api 호출 비용이라도 가능한 최소한으로 줄여보자는 목표로 계획을 세웠습니다.
- `ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot`: 저희는 ArgoCD의 Sync 기능으로 배포가 가능했으며 이를 Hubot이 호출할 수 있게 연계하면 배포가 가능할 것이라고 생각했습니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 처음에는 관련 키워드를 모두 블랙리스트로 구성해서 이와 일치하거나 부분 문자열로 포함하는 단어는 트렌딩 키워드로 추출되지 않도록 만들어 봤습니다. 그랬더니 미처 예상치 못했던 단어들이, 예를 들어 오랜만에 경기가 열리는 지방 도시 이름이라던가 말이나 기수 또는 참가 팀 이름 등 미리 지정하는 게 사실상 불가능한 단어들이 걸러지지 못하고 추천 키워드로 추출됐습니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 검토 결과 다양성이 충분히 확보되는 편이 바람직하다고 의견이 모여 페널티 가중치가 2 이상인 구간에서 α값을 결정했습니다.
- `ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status`: 온콜에서 수신하는 알람을 그대로 반영할 것인지 혹은 오류 예산 기반으로 표현할 것인지 등을 검토했는데요.
- `ly/japanese-search-kuromoji-to-sudachi`: compact_product_name_analyzer는 icu_normalizer → model_delim_to_space(커스텀 char_filter: -, _, / → 공백 변환) → punct_to_space(커스텀 char_filter: 나카구로·물결표 등 → 공백 변환) → collapse_spaces(커스텀 char_filter: 연속 공백   → 단일 공백)를 거친 뒤 whitespace tokenizer로 분리합니다.
- `woowahan/24999`: 사용자 입력 시퀀스를 받아 게임을 시뮬레이션하여 점수를 계산하는 것은 다항 시간에 가능하지만 원하는 점수에서 입력을 찾는 것은 물리 엔진 전체를 역산해야 하므로 NP-Hard입니다.

## 기술 사전에 없는 이름 148종

- Locust (3)
- Jira (3)
- LLM (3)
- GitHub (2)
- SWC (2)
- Web Worker (2)
- Milvus (2)
- Netty (2)
- C++ (2)
- Vite (2)
- Storybook (2)
- esbuild (2)
- Rollup (2)
- Babel (2)
- ZSTD (2)
- Wallga (2)
- HDFS (2)
- Confluence (2)
- Hubot (2)
- hubot-conversation (2)
- Spring Data MongoDB (2)
- Figma (1)
- Token Studio (1)
- Style Dictionary (1)
- CSS (1)
- ESBuild (1)
- react-refresh (1)
- WebSocket (1)
- MIG (1)
- nvidia-device-plugin (1)
- dcgm-exporter (1)
- nvidia-smi (1)
- H100 (1)
- NVLink (1)
- HTML (1)
- Node2Vec (1)
- Transformer (1)
- pgvector (1)
- Atlas MongoDB (1)
- WASM (1)
- Rust (1)
- S2 (1)
- fastutil (1)
- AWS ALB (1)
- jstat (1)
- IPsec (1)
- LTE 라우터 (1)
- Virtual Thread (1)
- ForkJoinPool (1)
- Spring Cloud (1)
- AWS Athena (1)
- Kanana-2 (1)
- MLA (1)
- MoE (1)
- JMH (1)
- JFR (1)
- async-profiler (1)
- jstack (1)
- Codex (1)
- v0 (1)
- Supabase (1)
- Vercel (1)
- Veo3 (1)
- Flowith (1)
- Claude API (1)
- IntelliJ (1)
- Webpack (1)
- Vitest (1)
- AttributeConverter (1)
- UserType (1)
- ParameterizedType (1)
- AWS KMS (1)
- CloudTrail (1)
- reach.tech (1)
- OpenSearch Dashboards (1)
- Apache Lucene (1)
- HyperDX (1)
- Parquet (1)
- InfluxDB (1)
- Mongo (1)
- Spinnaker (1)
- DBT (1)
- Clang-Tidy (1)
- datasource-proxy (1)
- Hive (1)
- Release Please Action (1)
- Dokka (1)
- vanniktech gradle maven publish plugin (1)
- JFrog Artifactory (1)
- Maven Central (1)
- GitHub Pages (1)
- Ruler (1)
- Nexus (1)
- JuiceFS (1)
- JuiceFS CSI Driver (1)
- nubes (1)
- MinIO (1)
- Sudachi (1)
- Edge N-gram (1)
- ICU (1)
- LINE (1)
- Iceberg (1)
- WebAuthn (1)
- CTAP (1)
- MinHash (1)
- NPMI (1)
- MMR (1)
- Z-test (1)
- Slack Workflow (1)
- Ansible (1)
- Harbor (1)
- Vector (1)
- Graphviz (1)
- Akamai (1)
- node_exporter (1)
- kube-state-metrics (1)
- client-go (1)
- Informer (1)
- Kubernetes Python client (1)
- WebView (1)
- Taskmaster (1)
- MobX (1)
- Material-UI (1)
- dayjs (1)
- react-csv (1)
- qs (1)
- Google Sheets (1)
- BigQuery (1)
- Vue Router (1)
- Swagger (1)
- Postman (1)
- mysql-connector-j (1)
- MemoryAnalyzer (1)
- AWS EC2 (1)
- 행안부 도로명주소조회 API (1)
- 행안부 좌표정보 API (1)
- MariaDB Connector/J (1)
- BERT4Rec (1)
- gradio (1)
- mlflow (1)
- mitmproxy (1)
- OffscreenCanvas (1)
- Yarn (1)
- Panda CSS (1)
- Tokens Studio For Figma (1)
- token-transformer (1)
- Jotai (1)
- AWS ECR (1)

## 버린 대안 92개 (사례 80개 중)

- `case_0001` 부분적인 팔레트 수정: 일부 토큰만 수정하면 팔레트 전체와 다크모드까지 영향을 주어 문제가 해결되지 않음.
- `case_0003` 클라우드 활용: 장기적 지속 워크로드나 컴플라이언스 환경에서 제약
- `case_0003` 혼합 GPU 운영: 수요 예측 어려움으로 자원 낭비 우려
- `case_0003` MPS: 격리·모니터링이 어려움
- `case_0004` Virtual Scrolling: UX가 페이지네이션(100건) 기반이라 적용하지 않음
- `case_0004` IndexedDB 캐싱: 무효화 판단 불명확·요구 대비 과함·부수 비용으로 보류
- `case_0008` Atlas MongoDB: 부하 상황에서 CPU 포화로 응답 지연·처리량 한계가 확인되어 2차 실험 최종 선택은 아님.
- `case_0008` OpenSearch: 부하에서 시스템 한계로 API 성능이 더 이상 개선되지 않고 요청 실패가 발생함. **(technologies에도 있음)**
- `case_0008` Milvus: 1차 실험에서는 기능 검증 대상이었지만 2차 성능 시험 후보로는 선정되지 않음.
- `case_0008` Redis Stack: 1차 실험에서 검토했으나 2차 실험 후보로는 최종 선정되지 않음.
- `case_0008` Pinecone (managed vector DB): 사내 도입·운영 주체 부재와 신규 비용 계약 이슈로 1차 후보군에 포함하지 않음.
- `case_0009` 코드 난독화: 코드 난독화로는 근본적 방어가 되지 않음
- `case_0009` CAPTCHA: 매크로는 막았지만 게임 재미가 크게 훼손됨
- `case_0009` 클라이언트 점수 전송: 클라이언트가 점수를 전송하면 해킹이 극도로 쉬워짐
- `case_0010` 완벽한 실시간 반영: 실시간 고집 시 데이터베이스 병목·부하 증가 우려
- `case_0011` 캐시 레이어: 캐시/DB 레이어 도입은 비용 및 작업량 증가로 인해 채택하지 않음
- `case_0011` Redis: 캐시 레이어(예: Redis)를 검토했으나 2안(메모리 유지)을 선택하여 도입하지 않음
- `case_0011` hazelcast: in-memory data grid는 기능이 과하고 진입 장벽이 높아 채택하지 않음
- `case_0011` chronicle-map: 힙 외부 저장 등 장점이 있으나 기능이 과해 채택하지 않음
- `case_0011` HPPC: primitive 컬렉션들 중 fastutil을 선택하여 대체함
- `case_0011` trove: primitive 컬렉션들 중 fastutil을 선택하여 대체함
- `case_0011` koloboke: primitive 컬렉션들 중 fastutil을 선택하여 대체함
- `case_0012` 에그: 운영 비용(사용자 교육·네트워크 관리) 증가 우려
- `case_0012` 동일 사업자 이중화: 단일 사업자 의존 시 지역/전국 사업자 장애에 취약
- `case_0012` 5G 라우터: 유선 인터넷 대비 속도·안정성 부족
- `case_0016` 배치: 배치 등을 사용하여 분석을 위한 데이터를 제공할 수도 있지만, 일정 주기로 배치를 수행하기 때문에 실시간 데이터를 반영하기 어려운 문제가 있습니다.
- `case_0021` 재사용 가능한 script: 사람이 판단하기에 묶음으로 동작해야 하는 작업을 명시했고, LLM 덕분에 고정적인 script가 아니더라도 빠르고 쉬운 변경이 가능해집니다.
- `case_0022` Cursor: 초보자나 비개발자가 1시간 안에 사용법을 익히고 의미 있는 성과를 내기엔 진입장벽이 높다고 판단됨
- `case_0022` Claude Code: 초보자나 비개발자가 1시간 안에 사용법을 익히고 의미 있는 성과를 내기엔 진입장벽이 높다고 판단됨
- `case_0025` Parcel: 프로젝트 복잡성으로 Zero-config 자동화가 리스크가 크다고 판단됨
- `case_0025` Rsbuild: 생태계·문서·커뮤니티 지원이 부족해 실서비스 적용에 부적절하다고 판단됨
- `case_0026` Entity LifeCycle(PrePersist 등) 콜백: 조회 시 복호화로 인해 1차 캐시 값이 변경되어 불필요한 update가 발생함
- `case_0027` AWS SDK 1.x: 지원 중단 예정으로 장기 운영에 적합하지 않음
- `case_0034` OpenSearch / Elasticsearch: 대용량 집계·저장 효율 요구를 만족하지 못함
- `case_0034` Grafana Loki: 라벨 기반 제약과 집계 기능 한계로 요구에 부적합
- `case_0034` Signoz: 자체 스키마 강제와 LogAttributes 접근 제한으로 설계 이점 활용 불가
- `case_0036` Backstage: 사내 환경에 알맞는 자체 IDP를 구축하기 위해 오픈소스 참조 후 적용하지 않음
- `case_0039` 검증 로직 별도 클래스: 검증 로직을 별도 클래스로 분리할 수도 있지만, 매번 별도로 검증 로직을 호출해야 한다면 실수로 검증을 누락할 가능성이 있습니다.
- `case_0045` reinterpret_cast: 타입 퍼닝 목적으로 사용하면 엄격한 앨리어싱 규칙을 위반하여 UB가 발생한다고 명시되어 검토에서 제외됨
- `case_0045` union: C++에서는 비활성 멤버 읽기가 미정의 동작이라 표준적으로 안전하지 않음
- `case_0045` std::bit_cast (포인터 변환): std::bit_cast는 값 대 값 도구로 포인터 변환 용도로 쓰지 않기로 검토에서 제외됨
- `case_0046` ChainedTransactionManager / 분산 트랜잭션: 분산 트랜잭션으로 MySQL 쿼리를 포함시키면 MySQL 쿼리 실패가 전체 트랜잭션에 영향을 주어 롤백/가용성 보장이 어렵고, 초기 정합성이 맞지 않는 상태에서 위험이 크므로 채택하지 않음.
- `case_0046` MyBatis 별도 MySQL 리포지토리 호출: 비즈니스 로직 전체에 걸쳐 수백~수천 곳의 호출을 수정해야 해 휴먼 에러 증가와 개발 기간 대폭 증가가 우려되어 채택하지 않음.
- `case_0047` react-window: div 기반 절대 배치로 CSS 적용·동적 행 처리·colspan 등 표 고유 기능 지원이 어려워 자체 구현으로 전환
- `case_0047` @tanstack/react-virtual: 네이버 로그 표현 방식의 복잡성을 오픈소스로 대응하기 어렵다고 판단
- `case_0047` IndexDB 캐시: 브라우저 메모리 부담을 줄이기 위한 캐시·언로드 방안으로 검토됨
- `case_0047` 페이징: 무한 스크롤로 인한 OOM을 피하기 위한 전통적 대안으로 검토됨
- `case_0047` React Query maxPage: 캐시된 페이지 수를 제한해 메모리 사용을 통제하는 방안으로 검토됨
- `case_0053` GlusterFS: 직접 운영 부담
- `case_0053` CephFS: 직접 운영 부담
- `case_0053` Ceph-rbd: 동시 접근(ReadWriteMany) 불가
- `case_0053` NFS: 확장성·HA 문제
- `case_0053` local-path: 동시 접근 불가
- `case_0053` Alluxio: 일부 POSIX API 미지원
- `case_0053` DDN EXAScaler: 도입 비용 과다
- `case_0054` mecab-ipadic-neologd: Kuromoji 구조 및 Elasticsearch 7.10.2 환경 제약으로 적용 불가
- `case_0054` Elasticsearch 8.x 업그레이드: 사내 플랫폼은 7.10.2까지만 지원하여 업그레이드가 현실적이지 않음
- `case_0056` SLI/SLO 용어 그대로 노출: 직관적 이해를 위해 기능 중심 이름으로 노출하기로 결정
- `case_0057` Spark Structured Streaming: 마이크로 배치 방식으로 이벤트타임 기반 상태 제어가 어려워 요구사항 불충족
- `case_0057` 네이티브 쿠버네티스 방식: 설정·운영이 수동으로 복잡해 운영 부담이 큼
- `case_0057` Flink 이미지에 Hadoop 에코시스템 전체 포함: 이미지 크기 증가 및 유지보수 부담으로 비선호
- `case_0057` non-keyed window: 단일 태스크 병목으로 성능 저하 발생
- `case_0058` WebAuthn Level 3 / Passkey: Level 3 스펙은 초안 상태이고, Passkey의 플랫폼 동기화를 제어할 수 없어 채택하지 않았다.
- `case_0059` 직전일(d-1) 기준 비교: 직전일 대비 증감만 고려하면 계속 증가 중인 화제가 탐지되지 않을 수 있어 채택하지 않음
- `case_0062` 자체 익스포터: CDN 업체에서 포맷을 업데이트하거나 커스텀 로그 필드를 추가할 경우 익스포터를 함께 업데이트해야 하는 불편함이 있었습니다.
- `case_0063` Python Kubernetes client: Python 클라이언트에서는 가까운 시일 안에 Informer를 사용할 수 없겠다고 판단
- `case_0063` Redis: 외부 캐시 대신 Informer 로컬 캐시 사용(외부 캐시 불필요)
- `case_0066` 메모리 증설: 임시방편으로 문제를 계속 미루는 접근
- `case_0066` Parcel: 커스텀 제한적
- `case_0066` Rsbuild: 생태계 작음
- `case_0067` nginx 라우팅 설정: 인스턴스의 nginx 설정/재시작 권한이 없어 운영팀 협조 없이 적용 불가
- `case_0067` 스케줄링 배치 캐싱: 주기적 배치 대신 최소 공수로 단일 인스턴스에서 즉시 캐싱 처리하기로 결정
- `case_0067` 별도 인스턴스 UI: 해당 기능만 위해 별도 인스턴스를 띄우는 것은 오버스펙
- `case_0068` Notion: 수작업 정리는 지속 불가했음
- `case_0068` AI 직접 조회 (MCP): 외부 텍스트를 그대로 AI가 처리하자 비용·속도 문제가 발생함
- `case_0071` nginx 설정: 인프라 구조(프론트/서버 각자 nginx, 인프라팀 관리 이미지) 때문에 nginx 설정으로 접근 차단을 적용할 수 없어 채택하지 않음.
- `case_0071` BigQuery 직접 조회: 매 요청마다 BigQuery를 직접 조회하면 지연이 커져 프로덕트 성능에 악영향을 주므로 채택하지 않음.
- `case_0072` max-lifetime 증가: 컬리로에서는 DB failover 시에 slave로 빠르게 연결하기 위해 max-lifetime을 작게 설정하고 있습니다.
- `case_0074` READ COMMITTED: 격리수준을 낮추면 Phantom Read 등 기존 비즈니스 로직에 영향을 줄 수 있어 사용하지 않기로 함
- `case_0074` 잠금 읽기 (LOCK IN SHARE MODE): 잠금 읽기는 최신 데이터를 보장하지만 락 경합 및 데드락 위험이 있어 채택하지 않음
- `case_0076` 수작업 카테고리 매핑: 사람의 수작업으로 카테고리 보완재 관계를 설정하는 방식은 채택하지 않음
- `case_0076` 주문서 전체 그대로 학습: 학습 시 특정 인기 상품이 과다 추천되는 편향 발생
- `case_0077` Chrome overwrite: 수동으로 필드 값을 하나씩 바꿔야 하므로 반복 테스트에 리소스 과다 소모
- `case_0077` Charles/Fiddler: 수동으로 필드 값을 하나씩 바꿔야 하므로 반복 테스트에 리소스 과다 소모
- `case_0077` 실제 데이터 수정: API가 언제 null을 반환하는지 정의되어 있지 않아 실제 데이터로 null을 재현하기 어려움
- `case_0079` WebP 변환: 복잡한 이미지에서 압축 효율이 낮아 적용에 제약이 발생
- `case_0079` Canvas 리사이징(메인 스레드): Canvas 처리 비용과 디코딩/인코딩으로 인해 메인 스레드를 점유하여 UI 블로킹이 발생
- `case_0079` Shared/Service Worker: 이미지 처리에 필요한 단순한 1:1 처리에 비해 불필요한 기능이 많아 부적합
- `case_0080` WriteConcern MAJORITY: 모든 요청에 대해 Secondary 과반수 ACK 응답을 기다리면 큰 오버헤드를 발생시킬 수 있음
- `case_0080` ReadPreference PRIMARY(전역): SECONDARY 노드가 유휴 상태로 남아 리소스를 낭비할 수 있음
- `case_0081` SQS 지연 전송: 지연 시간이 너무 짧다면 타이밍 문제가 여전히 발생할 수 있어 임시방편에 불과함
- `case_0081` Outbox 패턴: 설계 및 구현에 걸리는 시간과 비용이 부담되어 당장의 해결책으로는 부적절함

## 글 목록

| 글 | 길이 | 결과 | 항목 | 발췌 탈락 | 제목 |
| --- | --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | - | 0/0 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics |
| d2/4555524 | 18,452 | 사례/기술 선택·도입형 | case_0053 | 0/19 | AI 플랫폼을 위한 스토리지 JuiceFS 도입기 |
| d2/8366976 | 3,331 | 사례/문제 해결형 | case_0049, case_0050, case_0051, case_0052 | 0/21 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/3814947 | 16,662 | 사례/실험·활용기 | case_0048 | 0/11 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | - | 0/0 | Thread-safety in C++ |
| d2/1450243 | 15,218 | 사례/문제 해결형 | case_0047 | 0/15 | 윈도잉(windowing) 기법을 적용한 고성능 표 컴포넌트 개발기 |
| d2/8992409 | 1,342 | 사례/기술 선택·도입형 | case_0044 | 0/10 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| d2/6512234 | 22,022 | 사례/기술 선택·도입형 | case_0046 | 0/13 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/1155434 | 9,048 | 사례/기술 선택·도입형 | case_0045 | 0/14 | C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가 |
| d2/9290861 | 796 | 제외/회고·문화·행사 | - | 0/0 | Inside VictoriaMetrics |
| kakao/601 | 3,137 | 제외/회고·문화·행사 | - | 0/0 | 제3회 Kakao Tech Meet 후기 - 불확정성에서 감동까지 |
| kakao/624 | 787 | 제외/회고·문화·행사 | - | 0/0 | 카카오의 스팸 메일 대응 전략: 문자열 변형 CASE STUDY / 제6회 Kakao Tech Meet |
| kakao/761 | 3,645 | 인사이트/회고·문화·행사 | case_0023 | 0/8 | 실패를 장려하는 실험적 문화 |
| kakao/762 | 13,811 | 사례/실험·활용기 | case_0024 | 0/9 | 생산성 혁신의 실험: AI 마일리지 프로그램 |
| kakao/770 | 16,500 | 사례/기술 선택·도입형 | case_0025 | 1/15 | 5년 된 프로젝트의 빌드 도구를 교체하며 얻은 것들 |
| kakao/784 | 8,710 | 사례/실험·활용기 | case_0022 | 0/12 | 단 1시간 만에 99개의 MVP가? AI와 함께한 1K: 바이브코딩전 생생 후기 |
| kakao/785 | 4,597 | 인사이트/회고·문화·행사 | case_0018 | 0/8 | if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며 |
| kakao/804 | 3,760 | 사례/기술 선택·도입형 | case_0019 | 0/11 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/822 | 20,047 | 사례/실험·활용기 | case_0020, case_0021 | 0/19 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakao/835 | 12,198 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 둘째 날, 기술 세션 소개 |
| kakaopay/slack-bot-improving-operational-efficiency-2 | 5,044 | 사례/기술 선택·도입형 | case_0043 | 0/11 | 카카오페이 배포 효율화 1년 회고: 자동화 도입과 팀 생산성 향상 |
| kakaopay/tech-strategy-tpm | 9,673 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이 TPM은 어떤 일을 하나요? |
| kakaopay/katfun-joy-kotlin | 14,709 | 사례/실험·활용기 | case_0039, case_0040, case_0041, case_0042 | 0/21 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kakaopay/ifkakao2024-devrel | 10,598 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스 준비 맛보기 |
| kakaopay/perftest_zone | 4,708 | 사례/기술 선택·도입형 | case_0035 | 0/9 | 카카오페이 성능 테스트 존을 소개합니다. |
| kakaopay/kakaopaysec-wecan | 8,650 | 사례/기술 선택·도입형 | case_0036, case_0037, case_0038 | 0/24 | We Can Do Better: 개발자 플랫폼 효율화 이야기 |
| kakaopay/kakaopayins-opensearch-analyzer | 10,157 | 사례/실험·활용기 | case_0031, case_0032, case_0033 | 0/17 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/kakaopayins-envelope-encryption | 18,389 | 사례/기술 선택·도입형 | case_0026, case_0027 | 0/16 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/pallas-v2-log-platform | 25,659 | 사례/기술 선택·도입형 | case_0034 | 0/15 | 일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트 |
| kakaopay/kakaopayins-fe-common-component | 7,059 | 사례/기술 선택·도입형 | case_0028, case_0029, case_0030 | 0/21 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kurly/cart-recommend-model-development | 9,206 | 사례/실험·활용기 | case_0076 | 0/13 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 1부 |
| kurly/commit-mvcc-set-autocommit | 16,463 | 사례/문제 해결형 | case_0074 | 0/10 | 데이터가 있었는데요, 아니 없어요 |
| kurly/deliveryproductteam-culture-1 | 4,454 | 사례/문제 해결형 | case_0075 | 0/10 | 딜리버리 프로덕트 개발팀의 개발문화 - 로그 & 알람편 |
| kurly/connection-leak | 6,791 | 사례/문제 해결형 | case_0072 | 0/9 | 99%가 모른다는 DB Connection 누수 문제 |
| kurly/refine-address-internalization-2 | 4,312 | 사례/문제 해결형 | case_0073 | 1/12 | 주소정제 서비스 내재화 - 2화 ( 그럴싸한 계획 ) |
| kurly/access-block-1 | 5,663 | 사례/문제 해결형 | case_0067 | 0/14 | nginx 설정 없이 우아하게 서비스 점검하기 (上) |
| kurly/access-block-2 | 8,383 | 사례/기술 선택·도입형 | case_0071 | 0/16 | nginx 설정 없이 우아하게 서비스 점검하기 (下) |
| kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0 | 13,290 | 사례/기술 선택·도입형 | case_0066 | 0/14 | 빌드가 터졌다: 5년 된 CMS 프로젝트의 Webpack4 → Vite 전환 |
| kurly/tech-spec-adoption-with-ai-automation | 8,164 | 사례/기술 선택·도입형 | case_0064, case_0065 | 0/22 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| kurly/claude-code-redesign-my-day | 7,389 | 사례/기술 선택·도입형 | case_0068, case_0069, case_0070 | 0/27 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| ly/managing-multi-cdn-logs-traffics-with-vector | 16,695 | 사례/기술 선택·도입형 | case_0062 | 0/15 | Vector를 활용해 멀티 CDN 로그 및 트래픽 관리하기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 18,813 | 사례/기술 선택·도입형 | case_0060, case_0061 | 1/17 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/improving-kubernetes-relay-api-server-performance-with-informer | 12,361 | 사례/기술 선택·도입형 | case_0063 | 0/12 | Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기 |
| ly/introducing-fido2-client-sdk-open-source | 9,957 | 사례/기술 선택·도입형 | case_0058 | 0/13 | FIDO2 클라이언트 SDK 오픈소스 소개 |
| ly/how-to-evaluate-ai-generated-images-1 | 16,708 | 제외/개념·튜토리얼 | - | 0/0 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/extracting-trending-keywords-from-openchat-messages | 14,017 | 사례/문제 해결형 | case_0059 | 2/19 | 오픈챗 메시지들로부터 트렌딩 키워드 추출하기 |
| ly/pd1-ai-hackathon-recap | 4,153 | 인사이트/회고·문화·행사 | case_0055 | 0/7 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 6,232 | 사례/기술 선택·도입형 | case_0056 | 1/14 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 및 서비스 상태 확인 도구 LINE Status 개발기 |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 19,601 | 사례/기술 선택·도입형 | case_0057 | 0/19 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/japanese-search-kuromoji-to-sudachi | 15,395 | 사례/기술 선택·도입형 | case_0054 | 1/14 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자가 좋아하는 과자는? |
| oliveyoung/2024-06-05_google-cloud-next-24-review | 3,796 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next '24 방문기 |
| oliveyoung/2024-08-11_type-and-type-system-with-typescript | 11,673 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 타입과 타입 시스템 |
| oliveyoung/2024-09-30_oy-feconf-2024 | 8,894 | 제외/회고·문화·행사 | - | 0/0 | 올리브영에서는 프론트엔드 개발자들이 이런 고민을 하는군요? |
| oliveyoung/2024-10-17_oy-delivery-mq | 4,642 | 사례/기술 선택·도입형 | case_0082 | 0/10 | 올리브영 물류시스템에서는 데이터를 어떻게 주고 받을까? |
| oliveyoung/2024-12-16_Design-System-Token-Automation | 17,955 | 사례/실험·활용기 | case_0083 | 0/12 | 디자인 시스템 중 디자인 토큰을 여러 도구를 이용하여 자동화 하는 방법 |
| oliveyoung/2024-12-17_catalog-mongo-transaction-2 | 11,450 | 사례/문제 해결형 | case_0080, case_0081 | 0/18 | Spring Boot MongoDB 트랜잭션 도입 실전 가이드 |
| oliveyoung/2025-02-14_oy-global-mall-address | 4,978 | 사례/기술 선택·도입형 | case_0078 | 0/12 | 올리브영 글로벌몰 주소 자동완성 및 검증 솔루션 도입기 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 7,158 | 사례/문제 해결형 | case_0079 | 0/12 | Web Worker로 이미지 처리 최적화하기 |
| oliveyoung/2025-06-10_chaos | 7,289 | 사례/기술 선택·도입형 | case_0077 | 0/12 | 버그가 아니라 장애를 잡아라!! QA와 카오스 엔지니어링의 만남 |
| toss/27752 | 5,980 | 사례/문제 해결형 | case_0006 | 0/11 | 드래그 앤 드롭은 사실 편한 UX가 아니다? |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | - | 0/0 | 오픈소스에 기여하고 토스에 합격한.ssul \| EP.4 모닥불 |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | - | 0/0 | 개발자 리더로서 성장당한 썰 \| EP.7 모닥불 |
| toss/toss-frontend-ai-docs | 2,869 | 사례/기술 선택·도입형 | case_0005 | 0/10 | 토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유 |
| toss/toss-people-3 | 7,801 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 문과생에서 토스 개발 리더까지 |
| toss/frontend-esbuild-hmr | 10,415 | 사례/문제 해결형 | case_0002 | 0/11 | ESBuild를 위한 HMR, 직접 만들기 |
| toss/frontend-apply-without-resume | 2,783 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드에 이력서 없이 리포지토리 링크로 지원하세요 (~5/31) |
| toss/toss-securities-gpu-mig | 13,794 | 사례/기술 선택·도입형 | case_0003 | 0/16 | GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기 |
| toss/tds-color-system-update | 13,423 | 사례/기술 선택·도입형 | case_0001 | 0/13 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| toss/ads_dashboard_fe | 12,467 | 사례/기술 선택·도입형 | case_0004 | 0/14 | 전체 데이터를 브라우저에 두는 광고 대시보드 만들기 |
| woowahan/14484 | 5,518 | 사례/문제 해결형 | case_0017 | 0/10 | “일단 백로그에 넣어두고 여유 있을 때 보는 걸로 할까요?” : 백로그를 백로그로 두지 않는 법 |
| woowahan/14671 | 6,108 | 제외/회고·문화·행사 | - | 0/0 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/15398 | 10,772 | 사례/기술 선택·도입형 | case_0013 | 0/13 | Java의 미래, Virtual Thread |
| woowahan/15541 | 6,445 | 제외/개념·튜토리얼 | - | 0/0 | 웹 접근성 준수를 통한 모두에게 배달되는 일상의 행복 |
| woowahan/17386 | 11,245 | 사례/실험·활용기 | case_0014, case_0015, case_0016 | 0/34 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/17911 | 4,799 | 사례/기술 선택·도입형 | case_0012 | 0/14 | B마트 주문 유실을 없애보자: 네트워크 편 |
| woowahan/20763 | 8,615 | 사례/기술 선택·도입형 | case_0011 | 0/20 | 이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기 |
| woowahan/21027 | 25,102 | 사례/기술 선택·도입형 | case_0008 | 0/14 | 실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법 |
| woowahan/24434 | 15,179 | 사례/문제 해결형 | case_0007 | 0/13 | “함께 구매하면 좋은 상품” 추천 모델 고도화 |
| woowahan/24999 | 12,341 | 사례/문제 해결형 | case_0009, case_0010 | 1/22 | WOOWACON 2025 미니게임 WOOWA POP! |
