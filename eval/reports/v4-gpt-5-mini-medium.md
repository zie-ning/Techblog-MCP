# 추출 점검 리포트: v4-gpt-5-mini-medium

- 모델: gpt-5-mini (medium)
- 프롬프트 버전: 5bafd9ddcc5d
- 글 80편: 추출 60, 제외 20
- 항목 74개
- 토큰: 호출 152회, 입력 1,189,097 (캐시 407,168), 출력 449,214 (reasoning 338,496)
- 비용: $1.104 (편당 $0.0138), 전체 1,262편 추정 $17.4 / Batch $8.7

## 블로그별 추출 여부

| 블로그 | 추출 | 제외 | 항목 수 |
| --- | --- | --- | --- |
| d2 | 7 | 3 | 9 |
| kakao | 6 | 4 | 7 |
| kakaopay | 8 | 2 | 11 |
| kurly | 10 | 0 | 12 |
| ly | 9 | 1 | 11 |
| oliveyoung | 6 | 4 | 7 |
| toss | 6 | 4 | 6 |
| woowahan | 8 | 2 | 11 |

## 글 유형 × 추출 여부

| 글 유형 | 추출 | 제외 |
| --- | --- | --- |
| 개념·튜토리얼 | 1 | 3 |
| 기술 선택·도입형 | 26 | 0 |
| 문제 해결형 | 12 | 0 |
| 실험·활용기 | 21 | 1 |
| 회고·문화·행사 | 0 | 16 |

## 짧은 글 (평문 1,500자 미만) 8편

| 글 | 길이 | 결과 | 항목 | 분류 이유 |
| --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 추출/문제 해결형 | 1 | 기존 Symbolicator의 문제점과 성능·품질 한계, 이를 해결한 New Symbolicator의 알고리즘(심볼 맵 파일), SymbolFile CLI 처리 방식, 서버 아키텍처 및 성능·리소스 비교 등 구체적인 설계·운영 정보와 판단 근거를 제공하므로 실무 참고용으로 유용함. |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | 0 | 세션 개요와 개념(데이터 레이스, happens-before, basic thread safety 등) 설명 위주로, 구체적인 실무 적용 사례나 설계·도입 판단에 참고할 만한 구현·비교·문제 해결 내용이 포함되어 있지 않음. |
| d2/8992409 | 1,342 | 제외/실험·활용기 | 0 | 세션 발표 소개 및 목차 수준의 글로, Flow.er와 DBT·Airflow를 활용한 사례를 다룬다는 개요만 제공됨. 구체적인 설계 결정, 구현·설정 내용, 문제·해결 과정이나 수치 등의 기술적 실무 정보가 본문에 포함되어 있지 않아 다른 팀의 설계·구현 판단에 바로 참고할 수 없음. |
| d2/9290861 | 796 | 제외/회고·문화·행사 | 0 | 행사(ENGINEERING DAY) 세션 공개 안내로 목차와 대상만 소개되어 있으며, 구체적인 구현·문제 해결 사례, 수치·비교·설계 결정 근거 등 실무 적용점이 포함되어 있지 않습니다. 따라서 기술 사례 데이터베이스로는 추출할 내용이 아닙니다. |
| kakao/624 | 787 | 제외/회고·문화·행사 | 0 | 발표 영상과 발표자 인터뷰를 소개하는 홍보성 글로, 구체적인 설계 결정·수치·문제 해결 과정 등 실무적 기술 근거가 본문에 포함되어 있지 않습니다. 따라서 기술 사례 데이터베이스에 참조할 실무 내용이 없어 제외합니다. |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | 0 | 사내 간식 설문조사 결과 및 조직 문화·이벤트 소개를 다룬 글입니다. 기술적 문제 해결, 도구 선택·도입 근거, 실무 적용 팁이나 구현 상세가 없어 기술 사례 데이터베이스로는 적합하지 않습니다. |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | 0 | 인터뷰 형식의 경험담 및 채용/성장 스토리 중심 글로, 오픈소스 기여 사례는 언급되지만 구체적인 설정·워크플로·문제 해결 과정, 설계 결정 근거나 수치 등 다른 팀이 설계·구현 판단에 참고할 실무적 기술 정보가 포함되어 있지 않습니다. |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | 0 | 리더십 성장, 피드백, 조직의 역할 등 조직·문화·개인 경험을 다루는 대화형 콘텐츠로서 구체적인 기술적 문제 해결, 설계·도구 선택 근거, 적용 방법·수치 등의 실무적 내용이 없음. 따라서 기술적 실무 사례 데이터베이스로서 추출할 유의미한 기술적 정보가 아니므로 제외한다. |

## 글당 항목 수 (제외 글 빼고)

| 항목 수 | 글 수 |
| --- | --- |
| 1 | 50 |
| 2 | 6 |
| 3 | 4 |

## 문제 유형 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 개발 생산성 | 37 | 50% |
| 모니터링·관측성 | 14 | 19% |
| 배포·CI/CD | 10 | 14% |
| 업무·운영 자동화 | 10 | 14% |
| 비용 절감 | 9 | 12% |
| 데이터 정합성·트랜잭션 | 9 | 12% |
| 트래픽 급증 대응 | 9 | 12% |
| 인프라·컨테이너 | 8 | 11% |
| 데이터 파이프라인 | 7 | 9% |
| 인증·보안 | 6 | 8% |
| 장애 대응·복구 | 6 | 8% |
| 메시징·비동기 처리 | 6 | 8% |
| 캐싱 | 5 | 7% |
| API 설계·외부 연동 | 5 | 7% |
| 테스트 자동화 | 5 | 7% |
| 클라이언트 성능(웹·앱) | 4 | 5% |
| DB 성능·쿼리 최적화 | 4 | 5% |
| 동시성·락 | 2 | 3% |
| DB 마이그레이션·샤딩 | 1 | 1% |

- 쏠림(30% 초과): 개발 생산성
- 한 번도 안 쓰인 분류 (1개): MSA

## 도메인 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 사내 플랫폼·개발 도구 | 42 | 57% |
| 커머스·주문·재고 | 18 | 24% |
| LLM·AI | 13 | 18% |
| 검색·추천 | 6 | 8% |
| 범용 | 5 | 7% |
| 결제·금융 | 3 | 4% |
| 배달·물류 | 3 | 4% |
| 콘텐츠·미디어 | 3 | 4% |
| 채팅·메시징 서비스 | 2 | 3% |
| 광고·마케팅 | 1 | 1% |

- 쏠림(30% 초과): 사내 플랫폼·개발 도구
- 한 번도 안 쓰인 분류 (0개): 없음

## 발췌 검증

- 채택한 시도 기준 발췌 793개 중 탈락 9개 (원문 존재율 99%)
- 재시도한 글 12편

- `d2/3461887`: # 제목: App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics
- `d2/4555524`: 이를 해결하기 위해 hdfs://nameservice와 같이 네임네스페이스를 설정할 수 있도록 개선했다.
- `kurly/refine-address-internalization-2`: 외부업체 주소정제 축적 데이터 만으로는 대한민국의 모든 건물의 위경도를 커버할수 없다. ( 신규가입 고객분들의 주소 요청 때문에라도 외부업체와의 계약은 종료하지 못할 것 )
- `kurly/refine-address-internalization-2`: 제 기억에 이 때 까지는 외부 업체와의 계약 종료라는 목표는 뭔가 멀게만 느껴지는 목표였고, 일단 외부업체 api 호출 비용이라도 가능한 최소한으로 줄여보자는 목표로 계획을 세웠습니다.
- `kurly/access-block-2`: 그리고, 우리는 서버 엔지니어가 아니거나, nginx 설정 파일의 문법을 모르는 사람도 직관적으로 접근 차단을 설정하고, 활성화할 수 있길 원했습니다.
- `kurly/tech-spec-adoption-with-ai-automation`: 이어서 테크 스펙에 Coupon_ID와 Deal_Product_No를 조합하여 유일성을 보장하는 고유 키(Unique Key) 생성 함수를 설계했습니다.
- `ly/improving-kubernetes-relay-api-server-performance-with-informer`: 스레드를 다수 생성해서 작동 방식을 비동기적으로 바꿔 우회하는 방법을 써도 한 리소스를 계산하는 데 10초 정도가 걸렸습니다.
- `ly/japanese-search-kuromoji-to-sudachi`: compact_product_name_analyzer는 ... icu_normalizer → model_delim_to_space(커스텀 char_filter: -, _, / → 공백 변환) → punct_to_space(커스텀 char_filter: 나카구로·물결표 등 → 공백 변환) → collapse_spaces(커스텀 char_filter: 연속 공백  → 단일 공백)를 거친 뒤 whitespace tokenizer로 분리합니다.
- `ly/japanese-search-kuromoji-to-sudachi`: 단어 하나에서 최소~최대 길이만큼 접두사 토큰이 모두 생성되기 때문에, 문서 수가 많을수록 토큰 수 증가는 인덱스 크기와 색인 처리 비용에 직접적인 영향을 줍니다.

## 기술 사전에 없는 이름 199종

- Jira (4)
- Milvus (3)
- Locust (3)
- HDFS (3)
- GitHub (2)
- Web Worker (2)
- SWC (2)
- Transformer (2)
- Netty (2)
- Vector (2)
- Webpack (2)
- Vite (2)
- Storybook (2)
- esbuild (2)
- Rollup (2)
- ZSTD (2)
- LLM (2)
- Nexus (2)
- XBU (2)
- CLOUS3.0 (2)
- Iceberg (2)
- Confluence (2)
- OKLCH (1)
- Figma (1)
- Token Studio (1)
- Style Dictionary (1)
- @tds/token-utils (1)
- CSS (1)
- MIG (1)
- nvidia-device-plugin (1)
- dcgm-exporter (1)
- nvidia-smi (1)
- H100 (1)
- A100 (1)
- Fetch API (1)
- ESBuild (1)
- react-refresh (1)
- WebSocket (1)
- HTML (1)
- WASM (1)
- Rust (1)
- Node2Vec (1)
- SASRec (1)
- Redis Stack (1)
- pgvector (1)
- IPSEC (1)
- LTE 라우터 (1)
- DNS (1)
- DHCP (1)
- NTP (1)
- RADIUS (1)
- S2 Geometry (1)
- fastutil (1)
- AWS ALB (1)
- Spring Cloud (1)
- Spring Cloud Bus (1)
- Athena (1)
- Virtual Thread (1)
- ForkJoinPool (1)
- NIO (1)
- Reactor (1)
- Canva (1)
- MLA (1)
- MoE (1)
- CoT (1)
- JMH (1)
- JFR (1)
- async-profiler (1)
- jstack (1)
- Codex (1)
- v0 (1)
- Supabase (1)
- Vercel (1)
- IntelliJ (1)
- Claude API (1)
- Veo3 (1)
- Flowith (1)
- Parcel (1)
- Rsbuild (1)
- Rspack (1)
- Vitest (1)
- Jest (1)
- Babel (1)
- MiniCssExtractPlugin (1)
- reach.tech (1)
- Polaris (1)
- AWS KMS (1)
- HyperDX (1)
- Parquet (1)
- Filebeat (1)
- Amazon Athena (1)
- Testcraft (1)
- InfluxDB (1)
- Mongo (1)
- GCP (1)
- OpenSearch Dashboards (1)
- Apache Lucene (1)
- Spinnaker (1)
- Hive (1)
- datasource-proxy (1)
- Release Please Action (1)
- Dokka (1)
- JFrog Artifactory (1)
- Maven Central (1)
- vanniktech-maven-publish-plugin (1)
- GitHub Pages (1)
- Ruler (1)
- react-window (1)
- ResizeObserver (1)
- C++ (1)
- std::bit_cast (1)
- reinterpret_cast (1)
- memcpy (1)
- POI (1)
- NCrashlytics (1)
- Old Symbolicator (1)
- New Symbolicator (1)
- Symbol Map File (1)
- SymbolFile CLI (1)
- JuiceFS (1)
- MinIO (1)
- CSI Driver (1)
- Kubeflow (1)
- FUSE (1)
- fio (1)
- Alluxio (1)
- DDN EXAScaler (1)
- EFS (1)
- Filestore (1)
- Flink Kubernetes Operator (1)
- Sudachi (1)
- Kuromoji (1)
- Edge N-gram (1)
- ICU (1)
- Inception (1)
- CLIP (1)
- DINO (1)
- VGG (1)
- FlanT5 (1)
- LAION (1)
- Android (1)
- iOS (1)
- Xcode (1)
- iOS Secure Enclave (1)
- ARM TrustZone (1)
- Android StrongBox (1)
- Hubot (1)
- Ansible (1)
- Harbor (1)
- Git (1)
- node_exporter (1)
- kube-state-metrics (1)
- client-go (1)
- Informer (1)
- kubectl (1)
- kube-apiserver (1)
- etcd (1)
- Notion (1)
- MobX (1)
- Material-UI (1)
- Tailwind CSS (1)
- vite-plugin-babel (1)
- @vitejs/plugin-react (1)
- rollup-plugin-visualizer (1)
- react-csv (1)
- dayjs (1)
- qs (1)
- ForkTsCheckerWebpackPlugin (1)
- Taskmaster (1)
- WebView (1)
- localStorage (1)
- mysql-connector-j (1)
- Eclipse MAT (1)
- AWS EC2 (1)
- Google Sheets (1)
- BigQuery (1)
- Swagger (1)
- Postman (1)
- 행정안전부 도로명주소조회 API (1)
- 행정안전부 좌표정보 API (1)
- 외부업체 주소정제 API (1)
- OMS API (1)
- BERT4Rec (1)
- PyTorch (1)
- MLflow (1)
- Gradio (1)
- Growthbook (1)
- MariaDB Connector/J (1)
- mitmproxy (1)
- OffscreenCanvas (1)
- MQ (1)
- EAI (1)
- DB (1)
- Yarn (1)
- Panda CSS (1)
- Tokens Studio For Figma (1)
- token-transformer (1)
- AWS ECR/ECS/S3 (1)
- Spring Data MongoDB (1)

## 버린 대안 86개 (항목 74개 중)

- `case_0001` 부분적 토큰 수정: 개별 토큰만 수정하면 다른 색상들과 전체 팔레트, 다크모드까지 연쇄적으로 영향을 받아 유지하기 어려움
- `case_0002` 클라우드 활용: 장기적·지속적 워크로드나 자체 IDC 환경에서는 비용이 더 발생할 수 있고 보안·컴플라이언스 제약이 존재함.
- `case_0002` 혼합 GPU 운영: 운영 정책 복잡성과 관리 부담, GPU 간 호환성 문제 및 장기적 수요 편중에 따른 유휴 자원 발생 리스크가 있음.
- `case_0002` MPS: 소프트웨어 방식이라 격리가 어려워 운영 리스크가 크고 모니터링·제어가 복잡함.
- `case_0003` Virtual Scrolling: 한 화면에 수천 개 행을 펼치는 UX가 아니라 페이지네이션(100건 단위)이므로 필요 없다고 판단.
- `case_0003` IndexedDB 캐싱: 캐시 무효화 규칙이 명확하지 않고, 요구 대비 과한 복잡도와 부수 비용이 발생한다고 판단.
- `case_0006` aria-roledescription: aria 1.3 지원이 필요한데 iPhone에서 지원하지 않아 사용하지 않음
- `case_0007` 코드 난독화: 시간을 지연시키는 수준이었고 근본적인 방어가 되지 못했다.
- `case_0007` 프로그래스바 중앙 클릭 트릭: 우회가 쉬워 무용지물이었다.
- `case_0007` CAPTCHA: 매크로는 막았지만 게임 재미가 크게 훼손되어 채택하지 않기로 함.
- `case_0008` 완벽한 실시간 반영: 동시접속 환경에서 DB 병목을 유발하므로 포기하고 일정 지연을 허용하는 설계를 선택함.
- `case_0009` Item2Vec: 초기 도입 모델이었으나 대체재 편향과 순서 정보를 반영하지 못하는 한계 때문에 개선 대상이 되었습니다.
- `case_0010` Milvus: 1차 실험 후보였으나 2차 실험 최종 후보로는 선정되지 않음
- `case_0010` Redis Stack: 1차 실험 후보였으나 2차 실험 최종 후보로는 선정되지 않음
- `case_0010` Pinecone: 관리 주체·비용 문제로 초기에는 fully-managed 전문 서비스 도입을 우선 고려하지 않음
- `case_0010` OpenSearch: 2차 실험 후보였으나 RDS가 더 나은 성능을 보여 최종 선정되지 않음 **(technologies에도 있음)**
- `case_0010` Atlas MongoDB: 2차 실험 후보였으나 RDS가 더 나은 성능을 보여 최종 선정되지 않음
- `case_0011` 에그(와이파이 도시락): 운영 비용(사용자 교육·네트워크 관리) 증가 우려로 불리함
- `case_0011` 동일 사업자 이중화: 지역/전국 단위 사업자 장애에 취약하므로 회선 이원화(다른 사업자)가 필요함
- `case_0012` 캐시 레이어: 캐시 레이어(예: Redis)를 도입하면 비용과 작업량 증가로 인해 선택하지 않음
- `case_0012` Redis: 캐시/DB 레이어 도입 검토 대상이었으나 비용·작업량 때문에 우선 보류
- `case_0012` hazelcast: 분산 in-memory 솔루션은 기능이 과하고 진입장벽이 높아 제외
- `case_0012` chronicle-map: 힙 외부 저장 라이브러리는 과한 기능과 복잡성 우려로 제외
- `case_0012` HPPC: primitive 컬렉션 라이브러리들 사이에 성능 차이가 없어 fastutil을 선택함
- `case_0012` trove: primitive 컬렉션 라이브러리들 사이에 성능 차이가 없어 fastutil을 선택함
- `case_0012` koloboke: primitive 컬렉션 라이브러리들 사이에 성능 차이가 없어 fastutil을 선택함
- `case_0016` Kotlin coroutine: 프로덕션 코드 변경 필요성 및 러닝커브
- `case_0016` Reactive programming: 코드 파편화·디버깅 어려움·성능 낭비
- `case_0021` Cursor: 초보자나 비개발자가 1시간 안에 사용법을 익히고 의미 있는 성과를 내기엔 진입장벽이 높다고 판단했습니다.
- `case_0021` Claude: 초보자나 비개발자가 1시간 안에 사용법을 익히고 의미 있는 성과를 내기엔 진입장벽이 높다고 판단했습니다.
- `case_0024` Parcel: Zero-config 장점이 있으나 복잡한 프로젝트에서 자동화 리스크가 있어 배제
- `case_0024` Rsbuild: 성능은 우수하나 생태계·문서·커뮤니티가 부족해 실서비스 적용 부담
- `case_0027` Entity LifeCycle 콜백(@PrePersist/@PostLoad): 조회 시 복호화로 인해 1차 캐시 값이 변경되며 의도치 않은 update 쿼리가 발생하는 부작용이 있었다.
- `case_0028` Elasticsearch / OpenSearch: 대용량 집계와 저장 효율 측면에서 비용이 높고 성능 한계가 있어 본안으로 채택하지 않음
- `case_0028` Grafana Loki: 라벨 기반 제약과 집계 기능 한계로 우리 요구(다양한 필드 검색·대용량 집계)에 부적합
- `case_0028` Signoz: Signoz의 고정된 스키마·UI 제약 때문에 ClickHouse 고유의 테이블 설계 장점을 활용할 수 없음
- `case_0036` MyBatis 리포지토리 분리 이중 호출: 소스 코드 변경 범위가 지나치게 넓음
- `case_0036` ChainedTransactionManager / 분산 트랜잭션: 이중 쓰기 시점에 Oracle과 MySQL 간 데이터 정합성이 맞지 않을 수 있고, MySQL 쿼리 실패로 전체 트랜잭션이 롤백되면 안 되기 때문
- `case_0038` @tanstack/react-virtual: 네이버 로그 표현의 다양성과 복잡성 때문에 오픈소스로 대응하기 어렵다고 판단되어 채택하지 않음
- `case_0038` react-window: div 기반 레이아웃의 한계로 인해 요구사항을 충족하지 못해 대체함
- `case_0039` union 타입 퍼닝: C++에서는 UB이므로 사용하지 않음
- `case_0039` reinterpret_cast 타입 퍼닝: 엄격한 앨리어싱 규칙 위반
- `case_0044` GlusterFS, CephFS: 직접 운영 부담이 크기 때문에 사용하지 않음
- `case_0044` Alluxio: 일부 POSIX API 미지원 등으로 AI 워크로드에 불편하여 사용하지 않음
- `case_0044` Ceph-rbd: 동시 접근(ReadWriteMany) 지원 부족
- `case_0044` NFS: 확장성·고가용성 문제
- `case_0044` local-path: 노드 로컬 저장이라 동시 접근 불가 및 스케줄링 부담
- `case_0044` DDN EXAScaler: 도입 비용이 커서 부분적으로만 도입
- `case_0044` 외부 클라우드 스토리지: AiSuite는 사내 구축이라 외부 클라우드 스토리지 사용 불가
- `case_0045` Apache Spark ← Spark: 마이크로 배치 방식의 한계로 데이터 최신성 판별과 정확히 한 번 처리 보장을 동시에 만족하기 어려워 채택하지 않음
- `case_0045` 네이티브 쿠버네티스: 설정·운영을 수동으로 모두 처리해야 하는 번거로움 때문에 오퍼레이터 방식 대신 채택하지 않음
- `case_0046` 온힙 메모리 증설: 온힙 메모리를 늘려도 압박이 계속되어 근본 해결이 되지 않아 다른 메모 할당 전략으로 전환
- `case_0047` mecab-ipadic-neologd: Kuromoji에 최신 MeCab 기반 사전을 직접 연동할 수 없고, 사내 Elasticsearch 7.10.2 환경에서는 적용에 제약이 있어 사용하지 않음
- `case_0047` Elasticsearch 업그레이드: Elasticsearch 최신 기능으로 해결하는 방안은 사내 플랫폼이 7.10.2만 지원하고 일몰 방향이라 선택지에서 제외됨
- `case_0050` api.line-status.info: 이 페이지는 LINE 메시징과 로그인, LIFF(LINE front-end framework) 등 외부 API 사용자가 API 상태를 확인할 수 있는 방법을 제공하는 것에 초점을 둔 페이지였습니다.
- `case_0050` 온콜 알람 반영: 따라서 서비스의 상태 역시 단순 장애 발생 유무가 아니라 CUJ 기반으로 정의한 SLI 메트릭을 측정해 SLO 달성 여부를 판단하는 관점에서 표현하는 것이 일관적인 접근 방식이라고 판단했습니다.
- `case_0051` WebAuthn Level 3 / Passkey: Level 3 스펙은 아직 공식적으로 확정되지 않은 초안(draft) 상태입니다.
- `case_0052` 블랙리스트 방식: 정적 블랙리스트로는 예측 불가능한 지명·인명 등이 필터링되지 않아 실용적이지 않았다.
- `case_0052` d-1 기준(하루 전 비교): 하루 전을 기준으로 삼으면 연속적 증가 중에 Z값이 급격히 하락해 화제성을 놓칠 수 있어 채택하지 않았다.
- `case_0055` Python 클라이언트 Informer 지원: Python 클라이언트에서 Informer를 사용할 수 없어 채택 불가
- `case_0056` AI의 외부 시스템 직접 조회 (MCP): 외부 시스템을 AI가 직접 조회하면 가져온 텍스트가 토큰으로 계산되어 비용과 속도가 악화되었기 때문에 대체하였다
- `case_0059` 메모리 증설: 임시 해결
- `case_0059` Webpack 최적화 (filesystem cache, splitChunks): 부분 개선으로 근본 해결 아님
- `case_0059` Parcel: 커스텀 제한적
- `case_0059` Rsbuild: 생태계 작음
- `case_0060` nginx 라우팅 설정: 애초에 생각은 했으나 인스턴스 설정 변경·재시작 권한이 없어서 적용할 수 없었다
- `case_0060` 스케줄링 배치 기반 캐싱: 주기적 배치 대신 최소한의 공수로 하나의 인스턴스 안에서 해결하는 쪽을 택했다
- `case_0061` 네이티브 앱 개발: 정책 변경 시마다 앱 심사와 업데이트가 필요해 운영 효율이 떨어지기 때문
- `case_0062` max-lifetime 증가: 하지만 컬리로에서는 DB failover 시에 slave로 빠르게 연결하기 위해 max-lifetime을 작게 설정하고 있습니다.
- `case_0064` nginx 설정으로 차단: 인프라 구성상 nginx 설정을 통한 차단은 적합하지 않음
- `case_0064` 호출 횟수 기반 동기화: 트래픽 변동에 따라 동기화 주기 예측이 어려움
- `case_0066` 주문서 기반 모든 상품을 보완재 가정: 주문서 내 모든 상품을 보완재로 가정하면 특정 상품 편향으로 실제 보완재 관계를 반영하지 못함
- `case_0067` READ COMMITTED 격리수준: 격리수준을 낮추면 Phantom Read 등 기존 비즈니스에 영향이 있을 수 있어 채택하지 않음.
- `case_0067` 잠금 읽기 (LOCK IN SHARE MODE): 잠금 읽기는 락 경합·데드락 위험이 있어 채택하지 않음.
- `case_0068` Chrome overwrite contents: 필드 값이 많을 경우 수동 수정의 번거로움과 리소스 과다 소모
- `case_0068` Charles/Fiddler: 필드 값이 많을 경우 수동 수정의 번거로움과 리소스 과다 소모
- `case_0068` 실제 데이터 수정: API가 언제 null을 반환하는지 정의되지 않아 데이터 수정으로 재현하기 어렵다
- `case_0069` WebP 포맷 변환: 복잡한 이미지에서는 압축 효율이 낮아 품질을 유지하면서 용량을 줄이기 어려움
- `case_0069` Canvas 리사이징(메인 스레드): Canvas 처리 비용으로 메인 스레드를 점유해 디코딩/인코딩 과정에서 JS 블로킹이 발생함
- `case_0069` Shared Worker: 여러 탭/창 공유 특성이 이미지 전처리에는 불필요해 배제됨
- `case_0069` Service Worker: 네트워크 프록시·캐싱 역할 등 이미지 전처리에 필요한 특성이 아님
- `case_0070` 국가별 주문서 양식 분리: 60개가 넘는 국가마다 주문서 양식을 모두 다르게 만들 수는 없었습니다.
- `case_0073` WriteConcern MAJORITY: 모든 요청에 대해 Secondary 과반수 ACK 응답을 기다리면 큰 오버헤드를 발생시킬 수 있습니다.
- `case_0073` ReadPreference PRIMARY (전역 설정): PRIMARY로 설정하면 SECONDARY 노드가 유휴 상태로 남아 리소스를 낭비할 수 있다.
- `case_0074` SQS 지연 전송: 지연 시간이 너무 짧다면 타이밍 문제가 여전히 발생할 수 있어 임시방편에 불과
- `case_0074` Outbox 패턴: 설계 및 구현에 걸리는 시간과 비용이 부담되어 당장 적용하기에는 무거움

## 글 목록

| 글 | 길이 | 결과 | 항목 | 발췌 탈락 | 제목 |
| --- | --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 추출/문제 해결형 | case_0043 | 1/10 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics |
| d2/4555524 | 18,452 | 추출/기술 선택·도입형 | case_0044 | 1/27 | AI 플랫폼을 위한 스토리지 JuiceFS 도입기 |
| d2/8366976 | 3,331 | 추출/문제 해결형 | case_0040, case_0041, case_0042 | 0/21 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/3814947 | 16,662 | 추출/실험·활용기 | case_0037 | 0/12 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | - | 0/0 | Thread-safety in C++ |
| d2/1450243 | 15,218 | 추출/문제 해결형 | case_0038 | 0/13 | 윈도잉(windowing) 기법을 적용한 고성능 표 컴포넌트 개발기 |
| d2/8992409 | 1,342 | 제외/실험·활용기 | - | 0/0 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| d2/6512234 | 22,022 | 추출/기술 선택·도입형 | case_0036 | 0/13 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/1155434 | 9,048 | 추출/문제 해결형 | case_0039 | 0/11 | C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가 |
| d2/9290861 | 796 | 제외/회고·문화·행사 | - | 0/0 | Inside VictoriaMetrics |
| kakao/601 | 3,137 | 제외/회고·문화·행사 | - | 0/0 | 제3회 Kakao Tech Meet 후기 - 불확정성에서 감동까지 |
| kakao/624 | 787 | 제외/회고·문화·행사 | - | 0/0 | 카카오의 스팸 메일 대응 전략: 문자열 변형 CASE STUDY / 제6회 Kakao Tech Meet |
| kakao/761 | 3,645 | 추출/실험·활용기 | case_0023 | 0/11 | 실패를 장려하는 실험적 문화 |
| kakao/762 | 13,811 | 추출/실험·활용기 | case_0022 | 0/9 | 생산성 혁신의 실험: AI 마일리지 프로그램 |
| kakao/770 | 16,500 | 추출/기술 선택·도입형 | case_0024 | 0/13 | 5년 된 프로젝트의 빌드 도구를 교체하며 얻은 것들 |
| kakao/784 | 8,710 | 추출/실험·활용기 | case_0021 | 0/12 | 단 1시간 만에 99개의 MVP가? AI와 함께한 1K: 바이브코딩전 생생 후기 |
| kakao/785 | 4,597 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며 |
| kakao/804 | 3,760 | 추출/기술 선택·도입형 | case_0018 | 0/11 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/822 | 20,047 | 추출/실험·활용기 | case_0019, case_0020 | 0/17 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakao/835 | 12,198 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 둘째 날, 기술 세션 소개 |
| kakaopay/slack-bot-improving-operational-efficiency-2 | 5,044 | 추출/문제 해결형 | case_0035 | 0/9 | 카카오페이 배포 효율화 1년 회고: 자동화 도입과 팀 생산성 향상 |
| kakaopay/tech-strategy-tpm | 9,673 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이 TPM은 어떤 일을 하나요? |
| kakaopay/katfun-joy-kotlin | 14,709 | 추출/실험·활용기 | case_0034 | 0/11 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kakaopay/ifkakao2024-devrel | 10,598 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스 준비 맛보기 |
| kakaopay/perftest_zone | 4,708 | 추출/기술 선택·도입형 | case_0032 | 0/11 | 카카오페이 성능 테스트 존을 소개합니다. |
| kakaopay/kakaopaysec-wecan | 8,650 | 추출/기술 선택·도입형 | case_0029, case_0030, case_0031 | 0/19 | We Can Do Better: 개발자 플랫폼 효율화 이야기 |
| kakaopay/kakaopayins-opensearch-analyzer | 10,157 | 추출/실험·활용기 | case_0033 | 0/11 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/kakaopayins-envelope-encryption | 18,389 | 추출/실험·활용기 | case_0026, case_0027 | 0/12 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/pallas-v2-log-platform | 25,659 | 추출/기술 선택·도입형 | case_0028 | 0/18 | 일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트 |
| kakaopay/kakaopayins-fe-common-component | 7,059 | 추출/기술 선택·도입형 | case_0025 | 0/11 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kurly/cart-recommend-model-development | 9,206 | 추출/기술 선택·도입형 | case_0066 | 0/12 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 1부 |
| kurly/commit-mvcc-set-autocommit | 16,463 | 추출/문제 해결형 | case_0067 | 0/10 | 데이터가 있었는데요, 아니 없어요 |
| kurly/deliveryproductteam-culture-1 | 4,454 | 추출/실험·활용기 | case_0063 | 0/9 | 딜리버리 프로덕트 개발팀의 개발문화 - 로그 & 알람편 |
| kurly/connection-leak | 6,791 | 추출/문제 해결형 | case_0062 | 0/10 | 99%가 모른다는 DB Connection 누수 문제 |
| kurly/refine-address-internalization-2 | 4,312 | 추출/기술 선택·도입형 | case_0065 | 2/13 | 주소정제 서비스 내재화 - 2화 ( 그럴싸한 계획 ) |
| kurly/access-block-1 | 5,663 | 추출/문제 해결형 | case_0060 | 0/11 | nginx 설정 없이 우아하게 서비스 점검하기 (上) |
| kurly/access-block-2 | 8,383 | 추출/기술 선택·도입형 | case_0064 | 1/19 | nginx 설정 없이 우아하게 서비스 점검하기 (下) |
| kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0 | 13,290 | 추출/기술 선택·도입형 | case_0059 | 0/14 | 빌드가 터졌다: 5년 된 CMS 프로젝트의 Webpack4 → Vite 전환 |
| kurly/tech-spec-adoption-with-ai-automation | 8,164 | 추출/기술 선택·도입형 | case_0061 | 1/12 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| kurly/claude-code-redesign-my-day | 7,389 | 추출/실험·활용기 | case_0056, case_0057, case_0058 | 0/18 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| ly/managing-multi-cdn-logs-traffics-with-vector | 16,695 | 추출/실험·활용기 | case_0054 | 0/12 | Vector를 활용해 멀티 CDN 로그 및 트래픽 관리하기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 18,813 | 추출/실험·활용기 | case_0053 | 0/10 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/improving-kubernetes-relay-api-server-performance-with-informer | 12,361 | 추출/기술 선택·도입형 | case_0055 | 1/12 | Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기 |
| ly/introducing-fido2-client-sdk-open-source | 9,957 | 추출/실험·활용기 | case_0051 | 0/9 | FIDO2 클라이언트 SDK 오픈소스 소개 |
| ly/how-to-evaluate-ai-generated-images-1 | 16,708 | 추출/개념·튜토리얼 | case_0048 | 0/9 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/extracting-trending-keywords-from-openchat-messages | 14,017 | 추출/실험·활용기 | case_0052 | 0/14 | 오픈챗 메시지들로부터 트렌딩 키워드 추출하기 |
| ly/pd1-ai-hackathon-recap | 4,153 | 제외/회고·문화·행사 | - | 0/0 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 6,232 | 추출/기술 선택·도입형 | case_0049, case_0050 | 0/18 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 및 서비스 상태 확인 도구 LINE Status 개발기 |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 19,601 | 추출/기술 선택·도입형 | case_0045, case_0046 | 0/19 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/japanese-search-kuromoji-to-sudachi | 15,395 | 추출/기술 선택·도입형 | case_0047 | 2/16 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자가 좋아하는 과자는? |
| oliveyoung/2024-06-05_google-cloud-next-24-review | 3,796 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next '24 방문기 |
| oliveyoung/2024-08-11_type-and-type-system-with-typescript | 11,673 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 타입과 타입 시스템 |
| oliveyoung/2024-09-30_oy-feconf-2024 | 8,894 | 제외/회고·문화·행사 | - | 0/0 | 올리브영에서는 프론트엔드 개발자들이 이런 고민을 하는군요? |
| oliveyoung/2024-10-17_oy-delivery-mq | 4,642 | 추출/기술 선택·도입형 | case_0071 | 0/11 | 올리브영 물류시스템에서는 데이터를 어떻게 주고 받을까? |
| oliveyoung/2024-12-16_Design-System-Token-Automation | 17,955 | 추출/실험·활용기 | case_0072 | 0/10 | 디자인 시스템 중 디자인 토큰을 여러 도구를 이용하여 자동화 하는 방법 |
| oliveyoung/2024-12-17_catalog-mongo-transaction-2 | 11,450 | 추출/문제 해결형 | case_0073, case_0074 | 0/17 | Spring Boot MongoDB 트랜잭션 도입 실전 가이드 |
| oliveyoung/2025-02-14_oy-global-mall-address | 4,978 | 추출/기술 선택·도입형 | case_0070 | 0/11 | 올리브영 글로벌몰 주소 자동완성 및 검증 솔루션 도입기 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 7,158 | 추출/문제 해결형 | case_0069 | 0/12 | Web Worker로 이미지 처리 최적화하기 |
| oliveyoung/2025-06-10_chaos | 7,289 | 추출/실험·활용기 | case_0068 | 0/11 | 버그가 아니라 장애를 잡아라!! QA와 카오스 엔지니어링의 만남 |
| toss/27752 | 5,980 | 추출/실험·활용기 | case_0006 | 0/13 | 드래그 앤 드롭은 사실 편한 UX가 아니다? |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | - | 0/0 | 오픈소스에 기여하고 토스에 합격한.ssul \| EP.4 모닥불 |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | - | 0/0 | 개발자 리더로서 성장당한 썰 \| EP.7 모닥불 |
| toss/toss-frontend-ai-docs | 2,869 | 추출/기술 선택·도입형 | case_0005 | 0/9 | 토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유 |
| toss/toss-people-3 | 7,801 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 문과생에서 토스 개발 리더까지 |
| toss/frontend-esbuild-hmr | 10,415 | 추출/문제 해결형 | case_0004 | 0/10 | ESBuild를 위한 HMR, 직접 만들기 |
| toss/frontend-apply-without-resume | 2,783 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드에 이력서 없이 리포지토리 링크로 지원하세요 (~5/31) |
| toss/toss-securities-gpu-mig | 13,794 | 추출/기술 선택·도입형 | case_0002 | 0/16 | GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기 |
| toss/tds-color-system-update | 13,423 | 추출/기술 선택·도입형 | case_0001 | 0/12 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| toss/ads_dashboard_fe | 12,467 | 추출/기술 선택·도입형 | case_0003 | 0/13 | 전체 데이터를 브라우저에 두는 광고 대시보드 만들기 |
| woowahan/14484 | 5,518 | 추출/문제 해결형 | case_0017 | 0/9 | “일단 백로그에 넣어두고 여유 있을 때 보는 걸로 할까요?” : 백로그를 백로그로 두지 않는 법 |
| woowahan/14671 | 6,108 | 제외/회고·문화·행사 | - | 0/0 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/15398 | 10,772 | 추출/실험·활용기 | case_0016 | 0/14 | Java의 미래, Virtual Thread |
| woowahan/15541 | 6,445 | 제외/개념·튜토리얼 | - | 0/0 | 웹 접근성 준수를 통한 모두에게 배달되는 일상의 행복 |
| woowahan/17386 | 11,245 | 추출/실험·활용기 | case_0013, case_0014, case_0015 | 0/20 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/17911 | 4,799 | 추출/기술 선택·도입형 | case_0011 | 0/13 | B마트 주문 유실을 없애보자: 네트워크 편 |
| woowahan/20763 | 8,615 | 추출/기술 선택·도입형 | case_0012 | 0/18 | 이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기 |
| woowahan/21027 | 25,102 | 추출/기술 선택·도입형 | case_0010 | 0/15 | 실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법 |
| woowahan/24434 | 15,179 | 추출/실험·활용기 | case_0009 | 0/11 | “함께 구매하면 좋은 상품” 추천 모델 고도화 |
| woowahan/24999 | 12,341 | 추출/실험·활용기 | case_0007, case_0008 | 0/19 | WOOWACON 2025 미니게임 WOOWA POP! |
