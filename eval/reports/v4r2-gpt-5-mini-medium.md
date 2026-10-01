# 추출 점검 리포트: v4r2-gpt-5-mini-medium

- 모델: gpt-5-mini (medium)
- 프롬프트 버전: 5bafd9ddcc5d
- 글 80편: 추출 61, 제외 19
- 항목 82개
- 토큰: 호출 156회, 입력 1,255,686 (캐시 996,480), 출력 484,058 (reasoning 355,904)
- 비용: $1.058 (편당 $0.0132), 전체 1,262편 추정 $16.7 / Batch $8.3

## 블로그별 추출 여부

| 블로그 | 추출 | 제외 | 항목 수 |
| --- | --- | --- | --- |
| d2 | 7 | 3 | 18 |
| kakao | 6 | 4 | 7 |
| kakaopay | 8 | 2 | 10 |
| kurly | 10 | 0 | 12 |
| ly | 9 | 1 | 10 |
| oliveyoung | 6 | 4 | 7 |
| toss | 6 | 4 | 6 |
| woowahan | 9 | 1 | 12 |

## 글 유형 × 추출 여부

| 글 유형 | 추출 | 제외 |
| --- | --- | --- |
| 개념·튜토리얼 | 1 | 4 |
| 기술 선택·도입형 | 27 | 0 |
| 문제 해결형 | 10 | 0 |
| 실험·활용기 | 21 | 0 |
| 회고·문화·행사 | 2 | 15 |

## 짧은 글 (평문 1,500자 미만) 8편

| 글 | 길이 | 결과 | 항목 | 분류 이유 |
| --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | 0 | NAVER ENGINEERING DAY 세션 공개 안내 글로 발표에서 다룰 주제 목록을 소개하고 있으나, 본문에 구체적인 설계 결정, 성능 수치, 구현·적용 경험이나 문제 해결 과정 등 다른 팀이 설계·구현 판단에 참고할 수 있는 실무적 기술 근거가 제시되어 있지 않음. |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | 0 | C++ 동시성(데이터 레이스, happens‑before, basic thread safety 등) 개념과 표준 라이브러리 보장, 예시를 정리한 발표 자료 중심의 교육/개념 설명 글입니다. 조직의 실제 도입 사례, 구체적 설계·구현 결정, 성능 수치나 문제 해결 과정(설정·워크플로·해결책)이 제시되어 다른 팀의 설계 판단에 직접 참고할 실무 근거가 충분치 않습니다. |
| d2/8992409 | 1,342 | 추출/기술 선택·도입형 | 1 | 과거 파이프라인 문제를 해결하기 위해 DBT·Airflow 기반의 on-demand 데이터 계보 파이프라인(Flow.er)을 설계·개발한 사례를 다룸. PoC, 구성요소, DBT와 Airflow의 역할, 개인 인스턴스·모델 관리 페이지·CI/CD, Manager DAG 개선, Partition Checker 등 구체적 구현·운영 컴포넌트와 확장 방안을 포함하고 있어 다른 팀의 설계·구현 판단에 참고 가능한 실무 정보가 있음. |
| d2/9290861 | 796 | 제외/개념·튜토리얼 | 0 | 발표 세션 개요(아키텍처 개관 및 컴포넌트 설명)를 소개하는 글로, 특정 팀의 적용 사례·문제 해결 과정·정량적 근거나 구체적 설계 결정(설정·워크플로·해결 방법)이 포함되어 있지 않음. 발표 주제는 개념·구조 설명 위주여서 설계 판단에 바로 참고 가능한 실무적 세부 정보가 부족함. |
| kakao/624 | 787 | 제외/회고·문화·행사 | 0 | 발표 인터뷰 및 행사 소개 중심의 내용으로, 구체적인 기술 적용 방식(설정·워크플로우), 문제 해결 과정, 비교·성능 수치 등 실무 판단에 활용할 수 있는 기술적 세부 정보가 포함되어 있지 않음. |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | 0 | 사내 간식 설문 결과를 공유하는 조직 문화/회고성 글입니다. 기술적 문제 해결 사례나 도입 근거, 실무 적용 팁 등 설계 판단에 참고할 기술적 내용이 포함되어 있지 않습니다. |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | 0 | 인터뷰/경험담 형식의 영상 소개 글로, 오픈소스 기여 경험과 채용 사례·커뮤니티 중요성 등을 다룸. 라이브러리 명과 기여 동기·성장 이야기는 있으나 구체적인 설계 결정·적용 방법(설정·워크플로·문제와 해결)이나 수치·비교 같은 실무적 근거가 없어 기술 사례 데이터베이스에 활용할 실무적 내용은 부족함. |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | 0 | 토스 프론트엔드 리더의 성장 경험과 조직·리더십에 관한 인터뷰/회고성 콘텐츠로, 구체적인 기술 도입·구현·문제 해결이나 실무 적용 팁이 포함되어 있지 않아 기술 사례 데이터베이스에 참고할 실무 정보가 아님. |

## 글당 항목 수 (제외 글 빼고)

| 항목 수 | 글 수 |
| --- | --- |
| 1 | 51 |
| 2 | 4 |
| 3 | 4 |
| 4 | 1 |
| 7 | 1 |

## 문제 유형 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 개발 생산성 | 40 | 49% |
| 모니터링·관측성 | 17 | 21% |
| 데이터 정합성·트랜잭션 | 15 | 18% |
| 데이터 파이프라인 | 11 | 13% |
| 비용 절감 | 10 | 12% |
| 메시징·비동기 처리 | 10 | 12% |
| 트래픽 급증 대응 | 9 | 11% |
| 배포·CI/CD | 9 | 11% |
| 장애 대응·복구 | 9 | 11% |
| 업무·운영 자동화 | 8 | 10% |
| DB 성능·쿼리 최적화 | 6 | 7% |
| 인프라·컨테이너 | 5 | 6% |
| 클라이언트 성능(웹·앱) | 5 | 6% |
| 테스트 자동화 | 5 | 6% |
| 캐싱 | 5 | 6% |
| 인증·보안 | 5 | 6% |
| 동시성·락 | 4 | 5% |
| DB 마이그레이션·샤딩 | 2 | 2% |
| API 설계·외부 연동 | 2 | 2% |
| MSA | 1 | 1% |

- 쏠림(30% 초과): 개발 생산성
- 한 번도 안 쓰인 분류 (0개): 없음

## 도메인 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 사내 플랫폼·개발 도구 | 42 | 51% |
| 커머스·주문·재고 | 23 | 28% |
| LLM·AI | 11 | 13% |
| 범용 | 9 | 11% |
| 검색·추천 | 8 | 10% |
| 배달·물류 | 4 | 5% |
| 결제·금융 | 2 | 2% |
| 채팅·메시징 서비스 | 2 | 2% |
| 콘텐츠·미디어 | 2 | 2% |
| 광고·마케팅 | 1 | 1% |

- 쏠림(30% 초과): 사내 플랫폼·개발 도구
- 한 번도 안 쓰인 분류 (0개): 없음

## 발췌 검증

- 채택한 시도 기준 발췌 852개 중 탈락 14개 (원문 존재율 98%)
- 재시도한 글 15편

- `d2/6512234`: INSERT나 UPDATE를 배치로 실행할 때, 여러 개의 쿼리를 하나의 쿼리(INSERT INTO ... VALUES (...), (...), (...))로 묶어서 보냅니다. 대량 데이터 삽입 시 성능이 수십 배 차이 날 수 있습니다.
- `kakao/770`: 저희는 과제를 진행 중이었기에, 영향을 최소화하고자 하였습니다. 그래서 과제를 진행 중인 브랜치를 A 브랜치(base)로 두고, Vite 전환을 작업할 신규 브랜치로 B 브랜치를 생성하였습니다.
- `kakaopay/kakaopayins-envelope-encryption`: 암호화 모듈의 의존 라이브러리 대부분이 초창기 버전에 머물러 있었습니다. 최근 애플리케이션들이 최신 버전으로 업그레이드하면서 애플리케이션과 암호화 모듈이 가지고 있는 라이브러리들의 호환성 문제로 AEM(Application Error Monitoring)이 울리는 가슴 아픈 사례들이 있었습니다.
- `kurly/cart-recommend-model-development`: 이때 검증셋 대해 HR과 MRR 계산 시 GPU OOM 에러가 발생할 수 있습니다. 따라서 아래와 같은 함수를 통해서 추론 결과를 전처리한 후 오프라인 지표를 계산하면 OOM 에러를 피할 수 있습니다.
- `kurly/cart-recommend-model-development`: 참고로 저희 팀에서는 머신러닝 학습 시 생성된 파일(모델, 사전 등)과 오프라인 지표는 mlflow를 통해서 관리하고 있습니다.
- `kurly/refine-address-internalization-2`: 제 기억에 이 때 까지는 외부 업체와의 계약 종료라는 목표는 뭔가 멀게만 느껴지는 목표였고, 일단 외부업체 api 호출 비용이라도 가능한 최소한으로 줄여보자는 목표로 계획을 세웠습니다.
- `ly/improving-kubernetes-relay-api-server-performance-with-informer`: 스레드를 다수 생성해서 작동 방식을 비동기적으로 바꿔 우회하는 방법을 써도 한 리소스를 계산하는 데 10초 정도가 걸렸습니다.
- `ly/improving-kubernetes-relay-api-server-performance-with-informer`: Go 클라이언트를 사용해 로컬 캐시를 굉장히 쉽게 구현할 수 있고, Redis 등을 사용해 억지로 etcd에 대한 로컬 캐시를 유지할 필요가 없습니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 그랬더니 미처 예상치 못했던 단어들이, 예를 들어 오랜만에 경기가 열리는 지방 도시 이름이라던가 말이나 기수 또는 참가 팀 이름 등 미리 지정하는 게 사실상 불가능한 단어들이 걸러지지 못하고 추천 키워드로 추출됐습니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 검토 결과 다양성이 충분히 확보되는 편이 바람직하다고 의견이 모여 페널티 가중치가 2 이상인 구간에서 α값을 결정했습니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 참고로 모든 데이터 분석에는 공개된 오픈챗 메시지만 이용됩니다.
- `ly/japanese-search-kuromoji-to-sudachi`: 카탈로그 인덱스는 약 1억 건 규모로 상대적으로 작고, 카탈로그명은 정제된 데이터이기 때문에 토큰 수 증가 폭을 예측할 수 있습니다.
- `toss/ads_dashboard_fe`: 하지만 저희는 100건 단위 페이지네이션을 씁니다. 한 번에 그리는 건 100행이고, 이 정도면 컬럼이 수십 개여도 DOM 부하가 병목이 아니라는 걸 확인했어요.
- `woowahan/20763`: 단점
– 캐시 레이어 관련 비용 발생
– 작업량이 많음

## 기술 사전에 없는 이름 183종

- Jira (6)
- Locust (3)
- Figma (2)
- GitHub (2)
- SWC (2)
- Web Worker (2)
- Transformer (2)
- Milvus (2)
- C++ (2)
- Dokka (2)
- LLM (2)
- datasource-proxy (2)
- MySQL Connector/J (2)
- HDFS (2)
- ZSTD (2)
- Confluence (2)
- Sudachi (2)
- Vector (2)
- Webpack (2)
- Vite (2)
- esbuild (2)
- Rollup (2)
- Babel (2)
- Storybook (2)
- Netty (2)
- Wallga (2)
- MIG (1)
- MPS (1)
- nvidia-device-plugin (1)
- dcgm-exporter (1)
- nvidia-smi (1)
- H100 (1)
- A100 (1)
- A40 (1)
- NVLink (1)
- Style Dictionary (1)
- Token Studio (1)
- CSS (1)
- ESBuild (1)
- react-refresh (1)
- WebSocket (1)
- Item2Vec (1)
- Node2Vec (1)
- SASRec (1)
- Redis Stack (1)
- pgvector (1)
- Spinnaker (1)
- Clang-Tidy (1)
- DBT (1)
- Flow.er (1)
- react-window (1)
- Big Table (1)
- Release Please Action (1)
- JFrog Artifactory (1)
- Maven Central (1)
- GitHub Pages (1)
- Ruler (1)
- 네이버 POI 플랫폼 (1)
- XBU (1)
- CLOUS (1)
- Nexus (1)
- Hive (1)
- JuiceFS (1)
- JuiceFS CSI Driver (1)
- nubes (1)
- MinIO (1)
- Kubeflow (1)
- Iceberg (1)
- Flink Kubernetes Operator (1)
- CLIP (1)
- Inception (1)
- DINO (1)
- ViT (1)
- VGG (1)
- FlanT5 (1)
- LAION (1)
- FID (1)
- IS (1)
- LPIPS (1)
- Aesthetic Score (1)
- CLIPIQA (1)
- Q-ALIGN (1)
- HPS v2 (1)
- Pick-a-Pic (1)
- Kuromoji (1)
- ICU (1)
- WebAuthn (1)
- FIDO2 (1)
- Android (1)
- iOS (1)
- Xcode (1)
- Apache-2.0 (1)
- Secure Enclave (1)
- ARM TrustZone (1)
- Android StrongBox (1)
- Hubot (1)
- Ansible (1)
- Harbor (1)
- hubot-conversation (1)
- node_exporter (1)
- kube-state-metrics (1)
- Notion (1)
- client-go (1)
- Informer (1)
- Python Kubernetes client (1)
- kubectl (1)
- etcd (1)
- MobX (1)
- Material-UI (1)
- Tailwind CSS (1)
- @vitejs/plugin-react (1)
- vite-plugin-babel (1)
- rollup-plugin-visualizer (1)
- qs (1)
- react-csv (1)
- dayjs (1)
- ForkTsCheckerWebpackPlugin (1)
- BigQuery (1)
- Google Sheets (1)
- Swagger (1)
- Postman (1)
- WebView (1)
- Taskmaster (1)
- MemoryAnalyzer (1)
- Eclipse MAT (1)
- AWS EC2 (1)
- jmap (1)
- 행정안전부 도로명주소 API (1)
- 행정안전부 좌표정보 API (1)
- 외부업체 주소정제 (1)
- MariaDB Connector/J (1)
- InnoDB (1)
- mitmproxy (1)
- OffscreenCanvas (1)
- BERT4Rec (1)
- gradio (1)
- growthbook (1)
- mlflow (1)
- Tokens Studio for Figma (1)
- token-transformer (1)
- Panda CSS (1)
- Yarn (1)
- Jotai (1)
- AWS ECR (1)
- AWS ECS (1)
- AWS S3 (1)
- IPsec (1)
- LTE 라우터 (1)
- Spring Cloud (1)
- AWS Athena (1)
- S2 Geometry (1)
- fastutil (1)
- AWS ALB (1)
- WASM (1)
- Rust (1)
- Virtual Thread (1)
- Project Loom (1)
- 스프레드시트 (1)
- 배민앱 (1)
- Canva AI 이미지 생성기 (1)
- Kanana-2 (1)
- MLA (1)
- MoE (1)
- JMH (1)
- Codex (1)
- v0 (1)
- Supabase (1)
- Vercel (1)
- IntelliJ (1)
- Claude API (1)
- Reach (1)
- Vitest (1)
- OpenSearch Dashboards (1)
- Apache Lucene (1)
- HyperDX (1)
- Parquet (1)
- Filebeat (1)
- Amazon Athena (1)
- LZ4 (1)
- AWS KMS (1)
- CloudTrail (1)
- InfluxDB (1)
- GCP (1)

## 버린 대안 94개 (항목 82개 중)

- `case_0001` 클라우드: 장기적 지속 워크로드나 컴플라이언스 환경에서 비용·제약 문제로 적합하지 않음
- `case_0001` 혼합 GPU 운영: 운영 복잡성·수요 편중으로 장기적 비효율 우려
- `case_0001` MPS: 격리성과 운영 관점에서 리스크가 커서 선택하지 않음
- `case_0002` 부분적인 팔레트 수동 보정: 부분만 고치면 다른 색들까지 함께 고려해야 해서 실용적이지 않음
- `case_0002` 플랫폼별 개별 다크모드 커스텀: 디자이너별로 다크모드를 따로 커스텀하면 토큰 관리 분산이 심화됨
- `case_0004` IndexedDB 캐싱: 캐시 무효화 규칙이 명확하지 않고, 요구 대비 과다하며 버전·마이그레이션 비용 등 부수 비용이 있어 보류함.
- `case_0004` Worker 직접 API 호출: 공통 HTTP 클라이언트(인증·에러 처리·재시도)를 Worker 쪽에 중복하거나 별도 경로를 만들면 관리 복잡도가 증가함.
- `case_0005` 문서를 더 잘 써서 방문하게 하기: 문서가 경로의존성을 가진 생산자 관점 구조라는 점을 해결하지 못한다고 보고 대안으로 채택하지 않음
- `case_0006` aria-roledescription: iPhone이 aria-roledescription(ARIA 1.3)을 지원하지 않아 의존할 수 없음
- `case_0006` button disabled 속성: Android에서 disabled 사용 시 포커스가 상단으로 튀는 문제로 대체 접근 방식(포커스 이동) 선택
- `case_0006` async onClick 상태 업데이트: Android에서 비동기 onClick 사용 시 체크박스 상태를 두 번 읽어주는 문제 발생
- `case_0008` Pinecone: 사내에 도입되어 있지 않고 관리 주체·비용 계약 이슈로 우선순위에서 제외하고, 먼저 사내에 도입된 OSS/서비스로 검증하기로 했음.
- `case_0008` ANN 알고리즘 (HNSW, IVFFlat 등): pre-filter로 좁혀진 후보군에 대응하는 미리 빌드된 인덱스가 없기 때문에 ANN을 사용할 수 없음(우리 시나리오에서는 Exact-KNN 동작이 선택됨).
- `case_0008` Milvus: 2차 성능 검증 대상으로 최종 후보에 포함되지 않음.
- `case_0008` Redis Stack: 2차 성능 검증 대상으로 최종 후보에 포함되지 않음.
- `case_0011` reinterpret_cast: 값 타입 퍼닝에 reinterpret_cast를 쓰면 엄격한 앨리어싱 규칙 위반으로 UB가 발생한다.
- `case_0011` union: C에서는 허용되지만 C++에서는 비활성 멤버 읽기가 UB라 표준적으로 사용할 수 없다.
- `case_0013` react-window: div 기반 레이아웃으로 표 고유 기능과 스타일 적용에 제약이 있고 동적 행 처리·헤더 동작 등에서 한계가 있어 자체 구현을 선택함.
- `case_0013` @tanstack/react-virtual: 네이버 로그 시스템의 복잡한 표현 방식과 향후 기획 대응을 위해 오픈소스만으로 대응하기 어렵다고 판단하여 도입을 포기함.
- `case_0021` ChainedTransactionManager / 분산 트랜잭션: 이중 쓰기를 구현하는 시점에는 Oracle과 MySQL 간 데이터 정합성이 대부분 맞지 않습니다.
- `case_0022` 분산 트랜잭션: 이중 쓰기를 구현하는 시점에는 Oracle과 MySQL 간 데이터 정합성이 대부분 맞지 않습니다.
- `case_0023` 별도 MyBatis 리포지토리 호출 방식: 다수의 비즈니스 로직에 걸쳐 광범위한 코드 변경이 필요하고 휴먼 에러 가능성이 커서 채택하지 않았다.
- `case_0024` 운영 트래픽 직접 복제(HTTP 트래픽 복사 / Kafka 토픽 복제): 타 부서 시스템에 중복 호출 부하를 야기하거나 운영에 영향을 줄 위험이 매우 높다.
- `case_0028` Alluxio: 일부 POSIX API 미지원, 원본 저장소와의 동기화 문제, 별도 클러스터 운영 부담 등으로 AiSuite 요구사항을 충분히 만족하지 못함.
- `case_0028` Ceph-rbd: ReadWriteMany/ReadOnlyMany를 지원하지 않아 다중 Pod 동시 접근이 불가능함.
- `case_0028` NFS: 간단하지만 확장성과 고가용성(H A) 측면에서 한계가 있어 대규모 AI 워크로드에 적합하지 않음.
- `case_0028` local-path: 노드 로컬 디스크 사용으로 동시 접근 불가 및 데이터 분산으로 인해 스케줄링/앱 단의 추가 구현 필요.
- `case_0028` GlusterFS/ CephFS: 직접 운영하는 경우 운영 부담이 크므로 우선순위에서 배제함.
- `case_0028` DDN EXAScaler: 요구사항을 만족하지만 도입 비용이 매우 커서 전체 도입은 현실적이지 않음.
- `case_0029` Spark: 마이크로배치 방식으로 인해 데이터 최신성 판별과 정확히 한 번 처리 보장을 동시에 만족하기 어렵다고 판단되어 채택하지 않음.
- `case_0029` 네이티브 쿠버네티스: 직접 리소스와 설정을 수동으로 구성해야 해 운영 부담이 크므로 오퍼레이터 방식으로 대체함.
- `case_0030` 온콜 알람 그대로 반영: 서비스의 상태를 CUJ 기반으로 정의해 SLI 메트릭과 SLO 달성 여부로 판단하기로 했기 때문에 온콜 알람 그대로 반영하지 않음
- `case_0030` 오류 예산 기반 표현: 서비스의 상태를 CUJ 기반으로 정의해 SLI 메트릭과 SLO 달성 여부로 판단하기로 했기 때문에 오류 예산 중심 표현을 최종 기준으로 삼지 않음
- `case_0031` IS: 사용 빈도가 감소하고 단점이 있음
- `case_0031` PSNR: 원본 이미지 필요로 해 일반 생성 평가에는 제한적임
- `case_0031` SSIM: 원본 이미지 필요로 해 일반 생성 평가에는 제한적임
- `case_0032` mecab-ipadic-neologd: MeCab 기반 사전 연동 불가
- `case_0032` Elasticsearch 7.10.2: 일몰 지원으로 장기 선택지 불가
- `case_0032` OpenSearch 2.4.1: Sudachi 공식 지원 범위 밖
- `case_0033` Edge N-gram on product index: 상품 인덱스 규모에서 토큰 폭증과 비용·지연 우려
- `case_0034` WebAuthn Level 3 (Passkey): Level 3 스펙(내 포함된 Passkey)은 초안 상태이고 Passkey 동기화 제어가 불가능하여 채택하지 않음
- `case_0035` 최근 등장 빈도: 최근 빈도만으로는 일상어가 상위에 올라 유행을 반영하지 못함
- `case_0035` 전일(d-1) 기준 비교만 사용: 전일 기준만 사용하면 지속되는 화제의 피크를 감지하지 못할 수 있음
- `case_0037` Agent: 로컬 에이전트 방식은 리소스 제약(vCPU/RAM) 등으로 대규모 환경에는 부적절해 Aggregator를 선택함.
- `case_0037` Unified: Unified는 에이전트와 애그리게이션을 결합한 형태로 엔터프라이즈/Datadog 연동 시 유리하나, 비용·복잡성 측면으로 이번 선택에서는 사용하지 않음.
- `case_0038` AI 직접 조회 (MCP): 외부 시스템을 AI가 직접 조회하면 가져온 텍스트가 전부 토큰 비용으로 계산되어 비용과 속도가 악화되기 때문에 버렸다.
- `case_0038` Notion 수동 정리: 수작업 정리는 노동력에 의존해 지속 가능하지 못해 버렸다.
- `case_0038` 한 덩어리 명령(모노리식 프롬프트): 한 번에 너무 많은 일을 시키면 단계가 얽혀 매번 다른 결과가 나와 신뢰성이 떨어져 분리했다.
- `case_0039` Python Kubernetes client: Python 클라이언트에서는 Informer를 사용할 수 없다고 판단해 Go로 재구현함.
- `case_0040` 메모리 증설: 임시방편으로 메모리만 늘리는 접근은 근본적 해결이 되지 않아 최종 채택하지 않음
- `case_0040` Parcel: 커스텀 제약으로 인해 현 프로젝트 요구에 부적합하다고 판단
- `case_0040` Rsbuild: 생태계가 작아 도입 후 확장성과 플러그인 지원이 우려되어 채택하지 않음
- `case_0041` nginx 라우팅 설정 변경: 웹서버 설정 변경 권한이 없어 실행할 수 없었음
- `case_0041` 스케줄링 배치 기반 캐싱: 최소한의 공수로 한 인스턴스 내에서 해결하기로 선택함
- `case_0042` nginx 설정: 인프라 구조상 적용 불가
- `case_0042` RDBMS 의존(예: MySQL 기반 방안): 시스템의 RDBMS 종속성을 피하기 위해 버림
- `case_0044` 네이티브 앱 구현: 앱 심사·업데이트로 운영 효율 저하
- `case_0046` max-lifetime 증가: 컬리로에서는 DB failover 시에 slave로 빠르게 연결하기 위해 max-lifetime을 작게 설정하고 있습니다.
- `case_0049` READ COMMITTED: 격리수준을 낮추면 Phantom Read가 발생하여 기존 비즈니스 로직에 영향이 있을 수 있어 채택하지 않음
- `case_0049` LOCK IN SHARE MODE (잠금 읽기): 잠금 읽기는 행을 잠궈 락 경합·데드락 위험이 있어 채택하지 않음
- `case_0050` Chrome Overrides: 매번 수동 작업이 필요한 1, 2번 방식은 리소스가 과도하게 소모될 것으로 판단했습니다.
- `case_0050` 프록시 툴(Charles/Fiddler): 매번 수동 작업이 필요한 1, 2번 방식은 리소스가 과도하게 소모될 것으로 판단했습니다.
- `case_0050` 실제 데이터 수정: API가 어떨 때 null 값을 넘겨주는지 정의되지 않아 데이터 수정으로 null을 넘겨주기는 어렵다고 판단했습니다.
- `case_0051` WebP 변환: 복잡한 이미지에서 압축 효율이 낮고, 품질을 낮추면 시각적 품질 저하가 발생하여 실제 적용에 제약이 있었음
- `case_0051` Canvas (메인 스레드): Canvas 기반 리사이징을 메인 스레드에서 수행하면 디코딩/인코딩 과정이 JS 블로킹을 초래하여 UI 응답성이 저하됨
- `case_0053` 수작업 카테고리 매핑: 사람이 수작업으로 카테고리 간 보완재 관계를 설정하는 방안
- `case_0053` 주문서 전체 그대로 학습: 한 건의 주문서를 모두 보완재로 가정해 그대로 학습하는 방식
- `case_0055` EAI I/F (DB 배치): 배치 기반 EAI는 배치로 인한 지연과 단일 EAI 어댑터 장애 시 전체 통신 정지 문제가 있어 채택하지 않음
- `case_0056` WriteConcern MAJORITY: 정확도를 높일 수 있으나 모든 요청에서 과반수 ACK를 기다리면 오버헤드가 크다.
- `case_0056` ReadPreference PRIMARY (글로벌 적용): 모든 읽기를 PRIMARY로 하면 SECONDARY 자원이 유휴화되어 자원 낭비가 발생한다.
- `case_0057` 메시지 지연 전달: 지연 전송은 간단하지만, 지연 시간이 짧으면 타이밍 문제가 여전히 발생할 수 있어 임시방편이다.
- `case_0057` Outbox 패턴: 데이터-메시지를 분리하는 안정적 방식이지만 설계·구현 비용과 시간이 부담된다.
- `case_0058` 에그: 운영 비용(사용자 교육 등)과 백업 회선에서 발생하는 모니터링 트래픽 문제로 부적합하다고 판단
- `case_0058` 동일 회선 사업자 이중화: 사업자 단위 장애에 취약하므로 동일 사업자 이중화는 선택하지 않음
- `case_0058` 5G 상품: 유선 인터넷 대비 품질·속도·안정성에서 아직 비교 불가로 주 회선 대체로 부적합
- `case_0062` hazelcast: 분산 in-memory data grid는 기능이 과하고 진입 장벽·운영 복잡도가 우려되어 사용하지 않음.
- `case_0062` chronicle-map: 힙 외 저장 등 장점이 있으나 기능·운영 측면에서 과하다고 판단되어 사용하지 않음.
- `case_0062` HPPC: fastutil을 선택했기 때문에 다른 primitive 컬렉션 라이브러리는 사용하지 않음; 라이브러리 간 성능 차이가 크지 않았음.
- `case_0062` trove: fastutil을 선택했기 때문에 사용하지 않음; 기능 면에서 차이가 크지 않았음.
- `case_0062` koloboke: fastutil을 선택했기 때문에 사용하지 않음; 기능 면에서 차이가 크지 않았음.
- `case_0063` 코드 난독화: 코드 난독화는 근본적인 방어가 되지 않았다.
- `case_0063` CAPTCHA: CAPTCHA는 매크로를 줄였지만 게임의 본질적 재미를 훼손했다.
- `case_0063` ZK-SNARK: 우아팝에 적용하기에 적절하지 않다고 판단했다.
- `case_0072` Cursor: 초보자·비개발자가 1시간 내에 사용하기엔 진입장벽이 높다고 판단
- `case_0072` Claude: 초보자·비개발자가 1시간 내에 사용하기엔 진입장벽이 높다고 판단
- `case_0075` Parcel: 프로젝트 구성이 복잡해 Zero-config 자동화 적용은 리스크가 크다고 판단되어 최종 선택에서 배제
- `case_0075` Rsbuild (Rspack 계열): 성능은 우수하지만 생태계·문서·커뮤니티가 작아 실서비스 적용의 위험 요소로 판단되어 배제
- `case_0077` OpenSearch(Elasticsearch): 전문 검색에는 강하지만 대용량 집계·비용 측면에서 부적합하여 배제
- `case_0077` Grafana Loki: 라벨 기반 제약과 집계 기능 한계로 복잡한 필드 기반 집계·검색 요구 충족 불가
- `case_0077` Signoz: 자체 스키마 강제 등으로 ClickHouse의 테이블 설계 장점을 활용하기 어려워 배제
- `case_0077` Amazon Athena: 컬럼 수·쿼리 성능·스키마 관리 한계로 장기 로그 조회 요구에 부적합
- `case_0078` Entity LifeCycle 콜백 (EntityListeners/AOP): 조회 시 복호화된 값을 1차 캐시에 저장하면서 JPA가 값 변경으로 판단해 불필요한 update 문을 발생시켰기 때문에 운영상 부작용이 발생하여 사용하지 않음.
- `case_0078` AWS SDK 1.x: 지원 중단 예정이라 장기간 유지보수 관점에서 선택하지 않음.
- `case_0079` Backstage: 오픈소스들을 참고했으나 자체 환경에 맞게 IDP를 구축하기로 함

## 글 목록

| 글 | 길이 | 결과 | 항목 | 발췌 탈락 | 제목 |
| --- | --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | - | 0/0 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics |
| d2/4555524 | 18,452 | 추출/기술 선택·도입형 | case_0028 | 0/17 | AI 플랫폼을 위한 스토리지 JuiceFS 도입기 |
| d2/8366976 | 3,331 | 추출/문제 해결형 | case_0017, case_0018, case_0019, case_0020 | 0/22 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/3814947 | 16,662 | 추출/기술 선택·도입형 | case_0014, case_0015, case_0016 | 0/19 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | - | 0/0 | Thread-safety in C++ |
| d2/1450243 | 15,218 | 추출/실험·활용기 | case_0013 | 0/15 | 윈도잉(windowing) 기법을 적용한 고성능 표 컴포넌트 개발기 |
| d2/8992409 | 1,342 | 추출/기술 선택·도입형 | case_0012 | 0/10 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| d2/6512234 | 22,022 | 추출/기술 선택·도입형 | case_0021, case_0022, case_0023, case_0024, case_0025, case_0026, case_0027 | 1/43 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/1155434 | 9,048 | 추출/문제 해결형 | case_0011 | 0/12 | C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가 |
| d2/9290861 | 796 | 제외/개념·튜토리얼 | - | 0/0 | Inside VictoriaMetrics |
| kakao/601 | 3,137 | 제외/회고·문화·행사 | - | 0/0 | 제3회 Kakao Tech Meet 후기 - 불확정성에서 감동까지 |
| kakao/624 | 787 | 제외/회고·문화·행사 | - | 0/0 | 카카오의 스팸 메일 대응 전략: 문자열 변형 CASE STUDY / 제6회 Kakao Tech Meet |
| kakao/761 | 3,645 | 제외/회고·문화·행사 | - | 0/0 | 실패를 장려하는 실험적 문화 |
| kakao/762 | 13,811 | 추출/실험·활용기 | case_0073 | 0/12 | 생산성 혁신의 실험: AI 마일리지 프로그램 |
| kakao/770 | 16,500 | 추출/기술 선택·도입형 | case_0075 | 1/15 | 5년 된 프로젝트의 빌드 도구를 교체하며 얻은 것들 |
| kakao/784 | 8,710 | 추출/실험·활용기 | case_0072 | 0/15 | 단 1시간 만에 99개의 MVP가? AI와 함께한 1K: 바이브코딩전 생생 후기 |
| kakao/785 | 4,597 | 추출/회고·문화·행사 | case_0069 | 0/10 | if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며 |
| kakao/804 | 3,760 | 추출/기술 선택·도입형 | case_0068 | 0/12 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/822 | 20,047 | 추출/실험·활용기 | case_0070, case_0071 | 0/19 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakao/835 | 12,198 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 둘째 날, 기술 세션 소개 |
| kakaopay/slack-bot-improving-operational-efficiency-2 | 5,044 | 추출/기술 선택·도입형 | case_0009 | 0/10 | 카카오페이 배포 효율화 1년 회고: 자동화 도입과 팀 생산성 향상 |
| kakaopay/tech-strategy-tpm | 9,673 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이 TPM은 어떤 일을 하나요? |
| kakaopay/katfun-joy-kotlin | 14,709 | 추출/실험·활용기 | case_0010 | 0/10 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kakaopay/ifkakao2024-devrel | 10,598 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스 준비 맛보기 |
| kakaopay/perftest_zone | 4,708 | 추출/기술 선택·도입형 | case_0082 | 0/10 | 카카오페이 성능 테스트 존을 소개합니다. |
| kakaopay/kakaopaysec-wecan | 8,650 | 추출/기술 선택·도입형 | case_0079, case_0080, case_0081 | 0/13 | We Can Do Better: 개발자 플랫폼 효율화 이야기 |
| kakaopay/kakaopayins-opensearch-analyzer | 10,157 | 추출/실험·활용기 | case_0076 | 0/9 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/kakaopayins-envelope-encryption | 18,389 | 추출/기술 선택·도입형 | case_0078 | 1/13 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/pallas-v2-log-platform | 25,659 | 추출/기술 선택·도입형 | case_0077 | 0/19 | 일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트 |
| kakaopay/kakaopayins-fe-common-component | 7,059 | 추출/기술 선택·도입형 | case_0074 | 0/10 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kurly/cart-recommend-model-development | 9,206 | 추출/실험·활용기 | case_0053 | 2/14 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 1부 |
| kurly/commit-mvcc-set-autocommit | 16,463 | 추출/문제 해결형 | case_0049 | 0/11 | 데이터가 있었는데요, 아니 없어요 |
| kurly/deliveryproductteam-culture-1 | 4,454 | 추출/실험·활용기 | case_0047 | 0/9 | 딜리버리 프로덕트 개발팀의 개발문화 - 로그 & 알람편 |
| kurly/connection-leak | 6,791 | 추출/문제 해결형 | case_0046 | 0/10 | 99%가 모른다는 DB Connection 누수 문제 |
| kurly/refine-address-internalization-2 | 4,312 | 추출/기술 선택·도입형 | case_0048 | 1/12 | 주소정제 서비스 내재화 - 2화 ( 그럴싸한 계획 ) |
| kurly/access-block-1 | 5,663 | 추출/문제 해결형 | case_0041 | 0/11 | nginx 설정 없이 우아하게 서비스 점검하기 (上) |
| kurly/access-block-2 | 8,383 | 추출/기술 선택·도입형 | case_0042 | 0/14 | nginx 설정 없이 우아하게 서비스 점검하기 (下) |
| kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0 | 13,290 | 추출/기술 선택·도입형 | case_0040 | 0/13 | 빌드가 터졌다: 5년 된 CMS 프로젝트의 Webpack4 → Vite 전환 |
| kurly/tech-spec-adoption-with-ai-automation | 8,164 | 추출/실험·활용기 | case_0043, case_0044, case_0045 | 0/21 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| kurly/claude-code-redesign-my-day | 7,389 | 추출/실험·활용기 | case_0038 | 0/13 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| ly/managing-multi-cdn-logs-traffics-with-vector | 16,695 | 추출/실험·활용기 | case_0037 | 0/15 | Vector를 활용해 멀티 CDN 로그 및 트래픽 관리하기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 18,813 | 추출/실험·활용기 | case_0036 | 0/8 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/improving-kubernetes-relay-api-server-performance-with-informer | 12,361 | 추출/기술 선택·도입형 | case_0039 | 2/13 | Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기 |
| ly/introducing-fido2-client-sdk-open-source | 9,957 | 추출/실험·활용기 | case_0034 | 0/13 | FIDO2 클라이언트 SDK 오픈소스 소개 |
| ly/how-to-evaluate-ai-generated-images-1 | 16,708 | 추출/개념·튜토리얼 | case_0031 | 0/12 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/extracting-trending-keywords-from-openchat-messages | 14,017 | 추출/실험·활용기 | case_0035 | 3/16 | 오픈챗 메시지들로부터 트렌딩 키워드 추출하기 |
| ly/pd1-ai-hackathon-recap | 4,153 | 제외/회고·문화·행사 | - | 0/0 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 6,232 | 추출/기술 선택·도입형 | case_0030 | 0/15 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 및 서비스 상태 확인 도구 LINE Status 개발기 |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 19,601 | 추출/기술 선택·도입형 | case_0029 | 0/12 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/japanese-search-kuromoji-to-sudachi | 15,395 | 추출/기술 선택·도입형 | case_0032, case_0033 | 1/20 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자가 좋아하는 과자는? |
| oliveyoung/2024-06-05_google-cloud-next-24-review | 3,796 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next '24 방문기 |
| oliveyoung/2024-08-11_type-and-type-system-with-typescript | 11,673 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 타입과 타입 시스템 |
| oliveyoung/2024-09-30_oy-feconf-2024 | 8,894 | 제외/회고·문화·행사 | - | 0/0 | 올리브영에서는 프론트엔드 개발자들이 이런 고민을 하는군요? |
| oliveyoung/2024-10-17_oy-delivery-mq | 4,642 | 추출/기술 선택·도입형 | case_0055 | 0/9 | 올리브영 물류시스템에서는 데이터를 어떻게 주고 받을까? |
| oliveyoung/2024-12-16_Design-System-Token-Automation | 17,955 | 추출/실험·활용기 | case_0054 | 0/9 | 디자인 시스템 중 디자인 토큰을 여러 도구를 이용하여 자동화 하는 방법 |
| oliveyoung/2024-12-17_catalog-mongo-transaction-2 | 11,450 | 추출/문제 해결형 | case_0056, case_0057 | 0/17 | Spring Boot MongoDB 트랜잭션 도입 실전 가이드 |
| oliveyoung/2025-02-14_oy-global-mall-address | 4,978 | 추출/기술 선택·도입형 | case_0052 | 0/12 | 올리브영 글로벌몰 주소 자동완성 및 검증 솔루션 도입기 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 7,158 | 추출/문제 해결형 | case_0051 | 0/11 | Web Worker로 이미지 처리 최적화하기 |
| oliveyoung/2025-06-10_chaos | 7,289 | 추출/실험·활용기 | case_0050 | 0/13 | 버그가 아니라 장애를 잡아라!! QA와 카오스 엔지니어링의 만남 |
| toss/27752 | 5,980 | 추출/실험·활용기 | case_0006 | 0/15 | 드래그 앤 드롭은 사실 편한 UX가 아니다? |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | - | 0/0 | 오픈소스에 기여하고 토스에 합격한.ssul \| EP.4 모닥불 |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | - | 0/0 | 개발자 리더로서 성장당한 썰 \| EP.7 모닥불 |
| toss/toss-frontend-ai-docs | 2,869 | 추출/문제 해결형 | case_0005 | 0/10 | 토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유 |
| toss/toss-people-3 | 7,801 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 문과생에서 토스 개발 리더까지 |
| toss/frontend-esbuild-hmr | 10,415 | 추출/실험·활용기 | case_0003 | 0/15 | ESBuild를 위한 HMR, 직접 만들기 |
| toss/frontend-apply-without-resume | 2,783 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드에 이력서 없이 리포지토리 링크로 지원하세요 (~5/31) |
| toss/toss-securities-gpu-mig | 13,794 | 추출/기술 선택·도입형 | case_0001 | 0/15 | GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기 |
| toss/tds-color-system-update | 13,423 | 추출/기술 선택·도입형 | case_0002 | 0/13 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| toss/ads_dashboard_fe | 12,467 | 추출/기술 선택·도입형 | case_0004 | 1/16 | 전체 데이터를 브라우저에 두는 광고 대시보드 만들기 |
| woowahan/14484 | 5,518 | 추출/문제 해결형 | case_0067 | 0/10 | “일단 백로그에 넣어두고 여유 있을 때 보는 걸로 할까요?” : 백로그를 백로그로 두지 않는 법 |
| woowahan/14671 | 6,108 | 추출/회고·문화·행사 | case_0066 | 0/11 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/15398 | 10,772 | 추출/실험·활용기 | case_0065 | 0/13 | Java의 미래, Virtual Thread |
| woowahan/15541 | 6,445 | 제외/개념·튜토리얼 | - | 0/0 | 웹 접근성 준수를 통한 모두에게 배달되는 일상의 행복 |
| woowahan/17386 | 11,245 | 추출/실험·활용기 | case_0059, case_0060, case_0061 | 0/20 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/17911 | 4,799 | 추출/기술 선택·도입형 | case_0058 | 0/13 | B마트 주문 유실을 없애보자: 네트워크 편 |
| woowahan/20763 | 8,615 | 추출/기술 선택·도입형 | case_0062 | 1/18 | 이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기 |
| woowahan/21027 | 25,102 | 추출/기술 선택·도입형 | case_0008 | 0/14 | 실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법 |
| woowahan/24434 | 15,179 | 추출/문제 해결형 | case_0007 | 0/11 | “함께 구매하면 좋은 상품” 추천 모델 고도화 |
| woowahan/24999 | 12,341 | 추출/실험·활용기 | case_0063, case_0064 | 0/20 | WOOWACON 2025 미니게임 WOOWA POP! |
