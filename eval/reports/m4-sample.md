# 추출 점검 리포트: data

- 모델: gpt-5.6-luna (medium)
- 프롬프트 버전: 5bafd9ddcc5d
- 글 220편: 추출 162, 제외 58
- 항목 250개
- 토큰: 호출 432회, 입력 3,431,632 (캐시 1,384,537), 출력 477,345 (reasoning 154,787)
- 비용: $1.010 (편당 $0.0046), 전체 1,262편 추정 $5.8 / Batch $2.9

## 블로그별 추출 여부

| 블로그 | 추출 | 제외 | 항목 수 |
| --- | --- | --- | --- |
| d2 | 12 | 13 | 23 |
| kakao | 13 | 12 | 26 |
| kakaopay | 20 | 5 | 28 |
| kurly | 24 | 1 | 34 |
| ly | 19 | 6 | 29 |
| oliveyoung | 36 | 9 | 51 |
| toss | 19 | 6 | 31 |
| woowahan | 19 | 6 | 28 |

## 글 유형 × 추출 여부

| 글 유형 | 추출 | 제외 |
| --- | --- | --- |
| 개념·튜토리얼 | 0 | 11 |
| 기술 선택·도입형 | 32 | 1 |
| 문제 해결형 | 89 | 1 |
| 실험·활용기 | 41 | 3 |
| 회고·문화·행사 | 0 | 42 |

## 짧은 글 (평문 1,500자 미만) 19편

| 글 | 길이 | 결과 | 항목 | 분류 이유 |
| --- | --- | --- | --- | --- |
| d2/5053838 | 607 | 제외/개념·튜토리얼 | 0 | RocksDB와 LSM Tree의 개념 및 기능을 소개하는 사내 발표 영상 공개 글로, 구체적인 기술 문제 해결 과정이나 적용 결과·설계 근거가 본문에 제시되지 않았습니다. |
| d2/3461887 | 842 | 제외/문제 해결형 | 0 | Crash 분석 시스템의 문제와 아키텍처를 다룬 세션으로 보이지만, 본문에는 구체적인 해결 근거나 설계·성능 비교 내용이 서술되지 않고 발표 주제 목록과 행사 소개만 제시되어 있어 제외합니다. |
| d2/5564264 | 522 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션 공개를 안내하는 글이며, 본문에 구체적인 문제 해결 과정이나 설계 근거·적용 결과가 제시되지 않고 목차만 나열되어 있다. |
| d2/7030870 | 571 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, 디자인 시스템 구축 주제와 목차만 제시되어 있으며 구체적인 적용 과정·문제 해결·비교 근거가 본문에 없다. |
| d2/2905424 | 868 | 제외/개념·튜토리얼 | 0 | Kubernetes DNS 구성 요소와 질의 동작 방식을 설명하는 발표 자료 소개 글이며, 특정 팀이 겪은 문제의 해결 과정이나 구체적인 적용 결과·설계 근거가 본문에 제시되지 않았습니다. |
| d2/7282210 | 534 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 공개하며 목차와 행사 소개만 제시하고, 로그 문제의 해결 근거나 구체적인 설계·적용 결과는 본문에 설명하지 않는다. |
| d2/1536585 | 654 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, Hazelcast 도입 배경·구성·모니터링 등의 목차만 제시되어 있고 구체적인 문제 해결 과정이나 도입 근거·적용 결과가 본문에 서술되어 있지 않다. |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | 0 | C++의 data race, happens-before, thread safety, 동기화 프리미티브 등 기본 개념과 사용법을 설명하는 행사 발표 자료 소개 글이며, 특정 팀의 기술 문제 해결이나 실제 적용 결과는 제시하지 않습니다. |
| d2/4706492 | 1,246 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표를 소개하는 글이며, 본문에는 구체적인 구현 과정·성능 비교·설계 근거보다 발표 목차와 행사 안내만 제시되어 있습니다. |
| d2/8992409 | 1,342 | 제외/실험·활용기 | 0 | DBT·Airflow를 활용한 Flow.er 개발과 적용을 다룬 세션이지만, 본문에는 구체적인 문제 해결 과정·비교 근거·설계 결정 없이 발표 주제와 목차만 소개되어 있어 기술 사례로 추출하기 어렵습니다. |
| d2/9290684 | 978 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 영상과 세션을 소개하는 글로, Iceberg·Materialized View 등의 구체적인 문제 해결 과정이나 설계 근거·성능 수치가 본문에 제시되지 않고 목차 수준으로만 나열되어 있습니다. |
| d2/9290861 | 796 | 제외/개념·튜토리얼 | 0 | VictoriaMetrics의 내부 구조와 구성 요소를 설명하는 발표 자료 소개 글이지만, 특정 팀의 기술 문제 해결 과정이나 도입·운영 결과, 구체적인 설계 근거가 본문에 제시되지 않았습니다. 사내 행사 세션 공개 및 목차 중심의 내용이므로 제외합니다. |
| d2/4394359 | 837 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, Automatic Sharding의 문제 해결 과정이나 설계 근거·도입 결과가 본문에 구체적으로 제시되지 않고 목차만 나열되어 있습니다. |
| kakao/624 | 787 | 제외/회고·문화·행사 | 0 | Kakao Tech Meet 발표 영상과 발표자 인터뷰를 소개하는 행사 후기 성격의 글이며, 문자열 변형 스팸 대응의 구체적인 설계·문제 해결 과정이나 적용 결과는 본문에 제시되지 않았습니다. |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | 0 | 개발자들의 간식 선호도를 설문하고 결과를 공유하는 조직 문화·구성원 대상 콘텐츠로, 기술 문제 해결이나 기술 도입·활용에 관한 실무 내용이 없습니다. |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | 0 | 토스 구성원의 오픈소스 기여 경험과 기술적 성장에 관한 영상 소개 및 대담 형식의 글이다. 구체적인 문제 해결 과정이나 설계·구현 근거보다 출연진과 타임스탬프, 주제 소개가 중심이므로 기술 사례로 추출하지 않는다. |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | 0 | 프론트엔드 리드들의 리더십 성장 고민과 경험을 다루는 조직·리더십 대담으로, 구체적인 기술 문제 해결이나 기술 도입·적용 사례가 중심이 아니다. |
| woowahan/19317 | 1,157 | 제외/회고·문화·행사 | 0 | 우아한테크세미나의 다시보기와 강연 주제·목차를 소개하는 행사 안내 글이다. 생성형 AI와 로컬 LLM 활용 사례가 나열되어 있지만, 구체적인 문제 해결 과정이나 설계 근거·적용 결과는 본문에 제시되지 않았다. |
| woowahan/20789 | 333 | 제외/회고·문화·행사 | 0 | 기술 콘퍼런스 발표 영상 공개를 안내하는 행사 홍보 글이며, 구체적인 기술 문제 해결 과정이나 설계·도입 근거를 다루지 않는다. |

## 글당 항목 수 (제외 글 빼고)

| 항목 수 | 글 수 |
| --- | --- |
| 1 | 111 |
| 2 | 19 |
| 3 | 27 |
| 4 | 5 |

## 문제 유형 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 개발 생산성 | 65 | 26% |
| 장애 대응·복구 | 52 | 21% |
| 데이터 정합성·트랜잭션 | 36 | 14% |
| 모니터링·관측성 | 34 | 14% |
| 데이터 파이프라인 | 32 | 13% |
| API 설계·외부 연동 | 28 | 11% |
| DB 성능·쿼리 최적화 | 28 | 11% |
| 비용 절감 | 23 | 9% |
| 트래픽 급증 대응 | 23 | 9% |
| 인프라·컨테이너 | 23 | 9% |
| 업무·운영 자동화 | 23 | 9% |
| 메시징·비동기 처리 | 22 | 9% |
| 배포·CI/CD | 18 | 7% |
| 테스트 자동화 | 17 | 7% |
| 인증·보안 | 16 | 6% |
| MSA | 15 | 6% |
| 클라이언트 성능(웹·앱) | 14 | 6% |
| 캐싱 | 12 | 5% |
| 동시성·락 | 9 | 4% |
| DB 마이그레이션·샤딩 | 7 | 3% |

- 한 번도 안 쓰인 분류 (0개): 없음

## 도메인 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 커머스·주문·재고 | 76 | 30% |
| 사내 플랫폼·개발 도구 | 72 | 29% |
| LLM·AI | 32 | 13% |
| 배달·물류 | 28 | 11% |
| 결제·금융 | 27 | 11% |
| 범용 | 20 | 8% |
| 검색·추천 | 18 | 7% |
| 콘텐츠·미디어 | 12 | 5% |
| 채팅·메시징 서비스 | 10 | 4% |
| 광고·마케팅 | 4 | 2% |

- 쏠림(30% 초과): 커머스·주문·재고
- 한 번도 안 쓰인 분류 (0개): 없음

## 발췌 검증

- 채택한 시도 기준 발췌 2379개 중 탈락 14개 (원문 존재율 99%)
- 재시도한 글 50편

- `kakao/777`: SnapshotQuery SPI를 구현해 최신 데이터만 조회하도록 스냅샷 쿼리를 직접 작성할 수 있습니다.
- `kurly/2024-spring-kafka-consumer-offset-seeking`: AbstractConsumerSeekAware를 상속한 컨슈머를 사용하면, 토픽 파티션 별로 쉽게 등록하고 제거할 수 있습니다.
- `ly/check-mp4-file-has-audio-using-filereader-in-front-end`: 동영상 섬네일에 오디오 존재 여부를 표시해야 하기 때문에 확인에 시간이 오래 걸리면 안 됩니다.
- `ly/migrate-mysql-with-read-only-mode`: 이전 완료 후에도 문제가 없는지 하루 정도 모니터링했는데요. 아무 문제도 발생하지 않았습니다.
- `ly/4-patterns-of-global-collaboration`: 민감한 개인정보를 다루는 서비스에서는 어쩔 수 없이 이 패턴을 사용하는 경우가 많습니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 따라서 공통 발생 빈도가 높은 키워드들은 동시에 선택되지 않도록 조정이 필요합니다.
- `ly/solving-slow-queries-optimizing-bitwise-operation-queries-with-functional-indexes`: 원인을 분석해 보니 인덱스 생성 작업 때문에 메인 DB에서 복제 DB로 복제하는 데 걸리는 지연 시간이 평소보다 증가했는데, 쓰기는 메인 DB에서, 읽기는 복제 DB에서 수행되다 보니 최신 데이터가 즉시 조회되지 않은 것이었습니다.
- `ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status`: 온콜에서 수신하는 알람을 그대로 반영할 것인지 혹은 오류 예산 기반으로 표현할 것인지 등을 검토했는 데요.
- `ly/from-hive-to-iceberg-12x-faster-data-updates`: 이 글의 제목이기도 한 '12배 속도 향상'은 기존에 1시간(60분) 주기로 돌던 데이터 반영 작업을 5분으로 단축하면서 얻어낸 결과입니다.
- `oliveyoung/2023-09-18_oliveyoung-coupon-rabbit`: 하지만 저희 스쿼드는 세일기간 혹은 특정 이벤트마다 scalability한 유연한 구조로 운영이 이루어지기 때문에 확장 이후 축소가 불가한 Kafka의 파티션 정책은 저희와 맞지 않았습니다.
- `oliveyoung/2024-06-12_goods-detail-description-improvement-par2`: - Lambda(Public) 를 통하여 외부 이미지 스크래핑 및 S3에 업로드
- `oliveyoung/2024-09-11_introduce-oy-ai-bedrock`: - 처리 시간: 이미지 업로드부터 검수 완료까지 5초 이내
- `oliveyoung/2026-09-14_global-store-new-way-of-working`: 이번에는 세 역할이 같은 테이블에 앉아 동시에 시작했습니다. 기획서(최소 스펙)를 입력으로 세 가지 초안을 AI로 뽑았습니다.
- `woowahan/20763`: 장점
– 범용적인 설계

단점
– 캐시 레이어 관련 비용 발생
– 작업량이 많음

## 기술 사전에 없는 이름 277종

- GitHub (5)
- Jira (5)
- Figma (4)
- LLM (4)
- Storybook (4)
- Iceberg (4)
- Webpack (4)
- GuardDuty (3)
- Git (3)
- Vite (3)
- Rollup (3)
- Locust (3)
- Codex (3)
- SonarQube (3)
- VictoriaMetrics (3)
- Central Dogma (3)
- AWS ECS (2)
- Web Worker (2)
- Yarn (2)
- Vector (2)
- Node2Vec (2)
- Transformer (2)
- Netty (2)
- Google Sheets (2)
- LM-SPT (2)
- YARN (2)
- Babel (2)
- Dokka (2)
- Hive (2)
- Confluence (2)
- HDFS (2)
- xDS (2)
- PyTorch (2)
- Tailwind CSS (2)
- Hubot (2)
- Nx (2)
- Bun (2)
- Apollo Client (2)
- Google Groups (1)
- NVIDIA Tesla T4 (1)
- Smithery (1)
- desktop-commander (1)
- pnpm (1)
- vitest (1)
- jest (1)
- Bugsnag (1)
- Firebase Crashlytics (1)
- IPS (1)
- WAF (1)
- AWS WAF (1)
- Wazuh (1)
- Falco (1)
- Falco Sidekick (1)
- Token Studio (1)
- Style Dictionary (1)
- H100 (1)
- H200 (1)
- MIG (1)
- nvidia-device-plugin (1)
- dcgm-exporter (1)
- Spark Operator (1)
- Zod (1)
- ESBuild (1)
- SWC (1)
- react-refresh (1)
- MDX (1)
- OAS (1)
- remark (1)
- Amazon EC2 (1)
- Express (1)
- @tossteam/tds (1)
- @tosspayments/log-tds (1)
- @tosspayments/log-core (1)
- @tosspayments/log-react (1)
- i18next (1)
- react-i18next (1)
- ESLint (1)
- eslint-plugin-i18next (1)
- typescript-eslint (1)
- ArchUnit (1)
- Lombok (1)
- Lucene (1)
- Claude Design (1)
- Figma Make (1)
- Claude Cowork (1)
- FastAPI (1)
- SQLite (1)
- IntelliJ (1)
- ELECTRA (1)
- WebAssembly (1)
- Rust (1)
- Amazon RDS for PostgreSQL (1)
- pgvector (1)
- Item2Vec (1)
- SASRec (1)
- LTE 라우터 (1)
- IPSEC (1)
- OpenFeign (1)
- Aho-Corasick (1)
- GitLab (1)
- S2 Geometry (1)
- AWS ALB (1)
- fastutil (1)
- Hazelcast (1)
- Chronicle Map (1)
- Spring Cloud (1)
- AWS Athena (1)
- Kanana-2 (1)
- Apps Script (1)
- clasp (1)
- Google Analytics (1)
- MockK (1)
- MockMvc (1)
- MockServer (1)
- LocalStack (1)
- Testcontainers (1)
- Whisper (1)
- Kanana-a (1)
- Codex CLI (1)
- JMH (1)
- JFR (1)
- async-profiler (1)
- Strimzi (1)
- Qwen2.5-Coder (1)
- DeepSeek-R1-Distill-Qwen (1)
- Pydantic (1)
- ORC (1)
- Jest (1)
- Vitest (1)
- Spring MVC (1)
- HyperDX (1)
- Amazon Athena (1)
- Filebeat (1)
- Lighthouse (1)
- Chrome (1)
- ts-node (1)
- tsconfig-paths (1)
- Megatron-LM (1)
- Open-RLHF (1)
- verl (1)
- Hugging Face Transformers (1)
- Cutlass (1)
- AES (1)
- RSA (1)
- AWS KMS (1)
- CloudTrail (1)
- PlantUML (1)
- InfluxDB (1)
- GCP (1)
- Apache Lucene (1)
- OpenSearch Dashboards (1)
- Kotlin Arrow (1)
- KEDA (1)
- sonar-java (1)
- sonar-kotlin-plugin (1)
- Spinnaker (1)
- Cilium (1)
- Hubble (1)
- Argo (1)
- Mockito (1)
- AssertJ (1)
- Avro (1)
- Schema Registry (1)
- Talend Open Studio (1)
- mongoimport (1)
- Microsoft Excel (1)
- Chromium (1)
- RxKotlin (1)
- JDBC (1)
- Exposed (1)
- react-window (1)
- XBU (1)
- CLOUS3.0 (1)
- Nexus (1)
- Release Please Action (1)
- JFrog Artifactory (1)
- Maven Central Repository (1)
- Vanniktech Maven Publish Plugin (1)
- GitHub Pages (1)
- Ruler (1)
- datasource-proxy (1)
- MySQL Connector/J (1)
- Kuromoji (1)
- Sudachi (1)
- NumPy (1)
- Kubeflow (1)
- JuiceFS (1)
- Fio (1)
- Envoy (1)
- Armeria (1)
- LiteRT (1)
- ONNX2TF (1)
- ZSTD (1)
- HeadlessUI (1)
- Flutter Web (1)
- Firebase (1)
- DeployGate (1)
- TestFlight (1)
- Deno (1)
- flutter_inappweb (1)
- platform_maps_flutter (1)
- google_maps_flutter (1)
- device_preview (1)
- ABC User Feedback (1)
- MinHash (1)
- FIDO2 (1)
- WebAuthn (1)
- Android (1)
- iOS (1)
- Decaton (1)
- Kubernetes Go client (1)
- etcd (1)
- Ansible (1)
- Cassandra (1)
- Akamai (1)
- FileReader (1)
- Taskmaster (1)
- WebView (1)
- Obsidian (1)
- QMD (1)
- iTerm (1)
- npm (1)
- Dependabot (1)
- Notion (1)
- MobX (1)
- Material-UI (1)
- PostCSS (1)
- esbuild (1)
- qs (1)
- react-csv (1)
- dayjs (1)
- @vitejs/plugin-react (1)
- vite-plugin-babel (1)
- rollup-plugin-visualizer (1)
- YOLO (1)
- Ultralytics (1)
- NestJS (1)
- Fastify (1)
- Apollo Server (1)
- graphql-codegen (1)
- BigQuery (1)
- Swagger (1)
- Postman (1)
- 행정안전부 도로명주소 조회 API (1)
- 행정안전부 좌표정보 API (1)
- Gson (1)
- MariaDB (1)
- AWS EC2 (1)
- MemoryAnalyzer (1)
- mysql-connector-j (1)
- Apache POI (1)
- MariaDB Connector/J (1)
- BERT4Rec (1)
- MLflow (1)
- Gradio (1)
- GrowthBook (1)
- AI Studios (1)
- Vrew (1)
- Adobe Premiere Pro (1)
- Module Federation (1)
- @module-federation/nextjs-mf (1)
- @tanstack/react-query (1)
- @tanstack/core (1)
- Jotai (1)
- Panda CSS (1)
- AWS ECR (1)
- AWS S3 (1)
- Tokens Studio for Figma (1)
- token-transformer (1)
- mitmproxy (1)
- OffscreenCanvas (1)
- Spring Data MongoDB (1)
- WiredTiger (1)
- WinForm (1)
- WPF (1)
- Google Forms (1)
- React Hook Form (1)

## 버린 대안 236개 (항목 250개 중)

- `case_0033` DLQ: 실패 원인 추적과 개별 재처리 제어가 어렵고 운영 가시성이 낮아 선택하지 않았다.
- `case_0035` 배치 수행 플래그 폴링: 단일 인스턴스에서는 유효하지만 다중 인스턴스 환경에서 폴링 지연과 상태 확인 비용이 발생한다.
- `case_0039` 규칙 기반 시스템: 자연스럽고 다양한 추천 문구를 생성하기에는 품질과 확장성에 한계가 있었다.
- `case_0039` 상용 LLM API: 모델 업데이트에 따른 응답 변화와 긴 프롬프트의 토큰 비용·응답 지연, 호출량 증가에 따른 비용 급증을 통제하기 어려웠다.
- `case_0039` Gemma2-2B: Gemma 3 출시 후 성능과 다국어 지원 면에서 Gemma3-4B가 더 적합하다고 판단해 변경했다.
- `case_0039` HyperCLOVA X ← HyperCLOVA X SEED 3B: 한국어 성능은 우수했지만 MAU 기반 라이선스 제약으로 서비스 적용이 어렵다고 판단했다.
- `case_0039` Qwen 2.5/3 시리즈: 벤치마크 성능은 우수했지만 실제 한국어 오타 정정 성능이 상대적으로 낮아 리뷰 기반 생성 Task에 부적합했다.
- `case_0041` 상품 정보 수작업 정합성 보정: 운영 로그를 대조하고 누락된 상품 번호를 추출해 강제 업데이트해야 하므로 시간 지연과 휴먼 에러 가능성이 있었다.
- `case_0043` Kafka Streams Join: 초기 프로모션 정보까지 포함한 재고 관리가 복잡한 비즈니스 관계로 간소화되면서 품절 시스템에는 조인을 사용하지 않고 상품 분류별 재고 토픽 필터링으로 대체했다.
- `case_0045` Cursor: Cursor에 대한 PoC는 진행 중이지만 아직 전사 도입 단계가 아니어서 Amazon Q를 대안으로 선택했다.
- `case_0046` Lua 스크립트: 미발급과 과발급은 0건으로 해결했지만 처리량이 약 21% 감소하고 Redis 단일 스레드 특성상 병목 및 운영 복잡도가 증가해 최종 채택하지 않았다.
- `case_0047` 인스턴스 증설: 메모리를 늘려도 이미 unsynchronized 상태가 된 미러링을 복구하지 못해 근본적인 해결책이 되지 못했다.
- `case_0047` 브로커 재시작: Memory Alarm이 해소된 후에야 재시작할 수 있었고, 고부하·고메모리 상태에서 재시작하면 unsynchronized 상태가 재현될 수 있었다.
- `case_0047` Classic Mirrored Queue 유지: 메모리 부족 시 미러 동기화 실패와 메시지 소비 중단이 발생하는 구조적 한계가 있어 Quorum Queue로 전환했다.
- `case_0049` 단순 JWT: OAuth2 기반의 검증된 표준 프레임워크가 필요했기 때문에 채택하지 않았다.
- `case_0057` RangeAssignor Strategy: Partition이 ECS Task에 고르게 배분되지 않고 배포 때마다 불규칙하게 재할당되었다.
- `case_0062` Claude 3 Haiku: 일부 케이스에서 분류 목표를 달성하지 못했다.
- `case_0062` OpenAI API ← GPT-4: 대부분의 케이스에서 목표를 달성했지만 일부 복잡한 사례에서 오류가 발생했다.
- `case_0062` OpenAI API ← GPT-3.5 Turbo: 이미지 분석 기능을 지원하지 않았다.
- `case_0062` OpenAI API ← ChatGPT: 별도의 API 설정, 관리 및 모니터링이 필요했다.
- `case_0063` Hardcoding without MCP: 외부 API 구현을 직접 하드코딩하면 API 변경 시 결합도가 높아지고 재사용할 수 없다.
- `case_0063` Skill Explosion: Skill을 지나치게 잘게 나누면 모든 Skill의 메타데이터가 시스템 프롬프트에 상주해 컨텍스트 부담이 커진다.
- `case_0063` 동적 정보를 CLAUDE.md에 상시 반영: CLAUDE.md를 계속 수정해야 한다면 동적인 정보는 대화나 sub-agent context로 전달해야 한다.
- `case_0064` Virtual Scrolling: 한 번에 그리는 행이 100건이고 DOM 부하가 병목이 아니어서 현재 페이지네이션 UX에는 필요하지 않았다.
- `case_0064` IndexedDB 캐싱: 캐시 무효화 기준이 명확하지 않고, 세션 안에서만 데이터를 유지해도 해결하려던 문제를 모두 풀 수 있어 부수적인 버전 관리와 스키마 마이그레이션 비용을 피했다.
- `case_0065` 2~4시간 버퍼: 시간 기준을 두면 핫픽스의 목적과 충돌하므로 충분히 검토했는지에 집중하기로 했다.
- `case_0067` 번거로운 사후기록: 기록 부담을 높이면 핫픽스에 대한 자각이 생길 것이라 예상했지만, 실제로는 행동이 아니라 기록만 줄어들었다.
- `case_0071` IP 기반 접근 통제: 시간이 지날수록 허용 범위가 넓어지고 직무나 PC 변경이 자동 반영되지 않으며, 사용자 식별과 최소 권한 원칙 준수가 어려웠다.
- `case_0071` SSL-VPN: 재택근무 시 인터넷 보안이 적용되지 않을 수 있고, 공인 IP 노출과 내부 네트워크 노출 문제가 있었다.
- `case_0071` 백신 설치 검사: 가짜 파일 배치, 인증 후 백신 무력화, 백신 관리서버 통신 차단으로 검증을 우회할 수 있었다.
- `case_0072` 부분 팔레트 수정: 일부 컬러만 수정해도 다른 색상과 전체 명도 진행을 함께 재검토해야 했다.
- `case_0072` 컴포넌트 추가 제작: 새로운 화면과 패턴의 증가를 컴포넌트를 더 제작하는 방식만으로 따라가는 것은 지속 가능하지 않다고 판단했다.
- `case_0073` 클라우드 활용: 자체 클러스터를 운용하는 지속적 워크로드 환경에서는 비용이 더 발생할 수 있고, 보안·컴플라이언스와 GPU 제어에도 제약이 있다.
- `case_0073` 혼합 GPU 운영: GPU 세대·메모리 차이로 드라이버, CUDA, 프레임워크 호환성과 스케줄링 관리가 복잡해지고, 수요가 고용량 GPU에 편중되면 저용량 GPU가 유휴화될 수 있다.
- `case_0073` MPS: 소프트웨어 방식이라 리소스 간 격리가 어렵고 성능 간섭 및 프로세스별 리소스 관리 부담이 있다.
- `case_0074` 세부 유저 플로우 설계: 디테일을 모두 반영한 플로우는 리허설에서 제한 시간 안에 문제를 풀 수 없을 정도로 어려워져 가장 단순한 형태로 변경했다.
- `case_0074` 친구초대 리워드 모델: 친구 초대 인원에 따라 보상을 지급하는 전형적인 모델 대신, 공유해야 가격이 내려가는 규칙을 선택했다.
- `case_0075` base package 기준 정의: 모듈 단위로 동일한 패키지 구조를 사용할 수 있어 base package 스캔 방식 적용이 어려웠다.
- `case_0075` annotation 기반 정의: 서비스와 어드민 repository에 동일한 어노테이션을 중복 선언해야 해 설정 누락·중복과 복잡성이 발생할 수 있었다.
- `case_0075` base 모듈에 설정 통합: 각 설정이 어떤 서비스에 영향을 미치는지 명확히 구분하고 관리하기 어려워 모듈별 분리 방식을 선택했다.
- `case_0077` Istio consistent hash: consistent hash는 해시값으로만 Pod를 정해 서버의 실제 부하를 고려하지 못한다.
- `case_0077` Kyuubi: Kyuubi가 제공하는 인터페이스는 Thrift/JDBC 기반 SQL Only라 DataFrame API를 그대로 서비스해야 하는 요구를 충족하지 못한다.
- `case_0079` if문 기반 분기: 가맹점 요구사항이 늘어나면서 핵심 비즈니스 로직을 파악하고 특정 가맹점 요구사항을 추적하기 어려워졌다.
- `case_0082` 라이브러리 코드 커스텀: 요구사항이 라이브러리가 상정한 문제의 범위를 넘어설 때 라이브러리의 구조와 새로운 요구사항이 맞지 않거나 업데이트를 따라가기 어려워지는 문제가 있다고 판단했다.
- `case_0085` OAS description으로 파라미터 설명 관리: 문서 내용과 구조를 관리하는 테크니컬 라이터가 MDX를 직접 수정하는 편이 OAS 스키마를 수정하는 것보다 간단하고 빠르며, 문서 반영 시점을 자유롭게 조정할 수 있기 때문이다.
- `case_0086` aria-roledescription: 아이폰이 aria 1.3을 지원하지 않아 사용하지 않고 다른 ARIA 속성 조합으로 대응했다.
- `case_0086` button disabled 속성: 버튼을 disabled 처리하면 안드로이드에서 접근성 초점이 상단으로 튈 수 있어 사용하지 않았다.
- `case_0087` Express: Next.js SSR 서버의 요구사항에 비해 기능이 과하고 미들웨어 등의 아키텍처가 오버헤드를 만들어 제거했다.
- `case_0088` tsyringe: 당장에는 의존성을 주입할 수 있는 구조만 필요해 라이브러리 도입을 나중으로 미뤘다.
- `case_0088` inversify: 당장에는 의존성을 주입할 수 있는 구조만 필요해 라이브러리 도입을 나중으로 미뤘다.
- `case_0090` React.lazy 재시도 패턴: React 상태를 새로 만들어 import()를 다시 호출해도 브라우저 모듈 맵이 실패 결과를 반환해 네트워크 요청이 발생하지 않았다.
- `case_0090` 새로고침: document를 새로 만들어야 모듈 맵의 실패 기록을 지울 수 있지만, SPA 상태가 초기화되므로 영업 중인 웹뷰에서 사용할 수 없었다.
- `case_0090` 쿼리스트링 재시도: 화면 청크의 가장 바깥 import() 주소만 바꿀 수 있고, 내부의 정적 import가 가리키는 공유 청크 주소는 바꾸지 못했다.
- `case_0090` Service Worker: 코드 스플리팅된 파일이 대부분 10KB 이하라 캐시 이득보다 관리 비용이 컸다.
- `case_0090` modulepreload: 지원 하한이 Chrome 66이라 Chrome 51이 지원 하한인 웹뷰 환경에 적절하지 않았다.
- `case_0090` 정적 import: 당장의 장애는 해결했지만 모든 화면이 메인 번들에 포함되어 화면 수가 늘수록 번들이 무거워지는 문제가 남았다.
- `case_0092` eslint-plugin-i18next: 첫 번째 컨벤션에 일부만 맞고 옵션 조절로도 프로젝트의 요구사항을 충족하기 어려워 도입하지 않았다.
- `case_0092` 린트 자동 교정: 자연어를 기계적으로 교정하기 어렵고 AI 반자동 교정으로 충분하다고 판단해 구현하지 않았다.
- `case_0096` Logstash: JVM 기반으로 시스템 자원을 많이 사용해 경량 로그 파이프라인으로 대체했다. **(technologies에도 있음)**
- `case_0097` 별도 Elasticsearch 클러스터: 데이터센터별로 클러스터를 하나 더 구축하는 대신 하나의 클러스터로 묶는 방안을 선택했다.
- `case_0098` SQLite: 앱이 여러 서버로 복제되어 실행되면서 SQLite 파일과 데이터가 서버마다 따로 쌓였기 때문에 공유 DB로 교체했다.
- `case_0098` PostgreSQL: 행사 규모의 동시 제출에 충분하고 문제가 생겨도 사내에서 빠르게 대처할 수 있다는 팀 내 개발자 의견에 따라 MySQL을 선택했다.
- `case_0098` FastAPI: 사내 표준인 Kotlin으로 옮겨 배포하기 위해 Kotlin과 Spring Boot로 전환했다.
- `case_0098` handoff 링크만 전달: 동작은 살아나지만 색과 간격이 변형됐다.
- `case_0098` 디자인 화면(HTML)만 전달: 겉모습은 유지되지만 버튼 동작과 서버 연결이 빠졌다.
- `case_0099` 기존 감성 분석: 긍정과 부정만 판단해 리뷰에 담긴 추천의 무게감 차이를 구분하기 어려웠다.
- `case_0100` 코드 난독화: 코드 분석 시간을 지연시킬 뿐 매크로를 근본적으로 막지 못했다.
- `case_0100` CAPTCHA: 매크로는 막았지만 게임의 본질적인 재미를 반감시켰다.
- `case_0103` Atlas MongoDB: 2차 부하 테스트에서 RDS보다 처리량과 응답시간 측면의 성능이 낮아 최종 선택하지 않았다.
- `case_0103` OpenSearch: 부하가 최대치에 달한 뒤 요청 성능이 더 나아지지 않았고, 부하를 견디지 못해 500 오류가 발생해 최종 선택하지 않았다.
- `case_0106` 동일 회선 사업자 이중화: 지역 또는 전국 단위의 회선 사업자 장애 위험을 피하고 서로 다른 사업자로 이원화하기 위해 선택하지 않았다.
- `case_0106` 에그: 사용자 교육 비용과 네트워크 관리 비용이 증가해 운영 비용 측면에서 적합하지 않았다.
- `case_0107` 자동증가 ID 하드코딩: 운영환경과 테스트환경의 자동증가 ID가 달라 환경별로 값을 관리해야 하고, 신규 상품 등록 순서를 예측하면 잘못된 상품에 할인이 적용될 수 있다.
- `case_0107` findByKey() 직접 조회: 유니크 키로 조회하는 기능은 동작하지만 동일 트랜잭션에서 호출할 때마다 쿼리가 실행된다.
- `case_0108` 중앙 금칙어 검사 API: 여러 시스템이 검사할 때마다 중앙 시스템 API를 호출하면 막대한 트래픽이 발생할 수 있어 애플리케이션 내부에서 검사하는 라이브러리 방식을 선택했다.
- `case_0108` nori 형태소 분석기: 예상하지 못한 엣지 케이스가 발생하고 내부 사전을 확인하거나 확장하기 어려워 범용 검사 로직에 사용하지 않았다.
- `case_0108` String.contains 순회: 금칙어 목록을 순회하며 문자열을 검사하는 방식은 시간복잡도가 O(nm)으로 느려서 사용하지 않았다.
- `case_0109` Chromatic: 유료여서 제외했다.
- `case_0109` BackstopJS: 한글을 지원하지 않아 제외했다.
- `case_0111` Redis 캐시 구조: 기존 구조를 유지하는 2안을 선택하고 필요할 때 추가 캐시나 DB 레이어를 검토하기로 했다.
- `case_0112` 일반적인 Blue/Green 배포: 트래픽을 세밀하게 조절하기 위해 사용하지 않았다.
- `case_0113` GC 파라미터 튜닝: IHOP 등의 GC 튜닝보다 메모리 저장 구조 개선을 우선했다.
- `case_0113` Hazelcast: 단순 key value 조회 이상의 기능을 지원해 현재 데이터 특성에는 과하고, 진입 장벽과 낮은 이해도가 걱정됐다.
- `case_0113` Chronicle Map: 단순 key value 조회 이상의 기능을 지원해 현재 데이터 특성에는 과하다고 판단했다.
- `case_0113` HPPC: fastutil을 선택해 사용했다.
- `case_0113` Trove: fastutil을 선택해 사용했다.
- `case_0113` Koloboke: fastutil을 선택해 사용했다.
- `case_0118` ContentSlotPlate 중간 추가 모델: ContentSlotPlate 각각의 Version을 관리해야 한다는 요구사항을 놓쳐 최종 모델로 채택하지 않았다.
- `case_0120` 정식 DB: 접근 권한을 매번 새로 설계해야 하고 운영·보안 부담이 생겼다.
- `case_0123` @SpringBootTest: 테스트 피드백이 느리고 테스트 격리와 동시 실행이 어려워 제거했다.
- `case_0123` 라이브 외부 시스템 호출: 잘못된 데이터 누적 등으로 테스트의 결정성이 떨어질 수 있어 사용하지 않았다.
- `case_0123` fixture 프레임워크 도구: Object Mother가 더 가볍고 관리하기 편리하다고 판단했다.
- `case_0127` DPO: 고정된 선호 데이터만 사용해 현재 모델이 새로 생성한 실패 유형을 충분히 반영하기 어려웠기 때문에 온라인 강화학습을 선택했다.
- `case_0127` 단일 RM 점수 최적화: 말하기 스타일 보상만 최대화하면 발음 오류, 화자 음성 변화, 전반적인 오디오 품질 저하가 발생할 수 있어 다중 목표 최적화를 적용했다.
- `case_0128` 폭포수 방법론: 기획과 개발의 경계를 허물고 AI 기반 프로토타이핑과 PoC 중심 개발을 채택하기 위해 기존 방식을 대체했다.
- `case_0134` 사람 평가: 사람을 동원한 평가는 시간과 비용이 많이 들고 확장성이 제한되며, 복잡한 PR 코드 리뷰 태스크를 직접 평가하기 어렵다.
- `case_0138` Webpack: 성능 측면에서 다른 도구보다 선택 우선순위가 낮아 고려 대상에서 제외했다.
- `case_0138` Parcel: 복잡한 프로젝트 설정을 자동화하는 리스크가 있고 복잡한 커스터마이징에 제한이 있을 수 있다고 판단했다.
- `case_0140` snapshot.select.statement.overrides: 간단하지만 Debezium이 여러 테이블을 캡처하면 테이블마다 설정해야 하며, 파티션 테이블에서는 부모 테이블 적용 여부를 확인해야 한다.
- `case_0141` TimestampRouter: 데이터가 변경된 시점의 날짜를 사용하므로 과거 데이터가 변경될 때 새 인덱스에 중복 저장됐다.
- `case_0143` Filter: 대상 클래스를 알아낼 수 없어 Request 처리 방식으로 적용하지 않았다.
- `case_0143` Interceptor: 원본 Request의 Body를 변경하기 어려워 Request 처리 방식으로 적용하지 않았다.
- `case_0143` ResponseBodyAdvice: 데이터를 전달받은 후가 아니라 외부 전달 직전에 동작해 Response 케이스 변환 방식으로 사용하지 않았다.
- `case_0145` OpenSearch: 전문 검색에는 강하지만 비용이 높고 대용량 집계 쿼리가 느리다고 판단했다. **(technologies에도 있음)**
- `case_0145` Grafana Loki: 라벨 기반 필터링과 집계 기능, 카디널리티 및 쿼리 표현력 측면에서 요구사항에 맞지 않았다.
- `case_0145` Signoz: 자체 테이블 구조를 강제하고 LogAttributes Map 검색과 ClickHouse 테이블 커스터마이징을 충분히 지원하지 않았다.
- `case_0145` Amazon Athena: 2,000개 이상 컬럼을 테이블로 정의하기 어렵고, 콜드 스타트와 대용량 집계 쿼리 지연, 스키마 관리 부담이 있었다.
- `case_0146` 동적 import: CommonJS 환경에서 await를 async 함수 안에서 사용하기 위해 여러 코드 변경이 필요했다.
- `case_0146` Lighthouse cjs 진입점: index.cjs가 Gatherer와 Audit 클래스를 내보내지 않아 필요한 기능을 사용할 수 없었다.
- `case_0146` CommonJS·ESM 이중 패키지: share 패키지를 두 벌로 나누면 변경할 때마다 두 번 작업해야 했다.
- `case_0147` Vary: Origin: 이론적으로 해결할 수 있지만 CDN 서버 수정이 필요해 당장 적용할 수 없었다.
- `case_0147` crossOrigin: anonymous: 첫 번째 CORS 에러에는 적용했지만 다른 서비스에서 새로운 CORS 에러와 스타일 깨짐 현상이 발생해 운영 배포를 롤백했다.
- `case_0149` From-scratch 학습: 학습 시간과 비용을 절약하기 위해 기존 Dense LLM을 upcycling하는 방식을 선택했다.
- `case_0149` Intermediate dimension shuffling·50% 랜덤 초기화: 내부 실험에서 loss나 모델 성능 측면의 이득이 보이지 않아 적용하지 않았다.
- `case_0150` RLVR·RLGRM 동시 훈련: 두 훈련 방식의 최적 성능 도달 시점이 달랐다.
- `case_0153` Entity Lifecycle 콜백: 조회 후 복호화된 값이 1차 캐시의 원래 값과 달라져 조회할 때마다 암호화된 데이터가 다시 암호화되고 update 문이 발생했다.
- `case_0154` JPA Entity public 선언: 배치에서 직접 사용할 수 있도록 JPA Entity를 public으로 선언하는 방안도 고려했지만, 기존 설계 규칙을 컴파일러가 강제하지 못해 규칙 위반 가능성이 있다고 판단했다.
- `case_0158` Spring Retry: 스프링에 의존해야 하고 정확한 사용 방식을 익혀야 하는 제한점이 있어 Kotlin 고차함수로 재시도 로직을 직접 구현했다.
- `case_0164` CPU·Memory 기반 Replicas 추천: 서비스 대부분에서 배포 시점을 제외하면 CPU 편차가 크지 않고 메모리 사용량도 일관되어 트래픽 시간대별 Replicas 추천에 적합하지 않았다.
- `case_0167` fromUri 메서드 사용: java.net.URI가 폐지된 RFC 2396을 따르면서 payweb_tab을 host로 인지하지 못했다.
- `case_0171` Mock 적극 활용: 목킹 코드가 실제 테스트보다 많아지고 내부 구현 변경에 테스트가 쉽게 깨질 수 있어 목킹을 최대한 자제하는 방향을 선택했다.
- `case_0172` Json Converter: 메시지마다 스키마를 포함해 Kafka 로그 증가 폭과 OS 자원 사용 측면에서 비효율적이고, 스키마를 생략하면 Sink Connector가 CDC 처리를 할 수 없다.
- `case_0173` Relational Migrator: 테스트 결과 성능이 느리고 병렬 실행이 어려우며 초대형 테이블에 적합한지 의문이 있었고, 대규모 Job에 적합한 Kafka Model도 아직 일반 제공되지 않았다.
- `case_0174` AI 기반 월말 보고서 생성: 같은 데이터에서도 표현이 달라지고 회사 보고 형식과 맞지 않는 문장이 생겼으며, 모델 연결 문제로 공식 보고서 생성이 영향을 받을 수 있어 공식 숫자 결정 역할에서 제외했다.
- `case_0174` 캐릭터 중심 디자인: 재무팀 사용자에게 필요한 익숙함, 신뢰감, 공적인 인상과 전문성보다 귀여운 캐릭터가 앞선다고 판단해 네이버 디자인 시스템 기반의 차분한 ERP 스타일로 전환했다.
- `case_0174` 응답 후 필터링 중심 가드레일: AI가 모든 데이터를 조회한 뒤 답변에서 일부를 가리는 방식보다, 데이터와 도구에 접근하기 전 권한 경계를 적용하는 방식이 안전하다고 판단했다.
- `case_0175` Claude Code: 두 에이전트의 결과를 얻고 맞춰 볼 시간이 부족해 이번 평가에서는 사용하지 않았다.
- `case_0176` DOM 재구성 로직 제거·수정: 일부 개선 효과는 기대할 수 있지만, 어절 단위 렌더링과 채팅 UI의 점진적 렌더링으로 인한 구조적 LCP 문제는 남는다.
- `case_0177` reinterpret_cast 타입 퍼닝: uint32_t 객체를 float 포인터로 접근하면 엄격한 앨리어싱 규칙을 위반해 미정의 동작이 발생한다.
- `case_0177` union 타입 퍼닝: C++에서는 비활성 union 멤버를 읽는 방식이 표준을 준수하지 않는다.
- `case_0178` 주문 API 대량 유저 조회: 주문 API를 변경할 수 없다고 가정하고 클라이언트 측 병렬 처리를 선택했다.
- `case_0179` 문자열 기반 JDBC Execute Batch: 문자열 기반 SQL 관리와 자원 해제 코드를 반복해서 작성해야 하므로 Exposed를 도입했다.
- `case_0183` @tanstack/react-virtual: 복잡한 로그 표현 방식을 오픈소스로 대응하기 어렵고, 스크롤 바닥 감지 실패 원인 분석과 커스텀 기능 구현에도 어려움이 있어 자체 개발을 선택했다.
- `case_0192` ChainedTransactionManager: 전환 초기에는 Oracle과 MySQL의 정합성이 맞지 않고 MySQL 쿼리와 환경 설정이 검증되지 않았기 때문에 MySQL 쓰기를 분산 트랜잭션에 포함하지 않았다.
- `case_0192` 분산 트랜잭션: MySQL 쿼리만 실패하는 상황을 허용하고 Oracle 쿼리 수행에는 영향을 주지 않아야 했다.
- `case_0193` HTTP 트래픽 복사: 비즈니스 로직 호출 시 타 부서 시스템에 중복 호출 부하를 주거나 운영에 영향을 줄 위험이 있었다.
- `case_0193` Kafka 토픽 복제: 비즈니스 로직 호출 시 타 부서 시스템에 중복 호출 부하를 주거나 운영에 영향을 줄 위험이 있었다.
- `case_0195` 애플리케이션 모드: job마다 별도의 클러스터가 필요해 배포 시간이 늘어날 수 있고, 배포 타이밍에 downtime이 발생할 수 있어 세션 모드를 선택했다.
- `case_0197` 전체 일괄 전환: 중복 복제로 인한 DB 리소스 사용량 증가 위험이 있어 단계별 전환을 선택했다.
- `case_0198` 사용자 사전 수동 등록: 누락되는 신조어·복합어·모델명 변형을 계속 수동으로 등록해야 하므로 검색어 범위가 넓어질수록 지속 가능한 해결책이 되지 못했다.
- `case_0198` Elasticsearch 8.x 업그레이드: 사내 검색 플랫폼이 Elasticsearch 7.10.2까지만 지원하고 이후 버전 업그레이드 없이 일몰 방향으로 가고 있어 고려 대상에서 제외했다.
- `case_0199` QR 분해: 실제로 필요한 상삼각 행렬 R만 효율적으로 계산하기 위해 숄레스키 분해를 사용했다.
- `case_0200` 오류 예산 기반 상태 표현: 오류 예산 기반이 아닌 CUJ 기반 SLI 메트릭의 SLO 달성 여부를 상태 표현 기준으로 채택했다.
- `case_0201` 장비 업그레이드: 비용 문제와 서버 성능을 고려해 채택하지 않았다.
- `case_0201` 캐싱: 데이터 일관성을 유지하기 어려워 채택하지 않았다.
- `case_0201` 파티셔닝 세분화: 근본적인 해결책이 되지 못해 채택하지 않았다.
- `case_0202` GlusterFS·CephFS 직접 운영: 직접 운영하는 부담이 크다.
- `case_0202` AWS EFS·Google Filestore: Object Storage보다 비용이 크고 네이버 사내 환경에서 사용할 수 없다.
- `case_0202` DDN EXAScaler: 요구 사항을 만족하지만 큰 비용이 발생해 부분적으로만 도입했다.
- `case_0202` C3 HDFS 직접 사용: Kubernetes CSI Driver를 지원하지 않아 Kubernetes 영구 볼륨으로 사용할 수 없다.
- `case_0202` nubes Object Storage 직접 사용: POSIX API를 완벽히 지원하지 않고 Kubernetes CSI Driver를 지원하지 않는다.
- `case_0202` Ceph-rbd: ReadWriteMany와 ReadOnlyMany를 지원하지 않아 여러 Pod에서 동시에 접근할 수 없다.
- `case_0202` NFS: 확장성과 HA 문제가 있다.
- `case_0202` local-path: 동시 접근이 불가능하고 노드별 데이터 위치를 위한 추가 구현이 필요하다.
- `case_0202` Alluxio: 일부 POSIX API를 지원하지 않아 AI 오픈소스와 라이브러리를 정상적으로 사용하지 못할 수 있다.
- `case_0202` Alluxio 원본 저장소 동기화: 원본 저장소와의 동기화로 메타데이터 요청과 NameNode 부하가 증가할 수 있다.
- `case_0202` Alluxio 클러스터 운영: master와 worker 서버로 구성된 별도 클러스터 운영이 필요하고 전체 사용자에게 영향을 줄 수 있다.
- `case_0204` 쿠버네티스 외부 Envoy 사이드카 프락시: 별도의 프로세스를 운영해야 하고 구조가 복잡해지며, 네트워크 홉과 실패 지점이 추가된다.
- `case_0205` 번역 파이프라인: 번역 품질에 따라 검색 결과가 흔들리고 번역으로 지연 시간이 늘어났다.
- `case_0205` 다국어 모델 처음부터 학습: 데이터와 연산 비용이 너무 컸다.
- `case_0205` CoreML: iOS에서만 작동하고 모델 변환 호환성 문제가 있었으며 크로스 플랫폼 유지 보수 부담이 컸다.
- `case_0205` ai-edge-torch: 옵션이 부족하고 당시 불안정했으며 연산 대체가 제한적이었다.
- `case_0206` Spark Streaming: 마이크로 배치 방식으로 동작해 이벤트 시각을 기준으로 상태를 세밀하게 제어하기 어렵고, 데이터 최신성 판별과 정확히 한 번 처리를 동시에 만족하기 어려웠다.
- `case_0206` 네이티브 쿠버네티스: Flink 배포와 권한, 라우팅, 잡 구동 등의 설정을 수동으로 해야 해 운영이 번거로웠다.
- `case_0207` Non-keyed window: 단일 태스크로 작동해 처리량 증가 시 성능이 심각하게 저하됐다.
- `case_0208` Spark 온힙 메모리 증설: 온힙 메모리를 늘렸지만 메모리 압박이 해소되지 않았다.
- `case_0208` 공격적인 파일 병합 기준: 파일이 조금만 쌓여도 병합하도록 설정해 대규모 테이블에서 잦은 병합과 HDFS 과부하가 발생했다.
- `case_0208` 비파티션 테이블: 동등 삭제 파일이 글로벌 삭제로 적용되어 테이블의 모든 데이터 파일에 삭제 조건 매칭을 수행해야 했다.
- `case_0209` Ant Design: 기존 디자인이 적용된 외부 UI 라이브러리는 사용자 요구에 맞게 디자인이나 기능을 수정하기 어렵다고 판단했다.
- `case_0209` 커스텀 CSS: HeadlessUI보다 사전에 코드로 구현된 기술 지원이 적어 작업량이 많다고 비교했다.
- `case_0210` 최종 사용자용 Flutter Web: Flutter Web은 초기 구동 속도가 느리고 웹 환경에서 상용 서비스 수준으로 활용 가능한 도구가 부족해 내부 개발 확인 용도로만 사용하기로 했다.
- `case_0210` 모바일·웹 기능 완전 동일: 웹을 지원하지 않는 패키지가 있고 앱 기능 중 웹에 적절하지 않은 기능도 있어 일부 기능 제약을 공유하고 활용하기로 했다.
- `case_0210` 전체 개발 환경 웹 지원: 6개의 개발 환경 중 우선 하나의 환경만 웹에서 실행할 수 있는 수준으로 준비하고, 수요가 늘면 웹 빌드·배포 환경을 개선하기로 했다.
- `case_0210` 웹 환경 Firebase 기능 지원: 웹 앱 등록과 관리 범위가 늘어나므로 웹 환경에서는 Firebase 기능을 지원하지 않기로 했다.
- `case_0213` 거리 기반 클러스터링: 중복 메시지가 일부 제거되지 않거나 잘못 제거돼도 심대한 영향이 없어 더 간단한 방식을 선택했다.
- `case_0215` WebAuthn Level 3: Level 3는 공식적으로 확정되지 않은 초안이고, Level 2가 이미 W3C 공식 권고로 채택되어 있어 Level 2를 선택했다.
- `case_0216` 프로모션 도메인 포함: 프로젝트 초기에는 포함됐지만 최종적으로 정의한 다섯 가지 도메인에는 포함되지 않았다.
- `case_0219` Python 클라이언트: Python 클라이언트에서 Informer를 사용할 수 없다고 판단해 API 서버 구현 언어를 Go로 변경했다.
- `case_0222` 양쪽 IDC에 쓰기 허용: 데이터 정합성을 보장할 수 없고, 롤백 시 양쪽 데이터베이스의 정합성을 수동으로 맞춰야 해 복잡하고 많은 시간과 인력이 필요하다.
- `case_0222` 신규 IDC에만 쓰기 허용: 이전 중 데이터 정합성을 완전히 보장할 수 없고, 롤백 시 신규 IDC에 새로 기록된 내용을 기존 IDC로 옮기면서 쓰기 요청을 막아야 한다.
- `case_0224` Integer 방식: 순서 변경 시 하위 항목들의 순위값을 수정해야 하고 수정 범위가 크다.
- `case_0224` GreenHopper 방식: 순위값이 고갈되면 시스템을 중단하고 재조정해야 한다.
- `case_0224` Linked List 방식: 순서 변경 시 연결된 항목들을 수정해야 하고 목록 조회 시 전체 스캔이 필요하다.
- `case_0227` 브라우저별 오디오 API: 브라우저마다 API 이름이 달라 브라우저별 확인이 필요했고 Chrome API가 정확하지 않았다.
- `case_0227` Access-Control-Allow-Headers에 Range 필드 추가: iOS 16.0 이상 사용자의 비율이 높아 추가 수정 없이 기능을 적용했다.
- `case_0229` RAG SaaS: SaaS의 임베딩 모델에 의존하지 않고 외부 연동 및 과금 없이 로컬 환경에서 구축하기 위해 사용하지 않았다.
- `case_0230` 서브에이전트: 부모 에이전트와 컨텍스트를 공유해 부모 컨텍스트가 오염될 수 있으므로 중규모 이상 작업의 병렬 실행 방식으로 사용하지 않았다.
- `case_0233` generatePackageJson 비활성화: 배포 환경에서 별도 스크립트로 package.json을 생성해야 하므로 유지보수 부담이 생긴다.
- `case_0233` 커스텀 webpack 플러그인: 메타데이터를 직접 주입하는 방식은 유지보수 부담이 증가한다.
- `case_0234` AI의 MCP 직접 조회: 수집한 텍스트가 모두 토큰 비용으로 계산되어 2~3일치만 수집해도 비용과 속도가 급격히 악화됐다.
- `case_0234` 노션 수작업 정리: 한 땀 한 땀 정리하는 방식은 노동력으로 오래가지 못했다.
- `case_0236` 워크플로우별 규칙 관리: 워크플로우마다 같은 규칙을 따로 관리해야 해서 동일한 교정을 반복해야 했다.
- `case_0237` Parcel: 커스텀 제한이 있어 레거시 설정 대응에 불리했다.
- `case_0237` Rsbuild: 생태계가 작았다.
- `case_0239` nginx 라우팅 설정으로 차단: 개발팀에 실행 중인 인스턴스의 nginx 설정 파일 변경 및 nginx 재시작 권한이 없었고, 인프라 팀에 협조를 요청하면 점검 시간이 끝난 뒤에 차단될 가능성이 있었다.
- `case_0243` nginx 설정으로 차단: nginx가 모든 요청을 받는 리버스 프록시 구조가 아니고, 게이트웨이가 없으며, nginx 설정을 인프라팀이 도커 베이스 이미지와 함께 관리하기 때문에 인프라 상황에 적합하지 않았다.
- `case_0243` BigQuery 직접 질의: 페이지 라우팅이나 API 호출마다 BigQuery를 조회하면 네트워크 지연과 프로덕트 성능 저하가 발생할 수 있었다.
- `case_0243` 호출 횟수 기반 동기화: 트래픽 증감에 따라 동기화 주기를 예측하기 어려웠다.
- `case_0245` 재시도 로직: 행정안전부 API 장애 상황에서는 재시도해도 정상 응답을 받을 확률이 낮다고 판단해 제거했다.
- `case_0246` 동일 우편번호 범위 검색: 우편번호마다 영역이 천차만별이고 범위가 너무 넓어 실패했다.
- `case_0246` 동일 전체 도로명 코드 범위 검색: 우편번호보다 낫지만 여전히 검색 범위가 넓어 실패했다.
- `case_0246` 반경 기반 주변 건물 검색: 200~300미터 정도로 보수적으로 설정하면 동작하는 듯했지만 최종 채택하지 않고 보류했다.
- `case_0250` 필드 가시성 확대: 캡슐화 및 보안성 측면에서 바람직하지 않아 채택하지 않았다.
- `case_0251` HikariCP max-lifetime 증가: Connection 누수 자체는 방지할 수 있지만 DB failover 시 slave로 빠르게 연결하기 위해 max-lifetime을 작게 설정하고 있어 최종적으로 선택하지 않았다.
- `case_0253` 카프카 클러스터 권한: 권한을 얻어 Kafka CLI 오프셋 재설정 명령을 사용하는 방식은 컨슈머 그룹을 비활성 상태로 만들어야 하므로 무중단 오프셋 변경 요구 사항을 충족하지 못했다.
- `case_0253` Apache Kafka Admin API: alterConsumerGroupOffsets API는 작업 성공을 위해 컨슈머 그룹이 비어 있어야 하므로 무중단 오프셋 변경 요구 사항을 충족하지 못했다.
- `case_0255` READ COMMITTED 격리수준: 격리수준을 낮추면 Phantom Read가 발생해 기존 비즈니스 로직에 영향을 줄 수 있어 채택하지 않았다.
- `case_0255` 잠금 읽기: 행 잠금으로 인해 락 경합 및 데드락 발생 가능성이 증가할 수 있어 채택하지 않았다.
- `case_0257` 라인 타입 아이콘: 하단 탭바 아이콘과 시각적으로 충돌하고 시각적 강조에 한계가 있어 새로운 아이콘 스타일을 도입했다.
- `case_0258` 주문서 전체 활용 학습: 주문서의 모든 상품을 서로 보완재라고 가정해 그대로 학습했지만 특정 상품이 입력과 무관하게 반복 추천되었다.
- `case_0258` 수작업 카테고리 관계 설정: 사람이 카테고리 간 보완재 관계를 직접 설정하는 방식은 어렵고 객관적으로 평가하기 어렵다고 판단했다.
- `case_0261` 외주 영상 제작: 제작 비용과 기간이 제한된 상황에서 외주 제작은 선택지에서 제외했다.
- `case_0261` 단일 AI 툴: 단일 툴보다 3개 내외의 툴을 조합하는 방식이 제작 효율에 더 적합하다고 판단했다.
- `case_0261` Gamma: AI로 생성한 PPT 초안이 회사의 브랜드 컬러, 폰트, 레이아웃 요구사항과 맞지 않았다.
- `case_0264` 기존 데몬 폴링 주기 단축: 데이터베이스 부하만 늘리고 WAS 격리와 표준 모니터링 문제를 해결하지 못한다.
- `case_0264` 서버 한 대의 crontab 배치: 중복 방지를 위해 한 대만 운영해야 하고, 확장하려면 락이나 분산 처리를 직접 구현해야 한다.
- `case_0264` 테이블 기반 직접 큐: 메시지 큐가 제공하는 기능을 직접 구현해야 하고 전환 후 제거할 코드의 양과 정확성 책임이 늘어난다.
- `case_0264` CDC 없이 서비스별 직접 이벤트 발행: 수십 개 서비스와 저장 프로시저를 모두 수정해야 하는 빅뱅 전환이다.
- `case_0266` 집중형 데이터베이스 원인 분석 지속: Aurora MySQL 호환 버전 1의 수명 종료 준비가 임박해 두 방법 모두 진행하기 어려웠다.
- `case_0266` MySQL 5.7에서 5.6으로 다운그레이드: Aurora MySQL 호환 버전 1의 수명 종료 준비가 임박해 두 방법 모두 진행하기 어려웠다.
- `case_0266` ElasticCloud: 컬리의 인프라가 AWS 중심으로 구성되어 있어 AWS OpenSearch를 선택했다.
- `case_0266` MongoDB: 후기 내용과 상품 검색에는 OpenSearch의 역색인이 더 적합하다고 판단했다.
- `case_0266` EventSourcing Pattern: 이미 1억 건 가까운 데이터가 쌓여 있어 EventSourcing Pattern으로 변경하는 데 많은 시간이 들었다.
- `case_0270` Google DevTools Overrides: 향후 테스트를 프로세스화할 때 매번 수동 작업이 필요해 리소스가 과도하게 소모된다고 판단했다.
- `case_0270` Charles·Fiddler: 향후 테스트를 프로세스화할 때 매번 수동 작업이 필요해 리소스가 과도하게 소모된다고 판단했다.
- `case_0270` 실제 데이터 수정: API가 어떤 경우에 null 값을 넘겨주는지 정의되지 않아 데이터 수정으로 null을 전달하기 어렵다고 판단했다.
- `case_0271` WebP 변환: 복잡한 이미지에서는 압축 효율이 낮았고, 품질을 낮추면 시각적 품질이 저하되어 실제 적용에 제약이 있었다.
- `case_0271` Canvas 리사이징: 파일 크기와 업로드 속도는 개선됐지만 Canvas 처리 비용과 디코딩·인코딩 과정이 메인 스레드를 점유하고 클릭 이벤트 지연을 일으켰다.
- `case_0271` Shared Worker: 이미지 처리에 불필요한 기능이 많아 배제했다.
- `case_0271` Service Worker: 이미지 처리에 불필요한 기능이 많아 배제했다.
- `case_0272` WriteConcern MAJORITY: 모든 요청이 Secondary 과반수 ACK 응답을 기다려야 하므로 큰 오버헤드가 발생할 수 있다.
- `case_0272` ReadPreference PRIMARY: 모든 읽기 트래픽을 PRIMARY에 집중시켜 SECONDARY 노드가 유휴 상태로 남을 수 있다.
- `case_0273` SQS 메시지 지연 전달: 지연 시간이 너무 짧으면 타이밍 문제가 다시 발생할 수 있어 임시방편에 불과하다.
- `case_0273` Outbox 패턴: 데이터와 메시지를 분리해 관리할 수 있지만 현재 상황에서는 설계 및 구현에 걸리는 시간과 비용이 부담된다.
- `case_0273` 로그 테일링 패턴: 현재 상황에서는 설계 및 구현에 걸리는 시간과 비용이 부담된다.
- `case_0279` Formik: 각 영역의 상태를 정의하고 change 이벤트로 상태를 업데이트해 입력할 때마다 렌더링이 발생할 수 있다.

## 글 목록

| 글 | 길이 | 결과 | 항목 | 발췌 탈락 | 제목 |
| --- | --- | --- | --- | --- | --- |
| d2/5053838 | 607 | 제외/개념·튜토리얼 | - | 0/0 | Local key-value 스토리지가 고민일땐 RocksDB 어때? |
| d2/3461887 | 842 | 제외/문제 해결형 | - | 0/0 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics |
| d2/4555524 | 18,452 | 추출/기술 선택·도입형 | case_0202 | 0/23 | AI 플랫폼을 위한 스토리지 JuiceFS 도입기 |
| d2/5564264 | 522 | 제외/회고·문화·행사 | - | 0/0 | 쿠버네티스 네이티브 사이드카 컨테이너 (Sidecar Containers) |
| d2/7030870 | 571 | 제외/회고·문화·행사 | - | 0/0 | 디자인시스템을 개발에서 적용 하는법 |
| d2/2905424 | 868 | 제외/개념·튜토리얼 | - | 0/0 | Kubernetes에서 DNS 다루는 방법 - 도메인을 찾아서 |
| d2/7282210 | 534 | 제외/회고·문화·행사 | - | 0/0 | 보낼 로그가 1000개가 되는동안 겪었던 고민들 |
| d2/1536585 | 654 | 제외/회고·문화·행사 | - | 0/0 | 신규 프로젝트 Hazelcast 도입기 |
| d2/7269246 | 6,386 | 추출/실험·활용기 | case_0188 | 0/12 | [DAN 24] 검색과 피드의 만남: LLM으로 완성하는 초개인화 서비스 ③ 사용자 관심 주제 추출 |
| d2/8366976 | 3,331 | 추출/문제 해결형 | case_0184, case_0185, case_0186, case_0187 | 0/20 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/3814947 | 16,662 | 추출/실험·활용기 | case_0189, case_0190, case_0191 | 0/28 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | - | 0/0 | Thread-safety in C++ |
| d2/4706492 | 1,246 | 제외/회고·문화·행사 | - | 0/0 | Windowing 기법을 적용한 대용량 고성능 표 컴포넌트 개발기 |
| d2/1450243 | 15,218 | 추출/문제 해결형 | case_0183 | 0/12 | 윈도잉(windowing) 기법을 적용한 고성능 표 컴포넌트 개발기 |
| d2/6388660 | 21,269 | 추출/문제 해결형 | case_0195, case_0196, case_0197 | 0/32 | 6개월 만에 연간 수십조를 처리하는 DB CDC 복제 도구 무중단/무장애 교체하기 |
| d2/8992409 | 1,342 | 제외/실험·활용기 | - | 0/0 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| d2/9290684 | 978 | 제외/회고·문화·행사 | - | 0/0 | Iceberg Low-Latency Queries with Materialized Views  (feat. 실시간 거래 리포트) |
| d2/4241703 | 5,509 | 추출/문제 해결형 | case_0176 | 0/9 | 네이버 통합검색 AIB 도입과 웹 성능 변화 분석 |
| d2/6512234 | 22,022 | 추출/문제 해결형 | case_0192, case_0193, case_0194 | 0/27 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/1155434 | 9,048 | 추출/문제 해결형 | case_0177 | 0/12 | C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가 |
| d2/9290861 | 796 | 제외/개념·튜토리얼 | - | 0/0 | Inside VictoriaMetrics |
| d2/4394359 | 837 | 제외/회고·문화·행사 | - | 0/0 | SNOW의 Automatic Sharding 도입기 |
| d2/2541696 | 7,090 | 추출/실험·활용기 | case_0175 | 0/11 | [AI 해커톤 후기] 코드와 문서만 읽은 LLM은 어떻게 사람과 같은 팀을 1위로 골랐을까 |
| d2/5788040 | 11,490 | 추출/문제 해결형 | case_0180, case_0181, case_0182 | 0/24 | VictoriaMetrics 운영기 2편 — 장비 증설 없이 리소스 위기를 해결한 3단계 최적화 전략 |
| d2/4821538 | 11,038 | 추출/실험·활용기 | case_0174 | 0/15 | [AI 해커톤 후기] AI 해커톤 1위 팀이 AI에게 맡기지 않은 것 |
| kakao/601 | 3,137 | 제외/회고·문화·행사 | - | 0/0 | 제3회 Kakao Tech Meet 후기 - 불확정성에서 감동까지 |
| kakao/605 | 22,040 | 추출/문제 해결형 | case_0146 | 0/15 | CommonJS에서 ESM으로 전환하기 |
| kakao/617 | 1,640 | 제외/회고·문화·행사 | - | 0/0 | Chrome Devtools를 활용하여 나만의 웹뷰 디버깅 환경 만들기 / 제5회 Kakao Tech Meet |
| kakao/624 | 787 | 제외/회고·문화·행사 | - | 0/0 | 카카오의 스팸 메일 대응 전략: 문자열 변형 CASE STUDY / 제6회 Kakao Tech Meet |
| kakao/633 | 6,684 | 제외/기술 선택·도입형 | - | 0/0 | LLM, 더 저렴하게, 더 빠르게, 더 똑똑하게 |
| kakao/665 | 10,722 | 추출/문제 해결형 | case_0143 | 0/14 | 추가배포 없이 API의 case 통일시키기 |
| kakao/690 | 14,392 | 추출/실험·활용기 | case_0134 | 0/11 | LLM as a Judge를 활용한 CodeBuddy 성능 평가 |
| kakao/692 | 4,073 | 제외/회고·문화·행사 | - | 0/0 | AI Agent와 개발자 - 카카오테크가 만난 Thomas Dohmke |
| kakao/716 | 21,657 | 추출/문제 해결형 | case_0149, case_0150, case_0151 | 0/20 | 국내 최초 MoE 모델 ‘Kanana-MoE’ 개발기 |
| kakao/718 | 12,162 | 추출/문제 해결형 | case_0135, case_0136, case_0137 | 0/23 | CDC 파이프라인 정합성 검사 Spark 잡 개발 - Part 2. Spark 최적화편 |
| kakao/756 | 2,566 | 제외/회고·문화·행사 | - | 0/0 | 에이전틱 코딩 가이드북, 그리고 AI 협업 치트 시트와 표준 룰셋 공유 시스템 |
| kakao/761 | 3,645 | 제외/회고·문화·행사 | - | 0/0 | 실패를 장려하는 실험적 문화 |
| kakao/762 | 13,811 | 제외/회고·문화·행사 | - | 0/0 | 생산성 혁신의 실험: AI 마일리지 프로그램 |
| kakao/770 | 16,500 | 추출/기술 선택·도입형 | case_0138 | 0/14 | 5년 된 프로젝트의 빌드 도구를 교체하며 얻은 것들 |
| kakao/776 | 13,270 | 추출/기술 선택·도입형 | case_0133 | 0/12 | PostgreSQL to ES: (1) Kafka Connect CDC 파이프라인 구성 |
| kakao/777 | 12,030 | 추출/문제 해결형 | case_0139, case_0140, case_0141, case_0142 | 1/30 | PostgreSQL to ES: (2) Kafka Connect 트러블슈팅 |
| kakao/784 | 8,710 | 제외/실험·활용기 | - | 0/0 | 단 1시간 만에 99개의 MVP가? AI와 함께한 1K: 바이브코딩전 생생 후기 |
| kakao/785 | 4,597 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며 |
| kakao/799 | 23,731 | 추출/실험·활용기 | case_0128, case_0129, case_0130 | 0/21 | AI TOP 100이 우리에게 남긴 것들 |
| kakao/804 | 3,760 | 추출/실험·활용기 | case_0119 | 0/8 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/809 | 1,548 | 제외/회고·문화·행사 | - | 0/0 | 카카오 AI 앰배서더 ‘KANANA 429 앰배서더’를 신규 모집합니다. |
| kakao/822 | 20,047 | 추출/실험·활용기 | case_0131, case_0132 | 0/23 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakao/823 | 5,040 | 추출/실험·활용기 | case_0120, case_0121, case_0122 | 0/19 | Vibe Coding하는 비개발자는 개발자인가(3) |
| kakao/828 | 48,105 | 추출/실험·활용기 | case_0126, case_0127 | 0/20 | Beyond AI That Speaks Well: Making Kanana-o Speak the Way Users Want |
| kakao/835 | 12,198 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 둘째 날, 기술 세션 소개 |
| kakaopay/spring-batch-performance | 12,920 | 추출/문제 해결형 | case_0178, case_0179 | 0/18 | Spring Batch 애플리케이션 성능 향상을 위한 주요 팁 |
| kakaopay/paytalks-with-krew-fe | 14,160 | 제외/회고·문화·행사 | - | 0/0 | FE 리더가 되어버린 나, 이대로 괜찮은가?: 시니어 개발자인 내가 주니어 매니저가 되어 버린 건에 대하여 |
| kakaopay/implementing-tdd-in-practical-applications | 16,086 | 추출/실험·활용기 | case_0171 | 0/12 | 실전에서 TDD하기 |
| kakaopay/kakaopaysec-mongodb-cdc | 17,302 | 추출/문제 해결형 | case_0172, case_0173 | 0/24 | Oracle에서 MongoDB로의 CDC Pipeline 구축 |
| kakaopay/slack-bot-improving-operational-efficiency-2 | 5,044 | 추출/실험·활용기 | case_0168 | 0/10 | 카카오페이 배포 효율화 1년 회고: 자동화 도입과 팀 생산성 향상 |
| kakaopay/tech-strategy-tpm | 9,673 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이 TPM은 어떤 일을 하나요? |
| kakaopay/given-test-code | 11,384 | 추출/실험·활용기 | case_0169 | 0/8 | 실무에서 적용하는 테스트 코드 작성 방법과 노하우 Part 3: Given 지옥에서 벗어나기 - 객체 기반 데이터 셋업의 한계 |
| kakaopay/jack-k8s-internals-part-1 | 9,222 | 제외/개념·튜토리얼 | - | 0/0 | 쓰기만 했던 개발자가 궁금해서 찾아본 쿠버네티스 내부 1편 |
| kakaopay/cilium-egress-gateway | 13,218 | 추출/기술 선택·도입형 | case_0170 | 0/16 | 카카오페이증권의 Egress Gateway |
| kakaopay/katfun-joy-kotlin | 14,709 | 추출/실험·활용기 | case_0166 | 0/8 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kakaopay/devsecops_sonarqube | 10,850 | 추출/실험·활용기 | case_0165 | 0/9 | DevSecOps를 위한 한걸음: Sonarqube를 활용한 지속적인 코드 품질 및 보안 관리 |
| kakaopay/url-is-strange | 15,372 | 추출/문제 해결형 | case_0167 | 0/9 | URL이 이상해요! Java와 Spring 중 범인은 누구? |
| kakaopay/way-to-functional-programming | 28,956 | 추출/실험·활용기 | case_0158 | 0/11 | 코틀린 함수형 프로그래밍의 길을 찾아서 |
| kakaopay/ifkakao2024-devrel | 10,598 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스 준비 맛보기 |
| kakaopay/ifkakao2024-dr-pym-project | 12,897 | 추출/기술 선택·도입형 | case_0162, case_0163, case_0164 | 0/25 | [if(kakaoAI)2024] 카카오페이증권의 Kubernetes 지능형 리소스 최적화 (feat. Dr.Pym Project 공유) |
| kakaopay/perftest_zone | 4,708 | 추출/기술 선택·도입형 | case_0156 | 0/11 | 카카오페이 성능 테스트 존을 소개합니다. |
| kakaopay/home-hexagonal-architecture | 11,913 | 추출/기술 선택·도입형 | case_0155 | 0/9 | Hexagonal Architecture, 진짜 하실 건가요? |
| kakaopay/kakaopaysec-wecan | 8,650 | 추출/기술 선택·도입형 | case_0159, case_0160, case_0161 | 0/24 | We Can Do Better: 개발자 플랫폼 효율화 이야기 |
| kakaopay/kakaopayins-opensearch-analyzer | 10,157 | 추출/실험·활용기 | case_0157 | 0/9 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/backend-domain-driven-design | 17,394 | 추출/기술 선택·도입형 | case_0154 | 0/10 | 카카오페이 여신코어 DDD(Domain Driven Design, 도메인 주도 설계)로 구축하기 |
| kakaopay/nextjs-troubleshooting-cors-version-skew | 13,603 | 추출/문제 해결형 | case_0147, case_0148 | 0/16 | Next.js 트러블슈팅: CORS와 Version Skew 에러 원인부터 해결까지 |
| kakaopay/kakaopayins-envelope-encryption | 18,389 | 추출/문제 해결형 | case_0152, case_0153 | 0/16 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/pallas-v2-log-platform | 25,659 | 추출/문제 해결형 | case_0145 | 0/15 | 일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트 |
| kakaopay/kakaopayins-fe-common-component | 7,059 | 추출/실험·활용기 | case_0144 | 0/9 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kakaopay/ai-agent-1 | 9,989 | 제외/개념·튜토리얼 | - | 0/0 | AI Agent, 넌 누구냐 1 - Tool, MCP, Skill, Harness는 무엇인가 |
| kurly/2023-review-opensearch | 8,418 | 추출/기술 선택·도입형 | case_0266, case_0267, case_0268 | 0/26 | 후기 서비스 AWS Opensearch 도입기 |
| kurly/prod-design-quick-menu | 2,512 | 추출/실험·활용기 | case_0257 | 0/8 | 퀵메뉴로 비즈니스 널리 알리기 (feat. 전지적 디자이너 시점) |
| kurly/cart-recommend-model-development | 9,206 | 추출/문제 해결형 | case_0258 | 0/12 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 1부 |
| kurly/commit-mvcc-set-autocommit | 16,463 | 추출/문제 해결형 | case_0255, case_0256 | 0/15 | 데이터가 있었는데요, 아니 없어요 |
| kurly/fix-hibernate-localtime-bug | 7,136 | 추출/문제 해결형 | case_0254 | 0/7 | 하이버네이트의 시간은 거꾸로 간다 |
| kurly/74-excel-upload-zip-bomb | 5,783 | 추출/문제 해결형 | case_0252 | 0/6 | 엑셀 업로드 중 발생한 Zip Bomb 에러 파헤치기! 🥊 |
| kurly/2024-spring-kafka-consumer-offset-seeking | 15,390 | 추출/문제 해결형 | case_0253 | 1/13 | 분산 시스템 환경에서 Kafka Consumer 오프셋 이동하기 |
| kurly/75-java-module-with-gson-serialization | 9,116 | 추출/문제 해결형 | case_0250 | 0/9 | Spring Boot 버전업 중 알게된 Java 버전별 캡슐화 정책 강화 |
| kurly/deliveryproductteam-culture-1 | 4,454 | 추출/문제 해결형 | case_0249 | 0/9 | 딜리버리 프로덕트 개발팀의 개발문화 - 로그 & 알람편 |
| kurly/connection-leak | 6,791 | 추출/문제 해결형 | case_0251 | 0/10 | 99%가 모른다는 DB Connection 누수 문제 |
| kurly/refine-address-internalization-1 | 5,382 | 추출/문제 해결형 | case_0242 | 0/7 | 주소정제 서비스 내재화 - 1화 ( 줄줄 새는 돈 ) |
| kurly/refine-address-internalization-2 | 4,312 | 추출/문제 해결형 | case_0245 | 0/11 | 주소정제 서비스 내재화 - 2화 ( 그럴싸한 계획 ) |
| kurly/refine-address-internalization-4 | 13,407 | 추출/문제 해결형 | case_0247, case_0248 | 0/18 | 주소정제 서비스 내재화 - 4화 ( 슬픈예감 ) |
| kurly/refine-address-internalization-5 | 9,433 | 추출/문제 해결형 | case_0246 | 0/13 | 주소정제 서비스 내재화 - 5화 ( 어질어질한 변화구들 ) |
| kurly/kafka-connect-pipeline | 9,612 | 추출/문제 해결형 | case_0244 | 0/11 | Kafka Connect로 DB 데이터 쉽게 연동하기 |
| kurly/2025-delivery-debug-study | 10,654 | 제외/회고·문화·행사 | - | 0/0 | 딜리버리 프로덕트 개발팀의 개발 문화 - 주니어 디버깅 스터디 |
| kurly/access-block-1 | 5,663 | 추출/문제 해결형 | case_0239 | 0/9 | nginx 설정 없이 우아하게 서비스 점검하기 (上) |
| kurly/access-block-2 | 8,383 | 추출/문제 해결형 | case_0243 | 0/15 | nginx 설정 없이 우아하게 서비스 점검하기 (下) |
| kurly/fintech-bff-introduction | 10,052 | 추출/실험·활용기 | case_0240, case_0241 | 0/15 | 핀테크그룹의 GraphQL 기반 BFF와 프론트엔드 활용기 |
| kurly/2025-delivery-photo-object-detection | 3,969 | 추출/실험·활용기 | case_0238 | 0/11 | 배송 완료 사진 속 객체 탐지를 통한 수기 검수 비용 줄이기 |
| kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0 | 13,290 | 추출/기술 선택·도입형 | case_0237 | 0/11 | 빌드가 터졌다: 5년 된 CMS 프로젝트의 Webpack4 → Vite 전환 |
| kurly/tech-spec-adoption-with-ai-automation | 8,164 | 추출/실험·활용기 | case_0228 | 0/10 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| kurly/nx-bun-migration | 5,492 | 추출/문제 해결형 | case_0232, case_0233 | 0/17 | Nx에서 Bun 더 잘 사용하기: Nx 18 -> 21 마이그레이션 |
| kurly/ai-orchestration-2 | 17,572 | 추출/실험·활용기 | case_0229, case_0230, case_0231 | 0/25 | AI 에이전트 15개를 동시에 굴리는 법 — AI 병렬 오케스트레이션 실전 운용기 |
| kurly/claude-code-redesign-my-day | 7,389 | 추출/실험·활용기 | case_0234, case_0235, case_0236 | 0/31 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| ly/managing-multi-cdn-logs-traffics-with-vector | 16,695 | 추출/문제 해결형 | case_0223 | 0/10 | Vector를 활용해 멀티 CDN 로그 및 트래픽 관리하기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 18,813 | 추출/실험·활용기 | case_0220, case_0221 | 0/15 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/check-mp4-file-has-audio-using-filereader-in-front-end | 8,381 | 추출/문제 해결형 | case_0227 | 1/11 | 프런트엔드 영역에서 FileReader를 이용해 MP4 파일 내 오디오 존재 여부 확인하기 |
| ly/about-atlassian-jira-ranking-algorithm-lexorank | 9,203 | 추출/문제 해결형 | case_0224, case_0225, case_0226 | 0/24 | Jira의 이슈 정렬 방식이 Integer 방식이 아니라고?! |
| ly/migrate-mysql-with-read-only-mode | 6,059 | 추출/문제 해결형 | case_0222 | 1/13 | 읽기 전용 설정으로 MySQL 이전하기 |
| ly/improving-kubernetes-relay-api-server-performance-with-informer | 12,361 | 추출/문제 해결형 | case_0219 | 0/9 | Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기 |
| ly/improve-development-experience-with-flutter-web | 10,853 | 추출/실험·활용기 | case_0210 | 0/14 | Flutter Web을 활용해 제품 개발 환경 개선하기 |
| ly/introducing-fido2-client-sdk-open-source | 9,957 | 추출/기술 선택·도입형 | case_0215 | 0/9 | FIDO2 클라이언트 SDK 오픈소스 소개 |
| ly/a-flexible-design-system-using-3-tier-tokens | 8,708 | 추출/기술 선택·도입형 | case_0209 | 0/12 | 3단계로 완성하는 유연한 디자인 시스템 |
| ly/4-patterns-of-global-collaboration | 8,902 | 추출/기술 선택·도입형 | case_0211 | 1/12 | 한국어 몰라요 - 글로벌 협업의 4가지 패턴 |
| ly/how-to-evaluate-ai-generated-images-1 | 16,708 | 제외/개념·튜토리얼 | - | 0/0 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/techniques-for-improving-code-quality-16 | 4,455 | 제외/개념·튜토리얼 | - | 0/0 | 코드 품질 개선 기법 16편: 불이 'null'인 굴뚝에 연기가 'null'이 아닐 수 없다 |
| ly/applying-ddd-to-merchant-system-development | 5,212 | 추출/기술 선택·도입형 | case_0216, case_0217, case_0218 | 0/18 | DDD를 Merchant 시스템 구축에 활용한 사례를 소개합니다 |
| ly/hack-day-2025-recap | 7,268 | 제외/회고·문화·행사 | - | 0/0 | 자네, 해커가 되지 않겠나? Hack Day 2025에 다녀왔습니다! |
| ly/extracting-trending-keywords-from-openchat-messages | 14,017 | 추출/문제 해결형 | case_0212, case_0213, case_0214 | 1/23 | 오픈챗 메시지들로부터 트렌딩 키워드 추출하기 |
| ly/pd1-ai-hackathon-recap | 4,153 | 제외/회고·문화·행사 | - | 0/0 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/risks-and-mitigations-in-ai-products-development | 11,404 | 제외/실험·활용기 | - | 0/0 | AI 제품 개발 중 마주칠 수 있는 보안 위협 사례와 대책 방안 |
| ly/connecting-thousands-of-services-with-central-dogma-control-plane | 8,894 | 추출/문제 해결형 | case_0203, case_0204 | 0/16 | Central Dogma 컨트롤 플레인으로 LY Corporation의 수천 개 서비스를 연결하기 |
| ly/solving-slow-queries-optimizing-bitwise-operation-queries-with-functional-indexes | 7,615 | 추출/문제 해결형 | case_0201 | 1/14 | 슬로우 쿼리 해결기: 함수형 인덱스로 비트 연산 쿼리 최적화하기 |
| ly/on-device-image-model-trainer-for-messenger-1 | 18,040 | 추출/문제 해결형 | case_0205 | 0/15 | 메신저용 온디바이스 이미지 모델 학습기 1편: 지식 증류로 확장한 다국어 이미지 검색 |
| ly/journey-to-perfect-ai-guardrails-neurips-2025-recap | 22,682 | 제외/회고·문화·행사 | - | 0/0 | 완벽한 AI 가드레일을 향한 여정: NeurIPS 2025 최신 안전성 기술 분석 |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 6,232 | 추출/실험·활용기 | case_0200 | 1/12 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 및 서비스 상태 확인 도구 LINE Status 개발기 |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 19,601 | 추출/기술 선택·도입형 | case_0206, case_0207, case_0208 | 1/34 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/techverse2026-62 | 6,551 | 추출/문제 해결형 | case_0199 | 0/11 | 임베딩 안정화로 검색 리랭킹의 콜드 스타트 문제를 해결하다: LINE Part Time Jobs 적용 사례 |
| ly/japanese-search-kuromoji-to-sudachi | 15,395 | 추출/기술 선택·도입형 | case_0198 | 0/14 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 |
| oliveyoung/2023-09-18_address-modal | 11,867 | 추출/기술 선택·도입형 | case_0279 | 0/9 | 새 배송지 추가 form 개발하기 |
| oliveyoung/2023-09-18_oliveyoung-coupon-rabbit | 2,012 | 추출/기술 선택·도입형 | case_0059 | 1/8 | 쿠폰 발급 RabbitMQ도입기 |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자가 좋아하는 과자는? |
| oliveyoung/2023-10-11_developer-hobby | 1,871 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자의 슬기로운 취미생활 |
| oliveyoung/2023-10-11_kotlin-detekt-reviewdog | 6,002 | 추출/기술 선택·도입형 | case_0275 | 0/8 | detekt와 reviewdog으로 코드 품질 향상 |
| oliveyoung/2023-10-17_oliveyoung-mall-home-new-architecture | 5,815 | 추출/문제 해결형 | case_0280, case_0281, case_0282 | 0/21 | 올리브영 온라인몰의 전시, 그리고 백엔드 여정 |
| oliveyoung/2023-12-15_seller-service-1 | 5,156 | 추출/문제 해결형 | case_0054 | 0/9 | 외부셀러 - 외부 스파크성 트래픽으로부터 내부 시스템을 보호하는 방법 1탄 |
| oliveyoung/2023-12-19_self-checkout | 2,877 | 추출/기술 선택·도입형 | case_0276 | 0/10 | 올리브영 셀프계산대 도입기 |
| oliveyoung/2024-06-05_google-cloud-next-24-review | 3,796 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next '24 방문기 |
| oliveyoung/2024-06-12_goods-detail-description-improvement-par2 | 4,317 | 추출/문제 해결형 | case_0277 | 1/11 | 상품 설명 영역 개선기 Part.2 |
| oliveyoung/2024-08-11_type-and-type-system-with-typescript | 11,673 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 타입과 타입 시스템 |
| oliveyoung/2024-09-11_introduce-oy-ai-bedrock | 5,664 | 추출/실험·활용기 | case_0062 | 1/14 | AWS Bedrock과 Claude 3.5 Sonnet을 활용한 자동 상품 이미지 검수 시스템 구축기 |
| oliveyoung/2024-09-30_oy-feconf-2024 | 8,894 | 제외/회고·문화·행사 | - | 0/0 | 올리브영에서는 프론트엔드 개발자들이 이런 고민을 하는군요? |
| oliveyoung/2024-10-16_oliveyoung-scm-oms-kafka | 11,362 | 추출/문제 해결형 | case_0055, case_0056, case_0057, case_0058 | 0/28 | Kafka 메시지 중복 및 유실 케이스별 해결 방법 |
| oliveyoung/2024-10-17_oy-delivery-mq | 4,642 | 추출/기술 선택·도입형 | case_0278 | 0/11 | 올리브영 물류시스템에서는 데이터를 어떻게 주고 받을까? |
| oliveyoung/2024-11-07_cdc-failover | 14,225 | 추출/문제 해결형 | case_0060, case_0061 | 0/14 | Debezium MSK Connect로 Failover 구현하여 서비스 안정성 높이기 |
| oliveyoung/2024-11-15_inventory-changed-stocks-function-with-redis-stream | 6,589 | 추출/문제 해결형 | case_0274 | 0/7 | 재고의 변동을 시계열 데이터로?! |
| oliveyoung/2024-12-10_present-promotion-multi-layer-cache | 8,351 | 추출/문제 해결형 | case_0053 | 0/10 | 고성능 캐시 아키텍처 설계 - 로컬 캐시와 Redis로 대규모 증정 행사 관리 최적화 |
| oliveyoung/2024-12-11_oliveyoung-coupon-mess-issue | 3,832 | 추출/문제 해결형 | case_0048 | 0/9 | 올리브영 초대량 쿠폰 발급 시스템 개선기 |
| oliveyoung/2024-12-16_Design-System-Token-Automation | 17,955 | 추출/실험·활용기 | case_0269 | 0/9 | 디자인 시스템 중 디자인 토큰을 여러 도구를 이용하여 자동화 하는 방법 |
| oliveyoung/2024-12-17_catalog-mongo-transaction-2 | 11,450 | 추출/문제 해결형 | case_0272, case_0273 | 0/19 | Spring Boot MongoDB 트랜잭션 도입 실전 가이드 |
| oliveyoung/2025-02-14_oy-global-mall-address | 4,978 | 추출/기술 선택·도입형 | case_0265 | 0/9 | 올리브영 글로벌몰 주소 자동완성 및 검증 솔루션 도입기 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 7,158 | 추출/문제 해결형 | case_0271 | 0/14 | Web Worker로 이미지 처리 최적화하기 |
| oliveyoung/2025-06-10_chaos | 7,289 | 추출/문제 해결형 | case_0270 | 0/10 | 버그가 아니라 장애를 잡아라!! QA와 카오스 엔지니어링의 만남 |
| oliveyoung/2025-07-22_what-is-MFE-part1 | 10,493 | 제외/개념·튜토리얼 | - | 0/0 | 대규모 프론트엔드 아키텍처의 새로운 패러다임 - Part 1. 마이크로프론트엔드 너 뭐야? |
| oliveyoung/2025-07-23_redis-tips-for-developer | 6,442 | 추출/실험·활용기 | case_0052 | 0/12 | 개발자가 알면 좋은 Redis 꿀팁 모음 |
| oliveyoung/2025-08-20_amazonq-vscode | 7,731 | 추출/실험·활용기 | case_0045 | 0/10 | Visual Studio Code를 Cursor처럼? Amazon Q로 AI 코딩 환경 업그레이드하기 |
| oliveyoung/2025-08-29_pos-pick-insights | 4,035 | 제외/회고·문화·행사 | - | 0/0 | PM’s Pick : 우리가 스크랩한 인사이트 |
| oliveyoung/2025-10-17_review-of-orderpay-squad | 5,747 | 제외/회고·문화·행사 | - | 0/0 | KPT 회고, 이렇게 했더니 스쿼드 문화가 바뀌었습니다: 올리브영 주문결제 스쿼드의 애자일 성장기 |
| oliveyoung/2025-10-28_coupon-mq-issue | 9,578 | 추출/문제 해결형 | case_0047 | 0/14 | RabbitMQ Classic Queue 메모리 장애와 Quorum Queue 전환기 |
| oliveyoung/2025-11-06_what-is-MFE-part2 | 15,441 | 추출/실험·활용기 | case_0262 | 0/10 | 대규모 프론트엔드 아키텍처의 새로운 패러다임 - Part 2. 모듈 페더레이션 PoC |
| oliveyoung/2025-11-11_sdui_with_caffein | 7,851 | 추출/문제 해결형 | case_0044 | 0/10 | SDUI의 성능 병목을 넘어: 올리브영 로컬 캐시 기반 백엔드 최적화 성공기 |
| oliveyoung/2025-12-08_creating-video-with-ai | 11,759 | 추출/실험·활용기 | case_0261 | 0/14 | QA 엔지니어가 AI로 만든 교육 영상, 25분짜리 인시던트 가이드 탄생기 |
| oliveyoung/2025-12-15_fcfs-coupon | 8,292 | 추출/문제 해결형 | case_0046 | 0/11 | 올영세일 선착순 쿠폰, 미발급 0%를 향한 여정 |
| oliveyoung/2025-12-15_kafka-streams-for-out-of-stock | 8,553 | 추출/문제 해결형 | case_0043 | 0/9 | Kafka Streams 기반 EDA 구축 사례: 올리브영 품절 시스템 현대화 프로젝트 |
| oliveyoung/2025-12-24_amazon-connect | 9,265 | 추출/문제 해결형 | case_0036, case_0037, case_0038 | 0/19 | 운영 비용을 95% 절감한 서버리스 온콜 시스템 구축기 |
| oliveyoung/2025-12-30_alimtalk_improve_event_driven_architecture | 16,155 | 추출/문제 해결형 | case_0033, case_0034 | 0/16 | SQS 기반 알림톡 처리에서 발생한 DB 커넥션 데드락 분석기 |
| oliveyoung/2026-01-21_oy_sllm | 14,577 | 추출/실험·활용기 | case_0039 | 0/17 | T4 GPU 1장으로 일궈낸 올리브영의 Gemma 3 기반 sLLM 구축기 |
| oliveyoung/2025-10-28_oliveyoung-zero-downtime-oauth2-migration | 14,957 | 추출/문제 해결형 | case_0049, case_0050, case_0051 | 0/23 | 올리브영 대규모 트래픽 레거시 시스템의 무중단 OAuth2 전환기 |
| oliveyoung/2026-03-06_delivery-optimization | 9,147 | 추출/기술 선택·도입형 | case_0259, case_0260 | 0/19 | 배송최적화 시스템 구축기 Part 01. 올리브영이 멀티 센터 체제로 배송 시간을 14시간 단축한 과정 |
| oliveyoung/2026-03-30_chaos-host-level | 11,756 | 추출/실험·활용기 | case_0040, case_0041, case_0042 | 0/24 | QA가 서버를 죽여본 이유 – Host Level 카오스 엔지니어링 테스트 |
| oliveyoung/2026-04-22_display-benefits-migration | 9,558 | 추출/문제 해결형 | case_0035 | 0/12 | 45분 배치에서 준실시간으로! 다수 도메인 데이터를 Kafka로 통합한 전환기 |
| oliveyoung/2026-08-31_a-lunch-that-builds-collaboration-culture | 4,359 | 제외/회고·문화·행사 | - | 0/0 | 한 끼의 점심이 협업 문화를 만든다면? |
| oliveyoung/2026-09-14_global-store-new-way-of-working | 9,809 | 추출/문제 해결형 | case_0263 | 1/10 | 리드타임 3일, 글로벌 매장 개발자가 출장지에서 일하는 법 |
| oliveyoung/2026-09-23_overengineering-message-system | 10,795 | 추출/기술 선택·도입형 | case_0264 | 0/14 | 때로는 오버엔지니어링이 필요합니다 |
| toss/frontend-diving-club-agora | 2,605 | 제외/회고·문화·행사 | - | 0/0 | 프론트엔드 다이빙클럽에서 만나는 아고라: 다른 회사에선 테스트 코드 어떻게 짜요? |
| toss/slash23-data | 7,570 | 추출/문제 해결형 | case_0094, case_0095, case_0096, case_0097 | 0/25 | 대규모 로그 처리도 OK! Elasticsearch 클러스터 개선기 |
| toss/engineering-note-5 | 14,437 | 추출/문제 해결형 | case_0089 | 0/9 | 프론트엔드 로깅 신경 안 쓰기 |
| toss/restructuring | 8,187 | 추출/문제 해결형 | case_0088 | 0/14 | 달리는 기차의 바퀴 교체하기 2. Restructuring |
| toss/docs-engineering | 5,875 | 추출/기술 선택·도입형 | case_0085 | 0/9 | 더 자유롭고, 빠르고, 정확하게: 토스페이먼츠 API 문서 엔지니어링 |
| toss/27752 | 5,980 | 추출/문제 해결형 | case_0086 | 0/10 | 드래그 앤 드롭은 사실 편한 UX가 아니다? |
| toss/ssr-server | 7,737 | 추출/문제 해결형 | case_0087 | 0/12 | SSR 서버 최적화로 비용 아끼기 |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | - | 0/0 | 오픈소스에 기여하고 토스에 합격한.ssul \| EP.4 모닥불 |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | - | 0/0 | 개발자 리더로서 성장당한 썰 \| EP.7 모닥불 |
| toss/toss-frontend-ai-docs | 2,869 | 추출/실험·활용기 | case_0083, case_0084 | 0/11 | 토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유 |
| toss/toss-people-3 | 7,801 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 문과생에서 토스 개발 리더까지 |
| toss/frontend-esbuild-hmr | 10,415 | 추출/문제 해결형 | case_0081 | 0/9 | ESBuild를 위한 HMR, 직접 만들기 |
| toss/frontend-tree-structure | 7,435 | 추출/문제 해결형 | case_0082 | 0/10 | 자료구조를 활용한 복잡한 프론트엔드 컴포넌트 제작하기 |
| toss/frontend-apply-without-resume | 2,783 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드에 이력서 없이 리포지토리 링크로 지원하세요 (~5/31) |
| toss/credit-loan-partner-mock-server | 10,361 | 추출/문제 해결형 | case_0075 | 0/13 | 신용대출 찾기 서비스 제휴사 mock 서버 개발기 #1 |
| toss/toss-securities-gpu-mig | 13,794 | 추출/기술 선택·도입형 | case_0073 | 0/14 | GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기 |
| toss/undercover-silo-2 | 5,209 | 추출/문제 해결형 | case_0074 | 0/12 | “AI가 문제 냈어요?” 출제자 PO가 직접 답해드립니다 \| 언더커버 사일로 비하인드 1화: 인플로우 사일로 |
| toss/payments-legacy-3 | 19,675 | 추출/기술 선택·도입형 | case_0078, case_0079, case_0080 | 0/25 | 100년 가는 프론트엔드 코드, SDK |
| toss/tds-color-system-update | 13,423 | 추출/문제 해결형 | case_0072 | 0/14 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| toss/payments-legacy-10 | 10,691 | 추출/기술 선택·도입형 | case_0068, case_0069, case_0070, case_0071 | 0/34 | 경계 보안부터 제로트러스트 보안까지, 고도화 여정 |
| toss/harness-for-team-productivity-eng | 15,730 | 추출/실험·활용기 | case_0063 | 0/13 | Stepping into the Software 3.0 Era |
| toss/tam-connect-2025 | 4,446 | 제외/회고·문화·행사 | - | 0/0 | 빠르게 움직이는 조직에서, TAM은 어떻게 문제를 해결할까? |
| toss/spark-connect-on-kubernetes-1 | 14,096 | 추출/문제 해결형 | case_0076, case_0077 | 0/20 | Spark Connect on Kubernetes #1: 견고한 Spark Connect 만들기 |
| toss/ads_dashboard_fe | 12,467 | 추출/기술 선택·도입형 | case_0064 | 0/13 | 전체 데이터를 브라우저에 두는 광고 대시보드 만들기 |
| toss/qa_hotfix | 6,406 | 추출/문제 해결형 | case_0065, case_0066, case_0067 | 0/25 | 1%가 겪은 버그 고쳐야할까요? |
| woowahan/13929 | 6,609 | 제외/회고·문화·행사 | - | 0/0 | 밤샘의 추억, 생성 AI 해커톤 “우아톤 2023” |
| woowahan/12947 | 12,972 | 제외/회고·문화·행사 | - | 0/0 | [모여서 각자 글쓰기] 온라인 출판기념회 |
| woowahan/14301 | 6,451 | 추출/문제 해결형 | case_0118 | 0/10 | 굴러가는 자동차에 안전하게 타이어 교체하기(w. CMS 기능 개발) |
| woowahan/14484 | 5,518 | 추출/문제 해결형 | case_0117 | 0/8 | “일단 백로그에 넣어두고 여유 있을 때 보는 걸로 할까요?” : 백로그를 백로그로 두지 않는 법 |
| woowahan/14671 | 6,108 | 제외/회고·문화·행사 | - | 0/0 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/14874 | 33,747 | 추출/문제 해결형 | case_0123, case_0124, case_0125 | 0/24 | 서버사이드 테스트 파랑새를 찾아서 |
| woowahan/15398 | 10,772 | 추출/실험·활용기 | case_0110 | 0/11 | Java의 미래, Virtual Thread |
| woowahan/15541 | 6,445 | 제외/개념·튜토리얼 | - | 0/0 | 웹 접근성 준수를 통한 모두에게 배달되는 일상의 행복 |
| woowahan/15764 | 9,265 | 추출/문제 해결형 | case_0108 | 0/12 | 고르곤졸라는 되지만 고르곤 졸라는 안 돼! 배달의민족에서 금칙어를 관리하는 방법 |
| woowahan/17081 | 8,547 | 추출/문제 해결형 | case_0109 | 0/12 | 우아한형제들 디자인 시스템에 시각적 회귀 테스트 적용하기 |
| woowahan/17221 | 16,046 | 추출/문제 해결형 | case_0107 | 0/11 | JPA에서 아이디를 자동증가 값으로 사용 시 하이버네이트의 @NaturalId 사용해 보기 |
| woowahan/17386 | 11,245 | 추출/실험·활용기 | case_0114, case_0115, case_0116 | 0/28 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/17911 | 4,799 | 추출/문제 해결형 | case_0106 | 0/12 | B마트 주문 유실을 없애보자: 네트워크 편 |
| woowahan/19317 | 1,157 | 제외/회고·문화·행사 | - | 0/0 | [다시 보기] 8월 우아한테크세미나: 생성AI로 똑똑하게 일하는 법 |
| woowahan/20789 | 333 | 제외/회고·문화·행사 | - | 0/0 | WOOWACON 2024 발표 영상, 지금 바로 만나 보세요! |
| woowahan/20763 | 8,615 | 추출/기술 선택·도입형 | case_0111, case_0112, case_0113 | 1/31 | 이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기 |
| woowahan/21027 | 25,102 | 추출/기술 선택·도입형 | case_0103 | 0/10 | 실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법 |
| woowahan/24434 | 15,179 | 추출/문제 해결형 | case_0104, case_0105 | 0/19 | “함께 구매하면 좋은 상품” 추천 모델 고도화 |
| woowahan/24999 | 12,341 | 추출/문제 해결형 | case_0100, case_0101, case_0102 | 0/22 | WOOWACON 2025 미니게임 WOOWA POP! |
| woowahan/25888 | 6,211 | 추출/실험·활용기 | case_0099 | 0/11 | 별점 뒤에 숨겨진 리뷰의 온도, LLM으로 한 끗 차이가 다른 추천 만들기 |
| woowahan/26388 | 11,938 | 추출/문제 해결형 | case_0092 | 0/11 | 사람도 AI도 놓친 번역 누락, ESLint 플러그인을 만들어 해결하기 |
| woowahan/26459 | 11,918 | 추출/실험·활용기 | case_0091 | 0/10 | AI가 내 프롬프트를 흘려듣는 이유: 원리부터 다시 본 컨텍스트 엔지니어링 |
| woowahan/26624 | 10,287 | 추출/문제 해결형 | case_0098 | 0/15 | 기술이 없던 곳에 기술 더하기: 사내 해커톤 플랫폼 만들기 |
| woowahan/26835 | 6,778 | 추출/문제 해결형 | case_0093 | 0/12 | 문서로만 지키던 아키텍처 규칙, 테스트 코드로 강제하기 |
| woowahan/27330 | 7,910 | 추출/문제 해결형 | case_0090 | 0/15 | 집 나간 네트워크는 돌아왔는데 React.lazy는 왜 안 돌아올까 |
