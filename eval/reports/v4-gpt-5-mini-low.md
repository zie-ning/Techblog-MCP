# 추출 점검 리포트: v4-gpt-5-mini-low

- 모델: gpt-5-mini (low)
- 프롬프트 버전: 5bafd9ddcc5d
- 글 80편: 추출 60, 제외 20
- 항목 69개
- 토큰: 호출 158회, 입력 1,282,673 (캐시 485,248), 출력 191,777 (reasoning 83,904)
- 비용: $0.595 (편당 $0.0074), 전체 1,262편 추정 $9.4 / Batch $4.7

## 블로그별 추출 여부

| 블로그 | 추출 | 제외 | 항목 수 |
| --- | --- | --- | --- |
| d2 | 8 | 2 | 11 |
| kakao | 5 | 5 | 5 |
| kakaopay | 9 | 1 | 11 |
| kurly | 10 | 0 | 10 |
| ly | 8 | 2 | 8 |
| oliveyoung | 6 | 4 | 7 |
| toss | 6 | 4 | 6 |
| woowahan | 8 | 2 | 11 |

## 글 유형 × 추출 여부

| 글 유형 | 추출 | 제외 |
| --- | --- | --- |
| 개념·튜토리얼 | 0 | 4 |
| 기술 선택·도입형 | 29 | 0 |
| 문제 해결형 | 11 | 0 |
| 실험·활용기 | 19 | 0 |
| 회고·문화·행사 | 1 | 16 |

## 짧은 글 (평문 1,500자 미만) 8편

| 글 | 길이 | 결과 | 항목 | 분류 이유 |
| --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | 0 | 사내 행사(엔지니어링 데이)에서 공개된 세션 소개/요약 문서입니다. 세션에서 다루는 주제 목록은 기술적 항목을 포함하지만 본문에 구체적인 설계·구현 세부사항(수치, 비교 결과, 설정·워크플로우 등)이 담겨 있지 않아 실무 설계 판단에 바로 참고 가능한 기술적 적용 내용은 없습니다. |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | 0 | 세션은 C++의 thread-safety 개념(데이터 레이스, happens-before, basic thread safety 등)을 정리하는 발표 내용 및 목차 소개로, 구체적인 실무 적용 사례·해결 과정·설계 판단 근거(설정, 워크플로우, 성능 수치 등)가 포함되어 있지 않음. 발표·행사 공개 안내 성격이 강해 기술적 실무 적용점이 부족하므로 분류 대상에서 제외합니다. |
| d2/8992409 | 1,342 | 추출/기술 선택·도입형 | 1 | DBT와 Airflow를 활용해 온디맨드 데이터 계보 중심 파이프라인(Flow.er)을 설계·구현하고 PoC, 구성 요소, DBT/Airflow의 역할, CI/CD, 운영 개선(Manager DAG 개선, Partition Checker 등) 및 확장 전략을 상세히 다루고 있어 다른 팀의 설계·구현 판단에 직접 참고 가능한 구체적 실무 내용이 포함되어 있음. |
| d2/9290861 | 796 | 추출/기술 선택·도입형 | 1 | VictoriaMetrics의 수집·라우팅·저장·쿼리 구성과 내부 동작, ingestion 파이프라인과 성능 관점의 Best/Worst case 등을 다루어 분산 메트릭 인프라 설계·도입 판단에 참고 가능한 구체적 기술 내용이 포함되어 있음. |
| kakao/624 | 787 | 제외/회고·문화·행사 | 0 | 발표 영상과 발표자 인터뷰를 소개하는 행사·공유성 글입니다. 제목에 'CASE STUDY'가 있으나 본문에는 구체적인 기술적 문제 해결 과정, 설계 결정, 적용 방법 또는 수치적 근거 등 실무에 참고할 만한 기술적 세부 내용이 포함되어 있지 않습니다. 따라서 기술 사례 데이터베이스에 수록할 실무적 내용은 추출할 수 없습니다. |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | 0 | 사내 간식 설문 결과와 추천 패키지를 소개하는 회고/문화성 글로, 기술적 문제 해결 과정·설계 판단·도구 적용 방법 등 실무에 참고할 만한 구체적 기술 내용이 없음. |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | 0 | 오픈소스 기여 경험과 채용·성장 스토리를 공유하는 인터뷰/회고 형식의 콘텐츠입니다. 라이브러리 목록과 기여 동기·커뮤니티 중요성 등을 다루지만, 구체적인 설계·구현 결정, 설정·워크플로우·문제 해결 사례나 수치·비교 같은 기술적 실무 정보는 포함되어 있지 않습니다. 따라서 설계 판단에 참고할 실무 사례로는 적합하지 않습니다. |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | 0 | 조직·리더십 성장과 개인 경험을 다루는 인터뷰/회고 콘텐츠로, 기술적 설계·도입·문제 해결이나 구체적 실무 적용(설정·워크플로·수치 등)이 포함되어 있지 않음. 따라서 다른 팀의 설계·구현 판단에 참고할 만한 기술적 실무 정보가 없음. |

## 글당 항목 수 (제외 글 빼고)

| 항목 수 | 글 수 |
| --- | --- |
| 1 | 55 |
| 2 | 2 |
| 3 | 2 |
| 4 | 1 |

## 문제 유형 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 개발 생산성 | 37 | 54% |
| 데이터 정합성·트랜잭션 | 13 | 19% |
| 모니터링·관측성 | 12 | 17% |
| 메시징·비동기 처리 | 11 | 16% |
| 데이터 파이프라인 | 9 | 13% |
| 장애 대응·복구 | 9 | 13% |
| 배포·CI/CD | 9 | 13% |
| 클라이언트 성능(웹·앱) | 7 | 10% |
| 인프라·컨테이너 | 7 | 10% |
| 트래픽 급증 대응 | 6 | 9% |
| 비용 절감 | 5 | 7% |
| 인증·보안 | 5 | 7% |
| DB 성능·쿼리 최적화 | 5 | 7% |
| 캐싱 | 4 | 6% |
| 업무·운영 자동화 | 4 | 6% |
| 동시성·락 | 3 | 4% |
| DB 마이그레이션·샤딩 | 2 | 3% |
| 테스트 자동화 | 2 | 3% |
| API 설계·외부 연동 | 2 | 3% |

- 쏠림(30% 초과): 개발 생산성
- 한 번도 안 쓰인 분류 (1개): MSA

## 도메인 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 사내 플랫폼·개발 도구 | 41 | 59% |
| 검색·추천 | 10 | 14% |
| 커머스·주문·재고 | 10 | 14% |
| LLM·AI | 9 | 13% |
| 범용 | 7 | 10% |
| 배달·물류 | 3 | 4% |
| 결제·금융 | 2 | 3% |
| 콘텐츠·미디어 | 2 | 3% |
| 광고·마케팅 | 1 | 1% |

- 쏠림(30% 초과): 사내 플랫폼·개발 도구
- 한 번도 안 쓰인 분류 (1개): 채팅·메시징 서비스

## 발췌 검증

- 채택한 시도 기준 발췌 641개 중 탈락 9개 (원문 존재율 99%)
- 재시도한 글 18편

- `d2/4555524`: JuiceFS의 성능은 기본적으로는 데이터 스토리지를 사용하는 저장소의 성능에 수렴한다.
- `kakaopay/kakaopayins-opensearch-analyzer`: "char_filter": {
  "remove_whitespace": {
    "type": "pattern_replace",
    "pattern": """\s+""",
    "replacement": ""
  },
  "remove_special_chars": {
    "type": "pattern_replace",
    "pattern": "[^a-zA-Z0-9가-힣]",
    "replacement": ""
  }
},
- `kakaopay/kakaopayins-opensearch-analyzer`: "tokenizer": {
  "ngram_tokenizer": {
    "type": "ngram",
    "token_chars": [
      "letter",
      "digit"
    ],
    "min_gram": "1",
    "max_gram": "20"
  }
}
- `kakaopay/pallas-v2-log-platform`: 기존 OpenSearch(Elasticsearch)는 전문 검색(Full-text) 에는 강하지만, 우리 상황에서는 여러 문제가 있었어요.
- `ly/extracting-trending-keywords-from-openchat-messages`: 검토 결과 다양성이 충분히 확보되는 편이 바람직하다고 의견이 모여 페널티 가중치가 2 이상인 구간에서 α값을 결정했습니다.
- `toss/toss-frontend-ai-docs`: 실록봇은 대화 스레드에 실록봇 이모지를 붙이거나 봇을 호출하면 AI가 대화를 분석하고 요약해서 PR을 올려요.
- `toss/ads_dashboard_fe`: 현재 최대 데이터

2만 건

데이터가 가장 많은 광고계정 기준

설계 목표

10만 건

현재 최대치의 5배 여유
- `toss/ads_dashboard_fe`: 그래서 데이터와 연산을 통째로 Web Worker로 보냈습니다.
...
→ 그래서 초기 데이터는 응답을 res.arrayBuffer()로 받아 Transferable(ArrayBuffer)로 소유권만 넘깁니다. 메인 스레드는 본문을 파싱조차 하지 않아요.
- `woowahan/21027`: pre filter라고 부르는데요. 먼저 조건 필터를 통해 우리가 원하는 대상을 축소한 다음에 후보군에 대해 벡터 유사도 검색을 통해 랭킹을 지정하는 것을 의미합니다.

## 기술 사전에 없는 이름 177종

- Jira (4)
- Vite (3)
- WECAN (3)
- Figma (2)
- GitHub (2)
- SWC (2)
- Webpack (2)
- Web Worker (2)
- LLM (2)
- Node2Vec (2)
- Transformer (2)
- Milvus (2)
- Locust (2)
- Netty (2)
- Storybook (2)
- esbuild (2)
- Rollup (2)
- Hive (2)
- Nexus (2)
- XBU (2)
- Confluence (2)
- HDFS (2)
- OKLCH (1)
- Token Studio (1)
- Style Dictionary (1)
- CSS (1)
- ESBuild (1)
- react-refresh (1)
- Metro (1)
- WebSocket (1)
- MIG (1)
- MPS (1)
- nvidia-device-plugin (1)
- dcgm-exporter (1)
- nvidia-smi (1)
- ArrayBuffer (1)
- Transferable (1)
- HTML (1)
- ARIA (1)
- DOM API (1)
- WASM (1)
- Rust (1)
- Bun (1)
- V8 (1)
- JavaScriptCore (1)
- LTE 라우터 (1)
- IPSEC (1)
- S2 (1)
- fastutil (1)
- AWS ALB (1)
- Hazelcast (1)
- Chronicle-map (1)
- pgvector (1)
- Virtual Thread (1)
- ForkJoinPool (1)
- Canva (1)
- Spring Cloud Bus (1)
- Athena (1)
- Vector DB (1)
- Codex (1)
- Kanana-2 (1)
- MLA (1)
- MoE (1)
- v0 (1)
- Supabase (1)
- Vercel (1)
- IntelliJ (1)
- Claude API (1)
- Parcel (1)
- Rsbuild (1)
- Jest (1)
- Vitest (1)
- Babel (1)
- MiniCssExtractPlugin (1)
- AWS KMS (1)
- reach.tech (1)
- Apache Lucene (1)
- Mongo (1)
- InfluxDB (1)
- GCP (1)
- HyperDX (1)
- ssak3 (1)
- Filebeat (1)
- Parquet (1)
- ZSTD (1)
- 로켓단 (1)
- Wallga (1)
- 닥터 핌 (1)
- Catalog (1)
- Developer Desk (1)
- VictoriaMetrics (1)
- vmagent (1)
- vminsert (1)
- vmstorage (1)
- vmselect (1)
- CMDB (1)
- Spinnaker (1)
- Mocking Platform (1)
- DBT (1)
- Flow.er (1)
- C++ (1)
- react-window (1)
- react-virtualized (1)
- @tanstack/react-virtual (1)
- ResizeObserver (1)
- IndexedDB (1)
- table (1)
- datasource-proxy (1)
- Release Please Action (1)
- repository_dispatch (1)
- Dokka (1)
- Ruler (1)
- JFrog Artifactory (1)
- Maven Central (1)
- GitHub Pages (1)
- 다국어 음차 변환 (1)
- 번역 모델 (1)
- 이미지 검색 (1)
- CLOUS3.0 (1)
- JuiceFS (1)
- nubes (1)
- CSI Driver (1)
- MinIO (1)
- Iceberg (1)
- Sudachi (1)
- Kuromoji (1)
- ICU (1)
- Android (1)
- iOS (1)
- Xcode (1)
- WebAuthn (1)
- CTAP (1)
- Secure Enclave (1)
- Android StrongBox (1)
- ARM TrustZone (1)
- client-go (1)
- Informer (1)
- kube-apiserver (1)
- etcd (1)
- Vector (1)
- node_exporter (1)
- kube-state-metrics (1)
- Hubot (1)
- Ansible (1)
- Harbor (1)
- hubot-conversation (1)
- Taskmaster (1)
- Notion (1)
- Git (1)
- BigQuery (1)
- Google Sheets (1)
- MobX (1)
- Material-UI (1)
- vite-plugin-babel (1)
- @vitejs/plugin-react (1)
- qs (1)
- react-csv (1)
- dayjs (1)
- 행정안전부 도로명주소 API (1)
- 행정안전부 좌표정보 API (1)
- mysql-connector-j (1)
- MemoryAnalyzer (1)
- jmap (1)
- BERT4Rec (1)
- mlflow (1)
- Gradio (1)
- mitmproxy (1)
- OffscreenCanvas (1)
- MariaDB Connector/J (1)
- MySQL Aurora (1)
- Spring Data MongoDB (1)
- Yarn (1)
- Jotai (1)
- Panda CSS (1)
- AWS ECR (1)
- Tokens Studio For Figma (1)
- token-transformer (1)

## 버린 대안 68개 (항목 69개 중)

- `case_0001` 부분적 팔레트 수정: 일부 색만 수정하면 팔레트 전체와 다크모드까지 고려해야 해서 문제 해결이 불충분함
- `case_0003` MPS: 관리 부담과 격리 어려움으로 운영 리스크가 컸기 때문에 선택하지 않음
- `case_0003` 혼합 GPU 운영: 장기적으로 수요 편중으로 자원 낭비가 발생할 수 있어 운영 리스크가 존재함
- `case_0003` 클라우드 GPU 인스턴스: 지속적이고 자체 클러스터가 있는 환경에서는 오히려 비용이 더 발생할 수 있음
- `case_0004` Virtual Scrolling: 한 번에 그리는 건 100행이라 DOM 부하가 병목이 아니고, UX가 수천 행을 한 화면에 펼치는 모양이 아니었음
- `case_0004` IndexedDB 캐싱: 무효화 규칙 불명확, 세션만으로도 요구 해결, 버전 관리·스키마 마이그레이션 등 부수 비용으로 기각
- `case_0007` 코드 난독화: 변수 이름 치환과 로직 섞기 등은 속도 지연만 줄 뿐 매크로를 막지 못했다.
- `case_0007` 프로그래스바 기반 입력 난이도: 정밀한 타이밍 요구 방식도 매크로로 우회되었다.
- `case_0007` 클라이언트 CAPTCHA: 클라이언트에서 요구하는 시각 인식형 방어는 게임의 본질을 훼손했고 결국 게임 재미를 잃게 했다.
- `case_0007` ZK-SNARK: 우아팝에 적용하기에는 적절하지 않다고 판단했다.
- `case_0008` Item2Vec: 동일 주문 동시 출현 기반으로 대체재 편향과 시퀀스 맥락 부재 발생
- `case_0009` 통합 그래프/임베딩: 셀러 타입 간 데이터·구매 패턴 차이를 반영하지 못함
- `case_0010` 에그: 운영 비용(사용자 교육·네트워크 관리 비용)과 모니터링 트래픽 과금 문제로 인해 에그 대신 사업자 위탁의 LTE 라우터를 선택했다.
- `case_0011` 캐시 레이어 (Redis): 캐시 레이어 도입은 범용적인 설계지만 비용 증가와 작업량이 많아 우선 도입하지 않았다.
- `case_0011` Hazelcast: 분산 in-memory 데이터 그리드는 기능이 과하고 진입 장벽·이해도 문제가 우려되어 도입하지 않았다.
- `case_0011` Chronicle-map: 힙 외부 저장 등 장점이 있으나 기능이 과하다고 판단하여 도입하지 않았다.
- `case_0012` Milvus: 1차 실험 후보였으나 2차(부하) 실험 대상에서 제외되어 운영·성능 관점에서 최종 후보에 들지 못함.
- `case_0012` Redis: 1차 실험 후보였으나 2차 실험 대상에서 제외되어 운영·성능 관점에서 최종 후보에 들지 못함. **(technologies에도 있음)**
- `case_0012` Pinecone: 외부 fully-managed 전문 솔루션은 도입 비용·계약 이슈 때문에 1차 우선 검증 대상에서 제외함.
- `case_0013` Kotlin coroutine: 프로덕션 코드 변경과 suspend 전파(함수 색 문제) 등 도입 비용이 존재함.
- `case_0013` Reactive (WebFlux/Netty): 컨텍스트 스위칭 시 실제 스레드 전환에 따른 성능 낭비와 스택 트레이스 유실 등 디버깅/복잡성 문제가 있음.
- `case_0020` Cursor: 초보자나 비개발자가 1시간 안에 사용법을 익히고 의미 있는 성과를 내기엔 진입장벽이 높다고 판단했습니다.
- `case_0020` Claude Code: 초보자나 비개발자가 1시간 안에 사용법을 익히고 의미 있는 성과를 내기엔 진입장벽이 높다고 판단했습니다.
- `case_0022` Parcel: 프로젝트 복잡성 때문에 Zero-config 자동화가 리스크로 판단되어 최종 선택에서 제외됨
- `case_0022` Rsbuild: 생태계 규모가 작아 실서비스 적용 시 지원이 부족하다고 판단되어 최종 선택에서 제외됨
- `case_0023` Entity LifeCycle 콜백: 조회 시 PostLoad에서 복호화 후 1차 캐시에 저장되면서 계속 update가 발생하는 등 예측하기 어려운 부작용이 있어 사용하지 않음.
- `case_0027` Grafana Loki: 라벨 기반 제약과 집계 기능 한계로 우리 요구에 부적합
- `case_0027` Signoz: 자체 스키마 강제와 LogAttributes Map 접근 제한으로 ClickHouse 설계 장점을 활용할 수 없음
- `case_0036` reinterpret_cast로 직접 값 타입 퍼닝: 객체를 다른 타입으로 재해석하기 위해 reinterpret_cast로 포인터를 변환해 역참조하면 엄격한 앨리어싱 규칙을 위반하여 UB가 된다.
- `case_0036` union을 이용한 타입 퍼닝: C에서는 허용되지만 C++에서는 비활성 멤버를 읽는 것이 미정의 동작이므로 표준적인 해결책이 아니다.
- `case_0038` ChainedTransactionManager: 분산 트랜잭션 또는 ChainedTransactionManager로 MySQL을 트랜잭션에 포함시키지 않기로 함(마이그레이션 초기에는 두 DB 정합성이 보장되지 않고 MySQL 쿼리 실패가 빈번할 수 있기 때문).
- `case_0038` MyBatis 별도 Repository 호출: 모든 쓰기 로직에 별도 MyBatis 리포지토리 호출을 추가하면 수백·수천 곳의 코드 수정이 필요해 위험하고 비효율적이라 중앙화 방식을 선택함.
- `case_0043` Elasticsearch ← Elastic Search: 검색 엔진을 기존 Elastic Search에서 네이버 자체 검색 엔진 Nexus로 전환
- `case_0044` 온콜 알람 반영: 온콜에서 수신하는 알람을 그대로 반영하는 방식은 CUJ 기반의 사용자 경험 판단 기준과 일치하지 않다고 보았다.
- `case_0044` 오류 예산 기반 표현: 오류 예산 기반 표현보다 CUJ 관점의 SLI/SLO 달성 여부로 상태를 표현하는 것이 사용자 경험 판단에 적합하다고 판단했다.
- `case_0045` Alluxio: POSIX 일부 미지원 등으로 AiSuite 요구를 만족하지 못함
- `case_0045` DDN EXAScaler: 요구사항 만족하지만 도입비용이 큼
- `case_0045` Ceph-rbd: 동시 다중 Pod 접근 불가
- `case_0045` NFS: 확장성·HA 문제
- `case_0046` Spark Streaming: 마이크로 배치 특성으로 이벤트타임 기반 상태 제어와 정확히 한 번 처리를 동시에 만족하기 어려움
- `case_0046` 네이티브 쿠버네티스 배포: 설정·운영 번거로움과 GitOps 기반 운영을 보장하기 어려움
- `case_0047` mecab-ipadic-neologd: 운영 중인 Elasticsearch 7.10.2 환경에서는 최신 MeCab 기반 사전을 적용하는 데 제약이 있었다.
- `case_0047` Elasticsearch 업그레이드: 사내 플랫폼이 Elasticsearch 7.10.2까지만 지원하고 일몰 방향이라 업그레이드는 현실적 대안이 아니었다.
- `case_0048` WebAuthn Level 3 / Passkey: Level 3 스펙은 초안 상태이며 Passkey 동기화 제어 문제로 현재 채택하지 않음
- `case_0048` WebAuthn Level 3 / Passkey (동기화 관련): Passkey 동기화 제어 불가로 인해 비즈니스 제약이 발생할 수 있어 채택 보류
- `case_0049` Python client: Python 클라이언트에서는 가까운 시일 안에 Informer를 사용할 수 없다고 판단했고, 번거로운 작업이기는 하나 서버의 성능 향상을 위해 API 서버의 구현 언어를 Python에서 Go로 변경하고... 재구현하는 작업을 진행했습니다.
- `case_0049` Redis: Redis 등을 사용해 억지로 etcd에 대한 로컬 캐시를 유지할 필요가 없다고 판단했다.
- `case_0050` 블랙리스트 기반 필터링: 미리 지정하기 어려운 관련 단어들이 걸러지지 못함
- `case_0054` AI가 직접 외부 시스템 조회 (MCP): 가져온 텍스트가 모두 토큰 비용으로 계산되어 비용·속도 문제 발생
- `case_0055` nginx 설정: 개발팀에 권한이 없어 적용 불가
- `case_0055` RDBMS에만 의존: RDBMS 장애 시 메타데이터 등록 불가
- `case_0056` nginx 설정을 통한 접근 차단: 인프라 구조상 nginx 설정을 통해 접근을 차단하는 방식은 적합하지 않음
- `case_0056` BigQuery에 매 요청 직접 조회: 분석용 DB 특성상 레이턴시가 높아 매 요청 쿼리는 성능 저하 유발
- `case_0057` 메모리 증설: 임시방편으로 메모리를 계속 늘리는 것은 근본 해결이 되지 않음
- `case_0057` Parcel: 커스텀 제약으로 레거시 요구를 맞추기 어려움
- `case_0057` Rsbuild: 생태계가 작아 도입 리스크가 있었다
- `case_0059` max-lifetime 늘리기: Connection 재생성 속도를 줄여 AbandonedConnectionCleanupThread의 처리 부담을 낮출 수 있으나, 컬리로는 빠른 DB failover를 위해 max-lifetime을 짧게 유지하고자 했다.
- `case_0062` Chrome overwrite contents: 필드 값이 많으면 하나하나 수동으로 수정하며 테스트하는 번거로움이 있습니다.
- `case_0062` 프록시 툴(Charles/Fiddler): 필드 값이 많으면 하나하나 수동으로 수정하며 테스트하는 번거로움이 있습니다.
- `case_0062` 데이터 수정: API가 어떨 때 null 값을 넘겨주는지까지는 정의되지 않았기 때문에 데이터 수정으로 null을 넘겨주기는 어렵다고 판단했습니다.
- `case_0063` WebP 변환: 복잡한 이미지에서는 압축 효율이 낮아 실용적이지 않았다
- `case_0063` 메인 스레드 Canvas 처리: Canvas 리사이징을 메인 스레드에서 실행하면 JS 블로킹과 클릭 이벤트 지연 등 UI 응답성 저하를 초래했다
- `case_0065` 잠금 읽기 (LOCK IN SHARE MODE): 잠금 읽기는 최신 데이터를 보장하지만 행 잠금으로 인해 락 경합 및 데드락 위험이 있어 채택하지 않음.
- `case_0066` WriteConcern MAJORITY: 이 방법은 정확성을 높일 수 있지만, 모든 요청에 대해 Secondary 과반수 ACK 응답을 기다리면 큰 오버헤드를 발생시킬 수 있습니다.
- `case_0066` ReadPreference PRIMARY (글로벌 설정): PRIMARY만을 우선하는 설정은 SECONDARY가 유휴 상태로 남아 리소스를 낭비할 수 있어 완벽한 해결책이 되지 않는다.
- `case_0067` 메시지 지연 전달: 지연 시간이 너무 짧다면 타이밍 문제가 여전히 발생할 수 있어 임시방편에 불과하다.
- `case_0067` Outbox 패턴: 설계 및 구현에 걸리는 시간과 비용이 부담되어 당장 적용하기에는 과한 솔루션이라고 판단했다.
- `case_0069` EAI I/F: 배치 기반과 단일 어댑터로 인한 지연 및 장애 전파 문제 때문에 대체했다.

## 글 목록

| 글 | 길이 | 결과 | 항목 | 발췌 탈락 | 제목 |
| --- | --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 제외/회고·문화·행사 | - | 0/0 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics |
| d2/4555524 | 18,452 | 추출/기술 선택·도입형 | case_0045 | 1/23 | AI 플랫폼을 위한 스토리지 JuiceFS 도입기 |
| d2/8366976 | 3,331 | 추출/문제 해결형 | case_0040, case_0041, case_0042, case_0043 | 0/18 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/3814947 | 16,662 | 추출/실험·활용기 | case_0039 | 0/12 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | - | 0/0 | Thread-safety in C++ |
| d2/1450243 | 15,218 | 추출/문제 해결형 | case_0037 | 0/9 | 윈도잉(windowing) 기법을 적용한 고성능 표 컴포넌트 개발기 |
| d2/8992409 | 1,342 | 추출/기술 선택·도입형 | case_0035 | 0/7 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| d2/6512234 | 22,022 | 추출/기술 선택·도입형 | case_0038 | 0/17 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/1155434 | 9,048 | 추출/실험·활용기 | case_0036 | 0/9 | C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가 |
| d2/9290861 | 796 | 추출/기술 선택·도입형 | case_0031 | 0/3 | Inside VictoriaMetrics |
| kakao/601 | 3,137 | 제외/회고·문화·행사 | - | 0/0 | 제3회 Kakao Tech Meet 후기 - 불확정성에서 감동까지 |
| kakao/624 | 787 | 제외/회고·문화·행사 | - | 0/0 | 카카오의 스팸 메일 대응 전략: 문자열 변형 CASE STUDY / 제6회 Kakao Tech Meet |
| kakao/761 | 3,645 | 제외/회고·문화·행사 | - | 0/0 | 실패를 장려하는 실험적 문화 |
| kakao/762 | 13,811 | 추출/실험·활용기 | case_0021 | 0/7 | 생산성 혁신의 실험: AI 마일리지 프로그램 |
| kakao/770 | 16,500 | 추출/기술 선택·도입형 | case_0022 | 0/11 | 5년 된 프로젝트의 빌드 도구를 교체하며 얻은 것들 |
| kakao/784 | 8,710 | 추출/실험·활용기 | case_0020 | 0/10 | 단 1시간 만에 99개의 MVP가? AI와 함께한 1K: 바이브코딩전 생생 후기 |
| kakao/785 | 4,597 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며 |
| kakao/804 | 3,760 | 추출/기술 선택·도입형 | case_0019 | 0/9 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/822 | 20,047 | 추출/실험·활용기 | case_0018 | 0/10 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakao/835 | 12,198 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 둘째 날, 기술 세션 소개 |
| kakaopay/slack-bot-improving-operational-efficiency-2 | 5,044 | 추출/기술 선택·도입형 | case_0033 | 0/8 | 카카오페이 배포 효율화 1년 회고: 자동화 도입과 팀 생산성 향상 |
| kakaopay/tech-strategy-tpm | 9,673 | 추출/회고·문화·행사 | case_0032 | 0/7 | 카카오페이 TPM은 어떤 일을 하나요? |
| kakaopay/katfun-joy-kotlin | 14,709 | 추출/실험·활용기 | case_0034 | 0/11 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kakaopay/ifkakao2024-devrel | 10,598 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스 준비 맛보기 |
| kakaopay/perftest_zone | 4,708 | 추출/기술 선택·도입형 | case_0026 | 0/9 | 카카오페이 성능 테스트 존을 소개합니다. |
| kakaopay/kakaopaysec-wecan | 8,650 | 추출/기술 선택·도입형 | case_0028, case_0029, case_0030 | 0/11 | We Can Do Better: 개발자 플랫폼 효율화 이야기 |
| kakaopay/kakaopayins-opensearch-analyzer | 10,157 | 추출/실험·활용기 | case_0025 | 2/10 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/kakaopayins-envelope-encryption | 18,389 | 추출/실험·활용기 | case_0023 | 0/9 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/pallas-v2-log-platform | 25,659 | 추출/기술 선택·도입형 | case_0027 | 1/17 | 일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트 |
| kakaopay/kakaopayins-fe-common-component | 7,059 | 추출/기술 선택·도입형 | case_0024 | 0/8 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kurly/cart-recommend-model-development | 9,206 | 추출/실험·활용기 | case_0061 | 0/9 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 1부 |
| kurly/commit-mvcc-set-autocommit | 16,463 | 추출/문제 해결형 | case_0065 | 0/10 | 데이터가 있었는데요, 아니 없어요 |
| kurly/deliveryproductteam-culture-1 | 4,454 | 추출/실험·활용기 | case_0060 | 0/7 | 딜리버리 프로덕트 개발팀의 개발문화 - 로그 & 알람편 |
| kurly/connection-leak | 6,791 | 추출/문제 해결형 | case_0059 | 0/8 | 99%가 모른다는 DB Connection 누수 문제 |
| kurly/refine-address-internalization-2 | 4,312 | 추출/기술 선택·도입형 | case_0058 | 0/8 | 주소정제 서비스 내재화 - 2화 ( 그럴싸한 계획 ) |
| kurly/access-block-1 | 5,663 | 추출/문제 해결형 | case_0055 | 0/12 | nginx 설정 없이 우아하게 서비스 점검하기 (上) |
| kurly/access-block-2 | 8,383 | 추출/기술 선택·도입형 | case_0056 | 0/13 | nginx 설정 없이 우아하게 서비스 점검하기 (下) |
| kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0 | 13,290 | 추출/기술 선택·도입형 | case_0057 | 0/14 | 빌드가 터졌다: 5년 된 CMS 프로젝트의 Webpack4 → Vite 전환 |
| kurly/tech-spec-adoption-with-ai-automation | 8,164 | 추출/기술 선택·도입형 | case_0053 | 0/9 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| kurly/claude-code-redesign-my-day | 7,389 | 추출/기술 선택·도입형 | case_0054 | 0/8 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| ly/managing-multi-cdn-logs-traffics-with-vector | 16,695 | 추출/실험·활용기 | case_0051 | 0/9 | Vector를 활용해 멀티 CDN 로그 및 트래픽 관리하기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 18,813 | 추출/기술 선택·도입형 | case_0052 | 0/12 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/improving-kubernetes-relay-api-server-performance-with-informer | 12,361 | 추출/기술 선택·도입형 | case_0049 | 0/11 | Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기 |
| ly/introducing-fido2-client-sdk-open-source | 9,957 | 추출/기술 선택·도입형 | case_0048 | 0/8 | FIDO2 클라이언트 SDK 오픈소스 소개 |
| ly/how-to-evaluate-ai-generated-images-1 | 16,708 | 제외/개념·튜토리얼 | - | 0/0 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/extracting-trending-keywords-from-openchat-messages | 14,017 | 추출/실험·활용기 | case_0050 | 1/10 | 오픈챗 메시지들로부터 트렌딩 키워드 추출하기 |
| ly/pd1-ai-hackathon-recap | 4,153 | 제외/회고·문화·행사 | - | 0/0 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 6,232 | 추출/기술 선택·도입형 | case_0044 | 0/11 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 및 서비스 상태 확인 도구 LINE Status 개발기 |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 19,601 | 추출/기술 선택·도입형 | case_0046 | 0/14 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/japanese-search-kuromoji-to-sudachi | 15,395 | 추출/기술 선택·도입형 | case_0047 | 0/12 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자가 좋아하는 과자는? |
| oliveyoung/2024-06-05_google-cloud-next-24-review | 3,796 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next '24 방문기 |
| oliveyoung/2024-08-11_type-and-type-system-with-typescript | 11,673 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 타입과 타입 시스템 |
| oliveyoung/2024-09-30_oy-feconf-2024 | 8,894 | 제외/회고·문화·행사 | - | 0/0 | 올리브영에서는 프론트엔드 개발자들이 이런 고민을 하는군요? |
| oliveyoung/2024-10-17_oy-delivery-mq | 4,642 | 추출/기술 선택·도입형 | case_0069 | 0/8 | 올리브영 물류시스템에서는 데이터를 어떻게 주고 받을까? |
| oliveyoung/2024-12-16_Design-System-Token-Automation | 17,955 | 추출/실험·활용기 | case_0068 | 0/8 | 디자인 시스템 중 디자인 토큰을 여러 도구를 이용하여 자동화 하는 방법 |
| oliveyoung/2024-12-17_catalog-mongo-transaction-2 | 11,450 | 추출/문제 해결형 | case_0066, case_0067 | 0/15 | Spring Boot MongoDB 트랜잭션 도입 실전 가이드 |
| oliveyoung/2025-02-14_oy-global-mall-address | 4,978 | 추출/기술 선택·도입형 | case_0064 | 0/9 | 올리브영 글로벌몰 주소 자동완성 및 검증 솔루션 도입기 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 7,158 | 추출/문제 해결형 | case_0063 | 0/8 | Web Worker로 이미지 처리 최적화하기 |
| oliveyoung/2025-06-10_chaos | 7,289 | 추출/실험·활용기 | case_0062 | 0/10 | 버그가 아니라 장애를 잡아라!! QA와 카오스 엔지니어링의 만남 |
| toss/27752 | 5,980 | 추출/실험·활용기 | case_0005 | 0/8 | 드래그 앤 드롭은 사실 편한 UX가 아니다? |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | - | 0/0 | 오픈소스에 기여하고 토스에 합격한.ssul \| EP.4 모닥불 |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | - | 0/0 | 개발자 리더로서 성장당한 썰 \| EP.7 모닥불 |
| toss/toss-frontend-ai-docs | 2,869 | 추출/기술 선택·도입형 | case_0006 | 1/7 | 토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유 |
| toss/toss-people-3 | 7,801 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 문과생에서 토스 개발 리더까지 |
| toss/frontend-esbuild-hmr | 10,415 | 추출/실험·활용기 | case_0002 | 0/10 | ESBuild를 위한 HMR, 직접 만들기 |
| toss/frontend-apply-without-resume | 2,783 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드에 이력서 없이 리포지토리 링크로 지원하세요 (~5/31) |
| toss/toss-securities-gpu-mig | 13,794 | 추출/기술 선택·도입형 | case_0003 | 0/10 | GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기 |
| toss/tds-color-system-update | 13,423 | 추출/기술 선택·도입형 | case_0001 | 0/9 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| toss/ads_dashboard_fe | 12,467 | 추출/실험·활용기 | case_0004 | 2/14 | 전체 데이터를 브라우저에 두는 광고 대시보드 만들기 |
| woowahan/14484 | 5,518 | 추출/문제 해결형 | case_0014 | 0/7 | “일단 백로그에 넣어두고 여유 있을 때 보는 걸로 할까요?” : 백로그를 백로그로 두지 않는 법 |
| woowahan/14671 | 6,108 | 제외/회고·문화·행사 | - | 0/0 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/15398 | 10,772 | 추출/실험·활용기 | case_0013 | 0/13 | Java의 미래, Virtual Thread |
| woowahan/15541 | 6,445 | 제외/개념·튜토리얼 | - | 0/0 | 웹 접근성 준수를 통한 모두에게 배달되는 일상의 행복 |
| woowahan/17386 | 11,245 | 추출/실험·활용기 | case_0015, case_0016, case_0017 | 0/21 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/17911 | 4,799 | 추출/문제 해결형 | case_0010 | 0/7 | B마트 주문 유실을 없애보자: 네트워크 편 |
| woowahan/20763 | 8,615 | 추출/기술 선택·도입형 | case_0011 | 0/13 | 이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기 |
| woowahan/21027 | 25,102 | 추출/기술 선택·도입형 | case_0012 | 1/10 | 실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법 |
| woowahan/24434 | 15,179 | 추출/문제 해결형 | case_0008, case_0009 | 0/19 | “함께 구매하면 좋은 상품” 추천 모델 고도화 |
| woowahan/24999 | 12,341 | 추출/문제 해결형 | case_0007 | 0/15 | WOOWACON 2025 미니게임 WOOWA POP! |
