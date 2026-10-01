# 추출 점검 리포트: v4-gpt-5.6-terra-medium

- 모델: gpt-5.6-terra (medium)
- 프롬프트 버전: 5bafd9ddcc5d
- 글 80편: 추출 50, 제외 30
- 항목 83개
- 토큰: 호출 139회, 입력 1,078,693 (캐시 365,217), 출력 132,143 (reasoning 26,516)
- 비용: $3.086 (편당 $0.0386), 전체 1,262편 추정 $48.7 / Batch $24.3

## 블로그별 추출 여부

| 블로그 | 추출 | 제외 | 항목 수 |
| --- | --- | --- | --- |
| d2 | 5 | 5 | 10 |
| kakao | 3 | 7 | 3 |
| kakaopay | 6 | 4 | 12 |
| kurly | 10 | 0 | 16 |
| ly | 8 | 2 | 15 |
| oliveyoung | 6 | 4 | 7 |
| toss | 5 | 5 | 8 |
| woowahan | 7 | 3 | 12 |

## 글 유형 × 추출 여부

| 글 유형 | 추출 | 제외 |
| --- | --- | --- |
| 개념·튜토리얼 | 0 | 7 |
| 기술 선택·도입형 | 23 | 0 |
| 문제 해결형 | 18 | 0 |
| 실험·활용기 | 9 | 0 |
| 회고·문화·행사 | 0 | 23 |

## 짧은 글 (평문 1,500자 미만) 8편

| 글 | 길이 | 결과 | 항목 | 분류 이유 |
| --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 영상을 소개하는 글이며, 본문에는 발표 주제 목록만 제시되어 있습니다. 구체적인 설계 결정, 성능 비교 수치, 문제 해결 근거가 서술되지 않아 기술 사례로 추출하기 어렵습니다. |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | 0 | C++ 동시성의 data race, happens-before, thread safety 등 기본 개념과 표준 라이브러리 사용법을 설명하는 발표 자료 소개다. 팀의 구체적인 문제 상황, 설계 결정 근거, 적용 결과가 서술되지 않았다. |
| d2/8992409 | 1,342 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사에서 진행된 발표를 소개하고 발표 목차·대상을 안내하는 글이다. 본문에는 DBT·Airflow 기반 설계의 구체적인 문제 해결 근거, 구현 방식, 비교 결과가 서술되어 있지 않다. |
| d2/9290861 | 796 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사에서 진행된 발표를 소개하는 글로, 본문에는 VictoriaMetrics의 구체적인 설계 결정·운영 문제·해결 근거가 서술되어 있지 않습니다. 발표 목차와 대상만 제시되어 있어 실무 기술 사례로 추출하기 어렵습니다. |
| kakao/624 | 787 | 제외/회고·문화·행사 | 0 | Kakao Tech Meet 발표 영상과 발표자 인터뷰를 소개하는 행사 후기 성격의 글이다. 스팸 메일 문자열 변형 대응의 구체적인 기술 설계, 비교 근거, 구현·적용 결과는 본문에 제시되지 않았다. |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | 0 | 개발 조직 구성원을 대상으로 한 간식 선호도 설문과 그 결과를 소개하는 조직 문화성 글입니다. 기술 문제 해결, 도입 근거, 실제 기술 적용 경험 등 설계·구현에 참고할 실무 내용이 없습니다. |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | 0 | 토스 개발자의 오픈소스 기여 경험과 성장 이야기를 소개하는 모닥불 영상·패널 토크 안내 글이다. 본문에 특정 기술 문제의 해결 과정, 설계 결정 근거, 적용 결과가 구체적으로 제시되지 않았다. |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | 0 | 프론트엔드 리드들의 리더십 성장, 조직 성장, 피드백 경험을 다루는 대화형 콘텐츠다. 구체적인 기술 문제 해결이나 설계·구현 판단 근거는 제시되지 않는다. |

## 글당 항목 수 (제외 글 빼고)

| 항목 수 | 글 수 |
| --- | --- |
| 1 | 32 |
| 2 | 6 |
| 3 | 9 |
| 4 | 3 |

## 문제 유형 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 개발 생산성 | 32 | 39% |
| 모니터링·관측성 | 12 | 14% |
| 데이터 정합성·트랜잭션 | 12 | 14% |
| 데이터 파이프라인 | 12 | 14% |
| 장애 대응·복구 | 11 | 13% |
| DB 성능·쿼리 최적화 | 9 | 11% |
| 인프라·컨테이너 | 8 | 10% |
| 비용 절감 | 7 | 8% |
| 배포·CI/CD | 7 | 8% |
| 인증·보안 | 7 | 8% |
| 메시징·비동기 처리 | 7 | 8% |
| 업무·운영 자동화 | 7 | 8% |
| 클라이언트 성능(웹·앱) | 6 | 7% |
| API 설계·외부 연동 | 6 | 7% |
| 테스트 자동화 | 5 | 6% |
| 캐싱 | 4 | 5% |
| 트래픽 급증 대응 | 4 | 5% |
| DB 마이그레이션·샤딩 | 3 | 4% |
| 동시성·락 | 1 | 1% |

- 쏠림(30% 초과): 개발 생산성
- 한 번도 안 쓰인 분류 (1개): MSA

## 도메인 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 사내 플랫폼·개발 도구 | 31 | 37% |
| 커머스·주문·재고 | 23 | 28% |
| 배달·물류 | 12 | 14% |
| LLM·AI | 10 | 12% |
| 검색·추천 | 5 | 6% |
| 콘텐츠·미디어 | 5 | 6% |
| 결제·금융 | 4 | 5% |
| 범용 | 3 | 4% |
| 채팅·메시징 서비스 | 2 | 2% |
| 광고·마케팅 | 1 | 1% |

- 쏠림(30% 초과): 사내 플랫폼·개발 도구
- 한 번도 안 쓰인 분류 (0개): 없음

## 발췌 검증

- 채택한 시도 기준 발췌 754개 중 탈락 3개 (원문 존재율 100%)
- 재시도한 글 9편

- `ly/introducing-fido2-client-sdk-open-source`: FIDO2 클라이언트 SDK에서는 서비스 개발자가 FIDO2 서버의 API를 호출할 때 네트워킹 방법을 선택하고 커스텀 로직을 적용할 수 있도록 RelyingParty 인터페이스를 제공합니다.
- `ly/introducing-fido2-client-sdk-open-source`: 또한 생체 인증 템플릿 추가에 영향을 받지 않으며, 추가된 템플릿도 기존의 인증 정보와 호환됩니다.
- `ly/from-hive-to-iceberg-12x-faster-data-updates`: 이 글의 제목이기도 한 '12배 속도 향상'은 기존에 1시간(60분) 주기로 돌던 데이터 반영 작업을 5분으로 단축하면서 얻어낸 결과입니다.

## 기술 사전에 없는 이름 110종

- Transformer (3)
- ZSTD (3)
- Jira (3)
- Hubot (3)
- Figma (2)
- GitHub (2)
- Web Worker (2)
- Locust (2)
- Node2Vec (2)
- Webpack (2)
- Storybook (2)
- Vite (2)
- Rollup (2)
- Hive (2)
- Dokka (2)
- HDFS (2)
- Confluence (2)
- Sudachi (2)
- Apache Iceberg (2)
- MIG (1)
- nvidia-device-plugin (1)
- dcgm-exporter (1)
- nvidia-smi (1)
- Token Studio (1)
- Style Dictionary (1)
- Android (1)
- iOS (1)
- Shadow DOM (1)
- Amazon RDS for PostgreSQL (1)
- pgvector (1)
- WebAssembly (1)
- Rust (1)
- Item2Vec (1)
- LTE 라우터 (1)
- IPSEC (1)
- AWS ALB (1)
- fastutil (1)
- Spring Cloud (1)
- Amazon Athena (1)
- Kanana-2 (1)
- MLA (1)
- MoE (1)
- Codex (1)
- Netty (1)
- JFR (1)
- async-profiler (1)
- Vitest (1)
- InfluxDB (1)
- GCP (1)
- AWS KMS (1)
- CloudTrail (1)
- Protocol Buffers (1)
- HyperDX (1)
- Parquet (1)
- Wallga (1)
- Spring JPA (1)
- datasource-proxy (1)
- Release Please Action (1)
- JFrog Artifactory (1)
- Maven Central Repository (1)
- GitHub Pages (1)
- Ruler (1)
- Milvus (1)
- JuiceFS (1)
- MinIO (1)
- Kuromoji (1)
- Lucene (1)
- Flink Kubernetes Operator (1)
- Ansible (1)
- Face ID (1)
- Touch ID (1)
- Secure Enclave (1)
- TrustZone (1)
- StrongBox (1)
- Vector (1)
- Akamai (1)
- node_exporter (1)
- kube-state-metrics (1)
- Taskmaster (1)
- WebView (1)
- 행안부 도로명 주소조회 API (1)
- Google Sheets (1)
- BigQuery (1)
- Vue Router (1)
- Swagger (1)
- MySQL Connector/J (1)
- AWS EC2 (1)
- MemoryAnalyzer (1)
- esbuild (1)
- Babel (1)
- MobX (1)
- Material-UI (1)
- Tailwind CSS (1)
- qs (1)
- react-csv (1)
- dayjs (1)
- BERT4Rec (1)
- MLflow (1)
- PyTorch (1)
- Gradio (1)
- MariaDB Connector/J (1)
- mitmproxy (1)
- OffscreenCanvas (1)
- Yarn (1)
- Jotai (1)
- Panda CSS (1)
- AWS ECR (1)
- AWS ECS (1)
- Tokens Studio for Figma (1)
- token-transformer (1)

## 버린 대안 65개 (항목 83개 중)

- `case_0001` 클라우드 활용: 지속적인 워크로드와 자체 클러스터 환경에서는 비용이 더 발생할 수 있고, 보안·컴플라이언스 및 정밀 제어·가용성 제약이 있다.
- `case_0001` 혼합 GPU 운영: 서로 다른 GPU 세대의 드라이버, CUDA, 프레임워크 호환성과 스케줄링 정책 관리가 복잡하고, 장기적으로 저용량 GPU가 유휴 자원이 될 수 있다.
- `case_0001` MPS: 리소스 격리가 어렵고 성능 간섭 및 프로세스별 사용량 모니터링·제어의 복잡성이 있어 운영 리스크가 컸다.
- `case_0008` Virtual Scrolling: 100건 단위 페이지네이션에서는 한 번에 100행만 그리며, 수십 개 컬럼이 있어도 DOM 부하가 병목이 아니었다.
- `case_0008` IndexedDB 캐싱: 캐시를 버릴 시점을 명확히 판단할 수 없었다.
- `case_0008` Worker 직접 API 호출: 공통 HTTP 클라이언트를 Worker에 중복으로 두거나 별도 호출 경로를 만들어 같은 규칙을 두 곳에서 관리해야 했다.
- `case_0009` Atlas MongoDB(Atlas Search): 2차 부하 테스트에서 RDS가 더 높은 초당 요청량, 실패 없음, 더 짧은 퍼센타일별 응답시간을 보여 최종 선정되지 않았다.
- `case_0009` OpenSearch: 2차 부하 테스트에서 RDS가 더 높은 초당 요청량, 실패 없음, 더 짧은 퍼센타일별 응답시간을 보여 최종 선정되지 않았다.
- `case_0010` ZK-SNARK 적용: 우아팝에 적용하는 것은 효과적이지 않다고 판단했다.
- `case_0014` 에그를 백업 회선으로 사용하는 방식: 내부망 연결, 배터리 충전 등의 사용자 교육이 필요하고 추가 회선에 따른 네트워크 관리 비용이 증가한다.
- `case_0015` 캐시 레이어를 이용한 구조 개선: 캐시 레이어 비용과 작업량이 발생하며, 전환 영향을 최소화하기 위해 기존 메모리 적재 구조를 유지하기로 했다.
- `case_0015` Blue/Green 배포: 트래픽을 세밀하게 조절하기 어려워 사용하지 않았다.
- `case_0016` in-memory data store: 데이터 변경이 잦지 않은 상황에서 단순 key value 조회 이상의 기능은 과했고, 진입 장벽과 라이브러리 이해도 문제가 우려됐다.
- `case_0016` HPPC: 기능상 fastutil과 큰 차이가 없었고, fastutil의 인지도와 최근 활동성을 고려해 선택하지 않았다.
- `case_0016` trove: 기능상 fastutil과 큰 차이가 없었고, fastutil의 인지도와 최근 활동성을 고려해 선택하지 않았다.
- `case_0016` koloboke: 기능상 fastutil과 큰 차이가 없었고, fastutil의 인지도와 최근 활동성을 고려해 선택하지 않았다.
- `case_0023` Parcel의 Zero-config 적용: 프로젝트 구성이 복잡해 설정을 자동화하는 위험이 높다고 판단했다.
- `case_0023` Rsbuild: 생태계와 문서·지원 규모가 작아 실서비스 적용이 어렵다고 판단했다.
- `case_0027` Entity LifeCycle에서 Entity 값 수정: 1차 캐시가 복호화된 값을 변경으로 판단해 update 문이 발생했고, PreLoad 주기가 없어 문제를 해결할 수 없었다.
- `case_0029` Elasticsearch / OpenSearch: 비용이 높고 대용량 집계 쿼리가 느렸다.
- `case_0029` Grafana Loki: 복잡한 쿼리가 불가능하고 집계 기능이 약했으며, 서비스가 1,000개 이상인 환경의 카디널리티 부담이 있었다.
- `case_0029` Signoz: 자체 테이블 구조를 강제하고 LogAttributes Map의 개별 필드 검색 및 ClickHouse 테이블 구조 활용이 어려웠다.
- `case_0030` Fluentd S3 Output: IAM Role Anywhere를 지원하지 않고, 처리 속도가 느리며 이미 파싱한 로그를 다시 파싱하고 메모리를 과다 사용했다.
- `case_0030` Amazon Athena: 2,000개 이상 컬럼의 테이블 정의가 어렵고, 콜드 스타트 및 대용량 집계 쿼리 성능 문제가 있었다.
- `case_0036` react-window: div 기반 절대 좌표 레이아웃이라 표 스타일·동적 행 변경·헤더 스크롤·colspan 지원에 제약이 있었다.
- `case_0036` @tanstack/react-virtual: 복잡한 로그 표현 방식 대응, 바닥 감지 실패 원인 분석, 커스텀 기능 구현과 향후 요구사항 대응에 한계가 있다고 판단했다.
- `case_0037` ChainedTransactionManager 사용: 두 DB의 정합성이 아직 맞지 않고 MySQL CUD 동작 및 환경 최적화가 검증되지 않은 상태에서 MySQL 실패가 전체 트랜잭션 롤백으로 이어지면 안 됐다.
- `case_0037` 분산 트랜잭션으로 MySQL 쿼리 포함: Read 전환 전에는 MySQL 쿼리만 실패할 수 있으므로, MySQL 실패를 무시하면서 원자적으로 처리할 방식이 필요했다.
- `case_0037` MyBatis 인터페이스 분리 호출: 모든 쓰기 로직에 MySQL Repository 호출을 추가하려면 레거시 비즈니스 로직의 수백~수천 곳을 수정해야 해 휴먼 에러와 개발 기간 증가 위험이 컸다.
- `case_0037` HTTP 트래픽 복사 또는 Kafka 토픽 복제: 비즈니스 로직 호출이 타 부서 시스템에 중복 부하와 예상치 못한 운영 부작용을 일으킬 수 있었다.
- `case_0045` GlusterFS: 직접 운영하는 부담이 컸다.
- `case_0045` CephFS: 직접 운영하는 부담이 컸다.
- `case_0045` AWS EFS: Object Storage보다 비용이 크고, 사내 구축 환경에서 외부 클라우드 스토리지를 사용할 수 없었다.
- `case_0045` Google Filestore: 사내 구축 환경에서 외부 클라우드 스토리지를 사용할 수 없었다.
- `case_0045` Alluxio: 일부 POSIX API를 지원하지 않고, 원본 저장소 동기화와 별도 클러스터 운영 부담이 있었다.
- `case_0045` DDN EXAScaler: 요구 사항을 만족하지만 큰 비용이 발생했다.
- `case_0049` OpenSearch 2.4.1: Sudachi 지원 범위인 OpenSearch 2.6 이상에 미치지 못했다.
- `case_0051` 상품 인덱스의 Edge N-gram 적용: 8억 건 규모의 비정형 상품 인덱스에서는 인덱스 크기와 색인 처리 비용이 크게 증가할 수 있었다.
- `case_0052` Spark Streaming: 마이크로 배치 방식은 이벤트 시간 기준의 세밀한 상태 제어가 어려워 데이터 최신성 판별과 정확히 한 번 처리를 함께 만족하기 어려웠다.
- `case_0052` 네이티브 쿠버네티스 방식: 권한, 라우팅, 배포, 잡 구동에 필요한 설정을 수동으로 해야 했다.
- `case_0053` non-keyed window: 처리량이 늘면 단일 태스크로 동작해 성능을 심각하게 저하시켰다.
- `case_0054` Spark 온힙 메모리 증설: 코어 수를 줄이고 온힙 메모리를 늘려도 메모리 압박이 계속됐다.
- `case_0054` 공격적인 파일 압축 임계치: 대규모 테이블에서 잦은 병합 작업이 HDFS 전체 성능을 저하시켰다.
- `case_0058` WebAuthn Level 3 채택: Level 3는 공식적으로 확정되지 않은 초안 상태이고, 플랫폼 API로는 Passkey 동기화를 제어할 수 없다.
- `case_0061` nginx 라우팅 설정으로 적치 API 차단: 개발팀에 nginx 설정 변경 및 재시작 권한이 없었고, 인프라팀 협조 절차를 거치면 짧은 DB 점검 시간이 끝날 것으로 판단했다.
- `case_0062` AI의 MCP 직접 조회: 가져온 텍스트가 AI 처리 토큰으로 계산되어 2~3일치 수집만으로도 비용과 속도가 급격히 악화됐다.
- `case_0069` nginx 설정을 통한 접근 차단: 리버스 프록시·별도 게이트웨이가 없고 CORS 환경에서 프론트와 서버가 각각 nginx를 사용하며, nginx 설정은 인프라팀이 관리하는 Docker 베이스 이미지와 함께 생성되어 인프라 상황에 맞지 않았다.
- `case_0070` max-lifetime 증가: DB failover 시 slave로 빠르게 연결하기 위해 max-lifetime을 작게 유지해야 했다.
- `case_0071` 메모리 증설: 4GB에서 8GB로 증설했지만 임시 해결에 그쳤다.
- `case_0071` Parcel: 커스텀 설정이 제한적이었다.
- `case_0071` Rsbuild: 생태계가 작았다.
- `case_0076` READ COMMITTED 격리수준: Phantom Read로 기존 비즈니스 로직에 영향을 주는 사이드 이펙트를 우려했다.
- `case_0076` 잠금 읽기: 행 잠금으로 락 경합 및 데드락 가능성이 증가할 수 있다.
- `case_0077` Chrome DevTools Overrides: 필드 값이 많을 때 수동 수정이 번거롭고, 프로세스화할 테스트에 매번 수동 작업이 필요해 리소스가 과도하게 소모된다.
- `case_0077` Charles·Fiddler 프록시 툴 사용: 필드 값이 많을 때 수동 수정이 번거롭고, 프로세스화할 테스트에 매번 수동 작업이 필요해 리소스가 과도하게 소모된다.
- `case_0077` 실제 데이터 입력: API가 null 값을 반환하는 조건이 정의되지 않아 데이터 수정으로 null을 주입하기 어렵다.
- `case_0079` WebP 포맷 변환: 복잡한 이미지에서는 압축 효율이 낮고, 용량을 줄이기 위해 품질을 낮추면 시각적 품질 저하가 발생했다.
- `case_0079` 메인 스레드 Canvas 리사이징: Canvas 처리 비용과 디코딩·인코딩의 JS 블로킹으로 메인 스레드를 점유하고 클릭 이벤트가 무시됐다.
- `case_0079` Shared Worker: 이미지 처리에 불필요한 기능이 많았다.
- `case_0079` Service Worker: 이미지 처리에 불필요한 기능이 많았다.
- `case_0080` WriteConcern MAJORITY: 모든 요청이 Secondary 과반수 ACK 응답을 기다리면 큰 오버헤드가 발생할 수 있다.
- `case_0080` 모든 읽기의 PRIMARY 설정: Secondary 노드가 유휴 상태가 되어 리소스를 낭비할 수 있다.
- `case_0081` SQS 메시지 지연 전달: 지연 시간이 짧으면 타이밍 문제가 계속 발생할 수 있어 임시방편으로 판단했다.
- `case_0081` Outbox 패턴: 현재 상황에서는 설계와 구현에 필요한 시간 및 비용이 부담됐다.
- `case_0081` 로그 테일링 패턴: 현재 상황에서는 설계와 구현에 필요한 시간 및 비용이 부담됐다.

## 글 목록

| 글 | 길이 | 결과 | 항목 | 발췌 탈락 | 제목 |
| --- | --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | - | 0/0 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics |
| d2/4555524 | 18,452 | 추출/기술 선택·도입형 | case_0045 | 0/18 | AI 플랫폼을 위한 스토리지 JuiceFS 도입기 |
| d2/8366976 | 3,331 | 추출/문제 해결형 | case_0041, case_0042, case_0043, case_0044 | 0/20 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/3814947 | 16,662 | 추출/문제 해결형 | case_0038, case_0039, case_0040 | 0/25 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | - | 0/0 | Thread-safety in C++ |
| d2/1450243 | 15,218 | 추출/기술 선택·도입형 | case_0036 | 0/12 | 윈도잉(windowing) 기법을 적용한 고성능 표 컴포넌트 개발기 |
| d2/8992409 | 1,342 | 제외/회고·문화·행사 | - | 0/0 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| d2/6512234 | 22,022 | 추출/문제 해결형 | case_0037 | 0/14 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/1155434 | 9,048 | 제외/개념·튜토리얼 | - | 0/0 | C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가 |
| d2/9290861 | 796 | 제외/회고·문화·행사 | - | 0/0 | Inside VictoriaMetrics |
| kakao/601 | 3,137 | 제외/회고·문화·행사 | - | 0/0 | 제3회 Kakao Tech Meet 후기 - 불확정성에서 감동까지 |
| kakao/624 | 787 | 제외/회고·문화·행사 | - | 0/0 | 카카오의 스팸 메일 대응 전략: 문자열 변형 CASE STUDY / 제6회 Kakao Tech Meet |
| kakao/761 | 3,645 | 제외/회고·문화·행사 | - | 0/0 | 실패를 장려하는 실험적 문화 |
| kakao/762 | 13,811 | 제외/회고·문화·행사 | - | 0/0 | 생산성 혁신의 실험: AI 마일리지 프로그램 |
| kakao/770 | 16,500 | 추출/기술 선택·도입형 | case_0023 | 0/12 | 5년 된 프로젝트의 빌드 도구를 교체하며 얻은 것들 |
| kakao/784 | 8,710 | 제외/회고·문화·행사 | - | 0/0 | 단 1시간 만에 99개의 MVP가? AI와 함께한 1K: 바이브코딩전 생생 후기 |
| kakao/785 | 4,597 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며 |
| kakao/804 | 3,760 | 추출/기술 선택·도입형 | case_0021 | 0/8 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/822 | 20,047 | 추출/실험·활용기 | case_0022 | 0/11 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakao/835 | 12,198 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 둘째 날, 기술 세션 소개 |
| kakaopay/slack-bot-improving-operational-efficiency-2 | 5,044 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이 배포 효율화 1년 회고: 자동화 도입과 팀 생산성 향상 |
| kakaopay/tech-strategy-tpm | 9,673 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이 TPM은 어떤 일을 하나요? |
| kakaopay/katfun-joy-kotlin | 14,709 | 추출/실험·활용기 | case_0035 | 0/10 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kakaopay/ifkakao2024-devrel | 10,598 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스 준비 맛보기 |
| kakaopay/perftest_zone | 4,708 | 추출/기술 선택·도입형 | case_0025 | 0/10 | 카카오페이 성능 테스트 존을 소개합니다. |
| kakaopay/kakaopaysec-wecan | 8,650 | 추출/기술 선택·도입형 | case_0031, case_0032, case_0033, case_0034 | 0/23 | We Can Do Better: 개발자 플랫폼 효율화 이야기 |
| kakaopay/kakaopayins-opensearch-analyzer | 10,157 | 제외/개념·튜토리얼 | - | 0/0 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/kakaopayins-envelope-encryption | 18,389 | 추출/기술 선택·도입형 | case_0026, case_0027 | 0/12 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/pallas-v2-log-platform | 25,659 | 추출/기술 선택·도입형 | case_0028, case_0029, case_0030 | 0/34 | 일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트 |
| kakaopay/kakaopayins-fe-common-component | 7,059 | 추출/기술 선택·도입형 | case_0024 | 0/9 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kurly/cart-recommend-model-development | 9,206 | 추출/문제 해결형 | case_0073, case_0074, case_0075 | 0/17 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 1부 |
| kurly/commit-mvcc-set-autocommit | 16,463 | 추출/문제 해결형 | case_0076 | 0/12 | 데이터가 있었는데요, 아니 없어요 |
| kurly/deliveryproductteam-culture-1 | 4,454 | 추출/문제 해결형 | case_0072 | 0/10 | 딜리버리 프로덕트 개발팀의 개발문화 - 로그 & 알람편 |
| kurly/connection-leak | 6,791 | 추출/문제 해결형 | case_0070 | 0/10 | 99%가 모른다는 DB Connection 누수 문제 |
| kurly/refine-address-internalization-2 | 4,312 | 추출/문제 해결형 | case_0068 | 0/9 | 주소정제 서비스 내재화 - 2화 ( 그럴싸한 계획 ) |
| kurly/access-block-1 | 5,663 | 추출/문제 해결형 | case_0061 | 0/11 | nginx 설정 없이 우아하게 서비스 점검하기 (上) |
| kurly/access-block-2 | 8,383 | 추출/기술 선택·도입형 | case_0069 | 0/11 | nginx 설정 없이 우아하게 서비스 점검하기 (下) |
| kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0 | 13,290 | 추출/기술 선택·도입형 | case_0071 | 0/15 | 빌드가 터졌다: 5년 된 CMS 프로젝트의 Webpack4 → Vite 전환 |
| kurly/tech-spec-adoption-with-ai-automation | 8,164 | 추출/실험·활용기 | case_0065, case_0066, case_0067 | 0/20 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| kurly/claude-code-redesign-my-day | 7,389 | 추출/실험·활용기 | case_0062, case_0063, case_0064 | 0/25 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| ly/managing-multi-cdn-logs-traffics-with-vector | 16,695 | 추출/문제 해결형 | case_0059 | 0/11 | Vector를 활용해 멀티 CDN 로그 및 트래픽 관리하기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 18,813 | 추출/실험·활용기 | case_0055, case_0056, case_0057 | 0/20 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/improving-kubernetes-relay-api-server-performance-with-informer | 12,361 | 추출/문제 해결형 | case_0060 | 0/11 | Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기 |
| ly/introducing-fido2-client-sdk-open-source | 9,957 | 추출/기술 선택·도입형 | case_0058 | 2/10 | FIDO2 클라이언트 SDK 오픈소스 소개 |
| ly/how-to-evaluate-ai-generated-images-1 | 16,708 | 제외/개념·튜토리얼 | - | 0/0 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/extracting-trending-keywords-from-openchat-messages | 14,017 | 추출/문제 해결형 | case_0048 | 0/12 | 오픈챗 메시지들로부터 트렌딩 키워드 추출하기 |
| ly/pd1-ai-hackathon-recap | 4,153 | 제외/회고·문화·행사 | - | 0/0 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 6,232 | 추출/기술 선택·도입형 | case_0046, case_0047 | 0/17 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 및 서비스 상태 확인 도구 LINE Status 개발기 |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 19,601 | 추출/기술 선택·도입형 | case_0052, case_0053, case_0054 | 1/27 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/japanese-search-kuromoji-to-sudachi | 15,395 | 추출/기술 선택·도입형 | case_0049, case_0050, case_0051 | 0/26 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자가 좋아하는 과자는? |
| oliveyoung/2024-06-05_google-cloud-next-24-review | 3,796 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next '24 방문기 |
| oliveyoung/2024-08-11_type-and-type-system-with-typescript | 11,673 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 타입과 타입 시스템 |
| oliveyoung/2024-09-30_oy-feconf-2024 | 8,894 | 제외/회고·문화·행사 | - | 0/0 | 올리브영에서는 프론트엔드 개발자들이 이런 고민을 하는군요? |
| oliveyoung/2024-10-17_oy-delivery-mq | 4,642 | 추출/기술 선택·도입형 | case_0083 | 0/9 | 올리브영 물류시스템에서는 데이터를 어떻게 주고 받을까? |
| oliveyoung/2024-12-16_Design-System-Token-Automation | 17,955 | 추출/실험·활용기 | case_0082 | 0/10 | 디자인 시스템 중 디자인 토큰을 여러 도구를 이용하여 자동화 하는 방법 |
| oliveyoung/2024-12-17_catalog-mongo-transaction-2 | 11,450 | 추출/문제 해결형 | case_0080, case_0081 | 0/14 | Spring Boot MongoDB 트랜잭션 도입 실전 가이드 |
| oliveyoung/2025-02-14_oy-global-mall-address | 4,978 | 추출/기술 선택·도입형 | case_0078 | 0/8 | 올리브영 글로벌몰 주소 자동완성 및 검증 솔루션 도입기 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 7,158 | 추출/문제 해결형 | case_0079 | 0/14 | Web Worker로 이미지 처리 최적화하기 |
| oliveyoung/2025-06-10_chaos | 7,289 | 추출/실험·활용기 | case_0077 | 0/12 | 버그가 아니라 장애를 잡아라!! QA와 카오스 엔지니어링의 만남 |
| toss/27752 | 5,980 | 추출/문제 해결형 | case_0007 | 0/10 | 드래그 앤 드롭은 사실 편한 UX가 아니다? |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | - | 0/0 | 오픈소스에 기여하고 토스에 합격한.ssul \| EP.4 모닥불 |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | - | 0/0 | 개발자 리더로서 성장당한 썰 \| EP.7 모닥불 |
| toss/toss-frontend-ai-docs | 2,869 | 추출/실험·활용기 | case_0002 | 0/8 | 토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유 |
| toss/toss-people-3 | 7,801 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 문과생에서 토스 개발 리더까지 |
| toss/frontend-esbuild-hmr | 10,415 | 제외/회고·문화·행사 | - | 0/0 | ESBuild를 위한 HMR, 직접 만들기 |
| toss/frontend-apply-without-resume | 2,783 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드에 이력서 없이 리포지토리 링크로 지원하세요 (~5/31) |
| toss/toss-securities-gpu-mig | 13,794 | 추출/기술 선택·도입형 | case_0001 | 0/15 | GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기 |
| toss/tds-color-system-update | 13,423 | 추출/기술 선택·도입형 | case_0003, case_0004, case_0005, case_0006 | 0/32 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| toss/ads_dashboard_fe | 12,467 | 추출/기술 선택·도입형 | case_0008 | 0/15 | 전체 데이터를 브라우저에 두는 광고 대시보드 만들기 |
| woowahan/14484 | 5,518 | 추출/문제 해결형 | case_0017 | 0/8 | “일단 백로그에 넣어두고 여유 있을 때 보는 걸로 할까요?” : 백로그를 백로그로 두지 않는 법 |
| woowahan/14671 | 6,108 | 제외/회고·문화·행사 | - | 0/0 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/15398 | 10,772 | 제외/개념·튜토리얼 | - | 0/0 | Java의 미래, Virtual Thread |
| woowahan/15541 | 6,445 | 제외/개념·튜토리얼 | - | 0/0 | 웹 접근성 준수를 통한 모두에게 배달되는 일상의 행복 |
| woowahan/17386 | 11,245 | 추출/실험·활용기 | case_0018, case_0019, case_0020 | 0/25 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/17911 | 4,799 | 추출/기술 선택·도입형 | case_0014 | 0/11 | B마트 주문 유실을 없애보자: 네트워크 편 |
| woowahan/20763 | 8,615 | 추출/기술 선택·도입형 | case_0015, case_0016 | 0/23 | 이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기 |
| woowahan/21027 | 25,102 | 추출/기술 선택·도입형 | case_0009 | 0/10 | 실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법 |
| woowahan/24434 | 15,179 | 추출/문제 해결형 | case_0012, case_0013 | 0/21 | “함께 구매하면 좋은 상품” 추천 모델 고도화 |
| woowahan/24999 | 12,341 | 추출/문제 해결형 | case_0010, case_0011 | 0/17 | WOOWACON 2025 미니게임 WOOWA POP! |
