# 추출 점검 리포트: v3-gpt-5-mini-medium

- 모델: gpt-5-mini (medium)
- 프롬프트 버전: 17bac37197a4
- 글 80편: 사례 58, 인사이트 0, 제외 22
- 항목 77개: 사례 77, 인사이트 0
- 토큰: 호출 154회, 입력 1,205,296 (캐시 542,208), 출력 517,724 (reasoning 398,016)
- 비용: $1.215 (편당 $0.0152), 전체 1,262편 추정 $19.2 / Batch $9.6

## 블로그별 구조화 유형

| 블로그 | 사례 | 인사이트 | 제외 | 항목 수 |
| --- | --- | --- | --- | --- |
| d2 | 7 | 0 | 3 | 10 |
| kakao | 5 | 0 | 5 | 9 |
| kakaopay | 8 | 0 | 2 | 15 |
| kurly | 10 | 0 | 0 | 11 |
| ly | 8 | 0 | 2 | 10 |
| oliveyoung | 6 | 0 | 4 | 8 |
| toss | 6 | 0 | 4 | 6 |
| woowahan | 8 | 0 | 2 | 8 |

## 글 유형 × 구조화 유형

| 글 유형 | 사례 | 인사이트 | 제외 |
| --- | --- | --- | --- |
| 개념·튜토리얼 | 1 | 0 | 4 |
| 기술 선택·도입형 | 34 | 0 | 0 |
| 문제 해결형 | 17 | 0 | 0 |
| 실험·활용기 | 6 | 0 | 0 |
| 회고·문화·행사 | 0 | 0 | 18 |

## 짧은 글 (평문 1,500자 미만) 8편

| 글 | 길이 | 결과 | 항목 | 분류 이유 |
| --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | 0 | 발표 세션(영상) 공개 안내 및 목차 중심의 글입니다. 본문에 구체적인 설계 결정, 성능 수치나 비교, 문제 해결 과정 등의 실무적 근거가 없어 기술 사례/인사이트로 분류하기 어렵습니다. |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | 0 | NAVER ENGINEERING DAY 발표자료로 C++ 스레드 안전성의 개념(데이터 레이스, sequenced-before/synchronizes-with/happens-before, basic thread safety, std::shared_ptr 등)을 정리한 튜토리얼/개념 설명 중심의 글입니다. 특정 서비스에서의 설계 결정, 도입 비교나 실험 결과(수치·벤치마크 등)가 없어 사례나 인사이트로 분류하기 어렵습니다. |
| d2/8992409 | 1,342 | 사례/문제 해결형 | 1 | 과거 데이터 파이프라인의 문제를 명확히 제시하고 이를 해결하기 위해 Flow.er를 개발한 과정(Proof of Concept, 구성 요소 설계, DBT·Airflow의 역할·선택 근거, CI/CD·정합성 검사 등 구체적 설계·운영 결정과 확장 사례)을 담고 있어 실제 기술적 선택과 근거가 있는 사례로 분류됩니다. |
| d2/9290861 | 796 | 제외/회고·문화·행사 | 0 | NAVER Engineering Day 발표 세션 소개 및 목차 안내에 해당함. 내부 구조를 다룬다는 주제는 있으나 본문에 구체적 설계 결정, 문제 해결 과정, 수치·비교·적용 결과 등 실무적 근거가 없어 기술 사례나 실무 인사이트로 분류하기 어렵습니다. |
| kakao/624 | 787 | 제외/회고·문화·행사 | 0 | 발표 영상 공유와 발표자 인터뷰 중심의 행사 소개글입니다. 구체적인 기술 문제 해결 과정, 설계 결정·근거(수치·비교) 또는 실무 적용 상세가 포함되어 있지 않아 실무용 사례나 인사이트로 분류하기 어렵습니다. |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | 0 | 사내 간식 선호도 설문 결과와 패키지 제안에 대한 문화·행사성 글로, 기술적 문제·설계·도입 근거나 실무 적용 가능한 팁·코드가 없음. 설문 방식을 일부 언급하나 기술적 실무 사례로 볼 수 없어 제외 대상임. |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | 0 | 오픈소스 기여 경험·합격 후기와 커뮤니티·성장 이야기를 다루는 인터뷰/회고성 글입니다. 구체적인 기술적 문제 해결, 설계 결정, 수치·비교 등 실무 적용 근거가 없어 기술 사례 데이터베이스용 '사례'나 '인사이트'로 분류할 수 없습니다. |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | 0 | 토스 프론트엔드 리더들의 리더십 성장과 조직 문화에 대한 인터뷰/토크 영상 요약입니다. 리더십, 피드백, 성장 경험을 다루며 기술적 설계·문제 해결·도입 사례나 실무 적용 가능한 기술적 내용이 포함되어 있지 않습니다. |

## 글당 항목 수 (제외 글 빼고)

| 항목 수 | 글 수 |
| --- | --- |
| 1 | 48 |
| 2 | 5 |
| 3 | 2 |
| 4 | 2 |
| 5 | 1 |

## 주 문제 유형 분포

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 개발 생산성 | 16 | 21% |
| API 설계·외부 연동 | 7 | 9% |
| 클라이언트 성능(웹·앱) | 6 | 8% |
| 배포·CI/CD | 6 | 8% |
| 데이터 정합성·트랜잭션 | 5 | 6% |
| 모니터링·관측성 | 5 | 6% |
| 테스트 자동화 | 5 | 6% |
| 인증·보안 | 4 | 5% |
| 데이터 파이프라인 | 4 | 5% |
| 업무·운영 자동화 | 3 | 4% |
| 인프라·컨테이너 | 3 | 4% |
| 비용 절감 | 2 | 3% |
| 장애 대응·복구 | 2 | 3% |
| 트래픽 급증 대응 | 2 | 3% |
| 캐싱 | 2 | 3% |
| 메시징·비동기 처리 | 2 | 3% |
| DB 성능·쿼리 최적화 | 1 | 1% |
| DB 마이그레이션·샤딩 | 1 | 1% |
| MSA | 1 | 1% |

- 한 번도 안 쓰인 분류 (1개): 동시성·락

## 도메인 분포

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 사내 플랫폼·개발 도구 | 30 | 39% |
| 범용 | 14 | 18% |
| 커머스·주문·재고 | 13 | 17% |
| 검색·추천 | 5 | 6% |
| LLM·AI | 4 | 5% |
| 채팅·메시징 서비스 | 4 | 5% |
| 콘텐츠·미디어 | 3 | 4% |
| 결제·금융 | 2 | 3% |
| 광고·마케팅 | 1 | 1% |
| 배달·물류 | 1 | 1% |

- 쏠림(30% 초과): 사내 플랫폼·개발 도구
- 한 번도 안 쓰인 분류 (0개): 없음

## 발췌 검증

- 채택한 시도 기준 발췌 822개 중 탈락 7개 (원문 존재율 99%)
- 재시도한 글 16편

- `d2/4555524`: nubes와 juicefs+nubes는 큰 차이 없었다. 즉, nubes에 데이터 스토리지로 JuiceFS를 사용해도 성능 저하는 없다.
- `kakao/822`: 처음에 저는 스트레스 테스트가 단순히 부하를 거는 테스트라고 생각했습니다. 하지만 한번의 테스트 수행을 위해 필요했던 노력을 리스팅해보면 아래와 같습니다.
- `kurly/refine-address-internalization-2`: 제 기억에 이 때 까지는 외부 업체와의 계약 종료라는 목표는 뭔가 멀게만 느껴지는 목표였고, 일단 외부업체 api 호출 비용이라도 가능한 최소한으로 줄여보자는 목표로 계획을 세웠습니다.
- `ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status`: 이때 저희가 SLI/SLO를 정의할 때 기준으로 삼았던 것은 개별 서비스의 장애 발생 여부가 아니라, CUJ 관점에서 사용자가 서비스를 ‘잘 이용하고 있는가(user happiness)’였습니다.
- `toss/toss-frontend-ai-docs`: 실록봇은 대화 스레드에 실록봇 이모지를 붙이거나 봇을 호출하면 AI가 대화를 분석하고 요약해서 PR을 올려요.
- `toss/toss-securities-gpu-mig`: 이 지표는 기존의 GPU 사용률 지표처럼 0부터 100 사이의 숫자로 표현되며, MIG 인스턴스별 SM 사용률(SM Active Ratio)을 나타납니다.
- `woowahan/21027`: pre filter라고 부르는데요. 먼저 조건 필터를 통해 우리가 원하는 대상을 축소한 다음에 후보군에 대해 벡터 유사도 검색을 통해 랭킹을 지정하는 것을 의미합니다.

## 기술 사전에 없는 이름 156종

- Jira (4)
- Web Worker (3)
- Locust (3)
- Figma (2)
- GitHub (2)
- ESBuild (2)
- SWC (2)
- Milvus (2)
- Vite (2)
- Storybook (2)
- Babel (2)
- Rollup (2)
- C++ (2)
- Wallga (2)
- HDFS (2)
- Confluence (2)
- Hubot (2)
- Style Dictionary (1)
- CSS (1)
- react-refresh (1)
- WebSocket (1)
- nvidia-device-plugin (1)
- dcgm-exporter (1)
- MIG (1)
- nvidia-smi (1)
- Node2Vec (1)
- Transformer (1)
- SASRec (1)
- WASM (1)
- Rust (1)
- Bun (1)
- V8 (1)
- S2 Geometry (1)
- fastutil (1)
- AWS ALB (1)
- IPSEC (1)
- LTE 라우터 (1)
- DNS (1)
- DHCP (1)
- NTP (1)
- RADIUS (1)
- pgvector (1)
- Atlas MongoDB (1)
- Redis Stack (1)
- Virtual Thread (1)
- ForkJoinPool (1)
- JDK (1)
- Netty (1)
- Webpack (1)
- Vitest (1)
- v0 (1)
- Supabase (1)
- Vercel (1)
- kanana-2-30b-a3b (1)
- MLA (1)
- MoE (1)
- IntelliJ (1)
- Claude API (1)
- vector DB (1)
- Codex (1)
- Reach (1)
- HyperDX (1)
- Parquet (1)
- ZSTD (1)
- Filebeat (1)
- Amazon Athena (1)
- AWS KMS (1)
- OpenSearch Dashboards (1)
- Apache Lucene (1)
- Mongo (1)
- InfluxDB (1)
- GCP (1)
- Spinnaker (1)
- Hive (1)
- datasource-proxy (1)
- react-window (1)
- Big Table (1)
- Clang-Tidy (1)
- DBT (1)
- Release Please Action (1)
- vanniktech-maven-publish-plugin (1)
- Dokka (1)
- JFrog Artifactory (1)
- Maven Central (1)
- GitHub Pages (1)
- Ruler (1)
- LLM (1)
- Nexus (1)
- Sudachi (1)
- Kuromoji (1)
- ICU (1)
- JuiceFS (1)
- JuiceFS CSI Driver (1)
- nubes (1)
- MinIO (1)
- Fio (1)
- Iceberg (1)
- WebAuthn (1)
- CTAP (1)
- Android (1)
- iOS (1)
- Xcode (1)
- Secure Enclave (1)
- ARM TrustZone (1)
- Android StrongBox (1)
- hubot-conversation (1)
- Ansible (1)
- Harbor (1)
- Slack Workflow (1)
- Vector (1)
- node_exporter (1)
- kube-state-metrics (1)
- Akamai (1)
- Informer (1)
- kubectl (1)
- etcd (1)
- kube-apiserver (1)
- MinHash (1)
- NPMI (1)
- MMR (1)
- Z-test (1)
- WebView (1)
- Taskmaster (1)
- esbuild (1)
- MobX (1)
- Material-UI (1)
- qs (1)
- dayjs (1)
- react-csv (1)
- Google Sheets (1)
- BigQuery (1)
- Vue Router (1)
- Swagger (1)
- Postman (1)
- MariaDB (1)
- AWS EC2 (1)
- Eclipse MAT (1)
- 행정안전부 도로명주소 API (1)
- 행정안전부 좌표정보 API (1)
- BERT4Rec (1)
- gradio (1)
- mlflow (1)
- mitmproxy (1)
- MariaDB Connector/J (1)
- OffscreenCanvas (1)
- WiredTiger (1)
- MQ (1)
- Yarn (1)
- Jotai (1)
- Panda CSS (1)
- AWS ECR (1)
- AWS ECS (1)
- AWS S3 (1)
- Tokens Studio For Figma (1)
- token-transformer (1)
- gh (1)

## 버린 대안 91개 (사례 77개 중)

- `case_0001` 부분적 팔레트 수정: 팔레트의 일부만 변경하면 다른 컬러 토큰과 전체 명도 진행에서 추가 조정이 필요해 근본적 해결이 되지 않음
- `case_0003` Virtual Scrolling: 페이지네이션(100건 단위) UX와 DOM 부하 확인으로 불필요하다고 판단
- `case_0003` IndexedDB 캐싱: 무효화 규칙 불명확성과 요구 대비 과다한 복잡도 때문에 보류
- `case_0003` Worker에서 직접 HTTP 클라이언트 사용: 공통 HTTP 클라이언트(인증·공통 에러 처리·재시도)를 Worker 쪽에도 중복 배치해야 해 관리 비용이 커져 보류
- `case_0004` 클라우드 활용: 장기적·지속적 워크로드나 컴플라이언스 제약에서는 비용·보안 이슈로 부적합
- `case_0004` 혼합 GPU 운영: 운영 복잡성·호환성 문제와 수요 편중으로 인한 자원 유휴 위험
- `case_0004` MPS: 소프트웨어 공유 방식으로 격리와 모니터링·제어에 한계가 있어 운영 리스크가 큼
- `case_0007` 문서를 더 잘 써서 방문하게 하기: 문서가 능동적으로 찾아가도록 하는 방식으로 전환함
- `case_0007` 테크니컬 라이터 중심 문서 작성: 소수 인력으로는 문서의 양·확장성 확보가 어려움
- `case_0008` 코드 난독화: 코드 난독화는 역공학을 지연시킬 뿐 근본적 해결이 아니어서 배제됨.
- `case_0008` 프로그레스바 중앙 클릭 제약: 클라이언트 조작으로 우회되어 효과적이지 않았음.
- `case_0008` 이미지 CAPTCHA: 매크로는 막았지만 게임의 재미가 크게 훼손되어 바람직하지 않았음.
- `case_0008` ZK-SNARK: 영지식 증명 계열 기술은 검토했으나 우아팝에 적용하기에는 부적절하다고 판단됨.
- `case_0009` 캐시 레이어(예: Redis 등): 캐시 레이어는 비용 증가와 작업량 증가가 있어 유지보수/배포 영향 최소화를 위해 채택하지 않음
- `case_0009` hazelcast: 단순 조회 중심인 서비스에선 기능이 과하고 진입 장벽이 높아 채택하지 않음
- `case_0009` chronicle-map: 힙 외부 저장 등 기능은 있으나 서비스 요구에는 과하다고 판단되어 채택하지 않음
- `case_0010` 에그(와이파이 도시락): 운영 비용(사용자 교육·관리)과 배터리·내부망 연결 등 운영 부담이 큼
- `case_0010` 동일 회선 사업자 이중화: 통신 사업자 회선의 장애 빈도·파급력 문제로 단일 사업자 이중화는 위험함
- `case_0012` Milvus: 1차 실험에서는 기능 검증을 했으나 2차 실험 대상(운영·부하 검증)으로는 선정되지 않았다.
- `case_0012` Redis Stack: 1차 실험에서 동작 검증은 했으나, 운영·부하 관점에서 2차 실험 후보로는 선정되지 않았다.
- `case_0012` Atlas MongoDB(Atlas Search): 하이브리드 검색 기능을 제공하지만 부하 테스트에서 리소스 포화로 응답 지연이 발생하여 최종 선택에서는 RDS에 밀렸다.
- `case_0012` OpenSearch: pre-filter 동작 확인 및 성능 검증을 했으나 부하 구간에서 요청 실패(500)가 발생하여 운영 요구를 만족하지 못했다. **(technologies에도 있음)**
- `case_0014` Kotlin Coroutine: 프로덕션 코드 변경과 suspend 전파(함수의 색) 및 러닝커브 때문에 전체 적용이 부담스러워 사용하지 않기로 검토됨
- `case_0014` Reactive Programming (WebFlux/Netty): 플로우 전반에 걸친 전염성(함수의 색)과 컨텍스트 스위칭 시 스택 트레이스 유실·성능 낭비로 인해 대안으로서 적용을 꺼림
- `case_0015` Parcel: Zero-config이지만 복잡한 프로젝트에서 커스터마이징 한계로 리스크가 큼
- `case_0015` Rsbuild: 생태계·문서·지원 부족으로 실서비스 적용이 어렵다고 판단
- `case_0016` Cursor: 초보자나 비개발자가 1시간 안에 사용법을 익히고 의미 있는 성과를 내기엔 진입장벽이 높다고 판단했습니다.
- `case_0016` Claude Code: 초보자나 비개발자가 1시간 안에 사용법을 익히고 의미 있는 성과를 내기엔 진입장벽이 높다고 판단했습니다.
- `case_0025` OpenSearch: 비용과 대용량 집계 성능 문제로 장기적 확장에 부적합 **(technologies에도 있음)**
- `case_0025` Grafana Loki: 라벨 기반 제약과 집계 기능 한계로 복잡한 필드 검색·집계에 부적합
- `case_0025` Signoz: 자체 스키마 강제와 LogAttributes 접근 제약으로 ClickHouse 설계 장점을 활용 불가
- `case_0026` Entity LifeCycle 콜백: 엔티티 라이프사이클 콜백(@PostLoad 등)을 사용한 접근은 1차 캐시 변경으로 인한 부작용 때문에 채택하지 않았다.
- `case_0033` nGrinder: nGrinder에서 지원하는 언어(Groovy 등)가 개발자에게 친숙하지 않아 허들이 되었다. **(technologies에도 있음)**
- `case_0034` 검증 로직 분리: 매번 별도로 검증 로직을 호출해야 한다면 실수로 검증을 누락할 가능성이 있습니다.
- `case_0039` 분산 트랜잭션(ChainedTransactionManager): 분산 트랜잭션을 사용하면 MySQL 쿼리 실패가 전체 트랜잭션에 영향을 줄 수 있고, 전환 초기에 두 DB 정합성이 맞지 않아 위험함.
- `case_0039` MyBatis 인터페이스를 각각 분리해 양쪽 호출: 비즈니스 로직 전반에 대규모 코드 변경이 필요해 휴먼 에러와 개발 기간 증가 위험이 큼.
- `case_0039` 운영 HTTP 트래픽 복제 / Kafka 토픽 복제(성능 검증용): 타 부서 시스템에 중복 호출 부하를 야기하거나 예상치 못한 부작용으로 운영에 영향을 줄 위험이 매우 높음.
- `case_0040` @tanstack/react-virtual: 오픈소스 라이브러리로는 네이버 로그의 다양하고 복잡한 표현을 대응하기 어렵다고 판단하여 채택하지 않음.
- `case_0040` react-window: div 절대배치 기반으로 표 고유 기능과 스타일링이 어렵고 동적 행 처리 복잡성으로 기존 사용을 포기하고 자체 구현함.
- `case_0041` reinterpret_cast (타입 퍼닝): 타입 퍼닝 목적으로 쓰면 엄격한 앨리어싱 규칙을 위반하여 UB가 발생함
- `case_0041` union: C++에서 비활성 멤버를 읽는 타입 퍼닝은 미정의 동작이므로 표준 준수 코드로 사용할 수 없음
- `case_0048` 사용자 사전 수동 등록: 수동 등록은 단기적 보완은 되나 신조어·대량 누락을 지속적으로 해결할 수 없음
- `case_0048` Elasticsearch 8.x 업그레이드: 사내 인프라가 7.10.2만 지원해 업그레이드가 현실적이지 않음
- `case_0048` mecab-ipadic-neologd: Kuromoji/Elasticsearch 7.10.2 환경에서 MeCab 기반 최신 사전 연동이 제약이 있음
- `case_0048` OpenSearch 2.4.1: Sudachi 공식 지원 범위 밖이라 도입 검토 대상에서 제외
- `case_0049` Alluxio: POSIX 일부 미지원, 원본과 불일치 가능성, 별도 클러스터 운영 부담으로 AI 워크로드에 부적절하다고 판단됨.
- `case_0049` GlusterFS: 직접 운영 부담이 커서 사내 지원 스토리지를 우선 검토함.
- `case_0049` CephFS: 직접 운영 부담이 커서 사내 지원 스토리지를 우선 검토함.
- `case_0049` Ceph-rbd: 다중 Pod 동시 접근을 지원하지 않아 공유 스토리지 요구를 만족하지 못함.
- `case_0049` NFS: 확장성·HA 한계로 대규모 AI 워크로드에 제약이 있음.
- `case_0049` local-path: 노드 로컬 디스크 기반으로 동시 접근이 불가능해 공유 스토리지 요구를 충족하지 못함.
- `case_0049` AWS EFS / Google Filestore: 비용이 높고 온프레미스 환경에서 사용 불가함.
- `case_0049` DDN EXAScaler: 요구사항을 만족하지만 도입 비용이 매우 커서 제한적으로만 사용 중임.
- `case_0050` Spark Structured Streaming: 마이크로배치 방식으로 데이터 최신성 판별과 exactly-once 보장 동시 만족 어려움
- `case_0050` 네이티브 쿠버네티스 방식: 운영·설정의 번거로움으로 오퍼레이터 방식보다 채택하지 않음
- `case_0051` WebAuthn Level 3 (Passkey 동기화): Level 3 스펙은 아직 공식적으로 확정되지 않은 초안(draft) 상태이고, Passkey 동기화는 플랫폼 API로 동기화 제어가 불가능해 비즈니스 로직상 문제가 될 수 있다.
- `case_0052` 기존 API 상태 페이지: 외부 API 사용자 대상·수동 갱신 구조라 내부 공통 기준 도구로 적합하지 않음
- `case_0052` 온콜 알람 기반 상태 반영: 온콜 알람 그대로 반영하는 방식 대신 CUJ/SLO 기반 사용자 경험 관점으로 판단하기로 함
- `case_0053` 기존 API 상태 페이지: 외부 사용자 대상·수동 갱신 구조라 내부 자동 갱신형 도구로 사용하지 않음
- `case_0057` Redis: 로컬 캐시로 Redis를 도입할 필요 없음(Informer 캐시 사용).
- `case_0057` 스레드 다수 생성(비동기 우회): 비동기 방식으로 우회해도 지연 문제가 해결되지 않음.
- `case_0057` Python 클라이언트의 Informer 사용: Python 클라이언트는 Informer 지원이 정체되어 있어 채택 불가.
- `case_0058` 단순 최근 빈도: 최근 등장 빈도만 쓰면 인삿말 등 일상어가 상위에 잡혀 유의미한 트렌드를 못 잡음
- `case_0058` 블랙리스트 방식: 정적 블랙리스트 대신 데이터 기반 연관성 분석으로 확장해 검출하는 편이 바람직하다고 판단
- `case_0058` 하루 전(d-1) 비교 기준: 직전일 기준은 증가 지속 중인 화제를 놓칠 수 있어 더 긴 기준을 사용
- `case_0059` AI 직접 외부 조회 (MCP): 가져온 텍스트가 모두 토큰으로 계산되어 비용과 속도가 급격히 악화되었기 때문에 실용적이지 않음.
- `case_0059` Notion 수작업 정리: 수작업으로는 지속 가능하지 않아 자동화 필요성이 높았음.
- `case_0060` 네이티브 앱: 정책 변경 시 앱 심사와 업데이트가 필요해 운영·배포 유연성이 떨어진다.
- `case_0062` 메모리를 계속 늘리기: 메모리를 계속 늘려 임시방편으로 버티는 방식은 선택지였으나 근본 해결을 위해 번들러 교체를 선택했다.
- `case_0063` nginx 라우팅 설정: 인스턴스의 nginx 설정 변경·재시작 권한이 없어 즉시 적용 불가
- `case_0063` 스케줄링 배치 캐싱: 주기적 배치 대신 최소한의 공수로 한 인스턴스 내에서 즉시 처리하기로 결정
- `case_0064` nginx 설정: 인프라 구조상 중앙 nginx로 차단을 처리하기 어려움
- `case_0064` BigQuery를 메인 DB로 사용: 빈번한 조회용 메인 DB로 사용하기에 응답 지연이 큼
- `case_0064` UI 직접 구현 / 신규 인스턴스 띄우기: 기능 관리용 UI를 직접 만들거나 전용 인스턴스를 띄우는 것이 운영상 애매함
- `case_0068` 수작업 카테고리 설정: 수작업으로 카테고리 간 보완재 관계를 설정하는 것은 어려워서 데이터 기반 방법을 사용함
- `case_0069` Chrome overwrite contents: 수동으로 필드를 하나씩 수정해야 해 반복 테스트에 비효율적이라 제외
- `case_0069` Charles/Fiddler: 수동 수정이 필요해 반복적 테스트에 적합하지 않아 제외
- `case_0069` 실제 데이터 수정: 언제 API가 null을 반환할지 정의되지 않아 데이터 변경으로는 재현이 어려워 제외
- `case_0070` READ COMMITTED 격리수준: 격리수준을 낮추면 기존 비즈니스 로직에 영향(Phantom Read 등)이 있어 채택하지 않음.
- `case_0070` 잠금 읽기 (LOCK IN SHARE MODE): 행 잠금으로 인해 락 경합·데드락 위험이 있어 채택하지 않음.
- `case_0072` WebP 변환: 복잡한 이미지에서 압축 효율이 낮아 실효성이 떨어짐
- `case_0072` Canvas 리사이징(메인 스레드): 메인 스레드를 점유해 디코딩/인코딩 과정에서 JS 블로킹 발생
- `case_0072` Shared Worker: 이미지 처리에는 불필요한 기능이 많아 배제
- `case_0072` Service Worker: 이미지 처리에는 불필요한 기능이 많아 배제
- `case_0073` WebP 변환: 복잡한 이미지에서 압축 효율이 낮아 적용에 제약이 있음
- `case_0073` Canvas 리사이징(메인 스레드): 메인 스레드 블로킹을 유발하여 UI 응답성 저하
- `case_0074` WriteConcern MAJORITY: 정확도를 높일 수 있지만 전체 요청에 과반수 ACK를 기다리면 오버헤드가 크기 때문에 채택하지 않음.
- `case_0074` ReadPreference PRIMARY(전체 적용): 모든 읽기를 PRIMARY로 하면 SECONDARY가 유휴 상태가 되어 리소스 낭비가 발생할 수 있어 전체 적용은 채택하지 않음.
- `case_0075` 메시지 지연 전송: 지연 전송은 간단하지만 지연 시간이 부족하면 타이밍 문제가 여전히 발생하므로 근본 해결책으로 보지 않음.
- `case_0075` Outbox 패턴: Outbox는 근본적인 해결책이지만 설계·구현 비용과 시간이 부담되어 즉시 적용하지 않음.
- `case_0076` EAI I/F: 배치를 사용해 지연을 유발하고, 단일 EAI 어댑터 장애 시 전체 통신이 중단되는 단점으로 더 이상 사용하지 않음

## 글 목록

| 글 | 길이 | 결과 | 항목 | 발췌 탈락 | 제목 |
| --- | --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | - | 0/0 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics |
| d2/4555524 | 18,452 | 사례/기술 선택·도입형 | case_0049 | 1/21 | AI 플랫폼을 위한 스토리지 JuiceFS 도입기 |
| d2/8366976 | 3,331 | 사례/문제 해결형 | case_0044, case_0045, case_0046, case_0047 | 0/25 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/3814947 | 16,662 | 사례/문제 해결형 | case_0043 | 0/11 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | - | 0/0 | Thread-safety in C++ |
| d2/1450243 | 15,218 | 사례/문제 해결형 | case_0040 | 0/12 | 윈도잉(windowing) 기법을 적용한 고성능 표 컴포넌트 개발기 |
| d2/8992409 | 1,342 | 사례/문제 해결형 | case_0042 | 0/8 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| d2/6512234 | 22,022 | 사례/기술 선택·도입형 | case_0039 | 0/17 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/1155434 | 9,048 | 사례/실험·활용기 | case_0041 | 0/14 | C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가 |
| d2/9290861 | 796 | 제외/회고·문화·행사 | - | 0/0 | Inside VictoriaMetrics |
| kakao/601 | 3,137 | 제외/회고·문화·행사 | - | 0/0 | 제3회 Kakao Tech Meet 후기 - 불확정성에서 감동까지 |
| kakao/624 | 787 | 제외/회고·문화·행사 | - | 0/0 | 카카오의 스팸 메일 대응 전략: 문자열 변형 CASE STUDY / 제6회 Kakao Tech Meet |
| kakao/761 | 3,645 | 제외/회고·문화·행사 | - | 0/0 | 실패를 장려하는 실험적 문화 |
| kakao/762 | 13,811 | 사례/실험·활용기 | case_0018 | 0/9 | 생산성 혁신의 실험: AI 마일리지 프로그램 |
| kakao/770 | 16,500 | 사례/기술 선택·도입형 | case_0015 | 0/13 | 5년 된 프로젝트의 빌드 도구를 교체하며 얻은 것들 |
| kakao/784 | 8,710 | 사례/기술 선택·도입형 | case_0016 | 0/14 | 단 1시간 만에 99개의 MVP가? AI와 함께한 1K: 바이브코딩전 생생 후기 |
| kakao/785 | 4,597 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며 |
| kakao/804 | 3,760 | 사례/기술 선택·도입형 | case_0017 | 0/10 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/822 | 20,047 | 사례/실험·활용기 | case_0019, case_0020, case_0021, case_0022, case_0023 | 1/25 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakao/835 | 12,198 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 둘째 날, 기술 세션 소개 |
| kakaopay/slack-bot-improving-operational-efficiency-2 | 5,044 | 사례/기술 선택·도입형 | case_0038 | 0/12 | 카카오페이 배포 효율화 1년 회고: 자동화 도입과 팀 생산성 향상 |
| kakaopay/tech-strategy-tpm | 9,673 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이 TPM은 어떤 일을 하나요? |
| kakaopay/katfun-joy-kotlin | 14,709 | 사례/실험·활용기 | case_0034, case_0035, case_0036, case_0037 | 0/21 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kakaopay/ifkakao2024-devrel | 10,598 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스 준비 맛보기 |
| kakaopay/perftest_zone | 4,708 | 사례/기술 선택·도입형 | case_0033 | 0/13 | 카카오페이 성능 테스트 존을 소개합니다. |
| kakaopay/kakaopaysec-wecan | 8,650 | 사례/기술 선택·도입형 | case_0030, case_0031, case_0032 | 0/18 | We Can Do Better: 개발자 플랫폼 효율화 이야기 |
| kakaopay/kakaopayins-opensearch-analyzer | 10,157 | 사례/실험·활용기 | case_0027, case_0028, case_0029 | 0/20 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/kakaopayins-envelope-encryption | 18,389 | 사례/기술 선택·도입형 | case_0026 | 0/11 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/pallas-v2-log-platform | 25,659 | 사례/기술 선택·도입형 | case_0025 | 0/14 | 일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트 |
| kakaopay/kakaopayins-fe-common-component | 7,059 | 사례/기술 선택·도입형 | case_0024 | 0/6 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kurly/cart-recommend-model-development | 9,206 | 사례/문제 해결형 | case_0068 | 0/12 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 1부 |
| kurly/commit-mvcc-set-autocommit | 16,463 | 사례/문제 해결형 | case_0070 | 0/11 | 데이터가 있었는데요, 아니 없어요 |
| kurly/deliveryproductteam-culture-1 | 4,454 | 사례/문제 해결형 | case_0066 | 0/8 | 딜리버리 프로덕트 개발팀의 개발문화 - 로그 & 알람편 |
| kurly/connection-leak | 6,791 | 사례/문제 해결형 | case_0065 | 0/9 | 99%가 모른다는 DB Connection 누수 문제 |
| kurly/refine-address-internalization-2 | 4,312 | 사례/기술 선택·도입형 | case_0067 | 1/14 | 주소정제 서비스 내재화 - 2화 ( 그럴싸한 계획 ) |
| kurly/access-block-1 | 5,663 | 사례/문제 해결형 | case_0063 | 0/13 | nginx 설정 없이 우아하게 서비스 점검하기 (上) |
| kurly/access-block-2 | 8,383 | 사례/기술 선택·도입형 | case_0064 | 0/15 | nginx 설정 없이 우아하게 서비스 점검하기 (下) |
| kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0 | 13,290 | 사례/기술 선택·도입형 | case_0062 | 0/16 | 빌드가 터졌다: 5년 된 CMS 프로젝트의 Webpack4 → Vite 전환 |
| kurly/tech-spec-adoption-with-ai-automation | 8,164 | 사례/기술 선택·도입형 | case_0060, case_0061 | 0/18 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| kurly/claude-code-redesign-my-day | 7,389 | 사례/기술 선택·도입형 | case_0059 | 0/13 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| ly/managing-multi-cdn-logs-traffics-with-vector | 16,695 | 사례/개념·튜토리얼 | case_0056 | 0/11 | Vector를 활용해 멀티 CDN 로그 및 트래픽 관리하기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 18,813 | 사례/기술 선택·도입형 | case_0054, case_0055 | 0/18 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/improving-kubernetes-relay-api-server-performance-with-informer | 12,361 | 사례/문제 해결형 | case_0057 | 0/13 | Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기 |
| ly/introducing-fido2-client-sdk-open-source | 9,957 | 사례/기술 선택·도입형 | case_0051 | 0/9 | FIDO2 클라이언트 SDK 오픈소스 소개 |
| ly/how-to-evaluate-ai-generated-images-1 | 16,708 | 제외/개념·튜토리얼 | - | 0/0 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/extracting-trending-keywords-from-openchat-messages | 14,017 | 사례/문제 해결형 | case_0058 | 0/15 | 오픈챗 메시지들로부터 트렌딩 키워드 추출하기 |
| ly/pd1-ai-hackathon-recap | 4,153 | 제외/회고·문화·행사 | - | 0/0 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 6,232 | 사례/기술 선택·도입형 | case_0052, case_0053 | 1/28 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 및 서비스 상태 확인 도구 LINE Status 개발기 |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 19,601 | 사례/기술 선택·도입형 | case_0050 | 0/15 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/japanese-search-kuromoji-to-sudachi | 15,395 | 사례/기술 선택·도입형 | case_0048 | 0/16 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자가 좋아하는 과자는? |
| oliveyoung/2024-06-05_google-cloud-next-24-review | 3,796 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next '24 방문기 |
| oliveyoung/2024-08-11_type-and-type-system-with-typescript | 11,673 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 타입과 타입 시스템 |
| oliveyoung/2024-09-30_oy-feconf-2024 | 8,894 | 제외/회고·문화·행사 | - | 0/0 | 올리브영에서는 프론트엔드 개발자들이 이런 고민을 하는군요? |
| oliveyoung/2024-10-17_oy-delivery-mq | 4,642 | 사례/기술 선택·도입형 | case_0076 | 0/11 | 올리브영 물류시스템에서는 데이터를 어떻게 주고 받을까? |
| oliveyoung/2024-12-16_Design-System-Token-Automation | 17,955 | 사례/기술 선택·도입형 | case_0077 | 0/12 | 디자인 시스템 중 디자인 토큰을 여러 도구를 이용하여 자동화 하는 방법 |
| oliveyoung/2024-12-17_catalog-mongo-transaction-2 | 11,450 | 사례/문제 해결형 | case_0074, case_0075 | 0/19 | Spring Boot MongoDB 트랜잭션 도입 실전 가이드 |
| oliveyoung/2025-02-14_oy-global-mall-address | 4,978 | 사례/기술 선택·도입형 | case_0071 | 0/12 | 올리브영 글로벌몰 주소 자동완성 및 검증 솔루션 도입기 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 7,158 | 사례/기술 선택·도입형 | case_0072, case_0073 | 0/20 | Web Worker로 이미지 처리 최적화하기 |
| oliveyoung/2025-06-10_chaos | 7,289 | 사례/기술 선택·도입형 | case_0069 | 0/14 | 버그가 아니라 장애를 잡아라!! QA와 카오스 엔지니어링의 만남 |
| toss/27752 | 5,980 | 사례/문제 해결형 | case_0005 | 0/10 | 드래그 앤 드롭은 사실 편한 UX가 아니다? |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | - | 0/0 | 오픈소스에 기여하고 토스에 합격한.ssul \| EP.4 모닥불 |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | - | 0/0 | 개발자 리더로서 성장당한 썰 \| EP.7 모닥불 |
| toss/toss-frontend-ai-docs | 2,869 | 사례/기술 선택·도입형 | case_0007 | 1/13 | 토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유 |
| toss/toss-people-3 | 7,801 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 문과생에서 토스 개발 리더까지 |
| toss/frontend-esbuild-hmr | 10,415 | 사례/문제 해결형 | case_0002 | 0/11 | ESBuild를 위한 HMR, 직접 만들기 |
| toss/frontend-apply-without-resume | 2,783 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드에 이력서 없이 리포지토리 링크로 지원하세요 (~5/31) |
| toss/toss-securities-gpu-mig | 13,794 | 사례/기술 선택·도입형 | case_0004 | 1/17 | GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기 |
| toss/tds-color-system-update | 13,423 | 사례/기술 선택·도입형 | case_0001 | 0/13 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| toss/ads_dashboard_fe | 12,467 | 사례/기술 선택·도입형 | case_0003 | 0/16 | 전체 데이터를 브라우저에 두는 광고 대시보드 만들기 |
| woowahan/14484 | 5,518 | 사례/문제 해결형 | case_0013 | 0/12 | “일단 백로그에 넣어두고 여유 있을 때 보는 걸로 할까요?” : 백로그를 백로그로 두지 않는 법 |
| woowahan/14671 | 6,108 | 제외/회고·문화·행사 | - | 0/0 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/15398 | 10,772 | 사례/실험·활용기 | case_0014 | 0/14 | Java의 미래, Virtual Thread |
| woowahan/15541 | 6,445 | 제외/개념·튜토리얼 | - | 0/0 | 웹 접근성 준수를 통한 모두에게 배달되는 일상의 행복 |
| woowahan/17386 | 11,245 | 사례/기술 선택·도입형 | case_0011 | 0/10 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/17911 | 4,799 | 사례/기술 선택·도입형 | case_0010 | 0/14 | B마트 주문 유실을 없애보자: 네트워크 편 |
| woowahan/20763 | 8,615 | 사례/기술 선택·도입형 | case_0009 | 0/14 | 이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기 |
| woowahan/21027 | 25,102 | 사례/기술 선택·도입형 | case_0012 | 1/13 | 실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법 |
| woowahan/24434 | 15,179 | 사례/문제 해결형 | case_0006 | 0/12 | “함께 구매하면 좋은 상품” 추천 모델 고도화 |
| woowahan/24999 | 12,341 | 사례/문제 해결형 | case_0008 | 0/17 | WOOWACON 2025 미니게임 WOOWA POP! |
