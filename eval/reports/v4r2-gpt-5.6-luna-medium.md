# 추출 점검 리포트: v4r2-gpt-5.6-luna-medium

- 모델: gpt-5.6-luna (medium)
- 프롬프트 버전: 5bafd9ddcc5d
- 글 80편: 추출 54, 제외 26
- 항목 83개
- 토큰: 호출 150회, 입력 1,214,002 (캐시 468,473), 출력 167,373 (reasoning 55,844)
- 비용: $0.359 (편당 $0.0045), 전체 1,262편 추정 $5.7 / Batch $2.8

## 블로그별 추출 여부

| 블로그 | 추출 | 제외 | 항목 수 |
| --- | --- | --- | --- |
| d2 | 6 | 4 | 15 |
| kakao | 2 | 8 | 2 |
| kakaopay | 8 | 2 | 12 |
| kurly | 10 | 0 | 14 |
| ly | 8 | 2 | 13 |
| oliveyoung | 6 | 4 | 7 |
| toss | 6 | 4 | 8 |
| woowahan | 8 | 2 | 12 |

## 글 유형 × 추출 여부

| 글 유형 | 추출 | 제외 |
| --- | --- | --- |
| 개념·튜토리얼 | 0 | 5 |
| 기술 선택·도입형 | 15 | 1 |
| 문제 해결형 | 25 | 1 |
| 실험·활용기 | 14 | 1 |
| 회고·문화·행사 | 0 | 18 |

## 짧은 글 (평문 1,500자 미만) 8편

| 글 | 길이 | 결과 | 항목 | 분류 이유 |
| --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/문제 해결형 | 0 | 기존 Symbolicator의 한계와 새로운 Crash 분석 시스템을 다룬 기술 발표이지만, 본문에는 구체적인 해결 과정·비교 수치·설계 근거가 없고 발표 주제 목록과 영상 공개 안내만 제시되어 있다. |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | 0 | C++의 data race, happens-before, thread safety, 동기화 primitive 등 동시성 개념과 사용법을 설명하는 행사 발표 자료 소개 글이며, 특정 팀이 겪은 문제의 해결 과정이나 실제 적용 결과·설계 근거는 제시하지 않는다. |
| d2/8992409 | 1,342 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 자료를 소개하는 글로, DBT·Airflow 기반 설계의 구체적인 해결 과정이나 수치·비교·적용 결과 없이 발표 내용과 목차만 나열하고 있다. |
| d2/9290861 | 796 | 제외/개념·튜토리얼 | 0 | VictoriaMetrics의 내부 구조와 구성 요소를 소개하는 발표 자료 공개 글이지만, 실제 운영 문제에 대한 해결 과정이나 구체적인 설계 결정·비교·적용 결과가 본문에 제시되지 않고 목차와 행사 소개 중심이다. |
| kakao/624 | 787 | 제외/회고·문화·행사 | 0 | 테크밋 발표 영상과 발표자 인터뷰를 소개하는 행사 후기 형식이며, 스팸 메일 대응의 구체적인 설계·해결 과정이나 적용 결과는 본문에 제시되지 않았습니다. |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | 0 | 개발자들의 간식 선호도를 설문하고 결과와 추천 패키지를 소개하는 조직 문화·구성원 대상 콘텐츠로, 기술 문제 해결이나 업무에 적용한 기술적 실무 내용이 없습니다. |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | 0 | 토스 개발자들의 오픈소스 기여 경험과 기술적 성장에 관한 발표·인터뷰 소개 글로, 구체적인 문제 해결 과정이나 적용 결과보다 출연진과 타임스탬프 등 행사성 콘텐츠 안내가 중심이다. |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | 0 | 프론트엔드 리드들의 리더십 성장과 조직 성장에 관한 경험을 다룬 콘텐츠로, 조직·리더십 문화 중심이며 구체적인 기술 문제 해결이나 기술 도입 사례가 없다. |

## 글당 항목 수 (제외 글 빼고)

| 항목 수 | 글 수 |
| --- | --- |
| 1 | 36 |
| 2 | 8 |
| 3 | 9 |
| 4 | 1 |

## 문제 유형 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 개발 생산성 | 29 | 35% |
| 모니터링·관측성 | 14 | 17% |
| 데이터 파이프라인 | 14 | 17% |
| 배포·CI/CD | 11 | 13% |
| 데이터 정합성·트랜잭션 | 11 | 13% |
| 장애 대응·복구 | 10 | 12% |
| DB 성능·쿼리 최적화 | 10 | 12% |
| 업무·운영 자동화 | 9 | 11% |
| 비용 절감 | 8 | 10% |
| 인프라·컨테이너 | 8 | 10% |
| 메시징·비동기 처리 | 7 | 8% |
| 인증·보안 | 6 | 7% |
| 클라이언트 성능(웹·앱) | 5 | 6% |
| 캐싱 | 5 | 6% |
| 트래픽 급증 대응 | 5 | 6% |
| API 설계·외부 연동 | 4 | 5% |
| DB 마이그레이션·샤딩 | 3 | 4% |
| 동시성·락 | 2 | 2% |
| 테스트 자동화 | 2 | 2% |

- 쏠림(30% 초과): 개발 생산성
- 한 번도 안 쓰인 분류 (1개): MSA

## 도메인 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 사내 플랫폼·개발 도구 | 29 | 35% |
| 커머스·주문·재고 | 20 | 24% |
| LLM·AI | 10 | 12% |
| 배달·물류 | 10 | 12% |
| 범용 | 10 | 12% |
| 검색·추천 | 8 | 10% |
| 채팅·메시징 서비스 | 4 | 5% |
| 광고·마케팅 | 3 | 4% |
| 결제·금융 | 3 | 4% |
| 콘텐츠·미디어 | 3 | 4% |

- 쏠림(30% 초과): 사내 플랫폼·개발 도구
- 한 번도 안 쓰인 분류 (0개): 없음

## 발췌 검증

- 채택한 시도 기준 발췌 817개 중 탈락 9개 (원문 존재율 99%)
- 재시도한 글 16편

- `d2/4555524`: JuiceFS는 기존의 저장소와 DB를 활용하는 분산 파일 시스템이다. 데이터 스토리지 역할의 저장소와 메타데이터 엔진 역할의 DB만 준비되어 있다면 별도의 서버 구동 없이 클라이언트만 있으면 된다.
- `ly/improving-kubernetes-relay-api-server-performance-with-informer`: 스레드를 다수 생성해서 작동 방식을 비동기적으로 바꿔 우회하는 방법을 써도 한 리소스를 계산하는 데 10초 정도가 걸렸습니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 하나의 이유는 대부분의 사용자들이 하루에 한번만 오픈챗 메인 화면에 방문한다는 데이터 분석 결과가 있었기 때문입니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 이로부터 자연스럽게 집합의 중첩도를 SetDup:=1−SetDiv으로 정의했습니다.
- `ly/from-hive-to-iceberg-12x-faster-data-updates`: 하지만 컨슈머 랙(consumer lag)이 발생하면 이미 처리된 최신 CDC 데이터 위로 뒤늦게 도착한 과거의 보정 데이터를 덮어써 버리는 문제가 발생할 수 있습니다.
- `ly/from-hive-to-iceberg-12x-faster-data-updates`: 데이터 추출 시점과 CDC 반영 시점이 일치하지 않아 데이터가 누락되는 현상을 완벽하게 방지해야 했습니다.
- `ly/from-hive-to-iceberg-12x-faster-data-updates`: 기존에 1시간(60분) 주기로 돌던 데이터 반영 작업을 5분으로 단축하면서 얻어낸 결과입니다.
- `woowahan/20763`: 단점
– 캐시 레이어 관련 비용 발생
– 작업량이 많음
- `woowahan/24999`: 비디오 영상을 저장하는 대신 플레이어의 키 입력과 마우스 움직임을 기록했고 리플레이할 때는 이 입력을 순서대로 재생하며 게임을 다시 실행했습니다.

## 기술 사전에 없는 이름 131종

- HDFS (5)
- Android (4)
- Jira (4)
- GitHub (3)
- Figma (2)
- iOS (2)
- Web Worker (2)
- Locust (2)
- Node2Vec (2)
- Transformer (2)
- Amazon Athena (2)
- Netty (2)
- Webpack (2)
- Storybook (2)
- Vite (2)
- Rollup (2)
- Babel (2)
- C++ (2)
- Hive (2)
- JFrog Artifactory (2)
- Dokka (2)
- LLM (2)
- JuiceFS (2)
- Apache Iceberg (2)
- Confluence (2)
- ESBuild (1)
- SWC (1)
- react-refresh (1)
- H100 (1)
- H200 (1)
- MIG (1)
- nvidia-device-plugin (1)
- dcgm-exporter (1)
- nvidia-smi (1)
- Token Studio (1)
- Style Dictionary (1)
- Milvus (1)
- Redis Stack (1)
- Atlas MongoDB (1)
- Amazon RDS for PostgreSQL (1)
- pgvector (1)
- SASRec (1)
- Rust (1)
- WebAssembly (1)
- IPSEC (1)
- Spring Cloud (1)
- S2 Geometry (1)
- libevent (1)
- AWS ALB (1)
- fastutil (1)
- JDK (1)
- JMH (1)
- JFR (1)
- async-profiler (1)
- Codex (1)
- Jest (1)
- Vitest (1)
- AES (1)
- RSA (1)
- AWS KMS (1)
- CloudTrail (1)
- Apache Lucene (1)
- Filebeat (1)
- Grafana Loki (1)
- Parquet (1)
- HyperDX (1)
- Wallga (1)
- Mongo (1)
- InfluxDB (1)
- GCP (1)
- AssertJ (1)
- Spinnaker (1)
- react-window (1)
- datasource-proxy (1)
- MySQL Connector/J (1)
- Release Please Action (1)
- Maven Central Repository (1)
- GitHub Pages (1)
- Ruler (1)
- Nexus (1)
- Kuromoji (1)
- Sudachi (1)
- JuiceFS CSI Driver (1)
- WebAuthn (1)
- ZSTD (1)
- Kerberos (1)
- Hadoop (1)
- Hubot (1)
- Ansible (1)
- Harbor (1)
- Git (1)
- hubot-conversation (1)
- Vector (1)
- Akamai (1)
- node_exporter (1)
- kube-state-metrics (1)
- Taskmaster (1)
- etcd (1)
- MobX (1)
- Material-UI (1)
- Tailwind CSS (1)
- esbuild (1)
- qs (1)
- react-csv (1)
- dayjs (1)
- @vitejs/plugin-react (1)
- vite-plugin-babel (1)
- rollup-plugin-visualizer (1)
- Google Sheets (1)
- BigQuery (1)
- Swagger (1)
- Postman (1)
- MariaDB (1)
- AWS EC2 (1)
- mysql-connector-j (1)
- MemoryAnalyzer (1)
- 행정안전부 도로명주소 조회 API (1)
- 외부업체 주소정제 API (1)
- mitmproxy (1)
- MariaDB Connector/J (1)
- OffscreenCanvas (1)
- BERT4Rec (1)
- PyTorch (1)
- MLflow (1)
- Gradio (1)
- GrowthBook (1)
- Yarn (1)
- Panda CSS (1)
- Tokens Studio for Figma (1)
- token-transformer (1)
- Spring Data MongoDB (1)

## 버린 대안 75개 (항목 83개 중)

- `case_0002` 클라우드 활용: 지속적인 워크로드와 자체 클러스터 환경에서는 비용이 더 발생할 수 있고, 보안·컴플라이언스와 GPU 제어에도 제약이 있다.
- `case_0002` 혼합 GPU 운영: GPU 세대별 드라이버·CUDA·프레임워크 호환성과 수요 편중으로 운영 복잡성과 유휴 자원이 증가할 수 있다.
- `case_0002` MPS: 리소스 격리가 어렵고 성능 간섭 및 프로세스별 리소스 모니터링·제어 부담이 커 운영 리스크가 있다.
- `case_0003` 부분 팔레트 수정: Blue 100 하나를 수정해도 관련 색상 전체와 다크모드 팔레트를 함께 다시 검토해야 하므로 전체 문제를 해결하기 어려웠다.
- `case_0004` 컴포넌트 추가 제작: 빠르게 늘어나는 패턴을 컴포넌트만 더 제작해 대응하는 방식은 지속 가능하지 않다고 판단했다.
- `case_0007` Virtual Scrolling: 100건 단위 페이지네이션을 사용하고 DOM 부하가 병목이 아니어서 선택하지 않았다.
- `case_0007` IndexedDB 캐싱: 캐시 무효화 판단이 명확하지 않고 세션 안에서 데이터를 유지하는 것만으로 문제를 해결할 수 있어 선택하지 않았다.
- `case_0009` Atlas MongoDB: 2차 실험에서 RDS가 더 높은 처리량과 더 짧은 응답시간을 보였고 실패 건도 없었다.
- `case_0009` OpenSearch: 부하가 최대치에 달하면서 API 요청 성능이 더 나아지지 않았고, 부하를 견디지 못한 500 오류가 발생했다. **(technologies에도 있음)**
- `case_0014` 동일 회선 사업자 이중화: 지역·전국 단위의 회선 사업자 장애에 취약할 수 있어 다른 회선 사업자를 추가하는 이원화 방식을 선택했다.
- `case_0014` 에그: 내부망 연결과 배터리 충전 등에 대한 사용자 교육 비용과 추가 네트워크 관리 비용이 발생한다.
- `case_0018` Hazelcast: 단순 key-value 조회에 비해 기능이 과하고 진입 장벽과 라이브러리 이해도 부족이 우려되어 선택하지 않았다.
- `case_0018` Chronicle Map: 단순 key-value 조회에 비해 기능이 과하고 진입 장벽과 라이브러리 이해도 부족이 우려되어 선택하지 않았다.
- `case_0018` HPPC: primitive 컬렉션 라이브러리 간 기능 차이가 크지 않아 fastutil을 선택하면서 채택하지 않았다.
- `case_0018` Trove: primitive 컬렉션 라이브러리 간 기능 차이가 크지 않아 fastutil을 선택하면서 채택하지 않았다.
- `case_0018` Koloboke: primitive 컬렉션 라이브러리 간 기능 차이가 크지 않아 fastutil을 선택하면서 채택하지 않았다.
- `case_0018` GC 튜닝: IHOP 등 GC 파라미터 튜닝보다 메모리 저장 구조 개선을 우선하기로 했다.
- `case_0018` Blue/Green 배포: 트래픽을 세밀하게 조절하기 위해 일반적인 Blue/Green 배포 대신 ALB의 두 TargetGroup을 활용했다.
- `case_0022` Parcel: 프로젝트 구성이 복잡한 상황에서 설정 자동화의 리스크가 높고 복잡한 커스터마이징에 제한이 있을 수 있다고 판단했다.
- `case_0024` Entity Life Cycle 콜백: 조회 후 복호화된 값이 1차 캐시에 반영되면서 엔티티가 변경된 것으로 판단되어 조회 때마다 불필요한 update가 발생했다.
- `case_0027` Elasticsearch / OpenSearch: 전문 검색에는 강하지만 비용이 높고 대용량 집계 쿼리가 느리다.
- `case_0027` Grafana Loki: 복잡한 쿼리와 집계 기능이 부족하고, 서비스가 1,000개 이상인 환경에서 카디널리티 부담이 있다.
- `case_0028` Fluentd S3 Output: IAM Role Anywhere를 지원하지 않았고, 처리 속도와 메모리 사용량에 문제가 있었다.
- `case_0028` Amazon Athena: 2,000개 이상의 컬럼을 정의하기 어렵고, 콜드 스타트와 대용량 집계 쿼리 지연 및 스키마 관리 부담이 있었다.
- `case_0028` Signoz: 자체 스키마를 강제하고 LogAttributes Map 검색과 ClickHouse 구조 커스터마이징을 제한했다.
- `case_0035` react-window: div 기반 절대 좌표 레이아웃 때문에 행 스타일, 동적 행 추가·삭제, 자연스러운 컬럼 헤더 이동, colspan 지원에 한계가 있어 자체 컴포넌트를 개발했다.
- `case_0035` @tanstack/react-virtual: 네이버 로그 시스템의 복잡하고 다양한 로그 표현 방식에 대응하기 어렵고, 오픈소스 내부 동작 분석과 커스텀 기능 구현에 부담이 있다고 판단했다.
- `case_0036` reinterpret_cast 타입 퍼닝: 서로 다른 타입의 객체를 다른 타입의 포인터로 접근하면 엄격한 앨리어싱 규칙을 위반한다.
- `case_0036` union 타입 퍼닝: C++에서는 비활성 union 멤버를 읽는 것이 허용되지 않는다.
- `case_0037` std::bit_cast 포인터-정수 변환: std::bit_cast는 포인터와 정수의 크기가 같다는 조건이 표준적으로 보장되지 않는다.
- `case_0038` ChainedTransactionManager: 전환 초기에는 두 DB의 정합성이 맞지 않고 MySQL 쿼리와 환경 설정이 검증되지 않았기 때문에 사용하지 않았다.
- `case_0038` 분산 트랜잭션: MySQL 쿼리 실패를 허용하고 Oracle 트랜잭션에 영향을 주지 않도록 하기 위해 사용하지 않았다.
- `case_0039` HTTP 트래픽 복사: 타 부서 시스템에 중복 호출 부하와 예상치 못한 부작용을 일으킬 위험이 있어 사용하지 않았다.
- `case_0039` Kafka 토픽 복제: 타 부서 시스템에 중복 호출 부하와 예상치 못한 부작용을 일으킬 위험이 있어 사용하지 않았다.
- `case_0047` Elasticsearch ← Elastic Search: 질의 분석 정확도를 높이고 복잡한 질의에 유연하게 대응하기 위해 기존 검색 엔진을 Nexus로 전환했다.
- `case_0048` 사용자 사전 등록: 검색어가 넓어질수록 신조어·복합어·모델명 변형을 계속 수동 등록해야 하므로 근본적이고 지속 가능한 해결책이 아니었다.
- `case_0048` Elasticsearch 8.x 업그레이드: 사내 검색 플랫폼의 지원 범위를 벗어나 고려 대상이 아니었다.
- `case_0049` GlusterFS·CephFS 직접 운영: 오픈소스 스토리지를 직접 운영하는 부담이 커서 우선 검토 대상에서 제외했다.
- `case_0049` Alluxio: 일부 POSIX API를 지원하지 않아 AI 오픈소스와 라이브러리의 호환성이 떨어지고, 원본 저장소 동기화와 별도 클러스터 운영 부담이 있었다.
- `case_0049` AWS EFS·Google Filestore: Object Storage보다 비용이 크고 AiSuite의 사내 구축 환경에서는 외부 클라우드 스토리지를 사용할 수 없었다.
- `case_0051` WebAuthn Level 3: 아직 공식적으로 확정되지 않은 초안 상태이며, Passkey 동기화를 제어할 방법이 없어 현재는 WebAuthn Level 2를 채택했다.
- `case_0052` Spark Streaming: 마이크로 배치 방식으로 이벤트 시간 기준 상태를 세밀하게 제어하기 어려워 데이터 최신성 판별과 정확히 한 번 처리를 동시에 만족하기 어렵다고 판단했다.
- `case_0052` 네이티브 쿠버네티스: Flink 배포와 권한·라우팅·잡 설정을 수동으로 구성해야 해 운영 부담이 컸다.
- `case_0053` Spark 온힙 메모리 증설: 온힙 메모리를 늘렸지만 메모리 압박이 해소되지 않았다.
- `case_0053` 공격적인 파일 병합 기준: 잦은 병합 작업이 HDFS의 NameNode와 DataNode에 과도한 I/O 부하를 일으켰다.
- `case_0054` 애플리케이션 내 직접 인증: 다수의 TaskManager가 각각 인증하면 KDC에 불필요한 부하를 유발할 수 있었다.
- `case_0054` Hadoop 에코시스템 전체 설치: Docker 이미지 크기를 키우고 유지 보수를 어렵게 만들 수 있었다.
- `case_0059` 전날 빈도 비교: 화제성이 정점에 달해 피크가 지속되는 경우 증가량이 미미해 트렌딩 키워드로 탐지되지 않을 수 있다.
- `case_0060` 거리 기반 클러스터링: 중복 메시지가 일부 제거되지 않거나 잘못 제거돼도 영향이 크지 않아 더 간단한 방식을 선택했다.
- `case_0061` 경주 관련 블랙리스트: 블랙리스트로 미리 지정하기 어려운 단어들이 걸러지지 않았다.
- `case_0063` Python 클라이언트 직접 조회: 전체 파드 목록을 직접 조회하는 방식은 질의 비용이 높고 API 응답 속도가 느리며 kube-apiserver와 etcd에 부하를 줬다.
- `case_0064` 메모리 증설: 메모리를 계속 늘리는 것은 임시방편이어서 번들러 교체를 선택했다.
- `case_0065` nginx 라우팅 설정으로 차단: 개발팀에 실행 중인 인스턴스의 nginx 설정 파일 변경 및 nginx 재시작 권한이 없었고, 인프라 팀에 협조를 요청하면 점검이 끝난 뒤일 가능성이 있었다.
- `case_0065` 스케줄링 배치 기반 캐싱: 최소한의 공수로 하나의 인스턴스 안에서 해결하기 위해 선택하지 않았다.
- `case_0066` nginx 설정으로 접근 차단: nginx 설정이 인프라팀 관리 하에 도커의 베이스 이미지와 함께 생성되고, 현재 시스템이 리버스 프록시·게이트웨이 구조가 아니어서 환경에 적합하지 않다.
- `case_0066` BigQuery 직접 조회: 페이지 라우팅과 API 호출마다 BigQuery를 조회하면 네트워크 지연과 프로덕트 성능 저하가 발생할 수 있다.
- `case_0067` AI의 MCP 직접 조회: 가져온 텍스트가 AI의 처리 비용으로 계산되어 2~3일치만 수집해도 비용과 속도가 악화됐다.
- `case_0067` 노션 수작업 정리: 수작업으로 정리하는 방식은 오래가지 못했다.
- `case_0070` max-lifetime 증가: Connection 누수 자체는 방지할 수 있지만 DB failover 시 slave로 빠르게 연결해야 하므로 기존의 짧은 max-lifetime 설정을 유지했다.
- `case_0072` 외부업체 계약종료: 기존 축적 데이터만으로 대한민국의 모든 건물 위경도를 커버할 수 없어 신규 고객 주소 요청에 대응하려면 외부업체 계약을 종료할 수 없었다.
- `case_0072` 행정안전부 API 지속 활용: 행정안전부 도로명주소 조회 API의 호출 안전성을 보장하기 어렵고, 외부업체와 함께 추가 관리 포인트가 되므로 현재 상태를 동결하고 새로운 방법을 찾기로 했다.
- `case_0073` Google Overwrite Contents: 일회성 테스트에는 유용하지만 반복 테스트를 프로세스화하려면 매번 수동 작업이 필요해 리소스가 과도하게 소모된다.
- `case_0073` Charles·Fiddler: 일회성 테스트에는 유용하지만 필드가 많으면 API 응답을 하나씩 수동 수정해야 한다.
- `case_0073` 실제 데이터 입력: API가 null 값을 반환하는 조건이 정의되지 않아 데이터 수정만으로 null을 전달하기 어렵다.
- `case_0074` READ COMMITTED 격리수준: 격리 수준을 낮추면 Phantom Read가 발생해 기존 비즈니스 로직에 영향을 줄 수 있어 채택하지 않았다.
- `case_0074` 잠금 읽기: 행을 잠가 다른 트랜잭션의 수정·삭제를 막으므로 락 경합과 데드락 가능성이 증가해 채택하지 않았다.
- `case_0076` WebP 포맷 변환: 복잡한 이미지에서는 압축 효율이 낮았고, 품질을 낮추면 시각적인 퀄리티 저하가 발생해 실제 적용에 제약이 있었다.
- `case_0076` Canvas 리사이징: 파일 크기와 업로드 속도는 개선됐지만 Canvas 처리 비용과 디코딩·인코딩 과정의 JS 블로킹으로 메인 스레드와 클릭 이벤트가 지연됐다.
- `case_0076` Shared Worker: 이미지 처리에 불필요한 기능들이 많아 배제했다.
- `case_0076` Service Worker: 이미지 처리에 불필요한 기능들이 많아 배제했다.
- `case_0081` WriteConcern MAJORITY: 정확성을 높일 수 있지만 모든 요청에서 Secondary 과반수 ACK를 기다리는 오버헤드가 발생할 수 있어 채택하지 않았다.
- `case_0081` ReadPreference PRIMARY: 모든 읽기 트래픽을 PRIMARY에 집중하면 SECONDARY가 유휴 상태로 남아 리소스를 낭비할 수 있어 전체 읽기 설정으로는 채택하지 않았다.
- `case_0082` SQS 메시지 지연 전달: 지연 시간이 너무 짧으면 타이밍 문제가 다시 발생할 수 있어 임시방편으로 판단했다.
- `case_0082` Outbox 패턴·로그 테일링 패턴: 데이터와 메시지를 분리할 수 있지만 현재 상황에서는 설계 및 구현 시간과 비용이 부담되어 채택하지 않았다.
- `case_0083` EAI I/F: 배치를 사용하는 EAI I/F에서 지연이 발생했고, EAI 어댑터 장애 시 전체 통신이 멈췄다.

## 글 목록

| 글 | 길이 | 결과 | 항목 | 발췌 탈락 | 제목 |
| --- | --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/문제 해결형 | - | 0/0 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics |
| d2/4555524 | 18,452 | 추출/기술 선택·도입형 | case_0049, case_0050 | 1/22 | AI 플랫폼을 위한 스토리지 JuiceFS 도입기 |
| d2/8366976 | 3,331 | 추출/문제 해결형 | case_0044, case_0045, case_0046, case_0047 | 0/23 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/3814947 | 16,662 | 추출/실험·활용기 | case_0041, case_0042, case_0043 | 0/28 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | - | 0/0 | Thread-safety in C++ |
| d2/1450243 | 15,218 | 추출/문제 해결형 | case_0035 | 0/13 | 윈도잉(windowing) 기법을 적용한 고성능 표 컴포넌트 개발기 |
| d2/8992409 | 1,342 | 제외/회고·문화·행사 | - | 0/0 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| d2/6512234 | 22,022 | 추출/문제 해결형 | case_0038, case_0039, case_0040 | 0/26 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/1155434 | 9,048 | 추출/문제 해결형 | case_0036, case_0037 | 0/20 | C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가 |
| d2/9290861 | 796 | 제외/개념·튜토리얼 | - | 0/0 | Inside VictoriaMetrics |
| kakao/601 | 3,137 | 제외/회고·문화·행사 | - | 0/0 | 제3회 Kakao Tech Meet 후기 - 불확정성에서 감동까지 |
| kakao/624 | 787 | 제외/회고·문화·행사 | - | 0/0 | 카카오의 스팸 메일 대응 전략: 문자열 변형 CASE STUDY / 제6회 Kakao Tech Meet |
| kakao/761 | 3,645 | 제외/회고·문화·행사 | - | 0/0 | 실패를 장려하는 실험적 문화 |
| kakao/762 | 13,811 | 제외/회고·문화·행사 | - | 0/0 | 생산성 혁신의 실험: AI 마일리지 프로그램 |
| kakao/770 | 16,500 | 추출/기술 선택·도입형 | case_0022 | 0/11 | 5년 된 프로젝트의 빌드 도구를 교체하며 얻은 것들 |
| kakao/784 | 8,710 | 제외/실험·활용기 | - | 0/0 | 단 1시간 만에 99개의 MVP가? AI와 함께한 1K: 바이브코딩전 생생 후기 |
| kakao/785 | 4,597 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며 |
| kakao/804 | 3,760 | 제외/기술 선택·도입형 | - | 0/0 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/822 | 20,047 | 추출/실험·활용기 | case_0021 | 0/12 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakao/835 | 12,198 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 둘째 날, 기술 세션 소개 |
| kakaopay/slack-bot-improving-operational-efficiency-2 | 5,044 | 추출/문제 해결형 | case_0034 | 0/9 | 카카오페이 배포 효율화 1년 회고: 자동화 도입과 팀 생산성 향상 |
| kakaopay/tech-strategy-tpm | 9,673 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이 TPM은 어떤 일을 하나요? |
| kakaopay/katfun-joy-kotlin | 14,709 | 추출/실험·활용기 | case_0033 | 0/9 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kakaopay/ifkakao2024-devrel | 10,598 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스 준비 맛보기 |
| kakaopay/perftest_zone | 4,708 | 추출/기술 선택·도입형 | case_0032 | 0/10 | 카카오페이 성능 테스트 존을 소개합니다. |
| kakaopay/kakaopaysec-wecan | 8,650 | 추출/기술 선택·도입형 | case_0029, case_0030, case_0031 | 0/20 | We Can Do Better: 개발자 플랫폼 효율화 이야기 |
| kakaopay/kakaopayins-opensearch-analyzer | 10,157 | 추출/실험·활용기 | case_0025 | 0/9 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/kakaopayins-envelope-encryption | 18,389 | 추출/문제 해결형 | case_0024 | 0/11 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/pallas-v2-log-platform | 25,659 | 추출/기술 선택·도입형 | case_0026, case_0027, case_0028 | 0/35 | 일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트 |
| kakaopay/kakaopayins-fe-common-component | 7,059 | 추출/실험·활용기 | case_0023 | 0/12 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kurly/cart-recommend-model-development | 9,206 | 추출/문제 해결형 | case_0077, case_0078 | 0/15 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 1부 |
| kurly/commit-mvcc-set-autocommit | 16,463 | 추출/문제 해결형 | case_0074, case_0075 | 0/15 | 데이터가 있었는데요, 아니 없어요 |
| kurly/deliveryproductteam-culture-1 | 4,454 | 추출/문제 해결형 | case_0071 | 0/10 | 딜리버리 프로덕트 개발팀의 개발문화 - 로그 & 알람편 |
| kurly/connection-leak | 6,791 | 추출/문제 해결형 | case_0070 | 0/10 | 99%가 모른다는 DB Connection 누수 문제 |
| kurly/refine-address-internalization-2 | 4,312 | 추출/문제 해결형 | case_0072 | 0/12 | 주소정제 서비스 내재화 - 2화 ( 그럴싸한 계획 ) |
| kurly/access-block-1 | 5,663 | 추출/문제 해결형 | case_0065 | 0/12 | nginx 설정 없이 우아하게 서비스 점검하기 (上) |
| kurly/access-block-2 | 8,383 | 추출/문제 해결형 | case_0066 | 0/12 | nginx 설정 없이 우아하게 서비스 점검하기 (下) |
| kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0 | 13,290 | 추출/문제 해결형 | case_0064 | 0/11 | 빌드가 터졌다: 5년 된 CMS 프로젝트의 Webpack4 → Vite 전환 |
| kurly/tech-spec-adoption-with-ai-automation | 8,164 | 추출/실험·활용기 | case_0062 | 0/9 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| kurly/claude-code-redesign-my-day | 7,389 | 추출/실험·활용기 | case_0067, case_0068, case_0069 | 0/24 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| ly/managing-multi-cdn-logs-traffics-with-vector | 16,695 | 추출/문제 해결형 | case_0058 | 0/12 | Vector를 활용해 멀티 CDN 로그 및 트래픽 관리하기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 18,813 | 추출/실험·활용기 | case_0057 | 0/11 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/improving-kubernetes-relay-api-server-performance-with-informer | 12,361 | 추출/문제 해결형 | case_0063 | 1/13 | Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기 |
| ly/introducing-fido2-client-sdk-open-source | 9,957 | 추출/기술 선택·도입형 | case_0051 | 0/8 | FIDO2 클라이언트 SDK 오픈소스 소개 |
| ly/how-to-evaluate-ai-generated-images-1 | 16,708 | 제외/개념·튜토리얼 | - | 0/0 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/extracting-trending-keywords-from-openchat-messages | 14,017 | 추출/실험·활용기 | case_0059, case_0060, case_0061 | 2/28 | 오픈챗 메시지들로부터 트렌딩 키워드 추출하기 |
| ly/pd1-ai-hackathon-recap | 4,153 | 제외/회고·문화·행사 | - | 0/0 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 6,232 | 추출/실험·활용기 | case_0055, case_0056 | 0/15 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 및 서비스 상태 확인 도구 LINE Status 개발기 |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 19,601 | 추출/기술 선택·도입형 | case_0052, case_0053, case_0054 | 3/30 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/japanese-search-kuromoji-to-sudachi | 15,395 | 추출/기술 선택·도입형 | case_0048 | 0/13 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자가 좋아하는 과자는? |
| oliveyoung/2024-06-05_google-cloud-next-24-review | 3,796 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next '24 방문기 |
| oliveyoung/2024-08-11_type-and-type-system-with-typescript | 11,673 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 타입과 타입 시스템 |
| oliveyoung/2024-09-30_oy-feconf-2024 | 8,894 | 제외/회고·문화·행사 | - | 0/0 | 올리브영에서는 프론트엔드 개발자들이 이런 고민을 하는군요? |
| oliveyoung/2024-10-17_oy-delivery-mq | 4,642 | 추출/기술 선택·도입형 | case_0083 | 0/13 | 올리브영 물류시스템에서는 데이터를 어떻게 주고 받을까? |
| oliveyoung/2024-12-16_Design-System-Token-Automation | 17,955 | 추출/실험·활용기 | case_0080 | 0/9 | 디자인 시스템 중 디자인 토큰을 여러 도구를 이용하여 자동화 하는 방법 |
| oliveyoung/2024-12-17_catalog-mongo-transaction-2 | 11,450 | 추출/문제 해결형 | case_0081, case_0082 | 0/19 | Spring Boot MongoDB 트랜잭션 도입 실전 가이드 |
| oliveyoung/2025-02-14_oy-global-mall-address | 4,978 | 추출/기술 선택·도입형 | case_0079 | 0/11 | 올리브영 글로벌몰 주소 자동완성 및 검증 솔루션 도입기 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 7,158 | 추출/문제 해결형 | case_0076 | 0/13 | Web Worker로 이미지 처리 최적화하기 |
| oliveyoung/2025-06-10_chaos | 7,289 | 추출/문제 해결형 | case_0073 | 0/13 | 버그가 아니라 장애를 잡아라!! QA와 카오스 엔지니어링의 만남 |
| toss/27752 | 5,980 | 추출/문제 해결형 | case_0008 | 0/8 | 드래그 앤 드롭은 사실 편한 UX가 아니다? |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | - | 0/0 | 오픈소스에 기여하고 토스에 합격한.ssul \| EP.4 모닥불 |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | - | 0/0 | 개발자 리더로서 성장당한 썰 \| EP.7 모닥불 |
| toss/toss-frontend-ai-docs | 2,869 | 추출/실험·활용기 | case_0006 | 0/7 | 토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유 |
| toss/toss-people-3 | 7,801 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 문과생에서 토스 개발 리더까지 |
| toss/frontend-esbuild-hmr | 10,415 | 추출/문제 해결형 | case_0001 | 0/9 | ESBuild를 위한 HMR, 직접 만들기 |
| toss/frontend-apply-without-resume | 2,783 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드에 이력서 없이 리포지토리 링크로 지원하세요 (~5/31) |
| toss/toss-securities-gpu-mig | 13,794 | 추출/기술 선택·도입형 | case_0002 | 0/13 | GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기 |
| toss/tds-color-system-update | 13,423 | 추출/기술 선택·도입형 | case_0003, case_0004, case_0005 | 0/28 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| toss/ads_dashboard_fe | 12,467 | 추출/기술 선택·도입형 | case_0007 | 0/14 | 전체 데이터를 브라우저에 두는 광고 대시보드 만들기 |
| woowahan/14484 | 5,518 | 추출/문제 해결형 | case_0019 | 0/10 | “일단 백로그에 넣어두고 여유 있을 때 보는 걸로 할까요?” : 백로그를 백로그로 두지 않는 법 |
| woowahan/14671 | 6,108 | 제외/회고·문화·행사 | - | 0/0 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/15398 | 10,772 | 추출/실험·활용기 | case_0020 | 0/11 | Java의 미래, Virtual Thread |
| woowahan/15541 | 6,445 | 제외/개념·튜토리얼 | - | 0/0 | 웹 접근성 준수를 통한 모두에게 배달되는 일상의 행복 |
| woowahan/17386 | 11,245 | 추출/실험·활용기 | case_0015, case_0016, case_0017 | 0/27 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/17911 | 4,799 | 추출/문제 해결형 | case_0014 | 0/13 | B마트 주문 유실을 없애보자: 네트워크 편 |
| woowahan/20763 | 8,615 | 추출/기술 선택·도입형 | case_0018 | 1/21 | 이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기 |
| woowahan/21027 | 25,102 | 추출/기술 선택·도입형 | case_0009 | 0/11 | 실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법 |
| woowahan/24434 | 15,179 | 추출/문제 해결형 | case_0010, case_0011 | 0/20 | “함께 구매하면 좋은 상품” 추천 모델 고도화 |
| woowahan/24999 | 12,341 | 추출/문제 해결형 | case_0012, case_0013 | 1/17 | WOOWACON 2025 미니게임 WOOWA POP! |
