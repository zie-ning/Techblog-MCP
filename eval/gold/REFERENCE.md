# 정답셋 검수 참고표

`uv run python eval/gold.py reference`로 생성한다. 문제 유형·도메인·기술 사전은 `src/techblog_mcp/taxonomy/`, 글 유형·구조화 유형은 추출 스키마와 프롬프트가 기준이다. 분류 목록이 바뀌면 다시 생성한다. 라벨링 기준은 [README.md](README.md).

정답의 "(허용: …)"는 추출 결과가 그 값이어도 맞다고 보는 다른 답이다.

## 글 유형 (`post_type`, 5개)

| 값 | 정의 |
| --- | --- |
| 문제 해결형 | 겪은 기술 문제와 그 해결 과정을 다룸 |
| 기술 선택·도입형 | 기술·구조를 검토해 도입하거나 바꾼 경험과 근거를 다룸 |
| 실험·활용기 | 도구·기술을 실제 업무에 써 본 경험, 설계 팁, 적용 결과 |
| 개념·튜토리얼 | 교과서적인 개념 설명, 입문 튜토리얼, 문법·API 소개 |
| 회고·문화·행사 | 회고, 조직 문화, 협업 방식, 직무·팀 소개, 컨퍼런스·행사, 채용, 온보딩 |

## 추출 여부 (`kind`, 2개)

| 값 | 정의 |
| --- | --- |
| 추출 | 다른 팀이 설계·구현 판단에 참고할 기술적 실무 내용이 있는 글. 겪은 기술 문제와 해결, 기술 선택·도입의 근거, 도구·기술을 실제 업무에 적용한 경험과 팁 |
| 제외 | 개념·튜토리얼, 회고·문화·행사, 그 밖에 기술적 실무 적용점이 없는 글 |

- 행사·문화·협업 글은 AI 도구나 실무 팁이 섞여 있어도 제외.
- 발표 소개 글은 본문에 해결 근거(수치, 비교, 설계 결정과 이유)가 없으면 제외. 목차는 근거가 아니다.
- 언어 기능·개념 설명 글은 팀이 겪은 문제나 적용 결과가 없으면 제외.

항목 나누기: 독립된 문제-해법 쌍마다 항목 하나, 같은 문제의 단계적 해결은 한 항목, 팁 모음·도구 활용 경험 글은 항목 하나.

## 주 문제 유형 (`primary_problem_type`, 20개)

무엇을 풀었는지(해결의 목적) 기준으로 고른다. 쓴 기술 기준이 아니다.

| 값 | 정의 |
| --- | --- |
| 동시성·락 | 동시 요청으로 인한 경합, 중복 처리, 초과 발급을 락·원자 연산·큐 등으로 제어 |
| 캐싱 | 캐시 도입·전략·무효화, 캐시 일관성과 적중률 개선 |
| 메시징·비동기 처리 | 메시지 큐·이벤트 스트리밍, 비동기 작업 처리, 이벤트 기반 연동 |
| 트래픽 급증 대응 | 세일·이벤트 등 순간 트래픽 폭증 대비, 대기열, 부하 분산, 스로틀링 |
| DB 성능·쿼리 최적화 | 느린 쿼리, 인덱스, 실행 계획, 커넥션 풀 등 DB 성능 개선 |
| DB 마이그레이션·샤딩 | DB 엔진·스키마 이전, 데이터 이관, 샤딩·파티셔닝 |
| 데이터 정합성·트랜잭션 | 분산 트랜잭션, 정합성 보장, 중복·누락 방지, 정산 오차 |
| 장애 대응·복구 | 장애 원인 분석과 복구, 장애 격리·회복성 설계, 재발 방지 |
| 모니터링·관측성 | 로그·메트릭·트레이싱, 알림, 대시보드, APM |
| 배포·CI/CD | 빌드·배포 파이프라인, 무중단 배포, 릴리스 전략 |
| 인프라·컨테이너 | 클라우드 인프라 구성, 쿠버네티스·컨테이너, 네트워크, IaC |
| 비용 절감 | 클라우드·인프라·API 사용 비용을 줄이는 작업 |
| MSA | 서비스 분리, 모놀리스 전환, 서비스 간 경계·통신 설계 |
| API 설계·외부 연동 | API 설계, 외부 시스템·파트너 연동, 인터페이스 표준화 |
| 인증·보안 | 인증·인가, 개인정보 보호, 보안 취약점 대응 |
| 데이터 파이프라인 | 데이터 수집·적재·변환, CDC, 배치·스트리밍 처리, 데이터 플랫폼 |
| 클라이언트 성능(웹·앱) | 웹 프론트엔드·모바일 앱의 렌더링·로딩·번들·메모리 성능 개선 |
| 테스트 자동화 | 단위·통합·E2E 테스트, 테스트 데이터·환경, QA 자동화 |
| 업무·운영 자동화 | AI와 무관한 사내 봇, 운영 스크립트, 반복 업무 자동화 |
| 개발 생산성 | 코드 작성 방식·언어 기능 활용, 리팩터링, 빌드·개발 환경 개선, 개발 도구 도입(AI 코딩 도구 포함) |

## 도메인 (`domain`, 10개)

그 시스템이 속한 서비스 영역. 애매하면 범용.

| 값 | 정의 |
| --- | --- |
| LLM·AI | LLM 애플리케이션, AI 에이전트, AI 코딩 도구, ML 모델 서빙 |
| 결제·금융 | 결제, 송금, 정산, 대출·투자 등 금융 서비스 |
| 커머스·주문·재고 | 상품, 주문, 장바구니, 쿠폰·프로모션, 재고, 매장 |
| 배달·물류 | 배달, 배송, 물류 센터, 픽업 |
| 채팅·메시징 서비스 | 메신저, 채팅, 알림·푸시 발송 서비스 |
| 검색·추천 | 검색, 랭킹, 추천, 개인화 |
| 광고·마케팅 | 광고, 마케팅, CRM, 캠페인 |
| 콘텐츠·미디어 | 콘텐츠, 리뷰, 이미지·영상 등 미디어 처리 |
| 사내 플랫폼·개발 도구 | 개발자가 쓰는 도구·환경과 사내 공통 플랫폼 자체(로그·배포·인증 플랫폼, 빌드 도구, 백오피스). 특정 서비스의 시스템이면 그 서비스 도메인을 고른다 |
| 범용 | 특정 도메인에 묶이지 않는 일반 기술 주제 |

## 버린 대안 유형 (`rejected_alternatives[].kind`, 2개)

| 값 | 정의 |
| --- | --- |
| 기술 | 제품·라이브러리·서비스 자체 (예: OpenSearch, Hazelcast, MPS). 기술별 집계에 들어감 |
| 설계 방식 | 패턴, 구현·설정·운영 방법 (예: Outbox 패턴, READ COMMITTED 격리 수준). 상세 보기에서만 보임 |

## 기술 사전 (132개)

`technologies`는 정해진 목록이 아니라 자유 입력이다. 사전에 있는 기술은 아래 표준 이름으로 쓰고, 사전에 없는 기술도 넣을 수 있다. 괄호는 같은 계열로 묶어 세는 상위 기술.

| 종류 | 기술 |
| --- | --- |
| 언어·런타임 | Java, Kotlin, Kotlin Coroutines (→ Kotlin), Python, Go, TypeScript, JavaScript, Node.js, Swift, JVM, Lua |
| 백엔드 프레임워크·라이브러리 | Spring Framework, Spring Boot (→ Spring Framework), Spring Batch (→ Spring Framework), Spring WebFlux (→ Spring Framework), Spring Cloud Gateway (→ Spring Framework), Spring Kafka (→ Spring Framework), Spring Session (→ Spring Framework), Spring AOP (→ Spring Framework), Spring Cloud AWS (→ Spring Framework), Spring Cloud Config (→ Spring Framework), JPA, QueryDSL, MyBatis, Resilience4j, Jackson, HikariCP, gRPC, GraphQL |
| 프론트엔드·모바일 | React, Next.js (→ React), Vue.js, React Native, TanStack Query, SwiftUI, Jetpack Compose, Flutter |
| 데이터베이스 | MySQL, PostgreSQL, Oracle, Amazon Aurora, Amazon RDS, MongoDB, Amazon DocumentDB, Amazon DynamoDB, Apache HBase, ClickHouse |
| 캐시 | Redis, Caffeine |
| 검색 엔진 | Elasticsearch, OpenSearch |
| 스토리지 | Amazon S3 |
| 메시지 브로커 | Kafka, Amazon MSK (→ Kafka), RabbitMQ, Amazon MQ, Amazon SQS, Amazon SNS, Amazon EventBridge, Amazon Kinesis |
| 데이터 처리·파이프라인 | Kafka Connect (→ Kafka), Kafka Streams (→ Kafka), Debezium, Apache Spark, Apache Flink, Apache Airflow, Logstash, Fluentd, Amazon Kinesis Data Firehose (→ Amazon Kinesis), Oracle GoldenGate |
| 클라우드·인프라 | AWS, AWS Lambda, Amazon ECS, Kubernetes, Amazon EKS (→ Kubernetes), Docker, Helm, Terraform, Istio, Nginx, Amazon CloudFront, Amazon Route 53 |
| CI/CD·빌드 | Argo CD, Jenkins, GitHub Actions, GitLab CI, Gradle |
| 관측성 | Datadog, Prometheus, Grafana, OpenTelemetry, Kibana, Sentry, Pinpoint, Amazon CloudWatch, AKHQ |
| 테스트·품질 | JUnit, Kotest, Fixture Monkey, MSW, Playwright, Cypress, k6, nGrinder, Detekt, reviewdog |
| 인증·보안 | OAuth 2.0, JWT |
| AI 모델·학습 | OpenAI API, Azure OpenAI (→ OpenAI API), Claude, Gemini, Gemma, Qwen, HyperCLOVA X, Amazon Bedrock, Hugging Face, LoRA, QLoRA (→ LoRA) |
| LLM 애플리케이션 | LangChain, LangGraph (→ LangChain), MCP, RAG |
| AI 코딩 도구 | Claude Code, Cursor, GitHub Copilot, Amazon Q |
| 협업·개발 도구 | Slack, Visual Studio Code |
| 기타 클라우드 서비스 | Amazon SES, Amazon Connect, Amazon Polly |
