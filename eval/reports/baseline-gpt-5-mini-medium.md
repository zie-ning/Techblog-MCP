# 추출 점검 리포트: baseline-gpt-5-mini-medium

- 모델: gpt-5-mini (medium)
- 프롬프트 버전: d2178d29df58
- 글 80편: 사례 62, 인사이트 2, 제외 16
- 항목 95개: 사례 93, 인사이트 2
- 토큰: 호출 171회, 입력 1,224,405 (캐시 431,872), 출력 544,136 (reasoning 397,120)
- 비용: $1.297 (편당 $0.0162), 전체 1,262편 추정 $20.5 / Batch $10.2

## 블로그별 구조화 유형

| 블로그 | 사례 | 인사이트 | 제외 | 항목 수 |
| --- | --- | --- | --- | --- |
| d2 | 7 | 1 | 2 | 11 |
| kakao | 6 | 1 | 3 | 10 |
| kakaopay | 10 | 0 | 0 | 19 |
| kurly | 10 | 0 | 0 | 13 |
| ly | 8 | 0 | 2 | 13 |
| oliveyoung | 6 | 0 | 4 | 7 |
| toss | 6 | 0 | 4 | 8 |
| woowahan | 9 | 0 | 1 | 14 |

## 글 유형 × 구조화 유형

| 글 유형 | 사례 | 인사이트 | 제외 |
| --- | --- | --- | --- |
| 개념·튜토리얼 | 0 | 0 | 5 |
| 기술 선택·도입형 | 26 | 0 | 0 |
| 문제 해결형 | 16 | 0 | 0 |
| 실험·활용기 | 18 | 1 | 0 |
| 회고·문화·행사 | 2 | 1 | 11 |

## 짧은 글 (평문 1,500자 미만) 8편

| 글 | 길이 | 결과 | 항목 | 분류 이유 |
| --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 사례/문제 해결형 | 1 | Old Symbolicator의 기능·성능·리소스 한계를 문제로 제시하고, New Symbolicator의 알고리즘(핵심: Symbol Map File), SymbolFile CLI, 저비용 고효율 서버 아키텍처 등 구체적 해결책을 설명. 품질·성능·리소스 사용에 대한 비교와 결과(근거)가 포함되어 있어 구체적 사례에 해당함. |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | 0 | C++의 data race, sequenced-before, synchronizes-with 등 스레드 안전성 개념과 표준 라이브러리 동작을 정리하는 개념·튜토리얼 성격의 발표자료입니다. 특정 문제 해결이나 기술 도입 사례·근거를 다루지 않아 '제외'로 분류합니다. |
| d2/8992409 | 1,342 | 사례/실험·활용기 | 1 | 과거 파이프라인 문제를 해결하기 위해 DBT와 Airflow 기반의 on-demand 데이터 계보 파이프라인(Flow.er)을 설계·구현한 경험을 공유하는 글입니다. PoC, 구성요소, DBT/Airflow 역할, CI/CD, 확장 사례(Playground, Tower, Partition Checker) 등 구체적 설계와 운영·확장 근거가 제시되어 있어 실무 적용이 가능한 사례로 분류됩니다. |
| d2/9290861 | 796 | 인사이트/실험·활용기 | 1 | VictoriaMetrics의 수집·라우팅·저장·쿼리 구성과 운영 관점을 중심으로 내부 구조와 ‘좋은 수집 구조’ 원리를 설명하는 실무 적용형 글입니다. 구체적인 설계·운영 팁과 사례 위주이지만, 명시적인 문제-해법 쌍이나 정량적 근거(수치·비교)는 많지 않아 '사례'보다는 실무에 적용 가능한 인사이트를 제공하는 '인사이트' 유형으로 분류했습니다. |
| kakao/624 | 787 | 제외/회고·문화·행사 | 0 | 발표 영상과 발표자 인터뷰를 소개하는 행사 후기/공유성 글입니다. 본문에 구체적인 기술적 문제 해결 과정이나 도입·활용에 대한 실무적 사례·인사이트는 포함되어 있지 않습니다. |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | 0 | 사내 간식 설문 및 결과 공유로 조직 문화·이벤트 성격의 글입니다. 기술적 문제 해결이나 설계·도입 경험·실무 적용 인사이트가 없어 '제외'로 분류합니다. |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | 0 | 오픈소스 기여 경험과 채용 이야기를 인터뷰 형식으로 다루는 회고/경험담 중심 글로, 구체적인 기술 문제 해결이나 실무 적용 가이드(설계·수치 기반 비교 등)를 제공하지 않아 '제외'에 해당합니다. |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | 0 | 리더십 성장과 조직 문화에 대한 인터뷰/대담형 에피소드로, 기술적 문제 해결이나 도입·실무 적용에 대한 구체적 사례나 가이드를 담고 있지 않음. 따라서 회고·문화 성격의 글로 분류하여 제외로 처리함. |

## 글당 항목 수 (제외 글 빼고)

| 항목 수 | 글 수 |
| --- | --- |
| 1 | 45 |
| 2 | 8 |
| 3 | 10 |
| 4 | 1 |

## 주 문제 유형 분포

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 개발 생산성 | 22 | 23% |
| 업무·운영 자동화 | 9 | 9% |
| 캐싱 | 8 | 8% |
| 모니터링·관측성 | 7 | 7% |
| 배포·CI/CD | 6 | 6% |
| 클라이언트 성능(웹·앱) | 5 | 5% |
| 인증·보안 | 5 | 5% |
| 데이터 정합성·트랜잭션 | 5 | 5% |
| 데이터 파이프라인 | 5 | 5% |
| 인프라·컨테이너 | 4 | 4% |
| API 설계·외부 연동 | 4 | 4% |
| 장애 대응·복구 | 3 | 3% |
| 트래픽 급증 대응 | 3 | 3% |
| 메시징·비동기 처리 | 3 | 3% |
| DB 성능·쿼리 최적화 | 2 | 2% |
| 테스트 자동화 | 2 | 2% |
| 비용 절감 | 1 | 1% |
| DB 마이그레이션·샤딩 | 1 | 1% |

- 한 번도 안 쓰인 분류 (2개): 동시성·락, MSA

## 도메인 분포

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 사내 플랫폼·개발 도구 | 38 | 40% |
| 커머스·주문·재고 | 28 | 29% |
| LLM·AI | 7 | 7% |
| 범용 | 7 | 7% |
| 결제·금융 | 4 | 4% |
| 검색·추천 | 3 | 3% |
| 콘텐츠·미디어 | 3 | 3% |
| 채팅·메시징 서비스 | 3 | 3% |
| 광고·마케팅 | 1 | 1% |
| 배달·물류 | 1 | 1% |

- 쏠림(30% 초과): 사내 플랫폼·개발 도구
- 한 번도 안 쓰인 분류 (0개): 없음

## 발췌 검증

- 채택한 시도 기준 발췌 921개 중 탈락 25개 (원문 존재율 97%)
- 재시도한 글 27편

- `d2/3461887`: App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics
- `d2/3461887`: - 성능
- `d2/8366976`: '예시: '호텔 한큐 레스파이어 오사카'는 한국인 여행자들에게 인기가 많은 호텔인데요, 영문명인 'Hotel Hankyu Respire Osaka'를 흔히 '호텔 한큐 리스파이어 오사카'라고 읽기도 하지만 '리스파이어'라는 한글 키워드가 없기 때문에 '한큐 리스파이어 오사카'로는 검색할 수 없었습니다.'
- `d2/8366976`: '예시: 사용자가 '도쿄 야경 호텔'을 검색했을 때에는 대표 사진에 글자만 잔뜩 나열된 결과보다는 야경이 보이는 사진, 야경과 관련된 리뷰 등 관련도 높은 직관적인 정보를 원할 것이라고 생각했습니다.'
- `kakao/762`: '특정 도구로 기획하는데 연동된 AI 기능이 없어 도움이 되지 않았다'거나 '회사 배포 시스템과 AI가 연결돼 있지 않아 실수가 우려되어 사용하지 않았다'는 응답에서 보듯이, AI 도구가 기존 업무 환경과 통합되지 않을 때 효과가 제한됩니다.
- `kakao/762`: '설문 당시 도구 적응·셋업에 시간이 더 들었다'고 응답하는 이들도 있습니다.
- `kakao/762`: 'AI가 만든 코드는 영향 범위 파악이 어려워 리뷰 시간이 늘었다'거나 '실제 수정 작업은 수십 줄인데 AI가 작성한 테스트 코드 수백 줄을 검토해야 해서 부담이 증가했다'는 지적도 있었습니다.
- `kakaopay/tech-strategy-tpm`: 보안 제약 사항이 많아요. 마지막으로 제도적인 법 관련된 것도 확인해야 돼서 법무팀이랑도 일을 많이 해야 돼요.
- `kakaopay/tech-strategy-tpm`: 기술협의체는 2주 단위로 운영합니다. 기술협의체에서 논의되는 안건을 체계적으로 관리하고, 진행 상황을 명확하게 파악할 수 있는 방법을 고려합니다.
- `kakaopay/kakaopayins-fe-common-component`: - 이미 존재하는 컴포넌트를 조합해서 해결할 수는 없는지
- 지금은 공통이 아니다라고 말해도 괜찮은 시점은 아닌지
- 나중에 공통으로 옮겨도 문제가 없는 구조인지
- `kurly/commit-mvcc-set-autocommit`: 하지만 격리수준을 낮추는 경우에 Phantom Read 이슈가 발생하여 기존 비즈니스 로직에 영향을 주는 등의 사이드 이펙트를 고려하여 다른 해결방법을 찾아보기로 해요.
- `kurly/access-block-2`: API 호출에 대한 접근제어는 Spring AOP 를 활용해 RestController 로 들어오는 모든 요청을 인터셉트하여 선처리 합니다. 마찬가지로, 차단이 되면 안되는 API 도 있으니 @ExcludeAccessBlock 라는 어노테이션도 같이 생성하여, 해당 어노테이션이 선언되어 있는 클래스와 메서드는 Aspect 가 수행되지 않도록 합니다.
- `kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0`: 선택지는 두 가지였다. 메모리를 계속 늘리며 임시방편을 쓰거나, 번들러를 바꾸거나. 저희는 후자를 선택했습니다.
- `ly/introducing-fido2-client-sdk-open-source`: PublicKeyCredential은 WebAuthn Level 2 문서의 PublicKeyCredential 인터페이스를 구현한 것으로, 패스워드가 아닌 비대칭 키 쌍(asymmetric key pair)을 크리덴셜로 사용합니다. PublicKeyCredential 인터페이스는 사용자 등록 및 인증을 위해 WebAuthn Level 2 문서에 정의된 두 개의 API인 create와 get 메서드를 지원합니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 처음에는 관련 키워드를 모두 블랙리스트로 구성해서 이와 일치하거나 부분 문자열로 포함하는 단어는 트렌딩 키워드로 추출되지 않도록 만들어 봤습니다. 그랬더니 미처 예상치 못했던 단어들이, 예를 들어 오랜만에 경기가 열리는 지방 도시 이름이라던가 말이나 기수 또는 참가 팀 이름 등 미리 지정하는 게 사실상 불가능한 단어들이 걸러지지 못하고 추천 키워드로 추출됐습니다.
- `ly/japanese-search-kuromoji-to-sudachi`: 하나의 의미 단위로 취급되어야 할 상품명이 여러 토큰으로 분해되면서, 사용자의 검색 의도와 다른 결과가 매칭되거나 검색 정확도가 떨어지는 문제가 발생했습니다.
- `ly/japanese-search-kuromoji-to-sudachi`: 짧은 일본어 검색어에도 compact 필드를 함께 조회하면, 의도치 않은 상품이 포함될 수 있습니다.
- `ly/japanese-search-kuromoji-to-sudachi`: compact_product_name_analyzer는 이 문제를 tokenizer 선택으로 해결합니다. 인덱스 settings에 직접 정의한 커스텀 analyzer로, icu_normalizer → model_delim_to_space(커스텀 char_filter: -, _, / → 공백 변환) → punct_to_space(커스텀 char_filter: 나카구로·물결표 등 → 공백 변환) → collapse_spaces(커스텀 char_filter: 연속 공백  → 단일 공백)를 거친 뒤 whitespace tokenizer로 분리합니다.
- `ly/japanese-search-kuromoji-to-sudachi`: // 길이 > 3 글자 이고, 영숫자가 포함된 경우에만 compact 필드 추가
val isLongEnough = text.length > PRODUCT_NAME_MIN_LENGTH_FOR_COMPACT
val hasAsciiAlphaNum = text.any { c ->
        c in 'a'..'z' || c in 'A'..'Z' || c in '0'..'9'
}

if (isLongEnough && hasAsciiAlphaNum) {
        shouldQueries.add(compactMatchQuery(text))
}
- `ly/japanese-search-kuromoji-to-sudachi`: 카탈로그 매칭 작업에서 관리자는 상품명 전체를 기억하지 못하는 경우가 많습니다. 'スマートフォン(스마트폰)'이 들어간 카탈로그를 찾고 싶을 때 'スマ' 두 글자만 입력해도 후보가 나타나야 작업이 빠릅니다.
- `oliveyoung/2024-12-16_Design-System-Token-Automation`: 저희는 Panda CSS를 사용하고 있기에 Panda CSS Tokens 문서를 보고 Panda CSS가 지원하는 형태로 변경하는 과정을 거치기로 판단했습니다. 해당 토큰을 Panda CSS의 설정파일에 추가만 해주면 된다.
- `toss/toss-frontend-ai-docs`: 실록봇은 대화 스레드에 실록봇 이모지를 붙이거나 봇을 호출하면 AI가 대화를 분석하고 요약해서 PR을 올려요.
- `woowahan/20763`: 단점
– 캐시 레이어 관련 비용 발생
– 작업량이 많음
- `woowahan/20763`: D-6 (화) 06:30 ~ 07:00 | 1차 Canary 배포 후 롤백 | 1% 트래픽 설정
D-5 (수) 15:00 ~ 16:00 | 2차 Canary 배포 후 롤백 | 5% 트래픽 설정
... 
AWS ALB에 동시에 두 TargetGroup을 등록하고 트래픽을 세밀하게 조정할 수 있게끔 하였으며
이를 통해 문제 발생 시 최대 1분 내에 롤백할 수 있도록 대비하였습니다.
- `woowahan/24999`: 마지막으로, CAPTCHA 형태의 방어 로직이 추가되었습니다. 서버에서 변형된 동물 이미지를 내려주면 사용자는 변형되지 않은 이미지를 골라야지만 Level을 올릴 수 있었습니다.
... 
결과적으로 매크로 개발자는 사라졌습니다. 코드 분석만으로는 더이상 매크로를 만들 수 없어서 그런 걸 수도 있고 더이상 흥미를 잃어서일 수도 있습니다. 매크로는 막았지만, 게임의 재미는 크게 반감됐습니다. 레벨업 게임 본질의 단순함은 사라지고 동물 이미지를 맞추는 일만 남았습니다.

## 기술 사전에 없는 이름 380종

- Jira (4)
- Locust (3)
- 클로드 코드 (3)
- ESBuild (2)
- SWC (2)
- Webpack (2)
- Vite (2)
- Web Worker (2)
- LLM (2)
- Figma (2)
- Transformer (2)
- kanana-2-30b-a3b (2)
- ZSTD (2)
- 로켓단 (2)
- Hive (2)
- Dokka (2)
- HDFS (2)
- MariaDB (2)
- icu_normalizer (2)
- Confluence (2)
- DB (2)
- Git (2)
- NVIDIA MIG (1)
- MPS (1)
- nvidia-smi (1)
- nvidia-device-plugin (1)
- dcgm-exporter (1)
- H100 (1)
- A100 (1)
- H200 (1)
- react-refresh (1)
- WebSocket (1)
- Metro (1)
- res.arrayBuffer() (1)
- ArrayBuffer (1)
- Transferable (1)
- Structured Clone (1)
- HTTP 클라이언트 (1)
- IndexedDB (1)
- Virtual Scrolling (1)
- ARIA (aria-live, aria-pressed, aria-label, aria-hidden, aria-checked) (1)
- focus API (1)
- 박씨 (1)
- 실록봇 (1)
- 사내 메신저 (1)
- OKLCH (1)
- HSLuv (1)
- APCA (1)
- RGB (1)
- Token Studio (1)
- GitHub (1)
- Style Dictionary (1)
- @tds/token-utils (1)
- tokengen (1)
- CSS (1)
- Deus Variable Collection Schema (1)
- Server Driven Format (1)
- Token v1 (1)
- Token v2 (1)
- CLI (1)
- Deus (1)
- ShadowDOM (1)
- Variable Collection (1)
- Frontend Platform (1)
- Android (1)
- iOS (1)
- Server Driven UI (1)
- monorepo (1)
- peerDeps (1)
- Item2Vec (1)
- Node2Vec (1)
- Random Walk (1)
- SASRec (1)
- Multi-Task Learning (1)
- Focal Loss (1)
- Bayesian Smoothing (1)
- Epoch-wise Target Sampling (1)
- Metapath (1)
- Association Rule (1)
- Milvus (1)
- Redis Stack (1)
- Atlas MongoDB (Atlas Search) (1)
- HNSW (1)
- IVF_FLAT (1)
- pgvector (1)
- WASM (1)
- Rust (1)
- V8 (1)
- JavaScriptCore (1)
- Bun (1)
- reCAPTCHA (1)
- LTE 라우터 (1)
- IPSEC (1)
- DNS (1)
- DHCP (1)
- NTP (1)
- RADIUS (1)
- 에그 (1)
- Virtual Thread (1)
- JDK21 (1)
- JDK19 (1)
- Netty (1)
- ForkJoinPool (1)
- NIOSocketImpl (1)
- LockSupport (1)
- C++ (1)
- libevent(evhttp) (1)
- fastutil (1)
- AWS ALB (1)
- Hazelcast (1)
- chronicle-map (1)
- jstat (1)
- JDK 11 (1)
- MySQL source connector (1)
- Spring Cloud Bus (1)
- RemoteApplicationEvent (1)
- Spring Cloud (1)
- S3 싱크 커넥터 (1)
- AWS S3 (1)
- AWS Athena (1)
- 슬랙 워크플로 (1)
- IMR(Information Management Request) (1)
- 지라 (1)
- 칸반보드 (1)
- 스프레드시트 (1)
- 배민선물하기 (1)
- 배민 앱 (1)
- codex (1)
- promQL (1)
- bash (1)
- org.openjdk.jmh:jmh-core (1)
- ZGC (1)
- virtual thread (1)
- netty (1)
- JFR (1)
- async-profiler (1)
- jstack (1)
- heap dump (1)
- kanana-1.5-32.5b (1)
- Qwen3-30B-A3B-2507 (1)
- MLA (1)
- MoE (1)
- 토크나이저 (1)
- v0 (1)
- Supabase (1)
- Vercel (1)
- IntelliJ (1)
- Claude API (1)
- Parcel (1)
- Rsbuild (1)
- Rspack (1)
- Storybook (1)
- Babel (1)
- Rollup (1)
- MiniCssExtractPlugin (1)
- TerserPlugin (1)
- CssMinimizerPlugin (1)
- Vitest (1)
- Jest (1)
- babel-loader (1)
- Veo3 (1)
- Flowith (1)
- HyperDX (1)
- Filebeat (1)
- ssak3 (1)
- Parquet (1)
- Grafana Loki (1)
- Signoz (1)
- Amazon Athena (1)
- AWS KMS (1)
- ProfileCredentialsProvider (1)
- AttributeConverter (1)
- UserType (1)
- ParameterizedType (1)
- AES (1)
- RSA (1)
- StaticLabelTextArea (1)
- DelayRender (1)
- RenderAfter (1)
- KID (Kakaopay insurance Design) (1)
- CoverageSelectCard (1)
- reach.tech (1)
- Testcraft (1)
- k6 browser (1)
- InfluxDB (1)
- Mongo (1)
- GCP (1)
- WECAN (1)
- 인사시스템 (1)
- Wallga2 (1)
- Catalog (1)
- Platform Catalog (1)
- Developer Desk (1)
- 닥터 핌 (1)
- Apache Lucene (1)
- ngram tokenizer (1)
- OpenSearch Dashboards (1)
- VictoriaMetrics (1)
- vmagent (1)
- vminsert (1)
- vmstorage (1)
- vmselect (1)
- Remote Write (1)
- Spinnaker (1)
- 슬랙봇 (1)
- Mocking Platform (1)
- Kotlin Value Class (1)
- Regex (1)
- Kotlin extension functions (1)
- object declaration (1)
- insurance-common (1)
- Kotlin data class (1)
- 코파일럿 (1)
- 클라우드 (1)
- IDC (1)
- 데브옵스(DevOps) (1)
- CMDB (1)
- ODS/DW (1)
- CDC (1)
- 데이터 서빙 (1)
- 방화벽 (1)
- 백오피스 (1)
- DBT (1)
- Flow.er (1)
- react-window (1)
- react-virtualized (1)
- @tanstack/react-virtual (1)
- ResizeObserver (1)
- IndexDB (1)
- Big Table (1)
- datasource-proxy (1)
- TransactionSynchronizationManager (1)
- LocalContainerEntityManagerFactoryBean (1)
- CombinedSqlSessionFactory (1)
- CombinedSqlSessionHandler (1)
- JdbcPagingItemReader (1)
- MySQL Connector/J (1)
- Release Please Action (1)
- googleapis/release-please-action@v4 (1)
- repository_dispatch (1)
- curl (1)
- Kotlin DSL (1)
- vanniktech-maven-publish-plugin (1)
- JFrog Artifactory (1)
- Maven Central Repository (1)
- GitHub Pages (1)
- Ruler (1)
- JuiceFS (1)
- juicefs-csi-driver (1)
- Alluxio (1)
- nubes (1)
- nubes-s3-proxy (1)
- nBase-ARC Redis (1)
- MinIO (1)
- fio (1)
- NCrashlytics (1)
- Old Symbolicator (1)
- New Symbolicator (1)
- Symbol Map File (1)
- SymbolFile CLI (1)
- 네이버 POI 플랫폼 (1)
- XBU (1)
- CLOUS3.0 (1)
- Nexus (1)
- Milvus DB (1)
- Apache Iceberg (1)
- Kerberos (KDC) (1)
- Flink 쿠버네티스 오퍼레이터 (1)
- flink-shaded-hadoop-3-uber (1)
- Kuromoji (1)
- Sudachi (1)
- Sudachi 플러그인 (1)
- sudachi_split 토큰 필터 (1)
- compact_product_name_analyzer (1)
- compact_normalizer (1)
- whitespace tokenizer (1)
- char_filter (model_delim_to_space, punct_to_space, collapse_spaces) (1)
- Edge N-gram (1)
- constant_score (1)
- productName.edge (1)
- PromQL (1)
- webhook (1)
- AI (1)
- 바이브 코딩 (1)
- WebAuthn Level 2 (1)
- CTAP (1)
- Android API level 28 (1)
- Xcode 15.4 (1)
- Apache-2.0 (1)
- iOS Secure Enclave (1)
- ARM TrustZone (1)
- Android StrongBox (1)
- FIDO2 서버 (1)
- MinHash (1)
- k-MinHash (1)
- Z-테스트 (1)
- NPMI (1)
- MMR (1)
- SetDiv (1)
- Informer (1)
- kubernetes Go client (1)
- kubernetes Python client (1)
- kube-apiserver (1)
- etcd (1)
- SharedInformerFactory (1)
- Indexer (1)
- Hubot (1)
- Slack Workflow (1)
- Ansible (1)
- Notion (1)
- CLAUDE.md (1)
- Vector (1)
- Beats (1)
- node_exporter (1)
- kube-state-metrics (1)
- Akamai (1)
- StatefulSet (1)
- PersistentVolumeClaim (1)
- Webpack 4.44.2 (1)
- Vite (^6.2.1) (1)
- @vitejs/plugin-react (1)
- vite-plugin-babel (1)
- rollup (^4.35.0) (1)
- rollup-plugin-visualizer (1)
- esbuild (1)
- ForkTsCheckerWebpackPlugin (1)
- react-csv (1)
- dayjs (1)
- qs (1)
- MobX 5 (1)
- Material-UI 4 (1)
- WebView (1)
- Taskmaster (1)
- RMS Server (1)
- WMS Server (1)
- RestAPI (1)
- 행정안전부 도로명주소 조회 API (1)
- 행정안전부 좌표정보 API (1)
- 외부업체 주소정제 축적 데이터 (1)
- OMS API (1)
- GRS80 UTM-K (1)
- 구글 스프레드시트 (1)
- BigQuery (1)
- VueRouter (1)
- Swagger (1)
- Postman (1)
- UUID (1)
- 디비 (1)
- mysql-connector-j (1)
- BERT4Rec (1)
- mlflow (1)
- gradio (1)
- growthbook (1)
- Spotify의 셔플링 알고리즘 (1)
- mitmproxy (1)
- charles (1)
- fiddler (1)
- google overwrite contents (1)
- Dedicated Worker (1)
- OffscreenCanvas (1)
- createImageBitmap (1)
- WebP (1)
- JPEG (1)
- HEIC (1)
- Blob (1)
- File (1)
- atob (1)
- 5.7.mysql_aurora.2.11.1 (1)
- MariaDB Connector/J 2.7 (aurora 모드) (1)
- MongoClient (1)
- Spring Data MongoDB (1)
- MongoTransactionManager (1)
- ApplicationEventPublisher (1)
- EAI I/F (1)
- MQ (1)
- Tokens Studio For Figma (1)
- token-transformer (1)
- gh (GitHub CLI) (1)
- Panda CSS (1)
- Yarn berry/Yarn workspace (Monorepo) (1)

## 버린 대안 75개 (사례 93개 중)

- `case_0001` MPS: 관리 부담이 크고 리소스 격리가 어려워 운영 리스크가 크기 때문에 채택하지 않음
- `case_0003` Virtual Scrolling: 페이지네이션이 100건 단위라 DOM 부하가 병목이 아니고 UX와 맞지 않음
- `case_0003` IndexedDB 캐싱: 무효화 규칙 불명확·과한 복잡도·버전/스키마 관리 비용 때문에 도입 보류
- `case_0004` aria-roledescription 사용: 아이폰이 aria-roledescription(ARIA 1.3)을 지원하지 않음
- `case_0004` 단순히 button disabled 속성만 사용: Android에서 disabled만 사용하면 초점이 상단으로 튀는 현상이 발생함
- `case_0005` 문서를 더 잘 써서 방문하게 하기: 문서를 더 잘 써서 방문하게 하는 접근 대신, 문서가 직접 찾아가는 방식을 선택했음
- `case_0006` 단일 컬러 토큰(예: Blue 100)만 밝기 조정: 부분 변경이 전체 팔레트와 다크모드까지 연쇄적으로 문제를 발생시키므로 근본적 해결이 되지 않음
- `case_0010` Milvus: 1차 실험에서는 기능 검증을 진행했으나 2차 성능 검증 대상은 아니어서 다음 단계로 진행되지 않음.
- `case_0010` Redis Stack: 1차 실험에서 기능을 검증했으나 2차 성능 검증 대상은 아니어서 다음 단계로 진행되지 않음.
- `case_0010` Atlas MongoDB (Atlas Search): 실험에서는 구현·하이브리드 검색이 가능했으나 부하 시 CPU 포화로 응답 지연 문제가 관찰되어 최종 선택에서 밀림.
- `case_0010` OpenSearch: 실험에서 부하 시 요청 실패(500)가 발생하는 등 운영 관점에서 한계가 확인되어 최종 선택에서 밀림. **(technologies에도 있음)**
- `case_0010` Pinecone (managed 전문 벡터 검색 서비스): 프로젝트 초기에는 사내에 도입되어 있지 않은 관리 주체 없는 managed 서비스의 신규 비용·계약 이슈로 우선 후보에서 제외함; 먼저 내부 도입/OSS 기반으로 검증을 시도.
- `case_0011` 클라이언트 쪽 코드 난독화: 그저 시간을 지연시킬 뿐이었습니다.
- `case_0011` 프로그래스바 기반 클릭 제약: 이 또한 무용지물이었습니다.
- `case_0011` ZK-SNARK 적용: 우아팝에 적용하는 것은 효과적이지 않다 판단함
- `case_0012` 완벽한 실시간 반영: 완벽한 실시간 반영을 고집하는 대신 시간을 정지시키는 방식을 선택함
- `case_0013` 에그: 운영 비용(사용자 교육)과 백업 회선에서의 모니터링 트래픽 과금 문제가 있어 채택하지 않았다.
- `case_0015` in-memory data store (Hazelcast, Chronicle-Map): 기능이 과하고 진입 장벽·운용 복잡도 우려로 채택하지 않음.
- `case_0015` GC 임계치(IHOP) 파라미터 튜닝 우선 적용: GC 파라미터 튜닝보다 메모리 저장 구조 개선을 우선 적용하기로 결정함.
- `case_0028` Cursor, Claude Code 등: 초보자나 비개발자가 1시간 안에 사용법을 익히고 의미 있는 성과를 내기엔 진입장벽이 높다고 판단했습니다.
- `case_0030` Parcel: 프로젝트 구성이 복잡하여 설정 자동화(Zero-config)가 리스크가 크다고 판단
- `case_0030` Rsbuild (Rspack 계열): 생태계·문서·커뮤니티가 작아 실서비스 적용에 어려움이 있다고 판단
- `case_0033` OpenSearch / Elasticsearch: 대용량 집계·저장 비용·압축률 측면에서 요구사항을 충족하지 못함
- `case_0033` Grafana Loki: 라벨 기반 제약과 집계 기능 한계로 복잡한 필드 검색·집계 요구에 부적합
- `case_0033` Signoz: Signoz는 자체 스키마 강제 및 LogAttributes Map 접근 제한으로 ClickHouse 구조의 장점을 활용할 수 없음
- `case_0033` Fluentd (기존 처리기): 서비스별 고정 Fluentd 배포로 리소스 비효율·처리 지연 발생
- `case_0034` Entity LifeCycle 콜백(@PrePersist/@PreUpdate/@PostLoad): 조회 시마다 복호화 후 1차 캐시 변경으로 불필요한 update가 발생하는 치명적 부작용 때문에 사용하지 않음
- `case_0035` StaticLabelTextArea를 공통으로 분리: 공통화로 얻을 수 있는 이점에 비해 단점(유지 비용·영향 범위)이 더 클 것으로 판단
- `case_0039` 오픈소스 프로젝트: 카카오페이증권의 환경에 알맞지 않아 자체 IDP 구축을 선택
- `case_0042` CTO 리허설을 마지막(3차)으로 진행: 기술 방향성 피드백을 최종 단계에서 받으면 발표 막바지에 불가피한 수정이 발생하므로 순서를 바꾸었음
- `case_0042` 디자이너와 별도 미팅 없이 자료 전달 방식: 발표자와 디자이너가 직접 소통하지 않으면 의도와 다른 수정이 발생함
- `case_0043` 기본 analyzer: 기본 analyzer만으로는 요구사항을 만족하기 어려움.
- `case_0048` 검증 로직을 별도 클래스로 분리: 매번 별도로 검증 로직을 호출해야 한다면 실수로 검증을 누락할 가능성이 있습니다.
- `case_0054` @tanstack/react-virtual: 네이버 로그 시스템의 복잡한 표현 방식과 스크롤 바닥 인식 문제 등으로 오픈소스만으로는 대응하기 어렵다고 판단하여 채택하지 않음.
- `case_0054` @tanstack/react-virtual: 스크롤 바닥 인식 실패 사례의 원인 분석이 어려워 내재된 문제 대응이 어려움.
- `case_0055` ChainedTransactionManager / 분산 트랜잭션 포함: ChainedTransactionManager 또는 분산 트랜잭션으로 MySQL 쿼리를 트랜잭션에 포함시키지 않음
- `case_0055` 비즈니스 로직에 직접 MySQL 호출을 일괄 추가: 모든 비즈니스 로직을 수정하는 방식은 범위가 지나치게 넓어 위험하다고 판단
- `case_0059` Alluxio: 일부 POSIX API 미지원, 원본 저장소와의 동기화 불일치, 마스터/워커 별도 클러스터 운영으로 운영 부담이 큼.
- `case_0059` 네이버 C3 HDFS: Kubernetes CSI Driver 미지원으로 Kubernetes PV로 사용 불가.
- `case_0059` nubes Object Storage (직접 사용): Object Storage 특성상 POSIX API 완전 지원 불가하고 CSI Driver 미지원으로 Kubernetes PV로 사용 불가.
- `case_0059` Ceph-rbd: ReadWriteMany/ReadOnlyMany 미지원으로 다중 Pod 동시 접근 불가.
- `case_0059` NFS: 간단하지만 확장성 및 HA 문제로 대규모 AI 워크로드에 부적합.
- `case_0059` DDN EXAScaler (상용 전용 스토리지): 요구사항을 만족하나 도입 비용이 매우 큼(부분 도입으로 한정 사용).
- `case_0063` Apache Spark (Structured Streaming): 마이크로 배치 방식으로 이벤트 단위 상태·데이터 최신성 판별 및 정확히 한 번 처리 보장 동시 만족이 어려워 채택되지 않음.
- `case_0063` 네이티브 쿠버네티스 방식: 모든 설정을 수동으로 해야 하는 번거로움과 운영 복잡성 때문에 오퍼레이터 방식이 더 적합하다고 판단되어 채택되지 않음.
- `case_0064` mecab-ipadic-neologd: Elasticsearch 7.10.2 환경에서 적용 제약으로 실사용 환경에서 활용 불가
- `case_0066` product 인덱스에 edge 필드 적용: 문서 수(8억 건)에서 토큰 수 증가로 인덱스 크기·색인 처리 비용이 감당 불가
- `case_0068` 온콜 알람을 그대로 반영: 온콜 알람 기반 단순 반영 대신 CUJ 관점의 SLI/SLO 달성 여부로 상태를 표현하기로 결정함
- `case_0068` 모든 CUJ를 동일하게 노출: 핵심 경험을 대표하는 항목 위주로 보여주기로 결정함
- `case_0069` WebAuthn Level 3 / Passkey: Level 3 스펙의 불확실성과 Passkey 동기화 제어 불가로 현재 채택하지 않음.
- `case_0070` 단순 최근 등장 빈도 상위 추출: 일상적 표현들이 상위에 올라 의미있는 트렌드를 잡기 어려움
- `case_0071` Python 클라이언트: Python 클라이언트에서는 Informer 구현 지원이 실무에서 사용 가능한 상태가 아니었다.
- `case_0071` 다수 스레드로 비동기 처리: 스레드 기반 우회는 성능 개선에 한계가 있어 실사용에 부적합했다.
- `case_0075` AI가 MCP로 외부 시스템을 직접 조회하도록 하는 방식: 토큰 비용과 속도 문제
- `case_0080` 네이티브 개발: 앱 심사·업데이트 필요로 운영 효율이 떨어짐
- `case_0082` nginx 라우팅 설정으로 차단: 실행중인 인스턴스의 nginx 설정 변경 및 재시작 권한이 없어 적용 불가했다.
- `case_0082` 스케줄링 배치로 주기적 캐싱: 최소한의 공수로 하나의 인스턴스 안에서 해결하고자 하여 채택하지 않았다.
- `case_0083` 롤백: 롤백 대신 핫픽스로 문제를 우선 완화하기로 결정하여 롤백을 실행하지 않음.
- `case_0084` nginx 설정을 통한 접근 차단: 인프라 구조상 적합하지 않아 채택되지 않음
- `case_0084` BigQuery를 메인 DB처럼 직접 조회: 응답 지연으로 프로덕트 성능 저하 우려
- `case_0086` max-lifetime을 다시 늘리기: 서비스 요구상 max-lifetime을 짧게 유지해야 하므로 적용하지 않음
- `case_0087` 주문서의 모든 상품을 동일하게 보완재로 가정하고 그대로 학습: 해당 방식은 특정 인기 상품이 과도하게 반복 추천되는 등 성능 문제가 발생하여 최종 채택되지 않음
- `case_0087` 사람의 수작업으로 카테고리 간 보완재 관계 설정: 수작업은 매우 어렵고 객관적 평가가 불가능하여 데이터 기반 방법으로 대체됨
- `case_0088` 1, 2번 방식 (google overwrite contents / charles, fiddler 등 수동 툴): 필드 값이 많을 경우 수동으로 하나하나 수정해야 하므로 매번 수동 작업으로 리소스 낭비
- `case_0088` 실제 데이터 수정으로 null을 생성하는 방법: API가 어떤 경우에 null을 반환하는지 정의되어 있지 않아 데이터 수정으로 null을 넘겨주기 어려움
- `case_0089` 포맷 변환(WebP 등): 복잡한 이미지에서는 압축 효율이 낮아 용량 절감이 제한적이고, 품질을 낮출 경우 시각적 품질 저하가 발생해 실제 적용에 제약이 있음
- `case_0089` Canvas 리사이징(메인 스레드): Canvas 처리 비용이 메인 스레드를 점유해 디코딩/인코딩 과정에서 JS 블로킹과 클릭 이벤트 무시 등 부작용 발생
- `case_0089` Shared Worker / Service Worker: 이미지 처리에는 불필요한 기능이 많아 설계상 비적합
- `case_0090` 잠금 읽기(locking read): 행 잠금으로 인한 락 경합 및 데드락 발생 가능성
- `case_0091` 국가별 주문서 양식 개별화: 각 국가마다 별도 주문서 양식을 만들 수 없어 실행 불가
- `case_0092` WriteConcern = MAJORITY: 모든 요청에서 과반수 ACK를 기다려 성능 저하 우려
- `case_0092` 전역 ReadPreference = PRIMARY (모든 읽기 트래픽을 PRIMARY로 집중): SECONDARY 자원 낭비 및 읽기 분산 이점 상실
- `case_0093` SQS 메시지 지연 전달: 간단하지만 지연 시간이 짧으면 타이밍 문제가 여전히 발생하여 임시방편에 불과
- `case_0093` Outbox 패턴 / 로그 테일링 패턴 도입: 설계·구현에 걸리는 시간과 비용이 현재 상황에서 부담스러워 당장 도입하기 어려움
- `case_0094` EAI I/F: 배치 기반으로 지연이 발생하고, 단일 EAI 어댑터 장애 시 전체 통신에 영향이 있어 사용 중단.

## 글 목록

| 글 | 길이 | 결과 | 항목 | 발췌 탈락 | 제목 |
| --- | --- | --- | --- | --- | --- |
| d2/3461887 | 842 | 사례/문제 해결형 | case_0060 | 2/10 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics |
| d2/4555524 | 18,452 | 사례/기술 선택·도입형 | case_0059 | 0/17 | AI 플랫폼을 위한 스토리지 JuiceFS 도입기 |
| d2/8366976 | 3,331 | 사례/문제 해결형 | case_0061, case_0062 | 2/23 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/3814947 | 16,662 | 사례/실험·활용기 | case_0056, case_0057, case_0058 | 0/25 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | - | 0/0 | Thread-safety in C++ |
| d2/1450243 | 15,218 | 사례/기술 선택·도입형 | case_0054 | 0/14 | 윈도잉(windowing) 기법을 적용한 고성능 표 컴포넌트 개발기 |
| d2/8992409 | 1,342 | 사례/실험·활용기 | case_0053 | 0/10 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| d2/6512234 | 22,022 | 사례/문제 해결형 | case_0055 | 0/16 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/1155434 | 9,048 | 제외/개념·튜토리얼 | - | 0/0 | C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가 |
| d2/9290861 | 796 | 인사이트/실험·활용기 | case_0046 | 0/5 | Inside VictoriaMetrics |
| kakao/601 | 3,137 | 제외/회고·문화·행사 | - | 0/0 | 제3회 Kakao Tech Meet 후기 - 불확정성에서 감동까지 |
| kakao/624 | 787 | 제외/회고·문화·행사 | - | 0/0 | 카카오의 스팸 메일 대응 전략: 문자열 변형 CASE STUDY / 제6회 Kakao Tech Meet |
| kakao/761 | 3,645 | 사례/실험·활용기 | case_0031, case_0032 | 0/17 | 실패를 장려하는 실험적 문화 |
| kakao/762 | 13,811 | 사례/실험·활용기 | case_0029 | 3/10 | 생산성 혁신의 실험: AI 마일리지 프로그램 |
| kakao/770 | 16,500 | 사례/기술 선택·도입형 | case_0030 | 0/12 | 5년 된 프로젝트의 빌드 도구를 교체하며 얻은 것들 |
| kakao/784 | 8,710 | 사례/실험·활용기 | case_0028 | 0/10 | 단 1시간 만에 99개의 MVP가? AI와 함께한 1K: 바이브코딩전 생생 후기 |
| kakao/785 | 4,597 | 인사이트/회고·문화·행사 | case_0027 | 0/7 | if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며 |
| kakao/804 | 3,760 | 사례/기술 선택·도입형 | case_0025, case_0026 | 0/14 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/822 | 20,047 | 사례/실험·활용기 | case_0023, case_0024 | 0/18 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakao/835 | 12,198 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 둘째 날, 기술 세션 소개 |
| kakaopay/slack-bot-improving-operational-efficiency-2 | 5,044 | 사례/문제 해결형 | case_0047 | 0/10 | 카카오페이 배포 효율화 1년 회고: 자동화 도입과 팀 생산성 향상 |
| kakaopay/tech-strategy-tpm | 9,673 | 사례/실험·활용기 | case_0052 | 2/9 | 카카오페이 TPM은 어떤 일을 하나요? |
| kakaopay/katfun-joy-kotlin | 14,709 | 사례/실험·활용기 | case_0048, case_0049, case_0050, case_0051 | 0/25 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kakaopay/ifkakao2024-devrel | 10,598 | 사례/회고·문화·행사 | case_0042 | 0/15 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스 준비 맛보기 |
| kakaopay/perftest_zone | 4,708 | 사례/기술 선택·도입형 | case_0038 | 0/11 | 카카오페이 성능 테스트 존을 소개합니다. |
| kakaopay/kakaopaysec-wecan | 8,650 | 사례/기술 선택·도입형 | case_0039, case_0040, case_0041 | 0/27 | We Can Do Better: 개발자 플랫폼 효율화 이야기 |
| kakaopay/kakaopayins-opensearch-analyzer | 10,157 | 사례/실험·활용기 | case_0043, case_0044, case_0045 | 0/16 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/kakaopayins-envelope-encryption | 18,389 | 사례/기술 선택·도입형 | case_0034 | 0/11 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/pallas-v2-log-platform | 25,659 | 사례/문제 해결형 | case_0033 | 0/18 | 일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트 |
| kakaopay/kakaopayins-fe-common-component | 7,059 | 사례/기술 선택·도입형 | case_0035, case_0036, case_0037 | 1/15 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kurly/cart-recommend-model-development | 9,206 | 사례/실험·활용기 | case_0087 | 0/13 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 1부 |
| kurly/commit-mvcc-set-autocommit | 16,463 | 사례/문제 해결형 | case_0090 | 1/9 | 데이터가 있었는데요, 아니 없어요 |
| kurly/deliveryproductteam-culture-1 | 4,454 | 사례/문제 해결형 | case_0085 | 0/10 | 딜리버리 프로덕트 개발팀의 개발문화 - 로그 & 알람편 |
| kurly/connection-leak | 6,791 | 사례/문제 해결형 | case_0086 | 0/8 | 99%가 모른다는 DB Connection 누수 문제 |
| kurly/refine-address-internalization-2 | 4,312 | 사례/기술 선택·도입형 | case_0083 | 0/11 | 주소정제 서비스 내재화 - 2화 ( 그럴싸한 계획 ) |
| kurly/access-block-1 | 5,663 | 사례/문제 해결형 | case_0082 | 0/11 | nginx 설정 없이 우아하게 서비스 점검하기 (上) |
| kurly/access-block-2 | 8,383 | 사례/기술 선택·도입형 | case_0084 | 1/15 | nginx 설정 없이 우아하게 서비스 점검하기 (下) |
| kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0 | 13,290 | 사례/기술 선택·도입형 | case_0079 | 1/15 | 빌드가 터졌다: 5년 된 CMS 프로젝트의 Webpack4 → Vite 전환 |
| kurly/tech-spec-adoption-with-ai-automation | 8,164 | 사례/기술 선택·도입형 | case_0080, case_0081 | 0/23 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| kurly/claude-code-redesign-my-day | 7,389 | 사례/실험·활용기 | case_0075, case_0076, case_0077 | 0/21 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| ly/managing-multi-cdn-logs-traffics-with-vector | 16,695 | 사례/기술 선택·도입형 | case_0078 | 0/9 | Vector를 활용해 멀티 CDN 로그 및 트래픽 관리하기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 18,813 | 사례/실험·활용기 | case_0072, case_0073, case_0074 | 0/17 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/improving-kubernetes-relay-api-server-performance-with-informer | 12,361 | 사례/기술 선택·도입형 | case_0071 | 0/11 | Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기 |
| ly/introducing-fido2-client-sdk-open-source | 9,957 | 사례/기술 선택·도입형 | case_0069 | 1/12 | FIDO2 클라이언트 SDK 오픈소스 소개 |
| ly/how-to-evaluate-ai-generated-images-1 | 16,708 | 제외/개념·튜토리얼 | - | 0/0 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/extracting-trending-keywords-from-openchat-messages | 14,017 | 사례/실험·활용기 | case_0070 | 1/15 | 오픈챗 메시지들로부터 트렌딩 키워드 추출하기 |
| ly/pd1-ai-hackathon-recap | 4,153 | 제외/회고·문화·행사 | - | 0/0 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 6,232 | 사례/기술 선택·도입형 | case_0067, case_0068 | 0/19 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 및 서비스 상태 확인 도구 LINE Status 개발기 |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 19,601 | 사례/실험·활용기 | case_0063 | 0/14 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/japanese-search-kuromoji-to-sudachi | 15,395 | 사례/기술 선택·도입형 | case_0064, case_0065, case_0066 | 5/26 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자가 좋아하는 과자는? |
| oliveyoung/2024-06-05_google-cloud-next-24-review | 3,796 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next '24 방문기 |
| oliveyoung/2024-08-11_type-and-type-system-with-typescript | 11,673 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 타입과 타입 시스템 |
| oliveyoung/2024-09-30_oy-feconf-2024 | 8,894 | 제외/회고·문화·행사 | - | 0/0 | 올리브영에서는 프론트엔드 개발자들이 이런 고민을 하는군요? |
| oliveyoung/2024-10-17_oy-delivery-mq | 4,642 | 사례/기술 선택·도입형 | case_0094 | 0/11 | 올리브영 물류시스템에서는 데이터를 어떻게 주고 받을까? |
| oliveyoung/2024-12-16_Design-System-Token-Automation | 17,955 | 사례/실험·활용기 | case_0095 | 1/8 | 디자인 시스템 중 디자인 토큰을 여러 도구를 이용하여 자동화 하는 방법 |
| oliveyoung/2024-12-17_catalog-mongo-transaction-2 | 11,450 | 사례/기술 선택·도입형 | case_0092, case_0093 | 0/16 | Spring Boot MongoDB 트랜잭션 도입 실전 가이드 |
| oliveyoung/2025-02-14_oy-global-mall-address | 4,978 | 사례/기술 선택·도입형 | case_0091 | 0/10 | 올리브영 글로벌몰 주소 자동완성 및 검증 솔루션 도입기 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 7,158 | 사례/문제 해결형 | case_0089 | 0/14 | Web Worker로 이미지 처리 최적화하기 |
| oliveyoung/2025-06-10_chaos | 7,289 | 사례/실험·활용기 | case_0088 | 0/12 | 버그가 아니라 장애를 잡아라!! QA와 카오스 엔지니어링의 만남 |
| toss/27752 | 5,980 | 사례/실험·활용기 | case_0004 | 0/13 | 드래그 앤 드롭은 사실 편한 UX가 아니다? |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | - | 0/0 | 오픈소스에 기여하고 토스에 합격한.ssul \| EP.4 모닥불 |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | - | 0/0 | 개발자 리더로서 성장당한 썰 \| EP.7 모닥불 |
| toss/toss-frontend-ai-docs | 2,869 | 사례/문제 해결형 | case_0005 | 1/8 | 토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유 |
| toss/toss-people-3 | 7,801 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 문과생에서 토스 개발 리더까지 |
| toss/frontend-esbuild-hmr | 10,415 | 사례/문제 해결형 | case_0002 | 0/10 | ESBuild를 위한 HMR, 직접 만들기 |
| toss/frontend-apply-without-resume | 2,783 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드에 이력서 없이 리포지토리 링크로 지원하세요 (~5/31) |
| toss/toss-securities-gpu-mig | 13,794 | 사례/기술 선택·도입형 | case_0001 | 0/11 | GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기 |
| toss/tds-color-system-update | 13,423 | 사례/기술 선택·도입형 | case_0006, case_0007, case_0008 | 0/26 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| toss/ads_dashboard_fe | 12,467 | 사례/기술 선택·도입형 | case_0003 | 0/15 | 전체 데이터를 브라우저에 두는 광고 대시보드 만들기 |
| woowahan/14484 | 5,518 | 사례/문제 해결형 | case_0022 | 0/9 | “일단 백로그에 넣어두고 여유 있을 때 보는 걸로 할까요?” : 백로그를 백로그로 두지 않는 법 |
| woowahan/14671 | 6,108 | 사례/회고·문화·행사 | case_0019, case_0020, case_0021 | 0/26 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/15398 | 10,772 | 사례/기술 선택·도입형 | case_0014 | 0/11 | Java의 미래, Virtual Thread |
| woowahan/15541 | 6,445 | 제외/개념·튜토리얼 | - | 0/0 | 웹 접근성 준수를 통한 모두에게 배달되는 일상의 행복 |
| woowahan/17386 | 11,245 | 사례/실험·활용기 | case_0016, case_0017, case_0018 | 0/21 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/17911 | 4,799 | 사례/문제 해결형 | case_0013 | 0/13 | B마트 주문 유실을 없애보자: 네트워크 편 |
| woowahan/20763 | 8,615 | 사례/기술 선택·도입형 | case_0015 | 2/15 | 이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기 |
| woowahan/21027 | 25,102 | 사례/기술 선택·도입형 | case_0010 | 0/16 | 실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법 |
| woowahan/24434 | 15,179 | 사례/문제 해결형 | case_0009 | 0/12 | “함께 구매하면 좋은 상품” 추천 모델 고도화 |
| woowahan/24999 | 12,341 | 사례/문제 해결형 | case_0011, case_0012 | 1/20 | WOOWACON 2025 미니게임 WOOWA POP! |
