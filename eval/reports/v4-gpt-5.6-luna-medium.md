# 추출 점검 리포트: v4-gpt-5.6-luna-medium

- 모델: gpt-5.6-luna (medium)
- 프롬프트 버전: 5bafd9ddcc5d
- 글 80편: 추출 53, 제외 27
- 항목 83개
- 토큰: 호출 143회, 입력 1,118,884 (캐시 405,797), 출력 155,519 (reasoning 54,777)
- 비용: $0.337 (편당 $0.0042), 전체 1,262편 추정 $5.3 / Batch $2.7

## 블로그별 추출 여부

| 블로그 | 추출 | 제외 | 항목 수 |
| --- | --- | --- | --- |
| d2 | 6 | 4 | 13 |
| kakao | 2 | 8 | 3 |
| kakaopay | 8 | 2 | 10 |
| kurly | 10 | 0 | 13 |
| ly | 8 | 2 | 14 |
| oliveyoung | 6 | 4 | 7 |
| toss | 6 | 4 | 10 |
| woowahan | 7 | 3 | 13 |

## 글 유형 × 추출 여부

| 글 유형 | 추출 | 제외 |
| --- | --- | --- |
| 개념·튜토리얼 | 0 | 5 |
| 기술 선택·도입형 | 17 | 1 |
| 문제 해결형 | 22 | 1 |
| 실험·활용기 | 14 | 1 |
| 회고·문화·행사 | 0 | 19 |

## 짧은 글 (평문 1,500자 미만) 8편

| 글 | 길이 | 결과 | 항목 | 분류 이유 |
| --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션과 발표 목차를 소개하는 글로, 본문에 구체적인 문제 해결 과정이나 성능 비교·설계 근거가 서술되어 있지 않다. |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | 0 | C++의 data race, 메모리 순서, thread safety, 동기화 프리미티브 등의 기본 개념과 사용법을 설명하는 행사 발표 자료 소개 글이며, 특정 팀의 문제 해결 과정이나 실제 적용 결과·설계 근거는 제시하지 않습니다. |
| d2/8992409 | 1,342 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, DBT·Airflow 기반 파이프라인의 구체적인 문제 해결 과정이나 설계 근거·적용 결과는 제시하지 않고 발표 내용과 목차만 나열하고 있다. |
| d2/9290861 | 796 | 제외/개념·튜토리얼 | 0 | VictoriaMetrics의 내부 구조와 구성 요소를 설명하는 발표 소개 글이지만, 실제 운영 문제를 해결한 과정이나 구체적인 설계 결정·비교·적용 결과가 본문에 제시되지 않았습니다. 사내 행사 세션 공개 및 목차 중심의 글이므로 제외합니다. |
| kakao/624 | 787 | 제외/회고·문화·행사 | 0 | Kakao Tech Meet 발표 영상과 발표자 인터뷰를 소개하는 행사 후기 성격의 글이며, 문자열 변형 스팸 대응의 구체적인 문제 해결 과정이나 설계 근거·적용 결과는 본문에 제시되지 않았습니다. |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | 0 | 개발자 대상 간식 선호도 설문과 결과를 소개하는 조직 문화·구성원 관련 글이며, 기술 문제 해결이나 기술 적용 사례가 없습니다. |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | 0 | 토스 개발자들의 오픈소스 기여 경험과 기술적 성장에 관한 영상·대담을 소개하는 행사성 콘텐츠로, 구체적인 문제 해결 과정이나 적용 결과·설계 근거가 본문에 제시되지 않는다. |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | 0 | 프론트엔드 리드들의 리더십 성장과 조직 성장에 관한 경험을 다루는 콘텐츠로, 구체적인 기술 문제 해결이나 기술 도입·적용 사례가 아니라 리더십·조직 문화 중심의 이야기이다. |

## 글당 항목 수 (제외 글 빼고)

| 항목 수 | 글 수 |
| --- | --- |
| 1 | 34 |
| 2 | 10 |
| 3 | 7 |
| 4 | 2 |

## 문제 유형 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 개발 생산성 | 30 | 36% |
| 모니터링·관측성 | 16 | 19% |
| 데이터 파이프라인 | 15 | 18% |
| 배포·CI/CD | 12 | 14% |
| DB 성능·쿼리 최적화 | 12 | 14% |
| 업무·운영 자동화 | 11 | 13% |
| 인프라·컨테이너 | 10 | 12% |
| 데이터 정합성·트랜잭션 | 10 | 12% |
| 장애 대응·복구 | 9 | 11% |
| 비용 절감 | 7 | 8% |
| 인증·보안 | 6 | 7% |
| API 설계·외부 연동 | 6 | 7% |
| 클라이언트 성능(웹·앱) | 5 | 6% |
| 메시징·비동기 처리 | 5 | 6% |
| 캐싱 | 4 | 5% |
| 트래픽 급증 대응 | 4 | 5% |
| 테스트 자동화 | 2 | 2% |
| DB 마이그레이션·샤딩 | 2 | 2% |
| 동시성·락 | 1 | 1% |

- 쏠림(30% 초과): 개발 생산성
- 한 번도 안 쓰인 분류 (1개): MSA

## 도메인 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 사내 플랫폼·개발 도구 | 31 | 37% |
| 커머스·주문·재고 | 22 | 27% |
| 검색·추천 | 14 | 17% |
| 배달·물류 | 10 | 12% |
| 범용 | 8 | 10% |
| LLM·AI | 7 | 8% |
| 채팅·메시징 서비스 | 5 | 6% |
| 결제·금융 | 4 | 5% |
| 콘텐츠·미디어 | 3 | 4% |
| 광고·마케팅 | 1 | 1% |

- 쏠림(30% 초과): 사내 플랫폼·개발 도구
- 한 번도 안 쓰인 분류 (0개): 없음

## 발췌 검증

- 채택한 시도 기준 발췌 795개 중 탈락 6개 (원문 존재율 99%)
- 재시도한 글 10편

- `d2/4555524`: 이를 ${pvc.name}, ${pvc.namespace}, ${pvc.annotations['<annotation>']}와 같이 사용자가 생성한 PVC에서 Secret을 참조할 수 있도록 개선했다.
- `d2/1155434`: reinterpret_cast로 포인터 타입을 변환하는 것 자체는 미정의 동작이 아닙니다. 미정의 동작이 발생하는 시점은 변환 결과를 역참조할 때입니다.
- `kakao/770`: 이와 더불어 Rsbuild의 생태계 규모도 상대적으로 작아 보였습니다. GitHub Star 개수, StackOverflow에서의 질문 개수도 2025년 9월 기준, 50개 미만일 정도로 도움이 필요할 때 지원받기에는 부족하고 실서비스에는 적용하기 어렵다고 느꼈습니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 그랬더니 미처 예상치 못했던 단어들이, 예를 들어 오랜만에 경기가 열리는 지방 도시 이름이라던가 말이나 기수 또는 참가 팀 이름 등 미리 지정하는 게 사실상 불가능한 단어들이 걸러지지 못하고 추천 키워드로 추출됐습니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 검토 결과 다양성이 충분히 확보되는 편이 바람직하다고 의견이 모여 페널티 가중치가 2 이상인 구간에서 α값을 결정했습니다.
- `oliveyoung/2025-02-14_oy-global-mall-address`: 딱 '미국'만을 대상으로 제공되고 있었죠. 그것도 '우편번호'로만 검색하도록요.

## 기술 사전에 없는 이름 133종

- Jira (4)
- GitHub (3)
- Locust (3)
- HDFS (3)
- Web Worker (2)
- Figma (2)
- Android (2)
- iOS (2)
- Node2Vec (2)
- Transformer (2)
- Netty (2)
- C++ (2)
- Webpack (2)
- Storybook (2)
- Vite (2)
- Babel (2)
- Rollup (2)
- Confluence (2)
- Dokka (2)
- Hive (2)
- Sudachi (2)
- JuiceFS (2)
- Iceberg (2)
- MIG (1)
- H100 (1)
- H200 (1)
- nvidia-device-plugin (1)
- dcgm-exporter (1)
- ESBuild (1)
- SWC (1)
- react-refresh (1)
- Token Studio (1)
- Style Dictionary (1)
- WebAssembly (1)
- Rust (1)
- Item2Vec (1)
- Focal Loss (1)
- Bayesian Smoothing (1)
- Amazon RDS for PostgreSQL (1)
- pgvector (1)
- Atlas MongoDB (1)
- Milvus (1)
- Redis Stack (1)
- LTE 라우터 (1)
- IPSEC (1)
- RADIUS (1)
- Spring Cloud (1)
- AWS S3 (1)
- AWS Athena (1)
- Virtual Thread (1)
- libevent (1)
- S2 Geometry (1)
- AWS ALB (1)
- Hazelcast (1)
- Chronicle Map (1)
- fastutil (1)
- HPPC (1)
- Trove (1)
- Koloboke (1)
- JMH (1)
- Codex (1)
- Jest (1)
- Vitest (1)
- ClickStack (1)
- HyperDX (1)
- Amazon Athena (1)
- Filebeat (1)
- AWS KMS (1)
- CloudTrail (1)
- Apache Lucene (1)
- MobX (1)
- Material-UI (1)
- Tailwind CSS (1)
- esbuild (1)
- qs (1)
- dayjs (1)
- react-csv (1)
- Taskmaster (1)
- MariaDB (1)
- AWS EC2 (1)
- mysql-connector-j (1)
- MemoryAnalyzer (1)
- 행안부 도로명주소 조회 API (1)
- Google Sheets (1)
- BigQuery (1)
- Vue Router (1)
- Swagger (1)
- Postman (1)
- mitmproxy (1)
- OffscreenCanvas (1)
- MySQL Aurora (1)
- MariaDB Connector/J (1)
- BERT4Rec (1)
- MLflow (1)
- PyTorch (1)
- Gradio (1)
- GrowthBook (1)
- Yarn (1)
- Panda CSS (1)
- Tokens Studio for Figma (1)
- token-transformer (1)
- Spring Data MongoDB (1)
- WiredTiger (1)
- AssertJ (1)
- Spinnaker (1)
- Mongo (1)
- InfluxDB (1)
- GCP (1)
- react-window (1)
- @tanstack/react-table (1)
- Release Please Action (1)
- Maven Central Repository (1)
- JFrog Artifactory (1)
- GitHub Pages (1)
- Ruler (1)
- datasource-proxy (1)
- Kuromoji (1)
- IPADIC (1)
- Lucene (1)
- MinIO (1)
- Secure Enclave (1)
- ARM TrustZone (1)
- Android StrongBox (1)
- ZSTD (1)
- Kubernetes Python client (1)
- Kubernetes Go client (1)
- Hubot (1)
- Ansible (1)
- Harbor (1)
- Git (1)
- hubot-conversation (1)
- Vector (1)
- Akamai (1)

## 버린 대안 80개 (항목 83개 중)

- `case_0001` 클라우드 GPU: 장기적이고 지속적인 워크로드와 자체 클러스터 환경에서는 비용이 더 발생할 수 있고, 데이터 보안·컴플라이언스 및 인스턴스 제어 제약이 있다.
- `case_0001` 혼합 GPU 운영: GPU 세대·메모리 차이로 드라이버, CUDA, 프레임워크 호환성과 스케줄링 관리가 복잡해지고, 수요가 고용량 GPU에 집중되면 저용량 GPU가 유휴화될 수 있다.
- `case_0001` MPS: 소프트웨어 방식이라 리소스 간 명확한 격제가 어렵고 성능 간섭과 프로세스별 리소스 모니터링·제어의 복잡성이 있다.
- `case_0002` Virtual Scrolling: 한 번에 그리는 행이 100건이라 DOM 부하가 병목이 아니었고, 현재 페이지 단위 UX에는 필요하지 않았다.
- `case_0002` IndexedDB 캐싱: 세션 안에서 데이터를 유지하는 것만으로 문제를 해결할 수 있었고, 무효화 규칙·버전 관리·스키마 마이그레이션 비용이 필요 이상으로 컸다.
- `case_0011` ZK-SNARK: 우아팝에 적용하는 것은 효과적이지 않다고 판단했다.
- `case_0016` Atlas MongoDB: RDS가 더 높은 처리량과 짧은 응답 시간, 실패 없는 결과를 보여 최종 선정에서 제외했다.
- `case_0016` OpenSearch: 부하 테스트에서 요청 실패가 발생했고 RDS보다 성능이 낮았다. **(technologies에도 있음)**
- `case_0017` 에그: 내부망 연결, 배터리 충전 등의 사용자 교육 비용과 추가 네트워크 관리 비용이 발생해 운영 비용이 커진다.
- `case_0017` 5G 상품: 유선 인터넷과 비교해 품질, 속도 및 안정성이 낮다고 판단했다.
- `case_0022` 캐시 레이어를 이용한 구조 개선: 기존 메모리 적재 구조를 유지하는 방안으로 결정해 채택하지 않았다.
- `case_0022` Blue/Green 배포: 트래픽을 세밀하게 조절하기 위해 일반적인 Blue/Green 배포 대신 두 TargetGroup을 이용하는 방식을 선택했다.
- `case_0023` GC 튜닝: GC 파라미터 튜닝보다 메모리 저장 구조 개선을 우선하기로 했다.
- `case_0023` Hazelcast: 단순 key-value 조회 이상의 기능을 지원해 현재 상황에서는 과하다고 판단했다.
- `case_0023` Chronicle Map: 진입 장벽이 높고 라이브러리 이해도가 낮은 부분이 걱정되어 채택하지 않았다.
- `case_0023` HPPC: fastutil과 기능 차이가 크지 않았고 특정 라이브러리가 크게 우수하다는 근거가 없었다.
- `case_0023` Trove: fastutil과 기능 차이가 크지 않았고 특정 라이브러리가 크게 우수하다는 근거가 없었다.
- `case_0023` Koloboke: fastutil과 기능 차이가 크지 않았고 특정 라이브러리가 크게 우수하다는 근거가 없었다.
- `case_0023` static final 선언: JDK 11 기준으로 효과가 없었다.
- `case_0025` 재사용 가능한 script: 반복 명령을 재사용 가능한 script로 묶을 수 있지만, LLM을 사용하면 고정적인 script가 아니어도 빠르고 쉽게 변경할 수 있고 skill 단위 구성이 orchestrator 기반이 된다.
- `case_0026` Parcel: Zero-config는 매력적이지만 복잡한 프로젝트에서는 설정 자동화의 리스크가 있고, 복잡한 커스터마이징에 제한이 있다고 판단했다.
- `case_0028` OpenSearch: 비용이 높고 대용량 집계 쿼리가 느려 현재 로그 조회 패턴에 맞지 않았다. **(technologies에도 있음)**
- `case_0028` Grafana Loki: 복잡한 쿼리와 집계 기능이 부족하고 서비스 1,000개 이상의 환경에서 카디널리티 부담이 있었다.
- `case_0028` Amazon Athena: 2,000개 이상 컬럼의 로그를 테이블로 정의하기 어렵고 대용량 집계 쿼리가 느렸다.
- `case_0028` Signoz: 자체 스키마를 강제해 Buffer·Store·View를 분리한 ClickHouse 구조를 활용할 수 없었다.
- `case_0029` Entity Life Cycle 콜백: 조회 시 @PostLoad에서 엔티티 필드를 복호화하면 JPA 1차 캐시가 값 변경으로 판단해 불필요한 UPDATE를 발생시키며, PreLoad 주기가 없어 해결할 수 없었다.
- `case_0031` 메모리 증설: 메모리를 계속 늘리는 방식은 임시방편에 불과해 번들러 전환을 선택했다.
- `case_0031` Parcel: 커스텀 설정이 제한적이고 MobX Decorator 지원이 제한적이었다.
- `case_0031` Rsbuild: 생태계가 작아 선택하지 않았다.
- `case_0032` 네이티브 앱 구현: 쿠폰 및 프로모션 정책이 변경될 때마다 앱 심사와 업데이트를 거쳐야 하므로, 배포 즉시 최신 로직을 반영할 수 있는 웹뷰를 선택했다.
- `case_0033` Notion: 수작업으로 정리하는 방식은 노동력 때문에 오래 유지되지 않았다.
- `case_0036` nginx 라우팅 설정: 개발팀에 실행 중인 인스턴스의 nginx 설정 파일을 변경하거나 nginx를 재시작할 권한이 없었고, 인프라 팀에 협조를 요청하면 점검이 끝난 뒤에 처리될 가능성이 있었다.
- `case_0036` 주기적 스케줄링 배치: 스케줄링 배치를 활용하는 방안을 고민했지만, 최소한의 공수로 하나의 인스턴스 안에서 해결하기 위해 채택하지 않았다.
- `case_0037` HikariCP max-lifetime 증가: Connection 누수 자체는 방지할 수 있지만, DB failover 시 slave로 빠르게 연결하기 위해 max-lifetime을 작게 설정하고 있어 최종적으로 선택하지 않았다.
- `case_0039` nginx 설정을 통한 접근 차단: nginx가 모든 요청을 받는 리버스 프록시 구조가 아니고, nginx 설정이 인프라팀 관리 하에 도커의 베이스 이미지와 함께 생성되므로 현재 인프라에 적합하지 않았다.
- `case_0039` BigQuery 직접 질의: 페이지 라우팅과 API 호출마다 BigQuery를 조회하면 네트워크 지연과 프로덕트 성능 저하가 발생할 수 있었다.
- `case_0039` 업무 시스템 RDBMS 연동: 업무 시스템에서 사용하는 RDBMS와 종속되지 않는 별도의 데이터 저장소가 필요했다.
- `case_0041` Google Overwrite Contents: 일회성 테스트에는 유용하지만 매번 수동 작업이 필요해 프로세스화하기에 리소스가 과도하게 소모된다고 판단했다.
- `case_0041` Charles·Fiddler 수동 수정: API 필드가 많을 때 하나씩 수동으로 수정해야 하므로 향후 반복 테스트에 적합하지 않다고 판단했다.
- `case_0041` 실제 데이터 수정: API가 어떤 조건에서 null 값을 전달하는지 정의되지 않아 데이터 수정만으로 null을 전달하기 어렵다고 판단했다.
- `case_0042` 이미지 포맷 변환: WebP 등으로 변환했지만 복잡한 이미지의 압축 효율이 낮았고, 품질을 낮추면 시각적 퀄리티가 저하되어 실제 적용에 제약이 있었다.
- `case_0042` Canvas 이미지 리사이징: 파일 크기와 업로드 속도는 개선됐지만 Canvas 처리 비용과 디코딩·인코딩 과정이 메인 스레드를 점유해 클릭 이벤트가 지연됐다.
- `case_0042` Shared Worker: 이미지 처리에는 여러 탭·창 공유 기능이 불필요해 배제했다.
- `case_0042` Service Worker: 이미지 처리에는 네트워크 프록시와 오프라인 지원 등의 기능이 불필요해 배제했다.
- `case_0043` READ COMMITTED 격리수준: REPEATABLE READ를 READ COMMITTED로 낮추면 Phantom Read가 발생해 기존 비즈니스 로직에 영향을 줄 수 있어 채택하지 않았다.
- `case_0043` 잠금 읽기: 최신 데이터를 읽을 수 있지만 행 잠금으로 락 경합과 데드락 가능성이 증가해 채택하지 않았다.
- `case_0045` 주문서 원본 데이터 그대로 학습: 주문서 상품을 모두 보완재로 가정해 그대로 학습했지만 특정 상품이 반복 추천되어 보완재 추천 품질이 떨어졌다.
- `case_0045` 카테고리 관계 수작업 설정: 사람이 보완재 카테고리 관계를 설정하면 작업이 어렵고 객관적으로 평가하기 어렵기 때문에 데이터 기반 정량 평가를 선택했다.
- `case_0048` WriteConcern MAJORITY: 데이터 정확성은 높일 수 있지만 모든 요청에서 Secondary 과반수 ACK를 기다려 큰 오버헤드가 발생할 수 있다.
- `case_0048` MongoClient ReadPreference PRIMARY: 모든 읽기를 PRIMARY에 집중하면 SECONDARY가 유휴 상태로 남을 수 있어 트랜잭션에만 PRIMARY를 적용하기로 했다.
- `case_0049` SQS 메시지 지연 전달: 지연 시간이 너무 짧으면 타이밍 문제가 다시 발생할 수 있어 임시방편으로 판단했다.
- `case_0049` Outbox 패턴·로그 테일링 패턴: 데이터와 메시지를 분리할 수 있지만 현재 상황에서는 설계 및 구현 비용이 부담됐다.
- `case_0050` EAI I/F: 배치 지연과 EAI 어댑터 장애 시 전체 통신이 멈추는 문제가 있어 새 시스템으로 전환했다.
- `case_0057` @tanstack/react-virtual: 로그 표현 방식이 복잡하고 스크롤 바닥 감지 실패 원인 분석, 커스텀 기능 구현, 향후 요구사항 대응에 어려움이 있어 자체 개발을 선택했다.
- `case_0058` reinterpret_cast 타입 퍼닝: uint32_t 객체를 float*로 접근하면 엄격한 앨리어싱 규칙을 위반하므로 미정의 동작이 발생한다.
- `case_0058` union 타입 퍼닝: C++에서는 비활성 union 멤버를 읽는 방식이 표준을 준수하지 않는다.
- `case_0058` std::bit_cast 포인터 변환: 포인터의 대상이 아니라 포인터 값의 비트를 복사하며, 역참조 시 엄격한 앨리어싱 위반과 const 우회 문제가 발생할 수 있다.
- `case_0062` ChainedTransactionManager: Oracle과 MySQL 간 데이터 정합성이 대부분 맞지 않고 MySQL 쿼리와 환경 설정이 검증되지 않은 상태였기 때문에 사용하지 않았다.
- `case_0062` 분산 트랜잭션: MySQL 쿼리만 실패하는 상황을 허용하고 실패해도 트랜잭션을 롤백하지 않아야 했기 때문에 사용하지 않았다.
- `case_0062` MyBatis 양쪽 Repository 직접 호출: 모든 쓰기 로직에 양쪽 Repository 호출을 추가하려면 10년 넘은 서비스의 비즈니스 로직 전체를 수정해야 했다.
- `case_0063` HTTP 트래픽 복사: 타 부서 시스템에 중복 호출 부하를 야기하거나 예상치 못한 부작용으로 운영에 영향을 줄 위험이 높았다.
- `case_0063` Kafka 토픽 복제: 타 부서 시스템에 중복 호출 부하를 야기하거나 예상치 못한 부작용으로 운영에 영향을 줄 위험이 높았다.
- `case_0067` Elasticsearch ← Elastic Search: 질의 분석 정확도를 높이고 복잡한 질의에 유연하게 대응하기 위해 네이버 자체 검색 엔진으로 전환했습니다.
- `case_0068` Elasticsearch 8.x 업그레이드: 사내 검색 플랫폼이 Elasticsearch 7.10.2까지만 지원하고 이후 버전 업그레이드 없이 일몰 방향으로 가고 있어 고려 대상에서 제외했다.
- `case_0068` mecab-ipadic-neologd: Kuromoji는 MeCab 기반 사전을 직접 연동하는 구조가 아니며 Elasticsearch 7.10.2 환경에서 최신 사전 적용에 제약이 있었다.
- `case_0072` Alluxio: 일부 POSIX API를 지원하지 않고 원본 저장소와 동기화해야 하며 master·worker 클러스터 운영 부담이 있었다.
- `case_0072` GlusterFS·CephFS 직접 운영: 오픈소스를 직접 운영하는 부담이 컸다.
- `case_0072` Ceph-rbd: ReadWriteMany와 ReadOnlyMany를 지원하지 않아 여러 Pod의 동시 접근이 불가능했다.
- `case_0072` NFS: 간단하지만 확장성과 HA 문제가 있었다.
- `case_0072` local-path: 노드 간 동시 접근이 불가능하고 노드별 데이터 위치에 따른 추가 스케줄링 또는 앱 구현이 필요했다.
- `case_0073` HDFS credential cache: KRB5CCNAME으로 설정한 credential cache가 일정 시간이 지나면 만료되어 유효하지 않게 된다.
- `case_0073` 고정된 StorageClass Secret: 사용자별 Secret을 동적으로 참조할 수 없었다.
- `case_0074` WebAuthn Level 3: Level 3 스펙은 아직 공식적으로 확정되지 않은 초안 상태이며, Passkey 동기화를 현재 플랫폼 API로 제어할 수 없어 채택하지 않았다.
- `case_0075` Spark Streaming: 마이크로 배치 방식으로는 이벤트 시간 기반 상태를 세밀하게 제어하기 어려워 데이터 최신성 판별과 정확히 한 번 처리를 동시에 만족하기 어렵다고 판단했다.
- `case_0075` 네이티브 쿠버네티스: Flink 배포와 권한·라우팅·잡 구동 설정을 수동으로 구성해야 했다.
- `case_0076` 비키 기반 윈도: 단일 태스크로 작동해 처리량 증가 시 성능을 심각하게 저하시켰다.
- `case_0077` Spark 온힙 메모리 증설: 코어 수를 줄이고 온힙 메모리를 늘렸지만 메모리 압박이 계속됐다.
- `case_0078` Python 클라이언트: Python 클라이언트에서는 Informer를 사용할 수 없다고 판단해 Go 클라이언트로 변경했다.
- `case_0079` 전날 빈도 비교: 화제성이 정점에 달해 증가량이 작아지면 트렌딩 키워드로 탐지되지 않을 수 있다.
- `case_0080` 블랙리스트: 미리 지정하기 어려운 연관 단어들이 추천 키워드로 추출됐다.

## 글 목록

| 글 | 길이 | 결과 | 항목 | 발췌 탈락 | 제목 |
| --- | --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | - | 0/0 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics |
| d2/4555524 | 18,452 | 추출/기술 선택·도입형 | case_0072, case_0073 | 1/29 | AI 플랫폼을 위한 스토리지 JuiceFS 도입기 |
| d2/8366976 | 3,331 | 추출/문제 해결형 | case_0064, case_0065, case_0066, case_0067 | 0/21 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/3814947 | 16,662 | 추출/실험·활용기 | case_0059, case_0060, case_0061 | 0/24 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | - | 0/0 | Thread-safety in C++ |
| d2/1450243 | 15,218 | 추출/문제 해결형 | case_0057 | 0/11 | 윈도잉(windowing) 기법을 적용한 고성능 표 컴포넌트 개발기 |
| d2/8992409 | 1,342 | 제외/회고·문화·행사 | - | 0/0 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| d2/6512234 | 22,022 | 추출/문제 해결형 | case_0062, case_0063 | 0/24 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/1155434 | 9,048 | 추출/문제 해결형 | case_0058 | 1/13 | C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가 |
| d2/9290861 | 796 | 제외/개념·튜토리얼 | - | 0/0 | Inside VictoriaMetrics |
| kakao/601 | 3,137 | 제외/회고·문화·행사 | - | 0/0 | 제3회 Kakao Tech Meet 후기 - 불확정성에서 감동까지 |
| kakao/624 | 787 | 제외/회고·문화·행사 | - | 0/0 | 카카오의 스팸 메일 대응 전략: 문자열 변형 CASE STUDY / 제6회 Kakao Tech Meet |
| kakao/761 | 3,645 | 제외/회고·문화·행사 | - | 0/0 | 실패를 장려하는 실험적 문화 |
| kakao/762 | 13,811 | 제외/실험·활용기 | - | 0/0 | 생산성 혁신의 실험: AI 마일리지 프로그램 |
| kakao/770 | 16,500 | 추출/기술 선택·도입형 | case_0026 | 1/14 | 5년 된 프로젝트의 빌드 도구를 교체하며 얻은 것들 |
| kakao/784 | 8,710 | 제외/회고·문화·행사 | - | 0/0 | 단 1시간 만에 99개의 MVP가? AI와 함께한 1K: 바이브코딩전 생생 후기 |
| kakao/785 | 4,597 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며 |
| kakao/804 | 3,760 | 제외/기술 선택·도입형 | - | 0/0 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/822 | 20,047 | 추출/실험·활용기 | case_0024, case_0025 | 0/21 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakao/835 | 12,198 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 둘째 날, 기술 세션 소개 |
| kakaopay/slack-bot-improving-operational-efficiency-2 | 5,044 | 추출/기술 선택·도입형 | case_0052 | 0/10 | 카카오페이 배포 효율화 1년 회고: 자동화 도입과 팀 생산성 향상 |
| kakaopay/tech-strategy-tpm | 9,673 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이 TPM은 어떤 일을 하나요? |
| kakaopay/katfun-joy-kotlin | 14,709 | 추출/실험·활용기 | case_0051 | 0/8 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kakaopay/ifkakao2024-devrel | 10,598 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스 준비 맛보기 |
| kakaopay/perftest_zone | 4,708 | 추출/기술 선택·도입형 | case_0053 | 0/9 | 카카오페이 성능 테스트 존을 소개합니다. |
| kakaopay/kakaopaysec-wecan | 8,650 | 추출/기술 선택·도입형 | case_0054, case_0055, case_0056 | 0/21 | We Can Do Better: 개발자 플랫폼 효율화 이야기 |
| kakaopay/kakaopayins-opensearch-analyzer | 10,157 | 추출/실험·활용기 | case_0030 | 0/9 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/kakaopayins-envelope-encryption | 18,389 | 추출/문제 해결형 | case_0029 | 0/11 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/pallas-v2-log-platform | 25,659 | 추출/기술 선택·도입형 | case_0028 | 0/16 | 일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트 |
| kakaopay/kakaopayins-fe-common-component | 7,059 | 추출/기술 선택·도입형 | case_0027 | 0/8 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kurly/cart-recommend-model-development | 9,206 | 추출/문제 해결형 | case_0045 | 0/14 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 1부 |
| kurly/commit-mvcc-set-autocommit | 16,463 | 추출/문제 해결형 | case_0043, case_0044 | 0/17 | 데이터가 있었는데요, 아니 없어요 |
| kurly/deliveryproductteam-culture-1 | 4,454 | 추출/실험·활용기 | case_0040 | 0/10 | 딜리버리 프로덕트 개발팀의 개발문화 - 로그 & 알람편 |
| kurly/connection-leak | 6,791 | 추출/문제 해결형 | case_0037 | 0/10 | 99%가 모른다는 DB Connection 누수 문제 |
| kurly/refine-address-internalization-2 | 4,312 | 추출/문제 해결형 | case_0038 | 0/9 | 주소정제 서비스 내재화 - 2화 ( 그럴싸한 계획 ) |
| kurly/access-block-1 | 5,663 | 추출/문제 해결형 | case_0036 | 0/14 | nginx 설정 없이 우아하게 서비스 점검하기 (上) |
| kurly/access-block-2 | 8,383 | 추출/문제 해결형 | case_0039 | 0/13 | nginx 설정 없이 우아하게 서비스 점검하기 (下) |
| kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0 | 13,290 | 추출/기술 선택·도입형 | case_0031 | 0/12 | 빌드가 터졌다: 5년 된 CMS 프로젝트의 Webpack4 → Vite 전환 |
| kurly/tech-spec-adoption-with-ai-automation | 8,164 | 추출/기술 선택·도입형 | case_0032 | 0/10 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| kurly/claude-code-redesign-my-day | 7,389 | 추출/실험·활용기 | case_0033, case_0034, case_0035 | 0/22 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| ly/managing-multi-cdn-logs-traffics-with-vector | 16,695 | 추출/문제 해결형 | case_0083 | 0/11 | Vector를 활용해 멀티 CDN 로그 및 트래픽 관리하기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 18,813 | 추출/실험·활용기 | case_0082 | 0/10 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/improving-kubernetes-relay-api-server-performance-with-informer | 12,361 | 추출/문제 해결형 | case_0078 | 0/10 | Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기 |
| ly/introducing-fido2-client-sdk-open-source | 9,957 | 추출/기술 선택·도입형 | case_0074 | 0/6 | FIDO2 클라이언트 SDK 오픈소스 소개 |
| ly/how-to-evaluate-ai-generated-images-1 | 16,708 | 제외/개념·튜토리얼 | - | 0/0 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/extracting-trending-keywords-from-openchat-messages | 14,017 | 추출/실험·활용기 | case_0079, case_0080, case_0081 | 2/20 | 오픈챗 메시지들로부터 트렌딩 키워드 추출하기 |
| ly/pd1-ai-hackathon-recap | 4,153 | 제외/회고·문화·행사 | - | 0/0 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 6,232 | 추출/실험·활용기 | case_0070, case_0071 | 0/14 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 및 서비스 상태 확인 도구 LINE Status 개발기 |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 19,601 | 추출/문제 해결형 | case_0075, case_0076, case_0077 | 0/28 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/japanese-search-kuromoji-to-sudachi | 15,395 | 추출/기술 선택·도입형 | case_0068, case_0069 | 0/19 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자가 좋아하는 과자는? |
| oliveyoung/2024-06-05_google-cloud-next-24-review | 3,796 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next '24 방문기 |
| oliveyoung/2024-08-11_type-and-type-system-with-typescript | 11,673 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 타입과 타입 시스템 |
| oliveyoung/2024-09-30_oy-feconf-2024 | 8,894 | 제외/회고·문화·행사 | - | 0/0 | 올리브영에서는 프론트엔드 개발자들이 이런 고민을 하는군요? |
| oliveyoung/2024-10-17_oy-delivery-mq | 4,642 | 추출/문제 해결형 | case_0050 | 0/12 | 올리브영 물류시스템에서는 데이터를 어떻게 주고 받을까? |
| oliveyoung/2024-12-16_Design-System-Token-Automation | 17,955 | 추출/실험·활용기 | case_0046 | 0/9 | 디자인 시스템 중 디자인 토큰을 여러 도구를 이용하여 자동화 하는 방법 |
| oliveyoung/2024-12-17_catalog-mongo-transaction-2 | 11,450 | 추출/문제 해결형 | case_0048, case_0049 | 0/19 | Spring Boot MongoDB 트랜잭션 도입 실전 가이드 |
| oliveyoung/2025-02-14_oy-global-mall-address | 4,978 | 추출/기술 선택·도입형 | case_0047 | 1/11 | 올리브영 글로벌몰 주소 자동완성 및 검증 솔루션 도입기 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 7,158 | 추출/문제 해결형 | case_0042 | 0/13 | Web Worker로 이미지 처리 최적화하기 |
| oliveyoung/2025-06-10_chaos | 7,289 | 추출/문제 해결형 | case_0041 | 0/11 | 버그가 아니라 장애를 잡아라!! QA와 카오스 엔지니어링의 만남 |
| toss/27752 | 5,980 | 추출/문제 해결형 | case_0008 | 0/9 | 드래그 앤 드롭은 사실 편한 UX가 아니다? |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | - | 0/0 | 오픈소스에 기여하고 토스에 합격한.ssul \| EP.4 모닥불 |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | - | 0/0 | 개발자 리더로서 성장당한 썰 \| EP.7 모닥불 |
| toss/toss-frontend-ai-docs | 2,869 | 추출/실험·활용기 | case_0009, case_0010 | 0/15 | 토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유 |
| toss/toss-people-3 | 7,801 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 문과생에서 토스 개발 리더까지 |
| toss/frontend-esbuild-hmr | 10,415 | 추출/문제 해결형 | case_0003 | 0/9 | ESBuild를 위한 HMR, 직접 만들기 |
| toss/frontend-apply-without-resume | 2,783 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드에 이력서 없이 리포지토리 링크로 지원하세요 (~5/31) |
| toss/toss-securities-gpu-mig | 13,794 | 추출/기술 선택·도입형 | case_0001 | 0/15 | GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기 |
| toss/tds-color-system-update | 13,423 | 추출/기술 선택·도입형 | case_0004, case_0005, case_0006, case_0007 | 0/30 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| toss/ads_dashboard_fe | 12,467 | 추출/기술 선택·도입형 | case_0002 | 0/14 | 전체 데이터를 브라우저에 두는 광고 대시보드 만들기 |
| woowahan/14484 | 5,518 | 제외/문제 해결형 | - | 0/0 | “일단 백로그에 넣어두고 여유 있을 때 보는 걸로 할까요?” : 백로그를 백로그로 두지 않는 법 |
| woowahan/14671 | 6,108 | 제외/회고·문화·행사 | - | 0/0 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/15398 | 10,772 | 추출/실험·활용기 | case_0021 | 0/11 | Java의 미래, Virtual Thread |
| woowahan/15541 | 6,445 | 제외/개념·튜토리얼 | - | 0/0 | 웹 접근성 준수를 통한 모두에게 배달되는 일상의 행복 |
| woowahan/17386 | 11,245 | 추출/실험·활용기 | case_0018, case_0019, case_0020 | 0/25 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/17911 | 4,799 | 추출/문제 해결형 | case_0017 | 0/13 | B마트 주문 유실을 없애보자: 네트워크 편 |
| woowahan/20763 | 8,615 | 추출/기술 선택·도입형 | case_0022, case_0023 | 0/29 | 이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기 |
| woowahan/21027 | 25,102 | 추출/기술 선택·도입형 | case_0016 | 0/12 | 실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법 |
| woowahan/24434 | 15,179 | 추출/실험·활용기 | case_0014, case_0015 | 0/20 | “함께 구매하면 좋은 상품” 추천 모델 고도화 |
| woowahan/24999 | 12,341 | 추출/문제 해결형 | case_0011, case_0012, case_0013 | 0/20 | WOOWACON 2025 미니게임 WOOWA POP! |
