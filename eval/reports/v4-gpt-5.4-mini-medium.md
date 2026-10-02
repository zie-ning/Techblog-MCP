# 추출 점검 리포트: v4-gpt-5.4-mini-medium

- 모델: gpt-5.4-mini (medium)
- 프롬프트 버전: 5bafd9ddcc5d
- 글 80편: 추출 52, 제외 28
- 항목 88개
- 토큰: 호출 158회, 입력 1,315,305 (캐시 532,736), 출력 563,837 (reasoning 449,687)
- 비용: $3.164 (편당 $0.0396), 전체 1,262편 추정 $49.9 / Batch $25.0

## 블로그별 추출 여부

| 블로그 | 추출 | 제외 | 항목 수 |
| --- | --- | --- | --- |
| d2 | 5 | 5 | 15 |
| kakao | 4 | 6 | 5 |
| kakaopay | 7 | 3 | 12 |
| kurly | 9 | 1 | 13 |
| ly | 8 | 2 | 14 |
| oliveyoung | 6 | 4 | 7 |
| toss | 6 | 4 | 10 |
| woowahan | 7 | 3 | 12 |

## 글 유형 × 추출 여부

| 글 유형 | 추출 | 제외 |
| --- | --- | --- |
| 개념·튜토리얼 | 0 | 7 |
| 기술 선택·도입형 | 25 | 0 |
| 문제 해결형 | 11 | 0 |
| 실험·활용기 | 16 | 0 |
| 회고·문화·행사 | 0 | 21 |

## 짧은 글 (평문 1,500자 미만) 8편

| 글 | 길이 | 결과 | 항목 | 분류 이유 |
| --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | 0 | 네이버 사내 행사 NAVER ENGINEERING DAY 세션을 소개하는 글로, 본문은 발표 주제 목록과 행사 소개가 중심이며 구체적인 문제 해결 과정이나 설계 근거를 상세히 다루지 않습니다. |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | 0 | C++의 thread safety 개념과 data race, happens-before, mutex/atomic 등 기본 이론과 표준 라이브러리 동작을 설명하는 발표 자료 소개글로, 특정 실무 문제 해결이나 적용 결과보다는 개념 정리에 초점이 있다. 또한 사내 행사 세션 공개 형식이라 실무 판단에 참고할 만한 구체적 도입·해결 사례가 부족하다. |
| d2/8992409 | 1,342 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션 공개 및 발표 소개가 중심이며, 본문에는 데이터 계보 파이프라인의 구체적인 설계 결정·문제 해결 과정·적용 결과가 서술되어 있지 않습니다. |
| d2/9290861 | 796 | 제외/회고·문화·행사 | 0 | NAVER Engineering Day 세션 발표를 소개하는 행사성 글로, VictoriaMetrics의 내부 구조를 설명하는 내용이 중심이지만 특정 팀의 실무 문제 해결이나 도입 판단, 적용 결과가 제시되지 않습니다. 따라서 기술 사례 데이터베이스에 추출할 만한 실무적 설계·구현 판단 근거가 부족합니다. |
| kakao/624 | 787 | 제외/회고·문화·행사 | 0 | 테크밋 발표 영상과 인터뷰를 소개하는 행사 성격의 글이며, 본문은 참여 소감과 행사 후기 중심입니다. 문자열 변형을 이용한 스팸 대응의 구체적인 문제 해결 과정이나 설계 근거는 거의 없어 실무 참고용 기술 사례로 보기 어렵습니다. |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | 0 | 사내 간식 선호도 설문과 결과 공유가 중심인 문화/회고 성격의 글입니다. 기술 문제 해결, 기술 도입 근거, 실무 적용 방법 같은 설계 참고 내용이 없습니다. |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | 0 | 오픈소스 기여 경험과 기술적 성장 이야기를 담은 인터뷰/토크 형식의 콘텐츠로, 특정 기술 문제 해결이나 도입 판단보다는 개인 경험과 행사성 대담이 중심입니다. |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | 0 | 프론트엔드 리드들의 리더십 성장과 조직 문화에 대한 인터뷰/회고성 콘텐츠로, 특정 기술 문제 해결이나 도입·적용의 실무 판단 근거가 중심이 아니다. 개발 도구나 기술 적용 사례보다 리더 역할과 성장 경험을 다루므로 제외한다. |

## 글당 항목 수 (제외 글 빼고)

| 항목 수 | 글 수 |
| --- | --- |
| 1 | 30 |
| 2 | 12 |
| 3 | 6 |
| 4 | 4 |

## 문제 유형 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 개발 생산성 | 26 | 30% |
| 업무·운영 자동화 | 16 | 18% |
| 장애 대응·복구 | 14 | 16% |
| 모니터링·관측성 | 12 | 14% |
| 데이터 정합성·트랜잭션 | 10 | 11% |
| 배포·CI/CD | 9 | 10% |
| DB 성능·쿼리 최적화 | 9 | 10% |
| 메시징·비동기 처리 | 8 | 9% |
| 비용 절감 | 7 | 8% |
| 인프라·컨테이너 | 7 | 8% |
| 데이터 파이프라인 | 7 | 8% |
| 인증·보안 | 6 | 7% |
| 트래픽 급증 대응 | 4 | 5% |
| API 설계·외부 연동 | 4 | 5% |
| DB 마이그레이션·샤딩 | 4 | 5% |
| 클라이언트 성능(웹·앱) | 3 | 3% |
| 캐싱 | 3 | 3% |
| MSA | 1 | 1% |
| 테스트 자동화 | 1 | 1% |

- 한 번도 안 쓰인 분류 (1개): 동시성·락

## 도메인 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 사내 플랫폼·개발 도구 | 37 | 42% |
| 커머스·주문·재고 | 24 | 27% |
| 배달·물류 | 12 | 14% |
| 검색·추천 | 9 | 10% |
| LLM·AI | 7 | 8% |
| 범용 | 5 | 6% |
| 결제·금융 | 4 | 5% |
| 콘텐츠·미디어 | 3 | 3% |
| 채팅·메시징 서비스 | 2 | 2% |
| 광고·마케팅 | 1 | 1% |

- 쏠림(30% 초과): 사내 플랫폼·개발 도구
- 한 번도 안 쓰인 분류 (0개): 없음

## 발췌 검증

- 채택한 시도 기준 발췌 706개 중 탈락 20개 (원문 존재율 97%)
- 재시도한 글 26편

- `d2/6512234`: 운영과 동일한 부하를 주기 위해 HTTP 트래픽 복사나 Kafka 토픽 복제 같은 방식을 사용하면 비즈니스 로직 호출 시 타 부서 시스템에 중복 호출 부하를 야기하거나, 예상치 못한 부작용으로 운영에 영향을 줄 위험이 매우 높았습니다.
- `d2/6512234`: 운영과 동일한 부하를 주기 위해 HTTP 트래픽 복사나 Kafka 토픽 복제 같은 방식을 사용하면 비즈니스 로직 호출 시 타 부서 시스템에 중복 호출 부하를 야기하거나, 예상치 못한 부작용으로 운영에 영향을 줄 위험이 매우 높았습니다.
- `d2/6512234`: INSERT나 UPDATE를 배치로 실행할 때, 여러 개의 쿼리를 하나의 쿼리(INSERT INTO ... VALUES (...), (...), (...))로 묶어서 보냅니다. 대량 데이터 삽입 시 성능이 수십 배 차이 날 수 있습니다.
- `kakao/770`: Parcel의 Zero-config는 매력적이었지만, 프로젝트 구성이 다소 복잡하기에 설정 자체를 자동화하는 것은 리스크가 높다고 판단하였습니다.
- `kakaopay/katfun-joy-kotlin`: 코틀린의 확장 함수와 object declaration을 사용해서 싱글톤으로 사용할 수 있습니다.
- `kakaopay/pallas-v2-log-platform`: 83만 건/초 처리 시 | ~5,533 Core 필요 | ~230 Core 필요 |
- `kurly/cart-recommend-model-development`: 실제 장바구니 데이터를 기반으로 실험을 진행하였으며, ‘기존 방식(score 순 정렬)으로 구성한 상위 30개의 추천 결과’와 ‘200개의 상품을 셔플링하여 구성한 상위 30개의 추천 결과’의 카테고리별 상품 수에 대해서 지니 계수와 엔트로피를 계산해 보았습니다.
Kruskal-Wallis 검정을 통해 통계적으로도 두 결과의 중앙값에 유의한 차이가 있음을 확인하였습니다 (p < .05).
- `kurly/refine-address-internalization-2`: STEP 2. 외부업체 주소정제 축적 데이터에 없을때는 행안부 좌표조회 api 활용도 시도해보자.
- `ly/extracting-trending-keywords-from-openchat-messages`: 처음에는 관련 키워드를 모두 블랙리스트로 구성해서 이와 일치하거나 부분 문자열로 포함하는 단어는 트렌딩 키워드로 추출되지 않도록 만들어 봤습니다. 그랬더니 미처 예상치 못했던 단어들이, 예를 들어 오랜만에 경기가 열리는 지방 도시 이름이라던가 말이나 기수 또는 참가 팀 이름 등 미리 지정하는 게 사실상 불가능한 단어들이 걸러지지 못하고 추천 키워드로 추출됐습니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 이때 연관성 지표로는 Normalized pointwise mutual information(이하 NPMI)를 채택했습니다. 시드 단어들 중 하나라도 연관성 점수가 미리 정해둔 임계치를 넘는 것이 있으면 해당 후보 단어를 트렌딩 키워드에서 제외합니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 날짜를 달리해 여러 차례 적용해 보니 페널티 가중치가 2 이상이면 가중치를 더 늘리더라도 대체로 순위가 유지되는 것을 관찰했습니다. 검토 결과 다양성이 충분히 확보되는 편이 바람직하다고 의견이 모여 페널티 가중치가 2 이상인 구간에서 α값을 결정했습니다.
- `ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status`: 온콜에서 수신하는 알람을 그대로 반영할 것인지 혹은 오류 예산 기반으로 표현할 것인지 등을 검토했는데요.
- `ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status`: 온콜에서 수신하는 알람을 그대로 반영할 것인지 혹은 오류 예산 기반으로 표현할 것인지 등을 검토했는데요.
- `ly/from-hive-to-iceberg-12x-faster-data-updates`: 널리 쓰이는 Spark Streaming(Structured Streaming)은 마이크로 배치(micro-batch) 방식으로 작동합니다. 이 한계 때문에 앞서 정의한 세 가지 요구 사항 중 특히 데이터 최신성 판별과 정확히 한 번 처리 보장을 동시에 만족하기 어려웠습니다.
- `ly/from-hive-to-iceberg-12x-faster-data-updates`: 기존에 1시간(60분) 주기였던 데이터 반영 작업을 5분으로 단축하면서 얻어낸 결과입니다.
- `ly/from-hive-to-iceberg-12x-faster-data-updates`: 파티셔닝은 Iceberg에서 제공하는 bucket 함수를 활용해 상품 ID값을 기준으로 진행했습니다. 하지만 ID를 기준으로 파티셔닝을 적용하자 데이터를 조회하거나 병합할 때 읽어야 하는 데이터 파일과 삭제 파일의 범위가 해당 파티션 내로 대폭 축소되었습니다.
- `ly/from-hive-to-iceberg-12x-faster-data-updates`: 이를 통해 온힙에 치우쳐 있던 메모리를 재분배해 spark.executor.memoryOverhead값을 크게 늘려 오프힙 메모리를 넉넉하게 확보함으로써 OOM 문제를 완화할 수 있었습니다. 메모리 문제를 해결한 뒤 Heartbeat Timeout이라는 복병을 만났습니다.
- `ly/japanese-search-kuromoji-to-sudachi`: 카탈로그 매칭 작업에서 관리자는 상품명 전체를 기억하지 못하는 경우가 많습니다. 'スマートフォン(스마트폰)'이 들어간 카탈로그를 찾고 싶을 때 'スマ' 두 글자만 입력해도 후보가 나타나야 작업이 빠릅니다.
- `oliveyoung/2024-12-17_catalog-mongo-transaction-2`: @Async로 비동기로 처리까지 추가하면, 이벤트 발행 작업이 메인 로직을 방해하지 않고 진행됩니다.
- `woowahan/24434`: 마트 |
6% ↑ |
7% ↑ |
4% ↑ |

## 기술 사전에 없는 이름 141종

- Locust (3)
- Transformer (3)
- WECAN (3)
- Jira (3)
- HDFS (3)
- Figma (2)
- GitHub (2)
- Android (2)
- iOS (2)
- Web Worker (2)
- Node2Vec (2)
- SASRec (2)
- Webpack (2)
- Vite (2)
- Babel (2)
- S2 Geometry (2)
- Catalog (2)
- Dokka (2)
- Hive (2)
- JuiceFS (2)
- Confluence (2)
- Sudachi (2)
- Apache Iceberg (2)
- Hubot (2)
- Vector (2)
- 행정안전부 도로명주소 조회 API (2)
- ESBuild (1)
- SWC (1)
- React Refresh (1)
- Token Studio (1)
- Style Dictionary (1)
- Web (1)
- MIG (1)
- nvidia-device-plugin (1)
- dcgm-exporter (1)
- nvidia-smi (1)
- H100 (1)
- H200 (1)
- WebAssembly (1)
- Rust (1)
- pgvector (1)
- MongoDB Atlas (1)
- Milvus (1)
- Redis Stack (1)
- LTE 라우터 (1)
- IPSEC (1)
- Kanana-2 (1)
- MLA (1)
- MoE (1)
- Spring Cloud Bus (1)
- AWS Athena (1)
- JMH (1)
- Netty (1)
- JFR (1)
- async-profiler (1)
- jstack (1)
- Codex (1)
- IntelliJ (1)
- Claude API (1)
- Storybook (1)
- Vitest (1)
- C++ (1)
- libevent (1)
- AWS ALB (1)
- fastutil (1)
- AWS KMS (1)
- CloudTrail (1)
- Testcraft (1)
- InfluxDB (1)
- 너의 이름은 (1)
- 너의 권한은 (1)
- 로켓단 (1)
- Wallga (1)
- 닥터 핌 (1)
- Developer Desk (1)
- AssertJ (1)
- Spinnaker (1)
- Filebeat (1)
- Protocol Buffers (1)
- Grafana Loki (1)
- Amazon Athena (1)
- HyperDX (1)
- Signoz (1)
- Release Please Action (1)
- JFrog Artifactory (1)
- Maven Central Repository (1)
- GitHub Pages (1)
- Ruler (1)
- datasource-proxy (1)
- Java Reflection API (1)
- nubes Object Storage (1)
- nubes-s3-proxy (1)
- fio (1)
- JuiceFS CSI Driver (1)
- Kuromoji (1)
- IPADIC (1)
- ZSTD (1)
- Kubernetes Python client (1)
- Kubernetes Go client (1)
- kubectl (1)
- Informer (1)
- WebAuthn (1)
- Slack Workflow (1)
- Ansible (1)
- MobX (1)
- Material-UI (1)
- Tailwind CSS (1)
- Rollup (1)
- esbuild (1)
- qs (1)
- @vitejs/plugin-react (1)
- vite-plugin-babel (1)
- rollup-plugin-visualizer (1)
- ForkTsCheckerWebpackPlugin (1)
- dayjs (1)
- react-csv (1)
- tui-color-picker (1)
- Google Sheets (1)
- BigQuery (1)
- Swagger (1)
- Postman (1)
- Vue Router (1)
- Akamai (1)
- node_exporter (1)
- kube-state-metrics (1)
- 행정안전부 좌표정보 API (1)
- MariaDB Connector/J (1)
- MariaDB (1)
- MySQL Connector/J (1)
- AWS EC2 (1)
- Eclipse MAT (1)
- OffscreenCanvas (1)
- BERT4Rec (1)
- MLflow (1)
- Gradio (1)
- GrowthBook (1)
- mitmproxy (1)
- Tokens Studio for Figma (1)
- token-transformer (1)
- Panda CSS (1)
- Spring Data MongoDB (1)

## 버린 대안 63개 (항목 88개 중)

- `case_0002` 개별 색상만 수정: 부분의 변경사항이 있을 때 전체 팔레트를 건드려야 해서 해결책이 되지 않았어요.
- `case_0006` Virtual Scrolling: 100건 단위 페이지네이션이라 DOM 부하가 병목이 아니었고, UX도 그런 모양이 아니었다.
- `case_0006` IndexedDB 캐싱: 무효화 규칙이 명확하지 않았고, 세션 안에서만 유지해도 문제를 풀 수 있어서 과했다.
- `case_0006` Worker 직접 API 호출: 공통 HTTP 클라이언트를 Worker 쪽에 한 벌 더 두거나 별도 경로를 만들어야 해서 비용이 컸다.
- `case_0009` 클라우드 활용: 지속 워크로드와 자체 IDC 환경에서는 비용이 더 발생할 수 있고, 보안·컴플라이언스 제약과 정밀 제어 한계가 있다.
- `case_0009` 혼합 GPU 운영: 운영 정책과 호환성 관리가 복잡해지고, 고용량 GPU 수요가 집중되면 저용량 GPU가 유휴 자원이 될 수 있다.
- `case_0009` MPS: 리소스 간 격리가 어렵고 성능 간섭과 프로세스별 모니터링·제어가 복잡하다.
- `case_0010` ZK-SNARK: 효과적이지 않으며
- `case_0012` ANN + post filter: 배달 가능한 가게를 최종적으로 보장하기 어렵다.
- `case_0012` Pinecone: 사내에 도입되어 있지 않거나 관리 주체가 없는 상황에서 신규 fully-managed service 도입을 바로 검토하기 어려웠다.
- `case_0016` 에그: 에그는 사용이 쉽고 이용요금이 저렴해 보이지만 운영 비용과 사용자 교육 비용이 커서 선택하지 않았다.
- `case_0016` 동일 회선 사업자 이중화: 같은 회선 사업자로 이중화하는 대신 다른 회선 사업자를 추가해 이원화했다.
- `case_0021` 배치: 실시간 데이터를 반영하기 어려웠다.
- `case_0023` 재사용 가능한 script: 묶음으로 동작해야 하는 작업을 명시했고, LLM 덕분에 고정적인 script가 아니더라도 빠르고 쉬운 변경이 가능하기 때문이다.
- `case_0026` Rsbuild: 생태계 규모가 작아 실서비스에 적용하기 어렵다고 보았다.
- `case_0027` Blue/Green 배포: 트래픽을 세밀하게 조절하기 위해서 일반적인 Blue/Green 배포를 사용하지 않았다.
- `case_0028` in-memory data store: 단순 key value 조회 이상의 기능을 지원하는 라이브러리들로서 데이터를 변경할 일도 잦지 않은 입장에서는 과하다고 판단했다.
- `case_0029` Entity LifeCycle: 데이터 조회 시 값이 바뀌어 update 문이 발생했고, PreLoad 주기가 없어 문제를 해결하지 못했다.
- `case_0035` 별도 검증 클래스: 검증 로직을 매번 따로 호출해야 해서 검증 누락 가능성이 있다.
- `case_0038` OpenSearch: 비용이 높고, 대용량 집계 쿼리가 느렸다. **(technologies에도 있음)**
- `case_0038` Grafana Loki: 복잡한 쿼리 불가, 집계 기능이 약했다.
- `case_0039` Fluentd S3 Output: 처리 속도가 느리고 중복 파싱과 메모리 과다 사용 문제가 있었다.
- `case_0039` Amazon Athena: 컬럼 수 제한이 있고 쿼리 속도와 스키마 관리가 불리했다.
- `case_0039` Signoz: 테이블 구조가 고정되고 attributes Map 접근과 커스터마이징이 제한됐다.
- `case_0047` react-window: div를 절대 좌표로 배치했기 때문에 행에 CSS 스타일을 적용하기 어려웠다.
- `case_0047` @tanstack/react-virtual: 네이버의 로그 시스템에서 제공하는 로그 표현 방식이 다양하고 복잡하여 오픈소스로 대응하기 어렵다고 판단했다.
- `case_0048` 분산 트랜잭션: 이중 쓰기를 구현하는 시점에는 Oracle과 MySQL 간 데이터 정합성이 대부분 맞지 않았고, MySQL 쿼리만 실패하는 상황을 용인해야 했기 때문입니다.
- `case_0052` Alluxio: 일부 POSIX API를 지원하지 않는다.
- `case_0052` C3 HDFS: Kubernetes CSI Driver를 지원하지 않아 Kubernetes 영구 볼륨으로 사용할 수 없다.
- `case_0052` nubes Object Storage: POSIX API를 완벽히 지원하지 않고 Kubernetes CSI Driver도 지원하지 않는다.
- `case_0052` Ceph-rbd: ReadWriteMany, ReadOnlyMany를 지원하지 않아 동시에 여러 Pod에서 접근할 수 없다.
- `case_0052` NFS: 확장성, HA 문제가 있다.
- `case_0052` local-path: 동시 접근이 불가능하고, 노드별 저장이라 스케줄링 또는 앱 레벨에서의 구현이 필요하다.
- `case_0057` 사용자 사전 추가: 신조어·복합어·모델명 변형을 따라가기 어려워 근본 해결이 아니었다.
- `case_0059` 네이티브 쿠버네티스: 역할과 서비스 어카운트, 서비스, 디플로이먼트 등 설정 작업을 수동으로 해야 해서 운영이 번거로웠다.
- `case_0060` 온힙 메모리 증설: 메모리 압박이 여전히 심했다.
- `case_0060` 즉시 병합 기준: HDFS의 NameNode와 DataNode에 과도하게 I/O 부하를 일으켰다.
- `case_0061` non-keyed window: 처리량이 늘어날수록 단일 태스크로 작동해 성능을 심각하게 저하시켰다.
- `case_0062` Python 클라이언트: Informer를 지원하지 않아 가까운 시일 안에 원하는 구조를 만들 수 없었다.
- `case_0063` WebAuthn Level 3: 아직 공식적으로 확정되지 않은 초안 상태이고, Passkey 동기화를 제어할 방법이 없어서 채택하지 않았다.
- `case_0066` MCP 직접 조회: 가져온 텍스트가 전부 AI의 처리 비용(토큰)으로 계산되어 2~3일치만 수집해도 비용과 속도가 급격히 악화됐습니다.
- `case_0066` 노션 수작업 정리: 노동력으로는 오래가지 못했습니다.
- `case_0069` 최근 빈도 기반 선정: 최근 등장 빈도가 높은 단어를 그대로 뽑으면 인삿말이나 고마움, 웃음 표현 같은 일상적인 단어가 많이 나와 트렌딩 키워드로 부적합했다.
- `case_0069` 거리 기반 클러스터링: 중복 메시지 몇 건이 제거되지 않거나 잘못 제거돼도 심대한 영향이 크지 않아 더 간단한 방식을 택했다.
- `case_0070` nginx 설정으로 차단: 개발팀에 nginx 설정 변경과 재시작 권한이 없었다.
- `case_0071` 스케줄링 배치: 최소한의 공수로 하나의 인스턴스 안에서 해결하려고 했다.
- `case_0073` nginx 설정으로 차단: 인프라 상황에 적합하지 않았기 때문
- `case_0073` 전용 UI: 기존 시스템 안에 넣기도 애매했기 때문
- `case_0073` 신규 인스턴스: 이 기능 하나만을 위한 인스턴스를 띄우기 애매했기 때문
- `case_0078` retry 로직: 위와 같은 상황에서는 어차피 정상 응답을 받지 못할 확률이 높다
- `case_0079` READ COMMITTED: 격리수준을 낮추면 Phantom Read 이슈가 발생하여 기존 비즈니스 로직에 영향을 줄 수 있어서 선택하지 않았어요.
- `case_0079` 잠금 읽기: SELECT 시 행을 잠그게 되어 락 경합 및 데드락 발생 가능성이 증가할 수 있어서 선택하지 않았어요.
- `case_0080` max-lifetime 증가: DB failover 시에 slave로 빠르게 연결하기 위해 max-lifetime을 작게 설정하고 있어 선택하지 않았다.
- `case_0082` WebP 변환: 복잡한 이미지일수록 압축 효율이 낮았고, 품질을 낮추면 시각적인 퀄리티 저하가 발생했다.
- `case_0082` Shared Worker / Service Worker: 이미지 처리에 불필요한 기능들이 많아 배제했다.
- `case_0083` 주문서 그대로 학습: 좋은 결과로 이어지지 못했고, 추론 시 어떤 상품을 입력하든 E사 우유 상품이 계속해서 추천되었다.
- `case_0083` 수작업 카테고리 관계 설정: 카테고리 간 보완재 관계를 사람이 직접 설정하는 것은 매우 어렵고 객관적으로 평가하기도 어려웠다.
- `case_0084` 수동 응답 수정: 필드 값이 많으면 하나하나 수동으로 수정하며 테스트하는 번거로움이 있었다.
- `case_0084` 실제 데이터 입력: API가 null 값을 넘겨주는 조건이 정의되지 않아 데이터 수정으로 null을 만들기 어려웠다.
- `case_0087` WriteConcern MAJORITY: 모든 요청에 대해 Secondary 과반수 ACK 응답을 기다리면 큰 오버헤드를 발생시킬 수 있습니다.
- `case_0087` ReadPreference PRIMARY: SECONDARY 노드가 유휴 상태로 남아 리소스를 낭비할 수 있습니다.
- `case_0088` SQS 메시지 지연 전달: 지연 시간이 너무 짧다면 타이밍 문제가 여전히 발생할 수 있어 임시방편에 불과합니다.
- `case_0088` Outbox 패턴: 설계 및 구현에 걸리는 시간과 비용이 부담됩니다.

## 글 목록

| 글 | 길이 | 결과 | 항목 | 발췌 탈락 | 제목 |
| --- | --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | - | 0/0 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics |
| d2/4555524 | 18,452 | 추출/기술 선택·도입형 | case_0052, case_0053, case_0054 | 0/23 | AI 플랫폼을 위한 스토리지 JuiceFS 도입기 |
| d2/8366976 | 3,331 | 추출/문제 해결형 | case_0040, case_0041, case_0042, case_0043 | 0/16 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/3814947 | 16,662 | 추출/기술 선택·도입형 | case_0044, case_0045, case_0046 | 0/19 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | - | 0/0 | Thread-safety in C++ |
| d2/1450243 | 15,218 | 추출/문제 해결형 | case_0047 | 0/10 | 윈도잉(windowing) 기법을 적용한 고성능 표 컴포넌트 개발기 |
| d2/8992409 | 1,342 | 제외/회고·문화·행사 | - | 0/0 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| d2/6512234 | 22,022 | 추출/기술 선택·도입형 | case_0048, case_0049, case_0050, case_0051 | 3/34 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/1155434 | 9,048 | 제외/개념·튜토리얼 | - | 0/0 | C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가 |
| d2/9290861 | 796 | 제외/회고·문화·행사 | - | 0/0 | Inside VictoriaMetrics |
| kakao/601 | 3,137 | 제외/회고·문화·행사 | - | 0/0 | 제3회 Kakao Tech Meet 후기 - 불확정성에서 감동까지 |
| kakao/624 | 787 | 제외/회고·문화·행사 | - | 0/0 | 카카오의 스팸 메일 대응 전략: 문자열 변형 CASE STUDY / 제6회 Kakao Tech Meet |
| kakao/761 | 3,645 | 제외/회고·문화·행사 | - | 0/0 | 실패를 장려하는 실험적 문화 |
| kakao/762 | 13,811 | 추출/실험·활용기 | case_0024 | 0/8 | 생산성 혁신의 실험: AI 마일리지 프로그램 |
| kakao/770 | 16,500 | 추출/기술 선택·도입형 | case_0026 | 1/12 | 5년 된 프로젝트의 빌드 도구를 교체하며 얻은 것들 |
| kakao/784 | 8,710 | 제외/회고·문화·행사 | - | 0/0 | 단 1시간 만에 99개의 MVP가? AI와 함께한 1K: 바이브코딩전 생생 후기 |
| kakao/785 | 4,597 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며 |
| kakao/804 | 3,760 | 추출/기술 선택·도입형 | case_0018 | 0/9 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/822 | 20,047 | 추출/실험·활용기 | case_0022, case_0023 | 0/19 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakao/835 | 12,198 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 둘째 날, 기술 세션 소개 |
| kakaopay/slack-bot-improving-operational-efficiency-2 | 5,044 | 추출/문제 해결형 | case_0036 | 0/6 | 카카오페이 배포 효율화 1년 회고: 자동화 도입과 팀 생산성 향상 |
| kakaopay/tech-strategy-tpm | 9,673 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이 TPM은 어떤 일을 하나요? |
| kakaopay/katfun-joy-kotlin | 14,709 | 추출/실험·활용기 | case_0035 | 1/10 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kakaopay/ifkakao2024-devrel | 10,598 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스 준비 맛보기 |
| kakaopay/perftest_zone | 4,708 | 추출/기술 선택·도입형 | case_0030 | 0/10 | 카카오페이 성능 테스트 존을 소개합니다. |
| kakaopay/kakaopaysec-wecan | 8,650 | 추출/기술 선택·도입형 | case_0031, case_0032, case_0033, case_0034 | 0/25 | We Can Do Better: 개발자 플랫폼 효율화 이야기 |
| kakaopay/kakaopayins-opensearch-analyzer | 10,157 | 제외/개념·튜토리얼 | - | 0/0 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/kakaopayins-envelope-encryption | 18,389 | 추출/기술 선택·도입형 | case_0029 | 0/9 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/pallas-v2-log-platform | 25,659 | 추출/기술 선택·도입형 | case_0037, case_0038, case_0039 | 1/38 | 일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트 |
| kakaopay/kakaopayins-fe-common-component | 7,059 | 추출/기술 선택·도입형 | case_0025 | 0/5 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kurly/cart-recommend-model-development | 9,206 | 추출/문제 해결형 | case_0083 | 1/11 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 1부 |
| kurly/commit-mvcc-set-autocommit | 16,463 | 추출/문제 해결형 | case_0079 | 0/8 | 데이터가 있었는데요, 아니 없어요 |
| kurly/deliveryproductteam-culture-1 | 4,454 | 추출/실험·활용기 | case_0076 | 0/8 | 딜리버리 프로덕트 개발팀의 개발문화 - 로그 & 알람편 |
| kurly/connection-leak | 6,791 | 추출/문제 해결형 | case_0080 | 0/10 | 99%가 모른다는 DB Connection 누수 문제 |
| kurly/refine-address-internalization-2 | 4,312 | 추출/문제 해결형 | case_0077, case_0078 | 1/14 | 주소정제 서비스 내재화 - 2화 ( 그럴싸한 계획 ) |
| kurly/access-block-1 | 5,663 | 추출/기술 선택·도입형 | case_0070, case_0071 | 0/12 | nginx 설정 없이 우아하게 서비스 점검하기 (上) |
| kurly/access-block-2 | 8,383 | 추출/기술 선택·도입형 | case_0073 | 0/13 | nginx 설정 없이 우아하게 서비스 점검하기 (下) |
| kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0 | 13,290 | 추출/기술 선택·도입형 | case_0072 | 0/11 | 빌드가 터졌다: 5년 된 CMS 프로젝트의 Webpack4 → Vite 전환 |
| kurly/tech-spec-adoption-with-ai-automation | 8,164 | 제외/회고·문화·행사 | - | 0/0 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| kurly/claude-code-redesign-my-day | 7,389 | 추출/실험·활용기 | case_0066, case_0067, case_0068 | 0/19 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| ly/managing-multi-cdn-logs-traffics-with-vector | 16,695 | 추출/기술 선택·도입형 | case_0074, case_0075 | 0/12 | Vector를 활용해 멀티 CDN 로그 및 트래픽 관리하기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 18,813 | 추출/실험·활용기 | case_0064, case_0065 | 0/7 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/improving-kubernetes-relay-api-server-performance-with-informer | 12,361 | 추출/문제 해결형 | case_0062 | 0/9 | Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기 |
| ly/introducing-fido2-client-sdk-open-source | 9,957 | 추출/기술 선택·도입형 | case_0063 | 0/4 | FIDO2 클라이언트 SDK 오픈소스 소개 |
| ly/how-to-evaluate-ai-generated-images-1 | 16,708 | 제외/개념·튜토리얼 | - | 0/0 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/extracting-trending-keywords-from-openchat-messages | 14,017 | 추출/실험·활용기 | case_0069 | 3/13 | 오픈챗 메시지들로부터 트렌딩 키워드 추출하기 |
| ly/pd1-ai-hackathon-recap | 4,153 | 제외/회고·문화·행사 | - | 0/0 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 6,232 | 추출/실험·활용기 | case_0055, case_0056 | 2/17 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 및 서비스 상태 확인 도구 LINE Status 개발기 |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 19,601 | 추출/기술 선택·도입형 | case_0059, case_0060, case_0061 | 4/29 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/japanese-search-kuromoji-to-sudachi | 15,395 | 추출/기술 선택·도입형 | case_0057, case_0058 | 1/16 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자가 좋아하는 과자는? |
| oliveyoung/2024-06-05_google-cloud-next-24-review | 3,796 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next '24 방문기 |
| oliveyoung/2024-08-11_type-and-type-system-with-typescript | 11,673 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 타입과 타입 시스템 |
| oliveyoung/2024-09-30_oy-feconf-2024 | 8,894 | 제외/회고·문화·행사 | - | 0/0 | 올리브영에서는 프론트엔드 개발자들이 이런 고민을 하는군요? |
| oliveyoung/2024-10-17_oy-delivery-mq | 4,642 | 추출/기술 선택·도입형 | case_0086 | 0/10 | 올리브영 물류시스템에서는 데이터를 어떻게 주고 받을까? |
| oliveyoung/2024-12-16_Design-System-Token-Automation | 17,955 | 추출/실험·활용기 | case_0085 | 0/7 | 디자인 시스템 중 디자인 토큰을 여러 도구를 이용하여 자동화 하는 방법 |
| oliveyoung/2024-12-17_catalog-mongo-transaction-2 | 11,450 | 추출/문제 해결형 | case_0087, case_0088 | 1/10 | Spring Boot MongoDB 트랜잭션 도입 실전 가이드 |
| oliveyoung/2025-02-14_oy-global-mall-address | 4,978 | 추출/기술 선택·도입형 | case_0081 | 0/10 | 올리브영 글로벌몰 주소 자동완성 및 검증 솔루션 도입기 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 7,158 | 추출/문제 해결형 | case_0082 | 0/10 | Web Worker로 이미지 처리 최적화하기 |
| oliveyoung/2025-06-10_chaos | 7,289 | 추출/실험·활용기 | case_0084 | 0/11 | 버그가 아니라 장애를 잡아라!! QA와 카오스 엔지니어링의 만남 |
| toss/27752 | 5,980 | 추출/실험·활용기 | case_0015 | 0/10 | 드래그 앤 드롭은 사실 편한 UX가 아니다? |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | - | 0/0 | 오픈소스에 기여하고 토스에 합격한.ssul \| EP.4 모닥불 |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | - | 0/0 | 개발자 리더로서 성장당한 썰 \| EP.7 모닥불 |
| toss/toss-frontend-ai-docs | 2,869 | 추출/실험·활용기 | case_0007, case_0008 | 0/8 | 토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유 |
| toss/toss-people-3 | 7,801 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 문과생에서 토스 개발 리더까지 |
| toss/frontend-esbuild-hmr | 10,415 | 추출/실험·활용기 | case_0001 | 0/8 | ESBuild를 위한 HMR, 직접 만들기 |
| toss/frontend-apply-without-resume | 2,783 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드에 이력서 없이 리포지토리 링크로 지원하세요 (~5/31) |
| toss/toss-securities-gpu-mig | 13,794 | 추출/기술 선택·도입형 | case_0009 | 0/13 | GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기 |
| toss/tds-color-system-update | 13,423 | 추출/기술 선택·도입형 | case_0002, case_0003, case_0004, case_0005 | 0/25 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| toss/ads_dashboard_fe | 12,467 | 추출/기술 선택·도입형 | case_0006 | 0/12 | 전체 데이터를 브라우저에 두는 광고 대시보드 만들기 |
| woowahan/14484 | 5,518 | 추출/실험·활용기 | case_0017 | 0/6 | “일단 백로그에 넣어두고 여유 있을 때 보는 걸로 할까요?” : 백로그를 백로그로 두지 않는 법 |
| woowahan/14671 | 6,108 | 제외/회고·문화·행사 | - | 0/0 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/15398 | 10,772 | 제외/개념·튜토리얼 | - | 0/0 | Java의 미래, Virtual Thread |
| woowahan/15541 | 6,445 | 제외/개념·튜토리얼 | - | 0/0 | 웹 접근성 준수를 통한 모두에게 배달되는 일상의 행복 |
| woowahan/17386 | 11,245 | 추출/실험·활용기 | case_0019, case_0020, case_0021 | 0/24 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/17911 | 4,799 | 추출/기술 선택·도입형 | case_0016 | 0/12 | B마트 주문 유실을 없애보자: 네트워크 편 |
| woowahan/20763 | 8,615 | 추출/기술 선택·도입형 | case_0027, case_0028 | 0/21 | 이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기 |
| woowahan/21027 | 25,102 | 추출/기술 선택·도입형 | case_0012 | 0/8 | 실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법 |
| woowahan/24434 | 15,179 | 추출/문제 해결형 | case_0013, case_0014 | 1/21 | “함께 구매하면 좋은 상품” 추천 모델 고도화 |
| woowahan/24999 | 12,341 | 추출/실험·활용기 | case_0010, case_0011 | 0/14 | WOOWACON 2025 미니게임 WOOWA POP! |
