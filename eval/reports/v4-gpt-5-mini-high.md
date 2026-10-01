# 추출 점검 리포트: v4-gpt-5-mini-high

- 모델: gpt-5-mini (high)
- 프롬프트 버전: 5bafd9ddcc5d
- 글 80편: 추출 62, 제외 18
- 항목 108개
- 토큰: 호출 159회, 입력 1,284,566 (캐시 489,472), 출력 1,792,006 (reasoning 1,639,360)
- 비용: $3.795 (편당 $0.0474), 전체 1,262편 추정 $59.9 / Batch $29.9

## 블로그별 추출 여부

| 블로그 | 추출 | 제외 | 항목 수 |
| --- | --- | --- | --- |
| d2 | 8 | 2 | 13 |
| kakao | 6 | 4 | 10 |
| kakaopay | 9 | 1 | 29 |
| kurly | 10 | 0 | 13 |
| ly | 8 | 2 | 14 |
| oliveyoung | 6 | 4 | 7 |
| toss | 6 | 4 | 8 |
| woowahan | 9 | 1 | 14 |

## 글 유형 × 추출 여부

| 글 유형 | 추출 | 제외 |
| --- | --- | --- |
| 개념·튜토리얼 | 0 | 4 |
| 기술 선택·도입형 | 26 | 0 |
| 문제 해결형 | 13 | 0 |
| 실험·활용기 | 21 | 0 |
| 회고·문화·행사 | 2 | 14 |

## 짧은 글 (평문 1,500자 미만) 8편

| 글 | 길이 | 결과 | 항목 | 분류 이유 |
| --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 추출/기술 선택·도입형 | 1 | NCrashlytics 발표는 Old Symbolicator의 문제점·한계 분석과 New Symbolicator의 알고리즘(심볼 맵 파일), SymbolFile CLI 및 업로드 워크플로, 저비용 고효율 서버 아키텍처, 품질·성능·리소스 비교 등 구체적인 설계·운영 근거와 적용 결과를 다루고 있어 타 팀의 설계·구현 판단에 실무적으로 참고할 수 있으므로 추출로 분류합니다. |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | 0 | NAVER ENGINEERING DAY에서 발표된 세미나 형태로 C++의 data race, 선후관계, basic thread safety, 표준 라이브러리의 스레드 안전성 및 mutex/atomic 사용법 등 개념과 API 설명 중심입니다. 특정 프로젝트의 문제 해결 과정, 도입 비교, 설정·적용 사례나 측정 결과 등 다른 팀의 설계·구현 판단에 바로 활용할 실무적 근거가 포함되어 있지 않아 제외합니다. |
| d2/8992409 | 1,342 | 추출/문제 해결형 | 1 | 과거 데이터 파이프라인의 문제를 해결하기 위해 Flow.er를 설계·개발한 구체적 사례(Proof of Concept, DBT·Airflow 역할, 구성요소, CI/CD, Manager DAG 개선, Partition Checker 등)가 포함되어 있습니다. 이러한 설계·운영 관련 구체적 내용은 다른 팀의 기술 선택·구현 판단에 실무적 참고가 됩니다. |
| d2/9290861 | 796 | 제외/회고·문화·행사 | 0 | NAVER Engineering Day에서 공개된 발표 세션 소개문으로, VictoriaMetrics 아키텍처와 목차(구성 요소·원리)를 개요 수준으로 안내하고 있음. 구체적인 설계 결정·수치·비교·적용 사례나 해결 과정 등 실무에 바로 참고할 기술적 근거가 포함되어 있지 않아 추출 대상이 아님. |
| kakao/624 | 787 | 제외/회고·문화·행사 | 0 | 발표 영상과 발표자 인터뷰를 소개하는 행사 안내/후기성 글입니다. 본문은 참여 동기·소감·향후 계획과 영상 링크 중심으로, 구체적인 기술적 구현·설정·워크플로우·문제 해결 과정·수치나 설계 근거 등 실무 적용 정보를 포함하고 있지 않아 기술 사례 데이터베이스로는 제외합니다. |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | 0 | 사내 간식 선호도 설문과 결과 공유를 다루는 문화/행사성 글입니다. 기술적 문제 해결 과정, 도입·선택 근거, 실무 적용 팁 등이 없어 기술 사례 데이터베이스에 포함할 실무 정보가 없습니다. |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | 0 | 인터뷰·경험담 형식으로 오픈소스 기여와 커리어·커뮤니티 이야기를 주로 다루며, 구체적인 구현·설정·문제 해결 과정이나 수치·설계 근거가 포함되어 있지 않습니다. 실무 설계 판단에 참고할 기술적 디테일이 부족하므로 제외합니다. |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | 0 | 리더십과 조직 성장에 관한 인터뷰/토크 콘텐츠로, 구체적인 기술적 실무 사례나 설계·도구 적용·문제 해결 과정이 포함되어 있지 않습니다. 따라서 기술적 설계 판단에 참고할 만한 내용이 없어 제외합니다. |

## 글당 항목 수 (제외 글 빼고)

| 항목 수 | 글 수 |
| --- | --- |
| 1 | 42 |
| 2 | 5 |
| 3 | 9 |
| 4 | 3 |
| 5 | 1 |
| 6 | 2 |

## 문제 유형 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 개발 생산성 | 58 | 54% |
| 모니터링·관측성 | 19 | 18% |
| 배포·CI/CD | 15 | 14% |
| 업무·운영 자동화 | 14 | 13% |
| 데이터 파이프라인 | 14 | 13% |
| 데이터 정합성·트랜잭션 | 12 | 11% |
| 트래픽 급증 대응 | 12 | 11% |
| 메시징·비동기 처리 | 11 | 10% |
| 비용 절감 | 11 | 10% |
| 장애 대응·복구 | 9 | 8% |
| 클라이언트 성능(웹·앱) | 7 | 6% |
| 인프라·컨테이너 | 7 | 6% |
| 인증·보안 | 6 | 6% |
| API 설계·외부 연동 | 5 | 5% |
| 캐싱 | 5 | 5% |
| DB 성능·쿼리 최적화 | 5 | 5% |
| 테스트 자동화 | 5 | 5% |
| DB 마이그레이션·샤딩 | 1 | 1% |
| MSA | 1 | 1% |
| 동시성·락 | 1 | 1% |

- 쏠림(30% 초과): 개발 생산성
- 한 번도 안 쓰인 분류 (0개): 없음

## 도메인 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 사내 플랫폼·개발 도구 | 60 | 56% |
| 커머스·주문·재고 | 25 | 23% |
| LLM·AI | 15 | 14% |
| 결제·금융 | 8 | 7% |
| 검색·추천 | 8 | 7% |
| 범용 | 7 | 6% |
| 배달·물류 | 6 | 6% |
| 콘텐츠·미디어 | 4 | 4% |
| 채팅·메시징 서비스 | 2 | 2% |
| 광고·마케팅 | 1 | 1% |

- 쏠림(30% 초과): 사내 플랫폼·개발 도구
- 한 번도 안 쓰인 분류 (0개): 없음

## 발췌 검증

- 채택한 시도 기준 발췌 1084개 중 탈락 16개 (원문 존재율 99%)
- 재시도한 글 17편

- `d2/3461887`: # 제목: App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics
- `d2/3461887`: # 제목: App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics
- `d2/3461887`: - 품질
- `d2/3461887`: - 성능
- `d2/6512234`: 다음과 같은 코드를 모든 쓰기 로직에 추가하려면 10년 넘은 서비스의 비즈니스 로직 전체에 걸쳐 수백, 수천 곳을 수정해야 합니다. 이는 휴먼 에러 발생 가능성 증대와 개발 기간 대폭 증가로 이어져 위험성이 높다고 판단해, 비즈니스 로직 코드 수정 없이 Oracle과 MySQL 양쪽으로 쓰기 작업을 수행하는 방법을 고민했습니다.
- `kakao/770`: 저희는 과제를 진행 중이었기에, 영향을 최소화하고자 하였습니다. 그래서 과제를 진행 중인 브랜치를 A 브랜치(base)로 두고, Vite 전환을 작업할 신규 브랜치로 B 브랜치를 생성하였습니다.
- `kakaopay/pallas-v2-log-platform`: Pod 수 | As-Is (Fluentd) | To-Be (OpenTelemetry) | 1,000개 이상 | 150개 |
- `kakaopay/pallas-v2-log-platform`: 단점 | IAM Role Anywhere 미지원 | Ruby 기반이라 AWS SDK Ruby에서 IAM Role Anywhere를 지원하지 않음 |
- `kakaopay/pallas-v2-log-platform`: 단점 | IAM Role Anywhere 미지원 | Ruby 기반이라 AWS SDK Ruby에서 IAM Role Anywhere를 지원하지 않음 |
- `kurly/cart-recommend-model-development`: 참고로 저희 팀에서는 머신러닝 학습 시 생성된 파일(모델, 사전 등)과 오프라인 지표는 mlflow를 통해서 관리하고 있습니다.
- `ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot`: NGINX 설정을 Ansible로 구성해 두고 Jenkins에서는 Ansible을 호출하도록 아래와 같이 구성했습니다.
- `ly/improving-kubernetes-relay-api-server-performance-with-informer`: 스레드를 다수 생성해서 작동 방식을 비동기적으로 바꿔 우회하는 방법을 써도 한 리소스를 계산하는 데 10초 정도가 걸렸습니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 처음에는 관련 키워드를 모두 블랙리스트로 구성해서 이와 일치하거나 부분 문자열로 포함하는 단어는 트렌딩 키워드로 추출되지 않도록 만들어 봤습니다. 그랬더니  ￮￮미처 예상치 못했던 단어들이, 예를 들어 오랜만에 경기가 열리는 지방 도시 이름이라던가 말이나 기수 또는 참가 팀 이름 등 미리 지정하는 게 사실상 불가능한 단어들이 걸러지지 못하고 추천 키워드로 추출됐습니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 페널티 가중치가 2 이상이면 가중치를 더 늘리더라도 대체로 순위가 유지되는 것을 관찰했습니다. 검토 결과 다양성이 충분히 확보되는 편이 바람직하다고 의견이 모여 페널티 가중치가 2 이상인 구간에서 α값을 결정했습니다.
- `toss/toss-securities-gpu-mig`: 이러한 이유로 저희는 GPU 가상화를 선택했으며, 그중에서도 MIG 기반 가상화가 저희 환경에 가장 적합한 해법이라고 판단했습니다.
- `woowahan/17386`: 서비스 토픽과 분석에 사용되는 토픽은 서로 다른 데이터 처리량과 리소스가 필요하기에 토픽과 서버를 분리하여 특성에 맞는 리소스를 사용하고 조정할 수 있도록 구성하였습니다.

## 기술 사전에 없는 이름 179종

- Jira (5)
- Android (3)
- iOS (3)
- Locust (3)
- LLM (3)
- Sudachi (3)
- Hubot (3)
- Git (3)
- 클로드 코드 (3)
- ESBuild (2)
- SWC (2)
- Figma (2)
- GitHub (2)
- Web Worker (2)
- Milvus (2)
- Netty (2)
- C++ (2)
- AWS S3 (2)
- Vite (2)
- Storybook (2)
- Rollup (2)
- Dokka (2)
- HDFS (2)
- Iceberg (2)
- Confluence (2)
- react-refresh (1)
- WebSocket (1)
- Token Studio (1)
- Style Dictionary (1)
- CSS (1)
- MIG (1)
- nvidia-device-plugin (1)
- dcgm-exporter (1)
- nvidia-smi (1)
- NVLink (1)
- H100 (1)
- H200 (1)
- WASM (1)
- Rust (1)
- Node2Vec (1)
- Transformer (1)
- Item2Vec (1)
- SASRec (1)
- Redis Stack (1)
- Atlas MongoDB (1)
- pgvector (1)
- JDK (1)
- Virtual Thread (1)
- Kotlin coroutine (1)
- LTE 라우터 (1)
- IPSEC (1)
- S2 Geometry (1)
- fastutil (1)
- AWS ALB (1)
- jstat (1)
- libevent (1)
- Spring Cloud (1)
- AWS Athena (1)
- v0 (1)
- Supabase (1)
- Vercel (1)
- MLA (1)
- MoE (1)
- JMH (1)
- Vector DB (1)
- JFR (1)
- async-profiler (1)
- jstack (1)
- Codex (1)
- PromQL (1)
- Claude API (1)
- IntelliJ (1)
- Reach (1)
- Vitest (1)
- AWS KMS (1)
- CloudTrail (1)
- OpenSearch Dashboards (1)
- Apache Lucene (1)
- Wallga (1)
- InfluxDB (1)
- GCP (1)
- Filebeat (1)
- Protocol Buffers (1)
- Parquet (1)
- HyperDX (1)
- Spinnaker (1)
- Clang-Tidy (1)
- DBT (1)
- 코파일럿 (1)
- datasource-proxy (1)
- Hive (1)
- react-window (1)
- Release Please Action (1)
- GitHub API (1)
- kotlin-dsl (1)
- vanniktech-maven-publish-plugin (1)
- JFrog Artifactory (1)
- Maven Central (1)
- GitHub Pages (1)
- Ruler (1)
- 네이버 POI 플랫폼 (1)
- XBU (1)
- CLOUS (1)
- Nexus (1)
- JuiceFS (1)
- JuiceFS CSI Driver (1)
- MinIO (1)
- FUSE (1)
- fio (1)
- ZSTD (1)
- FIDO2 (1)
- WebAuthn (1)
- CTAP (1)
- Xcode (1)
- iOS Secure Enclave (1)
- ARM TrustZone (1)
- Android StrongBox (1)
- Vector (1)
- Akamai (1)
- node_exporter (1)
- kube-state-metrics (1)
- Graphviz (1)
- Informer (1)
- client-go (1)
- kube-apiserver (1)
- etcd (1)
- MinHash (1)
- NPMI (1)
- MMR (1)
- Z-test (1)
- Shingling (1)
- Jaccard (1)
- hubot-conversation (1)
- Harbor (1)
- Ansible (1)
- Taskmaster (1)
- Webpack (1)
- esbuild (1)
- @vitejs/plugin-react (1)
- vite-plugin-babel (1)
- rollup-plugin-visualizer (1)
- MobX (1)
- Material-UI (1)
- react-csv (1)
- qs (1)
- dayjs (1)
- ForkTsCheckerWebpackPlugin (1)
- MariaDB (1)
- mysql-connector-j (1)
- AWS EC2 (1)
- jmap (1)
- MemoryAnalyzer (1)
- 구글 스프레드시트 (1)
- BigQuery (1)
- VueRouter (1)
- Swagger (1)
- Postman (1)
- MariaDB Connector/J (1)
- 행정안전부 도로명주소 조회 API (1)
- 행정안전부 좌표정보 API (1)
- 외부업체 주소정제 API (1)
- mitmproxy (1)
- OffscreenCanvas (1)
- BERT4Rec (1)
- Gradio (1)
- mlflow (1)
- Growthbook (1)
- PyTorch (1)
- Yarn (1)
- Jotai (1)
- Panda CSS (1)
- AWS ECR (1)
- AWS ECS (1)
- Tokens Studio For Figma (1)
- token-transformer (1)
- GitHub CLI (1)
- Spring Data MongoDB (1)
- EAI I/F (1)
- MQ (1)

## 버린 대안 106개 (항목 108개 중)

- `case_0002` 단일 토큰 수정(예: Blue 100만 수정): 한 색만 고쳐서는 팔레트의 다른 색과 다크모드까지 함께 고려해야 해서 확장성이 없었다.
- `case_0002` 단순 토큰 통합: 흩어진 소스 통합만으로는 디자이너가 제어·실험할 수 있는 시스템을 제공하기에 부족했다.
- `case_0003` 원본 데이터 그대로 사용: Figma/Token Studio 원본은 UI 표시용 이름·중첩 구조·포맷 불일치 문제가 있어 그대로 쓰기 어렵다.
- `case_0005` 클라우드 활용: 장기적·지속적 워크로드나 자체 클러스터 환경에서는 비용상 불리하고 규제·가용성 제약이 있어 채택하지 않음.
- `case_0005` 혼합 GPU 운영: 초기에는 유연하나 장기적으로 수요 편중으로 저용량 GPU가 유휴화되고 관리 복잡성이 증가하므로 채택에서 제외됨.
- `case_0005` MPS: 소프트웨어 방식의 공유는 격리와 관리가 어렵고 성능 간섭·운영 부담이 커서 하드웨어 기반인 MIG를 선택함.
- `case_0007` Virtual Scrolling: 한 번에 그리는 건 100행이고, 이 정도면 컬럼이 수십 개여도 DOM 부하가 병목이 아니라는 걸 확인했어요.
- `case_0007` IndexedDB 캐싱: 무효화 판단이 명확하지 않고 세션만으로도 요구를 충족해 과한 솔루션이었다.
- `case_0007` Worker 직접 API 호출: Worker에서 직접 호출하려면 공통 HTTP 클라이언트를 Worker 쪽에 중복 배치하거나 별도 경로를 만들어야 했다.
- `case_0007` 서버 API 스펙 확장: 정렬 키·순번 계산 등 서버에 하나씩 API를 추가하는 방식은 근본 원인을 해결하지 못한다.
- `case_0008` aria-roledescription: aria-roledescription 속성은 iOS에서 사용 불가하여 적용하지 않음.
- `case_0008` button disabled 속성: 기본 disabled 사용 시 Android에서 포커스가 상단으로 튈 수 있어 사용하지 않음.
- `case_0009` 코드 난독화: 그저 시간을 지연시킬 뿐이었습니다.
- `case_0009` 프로그레스바 기반 매크로 방지: 이 또한 무용지물이었습니다.
- `case_0009` CAPTCHA(이미지 선택): 매크로는 막았지만, 게임의 재미는 크게 반감됐습니다.
- `case_0011` Item2Vec: 동일 주문 기반 임베딩으로 대체재 편향 발생, 시퀀스 맥락 반영 불가
- `case_0011` 통합 그래프 임베딩: 셀러 타입(마트/편의점) 특성 차이로 통합 학습 시 품질 저하
- `case_0011` 고정 타깃 샘플링: 학습 시 동일 타깃만 사용하면 모델 일반화가 제한됨
- `case_0012` Pinecone: 새로운 fully-managed 벡터 검색 서비스 도입은 비용·관리 주체 이슈로 우선 검증 대상에서 제외했다.
- `case_0012` ANN (HNSW, IVFFlat): pre-filter로 좁혀진 런타임 후보군에 대해 미리 빌드한 ANN 인덱스를 재활용할 수 없어 부적합하다고 판단했다.
- `case_0012` post filter 방식: post-filter는 필터 후 남는 결과를 보장하지 못해 실서비스 요구를 만족시키기 어려웠다.
- `case_0014` 에그: 운영 비용(사용자 교육) 증가
- `case_0014` 5G 상품: 유선 대비 품질·속도·안정성 부족
- `case_0014` 동일 회선 사업자 이중화: 사업자 단일화 시 지역/전국 장애에 취약
- `case_0015` 캐시 레이어: 캐시 레이어 관련 비용 발생, 작업량이 많음
- `case_0015` hazelcast: 기능 과다 및 진입 장벽 우려
- `case_0015` chronicle-map: 기능 과다 및 진입 장벽 우려
- `case_0015` HPPC: 기능 면에서 큰 차이 없음
- `case_0015` trove: 기능 면에서 큰 차이 없음
- `case_0015` koloboke: 기능 면에서 큰 차이 없음
- `case_0023` Cursor: 초보자나 비개발자가 1시간 안에 사용법을 익히기엔 진입장벽이 높음
- `case_0023` Claude: 초보자나 비개발자가 1시간 안에 사용법을 익히기엔 진입장벽이 높음
- `case_0038` Parcel: Zero-config이나 복잡한 프로젝트에서 커스터마이징 한계로 리스크가 큼
- `case_0038` Rsbuild: 생태계·문서·지원 부족으로 실서비스 도입에 부담
- `case_0038` Webpack: 설정 복잡성·유지보수 부담으로 장기적으로 대안 검토
- `case_0040` Entity LifeCycle 콜백: PostLoad에서 복호화를 수행하면 1차 캐시가 변경되어 조회 시 불필요한 update 문이 발생했다.
- `case_0051` Elasticsearch / OpenSearch: 비용이 높고, 대용량 집계 쿼리가 느림
- `case_0051` Grafana Loki: 복잡한 쿼리 불가, 집계 기능이 약함
- `case_0052` Amazon Athena: 컬럼 수 제한
- `case_0053` Signoz: 테이블 구조 고정
- `case_0054` 검증 로직 별도 클래스: 검증 호출 누락 가능성
- `case_0059` reinterpret_cast (값 타입 퍼닝): 값 타입을 reinterpret_cast로 재해석하면 엄격한 앨리어싱 규칙을 위반하여 미정의 동작이 발생함
- `case_0059` union (타입 퍼닝): C++에서는 비활성 멤버를 읽는 것이 미정의 동작이므로 표준적으로 안전하지 않음
- `case_0059` std::bit_cast (포인터에 사용): 포인터 값만 복사하므로 역참조 시 엄격한 앨리어싱 위반과 const 우회가 발생할 수 있음
- `case_0064` ChainedTransactionManager / 분산 트랜잭션: 분산 트랜잭션이나 ChainedTransactionManager로 MySQL 쿼리를 트랜잭션에 포함시키지 않음
- `case_0064` 운영 트래픽 복제(HTTP 트래픽 복사 / 외부 Kafka 토픽 복제): 운영 시스템에 불필요한 중복 호출 부하 및 부작용을 유발할 위험
- `case_0064` OraclePagingQueryProvider: 다중 PK 페이징에서 비효율적이라 커스텀 QueryProvider로 대체
- `case_0065` @tanstack/react-virtual: 네이버 로그 시스템의 복잡한 표현 방식과 바닥 감지 신뢰성 문제 등으로 오픈소스 활용이 어려웠음
- `case_0065` react-window: div 기반 레이아웃으로 인해 스타일 적용과 동적 행 처리, colspan 등 표 기능에 제약이 있어 대체를 검토
- `case_0065` IndexDB: 브라우저 메모리 부담을 줄이기 위한 캐시 방안으로 검토했음
- `case_0065` 페이징: OOM 안전 범위를 확보하기 위한 페이징 적용을 검토했음
- `case_0065` TanStack Query ← React Query: 캐시된 페이지 수를 제한해 메모리 부담을 줄이는 방안으로 검토했음
- `case_0074` Alluxio: 일부 POSIX API 미지원으로 AI 오픈소스 호환성 문제 및 운영 부담
- `case_0074` GlusterFS: 직접 운영해야 하는 오픈소스로 운영 부담이 큼
- `case_0074` CephFS: 직접 운영해야 하는 오픈소스로 운영 부담이 큼
- `case_0074` Ceph-rbd: ReadWriteMany/ReadOnlyMany 미지원으로 다중 Pod 동시 접근 불가
- `case_0074` NFS: 확장성·HA 문제로 대규모 AI 워크로드에 제한적
- `case_0074` local-path: 노드 로컬 디스크 기반으로 동시 접근 불가 및 스케줄링 부담
- `case_0074` AWS EFS / Google Filestore: 비용이 크고 AiSuite는 온프레미스라 외부 클라우드 사용 불가
- `case_0074` DDN EXAScaler: 요구사항을 만족하지만 도입 비용이 커서 부분 도입으로 한정
- `case_0075` Kuromoji: 형태소 단위 분해 특성으로 상품명 복합어가 분해되어 검색 품질 저하
- `case_0075` mecab-ipadic-neologd: MeCab 기반 최신 사전은 연동 제약으로 적용 불가
- `case_0075` Elasticsearch: Elasticsearch 8.x로 업그레이드 불가(사내 플랫폼 지원 범위 문제)
- `case_0078` Spark Streaming(Structured Streaming): 마이크로배치 방식으로 이벤트 타임 기반 상태 제어와 정확히 한 번 처리, 최신성 판별을 동시에 만족하기 어렵다고 판단하여 도입하지 않음.
- `case_0078` 네이티브 쿠버네티스 방식: 모든 설정을 수동으로 구성해야 해 운영 번거로움이 크므로 오퍼레이터 방식으로 대체.
- `case_0078` Flink 이미지에 Hadoop 에코시스템 전체 설치: 이미지 크기 증가와 유지보수 비용 때문에 단일 uber 라이브러리로 대체했음.
- `case_0078` 비키드 윈도(non-keyed window): 초기에는 사용했으나 단일 태스크로 병목이 발생해 키 기반 윈도로 전환함.
- `case_0079` 비키드 윈도(non-keyed window): 단일 태스크로 동작해 처리량 증가 시 병목이 발생해 키 기반 윈도로 전환함.
- `case_0080` CoW (copy-on-write): 실시간 스트리밍 환경의 Flink에서는 MoR만 지원되어 CoW를 적용할 수 없어 선택하지 않음.
- `case_0080` 공격적인 min-input-files·delete-file-threshold 설정: 자주 병합되면서 HDFS NameNode·DataNode에 과도한 I/O 부하를 일으켜 완화가 필요했음.
- `case_0082` WebAuthn Level 3: Level 3의 Passkey 동기화 제어가 불가능해 비즈니스 요구와 충돌할 수 있어 채택하지 않음
- `case_0083` 직접 개발한 익스포터: 관리 허들
- `case_0083` Vector 공식 Helm 차트: 공식 차트에 프로젝트와 관련 없는 리소스가 있어 자체 Helm 차트로 대체
- `case_0083` Agent 방식: 에이전트 스펙 제한으로 대규모 요구에 부적합
- `case_0084` Python 클라이언트: Informer를 사용할 수 없어 Go로 전환
- `case_0084` Redis: 외부 캐시 도입 불필요
- `case_0085` 거리 기반 클러스터링: 복잡한 클러스터링 대신 단순 일치 방식 선택
- `case_0085` 전날(d-1) 비교 기준: d-1 기준은 Z값이 급격히 하락해 부적절
- `case_0091` MCP로 외부 시스템 직접 조회: 토큰 비용·속도 문제
- `case_0094` 메모리 증설: 임시방편
- `case_0094` Parcel: 커스텀 제한적
- `case_0094` Rsbuild: 생태계 작음
- `case_0095` nginx 라우팅 설정: 인프라팀 협조 없이 개발팀에서 적용 불가해 사용하지 않음
- `case_0095` 스케줄링 배치로 주기적 캐싱: 주기적 배치 대신 최소 공수로 인스턴스 내에서 해결하는 방향을 택함
- `case_0095` 직접 UI 개발 / 새로운 인스턴스 띄우기: 기존 시스템에 넣으면 DB 다운 시 로그인 불가, 새 인스턴스는 오버스펙이라 보류
- `case_0096` max-lifetime 증가: DB failover 시 빠른 slave 연결을 위해 max-lifetime을 작게 유지하고 있음
- `case_0097` nginx 설정: 인프라 상황상 nginx 설정으로 차단할 수 없음
- `case_0097` 호출 횟수 기반 동기화: 트래픽 변동으로 동기화 주기 예측이 어려워 대체
- `case_0097` 업무 시스템 RDBMS: 업무용 RDBMS에 종속되지 않도록 설계
- `case_0097` UI 직접 제작: 기능 전용 UI를 새로 만들거나 기존 시스템에 바로 넣기 어려움
- `case_0099` READ COMMITTED 격리수준: 격리수준을 낮출 경우 Phantom Read 이슈로 기존 비즈니스 로직에 영향이 우려됨
- `case_0099` 잠금 읽기 (LOCK IN SHARE MODE): 잠금 읽기는 락 경합 및 데드락 가능성 증가로 인한 부작용 때문에 채택하지 않음
- `case_0101` Chrome DevTools Overrides: 필드가 많을 경우 수동으로 하나씩 수정해야 해서 자동화·프로세스화에 부적합
- `case_0101` Charles/Fiddler: 필드가 많을 경우 수동으로 하나씩 수정해야 해서 자동화·프로세스화에 부적합
- `case_0101` 데이터 수정: API가 언제 null을 반환하는지 정의되어 있지 않아 실제 데이터 변경으로 null을 재현하기 어려움
- `case_0102` WebP 변환: 복잡한 이미지에서 압축 효율이 낮고, 품질을 낮추면 시각적 저하가 발생해 적용에 제약이 있었다.
- `case_0102` Canvas 리사이징(메인 스레드): 메인 스레드에서 Canvas로 처리하면 JS 블로킹과 클릭 이벤트 무시 등의 부작용이 발생했다.
- `case_0102` Shared Worker: 이미지 처리에 적합하지 않아 배제했다.
- `case_0102` Service Worker: 이미지 처리에 적합하지 않아 배제했다.
- `case_0104` 주문서 원시 사용: 모두 보완재로 가정한 학습은 성능이 나오지 않아서 버림
- `case_0104` 수작업 카테고리 매핑: 수작업으로 카테고리 간 보완재 관계를 설정하기 어려워서 버림
- `case_0106` WriteConcern MAJORITY: 성능 저하 우려
- `case_0106` ReadPreference PRIMARY: SECONDARY 노드가 유휴 상태로 남아 리소스 낭비
- `case_0107` SQS 지연 전송: 지연 시간이 짧으면 문제 지속(임시방편)
- `case_0107` Outbox 패턴: 설계·구현에 필요한 시간과 비용이 부담
- `case_0108` EAI I/F: 배치 기반으로 인한 지연과 단일 EAI 어댑터 장애 시 전체 통신 중단 문제가 있어 교체함

## 글 목록

| 글 | 길이 | 결과 | 항목 | 발췌 탈락 | 제목 |
| --- | --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 추출/기술 선택·도입형 | case_0073 | 4/11 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics |
| d2/4555524 | 18,452 | 추출/기술 선택·도입형 | case_0074 | 0/19 | AI 플랫폼을 위한 스토리지 JuiceFS 도입기 |
| d2/8366976 | 3,331 | 추출/문제 해결형 | case_0069, case_0070, case_0071, case_0072 | 0/24 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/3814947 | 16,662 | 추출/실험·활용기 | case_0066, case_0067, case_0068 | 0/26 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | - | 0/0 | Thread-safety in C++ |
| d2/1450243 | 15,218 | 추출/실험·활용기 | case_0065 | 0/16 | 윈도잉(windowing) 기법을 적용한 고성능 표 컴포넌트 개발기 |
| d2/8992409 | 1,342 | 추출/문제 해결형 | case_0060 | 0/9 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| d2/6512234 | 22,022 | 추출/기술 선택·도입형 | case_0064 | 1/17 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/1155434 | 9,048 | 추출/실험·활용기 | case_0059 | 0/11 | C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가 |
| d2/9290861 | 796 | 제외/회고·문화·행사 | - | 0/0 | Inside VictoriaMetrics |
| kakao/601 | 3,137 | 제외/회고·문화·행사 | - | 0/0 | 제3회 Kakao Tech Meet 후기 - 불확정성에서 감동까지 |
| kakao/624 | 787 | 제외/회고·문화·행사 | - | 0/0 | 카카오의 스팸 메일 대응 전략: 문자열 변형 CASE STUDY / 제6회 Kakao Tech Meet |
| kakao/761 | 3,645 | 제외/회고·문화·행사 | - | 0/0 | 실패를 장려하는 실험적 문화 |
| kakao/762 | 13,811 | 추출/실험·활용기 | case_0031 | 0/11 | 생산성 혁신의 실험: AI 마일리지 프로그램 |
| kakao/770 | 16,500 | 추출/기술 선택·도입형 | case_0038 | 1/14 | 5년 된 프로젝트의 빌드 도구를 교체하며 얻은 것들 |
| kakao/784 | 8,710 | 추출/실험·활용기 | case_0023 | 0/13 | 단 1시간 만에 99개의 MVP가? AI와 함께한 1K: 바이브코딩전 생생 후기 |
| kakao/785 | 4,597 | 추출/회고·문화·행사 | case_0025, case_0026, case_0027, case_0028 | 0/31 | if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며 |
| kakao/804 | 3,760 | 추출/기술 선택·도입형 | case_0024 | 0/12 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/822 | 20,047 | 추출/실험·활용기 | case_0029, case_0030 | 0/20 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakao/835 | 12,198 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 둘째 날, 기술 세션 소개 |
| kakaopay/slack-bot-improving-operational-efficiency-2 | 5,044 | 추출/기술 선택·도입형 | case_0058 | 0/12 | 카카오페이 배포 효율화 1년 회고: 자동화 도입과 팀 생산성 향상 |
| kakaopay/tech-strategy-tpm | 9,673 | 추출/회고·문화·행사 | case_0061, case_0062, case_0063 | 0/24 | 카카오페이 TPM은 어떤 일을 하나요? |
| kakaopay/katfun-joy-kotlin | 14,709 | 추출/실험·활용기 | case_0054, case_0055, case_0056, case_0057 | 0/30 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kakaopay/ifkakao2024-devrel | 10,598 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스 준비 맛보기 |
| kakaopay/perftest_zone | 4,708 | 추출/기술 선택·도입형 | case_0047 | 0/12 | 카카오페이 성능 테스트 존을 소개합니다. |
| kakaopay/kakaopaysec-wecan | 8,650 | 추출/기술 선택·도입형 | case_0042, case_0043, case_0044, case_0045, case_0046 | 0/26 | We Can Do Better: 개발자 플랫폼 효율화 이야기 |
| kakaopay/kakaopayins-opensearch-analyzer | 10,157 | 추출/실험·활용기 | case_0041 | 0/11 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/kakaopayins-envelope-encryption | 18,389 | 추출/기술 선택·도입형 | case_0039, case_0040 | 0/16 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/pallas-v2-log-platform | 25,659 | 추출/기술 선택·도입형 | case_0048, case_0049, case_0050, case_0051, case_0052, case_0053 | 3/46 | 일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트 |
| kakaopay/kakaopayins-fe-common-component | 7,059 | 추출/기술 선택·도입형 | case_0032, case_0033, case_0034, case_0035, case_0036, case_0037 | 0/32 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kurly/cart-recommend-model-development | 9,206 | 추출/실험·활용기 | case_0104 | 1/14 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 1부 |
| kurly/commit-mvcc-set-autocommit | 16,463 | 추출/문제 해결형 | case_0099 | 0/13 | 데이터가 있었는데요, 아니 없어요 |
| kurly/deliveryproductteam-culture-1 | 4,454 | 추출/문제 해결형 | case_0098 | 0/11 | 딜리버리 프로덕트 개발팀의 개발문화 - 로그 & 알람편 |
| kurly/connection-leak | 6,791 | 추출/문제 해결형 | case_0096 | 0/10 | 99%가 모른다는 DB Connection 누수 문제 |
| kurly/refine-address-internalization-2 | 4,312 | 추출/문제 해결형 | case_0100 | 0/12 | 주소정제 서비스 내재화 - 2화 ( 그럴싸한 계획 ) |
| kurly/access-block-1 | 5,663 | 추출/문제 해결형 | case_0095 | 0/15 | nginx 설정 없이 우아하게 서비스 점검하기 (上) |
| kurly/access-block-2 | 8,383 | 추출/기술 선택·도입형 | case_0097 | 0/16 | nginx 설정 없이 우아하게 서비스 점검하기 (下) |
| kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0 | 13,290 | 추출/기술 선택·도입형 | case_0094 | 0/15 | 빌드가 터졌다: 5년 된 CMS 프로젝트의 Webpack4 → Vite 전환 |
| kurly/tech-spec-adoption-with-ai-automation | 8,164 | 추출/기술 선택·도입형 | case_0089, case_0090 | 0/15 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| kurly/claude-code-redesign-my-day | 7,389 | 추출/실험·활용기 | case_0091, case_0092, case_0093 | 0/24 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| ly/managing-multi-cdn-logs-traffics-with-vector | 16,695 | 추출/실험·활용기 | case_0083 | 0/14 | Vector를 활용해 멀티 CDN 로그 및 트래픽 관리하기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 18,813 | 추출/실험·활용기 | case_0086, case_0087, case_0088 | 1/27 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/improving-kubernetes-relay-api-server-performance-with-informer | 12,361 | 추출/실험·활용기 | case_0084 | 1/14 | Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기 |
| ly/introducing-fido2-client-sdk-open-source | 9,957 | 추출/실험·활용기 | case_0082 | 0/12 | FIDO2 클라이언트 SDK 오픈소스 소개 |
| ly/how-to-evaluate-ai-generated-images-1 | 16,708 | 제외/개념·튜토리얼 | - | 0/0 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/extracting-trending-keywords-from-openchat-messages | 14,017 | 추출/실험·활용기 | case_0085 | 2/28 | 오픈챗 메시지들로부터 트렌딩 키워드 추출하기 |
| ly/pd1-ai-hackathon-recap | 4,153 | 제외/회고·문화·행사 | - | 0/0 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 6,232 | 추출/기술 선택·도입형 | case_0081 | 0/12 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 및 서비스 상태 확인 도구 LINE Status 개발기 |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 19,601 | 추출/기술 선택·도입형 | case_0078, case_0079, case_0080 | 0/35 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/japanese-search-kuromoji-to-sudachi | 15,395 | 추출/기술 선택·도입형 | case_0075, case_0076, case_0077 | 0/22 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자가 좋아하는 과자는? |
| oliveyoung/2024-06-05_google-cloud-next-24-review | 3,796 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next '24 방문기 |
| oliveyoung/2024-08-11_type-and-type-system-with-typescript | 11,673 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 타입과 타입 시스템 |
| oliveyoung/2024-09-30_oy-feconf-2024 | 8,894 | 제외/회고·문화·행사 | - | 0/0 | 올리브영에서는 프론트엔드 개발자들이 이런 고민을 하는군요? |
| oliveyoung/2024-10-17_oy-delivery-mq | 4,642 | 추출/기술 선택·도입형 | case_0108 | 0/12 | 올리브영 물류시스템에서는 데이터를 어떻게 주고 받을까? |
| oliveyoung/2024-12-16_Design-System-Token-Automation | 17,955 | 추출/실험·활용기 | case_0105 | 0/10 | 디자인 시스템 중 디자인 토큰을 여러 도구를 이용하여 자동화 하는 방법 |
| oliveyoung/2024-12-17_catalog-mongo-transaction-2 | 11,450 | 추출/문제 해결형 | case_0106, case_0107 | 0/17 | Spring Boot MongoDB 트랜잭션 도입 실전 가이드 |
| oliveyoung/2025-02-14_oy-global-mall-address | 4,978 | 추출/기술 선택·도입형 | case_0103 | 0/12 | 올리브영 글로벌몰 주소 자동완성 및 검증 솔루션 도입기 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 7,158 | 추출/문제 해결형 | case_0102 | 0/13 | Web Worker로 이미지 처리 최적화하기 |
| oliveyoung/2025-06-10_chaos | 7,289 | 추출/실험·활용기 | case_0101 | 0/13 | 버그가 아니라 장애를 잡아라!! QA와 카오스 엔지니어링의 만남 |
| toss/27752 | 5,980 | 추출/문제 해결형 | case_0008 | 0/14 | 드래그 앤 드롭은 사실 편한 UX가 아니다? |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | - | 0/0 | 오픈소스에 기여하고 토스에 합격한.ssul \| EP.4 모닥불 |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | - | 0/0 | 개발자 리더로서 성장당한 썰 \| EP.7 모닥불 |
| toss/toss-frontend-ai-docs | 2,869 | 추출/기술 선택·도입형 | case_0006 | 0/9 | 토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유 |
| toss/toss-people-3 | 7,801 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 문과생에서 토스 개발 리더까지 |
| toss/frontend-esbuild-hmr | 10,415 | 추출/실험·활용기 | case_0001 | 0/11 | ESBuild를 위한 HMR, 직접 만들기 |
| toss/frontend-apply-without-resume | 2,783 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드에 이력서 없이 리포지토리 링크로 지원하세요 (~5/31) |
| toss/toss-securities-gpu-mig | 13,794 | 추출/기술 선택·도입형 | case_0005 | 1/15 | GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기 |
| toss/tds-color-system-update | 13,423 | 추출/기술 선택·도입형 | case_0002, case_0003, case_0004 | 0/30 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| toss/ads_dashboard_fe | 12,467 | 추출/기술 선택·도입형 | case_0007 | 0/17 | 전체 데이터를 브라우저에 두는 광고 대시보드 만들기 |
| woowahan/14484 | 5,518 | 추출/문제 해결형 | case_0019 | 0/12 | “일단 백로그에 넣어두고 여유 있을 때 보는 걸로 할까요?” : 백로그를 백로그로 두지 않는 법 |
| woowahan/14671 | 6,108 | 추출/실험·활용기 | case_0020, case_0021, case_0022 | 0/25 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/15398 | 10,772 | 추출/실험·활용기 | case_0013 | 0/12 | Java의 미래, Virtual Thread |
| woowahan/15541 | 6,445 | 제외/개념·튜토리얼 | - | 0/0 | 웹 접근성 준수를 통한 모두에게 배달되는 일상의 행복 |
| woowahan/17386 | 11,245 | 추출/실험·활용기 | case_0016, case_0017, case_0018 | 1/31 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/17911 | 4,799 | 추출/기술 선택·도입형 | case_0014 | 0/15 | B마트 주문 유실을 없애보자: 네트워크 편 |
| woowahan/20763 | 8,615 | 추출/기술 선택·도입형 | case_0015 | 0/18 | 이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기 |
| woowahan/21027 | 25,102 | 추출/기술 선택·도입형 | case_0012 | 0/13 | 실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법 |
| woowahan/24434 | 15,179 | 추출/문제 해결형 | case_0011 | 0/14 | “함께 구매하면 좋은 상품” 추천 모델 고도화 |
| woowahan/24999 | 12,341 | 추출/문제 해결형 | case_0009, case_0010 | 0/19 | WOOWACON 2025 미니게임 WOOWA POP! |
