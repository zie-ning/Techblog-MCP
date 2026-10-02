# 추출 점검 리포트: data

- 모델: gpt-5.6-luna (medium)
- 프롬프트 버전: 8d25a18fd593
- 글 1262편: 추출 863, 제외 399
- 항목 1315개
- 토큰: 호출 2392회, 입력 19,022,392 (캐시 7,939,732), 출력 2,532,270 (reasoning 837,441)
- 비용: $5.414 (편당 $0.0043)

## 블로그별 추출 여부

| 블로그 | 추출 | 제외 | 항목 수 |
| --- | --- | --- | --- |
| d2 | 75 | 81 | 111 |
| kakao | 105 | 106 | 194 |
| kakaopay | 91 | 23 | 140 |
| kurly | 49 | 2 | 71 |
| ly | 151 | 59 | 217 |
| oliveyoung | 120 | 39 | 172 |
| toss | 134 | 45 | 213 |
| woowahan | 138 | 44 | 197 |

## 글 유형 × 추출 여부

| 글 유형 | 추출 | 제외 |
| --- | --- | --- |
| 개념·튜토리얼 | 0 | 79 |
| 기술 선택·도입형 | 184 | 9 |
| 문제 해결형 | 416 | 8 |
| 실험·활용기 | 263 | 11 |
| 회고·문화·행사 | 0 | 292 |

## 짧은 글 (평문 1,500자 미만) 126편

| 글 | 길이 | 결과 | 항목 | 분류 이유 |
| --- | --- | --- | --- | --- |
| d2/4608596 | 688 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션과 발표 영상을 소개하는 글이며, 본문에는 AI 경량화의 구체적인 실험 결과·비교·설계 근거가 제시되지 않고 발표 주제 목록만 나열되어 있습니다. |
| d2/5053838 | 607 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션 영상 공개 글로, RocksDB·LSM Tree 등의 발표 목차와 대상만 제시할 뿐 구체적인 문제 해결 과정이나 적용 결과·설계 근거가 본문에 없다. |
| d2/2236952 | 529 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션 영상 공개를 안내하는 글이며, 구체적인 문제 해결 과정이나 설계·도입 근거, 적용 결과가 본문에 제시되지 않았습니다. |
| d2/3461887 | 842 | 제외/문제 해결형 | 0 | Crash 분석 시스템의 구체적인 문제와 개선 내용을 다루는 세션이지만, 본문에는 발표 영상의 주제와 목차만 제시되어 있고 실제 해결 근거·설계 결정·비교 수치가 서술되어 있지 않습니다. 사내 기술 행사 세션 공개 글이므로 제외합니다. |
| d2/3612055 | 1,371 | 제외/개념·튜토리얼 | 0 | Terraform과 네이버 클라우드 IaC의 개념, 명령어, 구성 방법을 소개하고 발표 세션 내용을 나열한 글이다. 팀이 겪은 구체적인 문제와 해결 과정이나 도입 근거·적용 결과가 서술되어 있지 않아 기술 사례로 추출하지 않는다. |
| d2/9139321 | 1,013 | 제외/개념·튜토리얼 | 0 | Terraform과 HCL의 개념, 명령어, 문법, 기능을 발표 목차 중심으로 소개하는 세션 공개 글이며, 구체적인 기술 문제 해결 과정이나 실제 적용 결과·근거가 제시되지 않았습니다. 사내 기술 교류 행사 세션 소개에 해당해 제외합니다. |
| d2/6014816 | 670 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션 영상 공개 글로, Text.Style Operation과 Multi User Undo/Redo를 다룬다는 목차만 제시하고 구체적인 문제 해결 과정·설계 근거·적용 결과는 본문에 설명하지 않는다. |
| d2/0983091 | 569 | 제외/회고·문화·행사 | 0 | 사내 기술 행사 발표 영상 공개 글로, One-Source Multi-Use 관련 주제 목록만 제시하고 구체적인 문제 해결 과정·비교 근거·적용 결과를 본문에서 설명하지 않는다. |
| d2/5564264 | 522 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션 공개를 안내하는 글이며, 본문에 구체적인 문제 해결 과정이나 설계 근거·적용 결과가 제시되지 않고 목차만 나열되어 있습니다. |
| d2/7472830 | 651 | 제외/개념·튜토리얼 | 0 | TypeScript 타입 이론과 추론 원리를 설명하고 문제 풀이 목차를 소개하는 행사 발표 자료 공개 글이다. 특정 팀의 기술 문제 해결이나 실제 라이브러리 개발 적용 결과·근거는 본문에 제시되지 않았다. |
| d2/0680815 | 811 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, gRPC·Spark·Kafka 등의 주제와 목차만 제시하고 구체적인 문제 해결 과정이나 설계 근거·적용 결과를 본문에서 설명하지 않는다. |
| d2/0623656 | 675 | 제외/개념·튜토리얼 | 0 | 사내 기술 교류 행사 발표 자료를 소개하는 글로, Figma와 Jetpack Compose를 활용한 디자인 시스템 구축을 다룬다고만 설명할 뿐 구체적인 문제 해결 과정·적용 결과·설계 근거가 본문에 제시되지 않았습니다. |
| d2/7030870 | 571 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글이며, 본문에 구체적인 자동화 구현 과정이나 적용 결과·해결 근거가 서술되지 않고 발표 목차만 제시되어 있어 기술 사례로 추출하기 어렵습니다. |
| d2/8011540 | 576 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, WritingPath의 구체적인 설계·구현·성능 비교나 적용 결과를 본문에서 설명하지 않고 발표 주제와 목차만 제시한다. |
| d2/2905424 | 868 | 제외/개념·튜토리얼 | 0 | Kubernetes의 CoreDNS와 Nodelocal DNSCache 구성 및 DNS 질의 동작을 설명하는 발표 자료 소개 글이지만, 구체적인 장애 해결 과정이나 비교 수치, 설계 결정의 근거와 적용 결과가 본문에 제시되지 않았다. 기술 행사 세션 공개 및 목차 중심의 개념 설명에 해당한다. |
| d2/7282210 | 534 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, 목차만 제시되어 있고 로그 문제의 해결 과정이나 구체적인 설계·적용 근거가 본문에 설명되어 있지 않다. |
| d2/7321313 | 732 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, AI 코드 리뷰의 아키텍처와 도입기를 목차 수준으로만 제시하며 구체적인 문제 해결 과정이나 적용 결과가 본문에 없다. |
| d2/0403593 | 1,201 | 추출/문제 해결형 | 1 | 뉴스서비스의 SPOF와 장애 예방을 위해 Chaos Engineering과 Toxiproxy를 실제 적용하고, 테스트 결과를 바탕으로 기존 코드의 문제점을 확인·개선한 구체적인 실무 사례를 다룬다. |
| d2/8866888 | 684 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션을 공개·소개하는 글이며, 본문에 모델 경량화의 구체적인 해결 과정이나 성능 비교·설계 근거가 제시되지 않고 발표 주제와 목차만 나열되어 있어 기술 사례로 추출하지 않는다. |
| d2/3247986 | 918 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션 공개 안내와 발표 목차 중심이며, VLM 적용 과정의 구체적인 문제 해결·설계 근거·성과 수치가 본문에 제시되지 않았습니다. |
| d2/1536585 | 654 | 제외/개념·튜토리얼 | 0 | 신규 프로젝트에서 Hazelcast를 도입한 배경과 구성 방법을 다룬다고 소개하지만, 본문에는 구체적인 문제 해결 과정·도입 근거·적용 결과가 없고 발표 목차와 행사 세션 공개 안내만 제시되어 있다. |
| d2/8808377 | 726 | 제외/회고·문화·행사 | 0 | 사내 기술 행사 세션 공개를 안내하는 글로, 모듈화 적용과 트러블슈팅을 다룬다는 목차만 제시되어 있으며 구체적인 해결 과정·비교·성과 등의 기술적 근거가 본문에 없다. |
| d2/5646819 | 551 | 제외/기술 선택·도입형 | 0 | Bazel을 활용한 Android·iOS 포팅 경험을 다룬 세션이지만, 본문에는 발표 목차와 행사 소개만 있고 Bazel 선택 근거, 포팅 과정의 구체적인 설계·문제 해결·적용 결과가 제시되지 않았다. 사내 기술 교류 행사 세션 공개 글이므로 제외한다. |
| d2/3012756 | 783 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, UX 장기 로드맵 수립의 목차와 대상만 제시하고 구체적인 적용 과정·해결 근거·결과를 본문에서 설명하지 않는다. |
| d2/4534298 | 650 | 제외/개념·튜토리얼 | 0 | 타입시스템과 대수적 데이터 타입을 활용한 도메인 모델링 개념을 소개하는 발표 자료 공개 글이며, 특정 팀이 겪은 문제의 해결 과정이나 적용 결과·근거가 제시되지 않았다. |
| d2/9114363 | 688 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션 공개 글로, GPU Kubernetes 이전 과정의 구체적인 문제·해결 근거나 적용 결과 없이 발표 주제와 목차만 소개하고 있어 기술 사례로 추출하기 어렵습니다. |
| d2/9591075 | 991 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, 소프트 스킬과 협업 경험을 다루지만 구체적인 기술 문제 해결이나 기술 적용 근거는 제시하지 않는다. |
| d2/4871077 | 1,148 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 영상을 소개하는 글로, Android SDK 배포 자동화의 구체적인 문제 해결 과정이나 적용 결과는 없이 발표 목차와 대상만 제시하고 있다. |
| d2/5294836 | 728 | 제외/개념·튜토리얼 | 0 | 사내 기술 교류 행사 세션과 발표 자료를 소개하는 글로, KMP·Compose Multiplatform 적용 과정의 구체적인 문제 해결, 비교 수치, 설계 결정 근거는 본문에 제시되지 않고 목차 수준으로만 나열되어 있다. |
| d2/0362045 | 1,119 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션 공개 글로, 코호트 시스템의 구조·활용 사례를 목차 수준으로 소개할 뿐 구체적인 문제 해결 과정이나 설계 근거·성과가 본문에 제시되지 않았습니다. |
| d2/8051412 | 751 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션을 공개·소개하는 글로, KMP·디자인 시스템·아이콘 자동화 등의 구체적인 설계 결정이나 적용 결과를 본문에서 설명하지 않고 발표 목차만 나열하고 있습니다. |
| d2/4678393 | 956 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, Flink·Paimon 아키텍처와 도입 이유는 목차 수준으로만 제시되어 있습니다. 구체적인 문제 해결 과정, 비교 근거, 설계 결정이나 적용 결과가 본문에 없어 기술 사례로 추출하기 어렵습니다. |
| d2/3675627 | 1,250 | 제외/문제 해결형 | 0 | 조회 트래픽 증가와 Elasticsearch 도입이라는 문제·해결 주제를 다루지만, 본문에는 구체적인 설계 근거·비교 수치·적용 결과 없이 발표 내용과 목차만 제시되어 있어 기술 사례로 추출하기 어렵습니다. |
| d2/1025526 | 769 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, Kafka 프로듀서 최적화와 압축을 다룬다는 목차만 제시되어 있으며 구체적인 문제 해결 과정이나 적용 결과·근거가 본문에 없다. |
| d2/2472336 | 696 | 제외/개념·튜토리얼 | 0 | Kafka metadata와 클라이언트·브로커 간 동작 메커니즘 및 옵션을 설명하는 발표 자료 소개 글이지만, 특정 문제를 해결한 과정이나 적용 결과·비교 근거가 본문에 제시되지 않아 개념·튜토리얼로 분류합니다. |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | 0 | C++의 data race, happens-before, 동기화 프리미티브 등 스레드 안전성 기본 개념과 사용법을 설명하는 공개 행사 세션 소개 글이다. 특정 팀이 겪은 문제의 해결 과정이나 실제 적용 결과·설계 근거는 제시되지 않는다. |
| d2/5251464 | 847 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션을 공개하는 글로, 본문에는 AI를 활용한 장애 처리·노이즈 분류 등의 목차와 소개만 있고 구체적인 설계 결정, 적용 과정, 비교·수치 등의 해결 근거가 제시되지 않았다. |
| d2/4706492 | 1,246 | 제외/실험·활용기 | 0 | 대용량 표 컴포넌트에 Windowing을 적용한 사례를 다루지만, 본문에는 목차와 발표 소개만 있고 성능 수치·비교·구체적인 설계 결정 및 해결 근거가 제시되지 않아 기술 사례로 추출하기 어렵다. |
| d2/6196427 | 1,234 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표를 소개하며 Docusaurus·Typesense와 배포 구성을 목차 수준으로 나열한 글이다. 구체적인 문제 해결 과정이나 비교 수치, 설계 근거가 본문에 제시되지 않아 기술 사례로 추출하지 않는다. |
| d2/6269411 | 1,042 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 자료를 소개하는 글이며, 본문에는 Spring Cloud Config 커스터마이징의 구체적인 설계 근거나 적용 결과 없이 발표 목차와 대상만 제시되어 있습니다. |
| d2/0251755 | 786 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, GPU 오토스케일링의 구체적인 설계·문제 해결 과정이나 적용 결과 없이 발표 주제와 목차만 제시한다. |
| d2/4348237 | 1,096 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, Ray·GPU 활용 주제와 목차만 제시되어 있으며 구체적인 문제 해결 과정이나 설계 근거·적용 결과가 본문에 서술되어 있지 않다. |
| d2/0539348 | 751 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션 공개 글로, SPLADE·FlashTokenizer·서빙 최적화의 구체적인 문제 해결 과정이나 성능 비교·설계 근거는 제시하지 않고 발표 주제와 목차만 소개한다. |
| d2/1072010 | 564 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글이며, 본문에 Large Screen 적용의 구체적인 문제 해결 과정·설계 근거·적용 결과가 제시되지 않고 발표 주제와 대상만 안내하고 있다. |
| d2/0548704 | 769 | 제외/개념·튜토리얼 | 0 | 사내 행사 발표 세션을 소개하며 ARC 기반 GPU CI/CD 인프라를 다룬다는 목차와 대상만 제시하고, 구체적인 문제 해결 과정·설계 근거·적용 결과가 본문에 서술되어 있지 않다. |
| d2/1104856 | 749 | 제외/개념·튜토리얼 | 0 | OpenTelemetry와 Collector의 구성 요소 및 생태계를 소개하는 발표 자료 공개 글로, 구체적인 기술 문제 해결 과정이나 설계 비교·적용 결과가 본문에 제시되지 않았습니다. |
| d2/8677833 | 606 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, Telegraf와 Exporter의 도입 배경·벤치마크·개선점이 목차 수준으로만 제시되어 구체적인 설계 결정이나 해결 근거가 없다. |
| d2/1580651 | 604 | 제외/문제 해결형 | 0 | JVM 웜업 문제와 라이브러리 웜업 구현을 다룬 세션을 소개하지만, 본문에는 구체적인 해결 근거·설계 결정·검증 결과가 제시되지 않고 발표 목차만 나열되어 있어 기술 실무 사례로 추출하기 어렵다. |
| d2/3974242 | 639 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션을 소개하는 글로, Consumer Group Protocol의 문제 해결 과정이나 성능 비교·설계 근거 등 구체적인 실무 내용은 본문에 제시되지 않고 발표 목차만 나열되어 있습니다. |
| d2/8992409 | 1,342 | 제외/회고·문화·행사 | 0 | 네이버 사내 기술 교류 행사 발표 세션을 소개하는 글로, DBT·Airflow와 Flow.er의 구체적인 설계 결정이나 적용 결과는 본문에 제시되지 않고 발표 목차만 나열되어 있다. |
| d2/0957098 | 642 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, 히트맵·히스토그램과 시행착오를 언급하지만 구체적인 문제 해결 과정이나 설계 근거·적용 결과를 본문에서 다루지 않는다. |
| d2/3691494 | 717 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션을 소개하는 글로, Ollama·mcp-agent 활용 사례는 목차와 개요 수준에 그치며 구체적인 문제 해결 과정이나 설계 근거·적용 결과가 제시되지 않았습니다. |
| d2/4199466 | 878 | 제외/문제 해결형 | 0 | 네이버 검색 장애 대응을 위한 LLM DevOps Agent의 구축과 평가를 다룬 세션이지만, 본문에는 발표 목차와 소개만 있고 구체적인 문제 해결 과정·설계 근거·적용 결과가 제시되지 않았다. |
| d2/9290684 | 978 | 제외/문제 해결형 | 0 | 실시간 거래 리포트의 저지연 조회 문제를 다룬 세션이지만, 본문에는 아키텍처·기술 선택·성능 결과 등의 구체적인 해결 근거가 없고 행사 발표 공개 및 목차 소개가 중심이다. |
| d2/0931890 | 998 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 공개하는 글로, Event-driven MLOps와 평가 시스템의 개요 및 목차만 소개하고 구체적인 문제 해결 과정·설계 근거·적용 결과를 본문에서 다루지 않는다. |
| d2/9036125 | 1,154 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표를 소개하는 글로, PDF 파서의 구체적인 문제 해결 과정이나 성능 비교·설계 근거는 본문에 제시하지 않고 발표 목차만 나열하고 있다. |
| d2/3442203 | 775 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, 본문에 구체적인 적용 과정·문제 해결 근거·결과가 서술되지 않고 발표 주제와 목차만 제시되어 있어 기술 사례로 추출하지 않습니다. |
| d2/8061804 | 1,141 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, 구체적인 구현 과정이나 실험 근거보다 발표 주제와 목차를 나열하는 데 그친다. 기술적 실무 사례를 다룬 발표 원문이 아니라 행사·발표 자료 소개 글이므로 제외한다. |
| d2/9290861 | 796 | 제외/개념·튜토리얼 | 0 | 사내 기술 교류 행사 발표 자료를 소개하는 글로, VictoriaMetrics의 내부 구조와 구성 요소를 다룬다는 목차만 제시되어 있습니다. 구체적인 기술 문제 해결 과정이나 적용 결과·설계 근거가 본문에 서술되어 있지 않아 제외합니다. |
| d2/0107009 | 1,032 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션을 소개하는 글로, 프롬프팅·MCP·문서화 등의 주제는 목차에 나열되어 있을 뿐 구체적인 적용 과정이나 해결 근거·결과가 본문에 제시되지 않았다. |
| d2/6647064 | 638 | 제외/문제 해결형 | 0 | AI 에이전트 개발의 모델 선택, 속도 최적화, Safety, 평가·QA 등을 목차로 제시하지만, 본문에 구체적인 문제·해결 과정이나 적용 결과가 서술되지 않은 사내 행사 발표 소개 글이다. |
| d2/4372269 | 961 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 자료를 소개하는 글로, 구체적인 해결 과정·설계 근거·수치나 적용 결과는 본문에 제시하지 않고 발표 주제와 목차만 나열하고 있다. |
| d2/3431313 | 624 | 제외/개념·튜토리얼 | 0 | 사내 행사 세션 공개와 발표 목차·대상 소개가 중심이며, Manifest Shield의 구체적인 문제 해결 과정이나 적용 결과, 설계 근거가 본문에 제시되지 않아 기술 사례로 추출하기 어렵습니다. |
| d2/1059238 | 861 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션 공개를 안내하는 글이며, 본문에는 구체적인 문제 해결 과정이나 설계 근거가 없고 발표 주제와 목차만 제시되어 있습니다. |
| d2/6811215 | 821 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션을 소개하는 글로, Playwright E2E 테스트나 AI 에이전트 워크플로우의 구체적인 설계·적용 결과와 해결 근거는 제시하지 않고 발표 주제와 목차만 나열하고 있다. |
| d2/8319114 | 741 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션을 소개하는 글로, 본문에는 광고 SDK 에러 모니터링 시스템의 구체적인 설계·구현 과정이나 비교·성과가 없고 발표 목차만 제시되어 있습니다. |
| d2/4399330 | 839 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사에서 발표된 세션과 목차를 소개하는 글이며, GNOSIS의 구체적인 구현·검증 결과나 설계 결정의 근거가 본문에 서술되어 있지 않고 발표 주제만 나열되어 있다. |
| d2/2852215 | 660 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션을 소개하는 글로, 자동화 파이프라인의 구체적인 설계 근거·적용 결과·해결 과정은 본문에 제시되지 않고 발표 주제와 목차만 나열되어 있다. |
| d2/7056385 | 666 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션을 공개하는 안내 글로, AI Agent와 Context Provider 구축의 구체적인 문제 해결 과정이나 설계 근거·적용 결과는 본문에 제시되지 않고 발표 목차 수준으로만 소개되어 있습니다. |
| d2/4394359 | 837 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션 공개 글로, Automatic Sharding의 구체적인 설계 근거·비교·도입 결과가 본문에 제시되지 않고 발표 목차와 소개 중심이다. |
| d2/3015479 | 644 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 공개하고 목차와 프레임워크 소개만 제공할 뿐, 구체적인 문제 해결 과정이나 설계 근거·적용 결과가 본문에 제시되지 않았습니다. |
| d2/9227131 | 707 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 발표 세션을 소개하는 글로, RUM의 구체적인 구현 과정이나 문제 해결 근거·적용 결과 없이 발표 목차와 서비스 소개만 제시하고 있다. |
| d2/3897377 | 830 | 제외/회고·문화·행사 | 0 | 사내 기술 교류 행사 세션을 소개하는 글로, AI 에이전트 시스템의 구체적인 설계·적용 과정이나 해결 근거는 본문에 제시되지 않고 발표 목차만 나열되어 있습니다. |
| d2/8118359 | 607 | 제외/개념·튜토리얼 | 0 | 에이전트, 워크플로우, 하네스, Context/Memory, MCP/A2A 등의 개념과 차이를 정리한 발표 자료 공유 글이다. 특정 팀의 기술 문제 해결 과정이나 실제 업무 적용 결과·설계 근거가 제시되지 않아 개념·튜토리얼에 해당한다. |
| kakao/600 | 648 | 제외/회고·문화·행사 | 0 | 카카오의 안정성 보고서 발간을 소개하는 글로, 안정성 업무 담당자들의 역할과 일상을 개괄할 뿐 구체적인 기술 문제 해결 과정이나 설계·구현 근거를 다루지 않습니다. |
| kakao/603 | 1,470 | 제외/회고·문화·행사 | 0 | Kakao Tech Meet 발표 영상과 발표자 인터뷰를 소개하는 행사 후기성 글이며, 대용량 트래픽 처리의 구체적인 설계·해결 근거나 적용 결과는 본문에 제시되지 않았다. |
| kakao/608 | 962 | 제외/회고·문화·행사 | 0 | 카카오 테크 밋의 발표 영상과 발표자 인터뷰를 소개하는 행사 후기성 글이며, Virtual Thread의 구체적인 적용 과정이나 문제 해결 근거는 제시하지 않는다. |
| kakao/616 | 1,290 | 제외/회고·문화·행사 | 0 | Kakao Tech Meet 발표 영상과 발표자 인터뷰를 소개하는 행사 후기 성격의 글이며, 웹 텍스트 에디터의 구체적인 문제 해결 과정이나 설계 근거·적용 결과는 본문에 제시되지 않았습니다. |
| kakao/620 | 102 | 제외/회고·문화·행사 | 0 | 구름톤유니브 행사 현장의 분위기와 모습을 소개하는 스케치 글로, 기술 문제 해결이나 구체적인 기술 적용 사례가 없습니다. |
| kakao/621 | 1,318 | 제외/회고·문화·행사 | 0 | KCC 2024 학회와 카카오 테크 워크숍의 일정 및 발표 프로그램을 안내하는 행사 홍보 글이다. 기술 주제와 사례가 제목 수준으로 나열되어 있을 뿐, 구체적인 문제 해결 과정이나 설계 근거·적용 결과가 본문에 제시되지 않았다. |
| kakao/624 | 787 | 제외/회고·문화·행사 | 0 | Kakao Tech Meet 발표 영상과 발표자 인터뷰를 소개하는 행사 후기성 글이며, 문자열 변형이나 스팸 대응 기술의 구체적인 설계·해결 과정과 근거는 본문에 제시되지 않습니다. |
| kakao/625 | 1,100 | 제외/회고·문화·행사 | 0 | 제6회 Kakao Tech Meet의 발표 영상과 발표자 인터뷰를 소개하는 행사 후기 성격의 글이다. 이미지 분류 모델 경험을 언급하지만 구체적인 문제 해결 과정이나 설계·적용 근거는 본문에 제시되지 않는다. |
| kakao/636 | 502 | 제외/회고·문화·행사 | 0 | 카카오 개발자 컨퍼런스의 일정, 장소, 참가 대상과 프로그램을 안내하는 행사 홍보 글이며, 구체적인 기술 문제 해결이나 실무 적용 근거를 다루지 않는다. |
| kakao/651 | 1,018 | 제외/회고·문화·행사 | 0 | if(kakaoAI)2024 행사에서 다룰 세션을 소개하는 글로, APM Agent 개발이나 DevOps 파이프라인의 구체적인 해결 과정과 근거는 본문에 제시되지 않고 주제와 일정만 나열되어 있다. |
| kakao/664 | 645 | 제외/회고·문화·행사 | 0 | if(kakaoAI)2024 행사와 카카오의 AI Native 전략 및 영상을 소개하는 글로, 구체적인 기술 문제 해결 과정이나 적용 근거가 제시되지 않았습니다. |
| kakao/708 | 1,334 | 제외/회고·문화·행사 | 0 | AI 도구와 바이브 코딩을 활용한 사내 해커톤 개최 소식과 참여 규모·운영 취지를 소개하는 공식 보도자료로, 구체적인 기술 적용 과정이나 문제 해결 근거보다 행사 자체와 조직 개발 문화 확산이 중심이다. |
| kakao/745 | 730 | 제외/회고·문화·행사 | 0 | 카카오 AI 앰배서더 모집과 활동 혜택·일정·밋업을 안내하는 홍보 및 행사성 글이며, 구체적인 기술 문제 해결이나 업무 적용 사례를 다루지 않습니다. |
| kakao/781 | 941 | 제외/회고·문화·행사 | 0 | AI 에이전트 경진대회의 일정, 장소, 시상, 멘토링 등 행사 참여 정보를 안내하는 모집 글이며, 구체적인 기술 문제 해결이나 실무 적용 결과를 다루지 않습니다. |
| kakao/783 | 1,144 | 제외/회고·문화·행사 | 0 | 학술대회 특별세션 발표와 AI 마일리지 프로그램의 운영 성과를 소개하며 조직의 일하는 방식과 문화 변화를 다룬 글이다. 구체적인 도구 설정, 업무 적용 과정, 기술적 문제 해결이나 설계 근거가 중심이 아니므로 제외한다. |
| kakao/830 | 1,223 | 제외/회고·문화·행사 | 0 | 지역 AI 생태계와 기술 교류를 위한 서밋 개최 안내 및 프로그램·참가 신청을 소개하는 행사 홍보 글이다. 구체적인 기술 문제 해결이나 업무 적용 결과는 제시하지 않는다. |
| kakao/832 | 435 | 제외/회고·문화·행사 | 0 | if(kakao)26 컨퍼런스를 홍보하고 관련 글을 안내하는 예고 글로, 구체적인 기술 문제 해결이나 실무 적용 사례를 다루지 않는다. |
| ly/20231001a | 254 | 제외/회고·문화·행사 | 0 | 두 회사의 통합과 새 기술 블로그 개설을 알리는 공지로, 구체적인 기술 문제 해결이나 실무 적용 사례를 다루지 않습니다. |
| ly/ly-tech-blog-fy23-retrospective | 938 | 제외/회고·문화·행사 | 0 | FY23 회고 블로그 릴레이라는 사내 행사와 예정된 글 목록을 소개하는 안내 글이며, 구체적인 기술 문제 해결이나 기술 적용 과정은 다루지 않습니다. |
| ly/techniques-for-improving-code-quality-list | 1,386 | 제외/회고·문화·행사 | 0 | 사내 Review Committee와 Weekly Report를 소개하고 코드 품질 개선 시리즈의 글 목록을 안내하는 글로, 구체적인 기술 문제 해결이나 적용 과정·결과를 다루지 않습니다. |
| ly/intruoduction-to-tech-verse-2025 | 1,258 | 제외/회고·문화·행사 | 0 | 테크 컨퍼런스 개최 일정과 참가 방법, 세션 목록을 안내하는 행사 홍보 글이며 구체적인 기술 문제 해결이나 적용 근거를 본문에서 다루지 않는다. |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | 0 | 개발자들의 선호 과자를 설문조사하고 결과와 추천 패키지를 소개하는 조직 구성원 대상의 문화·복지성 콘텐츠로, 기술적 문제 해결이나 실무 적용 내용이 없습니다. |
| toss/firesidechat_frontend_1 | 519 | 제외/회고·문화·행사 | 0 | 토스 프론트엔드 개발자들의 기술 대화 영상과 목차를 소개하는 글로, 가독성 좋은 코드에 대한 구체적인 문제 해결 과정이나 적용 결과가 본문에 제시되지 않는다. |
| toss/firesidechat_frontend_2 | 561 | 제외/회고·문화·행사 | 0 | 토스 프론트엔드 개발자들의 함수형·객체지향 프로그래밍에 대한 토론 영상 소개와 타임스탬프가 중심이며, 구체적인 기술 문제 해결 과정이나 적용 결과가 제시되지 않았다. |
| toss/firesidechat_frontend_3 | 547 | 제외/회고·문화·행사 | 0 | 토스의 프론트엔드 테스트 작성 방식을 다룬 영상 회차 소개 글이지만, 본문에는 구체적인 테스트 설계·적용 과정이나 문제 해결 근거가 없고 타임스탬프와 출연진 안내가 중심이다. |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | 0 | 토스 개발자들의 오픈소스 기여 경험과 기술적 성장에 관한 발표·대담을 소개하는 콘텐츠로, 구체적인 문제 해결 과정이나 설계·적용 결과보다 출연진과 타임스탬프 중심의 행사성 내용이다. |
| toss/firesidechat_frontend_5 | 545 | 제외/회고·문화·행사 | 0 | 개발자의 업무 태도와 제품 기여에 대한 토크 영상 소개 및 타임스탬프 중심으로, 구체적인 기술 문제 해결이나 기술 도입 근거가 제시되지 않았습니다. |
| toss/firesidechat_frontend_6 | 598 | 제외/개념·튜토리얼 | 0 | 프레임워크와 라이브러리의 정의·차이, 사용 여부와 학습 필요성을 설명하는 행사·콘텐츠 소개 글로, 특정 팀의 기술 문제 해결이나 실제 도입·적용 결과와 같은 실무 근거가 제시되지 않았습니다. |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | 0 | 프론트엔드 리드들의 리더십 성장과 조직 내 경험을 다루는 대담·콘텐츠로, 구체적인 기술 문제 해결이나 기술 도입·적용 사례가 중심이 아니다. |
| toss/firesidechat_frontend_8 | 622 | 제외/회고·문화·행사 | 0 | 채용 과정과 지원자 조언을 다루는 인터뷰·콘텐츠 소개 글로, 기술 문제 해결이나 구체적인 기술 도입·적용 결과가 아니라 채용 및 커리어 이야기가 중심이다. |
| toss/firesidechat_frontend_9 | 583 | 제외/회고·문화·행사 | 0 | 토스 개발자들의 최적화 사례를 다룬 영상 소개 글이지만, 본문에는 구체적인 문제 해결 과정·수치·비교·설계 근거가 없고 타임스탬프와 출연진 등 발표 콘텐츠 안내가 중심이다. |
| toss/firesidechat_frontend_10 | 786 | 제외/회고·문화·행사 | 0 | 시청자 질문과 코드 리뷰를 다루는 영상·캠프파이어 특집 소개 글로, 구체적인 문제 해결 과정이나 적용 결과보다 행사성 콘텐츠와 주제 목록 안내가 중심이다. |
| toss/firesidechat_frontend_10a | 878 | 제외/회고·문화·행사 | 0 | 시청자 질문과 코드 리뷰를 다루는 영상 소개 및 행사성 콘텐츠로, 테스트 코드·ESLint·useEffect에 대한 구체적인 문제 해결 과정이나 적용 결과보다 주제와 타임스탬프를 나열하는 데 그칩니다. |
| toss/firesidechat_frontend_11 | 808 | 제외/기술 선택·도입형 | 0 | 자체 디자인 편집기 개발과 기술적 도전, MobX 선택을 소개하지만, 본문에는 구체적인 문제 해결 과정이나 성능 최적화 근거가 제시되지 않고 영상·타임스탬프 중심의 소개에 그친다. |
| toss/firesidechat_frontend_12 | 713 | 제외/회고·문화·행사 | 0 | 토스 프론트엔드 챕터의 코드 리뷰 문화와 워킹그룹·위원회·배틀 등 조직 차원의 운영 사례를 소개하는 영상으로, 구체적인 기술 문제 해결이나 도구 적용 결과보다 문화와 활동 소개가 중심이다. |
| toss/payments-legacy-intro | 1,273 | 제외/회고·문화·행사 | 0 | 레거시 개편 여정을 소개하는 시리즈 예고·발표 기반의 서문으로, 구체적인 기술 문제 해결 과정이나 설계 근거·적용 결과가 제시되지 않았다. |
| woowahan/14224 | 85 | 제외/회고·문화·행사 | 0 | 우아한스터디 겨울시즌 모집 안내와 신청 방법을 다루는 글로, 기술적 실무 적용이나 문제 해결 내용이 없습니다. |
| woowahan/14513 | 1,326 | 제외/회고·문화·행사 | 0 | 우아한테크세미나 다시보기와 책·글쓰기 문화, 집필 경험을 소개하는 행사 안내 글이다. 구체적인 기술 문제 해결이나 도구·기술의 업무 적용 과정과 결과를 다루지 않는다. |
| woowahan/14644 | 13 | 제외/회고·문화·행사 | 0 | WOOWACON 2023 참가 등록을 안내하는 행사 홍보 글로, 기술 문제 해결이나 구체적인 기술 적용 경험을 다루지 않습니다. |
| woowahan/15488 | 1,176 | 제외/회고·문화·행사 | 0 | 우아콘 세션을 소개하고 다시보기 일정을 안내하는 행사·발표 홍보 글이며, 주문 시스템이나 Module Federation의 구체적인 문제 해결 과정과 근거는 본문에 제시되지 않았다. |
| woowahan/15983 | 1,159 | 제외/회고·문화·행사 | 0 | 우아한테크세미나의 다시보기와 강연 주제·목차·대상·연사 정보를 소개하는 행사 안내 글이며, 구체적인 기술 문제 해결이나 업무 적용 결과를 다루지 않는다. |
| woowahan/17163 | 1,110 | 제외/회고·문화·행사 | 0 | 우아한테크세미나의 다시보기와 강연 내용을 소개하는 행사 안내 글이다. Virtual Thread의 원리와 성능 테스트가 목차 수준으로만 제시되어 있고, 구체적인 해결 과정·설계 결정·적용 결과가 본문에 서술되어 있지 않다. |
| woowahan/17328 | 85 | 제외/회고·문화·행사 | 0 | 우아한스터디 여름 시즌 모집을 안내하는 행사·스터디 홍보 글로, 기술 문제 해결이나 구체적인 기술 적용 사례를 다루지 않습니다. |
| woowahan/17713 | 1,163 | 제외/회고·문화·행사 | 0 | 글로벌 개발자 커리어를 주제로 한 세미나와 다시보기 안내 글로, 행사 일정·강연 내용·연사 소개가 중심이며 구체적인 기술 문제 해결이나 실무 적용 사례는 제시하지 않는다. |
| woowahan/19317 | 1,157 | 제외/회고·문화·행사 | 0 | 우아한테크세미나 다시보기와 강연 주제·목차를 소개하는 행사 안내 글이다. 생성형 AI와 로컬 LLM 활용 사례가 나열되어 있지만 구체적인 설정, 문제 해결 과정, 적용 결과나 근거는 본문에 제시되지 않았다. |
| woowahan/19470 | 600 | 제외/회고·문화·행사 | 0 | 컨퍼런스 개최와 참여형 세션·멘토링 신청을 안내하는 행사 홍보 글이며, 구체적인 기술 문제 해결이나 실무 적용 사례를 다루지 않는다. |
| woowahan/20702 | 1,298 | 제외/회고·문화·행사 | 0 | 여러 기술 콘퍼런스의 LLM 사례를 소개하고 세미나 및 패널토크 참여를 안내하는 행사 홍보·다시보기 글이다. 구체적인 문제 해결 과정이나 설계 근거, 적용 결과는 본문에 제시되지 않았다. |
| woowahan/20789 | 333 | 제외/회고·문화·행사 | 0 | 기술 콘퍼런스 발표 영상 공개를 안내하는 행사 홍보 글이며, 구체적인 기술 문제 해결 과정이나 설계·적용 근거를 다루지 않는다. |
| woowahan/22828 | 1,095 | 제외/회고·문화·행사 | 0 | 우아한테크코스의 교육 철학과 지원을 홍보하는 모집 글로, 개발자 역량과 도전 문화를 강조할 뿐 구체적인 기술 문제 해결이나 업무 적용 사례를 다루지 않는다. |
| woowahan/23037 | 409 | 제외/회고·문화·행사 | 0 | 기술 콘퍼런스 개최와 세션·멘토링 참여를 안내하는 행사 홍보 글이며, 구체적인 기술 문제 해결이나 실무 적용 근거를 다루지 않습니다. |
| woowahan/24005 | 1,451 | 제외/회고·문화·행사 | 0 | 개인정보처리방침의 개정 사항과 시행 일자를 안내하는 공지로, 기술 문제 해결이나 기술 도입·적용 사례를 다루지 않는다. |
| woowahan/27782 | 456 | 제외/회고·문화·행사 | 0 | 기술 콘퍼런스 개최를 안내하는 행사 홍보 글로, 구체적인 기술 문제 해결 과정이나 설계·적용 근거를 다루지 않습니다. |

## 글당 항목 수 (제외 글 빼고)

| 항목 수 | 글 수 |
| --- | --- |
| 1 | 600 |
| 2 | 112 |
| 3 | 124 |
| 4 | 19 |
| 5 | 7 |
| 8 | 1 |

## 문제 유형 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 개발 생산성 | 368 | 28% |
| 검색·추천·모델 품질 | 203 | 15% |
| 장애 대응·복구 | 186 | 14% |
| 모니터링·관측성 | 160 | 12% |
| 인프라·컨테이너 | 146 | 11% |
| 업무·운영 자동화 | 129 | 10% |
| 데이터 파이프라인 | 125 | 10% |
| 데이터 정합성·트랜잭션 | 121 | 9% |
| API 설계·외부 연동 | 120 | 9% |
| DB 성능·쿼리 최적화 | 110 | 8% |
| 비용 절감 | 104 | 8% |
| 인증·보안 | 103 | 8% |
| 클라이언트 성능(웹·앱) | 101 | 8% |
| 메시징·비동기 처리 | 98 | 7% |
| 배포·CI/CD | 95 | 7% |
| 테스트 자동화 | 84 | 6% |
| 트래픽 급증 대응 | 74 | 6% |
| 캐싱 | 52 | 4% |
| 동시성·락 | 51 | 4% |
| MSA | 41 | 3% |
| DB 마이그레이션·샤딩 | 34 | 3% |

- 한 번도 안 쓰인 분류 (0개): 없음

## 도메인 분포 (항목 대비 비율, 다중 선택)

| 분류 | 항목 수 | 비율 |
| --- | --- | --- |
| 사내 플랫폼·개발 도구 | 363 | 28% |
| LLM·AI | 313 | 24% |
| 커머스·주문·재고 | 264 | 20% |
| 결제·금융 | 172 | 13% |
| 범용 | 130 | 10% |
| 검색·추천 | 103 | 8% |
| 배달·물류 | 101 | 8% |
| 채팅·메시징 서비스 | 70 | 5% |
| 콘텐츠·미디어 | 62 | 5% |
| 광고·마케팅 | 45 | 3% |

- 한 번도 안 쓰인 분류 (0개): 없음

## 발췌 검증

- 채택한 시도 기준 발췌 12414개 중 탈락 79개 (원문 존재율 99%)
- 재시도한 글 267편

- `d2/3010710`: const paths = await glob('**/*.js', {
            ignore: ['node_modules/**', '**/*.spec.*', 'transpiled/framework/MessageFramework.test.js'],
        });
- `d2/0207214`: 홈피드에서는 블로그, 카페, 포스트, 네이버TV, 인플루언서, 프리미엄 콘텐츠, 클립 등 다양한 콘텐츠를 개인화해 제공하고 있으며, 사용자의 취향에 맞춘 콘텐츠 묶음 형태로도 제공하고 있습니다.
- `d2/6388660`: Plasma 프로젝트를 마무리하기 위해서는 복제 도구까지 주문 개발으로 내재화해야 했는데, 기존 도구를 그대로 인수인계하기에는 백엔드 개발자 입장에서 유지 보수와 추가 개발이 어려웠습니다.
- `d2/0004394`: 1 |
설정된 최대 처리 속도의 5배까지 처리 |

2 |
설정된 최대 처리 속도만큼 처리 |

3 |
설정된 최대 처리 속도 X 실시간 보장 비율 만큼만 실시간 처리
- `d2/5788040`: 쿼리 1건당 메모리 점유율은 기존 45%에서 12% 수준으로 크게 낮아졌습니다. API 응답 시간도 최대 40초에서 7초로 단축되었습니다.
- `d2/5788040`: 배포 후 약 1.5개월 동안 Data 영역의 디스크 사용량은 약 8.7% 감소했습니다. 보관 기간이 모두 지나 기존 데이터의 만료와 삭제가 완료되면 줄어든 유입량이 온전히 반영되어, 전체 영역의 디스크 사용량은 기존 대비 약 58%까지 감소할 것으로 예상됩니다.
- `kakao/678`: 기존 라이브 서버 개발 당시 저희 조직의 개발자들은 모두 Java 개발자였고, Spring에 친숙했습니다.
- `kakao/690`: 이 방식에서는 System message와 User message가 명확하게 구분되지 않고 하나의 흐름으로 인식됩니다. 이로 인해 평가 모델이 태스크의 핵심 기준을 명확히 이해하지 못하고, 두 모델의 응답을 평가할 때 대부분 무승부로 평가되어 변별력이 떨어지는 경향이 나타났습니다.
- `kakao/707`: 하지만 DPO의 경우 optimal policy와 implicit reward 사이의 closed-form solution을 이용한 관계성을 이용하고 있지만, 근본적으로는 reward model 학습법을 목적함수로 사용하고 있기 때문에 이로 인해 얻어지는 policy 모델이 이전 버전보다 더 좋다 라는 보장 혹은 목적성을 직접적으로 내포하고 있지 않습니다.
- `kakao/724`: Stage I에서는 8×10−5→8×10−68 	imes 10^{-5} 	o 8 	imes 10^{-6}8×10−5→8×10−6 스케줄이 pass@8 = 0.667, avg@8 = 0.304로 가장 높은 성능을 보였습니다.
- `kakao/724`: Stage II에서는 3×10−5→3×10−63 	imes 10^{-5} 	o 3 	imes 10^{-6}3×10−5→3×10−6 스케줄이 pass@1 = 0.367, pass@8 = 0.700, avg@8 = 0.371로 최고 성능을 기록했습니다.
- `kakao/803`: 이렇듯 리샤딩은 모든 데이터를 임시 컬렉션에 복제하는 방식이어서 수행 전에 충분한 디스크 공간이 필요하며, 리샤딩 과정 중 자원 사용량의 증가로 서비스 워크로드에 따라 영향을 받을 수 있음을 고려해야 합니다.
- `kakao/810`: 구조 적용 이후 DB 기준 리포트 누락은 0%로 줄어들었지만, 과금 이벤트 누락은 오히려 이전보다 더 눈에 띄게 증가하기 시작했습니다.
- `kakao/827`: 이에 저희는 현재 모델이 직접 음성을 생성하고, 생성 결과를 평가한 뒤, 그 결과를 다시 모델 업데이트에 반영하는 온라인 강화학습(Online RL)[9,10]을 음성발화 모델에 적용하였습니다.
- `kakaopay/bluetooth-remittance`: 내 주변 송금에서는 사용자의 이름을 모두 담지 않고 앞 글자와 뒷글자, 그리고 글자 수를 담아 마스킹하여 표시할 수 있도록 정의하였습니다.
- `kakaopay/bluetooth-remittance`: while (isActive) {
        delay(5_000L)
        viewModel.updateMonitoringResult(bufferedResult)
    }
- `kakaopay/bluetooth-remittance`: 그래서 처음엔 UUID가 아닌 객체를 새롭게 만들어서 넘겨줘야 한다고 생각했습니다.
- `kakaopay/bluetooth-remittance`: 그런데, 데이터를 주고받는 객체를 UUID 객체에 넣어서 보내야 하는데, EUC-KR은 Int8이었고 UUID객체가 요구하는 데이터 타입은 UInt8이어서 인코딩 및 디코딩 과정에서 데이터 변형이 있지 않을까 하는 생각이 들었습니다.
- `kakaopay/url-is-strange`: 그리고 위험성에 공감하신 크루들의 추천으로 카카오페이 전사 소나큐브에 커스텀 룰로 등록될 수 있었습니다.
- `kakaopay/ifkakao2024-delayed-transfer`: 한 번에 얼마나 Consume 할지 정하는 값은 송금 실행 내부 서버 부담과 목표 송금 실행 시간을 고려하여 20으로 설정했습니다. 여기서 스레드 수는 몇 개로 해야 하는가에 대해서는 목표 실행 시간과 송금 실행 서버 부담을 고려하여 10개로 설정했습니다.
- `kurly/bulk-performance-tuning`: 이런 상황에서 BULK 처리의 성능을 높이기 위해서 JDBC의 batchUpdate를 이용해 INSERT INTO … VALUES (…), (…), (…), ... 형태의 쿼리가 실행되도록 개선할 수 있습니다.
- `kurly/bulk-performance-tuning`: JPA의 영속성과 JDBC는 다르기 때문에 함께 사용할 경우 JPA의 영속성에 대해 더욱 주의해야 합니다.
- `kurly/tc-optimization`: 하지만 각 TC의 담당 권역들이 최대한 한 데 모여있는 것이 추후 실행에 더 유리합니다.
- `ly/improve-operation-environment-with-rundeck`: 다만 Ansible을 학습하지 않는다면 이해하기 어렵거나 굳이 보이지 않아도 되는 항목들이 화면에 노출되고 있어서 사용 난이도가 조금 높다고 느꼈습니다.
- `ly/improve-operation-environment-with-rundeck`: 사실 서비스를 운영하면서 가장 많은 시간을 잡아먹는 작업은 서버 설치나 설정 동기화 작업이 아니었습니다. 로그 추출이나 덤프 작업, 파일 확인, ACL(access control list) 확인, 이슈 확인을 위한 모니터링 정보 수집 등 간헐적인 이슈에 대응하기 위해 특정 서버에서 명령어를 직접 실행하는 비정기적인 임시 작업(이하 애드혹(ad-hoc) 작업)이었습니다.
- `ly/improve-operation-environment-with-rundeck`: 따라서 운영 환경과 개발 환경의 서버 인프라의 구성을 최대한 비슷하게 만들어 테스트를 진행할 수 있는 최소한의 신뢰성을 갖춘 환경을 확보하는 게 중요했습니다.
- `ly/check-mp4-file-has-audio-using-filereader-in-front-end`: 동영상 섬네일에 오디오 존재 여부를 표시해야 하기 때문에 확인에 시간이 오래 걸리면 안 됩니다.
- `ly/how-to-develop-font-customizing-function-in-android-app`: override fun onActivityCreated(activity: Activity, savedInstanceState: Bundle?) {
        if (needToApplyCustomFont) {
            activity.setTheme(customFontStyle)
        }
    }
- `ly/abc-user-feedback`: 이슈 화면에서는 수천 개의 피드백이 이슈 단위로 분류돼 나타나기 때문에 전체 피드백 현황을 한눈에 쉽게 파악할 수 있습니다.
- `ly/demaecan-3rd-recode-react-native-to-flutter`: 기본적으로 RN 버전에서 제공하고 있는 기본 기능은 Flutter 버전에서도 모두 구현할 수 있어야 했습니다. 따라서 PoC를 통해 검색 및 탐색 기능과 주문에서 배달 완료까지의 흐름에서 사용하는 모든 기능을 Flutter로 전환할 수 있는지 확인하는 게 가장 중요했습니다.
- `ly/increase-vm-performance-to-reduce-global-warming`: 따라서 이 문제는 각 가상 머신에게 독점해서 사용할 수 있는 디스크를 할당하면 해결할 수 있으며, 그 해결 방법은 이미 많은 클라우드 회사는 물론 LY에서도 활용하고 있는 네트워크 블록 장치입니다.
- `ly/running-redis-at-scale`: 위 작업 과정에서 최우선으로 고려해야 할 사항은 '서비스에 중단이 없을 것'입니다.
- `ly/experience-in-migrating-order-db-on-ecommerce-platform`: 따라서 동시성을 제어하기 위해 세 곳 모두 AOP(Aspect Oriented Programming)를 이용해 분산 락을 걸었는데요. 분산 락 구현체가 재진입을 허용하지 않아 프로세스가 실행되지 못했습니다.
- `ly/automate-streaming-pipeline-validation-with-kubernetes-native-workflows-1`: 이미 기존에도 하루에 수십억 건의 실시간 데이터를 처리하고 있었지만 향후 두 배, 세 배의 트래픽을 지연 없이 처리 가능한지, 가능하다면 인프라 증설 및 확장 비용이 얼마나 필요할지 추정할 수 있어야 했습니다.
- `ly/how-to-measure-noise-suppression-performance-in-line-app`: G-MOS는 NS 모듈의 전반적인 통화 품질을 평가하는 지표이기 때문에 특정 지표의 성능 개선이 필요할 때 그 영향을 직접 파악하기 어려울 수 있어 제외했습니다.
- `ly/multi-label-classification-model-for-openchat-hashtag-prediction`: 그렇기에 모델 학습 파이프라인에서 점수 분포를 자동 모니터링하고 있으며, 새로운 데이터로 여러 차례 모델을 업데이트해 오는 동안 분포가 크게 변화하지 않음을 실험적으로 확인했습니다.
- `ly/multi-label-classification-model-for-openchat-hashtag-prediction`: ALIVE 전체 대상일 때 min_top1 값을 10.0으로 설정하면 커버리지가 60% 가까이 되었지만, 11.0으로 기준을 높이면 40% 근처로 하락합니다.
- `ly/define-and-manage-kubernetes-custom-resources-with-controller`: Verda VM이라는 리소스는 실 제로 Verda의 VM과 일대일로 대응되는 커스텀 리소스입니다.
- `ly/python-multi-project-application-with-poetry`: 저희 조직은 Gradle에 익숙해진 상태에서 Python 개발을 시작했기에 이 문제를 Gradle과 비슷한 방식으로 풀기를 원했고, Python 생태계에도 비슷한 기능을 제공하는 도구가 있는지 조사한 결과 Poetry를 발견해 사용하기로 결정했습니다.
- `ly/migrating-hbase-with-hbase-replication`: 이전에는 장애가 발생하면 이 데이터가 유실돼 정확한 데이터를 산출할 수 없는 문제가 발생했었습니다.
- `ly/techniques-for-improving-code-quality-5`: 아래와 같이 외부에서 사용하는 값을 열거형 속성으로 정의하는 방법이 있습니다. 이를 통해 AccountType 열거형의 이름이나 순서 변경으로부터 외부에서 사용하는 값을 보호할 수 있습니다.
- `ly/building-a-development-environment-for-llm-apps-for-everyone`: 또한 LLM 애플리케이션을 통해서만 프롬프트를 실행해야 한다면 변숫값 변경과 같은 프롬프트의 변화에 따른 결과의 변화를 개별적으로 확인하기 어렵습니다.
- `ly/building-llmops-for-creating-testing-deploying-of-llm-apps`: LINE GAME PLATFORM에서는 Harness를 이용해 LLM 애플리케이션의 결과를 아래와 같이 지표를 통해 어느 정도 정량화해서 도메인 전문가가 쉽게 파악할 수 있도록 만들었습니다.
- `ly/efficiently-using-cpu-in-kubernetes`: 무엇보다 CPU 상한 설정을 제거하더라도 동일한 노드에 다른 파드가 존재한다는 것과 단일 스레드를 사용하는 Node.js 서버의 특징의 영향이 컸던 것으로 파악했습니다.
- `ly/thailand-call-quality-report`: 태국에서는 5G에서의 최대 영상 비트레이트가 4G에서의 최대 영상 비트레이트보다 높게 설정돼 있습니다. 5G의 물리적인 속도가 4G보다 월등히 빠른 만큼 이는 분명 합리적인 판단이었지만, 태국 현지 네트워크의 상태를 분석한 결과 그 차이가 조금 과도한 것으로 나타났습니다.
- `ly/extracting-trending-keywords-from-openchat-messages`: 검토 결과 다양성이 충분히 확보되는 편이 바람직하다고 의견이 모여 페널티 가중치가 2 이상인 구간에서 α값을 결정했습니다.
- `ly/techniques-for-improving-code-quality-20`: 이 코드에서는 block과 dispose에서 모두 예외가 발생하면 block에서 발생한 예외를 우선합니다.
- `ly/finishing-a-1-month-assignment-in-5-days-with-vibe-coding`: 그래서 전략을 바꿨습니다. 전체 작업을 5단계로 쪼개고 각 단계 산출물을 다음 단계 입력으로 넘기는 짧은 프로세스를 만들었습니다.
- `ly/connecting-thousands-of-services-with-central-dogma-control-plane`: 또한 쿠버네티스 엔드포인트 플러그인을 이용해 쿠버네티스 노드의 정보도 가져오고 있습니다.
- `ly/the-evolution-of-the-ly-observability-platform`: 또한 S3 호환 저장소 도입으로 운영 복잡도가 크게 낮아졌으며, 더 나아가 주요 컴포넌트들을 쿠버네티스 환경으로 이관함으로써 운영 효율성까지 한층 높일 수 있었습니다.
- `ly/building-ai-code-review-platform-with-claude-code-action`: 포크 저장소에서 생성된 PR은 브랜치가 베이스 저장소(origin)가 아니라 외부 저장소에 존재하기 때문에 이 전제를 만족할 수 없어 실행 실패로 이어졌습니다.
- `ly/on-device-image-model-trainer-for-messenger-2`: 학습에 사용한 데이터의 내부를 살펴보니 캡션 품질이 불균일했습니다. 짧은 캡션과 장황한 캡션이 혼재되어 있었고, 이미지 내 텍스트를 읽으려는 OCR 시도 같은 불필요한 정보도 많았습니다.
- `ly/on-device-image-model-trainer-for-messenger-2`: 이후 자기회귀로 학습한 모델을 교사 모델로 설정하고 자기회귀 방식으로 생성한 캡션으로 학생 모델인 비자기회귀 모델을 학습시켰습니다.
- `ly/unification-of-group-chat-on-the-line-app`: 프로젝트 진행 결과 현재 동일한 구성원으로 생성되는 대화방의 비율이 15%(여러 명과의 대화)에서 0.78%(초대 없는 그룹 대화)로 감소했습니다.
- `ly/reduce-repetitive-tasks-with-sre-bot`: Slack 메타데이터 API는 조회 성능이 느려 이모지 클릭 같은 실시간 상호작용에 적합하지 않습니다.
- `ly/from-hive-to-iceberg-12x-faster-data-updates`: 문제를 분석해 본 결과 Iceberg와 Flink의 특정 식별자 설정을 누락한 것이 문제였습니다. Iceberg는 일반적인 데이터베이스의 기본키(프라이머리 키)와 유사한 역할을 하는 identifier-field-ids 설정을 통해 동일한 엔티티를 식별합니다. Flink 역시 이와 연동되는 equalityFieldColumn이라는 설정을 제공합니다.
- `ly/git-automation-mcp-vs-agent-skills-pros-and-cons`: - 버전: 0.1.0 → 0.2.0 (minor 버전 업)
- `ly/techverse2026-60`: 조치 착수부터 완료까지 적게는 수일에서 많게는 수주까지 걸리는 경우가 있습니다.
- `ly/techverse2026-219`: 완벽하지는 않습니다. 토론이 잘못 수렴하는 경우도 있고, 대규모 스펙은 여전히 잘 안 되며, 탐색적 작업은 빌드 단계 전에 리서치가 필요한 경우가 많고, 실제로 비용 오버헤드도 존재합니다.
- `ly/ai-agent-platform-sage-dev-log-part-1`: 현재 보안 분석 워크벤치에는 다음과 같은 네 가지 워크플로가 포함돼 있습니다.
- `oliveyoung/2023-10-10_oliveyoung-pickup-cart`: 위 두 가지의 경우 고객은 픽업에 대한 인지가 어렵고 주문서까지 와서 매장을 선택하여 상품의 재고가 있는지 체크를 해야함으로써 불편함이라는 문제점을 갖고 있었습니다.
- `oliveyoung/2024-04-19_pos-modernization`: 결과는...! 네트워크 홉이 늘어남으로써 응답속도가 다소 늘긴 했지만, API의 성능으로 봤을 때 유의미한 수치가 아니란 판단을 내리게 됩니다.
- `oliveyoung/2024-10-17_oy-delivery-mq`: 또한, 새로 만드는 시스템에서는 실시간 전송이 가능하고, 추후 주문량이 늘어나는 경우를 대비해 더 많은 대용량 데이터 전송이 가능하고, 일방적으로 보내주는 데이터이기에 여기에 적합한 MQ를 사용하는 방식을 사용하기로 했습니다.
- `oliveyoung/2024-11-06_who-caused-our-batch-to-stop`: 정리해보면, 서비스 메소드에서 트랜잭션을 Propagation.REQUIRES_NEW로 제대로 분리해 설정했었더라면 이런 문제를 예방할 수 있었을 겁니다. 추가로 CallerRunsPolicy 정책을 사용하면서도 메인 스레드에서 작업을 수행하지 않으려면 최대 스레드 수를 조정하거나 큐 길이를 무한으로 설정하는 등의 방안도 고려할 수 있습니다.
- `oliveyoung/2025-12-24_amazon-connect`: 이에 이메일(Amazon SES)을 온콜 트리거로 선택했습니다.
- `oliveyoung/2025-12-24_amazon-connect`: 가이드에는 다음과 같은 내용을 포함했습니다:
- `toss/monitoring-traffic`: 또한 최적화한 버전을 Canary로 배포하면서 장애가 발생하는지, 이전 버전과 비교하여 성능 개선이 유의미한지 모니터링을 해야 합니다.
- `toss/lightning-talks-package-manager`: 지금은 효용 대비 부담이 커서 Zero-install 을 기본으로 끄는 방향으로 가고 있습니다.
- `toss/undercover-silo-2`: 인플로우 사일로의 궁극적 목표는 바이럴 K(공유 시도율 × 공유 성공률 × 인당 초대자 수)를 끌어올리는 것이었어요.
- `woowahan/15469`: ①-Viewer request에서 user-agent로 bot임을 판단하면, ④-Viewer response에서 body를 OG meta tag들만 있는 HTML 파일로 교체(이 때, 기존의 body 내용은 참고하지 않습니다)하여 bot에게 리턴한다.
- `woowahan/20161`: "categoryId": {
    "type": "integer"
    "fields": {
        "keyword": {
            "type": "keyword"
        }
    }
  }
- `woowahan/20627`: ‘사업자정보 입력’ 단계는 총 6개의 퍼널(사업자등록증 정보 입력, 영업신고증 정보 입력, 본인인증, 만나서결제 사용여부, 주문접수채널 설정, 정산계좌 등록)으로 구성되어 있었고, 특히 사업자등록증과 영업신고증에 있는 정보를 모두 수기로 입력해야했기 때문에 큰 허들이 되었습니다.
- `woowahan/20371`: 마이그레이션 완료 후에도 이를 유지하면 불필요한 자원 소모로 이어질 수 있습니다.
- `woowahan/20156`: 쓰로틀링 대상이 되는 MessageListenerContainer의 개수(ConcurrentMessageListenerContainer 내부 포함)를 넘어서는 스레드가 사용되지 않으므로 고려해서 크기를 결정한다.
- `woowahan/21027`: 2차 실험에 대한 정리를 해보면, 저희 시나리오에서는 RDS가 가장 좋은 성능을 보여주는 것을 확인했습니다.
- `woowahan/23377`: 이런 부분을 보완하기 위해 매주 한 번 기한이 지난 티켓에 대해서 담당자에게 메신저 알림을 통해 알려주는 자동화를 운영하고 있습니다.
- `woowahan/25900`: 문제는 교육 정보를 파악하기 위해 여러 시스템을 매번 개별적으로 확인해야 했다는 점이었습니다.
- `woowahan/26492`: 그런데 NACL 생성이 조용히 실패한 경우에도 DDB에는 차단된 것으로 기록이 남았습니다. 게다가 NACL이 정상 응답(HTTP 200)을 받은 직후 바로 readback으로 룰의 실제 존재를 확인하는 단계도 없어서, AWS API의 일시적인 일관성 지연으로 룰이 잠시 안 보이는 순간 역시 같은 결과로 이어질 수 있었습니다.
- `woowahan/26624`: 코드는 한 줄도 써 본 적이 없었고 디자인도 Git도 GitLab도 처음이었지만, 마침 Claude가 전사 표준 AI 도구로 도입되며 사내 AI 교육 세션도 열려서 교육을 들으며 직접 만들어 보기로 했습니다.

## 기술 사전에 없는 이름 1069종

- Yarn (8)
- Central Dogma (7)
- es-toolkit (4)
- 카카오톡 (4)
- LLM (4)
- Kanana (4)
- YARN (4)
- Web Worker (3)
- WebView (3)
- PCIe (3)
- Canvas API (3)
- Orchestrator (3)
- Kanana Safeguard (3)
- Kanana Safeguard-Siren (3)
- Kanana Safeguard-Prompt (3)
- PPO (3)
- Kanana-1.5-3b-instruct (3)
- Kanana Essence (3)
- Kanana Nano (3)
- Athenz (3)
- asyncio (2)
- Chromium (2)
- SGLang (2)
- DeepSeek (2)
- DCGM Exporter (2)
- BERT (2)
- Jotai (2)
- ADB (2)
- macOS (2)
- TestRail (2)
- Spark Operator (2)
- HTTP/3 (2)
- Redash (2)
- Chrome (2)
- async-profiler (2)
- ts-morph (2)
- Harbor (2)
- Groovy (2)
- Async Profiler (2)
- AWS WAF (2)
- tree-sitter (2)
- ctags (2)
- ripgrep (2)
- Pydantic (2)
- springdoc (2)
- Apache Druid (2)
- Notion (2)
- Struts (2)
- JSP (2)
- MCP Inspector (2)
- GitHub Enterprise (2)
- Aerospike (2)
- unified (2)
- chokidar (2)
- @use-funnel/core (2)
- H2 (2)
- Infiniband (2)
- CircleCI (2)
- Recoil (2)
- Babel (2)
- Express (2)
- CloudFront Functions (2)
- fio (2)
- MDX (2)
- remark (2)
- Deno (2)
- Reactor Netty (2)
- Feign (2)
- ShedLock (2)
- Bootstrap (2)
- i18next (2)
- AWS Bedrock Knowledge Bases (2)
- AWS STS (2)
- @tanstack/react-query (2)
- Lighthouse (2)
- Node2Vec (2)
- Transformer (2)
- Google Drive (2)
- Opsgenie (2)
- MQTT (2)
- KEDA (2)
- Karpenter (2)
- LiteLLM (2)
- Chrome DevTools (2)
- Chrome DevTools Protocol (2)
- Charles (2)
- Athena (2)
- QuickSight (2)
- Jetson (2)
- torchvision (2)
- MobX (2)
- AWS Athena (2)
- AWS Secrets Manager (2)
- Jest (2)
- Uvicorn (2)
- Testcontainers (2)
- WireMock (2)
- Vitest (2)
- @rushstack/eslint-config (2)
- CodePush (2)
- StrongBox (2)
- OpenFeign (2)
- Turborepo (2)
- MockServer (2)
- Boto3 (2)
- LM-SPT (2)
- Kanana-a (2)
- Jupyter Notebook (2)
- JMH (2)
- Flash Attention (2)
- WiredTiger (2)
- DataTrove (2)
- Kanana-o (2)
- Kanana-v (2)
- Perl (2)
- v0 (2)
- JaCoCo (2)
- SQLite (2)
- Windsurf (2)
- Vercel (2)
- PM2 (2)
- Docker Compose (2)
- ORC (2)
- verl (2)
- Voicebox (2)
- Prometheus Pushgateway (2)
- Kanana Flag (2)
- Ingress Nginx Controller (2)
- Graphviz (2)
- go-json (2)
- Intel Xeon Silver 4410Y (2)
- Intel Xeon Silver 4214 (2)
- Querydsl-SQL (2)
- Amazon API Gateway (2)
- CodeDeploy (2)
- AWS EKS (2)
- AWS Application Load Balancer (2)
- MySQL Connector/J (2)
- Ktor (2)
- Micrometer (2)
- Amazon SageMaker (2)
- YOLO (2)
- TrOCR (2)
- R2DBC (2)
- Block Kit (2)
- Spinnaker (2)
- Spring Actuator (2)
- Amazon Athena (2)
- Exposed (2)
- Avro (2)
- AWX (2)
- Bluetooth Low Energy (2)
- Storm (2)
- Stable Diffusion (2)
- MapReduce (2)
- JuiceFS (2)
- Place sLLM (2)
- client-go (2)
- Beacon API (2)
- Toxiproxy (2)
- OpenAI Python SDK (2)
- OpenCode (2)
- OpenTofu (2)
- Ceph (2)
- LiteRT (2)
- ML Kit (2)
- Apache Cassandra (2)
- Armeria (2)
- MaxMind GeoIP2 City DB (2)
- Nbase-T (2)
- LINE (2)
- Docusaurus (2)
- Harness (2)
- Jinja2 (2)
- Xamarin (2)
- Kotlin Multiplatform Mobile (2)
- TestFlight (2)
- platform_maps_flutter (2)
- WebAuthn (2)
- Tekton (2)
- Hubot (2)
- Obsidian (2)
- Nx (2)
- Bun (2)
- iTerm (2)
- GrowthBook (2)
- Apollo Client (2)
- JDBC Connector (2)
- 행안부 도로명 주소조회 API (2)
- Gradio (2)
- OR-Tools (2)
- CP-SAT (2)
- SCIP (2)
- AWS Batch (2)
- AppsFlyer (2)
- Spring Boot Actuator (2)
- Amazon MemoryDB (2)
- AWS ECS (2)
- AWS CodeDeploy (2)
- AWS Media Converter (2)
- HLS.js (2)
- FFmpeg (2)
- Selenium (2)
- Gherkin (1)
- WebKit (1)
- Kimi (1)
- GLM (1)
- Bugsnag (1)
- Firebase Crashlytics (1)
- NVIDIA Container Toolkit (1)
- nvidia-validator (1)
- GPU Feature Discovery (1)
- DCGM (1)
- GPU Operator (1)
- MIG Manager (1)
- Neo4j (1)
- Rspack (1)
- yarn-plugin-catalogs (1)
- MRAID (1)
- CDN (1)
- Jupyter (1)
- commons-ml-model (1)
- pip (1)
- pfmls-stylepack (1)
- XCTest (1)
- scrcpy (1)
- Recharts (1)
- K-Means (1)
- NMF (1)
- PyYAML (1)
- gitleaks (1)
- Toss Front (1)
- Snowflake (1)
- dbt (1)
- Edge (1)
- AWS CDK (1)
- CloudFormation (1)
- Zabbix (1)
- Cluster API (1)
- CAPO (1)
- OCCM (1)
- BigIP (1)
- Argo Rollout (1)
- Global Accelerator (1)
- AWS Roles Anywhere (1)
- AWS Private Link (1)
- Job-DSL (1)
- IPS (1)
- WAF (1)
- Wazuh (1)
- Falco (1)
- Falco Sidekick (1)
- LangSmith (1)
- Instructor (1)
- SAP (1)
- Token Studio (1)
- Style Dictionary (1)
- Job DSL (1)
- Electron (1)
- @toss-place/plugin-sdk (1)
- @tossplace/pos-plugin-sdk (1)
- WebLogic (1)
- Databricks Iceberg Sink Connector (1)
- SpringDoc (1)
- SHAP (1)
- HTTP (1)
- iBATIS (1)
- Kotlin Reflections (1)
- JGit (1)
- GitHub App (1)
- Log4j (1)
- conntrack (1)
- Google Ads (1)
- PyTorch Lightning (1)
- Feast (1)
- remark-parse (1)
- unist-util-visit (1)
- dcgm-exporter (1)
- nvidia-smi (1)
- EnumString (1)
- WebP (1)
- Granite (1)
- React Navigation (1)
- @parcel/watcher (1)
- Flowise (1)
- Springdoc (1)
- Metro (1)
- react-refresh (1)
- @react-navigation/native (1)
- @use-funnel (1)
- react-navigation-native (1)
- ts-pattern (1)
- @tossteam/react (1)
- CocoaPods (1)
- Xcodeproj (1)
- RestAssured (1)
- ApprovalTests.Java (1)
- Confluent Schema Registry (1)
- DataFlint (1)
- SATA3 (1)
- NVMe (1)
- NVLink (1)
- NVSwitch (1)
- Ethernet (1)
- DevOn (1)
- Apache Sqoop (1)
- Spring Expression Language (1)
- Module Federation (1)
- react-helmet (1)
- OpenZFS (1)
- AWS EBS (1)
- LZ4 (1)
- TDS (1)
- @tosspayments/log-core (1)
- @tosspayments/log-react (1)
- @tosspayments/log-tds (1)
- Spring JDBC (1)
- Wireshark (1)
- Apache HttpClient (1)
- @tosspayments/payment-widget-sdk (1)
- @rollup/browser (1)
- esm.sh (1)
- sucrase (1)
- GoCD (1)
- gocd-yaml-config-plugin (1)
- Reactor-Netty (1)
- Node Exporter (1)
- Active Directory (1)
- Ant Design (1)
- 클로드 코드 (1)
- Web Audio API (1)
- react-i18next (1)
- typescript-eslint (1)
- openapi-typescript (1)
- Amazon OpenSearch Serverless (1)
- AWS Bedrock Guardrails (1)
- @modelcontextprotocol/sdk (1)
- ELECTRA (1)
- API Gateway (1)
- botocore (1)
- @types/react (1)
- @types/react-dom (1)
- @sentry/react (1)
- Figma Make (1)
- Claude Design (1)
- Amazon Nova 2 Lite (1)
- VoiceOver (1)
- TalkBack (1)
- 배달의민족 (1)
- zxing.js (1)
- Item2Vec (1)
- Google Calendar (1)
- WebAssembly (1)
- Rust (1)
- BLoC (1)
- Sparkle (1)
- Vanilla Extract (1)
- AWS Shield (1)
- Azure (1)
- devtools-frontend (1)
- IndexedDB (1)
- AWS IoT (1)
- rrweb (1)
- Valkey (1)
- Apache Commons Pool (1)
- Jira Automation (1)
- Superset (1)
- OSRM (1)
- AWS Cost Anomaly Detection (1)
- AWS Budgets (1)
- immer (1)
- Google Docs (1)
- Drone CI (1)
- EMR (1)
- Mixpanel (1)
- RADIUS (1)
- EAP-TLS (1)
- GlobalSign (1)
- day.js (1)
- Amazon EMR (1)
- sql-metadata (1)
- sqlglot (1)
- pytorch-quantization (1)
- Netron (1)
- DNS Firewall (1)
- Google 스프레드시트 (1)
- S2 Geometry (1)
- libevent (1)
- fastutil (1)
- Hazelcast (1)
- Chronicle Map (1)
- HPPC (1)
- Trove (1)
- Koloboke (1)
- Amazon RDS for PostgreSQL (1)
- pgvector (1)
- IntersectionObserver API (1)
- Noto Sans (1)
- Spoqa Han Sans (1)
- Inter (1)
- Interop (1)
- postgres_fdw (1)
- Mock Service GUI (1)
- 클로바 OCR API (1)
- AWS Cost Explorer (1)
- GCP Vertex AI (1)
- Naver Cloud Platform (1)
- Testing Library (1)
- TensorFlow (1)
- CatBoost (1)
- Scikit Learn (1)
- Docker Registry (1)
- oasdiff (1)
- Kubecost (1)
- Spring Statemachine (1)
- Kryo (1)
- LinkedBlockingQueue (1)
- SQLGlot (1)
- Polygraphy (1)
- Microsoft Azure OpenAI (1)
- Langserve (1)
- Polars (1)
- Pandas (1)
- Dask (1)
- H3 (1)
- Apache Arrow (1)
- pgVector (1)
- K3s (1)
- kubectl (1)
- NVIDIA Jetson (1)
- Trtexec (1)
- TREx (1)
- Nsight Systems (1)
- Trt-Infersight (1)
- JetPack (1)
- tegrastats (1)
- Spring Cloud Contract WireMock (1)
- JsonUnit (1)
- HttpBin (1)
- @vitejs/plugin-legacy (1)
- @juggle/resize-observer (1)
- React Testing Library (1)
- Testing Library User Event (1)
- LTE 라우터 (1)
- IPSEC (1)
- eslint-config-airbnb (1)
- @rushstack/eslint-patch (1)
- eslint-plugin-no-relative-import-paths (1)
- prettier-plugin-tailwindcss (1)
- gif.js (1)
- Hangul.js (1)
- Selection API (1)
- react-native-keychain (1)
- Android Keystore (1)
- Nori (1)
- ahocorasick (1)
- next-transpile-modules (1)
- craco (1)
- workspace-tools (1)
- cli-select (1)
- chalk (1)
- plopjs (1)
- Superstruct (1)
- LocalStack (1)
- TestContainers (1)
- MockMvc (1)
- PyMySQL (1)
- Requests (1)
- Miro (1)
- FigJam (1)
- Google Tag Manager (1)
- AWS SDK for Java (1)
- Vault (1)
- Cinder (1)
- VS Code for Web (1)
- JFR (1)
- jstack (1)
- MaxText (1)
- TPU (1)
- Nemotron (1)
- GradCache (1)
- Apps Script (1)
- clasp (1)
- Cucumber (1)
- OpenAI SDK (1)
- DeepGEMM (1)
- TransformerEngine (1)
- Lustre (1)
- Prefect (1)
- Toucan (1)
- YCSB (1)
- mongo-perf (1)
- TCMalloc (1)
- Kanana-v-embedding (1)
- VLM2Vec (1)
- DALL-E (1)
- FSDP (1)
- DeepSpeed (1)
- UI-Venus (1)
- GTA1 (1)
- ERes2Net (1)
- Strimzi (1)
- MHA (1)
- Google OAuth2 (1)
- Inception-ResNet-v2 (1)
- EfficientNet (1)
- Swin Transformer (1)
- GradCAM (1)
- A100 (1)
- DeviceFarm (1)
- TTS (1)
- Flask (1)
- Tabnine (1)
- Trae (1)
- Void (1)
- Firebase Studio (1)
- Bolt.new (1)
- Lovable (1)
- Supabase (1)
- Goose (1)
- Aider (1)
- InnoDB (1)
- @neshca/cache-handler (1)
- NotebookLM (1)
- Sysbench (1)
- pm2-metrics (1)
- Grafana Alloy (1)
- Scala (1)
- scalafmt (1)
- scalafix (1)
- caching_sha2_password (1)
- mysql_native_password (1)
- sha256_password (1)
- Genspark (1)
- AM-DeepSeek-Distilled-40M (1)
- AceReason-1.1-SFT (1)
- DeepDistill (1)
- DeepMath-103K (1)
- DeepMath-62K (1)
- GRPO (1)
- AceReason-Nemotron 1.1 (1)
- DeepSeekMath (1)
- PickScore (1)
- Kanana-1.5-v-9.8b-instruct (1)
- Open-RLHF (1)
- Cutlass (1)
- Univnet (1)
- StyleTTS2 (1)
- Apache ORC (1)
- Firestore (1)
- RxJS (1)
- NuminaMath (1)
- YaRN (1)
- ingress-nginx (1)
- ngx-quicklink (1)
- LLM2Vec (1)
- cAdvisor (1)
- gobwas (1)
- BMS (1)
- Ruby (1)
- 카카오워크 (1)
- Honeybee (1)
- NaViT (1)
- Kanana LLM (1)
- Pickscore (1)
- Aesthetic score (1)
- Atlassian JIRA (1)
- Singleflight (1)
- OLIVE Platform (1)
- OLIVE CLI (1)
- Safebot (1)
- VMWare (1)
- ESXi (1)
- Intel Xeon (1)
- VMWare ESXi (1)
- Hive Metastore (1)
- Apache Flink CDC (1)
- VMware (1)
- VMware ESXi (1)
- Storybook.js (1)
- oror-forge/react (1)
- react-share (1)
- ConvNext (1)
- ResNet (1)
- Trident (1)
- OpenAI Triton (1)
- ts-node (1)
- tsconfig-paths (1)
- zap (1)
- slog (1)
- Reach (1)
- CGLIB (1)
- Spec-kit (1)
- Yarn Berry (1)
- Spring Data (1)
- SwiftData (1)
- H200 (1)
- RDMA (1)
- GPUDirect (1)
- Knative (1)
- Grafana Image Renderer (1)
- 카카오페이 Open API (1)
- Vercel AI SDK (1)
- AWS KMS (1)
- CloudTrail (1)
- AWS Amplify (1)
- AWS Polly (1)
- AWS Transcribe (1)
- react-use-websocket (1)
- HyperDX (1)
- Amazon Knowledge Base (1)
- code-server (1)
- PlantUML (1)
- NodeLocal DNSCache (1)
- CoreDNS (1)
- AWS Network Load Balancer (1)
- Amazon Transcribe (1)
- OpenSearch Serverless (1)
- Nova Canvas (1)
- java-test-fixtures (1)
- IdeaVim (1)
- Bash (1)
- Titan (1)
- PGVector (1)
- boto3 (1)
- Guardrails (1)
- Spring Cloud Stream (1)
- Spring Integration (1)
- SLF4J (1)
- kotlin-logging (1)
- OpenCV (1)
- Core Location (1)
- Mongo (1)
- InfluxDB (1)
- GCP (1)
- 카카오클라우드 (1)
- Arrow (1)
- Scavenger (1)
- Corretto (1)
- jOOQ (1)
- TypeORM (1)
- Cilium (1)
- Hubble (1)
- Argo (1)
- sonar-plugin-api (1)
- sonar-kotlin-plugin (1)
- Jedis (1)
- Google Cloud (1)
- AskYourDatabase (1)
- Google Meet (1)
- Palsonic (1)
- r2dbc-pool (1)
- reactor-pool (1)
- jasync (1)
- kotlinx.coroutines (1)
- Canvas (1)
- AssertJ (1)
- AWS Cost & Usage Report (1)
- KubeCost (1)
- Amazon QuickSight (1)
- Gatling (1)
- Schema Registry (1)
- Talend Open Studio (1)
- mongoimport (1)
- Graviton (1)
- Thanos (1)
- HAProxy (1)
- TanStack React Query (1)
- RestTemplate (1)
- Fuel (1)
- Ktor HttpClient (1)
- Gatsby (1)
- Astro (1)
- @astrojs/image (1)
- RxKotlin (1)
- 카카오페이 (1)
- QR Code (1)
- Apache Thrift (1)
- Core Foundation (1)
- NVIDIA Nsight Compute (1)
- datasource-proxy (1)
- storm-kafka-client (1)
- TOONRADAR (1)
- IMPASTO (1)
- PhotoGuard (1)
- AdvDM (1)
- Anti-DB (1)
- Mist (1)
- SDST (1)
- AutoGen (1)
- react-window (1)
- ResizeObserver (1)
- Yappi (1)
- SnakeViz (1)
- Apache Paimon (1)
- yup (1)
- nBase-T (1)
- Hikari (1)
- Release Please Action (1)
- JFrog Artifactory (1)
- Maven Central Repository (1)
- Vanniktech Maven Publish Plugin (1)
- Ruler (1)
- Internet Explorer (1)
- egjs/Flicking (1)
- cgroups (1)
- stress (1)
- EASE (1)
- TF-IDF (1)
- TSDAE (1)
- NRMS (1)
- DCN (1)
- MDE (1)
- MMoE (1)
- LinUCB (1)
- Epsilon-Greedy (1)
- Q model-S (1)
- Kubebuilder (1)
- valgrind (1)
- Socket.IO (1)
- nBase-ARC (1)
- TRT-LLM (1)
- Triton (1)
- Model Analyzer (1)
- Performance Analyzer (1)
- XMLHttpRequest (1)
- Fetch API (1)
- Ragas (1)
- ARES (1)
- Nxcache (1)
- web-vitals (1)
- Gin (1)
- github.com/pkg/errors (1)
- MongoDB Go Driver (1)
- RequireJS (1)
- PEG.JS (1)
- CLOVA Studio (1)
- vmalert (1)
- vmauth (1)
- CDC (1)
- MirrorMaker (1)
- Katib (1)
- Zeppelin (1)
- Deequ (1)
- Great Expectations (1)
- PySpark (1)
- reactor-extra (1)
- Mocha (1)
- Chai (1)
- jsdom-global (1)
- Kuromoji (1)
- Sudachi (1)
- MeCab (1)
- Parallel Consumer (1)
- glob (1)
- mock-socket (1)
- OpenTelemetry Collector (1)
- Alertmanager (1)
- Granite Guardian (1)
- htmx (1)
- LIFF (1)
- LINE Official Account (1)
- LINE Planet (1)
- PlanetKit (1)
- Firebase Cloud Functions (1)
- ngrok (1)
- MediaPipe (1)
- Google Cloud Knowledge MCP (1)
- git-lfs (1)
- Gemini in Android Studio (1)
- OpenSpec (1)
- Nickel (1)
- Kong (1)
- golangci-lint (1)
- SQLFluff (1)
- Squawk (1)
- Devenv (1)
- Nix (1)
- direnv (1)
- gopls (1)
- Nixpkgs (1)
- DSPy (1)
- GEPA (1)
- GPT-4o-mini (1)
- superpowers (1)
- ID-JAG (1)
- Open WebUI (1)
- Ollama (1)
- Keycloak (1)
- Athenz KeycloakTokenExchangePlugin (1)
- ChromaDB (1)
- Flava (1)
- Apache Ranger (1)
- DistCP (1)
- ADK (1)
- skill-creator (1)
- git-release-mcp (1)
- MagicPod (1)
- Google Play Store (1)
- App Store (1)
- Channel Messaging API (1)
- OCR (1)
- ZSTD (1)
- Apache YuniKorn (1)
- Foundation (1)
- eBPF (1)
- FRRouting (1)
- ONNX2TF (1)
- BLIP-1 (1)
- Phi-3.5-vision-instruct (1)
- GPT-4o mini (1)
- OpenTSDB (1)
- GitHub Apps (1)
- APNs (1)
- FCM (1)
- PyPI (1)
- Vanna.ai (1)
- Plotly (1)
- PowerPoint (1)
- CCFS (1)
- Dio (1)
- Promtail (1)
- Decaton (1)
- Bolt for Python (1)
- paraphrase-multilingual-mpnet-base-v2 (1)
- Birdwatcher (1)
- True (1)
- AIS (1)
- LaMa (1)
- HINT (1)
- FLUX (1)
- MAT (1)
- MAE-FAR (1)
- ZITS++ (1)
- CoordFILL (1)
- SCAT (1)
- MxT (1)
- PUT (1)
- Phi (1)
- LINE Messaging API (1)
- Claude Desktop (1)
- httpx (1)
- Brave Search (1)
- SDXL (1)
- SD3.5 (1)
- HPS-V2 (1)
- Pick Score (1)
- Jazzy (1)
- Doxygen (1)
- JSDoc (1)
- Guava (1)
- Room (1)
- AD Exchange (1)
- HeadlessUI (1)
- Provider (1)
- Develocity (1)
- Dependency Injector (1)
- Language Model Evaluation Harness (1)
- Bolt (1)
- FIDO2 WebAuthn (1)
- Expo (1)
- Realm (1)
- SecureStorage (1)
- LiveData (1)
- newrelic_mobile (1)
- DeployGate (1)
- flutter_inappweb (1)
- flutter_app_badger (1)
- adjust_sdk (1)
- google_maps_flutter (1)
- flutter_cors (1)
- device_preview (1)
- controller-runtime (1)
- MongoDB Connector for Spark (1)
- Sqoop (1)
- Flapdoodle (1)
- ARM TrustZone (1)
- Secure Enclave (1)
- App Attest (1)
- Kubernetes Python client (1)
- Kubernetes Go client (1)
- Informer (1)
- Dart (1)
- flutter_lints (1)
- custom_lint (1)
- analyzer (1)
- custom_lint_builder (1)
- ZGC (1)
- Movable Type (1)
- Commander.js (1)
- Consola (1)
- CLI-Progress (1)
- 3QUEST (1)
- scikit-learn (1)
- multilingual-e5-large (1)
- REST API (1)
- tsup (1)
- Typesafe Config (1)
- LitmusChaos (1)
- Argo Workflows (1)
- Cassandra (1)
- DataStax Cassandra Driver (1)
- Springdoc-openapi Kotlin (1)
- springdoc-openapi-gradle-plugin (1)
- Redoc (1)
- Redocly CLI (1)
- yq (1)
- Swagger UI (1)
- ABC User Feedback (1)
- Django (1)
- Django REST framework (1)
- Ansible Runner (1)
- Supervisord (1)
- psutil (1)
- Jpype (1)
- UIKit (1)
- ktlint (1)
- kotlin-compiler-embeddable (1)
- Qemu (1)
- sysbench (1)
- iperf (1)
- NVMe-over-TCP (1)
- flutter_bloc (1)
- flutter_line_sdk (1)
- sign_in_with_apple (1)
- dio (1)
- ferry (1)
- geocoding (1)
- pay (1)
- flutter_inappwebview (1)
- firebase-messaging (1)
- build_runner (1)
- Bitrise (1)
- statsmodels (1)
- Jakarta EE (1)
- Spring Cloud Sleuth (1)
- Micrometer Tracing (1)
- Brave (1)
- Zipkin (1)
- Spring Cloud Vault (1)
- Spring Security (1)
- Flyway (1)
- Slack Workflow (1)
- Akamai (1)
- node_exporter (1)
- kube-state-metrics (1)
- FileReader (1)
- sqlite-vec (1)
- multilingual-e5-small (1)
- Kotlin Multiplatform (1)
- AECMOS (1)
- Adobe Audition (1)
- VB-AUDIO (1)
- VB-Cable (1)
- Matplotlib (1)
- SciPy (1)
- UDP (1)
- PacketStorm (1)
- POLQA (1)
- DSLA (1)
- Dependabot (1)
- Opus (1)
- SSH (1)
- QMD (1)
- Ultralytics (1)
- Taskmaster (1)
- Namastack Outbox for Spring Boot (1)
- Material-UI (1)
- PostCSS (1)
- qs (1)
- react-csv (1)
- dayjs (1)
- Vue Router (1)
- Fastify (1)
- Apollo Server (1)
- graphql-codegen (1)
- jqwik (1)
- IntelliJ Profiler (1)
- Confluent Hub (1)
- MariaDB (1)
- 행안부 좌표정보 API (1)
- Gson (1)
- Apache POI (1)
- MariaDB Connector/J (1)
- BigQuery ML (1)
- Vertex AI (1)
- AnyLogic (1)
- BERT4Rec (1)
- Vertex AI Search (1)
- GCS (1)
- TorchServe (1)
- NiFi (1)
- Argo CD Image Updater (1)
- Kustomize (1)
- Polyglot-Ko (1)
- GPT-OSS (1)
- Amazon MWAA (1)
- Kiro (1)
- Firebase App Distribution (1)
- ODI (1)
- PL/SQL (1)
- Google Groups (1)
- @module-federation/nextjs-mf (1)
- Spring Cloud Config Server (1)
- Spring Cloud Bus (1)
- AI STUDIOS (1)
- Vrew (1)
- Adobe Premiere Pro (1)
- Amplitude (1)
- CKEditor5 (1)
- Lit (1)
- Smithery.ai (1)
- desktop-commander (1)
- History API (1)
- mitmproxy (1)
- Sentence Transformers (1)
- DocC (1)
- Google Play Developer API (1)
- App Store Connect API (1)
- OffscreenCanvas (1)
- AWS DocumentDB (1)
- Monstache (1)
- AWS IAM (1)
- Panda CSS (1)
- Tokens Studio for Figma (1)
- token-transformer (1)
- VideoToolbox (1)
- MediaCodec (1)
- Emotion (1)
- BigDecimal (1)
- NuGet (1)
- MSBuild (1)
- jq (1)
- Ant Design Vue (1)
- GitHub Packages (1)
- Jennifer (1)
- AWS CloudFront (1)
- Opsnow360 (1)
- AlertNow (1)
- Vision (1)
- CameraX (1)
- AWS Fargate (1)
- FireLens (1)
- Elastic Load Balancing (1)
- Elastic Container Service (1)
- GS-CDN (1)
- Amazon MSK Connect (1)
- Oracle Cloud Infrastructure (1)
- JMeter (1)
- EditorConfig (1)
- WinForm (1)
- WPF (1)
- Google Forms (1)
- webdriver-manager (1)
- UiAutomator2 (1)
- AWS Glue (1)
- AWS Step Functions (1)
- AWS Glue Schema Registry (1)
- Lucidchart (1)
- Swiper (1)
- YouTube (1)
- 카카오톡 지도 API (1)
- react-intersection-observer (1)
- Formik (1)
- AWS MemoryDB (1)
- file-loader (1)
- axios-cache-interceptor (1)
- Vuex (1)
- Performance-Analyser (1)

## 버린 대안 1109개 (항목 1315개 중)

- `case_0285` Next.js Dev Server: 하나의 Dev Server 프로세스를 여러 사용자가 공유하면 한 사용자의 컴파일 에러 오버레이가 다른 사용자의 Preview에도 나타났다.
- `case_0285` Sandpack: Preview 첫 화면까지 47초가 걸렸고, private npm registry 인증과 패키지 metadata·tarball 요청 프록시, CORS·PNA 대응이 필요했다.
- `case_0285` HMR: esbuild-wasm이 HMR을 제공하지 않았고, TOI의 Preview에서는 편집 상태를 이어 가며 조작할 일이 없어 HMR의 이점이 크지 않았다.
- `case_0286` 전체 UI 트리 전달: 화면과 UI 트리를 통째로 AI에 넘기는 방식은 토큰 사용량을 감당하기 어려워 단계적 요소 탐색으로 변경했다.
- `case_0287` Global Instruction: 세션 초반에는 규칙을 지켰지만 대화가 길어지면 Context가 가운데로 밀려 무시됐고, 세부 규칙을 모두 넣으면 Context가 커졌습니다.
- `case_0287` AI 기반 규칙 관련성 판정: Hook이 실행될 때마다 AI를 호출해 요청 하나당 10초가 추가됐고, 최종 관련성 판단은 에이전트가 할 수 있어 사용하지 않았습니다.
- `case_0288` App Router: 화면에서 얻을 수 있는 이득보다 서비스 안정성을 지키며 전환하고 유지하는 비용이 컸다.
- `case_0288` 스트리밍 기반 영역별 표시: 레이아웃 이동을 줄이려면 스켈레톤을 계속 관리해야 해 영역을 나눠 먼저 보여주는 이득보다 부담이 컸다.
- `case_0288` Pages·App Router 점진적 마이그레이션: 두 라우터를 함께 두는 동안 basePath가 중복되어 404가 발생하는 문제가 생겼다.
- `case_0291` 2~4시간 버퍼: 시간을 기준으로 두면 핫픽스의 목적과 충돌하므로 충분히 검토했는지를 기준으로 바꿨습니다.
- `case_0293` 번거로운 사후기록: 사후기록을 어렵게 만들자 핫픽스는 줄지 않고 기록만 부실해졌기 때문에, AI가 초안을 만들고 사람이 검토하는 방식으로 바꿨습니다.
- `case_0296` MIG 수동 관리: 노드마다 접속해 MIG 인스턴스를 직접 만들고 구성이 바뀔 때마다 다시 설정해야 했다.
- `case_0296` Distributed Allocation: MIG 조각을 여러 물리 GPU에 골고루 배치해 Full GPU 확보와 구성 변경을 어렵게 했다.
- `case_0297` Virtual Scrolling: 한 번에 그리는 행이 100건이고 DOM 부하가 병목이 아니어서 현재 UX에는 필요하지 않았다.
- `case_0297` IndexedDB 캐싱: 세션 안에서 데이터를 유지하는 것만으로 해결하려던 문제를 모두 해결할 수 있어 무효화·버전 관리·스키마 마이그레이션 비용을 추가하지 않았다.
- `case_0298` 자율형 에이전트: 투자 정보 서비스에서는 실행 경로와 실패 지점이 늘어나고 비용·레이턴시·재현성·운영 안정성을 예측하기 어려워 응답 요건이 명확한 태스크에 절차형 그래프를 선택했다.
- `case_0298` ReAct 루프: 툴 콜과 토큰 사용량, 레이턴시가 늘어나고 실행 경로가 매번 달라져 관리할 트레이스가 많아지므로 필요한 노드만 남긴 절차형 그래프를 선택했다.
- `case_0298` 고정 Few-Shot: 이벤트·실패 유형의 다양성과 시장 국면 변화 때문에 전체 분포를 대표하지 못하고 관련 없는 예시가 컨텍스트를 낭비했다.
- `case_0302` 폴리리포: 리포지토리를 분리해도 서비스별 개발환경 파편화와 공통 코드·업데이트 비용 문제는 남고, 오히려 파편화가 심해질 수 있다고 판단했다.
- `case_0303` 모든 광고 규약을 받는 만능 컨테이너: 여러 광고 네트워크의 서로 다른 규약을 모두 지원하는 대신 하나의 표준을 깊게 지원하기로 했다.
- `case_0304` 로드 완료 콜백: HTML 파싱 완료만 보장하고 실제 캔버스 화면 렌더링은 보장하지 않는다.
- `case_0304` 브라우저 첫 페인트: 게임의 첫 프레임이 그려지기 전에도 발생할 수 있다.
- `case_0304` 소재 직접 통지: 모든 소재가 약속을 지켜야 하므로 약속을 모르는 소재에는 적용할 수 없다.
- `case_0304` MRAID exposureChange: 컨테이너의 화면 노출 비율만 알려 주고 컨테이너 내부가 실제로 그려졌는지는 알려 주지 않는다.
- `case_0305` 버전 구간별 매핑 테이블: 핫픽스마다 모든 분기를 패치해야 하고 설정 실수로 특정 앱 버전 구간의 광고가 멈출 수 있었다.
- `case_0306` 노트북 통째 전달: MLE가 서빙 코드를 처음부터 다시 작성해야 했고, 필요한 파일과 라이브러리를 반복적으로 확인해야 했다.
- `case_0306` .py 파일 분리: 파일로 분리해도 인터페이스가 표준화되지 않아 모델별 수정과 공통 기능 적용이 계속 필요했다.
- `case_0307` 검색 중심 접근: 검색 결과가 좋아져도 문서 최신성, 논의의 최종 결정 여부, 문서와 코드의 일치 여부를 판단할 수 없어 신뢰 가능한 컨텍스트 관리 계층으로 문제를 다시 정의했다.
- `case_0307` 단일 신뢰도 점수: 하나의 점수로는 근거 부족과 정보 노후화처럼 서로 다른 문제와 해결 방법을 설명할 수 없어 여섯 가지 판단 축으로 나눴다.
- `case_0307` 동의어 자동 병합: 사내 약어와 별칭은 비슷한 표현이 다른 시스템을 가리킬 수 있어 애매한 후보를 자동 병합하지 않고 사람 승인 방식으로 처리했다.
- `case_0308` lodash: 오래된 코드 구조와 레거시 브라우저 방어 로직을 포함하고 현대 브라우저의 네이티브 기능을 활용하지 않으며 ECMAScript Modules를 지원하지 않았다.
- `case_0308` lodash-es: ECMAScript Modules를 추가했지만 lodash의 오래된 내부 코드와 비효율성은 그대로였다.
- `case_0309` AWS Device Farm: 토스 앱에 필요한 커스텀과 금융 서비스의 보안·컴플라이언스 기준을 원하는 방식으로 적용하기 어려웠다.
- `case_0310` Appium: 규모가 커질수록 명령 지연과 세션 시작·실패·관리 문제가 발생해 자체 드라이버를 선택했다. **(technologies에도 있음)**
- `case_0311` scrcpy: 자체 클라이언트와 프로토콜을 전제로 해 서버를 거쳐 브라우저로 여러 명에게 배포하는 구조에 맞지 않았다.
- `case_0311` USB 직결 캡처: 화면 취득이 조작 세션과 충돌해 동시에 사용할 수 없었다.
- `case_0311` Appium MJPEG: 조작과 공존할 수 있지만 10~15fps 수준으로 끊기고 지연이 컸다.
- `case_0312` 리뷰 코멘트 체크리스트: 기존 리뷰 코멘트를 체크리스트로 만들어 AI가 항목을 하나씩 확인하게 했지만, 중요한 문제는 놓치고 불필요한 코멘트를 억지로 생성해 자율 리뷰 워크플로로 전환했다.
- `case_0312` 사용자 직접 설치·호출 방식: 사용자가 Skill을 직접 설치하고 업무 중 떠올려 호출하며 자료를 찾아 전달해야 해 사용성이 낮았기 때문에, 사내 메신저와 GitHub 업무 흐름에 자동화 기능을 통합했다.
- `case_0313` TestRail: 상용 도구가 업무 방식을 제한하고 필요한 AI 기능을 유연하게 붙이거나 제거하기 어려워 자체 플랫폼으로 대체했다.
- `case_0313` API Labs: API 테스트를 쉽게 하려는 방향이 맞지 않다고 판단해 8시간 만에 제거했다.
- `case_0315` 상용 TCM: 기능을 직접 추가·개선하거나 QA 데이터를 활용하기 어려웠다.
- `case_0318` lodash: 오래된 코드 구조와 불필요한 방어 로직이 있고 ECMAScript Modules를 지원하지 않았다.
- `case_0318` lodash-es: ECMAScript Modules 지원만 추가했을 뿐 코드가 낡고 비효율적으로 동작하는 문제는 해결하지 못했다.
- `case_0318` 자체 공통 유틸리티 라이브러리: 모든 함수를 직접 구현하고 엣지 케이스를 대응하는 데 부담과 시간이 들었다.
- `case_0319` es-toolkit 함수 직접 교체: lodash와 동작이 다른 함수가 있어 비슷한 함수로 바로 바꾸면 런타임 오류가 발생할 수 있었다.
- `case_0321` 개인 문서 작성 중심: 한 사람이 문서를 더 많이 작성하는 방식은 제품 변화 속도를 따라갈 수 없었다.
- `case_0321` 자발적 문서화 활동: 뉴스레터, 워크숍, 길드 등으로 참여를 유도했지만 지속적인 문서화 문화로 이어지지 않았다.
- `case_0323` Istio consistent hash: consistent hash는 세션을 같은 Replica에 고정할 수 있지만 서버의 실제 부하를 고려하지 못해 바쁜 서버에 새 세션이 계속 배치될 수 있었다.
- `case_0323` Kyuubi: Kyuubi는 Thrift/JDBC 기반 SQL Only 인터페이스를 제공해 DataFrame API를 서비스해야 하는 요구사항을 충족하지 못했다.
- `case_0325` 정규식 기반 트리거 판정: 한국어 표현, 이모지, 완곡한 동의 표현 등 다양한 트리거 조건을 정규식 리스트로 모두 포착하기 어려워 모델 판정으로 전환했다.
- `case_0325` 전략 패턴: 형식 결함 검사는 단순한 구현으로 충분했고, 전략 패턴은 당장의 요구사항에 비해 복잡성을 불러 일으킨다고 판단했다.
- `case_0328` 취약한 암호화 스위트 일괄 제거: 구형 서버를 사용하는 가맹점의 결제가 중단될 수 있어 채택하지 않았다.
- `case_0328` 가맹점 업그레이드 대기: 가맹점이 업그레이드할 때까지 전체 생태계가 보안 위험에 노출되므로 채택하지 않았다.
- `case_0330` Cipher Suite 한 번에 제거: 구형 서버를 사용하는 가맹점의 결제가 즉시 멈출 수 있어 채택하지 않았다.
- `case_0330` 가맹점을 기다린다: 가맹점이 전환할 때까지 기다리면 전체 생태계가 취약한 상태로 계속 남기 때문에 채택하지 않았다.
- `case_0331` lodash: 기존 아키텍처가 최신 ES Modules·엔진 최적화를 쉽게 적용하기 어렵고 번들 크기와 런타임 성능 측면에서 불리해 대체 대상으로 삼았다.
- `case_0331` lodash-es: ES Modules 버전이어도 내부 헬퍼 의존성을 포함해 단일 함수 import가 추가 코드를 끌어오므로 채택하지 않았다.
- `case_0331` @types/lodash: 소스 코드와 타입 정의가 분리된 별도 커뮤니티 패키지라 버전 불일치와 부정확성이 발생할 수 있다.
- `case_0334` Flink batchMode: Batch Job이 FINISHED되면 State도 함께 폐기되고, 재구축된 State를 Redis에 초기값으로 써줄 경로가 없었다.
- `case_0334` Spark와 Hive 분리 처리: 정합성이 핵심인 앱에 Hive와 Spark를 추가하면 State SSOT 보장이 복잡해진다.
- `case_0335` write_buffer_size 증설: per-CF 크기만 올리면 WBM 압박이 남아 근본 해결이 되지 않았다.
- `case_0336` NATIVE Savepoint: Changelog와 함께 사용하면 materializedId와 lastConfirmedMaterializationId가 불일치해 Materialization이 영구적으로 skip됐다.
- `case_0337` 런타임 분석: 실행 시 조건에 따라 한 경로만 확인할 수 있어 모든 케이스를 실행해야 하므로 정적 분석을 선택했다.
- `case_0338` Flat 패턴 단독: 시스템이 상정하지 않은 요구가 등장할 때 props가 끝없이 늘어나 확장과 유지보수가 어려워집니다.
- `case_0338` Compound 패턴 단독: 단순한 컴포넌트까지 Compound로 만들면 사용 방법과 학습 부담이 커져 오히려 불편해질 수 있습니다.
- `case_0338` 중앙 통제·제약 강화: 제약이나 금지를 강화하는 방식은 제품팀이 시스템을 우회하는 문제를 근본적으로 해결하지 못합니다.
- `case_0340` Magnum: 프라이빗 클라우드에서 모든 제어권을 확보하기 위해 PaaS 형태의 클러스터 관리 서비스를 선택하지 않았다.
- `case_0341` DNS 기반 부하 분산: OpenStack 신규 IP를 고객사 방화벽에 사전 등록해야 해서 운영 시작이 지연되었으므로 우선 Global Accelerator를 적용했다.
- `case_0343` 전용 노드 고정 할당: 전용 노드를 붙이면 문제는 단순하게 해결되지만 비용이 발생하므로 시간에 따라 노드를 동적으로 늘리고 줄이는 방식을 선택했다.
- `case_0345` 랜덤하게 25초 기다리기: UI가 실제로 상호작용 가능한 상태인지 확인하지 않고 고정된 시간만 기다리는 방식이기 때문이다.
- `case_0352` RAG: 코드 간 연관관계를 제대로 파악하기 어려웠다.
- `case_0352` Repomix: 전체 소스코드를 압축해도 토큰 문제를 해결하지 못했다.
- `case_0353` CodeQL: 프로젝트 빌드가 필요했다.
- `case_0353` CodeQL: 빌드 과정에서 상당한 Compute cost가 발생했다.
- `case_0353` CodeQL: 오픈소스 프로젝트가 아니면 유료였다.
- `case_0354` gpt-oss: 커버리지가 떨어지고 MCP Tool Calling이 실패하는 경우가 잦았다.
- `case_0354` Llama ← llama3.1: 정확도 순위에서 3위였고 분석률과 정탐률이 낮았다.
- `case_0358` LangGraph: 간단한 테스트에서는 직접 구축해야 하는 번거로움 때문에 LangSmith를 사용했다.
- `case_0361` 부분 팔레트 수정: Blue 100 하나를 수정해도 다른 색상과 전체 명도 진행, 다크모드까지 함께 재검토해야 하므로 팔레트 문제를 해결하기 어려웠다.
- `case_0365` 클래스 기반 POM: this 상태 관리와 상속 구조가 복잡성을 키우고 유지보수 비용을 증가시켜 함수형 POM으로 전환했다.
- `case_0365` Playwright 기본 networkidle 대기: 폴링이 있는 화면에서 네트워크가 계속 움직여 기본 대기 방식이 자주 실패했기 때문에 안전 대기로 대체했다.
- `case_0367` 동기화: 데이터 읽기 시점에 동기화를 적용하면 병렬 처리의 이점이 사라졌다.
- `case_0369` Kubernetes CronJob: 정확히 한 번의 실행을 보장하지 못해 배치 중복 실행 문제가 발생했고, 데이터센터와 AWS 간 RTT로 레거시 배치 성능도 저하됐다.
- `case_0372` Oracle DB에 테이블 추가: 기존 Oracle DB에 테이블을 추가하는 대신 결제팀 전용 MySQL 기반 원장을 독립적으로 구축했습니다.
- `case_0375` 가맹점별 if문 분기: 가맹점 요구사항이 늘어나면서 중요한 비즈니스 로직과 특정 가맹점 요구사항을 파악·추적하기 어려워져 조립 가능한 블록 구조로 변경했다.
- `case_0375` 수동 연동문서 관리: 수동 문서가 개발 사이클과 멀어지고 실제 동작과 불일치하는 문제가 있어 계약 기반 문서 자동 생성으로 변경했다.
- `case_0377` CDC: 조회 친화적인 역정규화 테이블을 만들기 위해 데이터팀이 승인팀의 도메인 로직 일부를 보유해야 해 도메인 의존성이 높아졌다.
- `case_0379` JIRA: 팀의 주요 소통 채널과 이슈 관리가 분리되어 맥락이 흩어졌고, 작은 단위의 QA 이슈를 빠르게 처리하기에는 사내 메신저 리스트·캔버스가 더 적합하다고 판단했다.
- `case_0386` SSE: 빈번한 세션 끊김으로 사실상 이용이 불가능했다.
- `case_0386` 일반 Streamable-HTTP: 서버 배포나 연결 끊김 시 세션이 유실되어 사용에 불편함이 있었다.
- `case_0389` 모든 미션 수행·아이템 전부 소진 가설: 로열 유저의 핵심 행동을 아이템 공급과 소비의 순환으로 판단했기 때문에, 매일 모든 미션을 수행하고 아이템을 전부 소진한다는 챌린저 가설을 선택하지 않았다.
- `case_0392` 동기 TCP 통신: 구현 편의성은 있지만 고성능 서비스를 위해 비동기 통신이 필요했다.
- `case_0395` 완전한 E2E 테스트 도입: 가장 이상적인 방법이지만 팀 상황상 당장 적용하기 어려웠다.
- `case_0395` Local 환경 포기: 새로운 서비스들이 Mock 서버를 연동할 때 Local 환경을 사용할 수 없게 되어 생산성에 영향을 줄 수 있었다.
- `case_0397` 커널 명령어로 커넥션 수집: IP:Port 연결 정보만 알 수 있어 Producer·Consumer와 Topic을 확인할 수 없다.
- `case_0397` GitHub 소스코드 분석: 서비스 담당 조직별 코딩 스타일과 실제 배포 형상의 차이 때문에 Producer·Consumer, Topic, 현재 연결 상태를 100% 정확하게 파악하기 어렵다.
- `case_0397` 공통 라이브러리 계측: 모든 서비스에 100% 반영·배포하기 어렵고 다양한 언어를 지원해야 한다.
- `case_0397` HEARTBEAT request log: 100%로 수집하면 초당 10만 건 이상 발생해 효용이 낮다고 판단했다.
- `case_0397` OFFSET_COMMIT request log: 100%로 수집하면 초당 10만 건 이상 발생해 효용이 낮다고 판단했다.
- `case_0398` 소셜 프루프: 얼굴 인증을 익숙하게 만드는 방법으로 검토했지만 자주 노출하는 방식을 택했다.
- `case_0398` 혜택 제공: 사용자가 개인정보를 판다고 느낄 수 있어 보상 없는 이벤트를 선택했다.
- `case_0400` 광고 시청 강제: 포인트를 받은 직후 광고를 강제로 보게 했지만 사용자는 한두 번 사용한 뒤 이탈했고, 광고 매출과 서비스 지속가능성을 만들기 어렵다고 판단해 포기했다.
- `case_0401` Feast: 토스의 복잡한 회사 니즈에 맞는 오픈소스가 없고, 자체 개발하면 현재 시스템을 유지하면서 최소한의 개발로 요구사항을 충족할 수 있다고 판단했다.
- `case_0401` Tecton: 토스의 복잡한 회사 니즈에 맞는 오픈소스가 없고, 자체 개발하면 현재 시스템을 유지하면서 최소한의 개발로 요구사항을 충족할 수 있다고 판단했다.
- `case_0401` Hopsworks: 토스의 복잡한 회사 니즈에 맞는 오픈소스가 없고, 자체 개발하면 현재 시스템을 유지하면서 최소한의 개발로 요구사항을 충족할 수 있다고 판단했다.
- `case_0405` WebSocket 기반 Remote MCP: 처음에는 고려했지만 로컬 기반 MCP 서버를 구현하기로 결정했다.
- `case_0405` SSE 기반 Remote MCP: 처음에는 고려했지만 로컬 기반 MCP 서버를 구현하기로 결정했다.
- `case_0405` 형태소 분석 라이브러리: Java나 C 같은 추가 환경 설정으로 인해 로컬 MCP 사용성을 저하시킬 수 있어 배제했다.
- `case_0405` 사전 정의 키워드 기반 문서 검색: 운영 결과 환각, 중요 정보 유실, LLM 호출 증가가 발생해 BM25 방식으로 변경했다.
- `case_0406` 클라우드 활용: 장기적이고 지속적인 워크로드와 자체 클러스터 환경에서는 비용이 더 발생할 수 있고, 데이터 보안·컴플라이언스 및 GPU 인스턴스 제어 제약이 있었다.
- `case_0406` 혼합 GPU 운영: GPU 세대별 드라이버·CUDA·프레임워크 호환성과 스케줄링 관리가 복잡해지고, 수요가 고용량 GPU에 집중되면 저용량 GPU가 유휴 자원이 될 수 있었다.
- `case_0406` MPS: 소프트웨어 방식이라 리소스 간 명확한 격제가 어렵고 성능 간섭 및 프로세스별 리소스 모니터링·제어 부담이 있었다.
- `case_0407` Enum 기본값 역직렬화: 기본값을 반환해도 도메인 로직에서 예기치 않은 버그가 발생할 수 있고 개발자가 동작을 완전히 제어하기 어려웠다.
- `case_0407` String 처리: 유연한 처리와 사용성 제한을 만족하기 어려웠다.
- `case_0408` 외부 마케팅: 기존 유저가 친구에게 추천하게 만드는 바이럴이 더 강력하다고 판단했다.
- `case_0408` 친구초대 리워드 모델: 공유한 친구 수에 따라 보상을 지급하는 전형적인 모델 대신 공유해야 가격이 내려가는 규칙을 선택했다.
- `case_0408` 상세한 플로우 설계: 디테일을 모두 적용하자 제한 시간 안에 문제를 풀 수 없을 정도로 난이도가 높아져 가장 단순한 형태로 바꿨다.
- `case_0409` base package 스캔 방식: 모듈 단위로 동일한 패키지 구조를 사용할 수 있어 적용이 어렵다.
- `case_0409` 어노테이션 기반 정의: 서비스와 어드민 repository 양쪽에 동일한 어노테이션을 선언해야 해 설정 누락이나 중복이 발생할 수 있다.
- `case_0409` base 모듈 프로퍼티 통합: 각 설정이 어떤 서비스에 영향을 미치는지 명확히 구분하고 관리하기 어렵다.
- `case_0411` Audio 우회: 모바일 Safari의 비디오 자동 재생 문제를 Audio로 우회하려 했지만 잘 동작하지 않아 채택하지 않았다.
- `case_0413` 정규 표현식 기반 검사: 코드 포맷에 따른 줄바꿈이나 공백 등의 예외 케이스를 처리하기 어려워 SWC를 활용한 AST 분석을 사용했어요.
- `case_0415` Replication Database: Replication 구조에서 복제 지연이 발생할 수 있어 Strong Consistency와 데이터 신뢰성을 보장하기 어렵다고 판단했다.
- `case_0416` 라이브러리 커스텀: 라이브러리의 원래 구조가 새로운 요구사항에 맞지 않거나 업데이트를 따라가기 어려워지는 등 커스텀에 따른 리소스 소모가 커진다고 판단했다.
- `case_0416` 좌표 방식 표현: 패널을 이동하거나 크기를 변경할 때 여러 패널의 좌표를 함께 변경해야 하는 규칙을 정하기 어려웠다.
- `case_0418` Stretched Cluster: 데이터센터 간 네트워크 단절 시 Split-brain으로 가용성을 확보할 수 없고, 데이터센터 간 통신 latency로 Kafka 성능이 저하되기 때문에 채택하지 않았다.
- `case_0420` Kafka MirrorMaker 2: OffsetSync 기록 주기 때문에 대부분의 경우 중복이 발생하고, 동일 Topic명 환경과 Data Mirror가 없는 Topic에서는 Offset Sync가 제한되었다.
- `case_0420` Confluent Replicator: Apache Kafka 기반이 아니라 Confluent Kafka를 구매해야 하며, 직접 구축하려면 전사 Consumer에 추가 기능을 개발·검증·배포해야 했다.
- `case_0424` use-funnel: 퍼널 단계는 관리하지만 상태관리를 지원하지 않아 상태를 퍼널과 별도로 직접 관리해야 했다.
- `case_0424` XState: 퍼널 컴포넌트와 상태관리 코드가 분리되어 한눈에 파악하기 어려웠고, 타입과 수정 지점이 많아 진입장벽이 컸다.
- `case_0429` MirrorMaker2: 복제된 토픽 이름에 Source Cluster alias가 자동으로 추가되어 동일한 토픽명으로 접근하려는 환경에 맞지 않았다.
- `case_0430` Prometheus 기반 모니터링: 데이터 보존 기간이 짧고 PromQL 연산에서 label을 일치시켜야 해 장기간 분석과 유연한 분석이 어려웠다.
- `case_0431` 의존성 관리 도구 병행: 각 의존성 관리 도구가 서로 관리하는 의존성을 알 수 없어 라이브러리가 중복될 수 있다.
- `case_0432` SQL 파일 기반 테스트 데이터 셋업: SQL 파일로 데이터를 관리하면 컬럼에 매핑되는 값을 식별하기 어렵고 컬럼 추가·변경 대응이 번거로워 JSON 포맷과 TestExecutionListener를 선택했다.
- `case_0432` 외부 서버 테스트 API 추가: 전사 의존적인 사용자 서버에 테스트용 API를 추가하면 문제 발생 시 전면 장애로 이어질 수 있고 테스트 현실성도 떨어진다고 판단했다.
- `case_0432` 모의 객체 프레임워크 중심 테스트: 테스트 컨텍스트 재활용이 어려워 속도가 느려지고, 테스트 현실성이 낮아지며 구현과 강결합되므로 최대한 지양했다.
- `case_0433` 외부 데이터베이스 조회: 구현은 간단하지만 ksqlDB의 노코드 장점을 살리지 못하고, 로그마다 데이터베이스를 조회하면 초당 5만 건 이상의 read 요청이 발생할 수 있다.
- `case_0434` 웹 파싱: Spark History Server 화면을 웹 파싱하는 방식을 고민했지만, 자체 계산 방식이 커스텀 메트릭과 임계치 조정에 더 유연하다고 판단해 채택하지 않았다.
- `case_0435` GPU 직결 네트워크 스토리지: 인피니밴드를 이용해 GPU에 네트워크 스토리지를 직접 연결하면 높은 대역폭을 얻을 수 있지만 비용이 많이 들어 일반적으로 권장하지 않는다.
- `case_0438` if-else 구현: 새로운 케이스가 추가되거나 특정 케이스를 수정할 때 유지보수가 어렵고 코드가 길어질 수 있다.
- `case_0438` 상속: 상속 대신 composition과 전략 패턴을 선택했다.
- `case_0439` if-else 구현: 분기 깊이가 깊어지고 수정 시 사이드 이펙트가 발생할 가능성이 있으며 가독성이 떨어진다.
- `case_0446` 커스텀 DSL: 유연한 노출 로직을 위해 검토했지만 유지보수가 어려워질 수 있어 SpEL을 선택했다.
- `case_0451` Spark Streaming: 소스코드 개발과 Job 배포·관리의 운영 부담을 줄이기 위해 ksqlDB를 선택했다.
- `case_0451` Apache Flink ← Flink: 소스코드 개발과 Job 배포·관리의 운영 부담을 줄이기 위해 ksqlDB를 선택했다.
- `case_0458` Next.js standalone 모드: Next.js standalone 기능이 node_modules 디렉터리에 의존해 Yarn PnP 환경에서는 그대로 사용할 수 없었다.
- `case_0462` lint rule: 오타와 누락을 줄일 수 있지만, 문제 발생의 근본적인 원인을 해결하기로 했다.
- `case_0462` 자동완성 기능: 오타와 누락을 줄일 수 있지만, 문제 발생의 근본적인 원인을 해결하기로 했다.
- `case_0463` Express: Next.js SSR 서버의 요구사항에 비해 과한 기능과 미들웨어 오버헤드가 있어 제거했다.
- `case_0464` 캐시 활성화 기반 무작위 분기: 초기 캐시 응답에서 선택된 한 버전이 캐시 TTL 동안 다른 기기에도 동일하게 전달되어 제한된 클라이언트에만 변경 사항을 적용할 수 없었다.
- `case_0464` 캐시 비활성화 기반 요청별 분기: 요청마다 Lambda@Edge를 실행해야 하므로 컴퓨팅 비용이 증가하고 정적 리소스 로딩이 지연되었다.
- `case_0465` tsyringe: 당장에는 의존성을 주입할 수 있는 구조만 필요해 라이브러리 도입을 나중으로 미뤘다.
- `case_0465` inversify: 당장에는 의존성을 주입할 수 있는 구조만 필요해 라이브러리 도입을 나중으로 미뤘다.
- `case_0467` OAS description 자동화: OAS의 description 항목으로 파라미터 설명까지 자동화하지 않고, 테크니컬 라이터가 MDX에서 설명을 관리하는 방식을 선택했다.
- `case_0468` pnpm: pnpm도 좋은 패키지 매니저이지만 Yarn의 플러그인 API가 더 확장성이 높다고 판단했다. **(technologies에도 있음)**
- `case_0473` Metro: 빌드 시간이 오래 걸리고 Tree-shaking을 지원하지 않으며 캐시를 리셋하지 않으면 일관적인 동작을 보장하기 어려워 사용하지 않았다.
- `case_0480` spring.jdbc.getParameterType.ignore 설정 변경: 전체 시스템에 영향을 줄 수 있는 Spring 설정 변경을 피했다.
- `case_0481` 리소스를 끊임없이 더 투입하기: 비용 대비 결과물의 효율성을 유지하기 어렵고 지속 가능하지 않다고 판단했다.
- `case_0481` 그린필드 프로젝트: 기존 제품과 새 제품을 동시에 운영해야 하며, 반복될수록 운영 제품 수가 늘어날 수 있다고 판단했다.
- `case_0486` iframe 기반 샌드박스: iframe 특성상 주소 이동을 할 수 없어 토스페이먼츠 SDK의 리다이렉트를 지원할 수 없었다.
- `case_0486` @babel/standalone: sucrase가 브라우저 커버리지보다 속도에 초점을 맞춘 트랜스파일러였기 때문에 샌드박스에 사용했다.
- `case_0488` 퍼널별 SPA: 퍼널 중간의 브라우저 뒤로가기를 대응할 수 없고, 새로고침하면 해당 페이지를 유지하지 못하고 시작점으로 돌아갈 수 있다.
- `case_0488` URL 쿼리 파라미터: 작은 퍼널을 재사용하려면 퍼널 종료 후 돌아갈 위치 정보를 계속 URL에 들고 다녀야 한다.
- `case_0491` Istio만 이용한 인증·인가: Istio의 matching rule보다 애플리케이션 코드가 자유도가 높고 Auditing과 카나리 배포를 처리할 수 있어 Gateway에서 인증·인가를 담당했다.
- `case_0491` Istio 인프라 레이어 서킷 브레이킹: 호스트 단위로만 설정할 수 있고 설정 가능한 룰에 한계가 있어 애플리케이션이나 Gateway에서 더 정교하게 적용했다.
- `case_0493` React.lazy 재시도 패턴: 새 import()를 호출해도 브라우저 모듈 맵이 실패 결과를 반환해 네트워크 요청이 발생하지 않았다.
- `case_0493` 페이지 새로고침: SPA의 상태가 초기화되어 영업 중인 웹뷰의 화면과 진행 중인 작업을 잃게 된다.
- `case_0493` 쿼리스트링 재시도: 바깥 import()의 URL만 바꿀 수 있고, 청크 내부의 정적 import 주소와 공유 청크 주소는 바꿀 수 없었다.
- `case_0493` Service Worker: 코드 스플리팅된 파일이 대부분 10KB 이하라 캐시 이득보다 관리 비용이 컸다.
- `case_0493` modulepreload: 지원 하한이 Chrome 66이라 Chrome 51을 지원해야 하는 웹뷰 환경에 적절하지 않았다.
- `case_0494` Temporal: 워크플로 코드의 결정론 규칙을 팀 전체가 익혀야 하고, 클러스터·DB·UI 등 별도 인프라를 직접 운영해야 하며, 엔진 내부 이슈와 기술 종속 위험도 있었다.
- `case_0496` Kafka: 자동승인 조건은 여러 시스템 상태의 조합이므로 특정 이벤트만으로는 나머지 조건이 충족됐는지 처리할 수 없다.
- `case_0496` ShedLock: 스케줄러를 한 대만 실행하게 하면 서버를 늘려도 처리량이 늘지 않고, 실행 중인 서버가 단일 장애점이 된다.
- `case_0496` DB 조건부 UPDATE: 실패한 선점 시도까지 쓰기 DB에 도달하고, 앞선 서버가 커밋할 때까지 실패를 알 수 없다.
- `case_0496` DB SKIP LOCKED: 후보 조건 일부가 조인 뒤에 적용되어 잠금 범위를 LIMIT 개수로 제한할 수 없다.
- `case_0500` 기존 코드 수정: 디자인시스템 변경으로 화면 코드도 모두 새로 작성해야 해서 기존 코드를 고치는 대신 새로 작성했다.
- `case_0501` WebSocket: 사내 배포플랫폼에서 사용하기 어려웠고, 남은 3주 안에 구현할 자신이 없어 제외했다.
- `case_0502` WebGL: 외장 그래픽카드가 없는 저사양 송출용 노트북에서 그래픽을 충분히 그려내지 못해 Canvas 2D로 교체했다.
- `case_0502` 참가자 수만큼 자리 배치: 참가자가 접속만 하고 게임을 하지 않거나 결과를 제출하지 않으면 화면에 구멍이 생길 수 있어 제외했다.
- `case_0503` 한 번에 코드 분류: 같은 의미의 응답이 서로 다른 코드로 분류되고 코드의 추상화 수준도 제각각이어서 단계적으로 나누는 방식을 선택했다.
- `case_0504` REST API: 한 번 응답하면 진행 중인 상태를 알 수 없어서 선택하지 않았다.
- `case_0504` Polling: 불필요한 반복 요청이 많고 진행 상황 변화를 다음 요청까지 기다려야 해서 선택하지 않았다.
- `case_0504` WebSocket: 클라이언트가 보낼 메시지가 없는 단방향 진행 상황 전달에는 오버스펙이라고 판단했다.
- `case_0504` mp3 파일 추가: 음원 파일을 번들에 넣거나 별도로 다운로드·관리하지 않기 위해 Web Audio API를 선택했다.
- `case_0505` 채팅방별 세션 사전 생성: 실제로 사용되지 않을 세션과 대화 컨텍스트가 불필요하게 생성될 수 있어 질문을 보내기 전 확인 후 필요할 때 생성하는 방식을 선택했다.
- `case_0505` 컴포넌트 내부 상태 관리: 탭 전환으로 컴포넌트가 사라질 때 진행 중인 연결이 끊길 수 있어 React 바깥의 서비스와 스토어로 분리했다.
- `case_0506` CFF rewrite: 내부 목적지를 직접 바꾸는 구성은 보안 요구사항을 충족하기 어려워 제외했다.
- `case_0506` 앱 내부 호스트 라우팅: 지원 웹 도메인이 추가될 때마다 앱 개발팀 변경과 앱 수정·배포 일정을 고려해야 하고, 웹 라우팅 책임이 앱에 쌓여 채택하지 않았다.
- `case_0507` Standard REST API: 가장 느린 작업에 전체 속도가 하향 평준화되는 문제를 해결할 수 없어 제외했다.
- `case_0507` HTTP Streaming: Raw Stream 방식이라 브라우저 내장 EventSource API를 사용할 수 없고, 메시지 경계 파싱 등 통신 스펙을 직접 정의해야 했다.
- `case_0507` WebSocket: 전시 정보 조회에는 양방향성이 불필요해 프로토콜 복잡도만 높아져 제외했다.
- `case_0507` EventSource 방식: 요청에 커스텀 헤더를 붙일 수 없어 Authorization을 비롯한 공통 헤더를 전달할 수 없었다.
- `case_0507` nginx proxy_buffering off: 300ms면 끝나는 가게목록 지면에서는 스트리밍을 동작시키는 이점이 없고, 기본값이 아닌 설정을 유지할 관리 부담이 생겼다.
- `case_0509` eslint-plugin-i18next: 첫 번째 컨벤션에 일부 맞지만 옵션 조절만으로 프로젝트의 요구사항을 해결하기 어려웠고, 두 번째와 세 번째 컨벤션에 적합한 규칙도 없었다.
- `case_0509` 린트 자동 교정: 자연어를 기계적으로 교정하는 정확도가 떨어지고 오버엔지니어링이라 판단해 AI 반자동 교정으로 대체했다.
- `case_0515` Agent Sync: 자동 동기화가 되지 않아 버전 드리프트가 발생할 수 있고, 동일한 자산이 여러 저장소에 중복되어 관리 부담이 커집니다.
- `case_0517` 컨슈머 메시지당 70초 대기: SQS FIFO의 MessageGroupId가 이미 메시지 직렬화를 담당하므로 컨슈머의 긴 대기를 제거하고 메시지당 처리 시간을 줄였다.
- `case_0518` tsconfig.json paths 우회: 모듈 해석 경로를 강제로 변경하면 Layer 2에서 정상적으로 해석된 타입과 다른 모듈로 인식되어 호환성 에러가 발생할 수 있다.
- `case_0518` shared-workspace-lockfile=false: 워크스페이스별 완전한 의존성 격리는 중복 설치, 설치 속도 저하, 다수의 lockfile 관리와 병합 충돌을 발생시켜 모노레포의 장점을 포기하게 한다.
- `case_0519` FastAPI: 사내 표준이 Kotlin이어서 베타 배포 전에 Kotlin·Spring Boot로 포팅했다.
- `case_0520` SQLite: 서버마다 파일과 데이터가 따로 쌓여 복제 환경에서 공유 DB로 사용할 수 없었다.
- `case_0520` PostgreSQL: 사내 대응성과 행사 규모의 동시 제출을 고려해 MySQL을 선택했다.
- `case_0521` handoff 링크만 전달: 동작은 구현되지만 색상과 간격이 변형됐다.
- `case_0521` HTML만 전달: 겉모습은 같지만 버튼 동작과 서버 연결이 빠졌다.
- `case_0522` Claude ← Claude Haiku: 마이그레이션 비용을 감당하기 어려워 Amazon Nova 2 Lite로 교체했다.
- `case_0522` 기능 플래그 기반 사내 오픈: 앱 언어 설정이 OS를 따라가 임직원 전용 제어가 구조적으로 불가능해 전체 오픈으로 전환했다.
- `case_0526` 이미지 가장자리 일괄 자르기: 이미지 유형에 따라 바코드 영역 자체가 손실될 위험이 있어 근본적인 해결책으로 채택하지 않았다.
- `case_0526` 노란색 영역 인식 후 자르기: 향후 카카오톡 선물하기 디자인 변경으로 이미지 내 다른 영역에 노란색이 사용되면 문제가 발생할 수 있어 채택하지 않았다.
- `case_0526` 중앙값 이진화 단독 적용: 일부 바코드 형태에서는 얇은 막대가 더 유실되어 흑백 비율이 왜곡되고 디코딩에 실패할 수 있어 최종 방식으로 채택하지 않았다.
- `case_0527` Item2Vec: 임베딩 유사도에 기반해 동일 카테고리의 대체재를 추천하고 상품을 담는 순서의 맥락을 반영하지 못했다.
- `case_0529` MCP: 모든 사용자가 MCP를 지원하는 LLM을 사용해야 했다.
- `case_0529` MCP 서버 직접 구현: MCP 지원 LLM이 필요했고 사용자 로컬에서 실행되는 구조적 한계로 격리 환경에 접근할 수 없었다.
- `case_0529` pgvector: Redis 인프라를 활용할 수 있어 별도의 벡터 전용 데이터베이스를 도입하지 않았다.
- `case_0530` IQR: 중앙값 방식이 더 직관적이고 분석이 용이하며 이상치에 강해 선택되지 않았다.
- `case_0530` 2-sigma: 중앙값 방식이 더 직관적이고 분석이 용이하며 이상치에 강해 선택되지 않았다.
- `case_0530` AI 기반 설계: 오탐 발생 시 빠르게 원인을 분석하고 개선하기 어려울 수 있어 채택하지 않았다.
- `case_0531` 프롬프트 템플릿: 팀 컨벤션을 문서화해도 의존성과 클래스별 정보를 계속 수동으로 입력해야 했다.
- `case_0531` 스크립트 자동화: IDE 통합이 부족하고 사용성이 떨어져 IntelliJ 플러그인 방식을 선택했다.
- `case_0531` 플러그인 단독 생성: Gemini API로 완성된 테스트 코드를 직접 생성했지만 컴파일 오류와 기존 테스트 손실이 빈번했다.
- `case_0532` ZK-SNARK: 우아팝에 적용하는 것은 효과적이지 않았다.
- `case_0536` 기본 HPA: CPU·메모리 평균 기반 방식은 상태를 가진 컴포넌트의 Pod별 사용률 편차와 OOM Kill 이후 평균 하락 때문에 타이트한 오토스케일링이 어려웠다.
- `case_0537` import 및 build 엔트리 순서 조정: 스타일 우선순위 이슈가 생길 때마다 적용한 임시 조치가 코드에 누적되어 리팩터링을 어렵게 만들었기 때문에 제거했다.
- `case_0537` 일반 주석: Vite 빌드 시 일반 주석이 제거되므로 청크 식별자와 정렬 기준으로 사용할 수 없었다.
- `case_0538` CloudFront 경로 기반 라우팅: 프런트엔드 전용 CDN과 API 엔드포인트가 동일한 CloudFront 배포에 묶여 보안 정책을 분리하기 어렵고, WAF/Shield 비용과 관리 부담이 증가하며 Private Subnet의 Internal LB를 직접 연결하는 것도 적절하지 않았다.
- `case_0538` SameSite=None / Secure: 특정 브라우저에서 예외 동작이 일어날 수 있고 CSRF 공격 위험이 증가하는 부작용이 있어 제외했다.
- `case_0538` 루트 도메인 쿠키: 서버 도메인 쿠키와 루트 도메인 쿠키가 함께 설정되어 의도한 쿠키가 전달되지 않았고, 타팀 API 호출에서 헤더 크기 초과 에러가 발생했다.
- `case_0539` Kafka: 엑셀 발송은 트래픽 폭증이나 Consumer Group 확장이 필요하지 않았고, 장시간 작업에서 max.poll.interval.ms 초과와 리밸런싱 문제가 반복되어 제거했다.
- `case_0539` Kafka 타임아웃 1시간 설정: 더 긴 작업에서 같은 문제가 재발할 수 있고 실제 Worker 장애 감지가 1시간 지연된다.
- `case_0539` 비동기 처리 후 즉시 ACK: 중복 발송은 막을 수 있지만 ACK 이후 오류·배포·장애가 발생하면 작업이 유실될 수 있어 임시 해결책으로만 사용했다.
- `case_0540` 네이티브 영역 미노출·암전: 앱과 통신해 네이티브 영역을 숨기거나 암전하는 방식은 구조적인 문제로 채택하지 않았다.
- `case_0540` IndexedDB: 객체 교환은 가능하지만 코드가 복잡하고 구현 복잡도가 높아 사용하지 않았다.
- `case_0540` Broadcast Channel: iOS 15.4부터 지원되어 사용하지 못했다.
- `case_0540` postMessage: 플로팅웹뷰의 레퍼런스를 알 수 없어 연결할 수 없었다.
- `case_0540` 네이티브 팝업: 해결 방법이 파편화되고 네이티브 요소를 제어하지 못하는 제약이 있어 후속 과제로 남겼다.
- `case_0541` Redis KEYS 전략: 전체 키 집합을 선형적으로 스캔해 Redis를 블로킹하고 다른 요청에 지연을 발생시킬 수 있다.
- `case_0541` lockingRedisCacheWriter: SCAN을 사용하더라도 캐시 삭제 실행 중 잠금으로 인해 요청이 Block될 수 있다.
- `case_0545` 규칙 기반 툴: 라이팅 규칙이 방대하고 지속적으로 변경되며 모든 케이스를 커버하기 어려워 최종적으로 RAG와 AI를 활용하는 방향으로 전환했다.
- `case_0545` 네이버 맞춤법 검사기: 배민 고유 명칭과 상황별 용어 같은 복잡한 규칙을 원하는 대로 적용하기 어려웠고 API 연동 비용도 낮지 않았다.
- `case_0545` Khaiii: 개발 및 지원이 공식적으로 중단됐고 CNN 모델을 원하는 대로 수정하기도 어려웠다.
- `case_0545` Vector DB 도입: 서버 비용 없는 빠른 PoC를 목표로 했기 때문에 도입하지 않았다.
- `case_0546` WebSocket: 기존 REST API 인프라와 별도로 WebSocket을 운영하고 모든 API를 WebSocket 기반으로 재구현해야 하므로 관리 비용이 커질 수 있고, 알림 전달에는 양방향 통신이 필요하지 않았다.
- `case_0546` 세션 연결 서버 직접 API 호출: 세션 추적과 별도 저장소가 필요하고, API 호출 시점의 서버 재시작이나 네트워크 타임아웃으로 메시지가 유실될 위험이 있었다.
- `case_0546` 세션 연결 서버별 브로커 토픽: 서버 인스턴스별 토픽 관리와 세션 추적이 필요하며, Auto Scaling 환경에서 동적 확장이 어렵고 부하 불균형이 발생할 수 있었다.
- `case_0547` service worker: msw와의 충돌 및 별도 JavaScript 파일이 필요해 불필요한 복잡성이 예상되어 채택하지 않았습니다.
- `case_0547` 구글 시트 운영: 프로젝트별 정보 수정, 사용자 증가에 따른 가독성 저하, 타인 정보의 실수 수정 등 운영 한계가 있어 어드민 페이지로 대체했습니다.
- `case_0548` Redis timeout 파라미터 변경: 100초 동안 사용하지 않는 커넥션을 제거하는 것이 타당하다고 판단하여 Redis timeout 파라미터를 수정하지 않았다.
- `case_0548` FIFO 커넥션 풀 전략: FIFO 전략도 검토하고 테스트했지만, 프로젝트에서는 IDLE 커넥션을 계속 유지할 필요가 없다고 판단해 IDLE 커넥션 정리 방식을 채택했다.
- `case_0549` DefaultTyping.EVERYTHING: 모든 클래스에 타입 정보가 추가되어 직렬화 결과가 커질 수 있고 성능상 이점이 없으며, Jackson에서도 Deprecated 방향으로 가고 있어 추천되지 않는다.
- `case_0549` record 대신 class: 일반 클래스를 사용하면 문제를 해결할 수 있지만, record를 많이 사용하는 팀 프로젝트에서는 record 적용 시 개발자 실수 가능성이 남는다.
- `case_0549` Wrapper 클래스 + @JsonTypeInfo: 타입 정보를 보장할 수 있지만 매번 Wrapper로 감싸야 하고, Redis 설정 레벨에서 자동 처리하지 않으면 개발자가 일일이 신경 써야 한다.
- `case_0550` 직접 서버 운영: Jira Automation보다 자유로운 조건과 복잡한 로직을 구현할 수 있지만, Jira가 제공하는 기본 자동화 기능과 통계까지 직접 구현해야 하므로 노력과 비용이 추가된다.
- `case_0552` FAQ 자동응답 시스템: 키워드 매칭 기반이라 질문 표현이 달라지거나 맥락이 필요한 문의를 처리하기 어렵고 FAQ 문서의 지속적인 업데이트도 어려웠다.
- `case_0553` Java 유지·점진적 개선: 언어 불일치로 인한 문맥 전환과 협업 비용을 줄이고 장기적인 유지보수성과 생산성을 높이기 위해 Kotlin 전환을 선택했다.
- `case_0553` Lombok부터 제거하는 전환 순서: 기능 단위로 나누어 점진적으로 전환하려는 전략과 맞지 않아 Lombok 플러그인 설정을 선택했다.
- `case_0553` Projections.fields(): Kotlin data class에 nullable 처리나 기본값 설정이 필요하고 불변성 철학과 어긋나므로 Projections.constructor()를 선택했다.
- `case_0553` @QueryProjection: DTO에 불필요한 정보가 담기는 것이 우려되어 사용하지 않았다.
- `case_0554` MLflow: LLM 특화 기능과 프롬프트 관련 기능이 부족했고, 최신 버전 업그레이드와 별도 Gateway 배포가 필요했다.
- `case_0554` PromptFlow: 독립적인 웹 UI가 없어 운영 단계의 대시보드·Trace 뷰어·협업 기능이 부족했다.
- `case_0554` LangSmith: LangChain 중심으로 설계되어 범용성이 제한되었다.
- `case_0554` Agenta: 엔터프라이즈 성숙도와 보안·권한 관리·대규모 운영 지원이 부족했다.
- `case_0554` Opik: 엔터프라이즈 성숙도와 보안·권한 관리·대규모 운영 지원이 부족했다.
- `case_0554` Pezzo: 운영 모니터링과 피드백 기능이 없어 확장성이 아쉬웠다.
- `case_0554` OpenPrompt: 로깅·버전 관리·권한 체계가 부족해 프로덕션 운영에 적합하지 않았다.
- `case_0556` Langfuse Playground: 당시 멀티모달 입력을 지원하지 않아 직접 GenAI Labs를 개발했다.
- `case_0557` 상용 내비게이션: 초당 2만 건의 경로 계산에서 API 호출 비용이 발생하고 계산 결과를 재활용하기 어려워 선택하지 않았다.
- `case_0557` Redis String에 전체 그래프 저장: 특정 거리 하나를 조회하거나 갱신해도 지역 전체 데이터를 읽고 다시 저장해야 해 네트워크 대역폭 위험이 커졌다.
- `case_0557` Zstandard 압축: 압축 후에도 원본 데이터가 커 초당 수천 회 수준의 조회를 감당하기 어려워 최종 해결책으로 채택하지 않았다.
- `case_0557` TTL로 삭제: 배달 완료 시점을 일률적으로 가정하기 어렵고 지역별 해시 TTL 갱신 및 만료에 따른 리소스 낭비가 발생해 명시적 삭제를 선택했다.
- `case_0557` 마스터-레플리카 모드: 모든 쓰기 작업이 Primary 노드에 집중되어 네트워크 병목과 대역폭 초과가 발생할 수 있어 클러스터 모드를 적용했다.
- `case_0559` 절대값 기준의 최적화 가이드: CPU 사용률 같은 절대값은 서비스 특성을 반영하지 못해 전사 공통 기준으로 활용하기 어렵다.
- `case_0561` Redux: 상태 변화 추적에는 도움이 되지만 관련 코드 전반을 설계부터 개발·테스트까지 마이그레이션할 리소스가 부족해 도입하지 않았다.
- `case_0562` IllegalArgumentException을 400으로 매핑: IllegalArgumentException은 서버 내부 로직 오류로도 발생할 수 있어 이를 400으로 매핑하면 서버 문제를 클라이언트 오류로 오인할 수 있다.
- `case_0563` 결합 모듈에 오케스트레이션 로직 집중: 모든 도메인에 접근할 수 있는 결합 모듈이 다시 비대해져 거대한 모놀리스로 돌아갈 수 있다고 판단했다.
- `case_0563` 문서로만 아키텍처 규칙 공유: 구조 규칙을 문서로 공유하는 것만으로는 충분하지 않아 코드 수준에서 강제하기로 했다.
- `case_0565` 주문번호 기반 파티셔닝: 재고 충돌과 동시성 이슈로 예측 불가능한 지연이 발생해 센터 코드 기반 파티셔닝으로 변경했습니다.
- `case_0566` JSON 파일 모킹: 시나리오별 JSON 파일이 늘어나고 API 변경 때마다 모든 파일을 수동으로 수정해야 해, 유지보수 부담과 오류 가능성이 컸다.
- `case_0568` Kubernetes: 적합한 클러스터가 없어 새로 만들어야 하고 Flink만을 위한 운영 비용이 부담되었다.
- `case_0568` AWS KDA: 같은 자원 기준 EMR보다 비용이 두 배 이상 비쌌다.
- `case_0569` Lambda 메모리 증설·호출수 개선: 메모리와 호출 수를 개선했지만 Lambda에서 Kinesis로의 속도 문제가 해결되지 않았다.
- `case_0579` 클라이언트 단말에 Cross Root 인증서 설치: 2만 대 이상의 단말과 다양한 OS에 인증서를 배포해야 하고 모바일 OS에서는 수동 설치가 어려워 서버 인증서에 Cross Root를 추가하는 방안보다 비효율적이었다.
- `case_0583` sqllineage: SQL 문법을 엄격하게 검사하여 처리 속도가 느리고 파싱 실패 사례가 많아 교체했다.
- `case_0584` torch.ao.quantization: PyTorch 생태계와 통합되고 커스터마이징 옵션이 풍부하지만 NVIDIA TensorRT와의 호환성이 떨어져 추가적인 변환 과정이 필요할 수 있어 pytorch-quantization을 선택했다.
- `case_0584` PTQ: 모델 크기와 연산 속도 개선에는 효과적이지만 양자화로 인한 성능 저하를 완전히 해결하지 못했다.
- `case_0585` 기존 데이터 기반 직접 모델 학습: 확보할 수 있는 데이터가 한정적이어서 충분한 성능이 나오기 어려웠고, 예측 가능한 속성값의 범위가 제한적이며 학습 데이터가 없는 카테고리도 있었다.
- `case_0585` GPT 자체 평가 점수: GPT-4o의 평가 점수도 기대하는 목표 수준에 미치지 못했고, 생성한 평가 점수를 직접 조정하거나 튜닝할 수 없었다.
- `case_0590` 머신러닝 모델 구축: 학습 데이터가 부족하고 정책이 자주 변경되어 대응하기 어려웠다.
- `case_0590` GPT-4V: 과도한 확대 정책에서 내부 기준에 필요한 만큼 정확한 객체 좌표를 반환하지 못했다.
- `case_0592` GC 튜닝: GC 파라미터를 조정하기보다 현재 메모리 저장 구조를 먼저 개선하기로 했다.
- `case_0592` Hazelcast: 단순 key value 조회보다 많은 기능을 제공해 현재 요구사항에 비해 과하고, 진입 장벽과 낮은 라이브러리 이해도가 우려되었다.
- `case_0592` Chronicle Map: 단순 key value 조회 이상의 기능을 제공하는 라이브러리로 판단되어 채택하지 않았다.
- `case_0592` HPPC: primitive 컬렉션 후보로 검토했지만 fastutil을 선택했다.
- `case_0592` Trove: primitive 컬렉션 후보로 검토했지만 fastutil을 선택했다.
- `case_0592` Koloboke: primitive 컬렉션 후보로 검토했지만 fastutil을 선택했다.
- `case_0593` Atlas MongoDB: 부하 테스트 결과 RDS보다 처리량과 응답시간 측면에서 불리했고 요청 실패도 발생했다.
- `case_0593` OpenSearch: 부하 테스트 결과 RDS보다 처리량과 응답시간 측면에서 불리했고 요청 실패도 발생했다.
- `case_0593` Milvus: 1차 실험 후보였지만 실제 성능 테스트인 2차 실험 후보로 선정되지 않았다.
- `case_0593` Redis Stack: 1차 실험 후보였지만 실제 성능 테스트인 2차 실험 후보로 선정되지 않았다.
- `case_0594` 기존 프로덕트 개선 중심의 해결책: 기대효과에 한계가 있거나 지속 가능한 방법이 아니어서 지표 개선 중심의 해결책을 선택했다.
- `case_0594` 제보 프로모션: 제보 건당 보상을 제공했지만 참여율을 높이기 어려웠고 지속 가능한 방법이 아니었다.
- `case_0596` 화면 너비 기반 기능 분기: 브라우저 너비를 줄인 PC에서 모바일용 URL Scheme이 실행되는 문제가 QA 과정에서 발견되었다.
- `case_0597` 별도 이벤트 서버: 이벤트가 자주 열리지 않고 언제든 사라질 수 있어 별도 서버 인프라를 구축하는 것은 리소스 효율이 낮다고 판단했다.
- `case_0597` PASS 인증 Open API: 상세 개인정보와 CI 수집, 정교한 중복 제출 검증이 필요하지 않아 휴대폰 번호만 사용하는 OTP 직접 구현을 선택했다.
- `case_0597` UUID v4: 랜덤 데이터라 제출 순서에 따른 정렬을 보장하기 어려웠다.
- `case_0598` 컨슈머 수평 확장: 랙을 줄이기 위해 컨슈머 수를 무작정 늘리면 DB 리소스가 고갈될 수 있고, 컨슈머 수 조절이 리밸런싱을 일으킬 수 있다.
- `case_0598` Thread.sleep() 지연: sleep 동안 다음 poll()이 발생하지 않아 리밸런싱이 발생할 수 있고, 처리 시간과 지연 시간의 상한을 함께 관리해야 한다.
- `case_0601` Spring Batch: 별도 배치 애플리케이션 개발과 코드 관리 부담이 있어 postgres_fdw 기반 SQL 마이그레이션을 선택했다.
- `case_0602` Axios Mock Adapter: 브라우저 네트워크 요청을 트래킹할 수 없어 디버깅이 어렵고 유지보수가 복잡해 MSW로 전환했다.
- `case_0603` API 연동으로 서류 자체 제거: 제출 서류 사본이 필요해 API 연동만으로 서류 자체를 없애기는 어려웠다.
- `case_0603` A안 입력 필드 방식: 최종 인터페이스로 B안이 결정되어 A안은 채택하지 않았다.
- `case_0604` AWS Compute Optimizer: 메트릭 조회 기간 제한, 메모리 모니터링을 위한 별도 에이전트 설치 필요, 기능별 배포 단위에 맞춘 커스터마이징 어려움 때문에 자체 솔루션을 개발했다.
- `case_0609` Kong: 기존 솔루션을 활용하는 대신 특정 AI 워크로드 지원, 빠른 수정·확장, 비용·보안·통합 요구를 충족하기 위해 직접 개발했다.
- `case_0609` Dify.ai: 기존 솔루션을 활용하는 대신 특정 AI 워크로드 지원, 빠른 수정·확장, 비용·보안·통합 요구를 충족하기 위해 직접 개발했다.
- `case_0610` fireEvent: 이벤트를 강제로 발생시키며 실제 사용자와 유사한 상호작용을 제공하지 않으므로 userEvent를 사용한다.
- `case_0613` Readiness Gate: Readiness Gate를 설정해도 Pod 생성 시의 트래픽 문제만 해결되고 Pod 삭제 시의 트래픽 문제는 남았다.
- `case_0615` State machine 직접 구현: 상태 진입·이탈 action, 초기 상태, 분산 환경의 상태 저장·동기화 등 요구사항을 직접 추가하면 자료구조와 프레임워크가 커지고 복잡해질 수 있어 채택하지 않았다.
- `case_0615` Squirrel Framework: Spring 친화적이고 업데이트가 더 활발한 Spring Statemachine을 선택했다.
- `case_0615` 공용 State Machine 하나 사용: 로봇 간 간섭을 막기 위한 작업 큐와 비동기 action 완료 확인이 필요하고, 대기 로봇이 많으면 반응성이 떨어질 수 있어 현실적으로 사용하기 어렵다고 판단했다.
- `case_0615` 이벤트마다 신규 State Machine 생성: 이벤트마다 생성·폐기하면 메모리는 아낄 수 있지만 state machine 생성 비용 때문에 CPU 리소스를 많이 사용할 수 있어 추천하지 않았다.
- `case_0622` 캐시 방식: 초기 조회 시 여러 요청이 동시에 들어오면 데이터베이스에 과도한 부하가 발생할 수 있고, 10MB가 넘는 데이터를 애플리케이션에서 매번 필터링해야 했다.
- `case_0622` 배치 방식: 배치 애플리케이션을 독립적으로 실행할 때 컨텍스트 로드와 서버 시작에 수 분이 걸려 통계 데이터의 실시간성이 떨어졌다.
- `case_0623` JPA: 로그에는 저장, 조회, 삭제만 필요하고 영속성을 활용하는 이점이 없다고 판단해 사용하지 않았다.
- `case_0623` NoSQL: 3주라는 짧은 기간에 새로운 DB를 학습하고 AWS에서 바로 활용하기 어려워 사용하지 않았다.
- `case_0624` 분산 캐시: 단일 인스턴스에서만 로그를 처리하는 상황이라 불필요하다고 판단했다.
- `case_0625` DB Scale-Up: DB를 Scale-Up해도 성능 변화가 없어 병목 해결책으로 채택하지 않았다.
- `case_0625` 서버 Scale-Up: 서버를 Scale-Up해도 성능 변화가 없어 병목 해결책으로 채택하지 않았다.
- `case_0626` 스레드 락: Gradle 병렬 테스트가 모듈별 프로세스로 실행되어 프로세스 간에는 synchronized나 ReentrantLock을 공유할 수 없었다.
- `case_0626` 분산락: 분산락은 인덱스 생성 단계만 해결하고, 여러 테스트가 하나의 인덱스 문서를 공유하면서 발생하는 동시성 문제와 추가 의존성·성능 저하를 남겼다.
- `case_0626` Fake 오버라이딩: 모든 alias 접근 로직을 테스트용 Fake 객체에서 오버라이딩해야 해 운영 코드가 복잡해지고 새로운 alias가 추가될 때 수정과 실수 가능성이 커졌다.
- `case_0628` CoT 방법론: 쿼리문과 테이블 해석 프롬프트에서 기존 방법론의 한계를 개선하기 위해 Plan and Solve Prompting을 적용했다.
- `case_0628` 기존의 복잡한 검색 알고리즘: 로그 검색에서 복잡한 알고리즘 대신 LLM의 자연어 이해 능력을 활용했다.
- `case_0629` Torch-TensorRT: 온전한 TensorRT 엔진보다 추론 속도가 느리고, TensorRT 호환 연산자가 적을수록 추론 속도가 더 느려진다.
- `case_0631` 프롬프트와 GPT-3.5 API만 활용: 기존 방식은 체계화·효율화·접근성·자동화를 구현하기에 한계가 있어 새로운 아키텍처를 설계했다.
- `case_0632` GPT-4 단독 사용: 사내 도메인과 데이터 정책에 대한 이해가 부족하고 불필요한 데이터와 허위 생성이 발생해 실제 업무 활용 품질이 낮다.
- `case_0633` Ray: 데이터 처리 기능이 부족하고 작은 데이터에서 비효율적이며 운영 배포 시 인프라 구축이 필요했다.
- `case_0633` Dask: Pandas DataFrame을 여러 파티션으로 나누는 구조로 인해 성능상 한계가 있었고 메모리 소모 면에서도 약점이 있었다.
- `case_0633` Modin: 성능 향상에 한계가 있었다.
- `case_0633` vaex: 문법 구조가 다르고 기능이 부족했으며 사용 사례가 적었다.
- `case_0633` Numba: 일부 연산은 병렬화·고속화할 수 있지만 범용성이 떨어졌다.
- `case_0635` ANN 검색(HNSW·IVFFlat): 사용자 주변에 위치한 N개의 가게에 대해서만 검색하므로 ANN 방식을 사용하지 않고 Exact search 방식을 선택했다.
- `case_0635` 새로운 가게 후보 사용: A/B 테스트에서 새로운 후보 대신 기존 Two Tower 기반 추천 가게 목록을 후보로 사용했다.
- `case_0636` Kubernetes: 전체 기능을 설치하는 Kubernetes보다 설치가 간편하고 Arm 노드를 쉽게 추가할 수 있는 K3s가 규모가 비교적 작은 시스템에 효율적이어서 K3s를 선택했다. **(technologies에도 있음)**
- `case_0639` 베타환경 API 직접 호출: 타 시스템에 부하를 주고 데이터 변경이나 베타 API 장애에 따라 테스트가 실패하며, Read Timeout과 장애 시 에러 디코딩 테스트가 불가능하다.
- `case_0639` Postman mock 서버: API 호출량 제한을 초과하면 이후 테스트가 모두 실패한다.
- `case_0642` polyfill.io: 외부 서비스 장애나 지연이 발생하면 폴리필 로딩과 초기 로드 속도에 영향을 줄 수 있고, 소유권 변경 이슈도 있어 직접 라이브러리를 사용하는 방식으로 결정했다.
- `case_0643` 이관요청서 단위 분산 락: 하위 SKU를 동시에 할당할 때 첫 번째 할당 요청만 성공하고 나머지 요청은 분산 락 획득에 실패한다.
- `case_0643` 분산 락 대기 방식: waitTime으로 요청을 순차 처리하면 하위 SKU가 많아질수록 할당 처리 시간이 늘어나 할당 속도를 포기하게 된다.
- `case_0645` Module Federation: 호스트 애플리케이션에 추가 설정이 필요하고 산출물의 안정성 검증과 QA가 필요했으며, 촉박한 일정에서 패키지 배포보다 비용이 컸다.
- `case_0646` 동일 회선 사업자 이중화: 지역 또는 전국 단위의 회선 사업자 장애 위험에 대응하기 어려웠다.
- `case_0646` 에그: 백업 회선으로 사용하려면 운영자 교육이 필요했다.
- `case_0646` 5G 상품: 유선 인터넷과 비교해 품질·속도·안정성이 낮다고 판단했다.
- `case_0651` 배치 처리: 일정 주기로 수행되므로 실시간 데이터를 반영하기 어렵다.
- `case_0653` Chromatic: 유료여서 제외했다.
- `case_0653` BackstopJS: 한글을 지원하지 않아 제외했다.
- `case_0654` 대화형 에이전트: 기술적 한계와 사용자 기대치 관리 측면의 우려로 제외했다.
- `case_0655` eslint-config-airbnb: 필요 이상으로 엄격한 규칙이 작업 흐름을 방해하고 생산성을 저하시킨다고 판단했습니다.
- `case_0655` 백지부터 공유 컨피그 구축: 베이스 컨피그를 두자는 팀의 의견을 수용해 대체 패키지를 조사했습니다.
- `case_0656` Canvas API 라이브러리: 구현 목표가 간단하고 공부도 해볼 겸 Canvas API를 직접 사용했다.
- `case_0657` 가입 시 이메일 수집 제거: 주문 과정에서 이메일이 필수였기 때문에 가입 과정에서 이메일 수집을 완전히 없애지 않았다.
- `case_0657` 하단 텍스트 버튼 노출: A/B 테스트 결과 휴대폰번호로 계속하기를 강조한 A안이 사용성이 뛰어나고 인증 비용 가드레일을 초과하지 않아 최종 채택되지 않았다.
- `case_0658` Elasticsearch 7.1.1: randomScore 함수를 지원하지 않아 광고 노출 관련 스크립트를 사용할 수 없었다.
- `case_0658` Elasticsearch 7.10.1: 현재 API에서 사용하는 기능들이 deprecated되어 보수적인 마이그레이션에 적합하지 않았다.
- `case_0658` remote reindex: 기존 Elasticsearch의 인덱스를 복사하면서 기존 리소스를 건드리게 되어 보수적인 마이그레이션 방식에 맞지 않았다.
- `case_0659` WebSocket: 응답을 찾는 과정이 실시간일 필요가 없고 클라이언트와 서버의 지속적인 연결도 불필요하다고 판단해 일반 HTTP를 선택했다.
- `case_0660` RDB 저장: 빈번한 조회와 하루 동안의 유지 조건을 고려해 빠른 저장·조회가 가능한 메모리 기반 Redis를 선택했다.
- `case_0665` Facebook Conceal: 이미 아카이브된 상태라 최신 보안 요구사항을 충족하거나 새로운 보안 위협에 대응하기 어려울 수 있어 채택하지 않았다.
- `case_0665` 상태관리 라이브러리 적용: 싱글톤 클래스 구조보다 변경 범위가 커 테스트 범위와 소요 시간이 늘어날 수 있어 채택하지 않았다.
- `case_0666` 임시 브랜치 방식: 임시 브랜치 방식은 실제로 강제 푸시한 릴리즈 브랜치의 로컬 저장소가 갱신되지 않아 최종 방식에서 제외했다.
- `case_0667` nori 형태소 분석기: 문장에 따라 예상치 못한 금칙어 판정이 발생했고, 자체 단어 사전을 확인하기 어려워 사전 관련 요구사항에 대한 확장이 어려웠다.
- `case_0667` String.contains() 순회: 금칙어 목록을 순회하며 검사하는 방식의 시간복잡도가 O(nm)이라 성능 테스트 결과가 좋지 않았다.
- `case_0668` Spring Cloud Hystrix: maintenance 모드로 전환되어 대체 모듈인 Resilience4j를 선택했다.
- `case_0668` try-catch 처리: 장애 상태에서 빠르게 실패 처리하고 공통플랫폼 정상화 시 자동으로 서비스가 정상화되는 운영상의 이점이 더 크다고 판단했다.
- `case_0669` 외부 업체 문자/API 장애 알림: 장애 알림이 충분히 빠르지 않았고 실제 결제 영향 여부를 판단하기 어려웠다.
- `case_0670` 수기 장애 대상 추출 후 배치 취소: 대사 작업이 다음날부터 가능해 VOC가 발생할 수 있어 실시간 상태 조회 및 취소 방식으로 개선했다.
- `case_0672` Kotlin Coroutine: suspend 함수와 확장함수 적용 등 프로덕션 코드 변경이 필요하고, suspend 전파와 Kotlin 러닝커브가 발생한다.
- `case_0672` Reactive Programming: 코드 흐름이 파편화되고 함수 전체에 Reactive Streams를 적용해야 하며, 실제 스레드 전환으로 성능 및 디버깅 부담이 발생한다.
- `case_0673` create-react-app: 추가 설정이 복잡하고 webpack 기반이라 코드 베이스가 커지면 빌드가 느리며 deprecate 가능성이 있어 변경했다.
- `case_0673` MobX: 새로운 표준으로 zustand를 정하면서 기존 상태 관리 라이브러리에서 변경했다.
- `case_0673` axios-mock-adapter: axios에 의존적이고 실제 네트워크 요청이 발생하지 않아 디버깅이 불편해 MSW로 변경했다.
- `case_0673` Styled Components: 스타일링 컴포넌트를 반복적으로 선언해야 하고 CSS 파일의 크기가 커져 Tailwind CSS로 변경했다.
- `case_0674` Lambda@Edge: 응답 body를 수정할 수 있다고 이해해 선택했지만, origin에서 전달되는 response body를 참고할 수 없어 최종적으로 CloudFront Functions를 사용했다. **(technologies에도 있음)**
- `case_0674` Viewer response에서 HTML body 수정: Viewer response에서는 origin에서 넘어온 body를 읽을 수 없어 기존 HTML에 OG 메타태그를 주입할 수 없었다.
- `case_0674` Custom header로 bot 여부 전달: Viewer request에서 추가한 custom header가 origin response 단계에서 사라져 Viewer response 함수가 bot 여부를 확인할 수 없었다.
- `case_0675` Nx: 당시 프로젝트가 아직 걸음마 수준이라 모노레포 빌드시스템 적용이 필요한 수준은 아니라고 판단했다.
- `case_0675` Turborepo: 당시에는 모노레포 빌드시스템 적용이 필요한 수준이 아니라고 판단해 도입하지 않았다.
- `case_0675` Lerna: 당시에는 모노레포 빌드시스템 적용이 필요한 수준이 아니라고 판단해 도입하지 않았다.
- `case_0676` Turbowatch: Turborepo의 dependsOn과 함께 사용할 경우 예상하지 못한 이슈가 발생할 수 있다고 명시되어 있어 사용하지 않았다.
- `case_0676` Vercel 원격 캐시: 외부 서비스라 보안 검토가 필요하고 사용 인원당 매월 비용이 발생해 자체 호스팅을 선택했다.
- `case_0679` @SpringBootTest: Spring IoC 컨테이너를 사용하는 테스트는 테스트 피드백이 느리고 테스트 격리와 동시 실행에 부담이 있어 제거했다.
- `case_0679` 라이브 환경의 외부 시스템 호출: 잘못된 데이터 누적과 외부 시스템의 비정상 기능으로 테스트의 결정성이 떨어질 수 있어 사용하지 않았다.
- `case_0679` fixture 기반 도구: Object Mother가 더 가볍고 관리하기 편리하다고 판단했다.
- `case_0686` GPT 단독 운영: 여러 케이스를 생성하고 검토한 결과 GPT의 메시지만으로는 운영에 한계가 있었다.
- `case_0691` CustomExecutorService: ExecutorService의 모든 메소드에 데코레이터를 적용하는 방식은 코드 관리 포인트가 증가해 채택하지 않고, 기존 ExecutorService를 ThreadPoolTaskExecutor로 전환했다.
- `case_0692` ContentSlotPlate 중간 추가 모델: ContentSlotPlate 각각의 Version을 관리해야 한다는 요구사항을 놓쳐 도메인 모델링을 수정했다.
- `case_0693` DCNv2: Two-Tower 임베딩 버전 변경 후 성능이 크게 흔들렸고, 모든 피처를 동일한 비중으로 교차시켜 피처 분포 변화에 민감하게 반응했다.
- `case_0693` 후보 900개 운영: 후보를 900개까지 늘려도 VTR 개선은 300개 대비 +0.9%p 수준이어서, 후보 증가에 따른 이득보다 지연시간 비용이 크다고 판단했다.
- `case_0694` LLM 전부 판정: 같은 코드에 대한 심각도 판정이 매번 달라질 수 있어 결과를 신뢰하기 어렵기 때문에 규칙 위반 여부와 심각도 판정을 분리했다.
- `case_0694` 린팅·리팩터링 설정 변경 규칙: 빌드 최적화나 린팅 목적의 변경이 대부분이라 탐지 빈도가 높고, 자주 잡히면 결과가 읽히지 않기 때문에 제거를 검토했다.
- `case_0696` 기존 선호 데이터셋: 화자, 문장, 음질 등 여러 조건이 함께 달라져 보상 모델이 말하기 스타일 지시가 아니라 자연스러움이나 화자 특성을 학습할 수 있기 때문에 counterfactual preference dataset을 사용했다.
- `case_0696` DPO: 고정된 오프라인 선호 데이터만 사용해 현재 모델이 새로 생성한 음성의 실패 유형을 학습에 반영하기 어려워 online reinforcement learning을 적용했다.
- `case_0697` 새로운 분석 플랫폼: 기존 Hadoop 환경과 실행 도구를 활용하고 새로운 분석 플랫폼을 만들지 않았다.
- `case_0697` MCP 서버: 실행 도구 자체의 문제가 아니라고 판단해 MCP 서버 같은 연동 계층을 새로 붙이지 않았다.
- `case_0698` 로컬 Airflow: 초기 구축 비용이 크고 실제 환경과 다르면 운영 환경에서 실패할 수 있었다.
- `case_0698` 개발용 Airflow: submodule update부터 DAG file processing까지 걸리는 시간이 길었다.
- `case_0698` 테스트용 Airflow: 수정할 때마다 파일을 복사해야 했고 접속할 때마다 prod VPN을 연결해야 했다.
- `case_0698` 사내 공유 스토리지: 파일 수가 많을 때 느려지고 권한이 바뀌는 문제가 있었다.
- `case_0701` 재사용 가능한 script: 반복 명령을 스크립트로 묶는 것보다 LLM을 활용하면 고정적인 script가 아니어도 빠르고 쉽게 변경할 수 있고, skill 단위 묶음이 LLM orchestrator의 기반이 된다고 판단했다.
- `case_0703` DPO: 고정된 preference dataset만 사용하는 offline 학습 방식은 학습 중 현재 모델이 새롭게 생성하는 음성의 장단점과 실패 유형을 학습 신호에 반영하기 어렵기 때문에 최종 방법으로 선택하지 않았다.
- `case_0703` 보상모델 단일 점수 최적화: 발화지시 점수만 최적화하면 발음 오류, 화자 음색 변화, 음질 저하가 발생할 수 있어 네 가지 목표를 함께 최적화하는 방식으로 대체했다.
- `case_0704` Index 기반 Hidden dimension pruning: PCA 기반 방식이 Distillation 전 구간에서 일관되게 더 높은 성능을 보여 채택하지 않았다.
- `case_0704` Layer pruning: 동일 파라미터 규모의 Width-pruned 모델보다 높은 성능을 보이지 못해 Layer 수를 유지했다.
- `case_0704` Single-stage Pruning & Distillation: 3B에서 0.9B로 직접 압축하는 방식이 Two-stage Cascade 방식보다 낮은 성능을 보여 선택하지 않았다.
- `case_0705` GRPO: GRPO의 한계를 극복하고 학습 효율과 안정성을 높이기 위해 DAPO를 도입했다.
- `case_0705` Reverse KL: 분포를 미리 날카롭게 만들어 RL이 사용할 탐색 여력을 제한할 수 있어 Forward KL을 선택했다.
- `case_0705` Rejection Sampling: 실패 trajectory의 exposure bias 교정 효과를 잃고 생성 비용이 낭비될 수 있어 적용하지 않았다.
- `case_0705` Parallel-RL: 1.3B·0.9B 모델에서는 학습이 불안정하고 성능 향상이 유의미하지 않아 Multi-Domain RL을 적용했다.
- `case_0706` Causal Attention + Last Token Pooling: 검색 태스크에서 Bidirectional Attention + Mean Pooling보다 낮은 성능을 보여 채택하지 않았다.
- `case_0706` In-batch NCE: HN-only 손실 함수가 더 우세한 성능을 보여 채택하지 않았다.
- `case_0706` GIST: HN-only 손실 함수가 더 우세한 성능을 보여 채택하지 않았다.
- `case_0706` HN-only, Temperature=0.05: Temperature=0.02가 0.05보다 더 좋은 성능을 보여 0.02를 채택했다.
- `case_0707` 정식 DB: 비개발자가 정식 DB를 붙이면 접근 권한 설계와 운영·보안 부담이 생긴다고 판단했다.
- `case_0708` 인력 증원: 이벤트 규모가 증가할 때마다 분석 인력을 늘리는 방식은 지속 가능하지 않았다.
- `case_0708` 범용 LLM에 원본 이벤트 전달: 내부 환경 맥락을 알지 못해 정상적인 배포 활동도 침투 시도로 판정했다.
- `case_0708` 개별 이벤트 분석: 개별 명령어만으로는 개발자의 배포 작업과 공격자의 침투 시퀀스를 구분할 수 없었다.
- `case_0708` 원본 이벤트 데이터 전달: 불필요한 정보가 토큰을 낭비하고 정확도를 떨어뜨렸으며, 탐지 유형별 신호 차이를 반영할 수 없었다.
- `case_0708` 모든 이벤트 AI 분석: 수억 건의 이벤트를 모두 분석하면 비용이 폭증하고 실시간 대응에 필요한 처리 속도를 확보할 수 없었다.
- `case_0710` H2 데이터베이스: 운영 환경과 동일한 DB를 사용하기 위해 PostgreSQL로 변경했다.
- `case_0711` 넓은 범위의 AI 리팩터링 요청: 변경 범위가 넓어 검증이 어려워 작은 단위의 요청으로 변경했다.
- `case_0712` Rust: 간단한 라이브러리도 기본 설정에서 MB 단위 바이너리가 생성되는 경우가 많았고, no_std를 사용하면 개발 생산성이 크게 떨어져 C++을 선택했다.
- `case_0712` no_std: 바이너리 크기는 줄일 수 있지만 문자열 처리, 오류 처리, 파일 입출력 등 기본 기능을 직접 다뤄야 해 개발 생산성이 크게 떨어졌다.
- `case_0712` RLE 압축: 비트 시퀀스 용량은 더 줄일 수 있지만 select0 연산을 더욱 복잡하게 만들기 때문에 적용하지 않았다.
- `case_0714` vllm-omni: Kanana-O의 파이프라인이 기존 프레임워크가 가정하는 패턴과 맞지 않아 채택하지 않았다.
- `case_0715` fork: 부모 프로세스의 메모리를 복사해 CUDA 컨텍스트와 충돌할 수 있어 사용하지 않았다.
- `case_0715` Uvicorn 멀티워커: GPU 메모리가 부족해지고 Thinker·Talker 간 임베딩 전달이 네트워크를 거치게 되어 사용하지 않았다.
- `case_0717` Newton-Schulz: Polar Express가 더 정확한 Orthogonalization을 가능하게 한다고 판단해 채택하지 않았다.
- `case_0718` Joint Scaling Law: 모델 크기와 데이터 양의 2축 Grid에서 최적 Hyperparameter를 탐색해야 해 비용이 많이 들고, 모델 크기에는 MuP라는 이론적으로 더 탄탄한 대안이 있다고 판단했다.
- `case_0718` Batch Size Transfer: Batch Size의 Scaling 방식에 대한 연구가 일관되지 않고 Throughput 최적화를 위해 훈련 중 변경되기도 해 Reliable한 방법론을 결정하기 어렵다고 판단했다.
- `case_0719` TransformerEngine 단독 구현: Non-GEMM 커널의 효율성이 낮아 BF16 Baseline 대비 기대한 성능 향상이 없었다.
- `case_0720` 트랜잭션 범위 축소: 트랜잭션을 가볍게 만들어 누락 건수는 줄였지만 DB 영속화 시간이 0이 되지 않아 경쟁 조건을 구조적으로 제거하지 못했다.
- `case_0720` 실시간 상태 전이와 Replayer 병행: Report Server와 Report Replayer가 동시에 상태 전이를 수행하면서 멱등성 가드가 과금 이벤트 발행을 막아 새로운 과금 이벤트 누락을 만들었다.
- `case_0720` 처리 순서 강제: 처리 순서를 코드 곳곳의 암묵적 제약으로 강제하는 방식은 유지보수 관점에서 위험하다고 판단했다.
- `case_0723` Sequential RL: IF RL 후 Tool RL을 순차적으로 수행하면 IF와 Tool 성능을 높이는 과정에서 수학 풀이 등 기존 문제 해결 능력이 저하되었다.
- `case_0723` 영어 추론 데이터 단순 번역: 전체 번역은 내용이 간소화되거나 논리적 연결이 헐거워졌고, 청크 단위 번역도 한국어 고난도 문제 해결에 부족했다.
- `case_0726` 상세 기획서 작성: 상세 기획서와 화면 설계서를 작성하는 대신 AI로 작동하는 프로토타입을 먼저 만들고 리뷰하는 방식을 선택했다.
- `case_0726` 바이브 코딩: 오목 문제에서 AI 모델들이 방어적으로 답변해 한계를 느껴 직접 알고리즘을 개발하는 방향으로 전환했다.
- `case_0727` KL Divergence Penalty: 기준 모델에서 크게 벗어나는 것을 막는 안정화 장치가 탐색을 지나치게 제한할 수 있었고, 적용하지 않은 경우 더 큰 성능 향상을 확인했다.
- `case_0729` 모델 분리·라우팅: 여러 모델로 분리하면 시스템 운영이 복잡해지고 모델별 운영 정책과 응답 형식을 따로 맞춰야 했다.
- `case_0734` Markdown만으로 QA 생성: Markdown만으로 QA를 생성하면 시험 문제 같은 어색한 질문이 나왔다.
- `case_0737` Type B 데이터 포함: Type B를 포함했을 때 모델 성능이 오히려 하락했다.
- `case_0739` 보이스 클로닝 재합성: 배우가 직접 녹음한 음성보다 표현력이 떨어져 제외했다.
- `case_0741` Logstash: CDC 파이프라인 도구로 검토했지만 Kafka Connect를 최종 선택했다.
- `case_0741` NiFi: CDC 파이프라인 도구로 검토했지만 Kafka Connect를 최종 선택했다.
- `case_0741` PGSync: CDC 파이프라인 도구로 검토했지만 Kafka Connect를 최종 선택했다.
- `case_0744` Parcel: 복잡한 커스터마이징에 제한이 있고 대규모 프로젝트에서 성능 저하와 한계가 있다고 판단했다.
- `case_0744` Rsbuild: 생태계 규모와 지원이 부족해 실서비스 적용이 어렵다고 판단했다.
- `case_0751` snapshot.select.statement.overrides: 여러 테이블을 캡처할 때 테이블마다 일일이 설정해야 하는 번거로움이 있다.
- `case_0752` TimestampRouter: 생성 날짜가 들어간 인덱스로 수정해야 하는 요구 사항을 충족하지 못했다.
- `case_0755` 위원회 기반 질의: 여러 모델을 동시에 실행해야 해 GPU 메모리 사용량과 추론 시간이 증가하고, 대량 이미지 처리 환경에서 오버헤드를 감당하기 어려웠다.
- `case_0757` 단일 모델 통합: 리스크별 성격과 탐지 기준이 달라 모델의 판단 기준이 모호해지고 성능이 희석될 수 있어 채택하지 않았다.
- `case_0758` 상용 LLM 서비스: 입출력 검사와 응답 생성에 모두 사용하면 비용이 빠르게 증가하고 필터링 시간으로 응답 시간이 길어질 수 있어 직접 작은 모델을 개발하는 방향을 택했다.
- `case_0758` LLM 정렬(Alignment): LLM을 만드는 과정에서 이루어지는 방법이므로 LLM을 응용해 서비스를 개발하는 입장에서는 시도할 수 없었다.
- `case_0772` TDD: 레거시 코드를 분석하는 특성상 Test Driven하게 개발하지 않기 때문에 불필요한 제안을 줄이기 위해 제외했다.
- `case_0772` 전체 프로젝트 일괄 리팩토링: 기대와 다른 결과나 감당하기 어려운 변경사항 덩어리가 생길 수 있다.
- `case_0774` MLflow: 학습에 필요한 시간과 인프라 운영 부담이 크고, 실제 필요한 기능보다 복잡성이 과도해 채택하지 않았다.
- `case_0781` CDN 정적 리소스 업로드: 관리 포인트가 늘어나고 리소스를 주기적으로 삭제·갱신해야 했으며, 추가 네트워크 요청으로 기대만큼의 성능 향상을 체감하기 어려웠다.
- `case_0782` STDIO Transport: 카카오 AI 서비스에 통합하기 쉬운 원격 MCP 서버를 목표로 하므로 로컬 프로세스 기반 STDIO Transport는 지원하지 않았다.
- `case_0783` 해외 OCR 모델: 한국적인 표현이나 복잡한 한글 상호명을 정확하게 인식하는 데 어려움이 있어 카나나 모델로 대체했다.
- `case_0785` 서버별 Alloy 설치: 수집 대상 서버가 현재 20대이고 앞으로 늘어날 예정이라 수십 대 서버의 설정을 관리하고 일관성을 유지하는 운영 부담이 컸다.
- `case_0785` 서버별 Alloy 에이전트 운영: SSR으로 이미 리소스 압박을 받고 있는 서버에 Alloy 프로세스를 추가하는 것이 바람직하지 않았다.
- `case_0789` CoT Prompting: 오픈소스 추론 모델의 안정적이고 높은 품질의 추론 경로를 활용하기 위해 자체 PLM 기반 CoT Prompting 대신 Data Distillation을 선택했다.
- `case_0790` GRPO: 동일 조건 비교에서 PPO가 학습 후반부에 GRPO보다 약간 더 높은 Reward에 도달했다.
- `case_0792` 범위 기반 쿼리(BETWEEN): 변화분 PK가 연속된 구간일 때 WHERE IN 대신 더 효율적인 방식인지 고민했지만 적용하지 않았다.
- `case_0796` 기존 Diffusion-DPO 방식: 생성 이미지들만으로 Winning과 Losing 이미지 쌍을 구성해 학습하므로 실사 수준의 품질을 학습하기 어렵다.
- `case_0796` Single stage 학습: 실사와 생성 이미지를 활용한 전략을 한 번에 적용하는 방식은 좋은 결과로 이어지지 않았다.
- `case_0801` Intermediate dimension shuffling: loss나 모델 성능 측면에서 이득이 보이지 않아 적용하지 않았다.
- `case_0801` 50% expert 파라미터 랜덤 초기화: loss나 모델 성능 측면에서 이득이 보이지 않아 적용하지 않았다.
- `case_0804` LLM 단일 모델 통합: 음성 토큰을 기존 텍스트 LLM vocabulary에 직접 포함하면 추론 속도와 계산 효율이 떨어지고, LLM을 fine-tuning하는 과정에서 기존 언어 지식이 손실될 가능성이 있었다.
- `case_0805` 순차 학습: 병합 학습이 모달리티별 성능 균형 측면에서 더 적합하다고 판단해 병합 학습을 기본 전략으로 채택했다.
- `case_0805` 전체 Joint Training: 모든 모달리티 데이터를 모든 스테이지에서 사용하면 학습 시간이 길고, 독립 모듈이 개선될 때마다 통합 모델을 처음부터 재학습해야 했다.
- `case_0809` 서버 로그 UPSERT: 서버 로그의 고유 ID로 중복을 제거할 수 있지만 로그 양이 많아 최적화 비용이 이점보다 컸고, 중복 제거를 Spark 지표 계산 단계에서 처리하기로 했다.
- `case_0809` event time과 watermarks: 재처리 중에도 최종 지표가 변하지 않는 멱등성을 보장하기 위해 사용하지 않았다.
- `case_0809` 시간 관련 타입과 hour transform: Iceberg의 UTC 해석과 팀 Spark 세션의 KST 설정 사이에 타임존 문제가 발생했다.
- `case_0811` UIzard·Galileo AI: 다양한 툴을 시도했으나 Design MVK 부족으로 실패했다.
- `case_0812` 순수 바이브 코딩: 코드를 거의 들여다보지 않고 느낌에 맡기는 방식은 현실의 프로덕션 개발 환경에 그대로 적용하기 어렵고 적용해서도 안 된다고 판단했다.
- `case_0823` DPO: DPO는 policy 모델이 이전 버전보다 좋아진다는 보장이나 목적성을 직접 내포하지 않았고, offline DPO는 실제 policy의 출력 분포에서 벗어난 데이터에 의존할 수 있었다.
- `case_0823` Scalar reward model: 하나의 숫자만 출력해 점수 부여 이유를 해석하기 어렵고, policy 모델이 업데이트되면 예측 reward의 신뢰도가 하락할 수 있었다.
- `case_0825` upstreamLatency 수집 비활성화: upstream latency 수집을 제외해도 Nginx의 초당 1만 개 이상 메트릭 누락은 계속 발생하며, 공통 Helm Chart 수정과 별도 운영에 따른 영향 및 장기 운영 리스크가 우려되어 채택하지 않았다.
- `case_0827` requestIdleCallback: 메시지 렌더링은 우선순위가 높은 작업이고 일정한 주기로 큐를 확인해야 하며, 글 작성일 기준 iOS Safari에서 지원되지 않아 제외했습니다.
- `case_0827` requestAnimationFrame: dequeue 및 말풍선 렌더링은 화면 프레임 주기와 무관하고 서버 데이터 속도에 의존하는 작업이라 적합하지 않았습니다.
- `case_0831` UPSERT 모드: 서버 로그의 데이터 양이 너무 방대해 중복 제거 이점보다 최적화 비용이 컸고 중복 제거는 Spark 지표 계산 과정에서 수행하기로 했습니다.
- `case_0831` 이벤트 타임·워터마크: 데이터 재처리 시에도 최종 지표 값이 변하지 않도록 멱득성을 보장하기 위해 사용하지 않았습니다.
- `case_0831` 시간 관련 transform 파티션: 시간대 차이로 인해 Spark에서 잘못된 시간이 반환되거나 실제 처리 시각보다 9시간 이전 파티션에 적재될 수 있어 사용하지 않았습니다.
- `case_0835` 데이터 로드 중 로딩 화면: 새로운 로딩 화면 디자인이 필요하므로 최종 방식으로 선택하지 않았다.
- `case_0835` 플래그 변수로 렌더링 제어: 코드 가독성을 떨어뜨리고 상태 관리가 복잡해질 수 있어 지양했다.
- `case_0836` NoPreloading 전략: 프리로드 작업은 제거했지만 페이지 전환 속도가 느려질 수 있어 최종 방식으로 선택하지 않았다.
- `case_0836` Custom Preloading 전략: 프리로드 기준이 모호하고 브라우저 유휴 상태·네트워크 상태·폴리필 등을 추가로 고려해야 해 ngx-quicklink를 선택했다.
- `case_0836` PreloadAllModules 전략: 공격적인 사전 로딩으로 네트워크 사용량과 메인 스레드 부하가 증가했다.
- `case_0838` Depth pruning: Width pruning에 비해 성능이 낮아 이 글에서는 다루지 않았다.
- `case_0838` From-scratch pre-training: 기존 Kanana Essence에서 Pruning & Distillation하는 방식을 선택했다.
- `case_0838` Learning rate annealing 및 Checkpoint averaging: 실험했지만 큰 효과를 확인하지 못했다.
- `case_0840` Publish API: 카리브의 Publish API는 Redis에 메시지를 전달하는 것만 수행하므로 메시지를 fan-out하는 구조의 성능을 측정하기에 적합하지 않았다.
- `case_0841` TCP_CORK: 버퍼링으로 네트워크 I/O는 줄였지만 setsockopt 등의 시스템 호출과 커널 작업으로 CPU 오버헤드가 증가했다.
- `case_0841` io_uring: Go 언어의 구조와 맞지 않는 부분과 추가 검토가 필요한 부분이 있어 적용을 보류했다.
- `case_0842` encoding/json: 더 높은 성능을 위해 여러 JSON 라이브러리를 비교한 뒤 go-json으로 교체했다.
- `case_0843` 메시지 값 전달: 값 복사 비용이 Heap Escape 비용보다 커서 포인터 전달 방식보다 지표가 좋지 않았다.
- `case_0853` 서버 점검 후 배포: DTO 케이스 변경만으로 여러 번의 서버 점검을 진행해야 해 작업 규모가 과도했다.
- `case_0853` 한 번에 모든 케이스 배포: 모든 케이스를 한 번에 변경하는 방식은 리스크가 너무 크다고 판단했다.
- `case_0853` Filter: Filter에서는 타겟이 되는 클래스를 알아낼 수 없었다.
- `case_0853` Interceptor: Interceptor에서는 원본 Request의 Body를 변경시키기 어려웠다.
- `case_0854` Resize: 고해상도 이미지를 비전 인코더가 처리할 수 있는 고정된 크기로 줄이기 때문에 실제로는 저해상도로 처리하게 된다.
- `case_0854` Dynamic high-resolution: 사전학습된 비전 인코더를 그대로 활용할 수 있지만 이미지를 조각내어 처리하므로 전체 이미지 맥락을 제한적으로만 고려한다.
- `case_0858` Redis pub/sub: 주기적으로 재연결하고 메시지를 모아서 내려주는 방식은 Redis pub/sub으로 달성하기 어려웠다.
- `case_0859` 롱폴링: 내부 메시지 전파 구조를 push 방식으로 전환하면서 롱폴링 지원을 중단했다.
- `case_0860` 기존 Scaling law: 파라미터와 데이터 규모를 늘리는 방식은 충분한 Compute budget을 필요로 하므로 조직의 목표에 적절하지 않았다.
- `case_0861` Kanana Essence 직접 Pruning: Kanana Essence에 직접 Pruning을 적용해 Kanana Nano를 초기화하면 학습에 실패했다.
- `case_0861` From scratch 학습: 비교를 위한 Baseline으로 학습했지만 Pruning & distillation보다 더 많은 데이터를 사용했고 최종 전략으로 채택하지 않았다.
- `case_0867` 단일 Iceberg 테이블 통합: 여러 Flink 작업이 하나의 Iceberg 테이블에 동시에 커밋하면서 커밋 충돌이 발생할 수 있고, 샤드가 많은 테이블에서는 재시도 횟수 증가만으로 안정성을 보장하지 못해 운영 서비스에 적용하지 않았다.
- `case_0870` Kafka 기반 Change event 적재: Iceberg로 직접 적재하면 Kafka 의존성과 메시지 처리율 상한을 제거할 수 있어 직접 RowData 적재 방식을 사용했다.
- `case_0871` 샤딩 테이블 단일 Iceberg 테이블 통합: 여러 Flink 잡이 하나의 Iceberg 테이블에 커밋하면서 커밋 충돌이 발생할 수 있어 실서비스의 안정성을 확보하기 어렵다고 판단했다.
- `case_0871` 커밋 재시도 횟수 증가: 샤딩 테이블이 100개를 넘는 경우 재시도 횟수만 늘리는 것으로는 안정성을 확보하기 어렵다고 판단했다.
- `case_0874` FlinkRuntimeException 발생 후 job 중지: DDL 직전 생성된 메시지가 Kafka에 전송되었다는 것을 보장하지 못한다.
- `case_0877` Debezium + Kafka Connect 조합: 대규모 테이블에서 스냅샷 처리량과 처리 시간이 운영 환경의 바이너리 로그 보존 기간을 초과할 수 있다.
- `case_0877` 별도 시스템 스냅샷: 스냅샷과 빈로그 스트림 단계에서 서로 다른 시스템을 사용해야 한다.
- `case_0878` DDL 이벤트 발생 시 예외로 중단: 잡이 중단되면 DDL 직전 메시지의 Kafka 커밋 여부를 보장할 수 없다.
- `case_0878` 별도 모니터링 잡: 데이터베이스와 테이블이 늘어남에 따라 모니터링 잡을 관리하기 어렵다.
- `case_0881` Amplify Studio: 컴포넌트가 아닌 디자인 요소의 처리, 일부 페이지의 디자인 반영, 대용량 디자인 파일 처리에 제약이 있어 실제 프로젝트 환경에 적용하기 어려웠다.
- `case_0881` Locofy: 범용적인 도구라서 팀의 특수한 요구사항과 상황에 완전히 부합하지 않았고, 디자인 변경 시 이벤트·바인딩·프로퍼티 유지와 생성 코드 적용이 불편했다.
- `case_0882` 상용 도구: 팀에 맞는 도구를 선택하기보다 필요한 기능을 직접 구현하기 위해 자체 개발을 택했다.
- `case_0885` 동적 import: await import()를 사용하면 CommonJS 환경에서 여러 코드 변경이 필요해 적용하지 않았다.
- `case_0885` Lighthouse index.cjs 가져오기: index.cjs가 Gatherer와 Audit 클래스를 내보내지 않아 필요한 기능을 사용할 수 없었다.
- `case_0886` ballast: GOMEMLIMIT이라는 GC 튜닝 해결책이 나왔으므로 ballast를 사용하지 않는다.
- `case_0890` @DBRef 객체 참조: find 기반 자동 로딩으로 연관 문서를 건별 조회해 N+1 문제가 발생할 수 있고, MongoDB에서는 같은 경계 안에서도 내장 도큐먼트나 ID 참조가 더 적절하다고 판단했다.
- `case_0891` repository.save: 전체 문서 교체 방식이라 저장 객체에 없는 필드가 삭제될 수 있고, 동시성 환경에서 다른 작업의 변경을 낡은 값으로 덮어쓸 수 있다.
- `case_0893` 메모리 한도 증가: 초기 대응으로 문제를 해결했지만 문제가 반복되었고, 전사 서버 배포 파이프라인의 공통 한도를 매번 늘리는 데 한계가 있었다.
- `case_0893` npm: 호이스팅으로 인한 유령 의존성 문제에서 자유롭지 못해 후보에서 제외했다.
- `case_0893` Yarn pnpm 모드: 문제 해결과 전환 비용 측면의 장점은 있었지만, PnP 중심의 Yarn 생태계에서 비주류 모드라 참고할 레퍼런스와 장기적인 생태계 지원이 부족할 것으로 판단했다.
- `case_0894` 커넥션 풀 증설: maximumPoolSize를 30개에서 50개로 늘렸지만 배포 직후의 커넥션 타임아웃과 응답 지연이 해결되지 않았다.
- `case_0894` 점진적 배포: 블루/그린 배포로 트래픽을 30초 간격으로 20%씩 유입했지만, 서비스 성장으로 초기 트래픽 자체가 커지면서 응답 지연이 다시 발생했다.
- `case_0895` FDD: ceo-plus에 여러 feature에서 사용되지만 범용적이지 않은 코드가 많아 shared나 common에 넣을 경우 재사용 범위를 통제하지 못하고 의존성이 다시 엉킬 위험이 있어 채택하지 않았다.
- `case_0895` 모든 API를 Entities에 배치: 특정 페이지에서만 필요한 API까지 전역 Entity에 섞여 Entity 레이어가 비대해지고 도메인 엔티티의 역할을 수행하기 어려워져 채택하지 않았다.
- `case_0897` Exposed: 대량 처리 성능 개선만을 위해 JPA 환경에 새로운 ORM을 도입하고 혼합하는 것은 설정 복잡성과 학습 곡선 측면에서 비효율적일 수 있다.
- `case_0899` 테스트 기기 문서화·OS 업데이트 제한: 테스트 기기 보유 현황을 문서화하고 기기별 OS 업데이트를 제한했지만 관리 비용이 많이 들고 근본적인 해결책이 되지 않았다.
- `case_0900` Apache Airflow ← Airflow: 확장성과 장기적인 운영 안정성 측면에서 한계가 있다고 판단했다.
- `case_0900` MLflow: 확장성과 장기적인 운영 안정성 측면에서 한계가 있다고 판단했다.
- `case_0902` Scale to Zero: 비용 효율은 높지만 콜드 스타트로 서비스 응답 속도를 보장할 수 없었다.
- `case_0903` MongoPagingItemReader: 페이지가 뒤로 갈수록 skip() 오버헤드가 증가해 수백만 건을 처리하는 배치에 적합하지 않다.
- `case_0903` Aggregation Pipeline: 이번 작업은 원본 데이터를 순차적으로 읽어 애플리케이션 레벨에서 통계를 재구성하므로 Cursor 방식이 더 적합했다.
- `case_0903` saveAll() 방식: 각 문서를 개별적으로 처리하므로 대규모 배치에서는 BulkOperations를 사용해야 했다.
- `case_0906` OpenAI function calling: 특정 AI 프레임워크에 의존하게 되어 다른 도구와의 호환성이 떨어지고, 새로운 AI 도구나 프레임워크가 등장할 때마다 별도 구현이 필요했다.
- `case_0906` LangChain tool: 특정 AI 프레임워크에 의존하게 되어 다른 도구와의 호환성이 떨어지고, 새로운 AI 도구나 프레임워크가 등장할 때마다 별도 구현이 필요했다.
- `case_0908` Entity Lifecycle 콜백: PostLoad에서 복호화한 값이 1차 캐시에서 변경된 것으로 인식되어 조회할 때마다 UPDATE가 발생했고, PreLoad 주기가 없어 문제를 해결할 수 없었다.
- `case_0910` 클라이언트 무음 감지: 구현해야 할 추가 기능이 많아 빠르게 처리할 수 있는 다른 방식을 선택했다.
- `case_0911` OpenSearch: 비용이 높고 대용량 집계 쿼리가 느렸다.
- `case_0911` Grafana Loki: 복잡한 쿼리, 집계, 다양한 필드 검색 요구사항에 맞지 않았다.
- `case_0912` Fluentd S3 Output: IAM Role Anywhere를 지원하지 않고 처리 속도가 느리며 중복 파싱과 메모리 사용량 문제가 있었다.
- `case_0912` Amazon Athena: 콜드 스타트와 대용량 집계 쿼리 지연, 스키마 관리 문제가 있었다.
- `case_0913` Signoz: 자체 스키마를 강제해 Buffer·Store·View 분리 구조를 사용할 수 없었다.
- `case_0913` Grafana: 로그 검색 UI가 부족했다. **(technologies에도 있음)**
- `case_0917` Vary: Origin: CDN 서버 수정이 필요했고 당장 적용할 수 없었다.
- `case_0917` crossOrigin: anonymous: 충전 서비스와 다른 서비스가 같은 서버에서 운영되고 있어 예상치 못한 사이드 이펙트를 우려했고, 적용 후 다른 서비스에서 CORS 에러가 발생해 롤백했다.
- `case_0920` RAG: 코드처럼 세부적인 분석이 필요한 경우 검색되지 않은 코드가 컨텍스트에서 누락될 수 있고, 사용한 모델의 입력 토큰 한도로는 기술과제 전체 코드를 제공할 수 있어 RAG를 사용하지 않았다.
- `case_0920` LangChain: 여러 기능을 사용할 필요가 없어 LLM 호출에는 사용하지 않고 문서·파일 loader 관련 기능만 사용했다. **(technologies에도 있음)**
- `case_0920` API Gateway + Lambda: 짧은 해커톤 기간에 빠른 프로토타이핑과 디버깅 편의성을 얻기 위해 EC2 배포를 선택했다.
- `case_0920` Amazon ECS ← ECS: 짧은 해커톤 기간에 빠른 프로토타이핑과 디버깅 편의성을 얻기 위해 EC2 배포를 선택했다.
- `case_0922` Istio: 기존에 Istio를 사용하지 않아 모든 클러스터에 신규 설치가 필요했고, 당시 IDC Kubernetes 버전이 지원하지 않아 버전 업그레이드와 구성 변경이 필요했다. sidecar proxy로 인한 리소스 점유와 Ingress 변경도 필요해 빠른 멀티 클러스터 도입에 비해 비용 대비 효과가 낮다고 판단했다.
- `case_0922` Cilium eBPF: 패킷 단위 제어만으로는 클러스터 컨텍스트와 서비스 식별을 포함한 고수준 라우팅을 구현하기 부족했고, 정책 관리와 클러스터 식별·서비스 맵핑 로직을 별도로 구현해야 해 운영·유지보수 난이도가 높다고 판단했다.
- `case_0922` AWS Global Accelerator: ALB에 고정 Anycast IP를 제공해 GSLB 연동과 자동 failover를 가능하게 하지만, 당시 운영 안정성과 장애 상황 대응에 대한 실질적인 경험이 부족해 적용을 보류했다.
- `case_0926` 파인튜닝: 변화하는 대출 상품과 고객 정보를 모델에 직접 반영하는 방식은 비용 효율성이 낮았다.
- `case_0926` 멀티 에이전트 아키텍처: 대출 상담 태스크가 선형적이고 명확하며, 에이전트 간 역할 분담과 협업이 불필요했다.
- `case_0928` Connection Pool의 PreparedStatement 캐시: HikariCP에서는 Connection Pool이 PreparedStatement를 캐시하는 것을 안티패턴으로 보고 JDBC 구현체에 캐시 관리를 위임한다.
- `case_0929` Amazon Titan Image Generator: Nova Canvas가 더 긴 프롬프트를 지원했고, 이미지 결과 비교에서 Nova Canvas가 가장 자연스럽고 예쁘다고 평가되어 선택하지 않았다.
- `case_0929` Stability AI SDXL: Nova Canvas가 더 긴 프롬프트를 지원했고, 이미지 결과 비교에서 Nova Canvas가 가장 자연스럽고 예쁘다고 평가되어 선택하지 않았다.
- `case_0930` Lambda와 Bedrock Agent 서버리스 구조: 길이를 알 수 없는 거래 내역 목록을 Lambda 함수 인자나 Bedrock Agent 프롬프트로 전달하는 것이 비효율적이라고 판단해 서버에서 Bedrock API를 호출하고 Tool 핸들러를 직접 실행하는 방식으로 변경했다.
- `case_0937` Mock HTTP 서버: 실제 Mock HTTP 서버를 띄우는 것보다 Mock 객체를 Bean으로 제공하는 방식이 편리하다고 설명한다.
- `case_0938` Ktor Generator: 기능별 의존성을 명확하게 확인하기 위해 직접 코틀린 프로젝트를 생성하는 방식을 선택했다.
- `case_0938` embeddedServer 방식: 서버 설정의 가시성을 위해 설정을 분리하는 EngineMain 방식을 선택했다.
- `case_0939` spring.config.import: 애플리케이션의 application.yml에 사용하는 클라이언트의 yml 파일을 모두 직접 명시해야 하므로 클라이언트가 늘어날수록 누락 가능성이 있다.
- `case_0939` spring.profiles.include: 애플리케이션의 application.yml에 프로필을 명시해야 하고, 환경변수 파일이 application-${프로필 이름}.yml 규칙을 따라야 한다.
- `case_0939` 동적 @PropertySource 경로: 여러 프로필을 활성화하면 spring.profiles.active에 의도하지 않은 값이 들어가 애플리케이션이 정상 동작하지 않을 수 있다.
- `case_0940` 어드민 서버 직접 호출: 서빙 서버의 스케일 아웃 시 어드민 서버로 트래픽과 부하가 전이되고, 동기적인 어드민 서버 의존으로 병목 지점이 바뀌기 때문입니다.
- `case_0940` RabbitMQ: 제한된 확장성 때문에 대규모 분산 시스템 환경에 적합하지 않을 수 있기 때문입니다.
- `case_0940` Kafka ← Apache Kafka: 복잡한 설정과 운영이 동반되며 다양한 기능 지원 때문에 러닝 커브가 높기 때문입니다.
- `case_0941` IntelliJ 플러그인 개발: 프로젝트와 설정 파일을 구성하고 IntelliJ API를 학습해야 하며, IntelliJ 버전 상향에도 대응해야 한다.
- `case_0942` invoke_model: 모델 공급사별 API 호출 방식이 달라 다양한 모델을 사용하기에 번거롭고 비효율적이어서 Converse API를 사용했다.
- `case_0944` 기존 AI 모델: 비정형 데이터 처리를 위한 학습 데이터가 부족해 실질적으로 활용하기 어려웠다.
- `case_0944` On-demand 추론: Batch 추론보다 비용이 비싸고 안정성이 낮았다.
- `case_0946` auto commit 옵션 변경: auto commit을 끄면 트랜잭션 수행 시 관련 요청을 줄일 수 있지만, 트랜잭션을 무조건 붙여야 하므로 적용하지 않았다.
- `case_0947` Hexagonal Architecture: 도메인 모델이 명확하지 않고 코어 모듈 재사용성이 낮은 홈 서버에서는 구조적 장점보다 운영과 개발 비효율성이 커져 제거했다.
- `case_0947` 레이어 단위 패키징: 기존 레이어드 아키텍처로 회귀하지 않고 관심사 단위 패키징을 적용했다.
- `case_0948` Spring Kafka ← spring-kafka: low level로 개발해야 하므로 코딩 스타일을 강제하기 어렵고, 데이터 흐름을 코드 베이스로 파악해야 하며 잘못 코딩하면 결합도가 높아질 수 있어 Spring Cloud Stream을 선택했습니다.
- `case_0949` 수동 isDebugEnabled 확인: 비즈니스 로직의 가독성을 떨어뜨리고 로그 레벨 확인이 두 번 실행될 수 있다.
- `case_0949` Logger 인스턴스 필드 정의: 1개의 인스턴스당 1개의 Logger를 갖게 되어 메모리 사용 측면에서 비효율적일 수 있다.
- `case_0953` 네이버 지도 SDK: 예상 사용량을 고려할 때 과금 발생 가능성이 높아 선택지에서 배제했다.
- `case_0953` 카카오 지도 SDK: 예상 사용량을 고려할 때 과금 발생 가능성이 높아 선택지에서 배제했다.
- `case_0953` MapBox: 예상 사용량을 고려할 때 과금 발생 가능성이 높아 선택지에서 배제했다.
- `case_0953` OSM: 한글 표시에서 자간과 폰트 문제가 발생해 선택하지 않았다.
- `case_0954` debugDescription 활용: addressDictionary가 deprecated된 프로퍼티이므로 다시 개발한다면 다른 방식을 선택하려 했다.
- `case_0956` RIBs: 과도한 프로토콜과 객체 분리로 코드 점핑이 많고 코드 간 연결 관계를 파악하기 어려워 제거했다.
- `case_0956` TCA: 과도한 프로토콜과 객체 분리로 코드 점핑이 많고 코드 간 연결 관계를 파악하기 어려워 제거했다.
- `case_0956` 서비스 Layer별 모듈화: 빌드 시간의 이득보다 모듈과 프로젝트의 복잡도를 줄이는 것을 우선해 Layer를 모듈이 아닌 폴더로 구분했다.
- `case_0959` spring-retry 라이브러리: 스프링에 의존해야 하고 정확한 사용 방식을 익혀야 하므로, 원하는 방식으로 동작하는 재시도 로직을 직접 고안하는 방법을 선택했다.
- `case_0961` 여러 대의 스케줄러: 송금 건을 겹치지 않게 읽기 위한 복잡한 분기가 필요하고 인프라 구성도 용이하지 않으며, 송금 실행 서버에 부담을 줄 수 있어 채택하지 않았다.
- `case_0964` BRMS: 탄력적인 개발, 특정 플랫폼 종속, 확장성, 비용과 개발문화에 미칠 영향을 우려해 사용하지 않았다.
- `case_0965` DB 베타 락: Repository(Infra) 단에서 예외를 던져 서버 리소스를 불필요하게 낭비한다고 판단했다.
- `case_0970` 예외 메시지에 키값 추가: 예외가 예상하지 못한 곳에서 발생하면 키값이 없는 에러 메시지가 될 수 있어 문제점을 모두 해결하지 못한다.
- `case_0976` DB 상태 관리: 데이터베이스를 사용한 상태 관리 방식보다 빠른 읽기·쓰기와 중앙 집중식 상태 관리가 가능한 Redis를 선택했다.
- `case_0978` fromUri 메서드 사용: java.net.URI로 한 번 감싼 뒤 fromUri를 호출하는 방식은 payweb_tab을 host로 전달하지 못해 URL 정보가 누락되므로 사용하지 않았다.
- `case_0983` universal-emoji-parser: 이모지를 잘못 매핑하는 경우가 있었고 Slack의 모든 커스텀 이모지에 대응할 수 없어 사용하지 않았다.
- `case_0983` 모달·워크플로우 입력 방식: 코드블록 지원과 작성 중 채널 이동 시 내용 유지가 가능한 채팅 형식을 최종 선택했다.
- `case_0987` UIColor·UIImage extension: 여러 앱에서 사용하는 리소스 모듈 환경에서는 red100과 같은 범용적인 이름이 디자인 시스템이나 다른 코드에 영향을 끼칠 수 있어 적합하지 않았다.
- `case_0989` MongoDB: 이력성 데이터만 저장하기에는 라이선스 비용이 크고, 데이터 특성상 즉시 조회가 필요하지 않아 선택하지 않았다. **(technologies에도 있음)**
- `case_0989` Elasticsearch: 이력성 데이터만 저장하기에는 라이선스 비용이 크고, 데이터 특성상 즉시 조회가 필요하지 않아 선택하지 않았다. **(technologies에도 있음)**
- `case_0989` 직접 메시지 컨슈머 서버: 다양한 input/output 플러그인을 제공해 데이터 파이프라인 구성에 적합한 Logstash를 사용하는 방법을 선택했다.
- `case_0990` requested_at 기준 조회: 로그성 데이터 테이블이 created_at 기준으로 파티셔닝되어 있어 created_at을 사용하는 range scan보다 성능이 나을 수 없었다.
- `case_0990` 기관 코드 순회 배치: created_at을 나눠 조회하는 방식과 함께 검토했지만 표준편차를 전체 데이터 기준으로 계산해야 해 채택하지 않았다.
- `case_0990` created_at 분할 조회: 조회 데이터 양은 줄일 수 있지만 표준편차를 전체 데이터 기준으로 계산할 수 없어 채택하지 않았다.
- `case_0992` 처음과 끝을 비교하지 않기: 처음과 끝을 제외해도 다른 첫 번째와 마지막 좌표를 잇는 선분에 눈이 쌓여 곡선에 적용할 수 없었다.
- `case_0992` 곡선 세분화: 곡선을 잘게 나눌수록 비교해야 할 정사영 좌표가 많아져 성능 문제가 발생할 수 있었다.
- `case_0993` asyncer-io: jasync 대신 사용해 보았지만 애플리케이션 시작 시 커넥션 풀이 생성되지 않는 동일한 동작이 발생했다.
- `case_0996` quadraticCurveTo: 곡선 위의 중간 좌표를 알 수 없어 전구 배치에 사용할 수 없었다.
- `case_0996` bezierCurveTo: 곡선 위의 중간 좌표를 알 수 없어 전구 배치에 사용할 수 없었다.
- `case_0997` 서비스 내부 로직 목킹: 목킹한 repository를 이용하지 않거나 다른 메서드를 호출하는 내부 구현 변경에도 테스트가 깨지고, 테스트 코드보다 목킹 코드가 많아질 수 있어 최대한 자제한다.
- `case_0999` Spring Framework: 업무 요구사항을 해결할 수 있지만 Ktor가 부팅 속도, 리소스 사용량, Blocking 처리 성능과 러닝커브 측면에서 더 적합하다고 판단해 최종적으로 Ktor를 선택했다. **(technologies에도 있음)**
- `case_1002` Json Converter: 메시지에 스키마를 포함해 Kafka 로그 증가 폭이 크고 OS 자원 사용과 성능 측면에서 불리해 Avro Converter를 선택했다.
- `case_1003` Relational Migrator: 성능이 느리고 병렬 실행이 어려우며 초대형 테이블에 적합한지 의문이 있어 이번 프로젝트에서는 사용하지 않았다.
- `case_1003` CSV Import: CSV로 적재하면 기존 데이터 타입이 보장되지 않고 Oracle의 Null 값이 MongoDB에서 공백문자로 저장되어 JSON Import로 변경했다.
- `case_1006` VPA: VPA와 HPA를 혼용할 수 없어 도입하지 않았다.
- `case_1007` 서비스 단위 알림: 개발자에게 너무 많은 추천값 알림이 전달되어 알림 노이즈가 될 수 있어 사용하지 않았다.
- `case_1007` 최소 추천값 상향 조정: 자원을 절약하기 위한 프로젝트 방향과 맞지 않았다.
- `case_1007` Readiness Probe 시간 연장: Memory 부족으로 OOM이 발생해 pod이 재시작될 수 있어 적용하기 어려웠다.
- `case_1011` useQueries: 기존 컴포넌트 구조를 대폭 수정하고 쿼리를 상위로 끌어올려 props로 전달해야 하므로 선택하지 않았다.
- `case_1011` Suspense 비활성화: 순차 API 호출은 제거할 수 있지만 기존의 선언적 컴포넌트 구성 장점을 이용할 수 없어 선택하지 않았다.
- `case_1012` null 반환·예외 발생 방식: 단순한 null 반환 또는 예외 발생만으로는 오류 응답에 따른 추가적인 복구 정책과 세부 예외 처리를 지원하기 어렵다.
- `case_1012` Triple 객체: HTTP 상태 코드, 응답 본문, 오류 응답을 함께 전달하지만 nullable 처리와 오류 핸들링 책임이 외부로 전가되어 직관적이지 않고 중복 코드와 부담을 만든다.
- `case_1012` ResponseEntity 반환: HTTP 클라이언트 라이브러리 의존성이 높아져 라이브러리 교체 시 관련 코드 전체에 변경이 발생한다.
- `case_1015` DB 분리: 전산 원장과 다른 팀·서비스에 미치는 영향, 애플리케이션 CPU 여유, 촉박한 일정 때문에 DB 분리보다 성능 개선 개발을 우선했다.
- `case_1015` 분산 lock: 동일 key 기준 동시 업데이트가 없는 서비스 특성을 고려해 Redis 요청 구간을 늘리는 분산 lock을 적용하지 않았다.
- `case_1016` Next.js ← NextJS: 개발 모드에서 마크다운 수정 시 HMR이 적용되지 않고, SSG 모드에서 이미지 최적화를 지원하지 않아 선택하지 않았다.
- `case_1016` Jekyll: 루비 기반이라 커스텀하기 어려울 것으로 판단했다.
- `case_1017` 주문 API 대량 유저 조회: 주문 API를 대량 유저 조회 방식으로 변경할 수 없다고 가정했다.
- `case_1020` Spark Metastore 클라이언트 버전 업그레이드: Spark 3.x 사용자가 많고 클라이언트 버전 변경 시 모든 잡을 재검증해야 해 파급 범위가 컸다.
- `case_1020` 프록시 계층에서 RPC 변환: 레거시 요청을 신형 요청으로 바꾸는 별도 계층의 복잡도와 운영 부담이 커진다.
- `case_1020` 호환 Metastore 클라이언트 배포: 직접 통제하지 못하는 Spark 배포본에서는 구버전 RPC 호출 문제를 막을 수 없다.
- `case_1022` 제휴사 직접 연결: 제휴사를 카카오페이와 직접 연결하면 보안상 문제가 생길 수 있었다.
- `case_1022` 전용선: 전용선을 설치하면 추가 비용이 발생하고 제휴사에서 원하지 않았다.
- `case_1024` jar 원본 코드 수정: jar로 제공받은 원래 코드는 수정이 불가능해 보였다.
- `case_1026` 체크포인트 구조: Claude Code가 1M 컨텍스트를 지원하면서 다섯 단계를 한 세션에서 처리할 수 있게 되어 단계별 체크포인트와 상태 필드의 필요성이 사라졌다.
- `case_1027` 전체 지식 강제 입력 훅: 관련 없는 지식까지 반복 입력해 토큰 사용량을 늘리고 attention dilution과 잘못된 규칙 참조를 일으켰다.
- `case_1028` 통합 SKILL.md: GitOps 인프라 지식과 vLLM 서빙 지식을 한 파일에 넣으면 도메인 소유자가 아닌 팀이 다른 도메인의 지식을 수정해야 하므로 분리했다.
- `case_1030` 하드웨어 Scan Batching 지원 여부에 따른 분기 처리: 기기별 동작의 일관성을 위해 지원 여부를 판단하지 않고 모든 기기에서 직접 Buffering하는 방식을 선택했다.
- `case_1034` vLLM 포크: 새 릴리스마다 변경 사항을 병합하고 달라진 내부 인터페이스에 대응해야 해 유지보수 비용이 커지므로 외부 플러그인을 선택했다.
- `case_1035` Claude Code: Claude Code와 Codex의 결과를 모두 비교·조율할 시간이 부족해 Codex 하나만 사용했다.
- `case_1035` 전체 코드 실행 검증: 모든 제출물의 코드를 실행해 확인하기에는 시간이 부족했다.
- `case_1042` vmctl: 555조 개의 데이터포인트를 API 기반으로 다시 읽는 작업은 운영 클러스터에 지나치게 큰 부하를 주고, 대규모 환경에서 속도 한계와 조회 제한이 있었습니다.
- `case_1043` reinterpret_cast를 이용한 타입 퍼닝: 서로 다른 타입의 포인터로 객체를 접근하면 엄격한 앨리어싱 규칙을 위반한다.
- `case_1043` union 타입 퍼닝: C++에서는 비활성 union 멤버를 읽는 것이 미정의 동작이다.
- `case_1044` 엑셀 대체 입력 화면: 입력 화면만으로는 숫자의 근거와 검증 결과를 관리할 수 없어 기준 시스템이라는 목표로 전환했다.
- `case_1045` AI 모델 기반 월말 보고서 생성: 표현과 결과가 달라질 수 있고 모델 연결 문제로 공식 보고서 생성이 영향을 받을 수 있어 명시적 규칙 기반 처리로 변경했다.
- `case_1046` 응답 필터 중심 가드레일: AI가 모든 데이터를 조회한 뒤 답변에서 일부를 가리는 방식은 안전하지 않다고 판단해 접근 전 권한 경계 방식으로 전환했다.
- `case_1047` ChainedTransactionManager: 전환 초기에는 두 DB의 정합성이 맞지 않고 MySQL 쿼리의 오류 가능성도 검증되지 않았기 때문에 사용하지 않았다.
- `case_1047` 분산 트랜잭션: MySQL 쿼리만 실패하는 상황을 허용하고 Oracle 트랜잭션의 롤백에는 영향을 주지 않도록 하기 위해 사용하지 않았다.
- `case_1048` HTTP 트래픽 복사: 비즈니스 로직 호출 시 타 부서 시스템에 중복 호출 부하를 일으키거나 운영에 영향을 줄 위험이 있어 사용하지 않았다.
- `case_1048` Kafka 토픽 복제: 타 부서 시스템에 중복 호출 부하를 주거나 예상치 못한 부작용을 일으킬 위험이 있어 채택하지 않았다.
- `case_1050` storm-kafka-client 1.1.0 다운그레이드: 멀티 토폴로지를 구성했을 때 장애 테스트에서 중단 시간이 약 6분으로 길어 합리적인 선택이 아니라고 판단했다.
- `case_1050` range assignor: supervisor 중단 시 전체 파티션의 소유권이 변경되어 sticky assignor보다 과도한 중복 처리가 발생했다.
- `case_1053` 단일 범용 적대적 왜곡(UAP): 입력 이미지의 특성과 무관한 단일 왜곡에 의존해 이미지별·작품별 다양성을 반영하지 못하고 기존 이미지별 최적화 방식보다 학습 방지 성능이 저하됐다.
- `case_1054` LangGraph: 간단한 예제를 작성했을 때 AutoGen과 MetaGPT보다 복잡하게 느껴졌다.
- `case_1054` MetaGPT: 역할 기반 책임보다 도구 기반 책임이 더 직관적이라고 판단해 AutoGen을 최종 선택했다.
- `case_1055` @tanstack/react-virtual: 로그 표현 방식이 다양하고 복잡해 오픈소스로 대응하기 어렵고, 스크롤 바닥 감지 실패 원인 분석과 커스텀 기능 구현에도 부담이 있다고 판단했다.
- `case_1056` 응답 객체 파라미터 전달: 호출 깊이가 깊거나 전략 패턴을 사용하는 경우 중간 계층과 불필요한 구현체까지 Profile 파라미터를 받아야 하고, 새로운 데이터가 필요할 때 모든 메서드 시그니처를 수정해야 한다.
- `case_1056` Redis/Local 캐시와 TTL 설정: 요청 처리 시간에 맞는 TTL을 설정하기 어렵고, TTL이 짧으면 요청 중 캐시가 만료되며 TTL이 길면 서로 다른 요청 간에 캐시가 공유된다.
- `case_1056` @RequestScope CacheManager: Spring Actuator의 CacheMetricsAutoConfiguration이 애플리케이션 시작 시 요청 범위를 resolve하려 해 ScopeNotActiveException이 발생한다.
- `case_1056` CacheMetricsAutoConfiguration 제외: 기술적으로 동작하지만 캐시 적중·미스와 같은 중요한 메트릭을 수집할 수 없다.
- `case_1056` ThreadLocal 캐시: ThreadLocal에 저장된 캐시는 자동으로 정리되지 않아 각 실행 생명주기마다 수동 정리가 필요하다.
- `case_1058` Flink 애플리케이션 모드: 복제 job마다 별도의 클러스터가 필요해 전체 배포 시간이 더 소요될 수 있어 세션 모드를 선택했다.
- `case_1059` 동기 검증: 동기 검증은 높은 병렬도가 필요했기 때문에 검증 순서가 중요하지 않다는 판단에 따라 비동기 검증으로 변경했다.
- `case_1061` Redis: Redis 클러스터는 안정성을 이유로 scale-out 상한이 존재해 이론상 무한대로 scale-out 가능한 인하우스 분산 DB를 사용하기로 했다.
- `case_1061` cProfile: 메인 스레드만 프로파일링하므로 멀티 스레드 환경에서 사용하려면 모든 스레드를 직접 프로파일링하고 결과를 합쳐야 한다.
- `case_1061` line_profiler: 프로파일링하려는 곳마다 @profile 코드를 삽입해야 하는 불편함이 있다.
- `case_1061` py-spy: 샘플링 기반 프로파일러라 결정론적 프로파일링을 지원하지 않아 서비스 환경에서 사용하지 않기로 했다.
- `case_1062` Spark 단독 사용: Spark만 사용하는 방법도 가능했지만 리소스 효율성과 빠르고 안정적인 파이프라인을 위해 Flink와 Paimon을 도입했다.
- `case_1062` Iceberg: 실시간 변경 로그가 필수인 아키텍처에서 Iceberg의 변경 로그 제약 때문에 Paimon을 채택했다.
- `case_1064` VARCHAR CAST로 바인딩 길이 고정: Oracle 드라이버 내부에서 바인딩 길이를 다시 계산해 VARCHAR 바인딩 타입이 고정되지 않았다.
- `case_1064` parent cursor 분리용 코멘트: child cursor 경쟁은 완화했지만 child cursor의 신규 생성을 해결하지 못했고 라이브러리 캐시 메모리 점유와 eviction 빈도를 증가시켰다.
- `case_1064` 세션 VARCHAR 바인딩 크기 4000 고정: 불필요하게 큰 VARCHAR 타입 사용으로 정상 상황에서 성능이 저하될 수 있고 동일 연결 풀의 모든 요청에 영향을 줄 수 있었다.
- `case_1064` UPDATE 쿼리 분리: child cursor 개수는 줄었지만 한 번에 처리할 쿼리를 나누는 방식이 DBA 권장 사항이 아니어서 최종 적용하지 않았다.
- `case_1069` SeqKLD: Label을 학습했지만 기대만큼의 성능이 나오지 않았다.
- `case_1069` 화이트박스 지식 증류: Label LM Loss와 Logit 정보를 함께 활용했지만 성능 향상 폭이 크지 않았다.
- `case_1069` MoE with LoRA: 가장 좋은 성능을 보였지만 서비스에서 개별 task 간 성능 간섭을 피하기 위해 적용하지 않았다.
- `case_1077` 모든 검색어를 seed로 사용: 날씨 등 일상 정보성 키워드는 추천 문서 품질이 낮았다.
- `case_1078` 리니어 랭커: DCN Stacked 구조보다 주요 지표가 낮았다.
- `case_1078` DCN 기반 multi-head 구조: MDE 개발 과정의 비교 실험에서 최종 모델로 채택되지 않았다.
- `case_1078` MMoE shared bottom 기반 모델: MDE 개발 과정의 비교 실험에서 최종 모델로 채택되지 않았다.
- `case_1079` 휴리스틱 규칙 기반 Rank1 선정: 사용자의 특성을 모두 반영하는 데 한계가 있었다.
- `case_1083` Elasticsearch ← Elastic Search: 네이버 자체 검색 엔진 Nexus로 전환했다.
- `case_1084` Kafka Connect: 동기화 대상 테이블이 수십만 개일 때 테이블 수가 수백 개 수준에 도달해도 OOM이 발생했다.
- `case_1084` Apache Flink ← Flink: 단일 테이블만 지원하고 테이블 fan-out 기능이 없어 테이블별 애플리케이션 운영이 필요했다.
- `case_1084` 쿼리 엔진 기반 데이터 최적화: 요구하는 테이블 규모를 지원하려면 비용 부담이 커지고 세부적인 스케줄링 및 스로틀링 설정이 어려웠다.
- `case_1084` Hive metastore: Hive lock 버그로 경합이 심할 때 데드락이 발생했다.
- `case_1084` Polaris: 특정 카탈로그에 제한될 우려가 있었다.
- `case_1086` Exact Match: 오탈자나 주소·전화번호 누락이 있으면 정확한 매칭이 어려워 Dense Retrieval 기반 모델로 대체했다.
- `case_1089` Argo Workflow: 이미 구현된 오픈소스 워크플로를 활용하는 대신 커스텀 컨트롤러로 직접 워크플로를 구현했다.
- `case_1089` Apache Airflow: 이미 구현된 오픈소스 워크플로를 활용하는 대신 커스텀 컨트롤러로 직접 워크플로를 구현했다.
- `case_1095` 검색 로그 기반 지도 학습 미세 조정: 검색 로그로 수집한 데이터가 사용자의 빈번한 검색 패턴에 편향되어 문서의 핵심과 무관한 패턴을 출력했습니다.
- `case_1095` HCX-L 기반 적은 예시 데이터 증강: 프롬프트에 다양한 제약 조건을 명시하고 강제하기 어려워 결과 품질 관리가 어려웠습니다.
- `case_1095` Hugging Face: 온라인 추론을 신속하게 처리하기 어려워 서빙 전용 프레임워크인 vLLM을 도입했습니다.
- `case_1096` 목록 단위 랭킹 + 개별 단위 스코어링: 목록 단위 랭킹과 개별 단위 스코어링을 결합하는 방식보다 목록 단위에서 랭킹과 스코어링을 함께 생성하는 방식의 랭킹·스코어링 성능이 모두 우수해 채택하지 않았다.
- `case_1096` 근거 생성 프롬프트: 근거를 생성하면 2배 이상의 시간과 계산 비용이 들고, 랭킹 성능에서는 근거를 생성하지 않는 방식보다 낮아 근거 없는 프롬프트를 채택했다.
- `case_1097` 텀 매칭 기반 리트리빙: 단어 중복에 의존해 중의성 문제로 전혀 관련 없는 문서가 노출될 수 있어 임베딩 기반 리트리빙을 채택했다.
- `case_1097` ANN 1차 검색 후 최신 문서 선별: ANN은 관련도만 기준으로 검색해 최신 문서를 원하는 만큼 확보하기 어려워 최신 문서 선검색 후 유사도 필터링·재순위화 방식을 채택했다.
- `case_1098` 코멘트 수 제한: 코멘트 수를 제한하면 코드 리뷰에서 활발한 의견 교환을 방해하고 코드 리뷰 문화에 부정적인 영향을 줄 수 있다고 판단해 시도하지 않았다.
- `case_1100` 클라이언트 폴링: 각 클라이언트가 주기적으로 조회 요청을 보내 구매자 수에 비례하는 통신 부하가 발생하고, 통신 자원만을 위해 대기열 서버를 확장하면 자원 비효율 문제가 생긴다.
- `case_1100` 정렬된 대기표 목록: 정렬된 목록 변경 비용이 대기 중인 구매자 수에 비례해 증가하고, 분산 저장소에서도 여러 노드 간 정렬 상태 유지 비용이 커진다.
- `case_1100` 특정 서버에 대기열 처리 고정: 컨테이너가 종료되거나 새로 실행될 수 있는 환경에 적합하지 않다.
- `case_1100` 총 서버 대수 기반 대기열 분배: 컨테이너 환경에서는 서버 수가 변할 수 있어 작업 할당에 적합하지 않다.
- `case_1101` 사용자 피드백 데이터셋: 탐색형 질의에서 발생하는 피드백 데이터만으로는 복잡한 질의의 연관성을 위한 양질의 정답 데이터셋을 구축하기 어려웠다.
- `case_1101` 양방향 인코더 모델: 세부적인 맥락을 포착하기 어려워 성능이 충분하지 않았다.
- `case_1101` 소형 생성형 모델: 복잡한 맥락에 대한 적절한 랭킹 결과를 생성하는 데 한계가 있었다.
- `case_1102` 템플릿 기반 UI: 새로운 요구 사항마다 템플릿을 수정하거나 새로 생성해야 해 유연성이 부족했다.
- `case_1102` 컴포넌트 기반 UI: 과도하게 세분화된 컴포넌트 구조로 데이터 전송량과 서버·클라이언트 통신 복잡성이 증가했다.
- `case_1103` 디자인 시스템 선 구축: 디자인 시스템 구축 경험이 부족해 시스템을 먼저 완성한 후 서비스에 적용하는 방식은 비현실적이었다.
- `case_1104` 에디터 기반 Design to Code: 개발 비용과 유지 보수 비용이 매우 클 것으로 판단했다.
- `case_1104` 웹훅 기반 변경 알림: UI가 실제로 바뀌지 않아도 1분마다 알림이 오고 변경 사항을 확인할 수 없었다.
- `case_1105` vLLM: 모델 아키텍처상 지원되지 않는 부분이 있어 제외했다.
- `case_1105` TorchServe: 커스텀 모델 사용과 추론 코드 수정에는 용이했지만 원하는 성능이 나오지 않아 제외했다.
- `case_1105` TEI: 라이선스 문제와 커스터마이징 장벽, 자체 양자화에 따른 성능 차이 및 상대적으로 낮은 성능 때문에 사용하지 않았다.
- `case_1105` 동적 배치: 서버 초기화 후 요청마다 배치 크기가 달라져 초기 성능이 저하될 수 있어 사용하지 않았다.
- `case_1106` 비동기 XHR·Fetch와 지연 후 페이지 전환: 페이지 전환을 지연해도 로그 전송이 지연 시간보다 오래 걸리거나 다른 링크를 클릭해 즉시 전환하면 로그가 유실될 수 있다.
- `case_1106` 동기 XHR: 로그 전송이 완료될 때까지 페이지 전환이 지연되어 사용자 경험을 해칠 수 있다.
- `case_1106` Redirect Bounce: 일부 브라우저 버전에서 301 또는 302 리디렉션 시 원래 페이지가 방문 기록에 저장되지 않아 :visited CSS 의사 클래스를 지원하지 못할 수 있다.
- `case_1107` Agenta: 검토 당시 필요한 기능이 포함되어 있지 않아 직접 개발하기로 결정했습니다.
- `case_1107` PromptTools: 검토 당시 필요한 기능이 포함되어 있지 않아 직접 개발하기로 결정했습니다.
- `case_1112` 조건문 기반 매핑: 모든 매핑 케이스를 빠짐없이 작성하지 않으면 예기치 않은 매핑 결과가 발생할 수 있어 그래프 구조를 선택했다.
- `case_1112` 프록시 기반 로드 밸런싱: 반드시 프록시를 거쳐야 하므로 성능 손실이 있을 수 있어 클라이언트 단 로드 밸런싱을 구성했다.
- `case_1115` Lighthouse: 특정 물리적 환경에서 측정하는 실험실 데이터라 실제 네이버 통합 검색 페이지의 다양한 사용자 환경과 페이지 구성을 대변하지 못하므로 사용하지 않았다.
- `case_1116` 하위 레이어 code 반환: 실제 API 응답에 사용하는 code를 DB 레이어에서 생성하면 비즈니스 로직이 DB 레이어에 침투할 가능성이 있어 제거했다.
- `case_1117` github.com/pkg/errors: errors.Wrap()을 무작정 사용하면 호출 스택이 재귀적으로 쌓이고, Wrap과 WithMessage를 구분해 사용하려면 라이브러리 동작을 미리 이해해야 하므로 최종 방식으로 채택하지 않았다.
- `case_1117` Wrap 1회·WithMessage 규칙: 최하위 함수에서만 Wrap()을 사용하고 상위 함수에서는 WithMessage()를 사용하도록 하는 규칙은 하위 함수까지 내려가 Wrap 여부를 확인해야 하고, 추가 메시지가 없어도 빈 문자열을 넣어야 하므로 직관적이지 않다고 판단했다.
- `case_1118` nil 반환·nil error: 상위 함수에서 document가 nil인지 별도로 확인해야 하고, MongoDB Go Driver가 문서 없음도 error로 정의하므로 채택하지 않았다.
- `case_1118` reflect 기반 Cursor 디코딩: interface{} 반환 후 caller에서 type assertion이 필요하고 사용이 불편해 제네릭 방식으로 대체했다.
- `case_1118` errors.As(): 오류를 확인할 때마다 target error 변수를 선언해 넘겨야 하는 불편함이 있어 type switch 방식을 선택했다.
- `case_1118` reflect 기반 error 판별: error struct를 public으로 공개해야 하고 확인할 struct 객체도 생성해야 하므로 채택하지 않았다.
- `case_1120` onLoad 이벤트 이후 JavaScript 로딩: JavaScript를 늦게 로딩할수록 LCP가 악화되고, 이미지나 CSS 등 특정 리소스 문제로 onLoad 이벤트가 지연되면 검색에 필요한 JavaScript도 로딩되지 않을 수 있어 DCL 기준으로 변경했다.
- `case_1122` 행동 구간 검출: 전체 영상이 모델에 입력되므로 영상이 매우 길면 잘 동작하지 않고, 학습한 도메인에만 동작하는 한계가 있었다.
- `case_1122` 영상 요약: 지도 학습 방식은 주관적인 기준이 개입되고, 비지도 학습 방식은 시각적으로 가장 이질적인 구간 위주로 검출해 쇼핑라이브에 바로 적용하기 어려웠다.
- `case_1122` 텍스트 기반 장면 탐색: 정적인 묘사에 집중해 행동을 잘 검출하지 못하고 2~3분 길이의 짧은 영상을 대상으로 한다는 문제가 있었다.
- `case_1124` SingleNode: 수천만 개 이상의 시계열 데이터를 단일 장비로 감당하기 어렵고 단일 장비가 SPOF가 될 수 있어 채택하지 않았다.
- `case_1127` HDFS 쓰기 파이프라인: WAL 쓰기에서 DataNode 간 파이프라인 복구가 실패하면 오류 DataNode를 잘못 식별해 복구가 반복 실패하고 사용자 요청 처리가 지연되었다.
- `case_1130` start-offset earliest 설정 후 중복 허용: 멱등성이 보장되지 않는 기존 컨슈머가 많아 부적합했다.
- `case_1130` 메시지 발행 중단 후 일괄 전환: 많은 컨슈머에서 동시에 작업해야 하고 실시간 처리가 중요한 컨슈머의 중단 시간이 길어질 수 있어 부적합했다.
- `case_1131` Alluxio: 일부 POSIX API를 지원하지 않고 원본 저장소와의 동기화 문제가 있으며, master·worker 클러스터 운영 부담이 있다.
- `case_1131` GlusterFS·CephFS: 직접 운영하는 부담이 크다고 판단했다.
- `case_1131` Ceph-rbd: ReadWriteMany와 ReadOnlyMany를 지원하지 않아 여러 Pod의 동시 접근이 불가능하다.
- `case_1131` NFS: 간단하게 구성할 수 있지만 확장성과 HA 문제가 있다.
- `case_1131` local-path: 노드 간 동시 접근이 불가능하고 데이터 위치에 따른 별도 스케줄링 또는 앱 레벨 구현이 필요하다.
- `case_1131` AWS EFS·Google Filestore: Object Storage보다 큰 비용이 발생하고 네이버 사내 환경에서 외부 클라우드 스토리지를 사용할 수 없다.
- `case_1132` SGD: 두 행렬의 내적에 따른 non-convex 문제로 학습 속도가 떨어져 ALS를 선택했다.
- `case_1132` Spark ALS: 결과 값이 나오지 않았고 GC로 작업에 11시간이 소요된 반면, GPU 모델은 5분 안에 학습이 완료됐다.
- `case_1133` Deequ: Great Expectations보다 문서화·커뮤니티, 데이터 품질 규칙, 다양한 도구와의 integration 측면에서 선택 기준에 덜 부합했다.
- `case_1135` AbortController: fetch에는 사용할 수 있지만 fetch가 아닌 일반적인 프로미스 상황의 중단에는 원하는 방식이 아니었다.
- `case_1135` CancellationToken: 작업 함수에서 취소 토큰을 주기적으로 확인해야 하고 중간 단계에서 멈추기 어렵다고 판단했다.
- `case_1135` CSS :not()·:is() 선택자: JavaScript에서 요소를 선택하기 어렵고 복잡한 상황이나 브라우저 호환성이 필요한 경우 사용하기 어려웠다.
- `case_1135` TreeWalker: DOM 트리를 순회할 수 있지만 코드가 다소 복잡하고 이해하기 어려웠다.
- `case_1135` MutationObserver: 동적 DOM 처리에는 유용하지만 불필요한 오버헤드와 코드 복잡성이 발생할 수 있었다.
- `case_1136` Elasticsearch 8.x 업그레이드: 사내 검색 플랫폼이 Elasticsearch 7.10.2까지만 지원하고 이후 버전 업그레이드 없이 일몰 방향으로 가고 있어 선택하지 않았다.
- `case_1137` Kafka 파티션 증가: 동시 처리량은 늘릴 수 있지만 파일 오픈 비용·디스크 사용량·장애 영향 범위·복제 비용이 증가할 수 있다.
- `case_1138` initializer 기반 @Recv: 프레임워크가 receiver 클래스의 인스턴스를 직접 관리하도록 변경하면서 initializer 호출을 제거하고 메서드명을 메타데이터에 저장하는 방식을 최종 채택했다.
- `case_1140` 단일 프롬프트: 전체 리포트를 한 번에 생성하는 방식에서 수치 오류, 중요 항목 누락, 불안정한 포맷, 얕은 해석 문제가 발생했다.
- `case_1141` 고정된 DAG: 분석 경로를 미리 정의해 매일 같은 경로로 실행하는 방식은 데이터에 따라 달라지는 원인 분석을 유연하게 처리하기 어려웠다.
- `case_1142` 오픈소스 플러그인: 사용자 컨텍스트와 권한 전파, 시스템 프롬프트 제어, 도구 호출 라운드, 데이터소스별 라벨 처리와 운영·라이선스 요구를 원하는 수준으로 통제하기 어려웠습니다.
- `case_1143` Alertmanager grouping: 정적인 라벨 일치에 의존해 의존 관계나 증상의 의미적 유사성으로 Alert를 묶기 어려웠다.
- `case_1143` 상용 AIOps: 운영 환경에 맞게 동작을 통제할 수 있는 제어권을 원하는 수준으로 확보하기 어려웠다.
- `case_1147` 완전 자율형 에이전트: 보안 업무에서 부정확한 답변이 잘못된 판단의 근거가 될 수 있고, 실제 복잡한 업무에서는 사람의 개입이 다시 필요했다.
- `case_1148` 단순 키워드 기반 라우팅: 표면 증상 뒤에 단말 보안 솔루션 상태, MDM 등록 상태, 계정 상태 같은 실제 원인이 숨어 있을 수 있다.
- `case_1149` 범용 챗봇: 하나의 AI 에이전트에 모든 질문을 맡기면 업무 책임과 근거 우선순위가 흐려질 수 있다.
- `case_1152` 단일 키 방식: 키 노출 시 전체 보안이 무너질 위험이 있어 DEK-KEK 이중 키 구조를 채택했다.
- `case_1152` 컨슈머별 고유 키: 컨슈머 수에 따라 메시지 헤더의 메타데이터가 누적되어 메시지 크기가 증가하므로 공유 KEK를 채택했다.
- `case_1153` Google Cloud Knowledge MCP: 개발자별 Google Cloud API 인증과 인증 프록시의 할당량 대응 로직을 운영해야 했다.
- `case_1154` 텍스트 검색 기반 심볼 검색: 이름 문자열만 비교해 동명 심볼을 구분하지 못하고 무관한 매치를 포함한다.
- `case_1156` 단일 프롬프트: 한 번은 작동할 수 있지만 누적 효과로 이어지지 않으므로 반복 가능한 워크플로를 사용한다.
- `case_1156` 모든 작업을 하나의 큰 워크플로로 자동화: 통제가 어렵고 문제가 발생한 단계를 파악하기 어려우므로 큰 워크플로를 피한다.
- `case_1157` AI 보조 방식: 기존 프로세스에 AI를 추가하면 개별 단계는 빨라지지만 의도·구현·검증·리뷰·전달 사이의 조율 계층이 남는다.
- `case_1157` 단일 AI 체커: 단일 체커를 추가해도 또 다른 단일 시각의 리뷰가 될 수 있다.
- `case_1157` 단일 어시스턴트 프롬프트 방식: 하나의 어시스턴트에 일련의 프롬프트를 입력하는 방식 대신 전문화된 AI 역할 간 구조적 협업을 채택했다.
- `case_1161` Athenz 모킹: Athenz의 인증 모델을 충실하게 모킹하려면 상당한 로직을 다시 구현해야 하므로 실제 Athenz를 로컬에서 실행했다.
- `case_1166` ID 토큰 직접 교환: 로그인 토큰을 리소스 접근을 위한 인가 그랜트로 암묵적으로 취급하게 되어 인증과 크로스 도메인 인가 권한이 혼동될 수 있다.
- `case_1167` 타사 후속 솔루션: 기술 내재화와 운영 프로세스 맞춤 대응을 위해 자체 기술로 전환했다.
- `case_1167` 고객 입력 미리보기: 사용자가 전송하지 않은 내용을 상담원이 열람하는 보안 취약점이 있어 제외했다.
- `case_1167` 지원 플래그: 상담원이 매니저에게 지원 요청을 보내는 대신 사무 공간에서 직접 문의할 수 있어 불필요했다.
- `case_1167` 연결 끊김 음성 경고음: 사무실에서는 소리를 켤 수 없어 실제 운영에서 사용할 수 없었다.
- `case_1171` 라우터 확충: CallQueue 정체는 일부 분산됐지만 기대만큼 큰 효과를 얻지 못했다.
- `case_1172` 기존 구 Yahoo Japan 구조 유지: 구 LINE의 권한 관리 시스템에 맞출 수 있지만 HDFS Path 기반 관리와 테이블 기반 관리가 공존해 장기적으로 운영 규칙과 사용자 경험이 복잡해질 우려가 있었다.
- `case_1174` PR 내용 AI 분석 후 개요 기반 리뷰: 변경 내용 파악은 쉬워졌지만 코드베이스의 영향 범위 조사와 잠재적 문제 발견에는 큰 도움이 되지 않았고, 매번 프롬프트를 붙여 넣어야 해 약 2주 만에 사용하지 않게 되었다.
- `case_1177` AI 단순 생산성 도구: 문서 요약이나 테스트 케이스 초안 생성만으로는 QA 업무 방식 자체를 바꾸기 어렵다고 판단했다.
- `case_1182` 네이티브 앱 SDK: 채팅 클라이언트를 네이티브 앱 SDK가 아니라 웹으로 제공했다.
- `case_1187` Spark Streaming: 마이크로 배치 방식이라 이벤트 시간 기준의 상태를 세밀하게 제어하기 어렵고 데이터 최신성 판별과 정확히 한 번 처리를 동시에 만족하기 어렵다고 판단했다.
- `case_1187` 네이티브 쿠버네티스: 권한, 라우팅, 배포, 잡 실행 설정을 수동으로 구성해야 해 Flink Kubernetes Operator보다 설정 및 운영이 번거로웠다.
- `case_1188` Spark 온힙 메모리 증설: 익스큐터 코어 수를 줄이고 Spark 온힙 메모리를 늘렸지만 메모리 압박이 계속됐다.
- `case_1189` YARN: YARN 환경의 구조적 한계 때문에 다른 컴퓨팅 엔진 도입을 검토했다.
- `case_1191` 슬래시 명령어: 사용자가 형식에 맞는 텍스트를 직접 입력해야 하고 필수 항목 누락이나 형식 오류가 발생할 수 있어 Slack 워크플로를 선택했다.
- `case_1191` 동기 처리: 여러 외부 API를 순차적으로 호출하면 Slack의 응답 제한을 초과할 수 있어 비동기 처리를 선택했다.
- `case_1191` 봇 메모리 저장: 봇 재시작 시 매핑 정보가 사라지므로 Redis를 선택했다.
- `case_1194` 기존 통계 스트림에 검증 로직 직접 결합: 기존 스트림에 부하 및 지연이 발생할 수 있어 별도 검증 프로세스를 유지했다.
- `case_1198` 파인 튜닝: 지식 주입 정확도가 낮고, 양질의 학습 데이터 구성과 문서 변경에 따른 동기화 유지 보수 비용이 크다.
- `case_1199` 청킹: 문서를 기계적으로 자르면 전후 문맥이 손실되고, 청크 간 겹침이나 문맥 첨부 같은 보완이 필요하다.
- `case_1200` 계획 후 실행: 계획 수립과 재계획 로직으로 시스템 복잡도는 크게 늘었지만 답변 품질 개선은 체감하기 어려웠다.
- `case_1200` 멀티 에이전트: 전문가 에이전트 위임으로 응답 시간이 약 50% 증가했고, 크로스 도메인 질문에서 정보가 누락됐다.
- `case_1201` 장비 업그레이드: 비용이 문제였고 현재 서버 성능도 양호해 채택하지 않았다.
- `case_1201` 캐싱: 데이터 일관성을 유지하기 어려워 채택하지 않았다.
- `case_1201` 파티셔닝 세분화: 근본적인 해결책이 되지 못해 채택하지 않았다.
- `case_1205` 번역 파이프라인: 번역 품질이 흔들리면 검색 결과가 흔들리고 번역으로 지연 시간이 늘어났다.
- `case_1205` 다국어 모델 처음부터 학습: 다국어 지원 이미지-텍스트 임베딩 모델을 처음부터 학습하는 방식은 데이터와 연산 비용이 너무 컸다.
- `case_1205` CoreML: iOS에서만 작동하고 모델 변환 호환성 문제와 크로스 플랫폼 유지 보수 부담이 있어 제외했다.
- `case_1205` FAISS 계열 모바일 포팅: iOS 중심의 모바일 포팅이었다.
- `case_1205` USearch: Android 빌드와 배포가 간단하지 않았다.
- `case_1205` sqlite-vec: 검색 성능과 운영에 대한 검증이 충분하지 않았다.
- `case_1208` BLIP-2·MobileVLM·PaliGemma·MiniCPM 계열: 모델 크기와 추론 지연 측면에서 모바일 환경에 현실적이지 않았습니다.
- `case_1208` Google GenAI Image Description: 정의한 모바일 사용 시나리오에 적합하지 않아 제외했습니다.
- `case_1208` 자기회귀 디코딩: 모델을 단순 경량화하는 것만으로는 모바일의 지연 목표를 맞출 수 없어 디코딩 방식을 변경했습니다.
- `case_1210` MySQL 샤딩: 급한 불은 껐지만 쓰기 부하와 대용량 읽기 성능 문제를 근본적으로 해결하지 못했다.
- `case_1210` OpenTSDB: 태그 활용, 문자 표현, 대용량 쿼리 효율성에 한계가 있었다.
- `case_1211` 모든 데이터를 Cassandra에 저장: Cassandra 의존도를 낮추고 저장 비용과 확장 문제를 개선하기 위해 채택하지 않았다.
- `case_1211` S3 호환 저장소로 완전 이관: S3 호환 저장소가 Cassandra의 성능을 완전히 대체하기에는 아직 이르다고 판단했다.
- `case_1212` 직접 I/O: 과도한 대역폭 점유로 다른 서비스에 영향을 줄 수 있어 적용을 철회했다.
- `case_1213` 시스템 프롬프트에 응답 가이드라인 추가: 응답 가이드라인이 시스템 프롬프트의 대원칙과 충돌해 문서 검색 없이 답변을 생성하는 문제가 발생했다.
- `case_1213` Minified JSON: YAML과 비교했을 때 토큰 수 차이가 생각보다 크지 않았고 YAML의 가독성이 더 높아 선택하지 않았다.
- `case_1215` 포크 PR 예외 처리: 포크 PR을 예외 처리하는 수준이 아니라 실행 흐름을 재설계하는 방향으로 접근했다.
- `case_1222` L7 로드 밸런서: Pushsphere가 요구하는 40만 QPS를 처리할 수 없어 해결책으로 사용할 수 없었다.
- `case_1233` Envoy 사이드카 프락시: 별도 프로세스 운영으로 구조가 복잡해지고 네트워크 홉과 실패 지점이 추가된다.
- `case_1234` DisposableException 포장: block에서 발생한 원래 예외를 DisposableException으로 대체해 호출자가 기대한 예외 유형을 잡지 못할 수 있다.
- `case_1234` dispose 예외 우선 처리: dispose는 보조적인 호출이므로 block에서 발생한 예외보다 dispose 예외를 최종 예외로 던지는 것은 오해의 소지가 있다.
- `case_1235` NADA: IETF RMCAT에서 표준으로 채택된 알고리즘이지만 LINE 통화에는 자체 개발한 CCFS를 사용했다.
- `case_1235` SCReAM: IETF RMCAT에서 표준으로 채택된 알고리즘이지만 LINE 통화에는 자체 개발한 CCFS를 사용했다.
- `case_1236` 사용자 네트워크 오류 로그 전송: 사용자의 일시적인 네트워크 상태 이상은 서비스 팀이 대응할 수 있는 앱이나 서버 결함이 아니므로 로그 전송 대상에서 제외했다.
- `case_1236` 단발성 네트워크 실패 알림: 사용자 재시도로 복구되는 오류는 알림이 발생해도 대응할 일이 없어 알림에서 제외했다.
- `case_1238` 블랙리스트 방식: 미리 지정하기 어려운 관련 키워드들이 필터링되지 않아 사용하지 않았다.
- `case_1238` 거리 기반 클러스터링: 중복 메시지가 일부 남거나 잘못 제거돼도 영향이 크지 않아 더 간단한 방식을 택했다.
- `case_1239` Ingress Nginx: 로드밸런서 프락시를 거치면 클라이언트의 실제 IP를 확인하기 어렵고 GeoIP 모듈 등 Nginx의 세부 기능을 활용하기 어려웠다.
- `case_1240` Loki Monolithic 모드: 주요 컴포넌트가 하나의 프로세스로 통합돼 수평 확장이 불가능하고, 트래픽 증가 시 병목이 전체 시스템에 영향을 줄 수 있었다.
- `case_1240` Loki Microservices 모드: 컴포넌트를 완전히 분리해 유연하지만 운영 복잡도가 증가한다.
- `case_1242` 프로모션 도메인 포함: 프로젝트 초기에는 프로모션 도메인을 포함했지만, 담당 범위를 논의한 끝에 최종 도메인에서 제외했다.
- `case_1243` gRPC 프로토콜: CPU 오버헤드가 발생했고 Vitess 측에서 MySQL 프로토콜 사용을 권장했다.
- `case_1243` 관리 방식 DDL: 온라인 DDL을 지원하지 않는 쿼리 수행 시 샤드별 순단과 애플리케이션 오류가 발생했다.
- `case_1244` Apache ShardingSphere: 리밸런싱을 직접 구현해야 하고 추가 개발 포인트가 많아 PoC 대상에서 제외했다.
- `case_1244` TiDB: 개발자와 DBA의 운용 비용을 줄여주지만 기본 장비 비용이 기존보다 최소 3배 이상 필요했다.
- `case_1246` GitHub Copilot 익스텐션: 당시 공개 프리뷰 버전이어서 프로토타입에 적용하지 못했다.
- `case_1246` VS Code 익스텐션: 특정 IDE에 의존하는 대신 MCP로 변경했다.
- `case_1247` SMS 인증: SMS를 수신할 수 있는 번호를 쿠폰 금액보다 저렴하게 구매할 수 있어 어뷰징이 빈번하게 발생했다.
- `case_1250` Qdrant: Milvus가 성능과 안정성, 인덱스 다양성, 스트림·배치 지원 측면에서 더 적합하다고 판단했다.
- `case_1261` 그리드 탐색: 좋은 이미지를 판단할 수 있지만 탐색 비용이 너무 많이 들어 선택하지 않았다.
- `case_1261` 잠재 벡터 직접 갱신: 그래픽 카드 여건상 잠재 벡터를 직접 갱신하기 어려워 손실 측정에 집중했다.
- `case_1261` 이미지 스타일 유사도 측정: 이미지 스타일 유사도를 평가할 만한 방법을 찾지 못해 네 가지 지표만 사용했다.
- `case_1263` 처리량 SLI: 미디어 유형과 크기가 다양해 서비스별 성능 편차가 크고 일관된 기준을 적용하기 어려워 SLI에서는 제외하고 참고 메트릭으로만 활용했다.
- `case_1263` 엔드포인트 메트릭 수집: OBS 특성상 서비스에서 SLI/SLO 관련 메트릭을 수집하기 어려워 로그에서 메트릭을 생성하는 방식을 선택했다.
- `case_1265` 열거형 name 직접 변환: 열거형 이름을 변경하면 외부에서 사용 중인 값이 깨진다.
- `case_1265` 열거형 ordinal 직접 변환: 열거형을 중간에 추가하면 기존 항목의 ordinal 값이 변경되어 외부 값도 업데이트해야 한다.
- `case_1266` 리뷰 작성 완료 화면: 리뷰 작성률이 낮아 광고 지면으로 선택하지 않았다.
- `case_1266` 주문 완료 메일: 메일을 확인하는 비중이 적어 광고 지면으로 선택하지 않았다.
- `case_1266` 다른 가맹점 추천: 주문 직후 다른 음식을 추가로 주문하는 경우가 거의 없어 광고로 교체했다.
- `case_1267` 사용자 타겟팅 미적용: 의미 없는 클릭만 발생하고 광고 상품 구매로 이어지지 않아 사용자 정보를 활용한 타겟팅 광고로 전환했다.
- `case_1267` 인앱 브라우저: 광고주 사이트에서 이탈할 수 있고 익숙한 외부 브라우저의 기능을 활용하기 어려워 외부 브라우저로 변경했다.
- `case_1268` Flowise: Typescript 기반이라 Langflow와 비교해 호환성이 떨어져 선택하지 않았다.
- `case_1270` 사용 가능한 CPU 리소스에 맞춘 CPU 상한 설정: 실제 사용 가능한 CPU 리소스를 계산하기 어렵다고 판단했다.
- `case_1271` CPU 상한 설정 제거: 멀티 테넌시 환경에서 일관성을 유지하기 위해 CPU 상한 설정을 유지하기로 결정했다.
- `case_1276` Gradle --no-scan: Develocity로 빌드 정보를 보내지 않도록 설정했지만 문제가 해결되지 않았다.
- `case_1276` CI 슬레이브 메모리 할당량 증대: OOM 증거를 찾지 못했고, 익스큐터 수와 힙 메모리를 조정해도 문제가 해결되지 않았다.
- `case_1276` 로그 수집 성능 증대: 로그 수집 성능을 높이는 방법은 인프라 비용 때문에 선택하지 않고 로그양을 줄이는 방법을 적용했다.
- `case_1277` Cloudera: 라이선스 비용 증가로 오픈소스 전환과 기술 내재화를 검토했다.
- `case_1279` venv: 빠른 가상 환경 기능은 제공하지만 의존성 문제와 프로젝트 구조 관리 기능을 제공하지 않습니다.
- `case_1279` conda: 패키지 간 의존성 문제는 해결하지만 프로젝트 구조 관리 기능을 지원하지 않습니다.
- `case_1282` Selenium: 초기 설정과 구성이 복잡하고 테스트 실행 속도가 느릴 수 있었다.
- `case_1282` Puppeteer: Chrome과 Chromium 기반 브라우저 외 다른 브라우저를 지원하지 않았다.
- `case_1282` Test Cafe: 커뮤니티 지원과 참고 자료가 부족하고 비동기 코드 처리가 복잡했다.
- `case_1282` Cypress: 오픈소스가 아니어서 모든 기능을 사용하려면 비용을 지불해야 했다.
- `case_1282` Datadog: 테스트 빈도와 복잡성에 따라 비용이 발생했다.
- `case_1284` 새로운 스펙과 디자인 동시 적용: 운영 조직의 혼란을 줄이고 QA 작업을 단순화하기 위해 기존 앱의 UI와 동작을 유지했다.
- `case_1288` Kotlin Multiplatform Mobile: iOS 디버깅 경험이 생산성과 안정성을 낮춰 Flutter로 다시 전환했다.
- `case_1289` 팩스 SaaS 서비스: 효율적이지 않거나 요구 조건에 맞지 않아 전환하지 못했다.
- `case_1292` WebAuthn Level 3: 아직 공식적으로 확정되지 않은 초안 상태이므로 WebAuthn Level 2를 채택했다.
- `case_1296` Kafka 파티셔닝: 대량의 데이터를 빠르게 처리할 수 있지만 동일 아이템의 변경 이벤트 순서를 보장하지 못했다.
- `case_1298` Python 클라이언트 직접 조회: 전체 파드 목록을 매번 조회하는 방식은 응답 속도가 느리고 kube-apiserver와 etcd에 과도한 부하를 발생시켰다.
- `case_1299` analyze_server: 커스텀 린트를 만들고 관리하는 엔지니어에게 친화적이지 않다.
- `case_1299` analyzer_plugin: 커스텀 린트를 만들고 관리하는 엔지니어에게 친화적이지 않다.
- `case_1300` Redis Cluster 캐시 사용: 캐시 히트율이 100%가 아닌 상황에서 다른 DB의 응답 속도가 늦으면 Redis Cluster를 메인 DB로 사용하는 방식보다 응답 시간이 불리했다.
- `case_1300` mget: 임베딩 유형이 추가될수록 키가 비례해서 증가하고 키를 기준으로 데이터를 한 번에 관리하기 불편했다.
- `case_1302` XML 추출: 특정 데이터가 XML에 포함되지 않을 수 있고, 추출 시간이 오래 걸리며, 일부 사이트만 선택하기 어렵고, 파싱이 불편했다.
- `case_1302` 직접 데이터 전송: 서비스마다 네트워크 환경이 달라 직접 데이터를 전송할 수 없었다.
- `case_1303` 사용자 의견 선반영: 디지털 리터러시가 낮은 사용자가 많고 기존 앱의 UI/UX가 최적화돼 있지 않다고 판단해 사용자 의견을 먼저 듣기보다 완성도 높은 버전을 먼저 출시하기로 했다.
- `case_1304` ITU-T P.835 주관적 평가: 주관적 평가는 비용과 시간이 많이 소요되고 평가자의 주관에 따라 결과에 오차가 발생할 수 있어 선택하지 않았다.
- `case_1305` Spring Cacheable sync=true: 캐시 미스 시 synchronized로 요청을 순차 처리해 sync=false보다 성능이 저하됐다.
- `case_1306` 생성형 모델: 논란의 소지가 있는 해시태그 출력 위험을 줄이기 위해 채택하지 않았다.
- `case_1306` 다중 클래스 분류: 복수 개의 해시태그를 허용하고 사용자가 실제로 복수의 해시태그를 활용하므로 채택하지 않았다.
- `case_1306` 지역별 별도 모델: 단일 다중 언어 모델과 성능 차이가 거의 없었다.
- `case_1307` 임베딩 유사도: 정성 평가에서 토큰 집합 유사도 방식이 문자열 중복을 더 확실하게 감소시키는 방식으로 평가됐다.
- `case_1310` 개별 프로젝트 구조: 프런트엔드와 백엔드를 분리할 수 있지만 프로젝트 간 코드 공유가 어렵다.
- `case_1310` 단일 프로젝트 구조: apps와 packages만으로 구성하는 구조보다 tooling 디렉터리를 추가한 구조를 최종적으로 채택했다.
- `case_1311` SemVer: SemVer는 API와 의존성 관리를 목적으로 하므로 최종 사용자가 사용하는 앱이나 웹 서비스의 버저닝에는 적합하지 않다고 판단했다.
- `case_1312` 양쪽 IDC에 쓰기 허용: 데이터베이스의 완벽한 이중화가 현실적으로 불가능해 데이터 정합성을 보장할 수 없고, 롤백 시 양쪽 데이터베이스의 정합성을 수동으로 맞춰야 했다.
- `case_1312` 신규 IDC에만 쓰기 허용: 이전 중 신규 IDC에만 새 데이터가 쌓여 데이터 정합성을 완전히 보장할 수 없고, 롤백 시 신규 데이터베이스의 변경 내용을 기존 IDC로 옮겨야 했다.
- `case_1314` 매 테스트마다 새 Kafka 토픽 생성: 테스트마다 토픽을 생성하고 삭제해야 해서 관리가 번거롭다.
- `case_1315` Go 언어 채널: 프로그램 종료나 장애 발생 시 메시지가 손실될 수 있고, 여러 인스턴스로 분산하거나 동적 버퍼링·처리 보장·모니터링을 제공하기 어렵다.
- `case_1315` Redis Lists: 데이터 처리에 실패하면 큐에서 데이터를 다시 가져와 재처리할 수 없어 메시지 유실 위험이 있다.
- `case_1315` Redis Pub-Sub: 메시지 수신을 보장하지 않고 구독자들에게 메시지를 일괄 발행하므로 중복 없는 동시 처리가 필요한 Retriever에 부적합하다.
- `case_1315` RabbitMQ: 중복 없는 동시 처리와 재처리는 가능하지만 사내 인프라 활용 및 인프라 유지 보수 위탁이 불가능했다.
- `case_1315` ActiveMQ: 중복 없는 동시 처리와 재처리는 가능하지만 사내 인프라 활용 및 인프라 유지 보수 위탁이 불가능했다.
- `case_1315` 주기별 Stream 생성: 시간이 지날수록 읽어야 할 Stream 목록이 변하고, 이전 Stream의 처리 완료 여부를 오차 없이 관리하기 어려웠다.
- `case_1315` 사전 N개 Stream 생성: Verda Redis의 해시 슬롯이 샤드에 무작위로 분배돼 특정 샤드에 일관되게 매핑되는 키를 생성하기 어려웠다.
- `case_1317` repair: 모든 노드가 동시에 데이터를 전송해 네트워크 사용량이 너무 높아 데이터 센터 복제에 사용할 수 없었다.
- `case_1317` Read Repair: 전체 키 조회를 신규 IDC 클러스터에 요청해야 하므로 실제 복제 작업에는 사용하지 않았다.
- `case_1317` Cassandra 버전 업그레이드: 버전 간 호환성 문제와 작업 기간 때문에 버전 업그레이드를 포기하고 2.0.17 버전을 유지했다.
- `case_1318` Swagger: 문서 가독성, 사용자 편의성, Redocly CLI의 문서 관리 기능을 고려해 Redoc을 선택했다.
- `case_1318` RapiDoc: 문서 가독성, 사용자 편의성, Redocly CLI의 문서 관리 기능을 고려해 Redoc을 선택했다.
- `case_1320` Apache HBase 직접 빌드: 도입 일정상 버그나 이슈 발생 시 빠르게 패치를 만들어 대응할 시간이 부족해 안정적인 서비스 제공이 어렵다고 판단했다.
- `case_1320` HBase REST API·Thrift API 별도 프로세스: 별도 프로세스가 중지되면 HBH가 정상 작동하지 않아 추가 관리가 필요하다.
- `case_1320` Central Dogma 기반 설정 관리: 설정 변경 후 리뷰·병합·배포와 프로세스 재시작 과정이 번거로워 HBH에서 설정 파일을 관리하는 방식으로 변경했다.
- `case_1321` 기존 코드 부분 수정: 영향 범위를 최소화하기 위해 기존 코드를 조금만 수정하는 방안을 고려했지만, 문제를 더 근본적으로 해결하기 위해 관련 코드를 처음부터 다시 작성했다.
- `case_1325` 1 Primary - 2 Replica 구조: Replica 노드 중 어느 노드를 Primary로 승격할지 결정하는 추가 과정이 필요하고 Replica 간 충돌 가능성까지 고려했다.
- `case_1328` JSON 문자열 역정규화: JSON 문자열로 저장한 필드 검색이 필요할 경우 테이블 구조를 다시 변경해야 할 수 있고, 성능 테스트에서 두 번째 안보다 읽기와 쓰기 성능이 모두 낮았다.
- `case_1329` 채번 테이블: 고려했지만 원하는 만큼의 성능이 나오지 않았다.
- `case_1330` 낙관적 락: 기존에 재고 차감 로직 등에 사용하던 분산 락 구현체를 이용해 빠르게 개발할 수 있다고 판단해 분산 락을 선택했다.
- `case_1333` 피드백 투표 점수: 점수 때문에 사용자 의견에 과도하게 얽매여 서비스 방향을 잃을 수 있고, 높은 점수의 의견이 처리되지 않을 때 좋은 인상을 주기 어렵다고 판단했다.
- `case_1333` Google Forms: 회사 보안 정책 때문에 사용할 수 없었다.
- `case_1335` Jekyll: 사이트를 쉽게 만들 수 있지만 기본적으로 블로그 형태이고 커스터마이징에 제한이 있다.
- `case_1335` Next.js: 웹 문서 개발보다 웹 사이트 개발에 적합하며 문서 기본 기능을 직접 구현하거나 플러그인으로 추가해야 한다.
- `case_1335` AsciiDoc·reStructuredText: 지원하는 SSG가 적고 팀원 모두가 새 문법을 익혀야 하며 Markdown보다 문법이 어렵다.
- `case_1335` OpenAPI Specification: 문서 작업용으로 사용하기에는 과하다고 판단해 자체 형식을 만들었다.
- `case_1340` Vector 공식 Helm 차트: 프로젝트와 무관한 리소스가 많아 공식 차트 대신 Helm 차트를 새로 생성했다.
- `case_1344` Google Fonts: LINE에서 라이선스를 획득한 폰트를 Google Fonts에서 제공받을 수 없고 다른 앱과 공유할 수도 없었습니다.
- `case_1345` 뷰별 XML 적용: 동적 적용 여부를 판단할 수 없고 각 서비스 담당자가 모든 텍스트 뷰에 일일이 적용해야 했습니다.
- `case_1345` 뷰별 프로그래매틱 적용: 동적으로 Typeface를 설정할 수 있지만 각 서비스 담당자가 뷰마다 직접 적용해야 했습니다.
- `case_1345` 텍스트 표시 커스텀 뷰: TextView뿐 아니라 Button, Toast, Header 등 다양한 뷰를 커스텀해야 하고 모든 뷰를 교체하는 데 큰 공수가 필요했습니다.
- `case_1346` 기존 UI 전체 전환: 이미 안정적으로 작동하는 기존 UI를 통째로 바꾸는 것은 적절하지 않다고 판단했다.
- `case_1346` Compose TextField 직접 사용: TextField에서 여러 문제가 보고되어 AndroidView로 기존 EditText를 사용하는 방식을 확인한 뒤 적용했다.
- `case_1347` 브라우저 지원 API: 브라우저마다 API 이름이 달랐고 Chrome에서 제공하는 API가 오디오 존재 여부를 정확하게 판단하지 못했다.
- `case_1347` Access-Control-Allow-Headers에 Range 추가: iOS 16.0 이상의 버전을 사용하는 사용자의 비율이 높아 추가 수정 없이 기능을 적용했다.
- `case_1348` Inverted Index: 색인 유지 자체가 부채가 되고 동의어 누락과 키워드 정확 매칭에 따른 무관 문서 참조가 발생했다.
- `case_1348` 본문 임베딩: 다주제 문서의 의미 평균화와 약어·식별자 검색 한계가 확인되어 summary 임베딩과 본문 FTS5로 분리했다.
- `case_1350` Linux: CLI 설계의 참고 대상으로는 Linux 기본 커맨드보다 Docker가 더 적합하다고 판단했다.
- `case_1355` Notion 수작업 정리: 업무 정보를 한 땀 한 땀 직접 정리하는 방식은 오래 유지되지 않았다.
- `case_1355` AI의 외부 시스템 직접 조회: 외부 시스템의 텍스트가 모두 토큰 비용으로 계산되어 비용과 속도가 악화됐다.
- `case_1359` generatePackageJson 비활성화: 배포 환경에서 별도 스크립트로 package.json을 생성해야 했다.
- `case_1359` 커스텀 webpack 플러그인: 메타데이터 주입을 위한 커스텀 플러그인의 유지보수 부담이 증가했다.
- `case_1360` Skills로 지식 관리: 지식 문서를 Skills로 구성하면 실행 시점에 동적으로 로드되어 토큰 소비를 예측하기 어렵고, 역할별로 필요한 지식을 명시적으로 제어하기 어렵기 때문에 ai-context와 분리했다.
- `case_1360` 헥사고날 아키텍처: 최초 AI Context 구성에는 더 유리할 것으로 생각했지만, 프로젝트 path 구조가 일관되고 위치를 잘 안내하면 AI 이해도에 차이가 없다고 정정했다.
- `case_1361` CommonJS 유지 후 번들러 옵션 보완: 사용 환경이나 빌드 도구에 따라 트리셰이킹 결과가 달라지고, 라이브러리 사용자가 구조보다 설정을 더 의식해야 할 수 있다고 판단했다.
- `case_1361` Rollup: 팀 내 빌드 환경 변경에 따른 영향 범위를 감안해 기존 도구를 유지하고 구조와 배포 방식을 우선 정리했다.
- `case_1362` Terraform: 배포와 확장에 이미 효율적인 프로세스와 대체재가 있어 제외했다.
- `case_1362` SaltStack: 오래된 대상 서버에 미니언 설치를 위한 변경 작업이 필요해 목표에 부합하지 않았다.
- `case_1363` 정적 인벤토리: hosts.ini에 호스트를 기록하는 방식은 서버 변경에 대응하기 어렵고 자동화하기 힘들어 동적 인벤토리로 전환했다.
- `case_1365` RAG SaaS: SaaS의 임베딩 모델 의존과 외부 연동 및 과금을 피하기 위해 로컬 환경에서 구축했다.
- `case_1367` 배치 기반 정산: 데이터가 누적될 때까지 기다려야 하므로 실시간성 확보가 어렵고 특정 시간에 시스템 부하가 발생할 수 있어 Kafka 기반 이벤트 처리 방식을 선택했다.
- `case_1368` Processor 내부 forward: Topology 내부 전파일 뿐 Kafka Streams의 스트림 시간을 갱신하지 못해 윈도우가 닫히지 않았다.
- `case_1368` WindowStore 직접 스캔: Store에서 데이터를 직접 발행해도 Streams 내부에서는 윈도우가 닫히지 않은 상태로 남아 다음 이벤트 처리 시 중복 발행이 발생했다.
- `case_1369` MLOps 관점 전 주기 설계: 라벨링 결과를 주고받는 과정이 매뉴얼하게 이루어졌고, 전 주기를 MLOps 관점에서 설계하는 방안은 향후 더 효율적인 작업을 위한 고려 사항으로 남았다.
- `case_1369` objectness score 사전 필터링: objectness score가 높은 오탐은 라벨링 품질이 개선되지 않을 위험이 있어 도입하지 않았다.
- `case_1370` 네이티브 앱 개발: 쿠폰·프로모션 정책이 변경될 때마다 앱 심사와 업데이트가 필요해 웹뷰보다 운영 효율성이 낮다고 판단했다.
- `case_1371` 스케줄링 배치 잡: 수신부가 발행부의 저장소인 인터페이스 테이블에 직접 의존하게 되어 발행부와 수신부의 책임을 분리하기 어렵다고 판단했다.
- `case_1373` 메모리 증설: 메모리를 계속 늘리는 방식 대신 번들러를 바꾸기로 했다.
- `case_1373` Parcel: 커스텀 제한적이었다.
- `case_1373` Rsbuild: 생태계가 작았다.
- `case_1375` 고정된 유저·상품 ID 기반 협업 필터링: 대규모 실시간 환경에서 업데이트가 어렵고 신규 유저·상품을 추천할 수 있는 콜드 스타트 대응이 어렵다.
- `case_1375` Transformer 기반 순차 추천 단독 방식: 실시간 추천마다 전체 Vocabulary에 대한 확률 분포를 계산해야 해 추론 비용과 latency가 크다.
- `case_1377` nginx 라우팅 설정: 개발팀에 실행 중인 인스턴스의 nginx 설정 파일 변경 및 nginx 재시작 권한이 없었고, 인프라 팀에 협조를 요청하면 점검 시간이 끝난 뒤에야 처리가 완료될 수 있었다.
- `case_1377` 스케줄링 배치: 최소한의 공수로 하나의 인스턴스 안에서 해결하기 위해 선택하지 않았다.
- `case_1378` 구글·Stack Overflow 검색: 검색 결과가 시스템 특화 에러를 정확히 해석하지 못할 수 있고, 결과를 다시 확인하고 검증하는 데 시간이 걸리기 때문에 채택하지 않았다.
- `case_1378` 에러 메시지만 전달: 에러 메시지만으로는 실제 코드와 비즈니스 로직을 파악하기 어려워 기초적인 해결 방안만 제시되었기 때문에 관련 로그와 소스 코드를 추가했다.
- `case_1379` nginx 설정으로 접근 차단: 리버스 프록시·게이트웨이 구조가 아니고 nginx 설정이 인프라팀 관리 하에 도커 베이스 이미지와 함께 생성되므로 인프라 상황에 적합하지 않았다.
- `case_1379` BigQuery 직접 질의: 페이지 라우팅이나 API 호출마다 BigQuery를 조회하면 네트워크 지연과 심각한 프로덕트 성능 저하가 발생할 수 있었다.
- `case_1384` JPA @PostLoad: 복호화된 값을 별도 필드에 보관하거나 개발자가 리스너를 작성해야 하고, 엔티티 필드 값을 바꾸면 dirty로 처리되어 조회만 해도 update가 발생했다.
- `case_1384` Hibernate PreLoad event: Spring Boot 3.0.4 환경에서 사용한 Hibernate 6.x에 PreLoad 시점을 제대로 활용할 수 없는 버그가 있었다.
- `case_1384` Hibernate 종속성 버전 변경: Hibernate 종속성만 다른 버전으로 고정하는 방법은 선호하지 않아 다른 대안을 찾았다.
- `case_1390` 동일 우편번호 범위 탐색: 우편번호 범위가 너무 넓고 우편번호마다 영역이 천차만별이라 실패했다.
- `case_1390` 동일 전체 도로명 코드 범위 탐색: 우편번호보다 낫지만 여전히 탐색 범위가 넓어 실패했다.
- `case_1392` max-lifetime 증가: Connection 누수 자체는 방지할 수 있지만 DB failover 시 slave로 빠르게 연결하기 위한 작은 max-lifetime 설정을 유지해야 하므로 채택하지 않았다.
- `case_1393` 지번주소 전용 DB 구성: 일평균 요청량이 적어 별도 데이터를 구성하는 것은 오버엔지니어링이라고 판단했다.
- `case_1396` CSV 직접 import: 좌표를 익숙한 지리적 위경도로 변환해야 했고, 행정안전부 연계방식으로 최신화하기 위한 파일 변환 로직도 필요했다.
- `case_1399` 필드 가시성 확대: 캡슐화 및 보안성 측면에서 바람직하지 않아 선택하지 않았다.
- `case_1402` 컬리몰·TOMS 분배: 컬리몰과 TOMS에서 각 배송 시스템으로 요청을 분배하면 수정해야 할 시스템과 협력 조직의 범위가 넓어지고, 롤백 시 다른 부서의 도움이 필요하다.
- `case_1404` CDC: Back Office 기능에서 실시간성이 중요하지 않아 배치 Polling 방식을 선택했다.
- `case_1406` 카프카 클러스터 권한 획득: 조직 간 권한 공유나 부여는 관리자가 체계적이고 안정적으로 권한을 관리하기 어렵고, Kafka CLI 방식도 컨슈머 그룹을 비활성화해야 했다.
- `case_1406` Apache Kafka Admin API: alterConsumerGroupOffsets API는 오프셋 변경에 성공하려면 컨슈머 그룹이 비어 있어야 하므로 무중단 오프셋 변경 요건을 충족하지 못했다.
- `case_1407` READ COMMITTED 격리수준: 격리수준을 낮추면 Phantom Read가 발생해 기존 비즈니스 로직에 영향을 줄 수 있어 채택하지 않았다.
- `case_1407` 잠금 읽기: 행 잠금으로 인해 락 경합 및 데드락 발생 가능성이 증가할 수 있어 채택하지 않았다.
- `case_1410` 과거 데이터 기반 분석: 이미 발생한 상황만 반영해 환경 변화 이후의 미래 결과를 예측하는 데 근본적인 한계가 있었다.
- `case_1410` 실제 환경 실험: 운영과 병행하기 어렵고 관찰자 개입으로 편향된 결과가 발생할 수 있었다.
- `case_1412` 기존 후기 이미지의 픽셀값 분포 비교: 흐린 이미지와 뚜렷한 이미지 집단 사이에 유의한 분포 차이가 나타나지 않았다.
- `case_1412` BDNet: 기존보다 흐린 이미지를 잘 잡아냈지만 precision이 0.6 정도로 낮았다.
- `case_1412` 인위적으로 만든 학습 데이터: 드라마틱한 성능 개선이 없었고 validation precision과 test precision 사이에 과적합 현상이 나타났다.
- `case_1413` 웹사이트 기반 데이터 소스: 크롤링 범위를 조절하기 어렵고 색인된 데이터를 직접 관리할 수 없어 불필요한 데이터가 포함되며 검색 결과의 신뢰도가 떨어질 수 있었다.
- `case_1413` 데이터 스토어 직접 접근: 보안과 데이터 소스와의 통합 유연성 측면에서 검색 애플리케이션을 별도로 생성하는 방식이 권장됐다.
- `case_1415` LimitRange와 ResourceQuota: 컴포넌트별로 다른 자원 요구사항을 가지는 데이터 애플리케이션들에는 적절하지 않다고 판단했다.
- `case_1416` 스케일 업·worker_concurrency 증가: 워커 자원을 늘리고 동시에 처리할 작업 수를 증가시키는 방법 대신 워커 수를 늘리는 스케일 아웃을 선택했다.
- `case_1417` BentoML: TorchServe가 응답 시간 측면에서 더 좋은 지표를 보여 최종적으로 선택하지 않았다. **(technologies에도 있음)**
- `case_1421` 라인 타입 아이콘: 퀵메뉴 위치에서 하단 탭바 아이콘과 시각적으로 충돌하고, 강조가 필요한 메뉴가 눈에 띄지 않아 새로운 아이콘 스타일을 도입했다.
- `case_1422` DB 비관적 락: 외부 API 호출이 포함된 구간에서 DB 커넥션과 락을 함께 점유한다.
- `case_1422` 낙관적 락 + 재시도: 충돌을 감지할 때는 이미 배달대행사로 외부 호출이 나가 되돌릴 수 없다.
- `case_1424` DPO만 적용: TPO 카드에서 formatmix 계열 변형으로는 DPO 기준선의 형식 통과율을 넘지 못해 형식 보정을 위해 GRPO를 추가했다.
- `case_1428` 기존 데몬 폴링 주기 축소: 폴링 주기를 줄이면 데이터베이스 부하만 커지고, WAS와의 자원 공유 및 표준 모니터링 밖에 있다는 문제가 남는다.
- `case_1428` crontab 배치: 한 대만 실행해야 중복을 막을 수 있고, 확장하려면 락이나 분산 처리를 직접 구현하고 검증해야 한다.
- `case_1428` 테이블 기반 큐 직접 구현: 메시지 큐가 이미 제공하는 배타적 점유, 처리 위치 기록, 재처리, 폭증 완충 기능을 사라질 코드로 직접 구현해야 한다.
- `case_1428` 서비스 직접 이벤트 발행: 수십 개 서비스와 저장 프로시저를 모두 수정해야 하는 빅뱅 전환이며, 통합 메시지 API 직접 호출이라는 최종 목표 구조와 같다.
- `case_1429` 이력 선저장 후 발송: 발송 기록은 남았지만 실제 문자가 나가지 않는 상황이 발생할 수 있어 선택하지 않았다.
- `case_1429` 큐 단위 재시도: 영구 실패 메시지가 큐 앞을 막아 정상 메시지까지 지연시키고, 큐가 제공하는 재처리 기회를 포기하더라도 발송 실패를 개별 결과로 남기는 쪽을 선택했다.
- `case_1431` 집중형 데이터베이스에서 원인 분석 지속: 기존 데이터베이스에서 원인 분석을 계속하는 방법은 선택하지 않았다.
- `case_1431` MySQL 5.7에서 5.6으로 다운그레이드: 분산 데이터베이스를 MySQL 5.6으로 되돌리는 방법은 선택하지 않았다.
- `case_1431` ElasticCloud: 컬리의 인프라가 AWS 중심으로 구성되어 있어 AWS OpenSearch를 선택했다.
- `case_1431` MongoDB: 후기 내용과 상품 검색 요구사항에는 OpenSearch의 역색인이 더 적합하다고 판단했다.
- `case_1432` 결제 API 우선 최적화: 결제 API를 먼저 빠르게 만드는 것보다 카드 혜택 식별 구조와 결제 경로를 먼저 정리하는 방식을 선택했다.
- `case_1433` iframe: Cross-Origin 보안 정책으로 부모 창과 쿠키·세션을 공유하지 못해 사용자가 iframe 안에서 다시 로그인해야 했다.
- `case_1433` 시스템 마이그레이션: 3가지 시스템을 Vue로 통일하려면 JSP 레거시 전체를 재작성해야 하고, 수개월의 작업 기간과 기존 시스템 안정성 저하 리스크가 필요했다.
- `case_1434` Bits AI: 권한 이슈가 있었고 외부 AI 연동에 MCP/API Key가 필요했으며, 분석 완료 시점을 파악하기 어려운 비동기 동작이라 원하는 운영 방식에 맞지 않았다.
- `case_1435` 가격 범위 계산 수식: 가격 범위를 계산하는 규칙은 일반화에는 유리했지만 한국어 가격 표현을 처리하지 못하는 케이스가 남아 Few-shot보다 정확도가 낮았다.
- `case_1437` MOST_REVIEWS_COUNT_DESC 정렬 옵션 제거: 정렬 옵션을 삭제해도 리뷰 기반 추천 툴이 호출되지 않아 원인이 아닌 것으로 확인됐다.
- `case_1445` @TransactionalEventListener: 레거시 시스템의 하위 Spring 버전과 공통 모듈 의존성 충돌, 클래스패스 혼재로 인한 런타임 오류와 빈 생성 오류가 발생해 채택하지 않았다.
- `case_1446` 알림 유형별 조회 쿼리: 알림 유형별로 쿼리를 만들면 레거시와 다른 점이 없어 채택하지 않았다.
- `case_1447` 플래그 폴링: 단일 인스턴스에서는 유효하지만 다중 인스턴스 환경에서 폴링 지연과 상태 확인 비용이 발생한다.
- `case_1447` 토픽 분리: 토픽을 분리하는 것만으로는 도메인 이벤트의 처리 순서를 제어할 수 없다.
- `case_1448` Spring Batch Multi-threaded Step: 스레드 수만큼 속도가 선형적으로 증가할 것이라 기대했지만, 병렬 처리 직후 Deadlock Loser 오류가 발생해 시스템이 멈췄다.
- `case_1449` RDS On-Demand 고정형 인스턴스: 세일 기간을 대비한 최고 사양 유지에는 비용 낭비가 크고, 평시 사양 유지에는 데이터 폭증 시 장애 위험이 있었다.
- `case_1453` 단순 JWT: 검증된 표준 프레임워크가 필요했기 때문에 단순 JWT 대신 OAuth2를 선택했다.
- `case_1456` 필요할 때마다 API 호출: 변경이 거의 없는 데이터를 빈번하게 호출해 리소스가 낭비된다.
- `case_1456` 1일 1회 S3 저장 후 조회: S3 전송 및 조회 과정이 추가되어 지연과 아키텍처 복잡성이 발생한다.
- `case_1458` DLQ 방식: 실패 원인 추적과 개별 재처리 제어가 어렵고 운영 가시성이 낮아 선택하지 않았다.
- `case_1460` if-else 분기: 파일 다운로드 API 수십 곳에 동일한 분기 로직을 복붙해야 하고 새로운 보안 솔루션이 추가될 때 여러 곳을 수정해야 하므로 채택하지 않았다.
- `case_1460` 별도 서비스 클래스 분리: 암호화 호출을 각 다운로드 메서드에서 명시해야 해 호출 누락 위험이 있고, 새로운 솔루션 추가 시 서비스 내부를 수정해야 하므로 채택하지 않았다.
- `case_1460` 팩토리 패턴: 객체 생성에 초점을 둔 방식이라 이미 Spring 컨테이너가 관리하는 싱글톤 빈을 선택해야 하는 요구에 맞지 않았고, new로 생성한 객체는 Spring의 의존성 주입과 AOP를 활용할 수 없었다.
- `case_1461` OGG 커넥터 단독: 기존 ODI 시스템의 다수 원천 테이블 조인과 데이터 가공 같은 복잡한 통합 비즈니스 로직을 처리할 수 없어 하이브리드 구조를 채택했다.
- `case_1463` 규칙 기반 시스템: 자연스럽고 다양한 추천 문구를 생성하는 품질과 확장성에 한계가 있었다.
- `case_1463` 상용 LLM API: 모델 업데이트에 따른 응답 변화, 긴 프롬프트의 비용·지연 증가, 호출량 증가에 따른 비용 급증 문제가 있었다.
- `case_1463` HyperCLOVA X ← HyperCLOVA X SEED: 한국어 성능은 우수했지만 MAU 기반 라이선스 제약으로 서비스 적용이 어렵다고 판단했다.
- `case_1463` Qwen ← Qwen 2.5/3: 실제 테스트에서 한국어 오타 정정 성능이 상대적으로 낮아 리뷰 기반 생성 과업에 부적합했다.
- `case_1463` Gemma2-2B: 개발 기간 중 출시된 Gemma3가 성능과 다국어 지원 면에서 더 적합해 Gemma3-4B로 변경했다.
- `case_1465` Kafka Streams Join: 초기 프로모션 정보까지 포함한 재고 관리 기획이 복잡한 비즈니스 관계로 인해 간소화되어 품절 시스템에는 조인을 사용하지 않았다.
- `case_1466` Lua 스크립트 적용: 미발급·과발급은 0건으로 해소했지만 기존 대비 약 21%의 성능 저하가 발생했고, 단일 스레드 특성에 따른 Redis 병목과 운영·관리 복잡도 증가 우려로 기각했다.
- `case_1477` URL 파라미터 토큰 전달: 브라우저 히스토리에 토큰이 노출되어 보안상 위험하다.
- `case_1477` Cookie: SameSite 정책 때문에 크로스 오리진에서 제약이 많다.
- `case_1477` 단순 플래그 제어: 토큰 갱신이 완료되기 전에 들어온 요청들이 실패한다.
- `case_1478` AWS Parameter Store: Git 버전 관리와 설정 계층 표현이 제한적이라고 판단해 Spring Cloud Config Server를 선택했다.
- `case_1481` 외주 제작: 제한된 예산 때문에 외주 제작을 선택지에서 제외했다.
- `case_1481` Gamma: 브랜드 컬러, 폰트, 레이아웃 가이드를 완벽히 따르기 어려워 수동 제작이 더 빠르고 정확했다.
- `case_1482` 모든 레이아웃을 서버 제어: 처음부터 모든 레이아웃 속성까지 서버가 제어하면 복잡도가 걷잡을 수 없이 커진다고 판단해 초기 범위에서 제외했습니다.
- `case_1482` 모든 화면 SDUI 전환: SDUI를 모든 화면에 적용하지 않고 화면 목적에 따라 네이티브·웹·SDUI를 전략적으로 조합하기로 했습니다.
- `case_1482` 이벤트 1안: 명시성과 이벤트 타입 집중이라는 장점은 있지만 새로운 이벤트 추가 시 확장성이 떨어져 2안을 권장했습니다.
- `case_1483` Native App: 개발 리소스와 일정이 제한되어 있었고 PDA가 단순 작업 위주로 운영되므로 웹 기반 시스템을 선택했다.
- `case_1484` 인스턴스 증설: 메모리를 늘려도 이미 동기화가 깨진 unsynchronized 상태가 해소되지 않아 근본적인 해결책이 되지 못했다.
- `case_1484` 브로커 재시작: Memory Alarm이 해소된 후에야 재시작이 가능했고, 관리형 서비스 특성상 즉시 재시작이 제한되었다.
- `case_1484` Classic Mirrored Queue: 메모리 부족 시 미러 동기화가 실패하고 out of sync 상태에서 메시지 소비가 중단되는 구조적 한계가 있어 Quorum Queue로 전환했다.
- `case_1486` contentEditable: 표준이 아니어서 브라우저마다 태그 처리, 줄바꿈 방식, execCommand 동작이 달라 일관성이 부족했다.
- `case_1487` Vue 기반 CMS: Vue 종속성으로 다른 프로젝트에서 재사용하기 어려웠고, 기능이 늘어날수록 상태 관리 복잡성이 커졌다.
- `case_1488` Cursor: PoC는 진행했지만 아직 전사 도입 단계가 아니어서 대안을 찾았다.
- `case_1495` 확률적 조기 갱신(PER): 비동기 처리를 활용하면 별도의 지연시간이 없지만 낮은 확률로 DB에 여러 번의 요청이 발생할 수 있어 선택하지 않았다.
- `case_1495` 백그라운드 업데이트: DB를 확실하게 보호할 수 있지만 별도의 배치 서비스 개발·운영이 필요하고 실시간 데이터 제공에 제약이 있어 선택하지 않았다.
- `case_1495` DB 락: 위험 부담이 커서 Redis를 활용한 락 방식으로 대체했다.
- `case_1496` 자체 서버 구축: 자체 서버 구축을 포함한 여러 로그 수집 솔루션을 비교한 뒤 Datadog을 최종 선택했다.
- `case_1499` 외부 WMS 의존: 기능 확장과 프로세스 개선에 한계가 있고, 시장 변화 대응과 물류센터 효율화가 지연되거나 무산됐다.
- `case_1503` 네트워크 구간 축소·메시징 구조 단순화: 여러 외부 시스템과 독립적으로 운영되는 서버 자원 때문에 Out-of-Order Events를 방지할 수 없는 구조였다.
- `case_1507` Chrome DevTools Overrides: 일회성 테스트에는 유용하지만 매번 수동 작업이 필요해 향후 Application Level 테스트를 프로세스화하기에는 리소스가 과도하게 소모된다고 판단했다.
- `case_1507` Charles·Fiddler 프록시: 간단한 테스트에는 적합하지만 필드 값이 많을 때 하나씩 수동으로 수정해야 해 프로세스화에 적합하지 않다고 판단했다.
- `case_1507` 실제 데이터 입력: API가 어떤 경우에 null 값을 전달하는지 정의되지 않아 데이터 수정만으로 null을 전달하기 어렵다고 판단했다.
- `case_1510` API Polling 기반 아키텍처: 요청 이력 ID를 API 응답으로 반환할 수 없게 되어 클라이언트가 요청과 응답을 연결할 수 없었기 때문에 포기했다.
- `case_1510` 발주 처리 로직 멱등화: 기존 발주 처리 로직 자체를 수정해야 하므로 채택하지 않았다.
- `case_1510` ReplyingKafkaTemplate: 요청 정보가 메모리에 저장되어 타임아웃이나 배포·스케일인 시 유실될 수 있고, 재요청으로 중복 발주가 발생할 수 있어 도입하지 않았다.
- `case_1512` Confluence: 코드와 문서가 별도로 존재해 코드 변경 후 문서 업데이트를 놓치기 쉬웠고, 코드와 문서의 차이가 커졌다.
- `case_1516` App Follow: 외부 플랫폼을 사용하면 크롤링 주기를 직접 설정하기 어려워 리뷰 수신 지연을 개선하기 어려웠다.
- `case_1516` 크롤링 방식: 스토어 API를 활용하는 방식이 크롤링보다 익숙해 API 기반 수신 방식을 선택했다.
- `case_1517` WebP 변환: 복잡한 이미지에서는 압축 효율이 낮았고, 품질을 낮추면 시각적인 퀄리티 저하가 발생해 실제 적용에 제약이 있었다.
- `case_1517` 메인 스레드 Canvas 리사이징: 파일 크기와 업로드 속도는 개선됐지만 Canvas 처리 비용과 디코딩·인코딩 과정의 JS 블로킹으로 메인 스레드가 점유됐다.
- `case_1517` Shared Worker·Service Worker: 이미지 처리에 불필요한 기능들이 많아 배제했다.
- `case_1521` Kotlin: 팀 구성원 대부분이 자바로 개발하고 코틀린을 사용해 본 인원이 없었으며, 코틀린의 특징과 패러다임을 이해하지 않고 도입하면 코드가 난잡해질 수 있다고 판단했다.
- `case_1524` WriteConcern MAJORITY: 모든 요청에서 Secondary 과반수 ACK 응답을 기다리면 큰 오버헤드가 발생할 수 있어 채택하지 않았다.
- `case_1524` ReadPreference PRIMARY: 모든 읽기 트래픽을 Primary에 집중하면 Secondary 노드가 유휴 상태로 남을 수 있어 트랜잭션에만 적용했다.
- `case_1525` SQS 메시지 지연 전달: 지연 시간이 너무 짧으면 타이밍 문제가 다시 발생할 수 있어 임시방편으로 판단했다.
- `case_1525` Outbox 패턴·로그 테일링 패턴: 데이터와 메시지를 분리해 관리할 수 있지만 설계 및 구현 시간과 비용이 부담되어 당장 적용하지 않았다.
- `case_1527` MP4: 파일을 처음부터 끝까지 다운로드해야 하고 네트워크 상태에 따라 지연이 발생할 수 있어 최종 채택하지 않았다.
- `case_1527` DASH: MP4, DASH, HLS를 비교한 결과 HLS를 선택했다.
- `case_1527` 웹 기반 구현: 웹 환경에서 영상 인코딩과 업로드를 처리하는 데 한계가 있었다.
- `case_1527` 100% 네이티브 구현: UI 변경과 A/B 테스트가 잦은 서비스 특성상 배포와 업데이트의 유연성이 떨어졌다.
- `case_1529` HDR → SDR 변환: 색상 왜곡은 해결했지만 변환 시간이 길어 최종적으로 클라이언트 기반 동적 톤 조정으로 전환했다.
- `case_1531` 미리 정해진 상품 선정: 상품 상태와 프로모션이 수시로 변경되므로 미리 정한 상품만으로는 최신 상태를 확인하기 어렵다고 판단했다.
- `case_1531` 테스트 상품·프로모션 직접 등록: STG와 운영에 테스트 상품이나 테스트 프로모션을 등록하는 것을 지양하는 회사 정책이 있어 API로 실제 데이터를 조회하는 방식을 선택했다.
- `case_1534` Oracle GoldenGate: 분당 약 3만 건의 처리량으로 대규모 데이터 처리에 적합하지 않았고, 수백만 건 이상의 대용량 데이터 처리에서 성능 이슈가 발생했다.
- `case_1540` Sink Connector: 기존 테이블 구조와 다른 신규 시스템 테이블로 데이터를 전송해야 해 데이터 변환과 매핑을 직접 수행하기로 했다.
- `case_1542` 웹 컴포넌트로 상품 컴포넌트 재구현: 복잡한 컴포넌트를 새로 만들기에는 기간이 촉박하고 결함이 많이 발생할 것으로 판단했다.
- `case_1543` scrollIntoView: 다른 컴포넌트에서 바인딩한 스크롤 이벤트와 겹쳐 사용할 수 없었다.
- `case_1547` EAI I/F: 배치를 사용하는 방식에서 지연이 발생했고, 하나의 EAI 어댑터 장애가 전체 통신 중단으로 이어질 수 있어 MQ로 대체했다.
- `case_1548` 업로드 완료 즉시 표시 후 백그라운드 업로드: 실제 업로드가 완료되지 않았는데 UI에서 완료된 것처럼 표현하는 방식보다 실시간 진행 상태 표시를 적용했다.
- `case_1551` At least once: OMS 데이터 특성상 메시지 중복을 허용할 수 없어 사용할 수 없었다.
- `case_1553` RangeAssignor Strategy: ECS Task에 Partition이 편중되고 배포 때마다 Partition이 불규칙하게 뒤섞여 할당되었다.
- `case_1558` 담당자 ID 하드코딩: 담당자가 늘어나면서 유지보수 및 관리가 어려워져 Slack 그룹에서 유저 리스트를 받아 초대하는 방식으로 변경했다.
- `case_1560` Claude 3 Haiku: 일부 케이스에서 분류 목표를 달성하지 못했다.
- `case_1560` OpenAI API ← GPT-4: 일부 복잡한 사례에서 오류가 발생했다.
- `case_1560` OpenAI API ← GPT-3.5 Turbo: 이미지 분석 기능을 지원하지 않았다.
- `case_1560` OpenAI API ← ChatGPT: 별도의 API 설정, 관리 및 모니터링이 필요했다.
- `case_1561` ZXing: Android에서 카메라 기능 사용 시 CameraX 사용을 권장하고 MLKit을 구글에서 밀고 있는 Vision API로 판단하여 ZXing을 제거했다.
- `case_1564` API Gateway: 현재 private로 사용이 불가능해 제외했다.
- `case_1564` Gateway 역할 WAS 혹은 Web Server: 개발 PoC에 시간이 소요되고 요청 흐름의 경로가 바뀌어 전수 테스트가 필요해 제외했다.
- `case_1565` JSON 파일 기반 Fixture: JSON에 클래스에 없는 키가 포함되거나 JSON 구조가 변경되면 ObjectMapper 변환 오류가 발생하고 모델 클래스도 수정해야 한다.
- `case_1568` Xstream: Xstream.jar를 업로드해야 하지만 MSK Connect가 매니지드 서비스라 지원하지 않아 사용하지 않았다.
- `case_1569` Postman Mock Server: 개발자마다 모의 서버를 만들어야 하고 다른 개발자들과 공유하기 불편했으며, API 주소를 특정해야 해 휴먼에러가 발생할 수 있고 기업 사용을 위해 플랜 가입이 필요했다.
- `case_1569` Nock: Node에서만 동작하고 단위 테스트 외에는 활용하기 어려워 도입을 보류했다.
- `case_1573` 스케줄러 방식: Spring Batch 실행에 스케줄러를 사용하는 방식보다 Kafka 이벤트에 의해 배치를 트리거하는 방식을 선택했다.
- `case_1579` Amazon SQS ← SQS: 판매데이터 수집용 파이프라인 구성 방안으로 모색했지만 랭킹의 준실시간성을 고려해 채택하지 않았습니다.
- `case_1579` 상시 운영 애플리케이션 서버: 랭킹의 준실시간성을 고려했을 때 항상 온라인 상태로 유지되는 온프레미스 또는 클라우드 애플리케이션 서버는 불필요하다고 판단했습니다.
- `case_1585` isTextSmall useState 구현: 처음 useState로 작성했으나 이후 값을 메모이제이션하는 useMemo로 대체했다.
- `case_1589` 브라우저 자체 스크롤 유지: 상품 상세페이지와 검색 결과 페이지가 서로 다른 프로젝트로 분리되어 있어 브라우저 자체 기능을 사용하는 것이 의미가 없었다.
- `case_1594` Formik: 각 입력 영역을 상태로 관리하고 change 이벤트마다 상태를 업데이트하므로 입력할 때마다 렌더링이 발생할 수 있다.
- `case_1596` Netflix Hystrix: 현재 deprecated 된 상태로 Resilience4j 사용 권장
- `case_1597` CDN: 보안 이슈로 도입이 어려웠다.
- `case_1597` .otf·.ttf를 .woff·.woff2로 변환: 폰트가 깨지거나 정상적으로 import되지 않았다.

## 글 목록

| 글 | 길이 | 결과 | 항목 | 발췌 탈락 | 제목 |
| --- | --- | --- | --- | --- | --- |
| d2/7976382 | 52,414 | 추출/실험·활용기 | case_1135 | 0/15 | 시니어 개발자가 대화형 인공지능(ChatGPT)과 페어 프로그래밍하는 법(feat. DEVIEW 2023 코드 구현하기) |
| d2/2771091 | 24,462 | 추출/실험·활용기 | case_1134 | 0/10 | flatMap만 사용하기는 그만! Reactor 오퍼레이터 파헤치기 |
| d2/3010710 | 17,508 | 추출/실험·활용기 | case_1138 | 1/10 | AOP in TypeScript |
| d2/7181840 | 11,754 | 추출/문제 해결형 | case_1137 | 0/12 | Kafka에서 파티션 증가 없이 동시 처리량을 늘리는 방법 - Parallel Consumer |
| d2/4608596 | 688 | 제외/회고·문화·행사 | - | 0/0 | AI 경량화: 더 빠르고 저렴한 AI 서비스 |
| d2/5053838 | 607 | 제외/회고·문화·행사 | - | 0/0 | Local key-value 스토리지가 고민일땐 RocksDB 어때? |
| d2/2236952 | 529 | 제외/회고·문화·행사 | - | 0/0 | Kotlin으로 Cli를 만든다고? |
| d2/5766317 | 9,180 | 추출/문제 해결형 | case_1133 | 0/10 | 데이터 품질 이슈로 발생하는 data downtime을 줄이자 |
| d2/3461887 | 842 | 제외/문제 해결형 | - | 0/0 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Crash 분석 시스템 NCrashlytics |
| d2/3612055 | 1,371 | 제외/개념·튜토리얼 | - | 0/0 | Terraform을 활용한 네이버 클라우드 플랫폼 IaC(Infrastructure as Code) 적용하기 |
| d2/9139321 | 1,013 | 제외/개념·튜토리얼 | - | 0/0 | Awesome Terraform Overview HCL Deep Dive & Terraform Expansion |
| d2/2184045 | 11,720 | 추출/기술 선택·도입형 | case_1132 | 0/11 | 거기 말고 이 호텔 어때? - 호텔 서비스 추천 시스템 도입기 |
| d2/6014816 | 670 | 제외/회고·문화·행사 | - | 0/0 | 중요한 것은 사용자의 의도를 꺾지 않으려는 마음 (동시편집에서 Text.Style Operation 개선 및 Multi User Undo/Redo 구현하기) |
| d2/0983091 | 569 | 제외/회고·문화·행사 | - | 0/0 | One-Source Multi-Use, 스마트플레이스 일본 진출 작업기 |
| d2/4555524 | 18,452 | 추출/기술 선택·도입형 | case_1131 | 0/18 | AI 플랫폼을 위한 스토리지 JuiceFS 도입기 |
| d2/6445508 | 17,733 | 추출/문제 해결형 | case_1127 | 0/11 | HDFS 쓰기 파이프라인을 활용한 HBase의 WAL 쓰기 최적화 |
| d2/8404108 | 11,072 | 추출/실험·활용기 | case_1128, case_1129 | 0/15 | 프로파일링 적용기 - 당신의 Go 애플리케이션은 좀 더 나아질 수 있다 |
| d2/6867189 | 4,035 | 추출/문제 해결형 | case_1124, case_1125, case_1126 | 0/18 | 네이버 검색 SRE의 시계열 데이터베이스 운영기 - VictoriaMetrics로 수천만 개의 시계열 데이터 다루기 |
| d2/1203723 | 18,712 | 추출/실험·활용기 | case_1123 | 0/7 | Virtual Thread의 기본 개념 이해하기 |
| d2/9581727 | 6,572 | 추출/문제 해결형 | case_1130 | 0/14 | 일 3,000만 건의 네이버페이 주문 메시지를 처리하는 Kafka 시스템의 무중단 전환 사례 |
| d2/6178029 | 23,416 | 추출/문제 해결형 | case_1118 | 0/14 | Golang, 그대들은 어떻게 할 것인가 - 2. MongoDB Go Driver 추상화 |
| d2/8588537 | 5,341 | 추출/문제 해결형 | case_1114 | 0/5 | Golang, 그대들은 어떻게 할 것인가 - 1. 들어가며 |
| d2/2690202 | 7,916 | 추출/문제 해결형 | case_1117 | 0/11 | Golang, 그대들은 어떻게 할 것인가 - 3. error 래핑 |
| d2/6507662 | 12,532 | 추출/문제 해결형 | case_1116 | 0/11 | Golang, 그대들은 어떻게 할 것인가 - 4. error 핸들링 |
| d2/9227596 | 6,802 | 추출/실험·활용기 | case_1115 | 0/12 | 네이버 통합 검색의 웹 성능 - 데이터 수집과 시각화 |
| d2/7136716 | 5,447 | 추출/문제 해결형 | case_1122 | 0/12 | 숏클립 생성을 위한 하이라이트 검출 기술 개발기 |
| d2/8113611 | 9,820 | 추출/문제 해결형 | case_1119, case_1120 | 0/19 | 네이버 통합 검색의 웹 성능 - 모니터링과 성능 개선 |
| d2/2461452 | 5,565 | 추출/실험·활용기 | case_1121 | 0/8 | UX 원칙에 따른 NELO 4.0 개발기 |
| d2/5564264 | 522 | 제외/회고·문화·행사 | - | 0/0 | 쿠버네티스 네이티브 사이드카 컨테이너 (Sidecar Containers) |
| d2/7472830 | 651 | 제외/개념·튜토리얼 | - | 0/0 | infer, never만 보면 두려워지는 당신을 위한 고급 TypeScript |
| d2/0680815 | 811 | 제외/회고·문화·행사 | - | 0/0 | 실시간 광고 사용자 ID 매핑 |
| d2/0623656 | 675 | 제외/개념·튜토리얼 | - | 0/0 | DESIGN SYSTEM FOR Android: From Figma to Jetpack Compose |
| d2/7030870 | 571 | 제외/회고·문화·행사 | - | 0/0 | 디자인시스템을 개발에서 적용 하는법 |
| d2/8011540 | 576 | 제외/회고·문화·행사 | - | 0/0 | Writing Path: MBTI J처럼 체계적으로 글쓰는 AI |
| d2/2905424 | 868 | 제외/개념·튜토리얼 | - | 0/0 | Kubernetes에서 DNS 다루는 방법 - 도메인을 찾아서 |
| d2/7282210 | 534 | 제외/회고·문화·행사 | - | 0/0 | 보낼 로그가 1000개가 되는동안 겪었던 고민들 |
| d2/7321313 | 732 | 제외/회고·문화·행사 | - | 0/0 | 시간은 금이다: LLM을 이용한 AI 코드 리뷰 도입기 |
| d2/3713986 | 5,118 | 제외/개념·튜토리얼 | - | 0/0 | infer, never만 보면 두려워지는 당신을 위한 타입 추론 - 고급 타입 추론 |
| d2/5088940 | 6,516 | 제외/개념·튜토리얼 | - | 0/0 | infer, never만 보면 두려워지는 당신을 위한 타입 추론 - 응용 문제 |
| d2/9283310 | 9,274 | 제외/개념·튜토리얼 | - | 0/0 | infer, never만 보면 두려워지는 당신을 위한 타입 추론 - 기초 타입 이론 |
| d2/0281668 | 5,799 | 추출/문제 해결형 | case_1113 | 0/10 | 네이버 검색 SRE -  상위 레벨 모니터링 시스템 |
| d2/1623894 | 2,777 | 추출/문제 해결형 | case_1111 | 0/10 | 네이버 검색 SRE - 지진과 비상 대응 시스템 |
| d2/7989422 | 6,522 | 추출/실험·활용기 | case_1112 | 0/10 | 실시간 광고 사용자 ID 매핑 |
| d2/8857983 | 2,711 | 추출/기술 선택·도입형 | case_1110 | 0/8 | 네이버 뉴스 서비스가 장애를 예방하는 방법 - 카오스 엔지니어링 |
| d2/0403593 | 1,201 | 추출/문제 해결형 | case_1109 | 0/5 | 서비스 장애를 예방하는 방법: Chaos Engineering |
| d2/3344073 | 5,564 | 추출/기술 선택·도입형 | case_1107 | 0/13 | LLMOps를 위한 프롬프트 엔지니어링 도구 개발 경험기 |
| d2/2380720 | 8,419 | 추출/문제 해결형 | case_1108 | 0/11 | 생성형 AI 기반 실시간 검색 결과 재순위화 1편 - 서빙 시스템 아키텍처 |
| d2/5692818 | 4,689 | 추출/기술 선택·도입형 | case_1105 | 0/15 | 생성형 AI 기반 실시간 검색 결과 재순위화 2편 - LLM 서빙 |
| d2/6480558 | 4,723 | 추출/기술 선택·도입형 | case_1100 | 0/13 | 네이버페이 주문에 적용된 확장 가능한 대기열 개발기 |
| d2/1773964 | 9,271 | 추출/기술 선택·도입형 | case_1106 | 0/12 | 네이버 검색 클라이언트 로그 수집 - Beacon API 전환기 |
| d2/8866888 | 684 | 제외/회고·문화·행사 | - | 0/0 | 경량화 레시피: Teacher 지식 조린 소형 모델, 근데 성능을 곁들인 |
| d2/3247986 | 918 | 제외/회고·문화·행사 | - | 0/0 | HCX-VLM과 함께 홈피드를 더 예쁘게 바꿔보자! |
| d2/1536585 | 654 | 제외/개념·튜토리얼 | - | 0/0 | 신규 프로젝트 Hazelcast 도입기 |
| d2/8149881 | 7,735 | 추출/문제 해결형 | case_1098, case_1099 | 0/16 | GitHub Actions를 이용한 코드 리뷰 문화 개선기 |
| d2/8808377 | 726 | 제외/회고·문화·행사 | - | 0/0 | 13년 된 네이버 캘린더 안드로이드 앱, 멀티 플랫폼 기반 모듈화 적용 |
| d2/5646819 | 551 | 제외/기술 선택·도입형 | - | 0/0 | C++에서 Kotlin, Swift 까지?! Bazel을 활용한 Android / iOS 모노레포 도입기 |
| d2/3012756 | 783 | 제외/회고·문화·행사 | - | 0/0 | [UX개선 장기 로드맵] 수립기 - "VOC많은 순"으로만 일하지 않기 위하여 |
| d2/4534298 | 650 | 제외/개념·튜토리얼 | - | 0/0 | 타입시스템 기반 도메인 모델링 - 보이지 않는 오류를 막아라 |
| d2/9114363 | 688 | 제외/회고·문화·행사 | - | 0/0 | 대규모 AI 서비스 운영을 위한 Kubernetes GPU 클러스터 도입기 |
| d2/9591075 | 991 | 제외/회고·문화·행사 | - | 0/0 | 일잘러 연구소: 소프트 스킬을 키우는 효과적인 방법 |
| d2/6754228 | 6,543 | 추출/문제 해결형 | case_1097 | 0/11 | [DAN 24] 서치피드: SERP를 넘어 SURF로! 검색의 새로운 물결 |
| d2/0556679 | 6,205 | 추출/기술 선택·도입형 | case_1101 | 0/13 | [DAN 24] LLM의 Re-Ranking Ability 검색에 이식하기 1편 - LLM 이식 방법 |
| d2/6482000 | 8,150 | 추출/문제 해결형 | case_1096 | 0/14 | [DAN 24] LLM의 Re-Ranking Ability 검색에 이식하기 2편 - LLM을 활용한 최신성 반영 |
| d2/4936925 | 7,089 | 추출/문제 해결형 | case_1095 | 0/15 | [DAN 24] 검색과 피드의 만남: LLM으로 완성하는 초개인화 서비스 ② 사용자 검색 의도 세분화 |
| d2/5152301 | 3,133 | 추출/기술 선택·도입형 | case_1093 | 0/7 | [DAN 24] 검색과 피드의 만남: LLM으로 완성하는 초개인화 서비스 ① 홈피드와 교차 도메인 컨텍스트 |
| d2/7269246 | 6,386 | 추출/문제 해결형 | case_1094 | 0/10 | [DAN 24] 검색과 피드의 만남: LLM으로 완성하는 초개인화 서비스 ③ 사용자 관심 주제 추출 |
| d2/4142663 | 13,626 | 추출/문제 해결형 | case_1088, case_1089 | 0/18 | Kubernetes Job과 커스텀 컨트롤러를 활용한 배치 처리 경험기 |
| d2/3435419 | 15,806 | 추출/문제 해결형 | case_1102, case_1103, case_1104 | 0/28 | [DAN 24] 데이터 기반으로 지속 성장이 가능한 네이버 검색 FE 시스템 구축하기 |
| d2/5316262 | 13,046 | 추출/문제 해결형 | case_1090, case_1091, case_1092 | 0/19 | Go GC를 너무 믿지 마세요 - 메모리 누수 탐지와 GC 주기 조절 |
| d2/7248350 | 9,114 | 추출/실험·활용기 | case_1076 | 0/11 | 리눅스의 Control Groups 기능이 Kubernetes에 어떻게 적용되는지 살펴보기 |
| d2/4896087 | 4,941 | 추출/문제 해결형 | case_1085, case_1086, case_1087 | 0/22 | 호텔 검색, 어떻게 달라졌을까요? 3편 - 검색 시스템 |
| d2/5453314 | 2,769 | 추출/문제 해결형 | case_1068 | 0/9 | 호텔 검색, 어떻게 달라졌을까요? 4편 - 이미지 검색 |
| d2/5871868 | 2,731 | 추출/문제 해결형 | case_1069 | 0/11 | 호텔 검색, 어떻게 달라졌을까요? 2편 - 지식 증류 |
| d2/8366976 | 3,331 | 추출/문제 해결형 | case_1080, case_1081, case_1082, case_1083 | 0/24 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/9582944 | 6,435 | 추출/실험·활용기 | case_1073, case_1074, case_1075 | 0/21 | 2024 네이버 통합검색의 웹 성능 리뷰 |
| d2/8998207 | 17,149 | 추출/기술 선택·도입형 | case_1084 | 0/17 | NELO Alaska: 대용량 로그 데이터 저장을 위한 Apache Iceberg 도입기 |
| d2/7061905 | 2,586 | 추출/실험·활용기 | case_1067 | 0/8 | 네이버 거리뷰3D, 디지털 트윈을 곁들인 |
| d2/9921217 | 12,349 | 제외/개념·튜토리얼 | - | 0/0 | 테스트는 어떻게 좋은 코드를 만드는가(feat. 험블 객체 패턴) |
| d2/6615449 | 5,675 | 추출/실험·활용기 | case_1063 | 0/8 | 나만의 Visual Studio Code Copilot 지침 만들고 활용하기 |
| d2/2523796 | 5,984 | 추출/문제 해결형 | case_1065 | 0/10 | 데이터센터 각 세종의 스마트 공조 설루션, NAMU III |
| d2/7823344 | 15,398 | 추출/문제 해결형 | case_1064 | 0/12 | CDC 복제 이후 오라클이 느려졌다? child cursor 폭증이 만든 예상치 못한 문제 |
| d2/1168674 | 8,004 | 추출/기술 선택·도입형 | case_1066 | 0/10 | StarRocks의 도입 배경과 성능 최적화 |
| d2/3814947 | 16,662 | 추출/실험·활용기 | case_1070, case_1071, case_1072 | 0/23 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/4871077 | 1,148 | 제외/회고·문화·행사 | - | 0/0 | [영상] 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/5294836 | 728 | 제외/개념·튜토리얼 | - | 0/0 | 14년 된 네이버 캘린더 앱, KMP & 컴포즈 멀티 플랫폼 모듈 적용기 |
| d2/0362045 | 1,119 | 제외/회고·문화·행사 | - | 0/0 | 데이터는 흐른다,  연결될 준비가 되었다면 |
| d2/8051412 | 751 | 제외/회고·문화·행사 | - | 0/0 | KMP 기반 UI 컴포넌트 통합 전략 |
| d2/4678393 | 956 | 제외/회고·문화·행사 | - | 0/0 | Paimon 겟또다제 ! (w/ ADVoost Shopping) |
| d2/3675627 | 1,250 | 제외/문제 해결형 | - | 0/0 | 늘어가는 조회트래픽 Elasticsearch로 분산시키기 |
| d2/0207214 | 12,104 | 추출/문제 해결형 | case_1077, case_1078, case_1079 | 1/32 | 홈피드: 네이버의 진입점에서 추천 피드를 외치다! 추천 피드 도입 고군분투기 |
| d2/4394645 | 10,493 | 추출/문제 해결형 | case_1061 | 0/15 | Yappi로 Python에서도 성능을 챙겨보자 |
| d2/1025526 | 769 | 제외/회고·문화·행사 | - | 0/0 | 서비스 조직에서 Kafka를 사용할 때 알아 두어야 할 것들 (4) |
| d2/2472336 | 696 | 제외/개념·튜토리얼 | - | 0/0 | 서비스 조직에서 Kafka를 사용할 때 알아 두어야 할 것들 (3) |
| d2/2774577 | 23,755 | 제외/개념·튜토리얼 | - | 0/0 | C++에서 안정적인 멀티 스레드 코드를 위한 스레드 안전성 개념 정리 |
| d2/3078195 | 1,326 | 제외/개념·튜토리얼 | - | 0/0 | Thread-safety in C++ |
| d2/5251464 | 847 | 제외/회고·문화·행사 | - | 0/0 | AI가 지켜보는 데이터 파이프라인: 노이즈 제거부터 장애 대응까지 |
| d2/4706492 | 1,246 | 제외/실험·활용기 | - | 0/0 | Windowing 기법을 적용한 대용량 고성능 표 컴포넌트 개발기 |
| d2/6196427 | 1,234 | 제외/회고·문화·행사 | - | 0/0 | Docusaurus를 이용한 API 문서 플랫폼의 진화 |
| d2/6269411 | 1,042 | 제외/회고·문화·행사 | - | 0/0 | Spring Cloud Config HA 적용을 위한 커스터마이징 |
| d2/0251755 | 786 | 제외/회고·문화·행사 | - | 0/0 | Kubernetes GPU 클러스터에서 AI 서비스 오토스케일링하기 |
| d2/4348237 | 1,096 | 제외/회고·문화·행사 | - | 0/0 | Ray를 활용한 GPU Util 100% MLOps: 배치처리부터 모델 서빙까지 |
| d2/0539348 | 751 | 제외/회고·문화·행사 | - | 0/0 | 레거시 GPU에 날개 달기: 극한의 서빙 최적화 가이드 |
| d2/1450243 | 15,218 | 추출/문제 해결형 | case_1055 | 0/10 | 윈도잉(windowing) 기법을 적용한 고성능 표 컴포넌트 개발기 |
| d2/2766731 | 40,762 | 추출/기술 선택·도입형 | case_1062 | 0/13 | 실시간 유효 광고 선정을 위한 Flink에서 Apache Paimon 도입기 |
| d2/5215257 | 15,955 | 추출/기술 선택·도입형 | case_1057 | 0/13 | JuiceFS: 오브젝트 스토리지를 활용하는 HDFS 호환 분산 파일 시스템 |
| d2/3088532 | 13,811 | 추출/실험·활용기 | case_1054 | 0/12 | AI로 E2E 테스트를 찍어내다: MAFT |
| d2/1072010 | 564 | 제외/회고·문화·행사 | - | 0/0 | 글로벌웹툰 안드로이드 Large Screen 적용기 |
| d2/0548704 | 769 | 제외/개념·튜토리얼 | - | 0/0 | ARC로 확장가능한 GPU 서비스 개발 인프라 구축하기 |
| d2/1104856 | 749 | 제외/개념·튜토리얼 | - | 0/0 | 처음 만나는 OpenTelemetry (feat. Collector) |
| d2/6388660 | 21,269 | 추출/기술 선택·도입형 | case_1058, case_1059, case_1060 | 1/24 | 6개월 만에 연간 수십조를 처리하는 DB CDC 복제 도구 무중단/무장애 교체하기 |
| d2/8677833 | 606 | 제외/회고·문화·행사 | - | 0/0 | Telegraf로 커스텀 지표 수집하기: Exporter 개발 경험 공유 |
| d2/1580651 | 604 | 제외/문제 해결형 | - | 0/0 | API 호출식 웜업의 부작용을 넘어서 : 라이브러리만 데우는 JVM 웜업 |
| d2/3974242 | 639 | 제외/회고·문화·행사 | - | 0/0 | 서비스 조직에서 Kafka를 사용할 때 알아 두어야 할 것들 (5) |
| d2/8992409 | 1,342 | 제외/회고·문화·행사 | - | 0/0 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| d2/0957098 | 642 | 제외/회고·문화·행사 | - | 0/0 | 이건 첫 번째 클릭! 히트맵 같이 보기 |
| d2/3691494 | 717 | 제외/회고·문화·행사 | - | 0/0 | AI와 함께하는 프로젝트 자동화 : 더 빠르고, 더 스마트하게 |
| d2/7610642 | 21,056 | 추출/문제 해결형 | case_1056 | 0/15 | @RequestCache: HTTP 요청 범위 캐싱을 위한 커스텀 애너테이션 개발기 |
| d2/4199466 | 878 | 제외/문제 해결형 | - | 0/0 | 경험이 쌓일수록 똑똑해지는 네이버 통합검색 LLM Devops Agent |
| d2/9290684 | 978 | 제외/문제 해결형 | - | 0/0 | Iceberg Low-Latency Queries with Materialized Views  (feat. 실시간 거래 리포트) |
| d2/2678553 | 1,643 | 제외/회고·문화·행사 | - | 0/0 | 사용자의 목소리를 AI로 재현하다: LLM기반 Multi Agent UX플랫폼 개발기 |
| d2/4571155 | 13,684 | 추출/실험·활용기 | case_1052, case_1053 | 0/21 | 웹툰 창작 생태계 보호를 위한 연구 |
| d2/0931890 | 998 | 제외/회고·문화·행사 | - | 0/0 | VLOps:Event-driven MLOps & Omni-Evaluator |
| d2/9036125 | 1,154 | 제외/회고·문화·행사 | - | 0/0 | LLM이지만 PDF는 읽고 싶어: 복잡한 PDF를 LLM이 이해하는 방법 |
| d2/3442203 | 775 | 제외/회고·문화·행사 | - | 0/0 | 디자인시스템이 AI를 만났을 때: FE 개발 패러다임의 변화 |
| d2/0004394 | 22,286 | 추출/문제 해결형 | case_1050, case_1051 | 1/25 | 비용, 성능, 안정성을 목표로 한 지능형 로그 파이프라인 도입 |
| d2/4241703 | 5,509 | 추출/문제 해결형 | case_1037 | 0/9 | 네이버 통합검색 AIB 도입과 웹 성능 변화 분석 |
| d2/6512234 | 22,022 | 추출/기술 선택·도입형 | case_1047, case_1048, case_1049 | 0/28 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/1155434 | 9,048 | 추출/문제 해결형 | case_1043 | 0/12 | C++ std::bit_cast와 reinterpret_cast — 언제 어떤 것을 써야 하는가 |
| d2/7997284 | 15,816 | 제외/개념·튜토리얼 | - | 0/0 | C++ 객체 수명과 암묵적 객체 생성 |
| d2/6475419 | 12,710 | 추출/기술 선택·도입형 | case_1041, case_1042 | 0/22 | 네이버 검색의 대규모 메트릭 저장소, VictoriaMetrics 운영기 |
| d2/2017402 | 7,626 | 추출/실험·활용기 | case_1036 | 0/11 | 비개발자의 AI 협업 도전기 — 생산성 측정하려다 서버까지 띄운 9일 |
| d2/8061804 | 1,141 | 제외/회고·문화·행사 | - | 0/0 | AI 에이전트가 코드를 실험하고 개선하는 법 |
| d2/9290861 | 796 | 제외/개념·튜토리얼 | - | 0/0 | Inside VictoriaMetrics |
| d2/0107009 | 1,032 | 제외/회고·문화·행사 | - | 0/0 | 비개발자가 한 달 동안 풀스택으로 개발하면서 배운 것 |
| d2/6647064 | 638 | 제외/문제 해결형 | - | 0/0 | AI국민비서: 공공 특화 에이전트 구축하기 |
| d2/4372269 | 961 | 제외/회고·문화·행사 | - | 0/0 | 안드로이드 빌드 대기 시간 없애기 |
| d2/3431313 | 624 | 제외/개념·튜토리얼 | - | 0/0 | Android 앱의 의도치 않은 변경 방지하기 |
| d2/1059238 | 861 | 제외/회고·문화·행사 | - | 0/0 | MLXP : Kubernetes LLM Serving  최적화 기술 도입기 |
| d2/6811215 | 821 | 제외/회고·문화·행사 | - | 0/0 | AI 에이전트를 위한 Playwright E2E 테스트 하네스 구축하기 |
| d2/8319114 | 741 | 제외/회고·문화·행사 | - | 0/0 | SaaS 대체하기: AI와 함께한 광고SDK 에러 모니터링 시스템 구축기 |
| d2/4399330 | 839 | 제외/회고·문화·행사 | - | 0/0 | 도구에서 동료로 — AI 에이전트 자율 성장 프레임워크 |
| d2/2852215 | 660 | 제외/회고·문화·행사 | - | 0/0 | 스펙만 바꾸면 프롬프트가 따라옵니다 - 답변 생성 모델 자동화 파이프라인 |
| d2/7056385 | 666 | 제외/회고·문화·행사 | - | 0/0 | 사람과 AI Agent를 위한 통합 Context Provider 구축 |
| d2/4394359 | 837 | 제외/회고·문화·행사 | - | 0/0 | SNOW의 Automatic Sharding 도입기 |
| d2/3015479 | 644 | 제외/회고·문화·행사 | - | 0/0 | Kelos - 쿠버네티스 네이티브 자율 코딩 에이전트 프레임워크 |
| d2/9227131 | 707 | 제외/회고·문화·행사 | - | 0/0 | End to End 유저 모니터링 RUM 으로 한방에 해결!! |
| d2/3897377 | 830 | 제외/회고·문화·행사 | - | 0/0 | AI 에이전트 회사 차리기: 설립부터 어디서든 동기화까지 |
| d2/2541696 | 7,090 | 추출/실험·활용기 | case_1035 | 0/13 | [AI 해커톤 후기] 코드와 문서만 읽은 LLM은 어떻게 사람과 같은 팀을 1위로 골랐을까 |
| d2/1883072 | 5,150 | 제외/회고·문화·행사 | - | 0/0 | [AI 해커톤 후기] AI 시대의 해커톤과 인간의 역할: AI의 계획과 사람의 전략 |
| d2/5788040 | 11,490 | 추출/문제 해결형 | case_1038, case_1039, case_1040 | 2/23 | VictoriaMetrics 운영기 2편 — 장비 증설 없이 리소스 위기를 해결한 3단계 최적화 전략 |
| d2/4821538 | 11,038 | 추출/실험·활용기 | case_1044, case_1045, case_1046 | 0/29 | [AI 해커톤 후기] AI 해커톤 1위 팀이 AI에게 맡기지 않은 것 |
| d2/0525182 | 17,051 | 추출/실험·활용기 | case_1032, case_1033, case_1034 | 0/28 | 우리 팀만의 vLLM 플러그인 만들기 1편 - 검색 AI 모델 서빙 성능 극대화하기 |
| d2/7337586 | 11,792 | 추출/실험·활용기 | case_1026, case_1027, case_1028 | 0/24 | 우리 팀만의 vLLM 플러그인 만들기 2편 - 모델 변환부터 배포까지 AI-native로 자동화하기 |
| d2/4452165 | 13,807 | 추출/실험·활용기 | case_1021 | 0/9 | Python의 멀티프로세싱과 Airflow, 그리고 관련된 문제 해결기 1편 |
| d2/7314597 | 17,141 | 추출/문제 해결형 | case_1020 | 0/14 | Hive는 잊으려 했지만, Spark는 기억하고 있었다: 사라진 get_table RPC 복원기 |
| d2/8118359 | 607 | 제외/개념·튜토리얼 | - | 0/0 | 에이전트, 개념부터 같이 정리해봐요 - 워크플로우 · 하네스 · Context/Memory · MCP/A2A |
| kakao/599 | 1,912 | 추출/실험·활용기 | case_0884 | 0/6 | Trident: 딥러닝 모델 개발을 위한 도구 |
| kakao/600 | 648 | 제외/회고·문화·행사 | - | 0/0 | 카카오 안정성 보고서(Kakao Reliability Report) 발간 |
| kakao/601 | 3,137 | 제외/회고·문화·행사 | - | 0/0 | 제3회 Kakao Tech Meet 후기 - 불확정성에서 감동까지 |
| kakao/602 | 1,683 | 제외/회고·문화·행사 | - | 0/0 | 신뢰성 있는 카프카 애플리케이션을 만드는 3가지 방법 / 제3회 Kakao Tech Meet |
| kakao/603 | 1,470 | 제외/회고·문화·행사 | - | 0/0 | 폭증하는 카카오톡 트래픽에 대처하는 방법 / 제3회 Kakao Tech Meet |
| kakao/604 | 2,390 | 제외/회고·문화·행사 | - | 0/0 | DKAPTCHA: 지도 이미지와 음성을 활용한 어뷰징 방지 전략 / 제3회 Kakao Tech Meet |
| kakao/605 | 22,040 | 추출/문제 해결형 | case_0885 | 0/10 | CommonJS에서 ESM으로 전환하기 |
| kakao/606 | 9,066 | 제외/회고·문화·행사 | - | 0/0 | 2024 카카오 채용 연계형 겨울 인턴십 Coming soon! |
| kakao/607 | 2,146 | 제외/회고·문화·행사 | - | 0/0 | 제4회 Kakao Tech Meet에 초대합니다! |
| kakao/608 | 962 | 제외/회고·문화·행사 | - | 0/0 | JDK 21의 신기능 Virtual Thread 알아보기 / 제4회 Kakao Tech Meet |
| kakao/609 | 1,689 | 제외/회고·문화·행사 | - | 0/0 | 큐라스: 메시지 광고 추천 플랫폼 / 제4회 Kakao Tech Meet |
| kakao/610 | 7,083 | 제외/개념·튜토리얼 | - | 0/0 | 2024 카카오 겨울 인턴십 코딩테스트 문제해설 |
| kakao/611 | 22,139 | 추출/실험·활용기 | case_0881 | 0/11 | OROR Forge: Figma to Code 도구 제작기 (1) 디자인을 코드로 만들어보자! |
| kakao/612 | 11,555 | 추출/실험·활용기 | case_0882 | 0/10 | OROR Forge: Figma to Code 도구 제작기 (2) 실전용으로 만들기 |
| kakao/613 | 2,842 | 제외/회고·문화·행사 | - | 0/0 | 테크밋 다시 달릴 준비! |
| kakao/614 | 2,601 | 제외/회고·문화·행사 | - | 0/0 | 제5회 Kakao Tech Meet에 초대합니다! |
| kakao/615 | 1,545 | 제외/회고·문화·행사 | - | 0/0 | [Phocus] 사용자 경험 중심 스벨트 이미지 뷰어 라이브러리 / 제5회 Kakao Tech Meet |
| kakao/616 | 1,290 | 제외/회고·문화·행사 | - | 0/0 | 웹 텍스트 에디터 개발에 필요한 고민과 신규 에디터 소개 / 제5회 Kakao Tech Meet |
| kakao/617 | 1,640 | 제외/회고·문화·행사 | - | 0/0 | Chrome Devtools를 활용하여 나만의 웹뷰 디버깅 환경 만들기 / 제5회 Kakao Tech Meet |
| kakao/618 | 19,997 | 추출/문제 해결형 | case_0886 | 0/12 | Golang GC 튜닝 가이드 |
| kakao/619 | 2,306 | 제외/회고·문화·행사 | - | 0/0 | 제6회 Kakao Tech Meet에 초대합니다! |
| kakao/620 | 102 | 제외/회고·문화·행사 | - | 0/0 | 구름톤유니브 2기 벚꽃톤! 현장 스케치 |
| kakao/621 | 1,318 | 제외/회고·문화·행사 | - | 0/0 | KCC2024 “Kakao Tech Workshop”에서 만나요! |
| kakao/622 | 8,503 | 추출/문제 해결형 | case_0876 | 0/9 | 코틀린을 활용한 안전한 효과 처리 |
| kakao/623 | 8,217 | 추출/문제 해결형 | case_0883 | 0/11 | 이미지 분류 모델 개발, 아직도 데이터만 기다려? |
| kakao/624 | 787 | 제외/회고·문화·행사 | - | 0/0 | 카카오의 스팸 메일 대응 전략: 문자열 변형 CASE STUDY / 제6회 Kakao Tech Meet |
| kakao/625 | 1,100 | 제외/회고·문화·행사 | - | 0/0 | 이미지 기반 스팸 대응을 위한 카카오의 AI 기술 활용 / 제6회 Kakao Tech Meet |
| kakao/626 | 1,958 | 제외/회고·문화·행사 | - | 0/0 | 스팸 콘텐츠 대응을 위한 카카오의 대규모 언어 모델(LLM) 도입 사례 / 제6회 Kakao Tech Meet |
| kakao/627 | 6,549 | 추출/문제 해결형 | case_0880 | 0/10 | 주니어 FE 개발자의 색상 추출 라이브러리 개발기 |
| kakao/628 | 3,003 | 제외/회고·문화·행사 | - | 0/0 | 카카오테크 부트캠프 2024 입과식, 인재들의 첫 걸음 🎊 |
| kakao/629 | 7,578 | 제외/회고·문화·행사 | - | 0/0 | 2024 카카오 인턴십 뉴크루들의 기술온보딩 여정 |
| kakao/630 | 9,776 | 제외/회고·문화·행사 | - | 0/0 | 모든 기술은 처음이 있었다 - 카카오테크가 만난 Andi Gutmans |
| kakao/631 | 5,456 | 제외/회고·문화·행사 | - | 0/0 | AI 시대와 로봇 - 카카오테크가 만난 조규진 교수님 |
| kakao/632 | 31,210 | 추출/실험·활용기 | case_0877, case_0878, case_0879 | 0/24 | 아파치 플링크와 CDC의 만남. 플링크 CDC 맛보기 |
| kakao/681 | 43,802 | 추출/문제 해결형 | case_0873, case_0874, case_0875 | 0/24 | Journey with Apache Flink & Flink CDC |
| kakao/633 | 6,684 | 제외/개념·튜토리얼 | - | 0/0 | LLM, 더 저렴하게, 더 빠르게, 더 똑똑하게 |
| kakao/635 | 2,506 | 제외/회고·문화·행사 | - | 0/0 | Spring Boot Meet Up, 카카오테크가 만난 Josh Long |
| kakao/636 | 502 | 제외/회고·문화·행사 | - | 0/0 | 모든 연결을 새롭게, if(kakaoAI)2024 |
| kakao/634 | 17,114 | 추출/실험·활용기 | case_0869 | 0/11 | 효율적인 VMWare 인프라 운영을 위한 최적의 VM 집적도 테스트 |
| kakao/637 | 16,286 | 추출/실험·활용기 | case_0872 | 0/11 | 効率的な VMWare インフラ運用のための最適な VM 密度テスト |
| kakao/638 | 29,539 | 추출/실험·활용기 | case_0868 | 0/11 | Optimal VM Density Testing for Efficient VMWare Infrastructure Operation |
| kakao/639 | 4,105 | 제외/회고·문화·행사 | - | 0/0 | KCC2024 후기(1) 첫 외부 발표 준비와 발표 PM 진행기 |
| kakao/640 | 3,918 | 제외/회고·문화·행사 | - | 0/0 | KCC2024 후기(2) 무대의 주역, 발표 세션! |
| kakao/641 | 5,956 | 제외/회고·문화·행사 | - | 0/0 | if(kakaoAI)2024 기술 세션 찾아보기 (날짜별) |
| kakao/642 | 6,790 | 제외/회고·문화·행사 | - | 0/0 | if(kakao AI)2024 첫째 날, 기술 세션 소개 |
| kakao/643 | 8,440 | 제외/회고·문화·행사 | - | 0/0 | if(kakaoAI)2024 둘째 날, 기술 세션 소개 |
| kakao/644 | 7,765 | 제외/회고·문화·행사 | - | 0/0 | if(kakaoAI)2024 셋째 날, 기술 세션 소개 |
| kakao/645 | 2,498 | 제외/회고·문화·행사 | - | 0/0 | if(kakaoAI)2024 크루 패널톡을 소개합니다 |
| kakao/646 | 3,966 | 제외/회고·문화·행사 | - | 0/0 | if(kakaoAI)2024 기술 세션 찾아보기 (주제별) |
| kakao/647 | 9,676 | 제외/회고·문화·행사 | - | 0/0 | if(kakaoAI)2024, AI 기술 세션 소개 |
| kakao/648 | 3,008 | 제외/회고·문화·행사 | - | 0/0 | if(kakaoAI)2024, Backend 기술 세션 소개 |
| kakao/649 | 2,058 | 제외/회고·문화·행사 | - | 0/0 | if(kakaoAI)2024, Cloud 기술 세션 소개 |
| kakao/650 | 2,774 | 제외/회고·문화·행사 | - | 0/0 | if(kakaoAI)2024, Data 기술 세션 소개 |
| kakao/651 | 1,018 | 제외/회고·문화·행사 | - | 0/0 | if(kakaoAI)2024, DevOps 기술 세션 소개 |
| kakao/652 | 2,731 | 제외/회고·문화·행사 | - | 0/0 | if(kakaoAI)2024, FrontEnd 기술 세션 소개 |
| kakao/653 | 1,616 | 제외/회고·문화·행사 | - | 0/0 | if(kakaoAI)2024, Infra/Network, 그 외 세션 소개 |
| kakao/654 | 2,990 | 제외/회고·문화·행사 | - | 0/0 | if(kakaoAI)2024, Mobile 기술 세션 소개 |
| kakao/655 | 5,837 | 제외/회고·문화·행사 | - | 0/0 | Kakao AI Native - CTO Keynote |
| kakao/656 | 67,193 | 추출/실험·활용기 | case_0870, case_0871 | 0/22 | Apache Iceberg와 Flink CDC 심층 탐구 |
| kakao/668 | 98,565 | 추출/실험·활용기 | case_0866, case_0867 | 0/20 | Deep Dive into Apache Iceberg with Flink CDC |
| kakao/657 | 3,796 | 제외/회고·문화·행사 | - | 0/0 | [if(kakaoAI)2024] 내일의 경쟁력이 되는 카카오 AI 이야기 - AI Finance Panel Talk |
| kakao/658 | 4,127 | 제외/회고·문화·행사 | - | 0/0 | [if(kakaoAI)2024] 새로운 유저 라이프를 연결하는 카카오 AI - AI Life Panel Talk |
| kakao/659 | 4,187 | 추출/실험·활용기 | case_0857 | 0/7 | 베네딕트는 왜 이프카카오에서 안성재 성대모사를 했을까? |
| kakao/660 | 3,522 | 제외/기술 선택·도입형 | - | 0/0 | 카카오의 AI 모델, 카나나 모델 패밀리를 소개합니다 |
| kakao/661 | 17,725 | 추출/실험·활용기 | case_0860, case_0861 | 0/18 | 밑바닥부터 Kanana LLM 개발하기: Pre-training |
| kakao/662 | 8,105 | 추출/실험·활용기 | case_0855 | 0/8 | 밑바닥부터 Kanana LLM 개발하기: Post-training |
| kakao/663 | 7,479 | 추출/실험·활용기 | case_0856 | 0/10 | 나만의 프로필 이미지 생성 모델 개발기 |
| kakao/664 | 645 | 제외/회고·문화·행사 | - | 0/0 | 카카오는 어떻게 AI를 일상의 언어로 만들까? |
| kakao/665 | 10,722 | 추출/문제 해결형 | case_0853 | 0/14 | 추가배포 없이 API의 case 통일시키기 |
| kakao/666 | 3,914 | 제외/회고·문화·행사 | - | 0/0 | 대학생 참가자들의 if(kakaoAI)2024 후기 |
| kakao/669 | 2,066 | 제외/회고·문화·행사 | - | 0/0 | 제7회 Kakao Tech Meet에 초대합니다! |
| kakao/671 | 7,726 | 추출/문제 해결형 | case_0849 | 0/12 | Log Aggregation의 진화: 카카오의 Fluentd 대체기 |
| kakao/667 | 17,907 | 추출/실험·활용기 | case_0854 | 0/12 | 이미지도 찰떡같이 이해하는 카카오의 멀티모달 언어모델 Kanana-v 알아보기 |
| kakao/670 | 56,911 | 제외/개념·튜토리얼 | - | 0/0 | MongoDB WiredTiger의 파일 구조 |
| kakao/672 | 3,210 | 제외/회고·문화·행사 | - | 0/0 | [안정성 보고서] 1. 프롤로그: 끊김 없는 서비스를 위한 카카오의 안정성 전략 |
| kakao/673 | 5,319 | 추출/기술 선택·도입형 | case_0846, case_0847, case_0848 | 0/22 | [안정성 보고서] 2. 안정성을 위한 인프라 구축 |
| kakao/674 | 5,727 | 추출/기술 선택·도입형 | case_0844, case_0845 | 0/15 | [안정성 보고서] 3. 안정성을 위한 클라우드 구축 |
| kakao/675 | 13,388 | 추출/실험·활용기 | case_0862, case_0863, case_0864, case_0865 | 0/30 | [안정성 보고서] 4. 안정성을 위한 품질 관리 |
| kakao/676 | 18,995 | 추출/실험·활용기 | case_0850, case_0851, case_0852 | 0/24 | [안정성 보고서] 5. 안정성을 위한 복구 체계 |
| kakao/677 | 7,271 | 제외/기술 선택·도입형 | - | 0/0 | [안정성 보고서] 6. 안정성을 위한 보안과 정보보호 |
| kakao/678 | 15,121 | 추출/문제 해결형 | case_0858, case_0859 | 1/25 | 실시간 메시징 시스템 개발기 - “삽질 과정” |
| kakao/679 | 22,773 | 추출/실험·활용기 | case_0840 | 0/13 | 실시간 메시징 시스템 개발 - “성능 테스트 설계와 분석” |
| kakao/680 | 16,702 | 추출/문제 해결형 | case_0841, case_0842, case_0843 | 0/26 | 실시간 메시징 시스템 개발기 - “성능 개선 레슨런“ |
| kakao/682 | 13,032 | 추출/실험·활용기 | case_0838, case_0839 | 0/20 | 작지만 강한 Kanana Nano 효율적으로 개발하기 |
| kakao/683 | 6,122 | 추출/문제 해결형 | case_0834 | 0/9 | Ingress Nginx Controller의 Prometheus Metric 병목 현상: 원인 분석과 해결 (1부) |
| kakao/684 | 11,773 | 추출/문제 해결형 | case_0825 | 0/9 | Ingress Nginx Controller의 Prometheus Metric 병목 현상: 원인 분석과 해결 (2부) |
| kakao/685 | 25,459 | 추출/문제 해결형 | case_0835, case_0836, case_0837 | 0/30 | 대규모 앵귤러 웹 애플리케이션 성능 최적화: 카카오 챗봇 관리자센터 사례 |
| kakao/686 | 11,847 | 추출/문제 해결형 | case_0826, case_0827, case_0828, case_0829 | 0/27 | 오픈채팅 Lite FE 성능 개선의 모든 것 |
| kakao/687 | 1,672 | 제외/회고·문화·행사 | - | 0/0 | (후원 후기) 전국 장애/비장애 대학생 창업경진대회 |
| kakao/688 | 27,550 | 제외/개념·튜토리얼 | - | 0/0 | MongoDB WiredTiger의 B+Tree |
| kakao/689 | 4,018 | 추출/기술 선택·도입형 | case_0824 | 0/10 | 카카오의 언어모델, Kanana 테크니컬 리포트 공개 |
| kakao/690 | 14,392 | 추출/실험·활용기 | case_0833 | 1/11 | LLM as a Judge를 활용한 CodeBuddy 성능 평가 |
| kakao/691 | 2,585 | 추출/문제 해결형 | case_0813, case_0814, case_0815, case_0816, case_0817, case_0818, case_0819, case_0820 | 0/19 | 2025년 1분기 카카오테크 블로그 글 모음 |
| kakao/692 | 4,073 | 제외/회고·문화·행사 | - | 0/0 | AI Agent와 개발자 - 카카오테크가 만난 Thomas Dohmke |
| kakao/694 | 19,991 | 추출/실험·활용기 | case_0830, case_0831, case_0832 | 0/25 | 로그 유형별 Iceberg 테이블 적재 및 운영 전략 |
| kakao/695 | 37,701 | 추출/실험·활용기 | case_0808, case_0809, case_0810 | 0/29 | Iceberg Operation Journey: Takeaways for DB & Server Logs |
| kakao/696 | 32,718 | 제외/개념·튜토리얼 | - | 0/0 | 바이브 코딩 바이블: AI 에이전트 시대의 새로운 코딩 패러다임 |
| kakao/697 | 3,511 | 제외/회고·문화·행사 | - | 0/0 | Vibe Coding하는 비개발자는 개발자인가(1) |
| kakao/698 | 7,596 | 추출/실험·활용기 | case_0811, case_0812 | 0/19 | Vibe Coding, 새로운 개발 패러다임의 시작일까요? |
| kakao/699 | 4,371 | 추출/실험·활용기 | case_0807 | 0/12 | AI는 어디까지 나를 대체할 수 있나? |
| kakao/700 | 4,833 | 추출/실험·활용기 | case_0806 | 0/9 | Vibe Coding하는 비개발자는 개발자인가(2) |
| kakao/702 | 29,690 | 추출/실험·활용기 | case_0804, case_0805 | 0/21 | 이미지와 음성을 아우르는 카카오의 멀티모달 언어모델 Kanana-o 알아보기 |
| kakao/703 | 14,821 | 제외/개념·튜토리얼 | - | 0/0 | MySQL ALTER DDL 수행 방식에 대한 이해 |
| kakao/706 | 3,691 | 제외/개념·튜토리얼 | - | 0/0 | 더 똑똑해진 카카오의 언어모델 Kanana 1.5, 상업 활용 가능한 오픈소스 공개 |
| kakao/707 | 21,303 | 추출/실험·활용기 | case_0821, case_0822, case_0823 | 1/27 | Kanana LLM 1.5 개발기 |
| kakao/705 | 7,087 | 추출/기술 선택·도입형 | case_0797 | 0/10 | 카카오 AI 가드레일 모델, Kanana Safeguard 시리즈를 소개합니다. |
| kakao/708 | 1,334 | 제외/회고·문화·행사 | - | 0/0 | 카카오, AI와 함께하는 사내 해커톤 '10K' 진행합니다. |
| kakao/709 | 9,450 | 추출/실험·활용기 | case_0796 | 0/10 | CVPR 2025 참관기: 고품질 인물 생성을 위한 HG-DPO 연구 소개 |
| kakao/710 | 6,080 | 추출/문제 해결형 | case_0795 | 0/10 | 바이브 코딩으로 48시간 만에 250명 규모 해커톤 AI 심사 시스템 구축기 |
| kakao/711 | 1,558 | 추출/실험·활용기 | case_0788 | 0/8 | Beyond Vibe Coding to Agentic Coding: 카카오의 AI 협업 개발 실험 |
| kakao/712 | 18,788 | 추출/기술 선택·도입형 | case_0787 | 0/10 | MySQL 인증 플러그인 caching_sha2_password에 대한 이해 |
| kakao/714 | 22,928 | 추출/실험·활용기 | case_0798, case_0799, case_0800 | 0/20 | 카카오의 경량 멀티모달 언어모델 ‘Kanana-1.5-v-3b’ 개발부터 공개까지 |
| kakao/716 | 21,657 | 추출/기술 선택·도입형 | case_0801, case_0802, case_0803 | 0/26 | 국내 최초 MoE 모델 ‘Kanana-MoE’ 개발기 |
| kakao/717 | 17,465 | 추출/실험·활용기 | case_0786 | 0/10 | CDC 파이프라인 정합성 검사 Spark 잡 개발 - Part 1. 코드 설계편 |
| kakao/718 | 12,162 | 추출/문제 해결형 | case_0792, case_0793, case_0794 | 0/26 | CDC 파이프라인 정합성 검사 Spark 잡 개발 - Part 2. Spark 최적화편 |
| kakao/719 | 2,290 | 제외/회고·문화·행사 | - | 0/0 | (인터뷰) AI와 함께 10시간 만에 서비스 개발하기 |
| kakao/721 | 13,255 | 제외/개념·튜토리얼 | - | 0/0 | MySQL InnoDB Log에 대한 이해 - (1) |
| kakao/720 | 3,162 | 추출/실험·활용기 | case_0783 | 0/10 | 카카오 AI가 법인카드 영수증을 처리하는 방법: AI 간편 정산 개발기 |
| kakao/722 | 3,915 | 제외/회고·문화·행사 | - | 0/0 | 해커들의 올림픽, DEFCON 33 CTF 본선 도전기 |
| kakao/724 | 18,201 | 추출/실험·활용기 | case_0789, case_0790, case_0791 | 2/22 | Kanana 언어모델에 추론 기능 붙여보기 (feat. Kanana-1.5) |
| kakao/725 | 1,667 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 컨퍼런스를 개최합니다. |
| kakao/731 | 14,313 | 추출/실험·활용기 | case_0784 | 0/10 | MySQL Ver. 8.0 New Feature: Instant DDL Algorithm에 대한 이해 |
| kakao/735 | 11,351 | 추출/실험·활용기 | case_0779 | 0/11 | AI 시대를 살아갈 개발자들에게 |
| kakao/734 | 27,226 | 추출/실험·활용기 | case_0782 | 0/12 | PlayMCP: 제로부터 시작하는 MCP 플랫폼 개발 |
| kakao/743 | 12,101 | 추출/문제 해결형 | case_0780, case_0781 | 0/16 | Next.js ISR 전환과 Redis 외부 캐싱 (SSR 지옥 탈출기 시리즈 1) |
| kakao/744 | 9,110 | 추출/문제 해결형 | case_0785 | 0/11 | Next.js SSR 서버를 위한 모니터링 시스템 구축 (SSR 지옥 탈출기 시리즈 2) |
| kakao/745 | 730 | 제외/회고·문화·행사 | - | 0/0 | 카카오 AI 앰배서더를 공개 모집합니다. |
| kakao/774 | 8,568 | 추출/기술 선택·도입형 | case_0778 | 0/8 | MySQL Json 데이터 타입의 저장 구조와 성능 비교 |
| kakao/723 | 13,091 | 추출/실험·활용기 | case_0776 | 0/10 | AI를 활용한 요구사항 분석 및 명세화 실전 가이드 |
| kakao/726 | 8,123 | 추출/실험·활용기 | case_0773, case_0774, case_0775 | 0/27 | AI 도구를 활용한 아이디어 검증 및 개발 플로우 혁신 |
| kakao/727 | 6,275 | 추출/실험·활용기 | case_0762 | 0/10 | 바이브코딩의 시작: 데이터 분석과 웹 시각화 |
| kakao/728 | 16,564 | 추출/실험·활용기 | case_0777 | 0/12 | AI 에디터 활용 사례 및 개발 생산성 |
| kakao/729 | 8,651 | 추출/실험·활용기 | case_0772 | 0/11 | AI와 함께 안전하게 리팩토링하기: 테스트부터 반복 개선까지 |
| kakao/730 | 4,325 | 제외/개념·튜토리얼 | - | 0/0 | 실시간 코드 리뷰 및 품질 관리: AI 도입의 필요성과 기대 효과 |
| kakao/732 | 10,874 | 제외/개념·튜토리얼 | - | 0/0 | 실시간 코드 리뷰 및 품질 관리: AI 기반 정적 분석 기술 |
| kakao/733 | 7,966 | 추출/실험·활용기 | case_0771 | 0/10 | 실시간 코드 리뷰 및 품질 관리: 단위 테스트 자동 생성을 통한 코드 품질 향상 |
| kakao/736 | 6,827 | 추출/실험·활용기 | case_0761 | 0/10 | AI 기반 API 테스트 자동화의 필요성과 TestLAB AI |
| kakao/737 | 5,491 | 추출/실험·활용기 | case_0760 | 0/10 | DeviceFarm AI를 사용한 QA 테스트 자동화 |
| kakao/738 | 2,076 | 제외/개념·튜토리얼 | - | 0/0 | 내가 쓴 글은 어디로 갈까?: 콘텐츠가 거치는 보이지 않는 여정 |
| kakao/739 | 4,395 | 추출/실험·활용기 | case_0756 | 0/10 | 텍스트 콘텐츠의 수호자: 모니터링 보조 LLM의 이야기 |
| kakao/740 | 10,754 | 추출/문제 해결형 | case_0754, case_0755 | 0/16 | 유해 이미지 분류 시스템 구축기 |
| kakao/741 | 13,492 | 추출/기술 선택·도입형 | case_0757, case_0758, case_0759 | 0/25 | AI의 자기 보호 시스템: AI 가드레일 |
| kakao/742 | 9,229 | 추출/문제 해결형 | case_0763, case_0764, case_0765 | 0/21 | AI 데브옵스 시스템, 카카오릴리즈 |
| kakao/746 | 7,603 | 제외/회고·문화·행사 | - | 0/0 | [목차] AI Native: 실행과 확산 사례집 |
| kakao/747 | 12,657 | 추출/실험·활용기 | case_0766, case_0767, case_0768, case_0769, case_0770 | 0/31 | 분산 추적 기반 AI 운영 생태계 |
| kakao/753 | 5,728 | 추출/실험·활용기 | case_0748, case_0749 | 0/17 | AI 협업을 위한 개발 환경과 평가 시스템 |
| kakao/756 | 2,566 | 제외/회고·문화·행사 | - | 0/0 | 에이전틱 코딩 가이드북, 그리고 AI 협업 치트 시트와 표준 룰셋 공유 시스템 |
| kakao/758 | 3,269 | 제외/회고·문화·행사 | - | 0/0 | 전사 AI 역량 강화를 위한 맞춤형 내부 교육 프로그램 |
| kakao/759 | 5,079 | 추출/기술 선택·도입형 | case_0740 | 0/9 | AI 윤리 원칙과 AI 리스크 관리 프레임워크 |
| kakao/761 | 3,645 | 제외/회고·문화·행사 | - | 0/0 | 실패를 장려하는 실험적 문화 |
| kakao/762 | 13,811 | 제외/회고·문화·행사 | - | 0/0 | 생산성 혁신의 실험: AI 마일리지 프로그램 |
| kakao/766 | 8,041 | 추출/실험·활용기 | case_0742, case_0743 | 0/18 | [칼럼] 오픈소스기술의 AI 네이티브 전환 성공 사례 |
| kakao/770 | 16,500 | 추출/기술 선택·도입형 | case_0744 | 0/13 | 5년 된 프로젝트의 빌드 도구를 교체하며 얻은 것들 |
| kakao/775 | 11,009 | 추출/기술 선택·도입형 | case_0745, case_0746, case_0747 | 0/23 | MySQL Orchestrator 기반의 새로운 HA 표준 개발기 |
| kakao/776 | 13,270 | 추출/기술 선택·도입형 | case_0741 | 0/13 | PostgreSQL to ES: (1) Kafka Connect CDC 파이프라인 구성 |
| kakao/777 | 12,030 | 추출/문제 해결형 | case_0750, case_0751, case_0752, case_0753 | 0/29 | PostgreSQL to ES: (2) Kafka Connect 트러블슈팅 |
| kakao/778 | 14,716 | 제외/개념·튜토리얼 | - | 0/0 | MySQL DATETIME, TIMESTAMP 데이터 타입에 대한 분석 |
| kakao/779 | 4,378 | 제외/기술 선택·도입형 | - | 0/0 | Agentic AI를 향한 카나나 모델의 진화 |
| kakao/781 | 941 | 제외/회고·문화·행사 | - | 0/0 | 카카오 x 한국정보과학회 AI 에이전트 경진대회를 개최합니다. |
| kakao/783 | 1,144 | 제외/회고·문화·행사 | - | 0/0 | 한국인사관리학회에서 공유한 ‘AI 네이티브 전환’ |
| kakao/782 | 6,476 | 제외/회고·문화·행사 | - | 0/0 | (FAQ) 카카오 x 한국정보과학회 AI 에이전트 경진대회 |
| kakao/784 | 8,710 | 제외/실험·활용기 | - | 0/0 | 단 1시간 만에 99개의 MVP가? AI와 함께한 1K: 바이브코딩전 생생 후기 |
| kakao/785 | 4,597 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 Krew Day AI Talk Lounge: AI 시대의 기회와 고민을 논하며 |
| kakao/787 | 2,131 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 Krew Day FE 패널톡: 혈관에 피 대신 철(Fe)이 흐르는 FE 개발자들의 이야기 |
| kakao/788 | 3,966 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 Krew Day AI 패널톡: AI 시대의 개발, 인프라, 전략 (외부 연사 초청 세션) |
| kakao/790 | 4,469 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 Krew Day CTO 패널톡: 7명의 카카오 공동체 CTO가 말하는 AI 시대의 카카오 |
| kakao/789 | 7,914 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 Krew Day Demo Station 생생한 현장 스케치 |
| kakao/793 | 9,348 | 제외/회고·문화·행사 | - | 0/0 | 카카오 그룹사 기술 공유의 장, Krew Day |
| kakao/791 | 3,681 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)25 정규돈 CTO 키노트 후기 |
| kakao/795 | 2,841 | 제외/실험·활용기 | - | 0/0 | POPM 과정은 어떻게 하나의 ‘제품’이 되었나 |
| kakao/796 | 3,307 | 제외/회고·문화·행사 | - | 0/0 | 우리가 진짜 문제를 풀고 있었을까? — POPM 과정이 남긴 질문 |
| kakao/797 | 11,491 | 제외/회고·문화·행사 | - | 0/0 | [AI_TOP_100] 문제 출제 후기 – 기술이 아닌, 사람을 묻다. |
| kakao/798 | 9,810 | 추출/문제 해결형 | case_0730, case_0731, case_0732 | 0/19 | YEYE가 지켜보고 있다–카카오의 공격 표면 관리 이야기 |
| kakao/799 | 23,731 | 추출/실험·활용기 | case_0726 | 0/13 | AI TOP 100이 우리에게 남긴 것들 |
| kakao/801 | 20,231 | 추출/실험·활용기 | case_0725 | 0/10 | ​한국어와 이미지를 한 번에, 카카오의 멀티모달 임베딩 모델 개발기 |
| kakao/802 | 32,228 | 추출/문제 해결형 | case_0738, case_0739 | 0/19 | 더욱 똑똑하게 답하며, 더욱 풍부한 감정표현을 향한 Kanana-o의 진화 과정 |
| kakao/803 | 34,496 | 추출/기술 선택·도입형 | case_0724 | 1/11 | MongoDB 8.0 업그레이드 해야하는 12가지 이유 |
| kakao/804 | 3,760 | 제외/실험·활용기 | - | 0/0 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/805 | 8,675 | 추출/문제 해결형 | case_0712, case_0713 | 0/18 | 초경량 클래식 형태소 분석기 개발기 |
| kakao/806 | 45,303 | 추출/실험·활용기 | case_0727, case_0728, case_0729 | 0/23 | “생각하고 답변하는” 카카오의 하이브리드 멀티모달 언어모델, Kanana-v-4b-hybrid 개발기 |
| kakao/807 | 17,307 | 추출/기술 선택·도입형 | case_0717, case_0718, case_0719 | 0/26 | Kanana-2 개발기 (1): Pre-training에서의 의사결정들을 중심으로 |
| kakao/808 | 29,110 | 추출/기술 선택·도입형 | case_0721, case_0722, case_0723 | 0/23 | Kanana-2 개발기 (2): 개선된 post-training recipe를 중심으로 |
| kakao/809 | 1,548 | 제외/회고·문화·행사 | - | 0/0 | 카카오 AI 앰배서더 ‘KANANA 429 앰배서더’를 신규 모집합니다. |
| kakao/810 | 14,550 | 추출/문제 해결형 | case_0720 | 1/16 | 잃어버린 리포트를 찾아서: 카카오 메시징 시스템의 경쟁 조건 문제와 안티 패턴 제거 과정 |
| kakao/811 | 1,575 | 제외/기술 선택·도입형 | - | 0/0 | Kanana-o 신규 모델 및 API 베타 서비스를 공개합니다. |
| kakao/812 | 35,365 | 추출/실험·활용기 | case_0733, case_0734, case_0735, case_0736, case_0737 | 0/41 | 한국 문화 이해부터 화면 조작까지: Kanana-V 기능 확장의 모든 것 |
| kakao/813 | 10,736 | 제외/개념·튜토리얼 | - | 0/0 | 2026 카카오그룹 신입크루 공채 코딩테스트 1차 문제해설 |
| kakao/814 | 8,106 | 제외/개념·튜토리얼 | - | 0/0 | 2026 카카오그룹 신입크루 공채 코딩테스트 2차 문제해설 |
| kakao/815 | 5,840 | 제외/회고·문화·행사 | - | 0/0 | 학생에서 개발자로: DB, 보안부터 AI까지, 정답보다 합리적인 선택을 배우다 |
| kakao/816 | 8,762 | 추출/실험·활용기 | case_0709, case_0710, case_0711 | 0/23 | 학생에서 개발자로: 로또 구현부터 레거시 개선까지, 서버의 흐름을 배우다 |
| kakao/817 | 9,197 | 추출/실험·활용기 | case_0708 | 0/17 | 수억 건의 보안 신호 속 진짜 위협 찾기 — AI로 보안 모니터링의 패러다임을 바꾸다 |
| kakao/819 | 2,776 | 제외/회고·문화·행사 | - | 0/0 | 카나나 스칼라 1회 세미나 현장 스케치 |
| kakao/820 | 4,989 | 추출/문제 해결형 | case_0699 | 0/7 | 카카오톡 예약하기에서 그려 본 캘린더 |
| kakao/821 | 11,335 | 추출/문제 해결형 | case_0714, case_0715, case_0716 | 0/31 | 음성 AI 모델을 프로덕션에 올리기까지: Kanana-O 서빙 최적화 여정 |
| kakao/822 | 20,047 | 추출/실험·활용기 | case_0700, case_0701 | 0/21 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakao/818 | 4,821 | 제외/회고·문화·행사 | - | 0/0 | 에이전틱 AI 생태계의 주인공들, MCP Player 10 성료와 Next! |
| kakao/823 | 5,040 | 추출/실험·활용기 | case_0707 | 0/13 | Vibe Coding하는 비개발자는 개발자인가(3) |
| kakao/824 | 6,600 | 추출/실험·활용기 | case_0697 | 0/12 | AI 에이전트로 카카오톡 추천 지표 분석 자동화하기 |
| kakao/825 | 3,033 | 제외/회고·문화·행사 | - | 0/0 | 개발을 넘어 AI로 사회문제를 해결하다 |
| kakao/826 | 27,115 | 추출/기술 선택·도입형 | case_0704, case_0705, case_0706 | 0/34 | 더 작고 강해진 Kanana SLM 개발 |
| kakao/827 | 25,116 | 추출/문제 해결형 | case_0702, case_0703 | 1/19 | 잘 말하는 AI를 넘어, 원하는 대로 말하는 AI로: Kanana-o 음성 생성 고도화 과정 |
| kakao/828 | 48,105 | 추출/실험·활용기 | case_0695, case_0696 | 0/20 | Beyond AI That Speaks Well: Making Kanana-o Speak the Way Users Want |
| kakao/829 | 14,946 | 추출/문제 해결형 | case_0698 | 0/18 | 개인화된 Airflow 테스트 환경 구축 및 운영 경험 |
| kakao/830 | 1,223 | 제외/회고·문화·행사 | - | 0/0 | 지역 AI 생태계의 새로운 가능성, 카카오 AI 돛 Summit 26을 개최합니다! |
| kakao/831 | 10,756 | 추출/기술 선택·도입형 | case_0694 | 0/13 | 같은 장애를 두 번 겪지 않기 위해, 배포 전에 리뷰합니다 — KRIS 개발기 |
| kakao/832 | 435 | 제외/회고·문화·행사 | - | 0/0 | 곧, if(kakao)26의 이야기가 시작됩니다. |
| kakao/834 | 2,059 | 제외/회고·문화·행사 | - | 0/0 | 카카오, if(kakao)26 컨퍼런스 개최... 모든 연결에 지능을 |
| kakao/833 | 8,370 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 첫째 날, 기술 세션 소개 |
| kakao/835 | 12,198 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26 둘째 날, 기술 세션 소개 |
| kakao/836 | 3,327 | 제외/회고·문화·행사 | - | 0/0 | if(kakao)26에서 네트워킹하는 법 |
| kakao/837 | 7,203 | 추출/기술 선택·도입형 | case_0693 | 0/13 | 개인화 추천을 위한 랭킹 모델 개발기 |
| kakaopay/kakaopay-techlog | 9,885 | 추출/기술 선택·도입형 | case_1016 | 0/12 | 카카오페이 기술 블로그는 어떻게 만들었을까요? |
| kakaopay/spring-batch-performance | 12,920 | 추출/문제 해결형 | case_1017, case_1018 | 0/18 | Spring Batch 애플리케이션 성능 향상을 위한 주요 팁 |
| kakaopay/bluetooth-remittance | 9,787 | 추출/문제 해결형 | case_1029, case_1030, case_1031 | 4/18 | 내 주변 송금이 블루투스로 만들어졌다고? |
| kakaopay/how-to-work-with-legacy-library | 7,607 | 추출/문제 해결형 | case_1022, case_1023, case_1024, case_1025 | 0/24 | 멀고도 험난했던 개발 지원이 중단된 Library 연동 과정 |
| kakaopay/kakaopay-techlog-2 | 6,235 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이 기술 블로그 월 평균 방문자 수 10,000명을 넘기까지 |
| kakaopay/kakaopay-payment-patent | 5,554 | 추출/기술 선택·도입형 | case_1019 | 0/13 | 끊김없는 게임 플레이를 실현한 카카오페이 결제 특허 |
| kakaopay/react-router-dom-csr-prefetch | 10,176 | 추출/문제 해결형 | case_1011 | 0/11 | CSR 환경에서 Suspense로 발생한 문제 해결하고 성능 개선하기 |
| kakaopay/sre-re-pylon | 9,488 | 추출/문제 해결형 | case_1014 | 0/10 | AWX를 이용한 CI/CD Pipeline: Pylon |
| kakaopay/kotlin-migration | 6,396 | 추출/기술 선택·도입형 | case_1013 | 0/10 | 자바 프로젝트 3개 코틀린 점진적 전환기(feat. lombok 됩니다.) |
| kakaopay/improve-service-performance | 11,884 | 추출/문제 해결형 | case_1015 | 0/14 | 카카오페이 온라인 결제 서비스 2.5배 성능 개선기 |
| kakaopay/paytalks-with-krew-fe | 14,160 | 제외/회고·문화·행사 | - | 0/0 | FE 리더가 되어버린 나, 이대로 괜찮은가?: 시니어 개발자인 내가 주니어 매니저가 되어 버린 건에 대하여 |
| kakaopay/make-http-client-design-flexible | 16,996 | 추출/기술 선택·도입형 | case_1012 | 0/13 | MSA 환경에서의 유연한 HTTP 클라이언트 설계 전략 |
| kakaopay/cloud-cost-visualization | 13,111 | 추출/문제 해결형 | case_0998 | 0/10 | 클라우드 비용 가시화 그렇게 어렵지 않아요! |
| kakaopay/kakaopaysec-devops-platform | 11,115 | 추출/실험·활용기 | case_1004, case_1005 | 0/15 | 카카오페이증권이 생각하는 DevOps문화와 Platform Engineering의 방향성 |
| kakaopay/spring-and-ktor | 12,302 | 추출/기술 선택·도입형 | case_0999 | 0/12 | Spring 공화국에서 Ktor 사용하기 |
| kakaopay/implementing-tdd-in-practical-applications | 16,086 | 추출/실험·활용기 | case_0997 | 0/11 | 실전에서 TDD하기 |
| kakaopay/2023-aws-reinvent-1 | 11,498 | 제외/회고·문화·행사 | - | 0/0 | AWS re:Invent 2023, 관심 세션을 중심으로 (1편): Aurora DB, Amplify |
| kakaopay/2023-aws-reinvent-2 | 12,545 | 제외/회고·문화·행사 | - | 0/0 | AWS re:Invent 2023, 관심 세션을 중심으로 (2편): Cost Optimization, Observability |
| kakaopay/kakaopaysec-mongodb-cdc | 17,302 | 추출/문제 해결형 | case_1002, case_1003 | 0/24 | Oracle에서 MongoDB로의 CDC Pipeline 구축 |
| kakaopay/eco-ami | 14,210 | 추출/문제 해결형 | case_1006, case_1007 | 0/20 | 환경미화 프로젝트(부제: 카카오페이 k8s에서 낭비되는 자원을 절약해 보자!) |
| kakaopay/kakaopaysec-redis-on-kubernetes | 18,205 | 추출/기술 선택·도입형 | case_1008, case_1009, case_1010 | 0/24 | Redis on Kubernetes 플랫폼을 구성해 나가기 |
| kakaopay/dion-interactive-animation | 9,742 | 추출/실험·활용기 | case_0996 | 0/9 | API 없이 웹 애니메이션 구현: 인터랙티브 웹 개발 1편 |
| kakaopay/katfun-joy-multiple-biz-partner-01 | 13,120 | 추출/문제 해결형 | case_0994, case_0995 | 0/17 | 여러 제휴사와 연동하는 신규 프로젝트 개발기 1편 |
| kakaopay/katfun-joy-multiple-biz-partner-02 | 18,559 | 추출/문제 해결형 | case_1000, case_1001 | 0/15 | 여러 제휴사와 연동하는 신규 프로젝트 개발기 2편 |
| kakaopay/ios-manage-resources-in-multi-framework | 7,614 | 추출/문제 해결형 | case_0987 | 0/11 | iOS 멀티 프레임워크 환경에서 리소스 효율적으로 관리하기 |
| kakaopay/dion-interactive-animation-2 | 9,279 | 추출/문제 해결형 | case_0991, case_0992 | 0/11 | API 없이 웹 애니메이션 구현: 인터랙티브 웹 개발 2편 |
| kakaopay/kakaopay-dr-03 | 5,823 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이 개발 문화, 다시 고민하기 |
| kakaopay/r2dbc-connection-pool-missing | 20,666 | 추출/문제 해결형 | case_0993 | 0/11 | R2DBC Connection Pool 실종 사건 |
| kakaopay/2024-google-cloud-next-1 | 12,996 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next 2024 참관 후기 1편 - AI로 업그레이드된 구글 클라우드와 우리의 준비 |
| kakaopay/2024-google-cloud-next-2 | 13,997 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next 2024 참관 후기 2편 - Google Cloud Serverless for Java developer |
| kakaopay/2024-google-cloud-next-3 | 15,186 | 추출/실험·활용기 | case_0986 | 0/10 | Google Cloud Next 2024 참관 후기 3편 - Generative AI with Enterprise Data |
| kakaopay/2024-google-cloud-next-4 | 6,635 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next 2024 참관 후기 4편 - AI를 장착한 개발자의 파워풀한 퍼포먼스 내기 |
| kakaopay/mydata-platfrom-improvement | 10,248 | 추출/문제 해결형 | case_0988, case_0989, case_0990 | 0/29 | 마이데이터 플랫폼의 대용량 데이터 처리 개선! 구경 한번 해볼래? |
| kakaopay/slack-bot-improving-operational-efficiency-2 | 5,044 | 추출/문제 해결형 | case_0984 | 0/10 | 카카오페이 배포 효율화 1년 회고: 자동화 도입과 팀 생산성 향상 |
| kakaopay/ro-spring-virtual-thread | 7,946 | 추출/기술 선택·도입형 | case_0985 | 0/9 | [Project Loom] Virtual Thread에 봄(Spring)은 왔는가 |
| kakaopay/tech-strategy-tpm | 9,673 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이 TPM은 어떤 일을 하나요? |
| kakaopay/how-to-simplify-kakaopay-testing-using-a-common-mock-server | 7,421 | 추출/기술 선택·도입형 | case_0981 | 0/10 | 사내 공통 목서버로 카카오페이 테스트 진입 장벽 낮추기 |
| kakaopay/given-test-code | 11,384 | 추출/실험·활용기 | case_0982 | 0/10 | 실무에서 적용하는 테스트 코드 작성 방법과 노하우 Part 3: Given 지옥에서 벗어나기 - 객체 기반 데이터 셋업의 한계 |
| kakaopay/jack-k8s-internals-part-1 | 9,222 | 제외/개념·튜토리얼 | - | 0/0 | 쓰기만 했던 개발자가 궁금해서 찾아본 쿠버네티스 내부 1편 |
| kakaopay/slack-angmondbot | 8,225 | 추출/실험·활용기 | case_0983 | 0/13 | 사내 기술 공유 슬랙봇 앙몬드 개발기 |
| kakaopay/slack-angmondbot-2 | 7,406 | 추출/문제 해결형 | case_0975, case_0976 | 0/15 | 분산 시스템 환경에서의 슬랙봇 앙몬드 개발기 |
| kakaopay/jack-k8s-internals-part-2 | 11,963 | 제외/개념·튜토리얼 | - | 0/0 | 쓰기만 했던 개발자가 궁금해서 찾아본 쿠버네티스 내부 2편 |
| kakaopay/cilium-egress-gateway | 13,218 | 추출/기술 선택·도입형 | case_0979 | 0/10 | 카카오페이증권의 Egress Gateway |
| kakaopay/katfun-joy-kotlin | 14,709 | 추출/실험·활용기 | case_0977 | 0/9 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kakaopay/devsecops_sonarqube | 10,850 | 추출/실험·활용기 | case_0980 | 0/8 | DevSecOps를 위한 한걸음: Sonarqube를 활용한 지속적인 코드 품질 및 보안 관리 |
| kakaopay/url-is-strange | 15,372 | 추출/문제 해결형 | case_0978 | 1/10 | URL이 이상해요! Java와 Spring 중 범인은 누구? |
| kakaopay/podo-elk-threadcontext-part-1 | 13,341 | 추출/문제 해결형 | case_0970 | 0/9 | ELK 환경에서 좀 더 정교한 이슈 트래킹 Part1 - 이슈 트래킹 기반 마련하기 |
| kakaopay/podo-elk-threadcontext-part-2 | 15,379 | 추출/문제 해결형 | case_0973, case_0974 | 0/16 | ELK 환경에서 좀 더 정교한 이슈 트래킹 Part2 - Thread Context 적극 활용하기 |
| kakaopay/podo-elk-threadcontext-part-3 | 16,981 | 추출/문제 해결형 | case_0968, case_0969 | 0/17 | ELK 환경에서 좀 더 정교한 이슈 트래킹 Part3 - Multi Thread Context 적극 활용하기 |
| kakaopay/troubleshooting-logs-as-a-junior-developer | 10,053 | 추출/문제 해결형 | case_0965, case_0966, case_0967 | 0/24 | 주니어 서버 개발자가 유저향 서비스를 개발하며 마주쳤던 이슈와 해결 방안 |
| kakaopay/payment-feed-server | 19,016 | 추출/문제 해결형 | case_0971, case_0972 | 0/15 | 콘텐츠를 조립하는 결제탭 피드 서버의 코드 아키텍처 |
| kakaopay/coroutine_virtual_thread_wayne | 11,238 | 추출/기술 선택·도입형 | case_0960 | 0/10 | 코루틴과 Virtual Thread 비교와 사용 |
| kakaopay/way-to-functional-programming | 28,956 | 추출/실험·활용기 | case_0959 | 0/10 | 코틀린 함수형 프로그래밍의 길을 찾아서 |
| kakaopay/ifkakao2024-devrel | 10,598 | 제외/회고·문화·행사 | - | 0/0 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스 준비 맛보기 |
| kakaopay/ifkakao2024-dr-pym-project | 12,897 | 추출/문제 해결형 | case_0958 | 0/12 | [if(kakaoAI)2024] 카카오페이증권의 Kubernetes 지능형 리소스 최적화 (feat. Dr.Pym Project 공유) |
| kakaopay/ifkakao2024-delayed-transfer | 8,687 | 추출/문제 해결형 | case_0961 | 1/15 | 지연이체 서비스 개발기: 은행 점검 시간 끝나면 송금해 드릴게요! (feat. 발표 후기) |
| kakaopay/perftest_zone | 4,708 | 추출/기술 선택·도입형 | case_0957 | 0/11 | 카카오페이 성능 테스트 존을 소개합니다. |
| kakaopay/ifkakao2024-architecture-migration-for-ceo-app | 6,782 | 추출/기술 선택·도입형 | case_0956 | 0/12 | 사장님플러스 앱 아키텍처 전환 이후에 대하여 |
| kakaopay/ifkakao2024-document-ai | 7,367 | 추출/실험·활용기 | case_0952 | 0/10 | Document AI로 문서 검토 한방에 끝내기 |
| kakaopay/ifkakao2024-instant-insurance-claim-payment | 9,173 | 추출/문제 해결형 | case_0962, case_0963, case_0964 | 0/25 | 사고접수와 동시에 보험금을 받는다면? |
| kakaopay/ifkakao2024-fds | 6,790 | 추출/실험·활용기 | case_0951 | 0/10 | FDS에 지속 성장하는 ML 모델 적용 이야기 |
| kakaopay/coroutine-exceptions-handling | 13,149 | 제외/개념·튜토리얼 | - | 0/0 | 코틀린 코루틴 예외 처리, 어떻게 해야 할까? |
| kakaopay/efficient-logging-with-kotlin | 9,600 | 추출/실험·활용기 | case_0949 | 0/10 | Kotlin 환경에서 로그를 기록할 때 불필요한 문자열 연산을 방지하는 방법 |
| kakaopay/spring-cloud-stream | 16,589 | 추출/기술 선택·도입형 | case_0948 | 0/12 | Spring Cloud Stream 도입하기 |
| kakaopay/local-caching-in-distributed-systems | 12,096 | 추출/기술 선택·도입형 | case_0950 | 0/11 | 분산 시스템에서 로컬 캐시 활용하기 |
| kakaopay/home-hexagonal-architecture | 11,913 | 추출/문제 해결형 | case_0947 | 0/12 | Hexagonal Architecture, 진짜 하실 건가요? |
| kakaopay/jpa-transactional-bri | 13,961 | 추출/문제 해결형 | case_0946 | 0/11 | JPA Transactional 잘 알고 쓰고 계신가요? |
| kakaopay/choonsiri | 15,908 | 추출/실험·활용기 | case_0942 | 0/11 | 페이증권의 업무도우미 AI봇을 소개합니다! 근데 이제 춘식이를 곁들인 |
| kakaopay/ios-mapkit | 13,908 | 추출/문제 해결형 | case_0953, case_0954, case_0955 | 0/22 | MapKit을 활용한 위치 기반 서비스를 개발하며 겪은 시행착오 |
| kakaopay/spring-multi-module-environment-variable | 15,712 | 추출/기술 선택·도입형 | case_0939 | 0/13 | Spring 기반 멀티모듈 프로젝트 환경변수 설정 방법 |
| kakaopay/ideavim-set-shell | 7,653 | 추출/실험·활용기 | case_0941 | 0/8 | Ideavim !:과 셸 스크립트 조합으로 초간단 플러그인 만들기 |
| kakaopay/feature-flag | 17,177 | 추출/문제 해결형 | case_0940 | 0/14 | 피처 플래그 개발기: 실시간 데이터 동기화를 향한 여정 |
| kakaopay/aws-reinvent-2024-database-and-storage | 17,620 | 제외/회고·문화·행사 | - | 0/0 | AWS re:Invent 2024 Recap: Database, Storage |
| kakaopay/ktor-api-server | 14,713 | 추출/기술 선택·도입형 | case_0938 | 0/12 | Ktor로 팀 환경에 맞는 API 서버 구현하기 |
| kakaopay/aws-compute | 7,976 | 제외/회고·문화·행사 | - | 0/0 | AWS re:Invent 2024 Recap: Compute |
| kakaopay/aws-reinvent-2024-ai-part-1 | 9,519 | 추출/실험·활용기 | case_0943, case_0944, case_0945 | 0/26 | AWS re:Invent 2024 Recap: AI 1편 |
| kakaopay/aws-reinvent-2024-ai-part-2 | 10,397 | 제외/회고·문화·행사 | - | 0/0 | AWS re:Invent 2024 Recap: AI 2편 |
| kakaopay/given-test-code-2 | 22,327 | 추출/실험·활용기 | case_0937 | 0/11 | 실무에서 적용하는 테스트 코드 작성 방법과 노하우 Part 3: Given 지옥에서 벗어나기 - 스노우볼을 굴려라 |
| kakaopay/will-effect-system | 23,692 | 제외/개념·튜토리얼 | - | 0/0 | 함수형 프로그래밍과 Effect System을 이용한 의도가 명확한 코드 작성하기 |
| kakaopay/kakaopaysec-wecan | 8,650 | 추출/기술 선택·도입형 | case_0934, case_0935, case_0936 | 0/27 | We Can Do Better: 개발자 플랫폼 효율화 이야기 |
| kakaopay/kakaopayins-opensearch-analyzer | 10,157 | 추출/실험·활용기 | case_0924 | 0/9 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/kakaopay-dr-04 | 4,817 | 제외/회고·문화·행사 | - | 0/0 | 제 2회 카카오페이 해커톤, 2025 카페톤 뜨거운 현장 이야기 |
| kakaopay/how-preparedstatement-works-in-our-apps | 18,475 | 추출/실험·활용기 | case_0928 | 0/12 | 우리의 애플리케이션에서 PreparedStatement는 어떻게 동작하고 있는가 |
| kakaopay/realtime-olap-with-apache-pinot | 18,502 | 추출/실험·활용기 | case_0931, case_0932, case_0933 | 0/23 | 실시간 OLAP을 위한 Apache Pinot 운영 노하우 |
| kakaopay/transaction-summary-and-search-with-ai | 15,355 | 추출/실험·활용기 | case_0929, case_0930 | 0/20 | 거래내역에 감성과 지능을 더하다: 이미지 캘린더와 자연어 검색으로 만드는 특별한 금융 경험 |
| kakaopay/loan-voice-ai-chatbot | 15,924 | 추출/실험·활용기 | case_0925, case_0926, case_0927 | 0/23 | 생성형 AI와 금융의 만남, 대출 음성 상담 챗봇 서비스 |
| kakaopay/backend-domain-driven-design | 17,394 | 추출/기술 선택·도입형 | case_0921 | 0/10 | 카카오페이 여신코어 DDD(Domain Driven Design, 도메인 주도 설계)로 구축하기 |
| kakaopay/multi-cluster | 22,699 | 추출/실험·활용기 | case_0922, case_0923 | 0/23 | 99.999%를 향한 집착: 멀티 & 하이브리드 클러스터로 살아남기 |
| kakaopay/nextjs-troubleshooting-cors-version-skew | 13,603 | 추출/문제 해결형 | case_0917, case_0918 | 0/16 | Next.js 트러블슈팅: CORS와 Version Skew 에러 원인부터 해결까지 |
| kakaopay/kakaopay-hackathon-aiva | 13,993 | 추출/실험·활용기 | case_0919, case_0920 | 0/23 | 해커톤 경험을 통해 엿본 AI시대에 개발자가 가져야 할 자세 |
| kakaopay/kakaopay-hackathon-ai-finance-glossary | 9,915 | 추출/실험·활용기 | case_0914, case_0915, case_0916 | 0/20 | 어려운 용어가 있으신가요? ‘금.용.사.’가 알려드립니다! |
| kakaopay/kakaopayins-envelope-encryption | 18,389 | 추출/문제 해결형 | case_0907, case_0908 | 0/15 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/kakaopay-mcp-agent-toolkit | 11,530 | 추출/기술 선택·도입형 | case_0906 | 0/10 | AI 에이전트와 카카오페이 결제 오픈 API 연동하기: MCP Agent Toolkit 개발기 |
| kakaopay/building-ai-loan-coaching-service | 8,394 | 추출/실험·활용기 | case_0905 | 0/9 | 당신의 대출을 코치해줄 AI, 나만의 대출 코치 서비스 개발기 |
| kakaopay/kakaopay-hackathon-paygenie | 20,050 | 추출/실험·활용기 | case_0909, case_0910 | 0/18 | "페이지니가 찾아올게요" 금융 AI 컨시어지, 페이지니 |
| kakaopay/kakaopay-hackathon-face-kiosk-solution | 14,481 | 제외/회고·문화·행사 | - | 0/0 | 안면 인식과 초개인화 키오스크 정도는 해커톤이면 충분하지 않나? |
| kakaopay/how-llm-works | 20,192 | 제외/개념·튜토리얼 | - | 0/0 | 백엔드 개발자의 시선으로 풀어본 LLM 내부 동작 원리: 6단계로 쉽게 이해하기 |
| kakaopay/pink-ward | 8,615 | 추출/문제 해결형 | case_0904 | 0/11 | 서비스에 와드 박기: 서비스 상태 가시화 프로젝트, 핑크와드를 소개합니다. |
| kakaopay/multiverse | 5,881 | 추출/실험·활용기 | case_0899 | 0/11 | 기기 없이 앱을 테스트하는 법, 멀티버스가 알려드립니다 |
| kakaopay/ai-platform | 6,659 | 추출/기술 선택·도입형 | case_0900, case_0901, case_0902 | 0/24 | AI 플랫폼 GPU 도입부터 Kubeflow까지 도입기 |
| kakaopay/fsd | 13,532 | 추출/기술 선택·도입형 | case_0895 | 0/12 | FSD 아키텍처 적용기 : "이 코드는 어디에 넣어야 할까?" FSD가 답해준 코드 위치의 명확성 |
| kakaopay/pallas-v2-log-platform | 25,659 | 추출/문제 해결형 | case_0911, case_0912, case_0913 | 0/32 | 일 41TB, 200억 건의 로그를 ClickStack으로 실시간 처리하기 - 호그와트 도서관 프로젝트 |
| kakaopay/jvm-warm-up | 28,121 | 추출/문제 해결형 | case_0894 | 0/11 | 배포 직후 발생하는 응답 지연을 해결하기 위한 여정 (feat. JVM 웜업) |
| kakaopay/from-yarn-berry-to-pnpm | 6,323 | 추출/기술 선택·도입형 | case_0893 | 0/12 | 그때는 맞고 지금은 틀리다. Yarn Berry에서 pnpm으로 패키지 매니저 전환기 |
| kakaopay/ifkakao-agentic-coding | 7,418 | 추출/실험·활용기 | case_0892 | 0/10 | SDD (spec-kit) 에이전트 코딩 실전기 |
| kakaopay/spring-batch-partitioning | 22,034 | 추출/문제 해결형 | case_0903 | 0/14 | 수억 건의 데이터, 맛있게 쪼개 먹는 방법 (with. Partitioning) |
| kakaopay/2026-kakaopay-developer-festival | 10,441 | 제외/회고·문화·행사 | - | 0/0 | 2026년 카페개페, AI와 함께한 현장 스케치 |
| kakaopay/kakaopayins-fe-common-component | 7,059 | 추출/문제 해결형 | case_0889 | 0/9 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kakaopay/tam-connect | 5,577 | 제외/회고·문화·행사 | - | 0/0 | 2025 TAM CONNECT: 카카오페이 x 토스, 기술지원의 미래를 함께 그리다 |
| kakaopay/kakaopayins-slow-pr-fast-dev | 8,769 | 추출/실험·활용기 | case_0888 | 0/10 | PR을 더 느리게 만들기 위한 고민 |
| kakaopay/ai-agent-1 | 9,989 | 제외/개념·튜토리얼 | - | 0/0 | AI Agent, 넌 누구냐 1 - Tool, MCP, Skill, Harness는 무엇인가 |
| kakaopay/kakaopayins-legacy-improvement-with-aop | 9,864 | 추출/문제 해결형 | case_0887 | 0/10 | 안전하게 레거시 코드 옮겨 보기 |
| kakaopay/mongodb-nplus1-issue | 46,277 | 추출/문제 해결형 | case_0890, case_0891 | 0/20 | Spring Data MongoDB 가이드: 연관관계 설계와 업데이트 전략 |
| kakaopay/querydsl-paging-strategy | 52,407 | 추출/문제 해결형 | case_0896, case_0897, case_0898 | 0/27 | Querydsl 대량 데이터 처리 완전 정리: Count 병목부터 커서 기반 페이지네이션, Batch Insert/Update까지 |
| kurly/bulk-performance-tuning | 7,744 | 추출/문제 해결형 | case_1427 | 2/9 | BULK 처리 Write에 집중해서 개선해보기 |
| kurly/2023-review-opensearch | 8,418 | 추출/기술 선택·도입형 | case_1431 | 0/14 | 후기 서비스 AWS Opensearch 도입기 |
| kurly/tc-optimization | 10,229 | 추출/문제 해결형 | case_1425, case_1426 | 1/17 | 컬리가 상품을 고객에게 빠르게 전달하는 똑똑한 방법 |
| kurly/prod-design-quick-menu | 2,512 | 추출/실험·활용기 | case_1421 | 0/8 | 퀵메뉴로 비즈니스 널리 알리기 (feat. 전지적 디자이너 시점) |
| kurly/kurly_review_image_detection | 8,853 | 추출/문제 해결형 | case_1412 | 0/12 | 고객에게 뚜렷한 경험을: 컬리의 후기 이미지 처리 기술 |
| kurly/cart-recommend-model-development | 9,206 | 추출/실험·활용기 | case_1411 | 0/10 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 1부 |
| kurly/cart-recommend-model-development_second | 13,847 | 추출/문제 해결형 | case_1417, case_1418, case_1419, case_1420 | 0/26 | 함께 구매하면 좋은 상품이에요! - 장바구니 추천 개발기 2부 |
| kurly/commit-mvcc-set-autocommit | 16,463 | 추출/문제 해결형 | case_1407, case_1408 | 0/13 | 데이터가 있었는데요, 아니 없어요 |
| kurly/airflow-1 | 9,494 | 추출/기술 선택·도입형 | case_1414, case_1415, case_1416 | 0/22 | 서버리스에서 쿠버네티스로 - Airflow 운영 경험기 |
| kurly/bigquery-gemini-review | 8,706 | 추출/실험·활용기 | case_1409 | 0/10 | BigQuery와 Gemini로 리뷰 분석 업무 자동화하기 |
| kurly/vertex-ai-search-nr | 7,010 | 추출/기술 선택·도입형 | case_1413 | 0/13 | Vertex AI Search를 활용한 결과 없는 검색 개선하기 |
| kurly/2024-review-llm-application | 10,038 | 추출/실험·활용기 | case_1403 | 0/9 | LLM Application 구축 도전기 (feat. 소중한 고객님들의 리뷰) - 1부 |
| kurly/picking-simulation | 6,022 | 추출/실험·활용기 | case_1410 | 0/13 | 컬리의 Virtual 물류 센터 |
| kurly/fix-hibernate-localtime-bug | 7,136 | 추출/문제 해결형 | case_1401 | 0/8 | 하이버네이트의 시간은 거꾸로 간다 |
| kurly/74-excel-upload-zip-bomb | 5,783 | 추출/문제 해결형 | case_1400 | 0/8 | 엑셀 업로드 중 발생한 Zip Bomb 에러 파헤치기! 🥊 |
| kurly/2023-delivery-system | 9,331 | 추출/문제 해결형 | case_1402 | 0/12 | 컬리의 새로운 배송 시스템 구축 과정과 우리가 배운점 |
| kurly/2024-spring-kafka-consumer-offset-seeking | 15,390 | 추출/문제 해결형 | case_1406 | 0/13 | 분산 시스템 환경에서 Kafka Consumer 오프셋 이동하기 |
| kurly/75-java-module-with-gson-serialization | 9,116 | 추출/문제 해결형 | case_1399 | 0/9 | Spring Boot 버전업 중 알게된 Java 버전별 캡슐화 정책 강화 |
| kurly/2024-mysql-paging-query-provider | 17,506 | 추출/문제 해결형 | case_1404, case_1405 | 0/15 | MySqlPagingQueryProvider 살펴보기 |
| kurly/deliveryproductteam-culture-1 | 4,454 | 추출/문제 해결형 | case_1391 | 0/8 | 딜리버리 프로덕트 개발팀의 개발문화 - 로그 & 알람편 |
| kurly/connection-leak | 6,791 | 추출/문제 해결형 | case_1392 | 0/9 | 99%가 모른다는 DB Connection 누수 문제 |
| kurly/refine-address-internalization-1 | 5,382 | 추출/문제 해결형 | case_1386 | 0/9 | 주소정제 서비스 내재화 - 1화 ( 줄줄 새는 돈 ) |
| kurly/refine-address-internalization-2 | 4,312 | 추출/문제 해결형 | case_1398 | 0/11 | 주소정제 서비스 내재화 - 2화 ( 그럴싸한 계획 ) |
| kurly/refine-address-internalization-3 | 5,766 | 추출/문제 해결형 | case_1396, case_1397 | 0/15 | 주소정제 서비스 내재화 - 3화 ( 노가다의 달달한 열매 ) |
| kurly/refine-address-internalization-4 | 13,407 | 추출/문제 해결형 | case_1389 | 0/12 | 주소정제 서비스 내재화 - 4화 ( 슬픈예감 ) |
| kurly/refine-address-internalization-5 | 9,433 | 추출/문제 해결형 | case_1390 | 0/13 | 주소정제 서비스 내재화 - 5화 ( 어질어질한 변화구들 ) |
| kurly/refine-address-internalization-6 | 5,103 | 추출/문제 해결형 | case_1393 | 0/11 | 주소정제 서비스 내재화 - 마지막 화 ( 엔드 게임 ) |
| kurly/oms_pm | 6,029 | 추출/기술 선택·도입형 | case_1394, case_1395 | 0/13 | 물류의 물짜도 모르던 OMS PM의 OMS 구축기 |
| kurly/kafka-connect-pipeline | 9,612 | 추출/문제 해결형 | case_1387, case_1388 | 0/16 | Kafka Connect로 DB 데이터 쉽게 연동하기 |
| kurly/2025-delivery-debug-study | 10,654 | 제외/회고·문화·행사 | - | 0/0 | 딜리버리 프로덕트 개발팀의 개발 문화 - 주니어 디버깅 스터디 |
| kurly/oms-msa-architecture-1 | 6,200 | 추출/기술 선택·도입형 | case_1382 | 0/10 | OMS의 최적화된 마이크로서비스 아키텍처 디자인 |
| kurly/delivery-encryption-module | 7,055 | 추출/기술 선택·도입형 | case_1383, case_1384, case_1385 | 0/26 | 딜리버리 암호화 모듈 개발기 |
| kurly/2025-delivery-jarvis-story | 4,661 | 추출/실험·활용기 | case_1378 | 0/12 | 우리 팀에도 Jarvis 가 생겼다 – 생성형 AI 로 만든 에러 분석가 이야기 |
| kurly/access-block-1 | 5,663 | 추출/문제 해결형 | case_1377 | 0/13 | nginx 설정 없이 우아하게 서비스 점검하기 (上) |
| kurly/access-block-2 | 8,383 | 추출/문제 해결형 | case_1379 | 0/12 | nginx 설정 없이 우아하게 서비스 점검하기 (下) |
| kurly/fintech-bff-introduction | 10,052 | 추출/실험·활용기 | case_1380, case_1381 | 0/15 | 핀테크그룹의 GraphQL 기반 BFF와 프론트엔드 활용기 |
| kurly/2025-delivery-photo-object-detection | 3,969 | 추출/문제 해결형 | case_1369 | 0/13 | 배송 완료 사진 속 객체 탐지를 통한 수기 검수 비용 줄이기 |
| kurly/personalized-recommendation-v1 | 14,411 | 추출/실험·활용기 | case_1374, case_1375, case_1376 | 0/26 | 개인화 추천 시스템 1편 - 유저의 행동은 “언어”일까? : Collaborative Embedding 구축기 (feat. Knowledge Distillation) |
| kurly/2025-kafka-streams-window | 9,459 | 추출/문제 해결형 | case_1367, case_1368 | 0/20 | Kafka Streams 윈도우 도입기 |
| kurly/cms-vite-%EC%A0%84%ED%99%98%EA%B8%B0 | 13,290 | 추출/기술 선택·도입형 | case_1373 | 0/15 | 빌드가 터졌다: 5년 된 CMS 프로젝트의 Webpack4 → Vite 전환 |
| kurly/tech-spec-adoption-with-ai-automation | 8,164 | 추출/기술 선택·도입형 | case_1370 | 0/11 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| kurly/vibe-coding-with-claude-code | 16,712 | 제외/개념·튜토리얼 | - | 0/0 | Claude Code를 활용한 예측 가능한 바이브 코딩 전략 |
| kurly/klds-web-structure-refactor | 7,548 | 추출/문제 해결형 | case_1361 | 0/13 | 디자인 컴포넌트 라이브러리를 ‘실제 사용 방식’에 맞게 다시 설계한 이야기 |
| kurly/oms-claude-ai-workflow | 19,474 | 추출/실험·활용기 | case_1360 | 0/12 | OMS에서 Claude AI를 활용하여 변화된 업무 방식 |
| kurly/2026-outbox-pattern-and-retry-topic | 23,535 | 추출/문제 해결형 | case_1371, case_1372 | 0/18 | 컬리의 입고 시스템이 외부 인입 데이터를 안전하게 동기화하는 방법 |
| kurly/nx-bun-migration | 5,492 | 추출/문제 해결형 | case_1358, case_1359 | 0/16 | Nx에서 Bun 더 잘 사용하기: Nx 18 -> 21 마이그레이션 |
| kurly/ai-orchestration-1 | 6,261 | 추출/실험·활용기 | case_1351 | 0/10 | AI 토큰 사용량 전사 1위 개발자가 148,000번의 대화에서 배운 것 |
| kurly/ai-orchestration-2 | 17,572 | 추출/실험·활용기 | case_1365, case_1366 | 0/16 | AI 에이전트 15개를 동시에 굴리는 법 — AI 병렬 오케스트레이션 실전 운용기 |
| kurly/claude-code-redesign-my-day | 7,389 | 추출/실험·활용기 | case_1355, case_1356, case_1357 | 0/27 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| kurly/image-based-misdelivery-detection | 14,393 | 추출/문제 해결형 | case_1349 | 0/11 | 현관문에도 얼굴이 있다: 배송 완료 사진 기반 On-device 오배송 탐지 시스템 |
| kurly/2026-delivery-domain-rag | 7,769 | 추출/문제 해결형 | case_1348 | 0/12 | AI에게 도메인을 가르치다 두 번 갈아엎은 이야기 — LLM Wiki + RAG 혼합기 |
| ly/20231001a | 254 | 제외/회고·문화·행사 | - | 0/0 | LINE과 Yahoo! JAPAN이 만나 함께 새로운 기술 블로그를 시작했습니다! |
| ly/how-to-measure-voice-quality-in-line-app | 29,697 | 추출/실험·활용기 | case_1352, case_1353, case_1354 | 0/26 | LINE 앱에서 음성 품질을 측정하는 방법 |
| ly/improve-operation-environment-with-rundeck | 19,095 | 추출/기술 선택·도입형 | case_1362, case_1363, case_1364 | 3/29 | Ansible과 Rundeck을 활용한 서버 작업 자동화 및 권한 제어 |
| ly/developing-android-ui-with-jetpack-compose | 11,990 | 추출/기술 선택·도입형 | case_1346 | 0/13 | Jetpack Compose로 LINE 앱 Yahoo!검색 모듈 개발하기 |
| ly/managing-multi-cdn-logs-traffics-with-vector | 16,695 | 추출/문제 해결형 | case_1340 | 0/11 | Vector를 활용해 멀티 CDN 로그 및 트래픽 관리하기 |
| ly/designing-software-like-an-open-source | 14,849 | 추출/실험·활용기 | case_1350 | 0/12 | 오픈소스답게 소프트웨어 설계하기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 18,813 | 추출/실험·활용기 | case_1338, case_1339 | 0/16 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/check-mp4-file-has-audio-using-filereader-in-front-end | 8,381 | 추출/문제 해결형 | case_1347 | 1/11 | 프런트엔드 영역에서 FileReader를 이용해 MP4 파일 내 오디오 존재 여부 확인하기 |
| ly/how-to-migrate-to-spring-boot-3 | 38,278 | 추출/문제 해결형 | case_1337 | 0/11 | 실전! Spring Boot 3 마이그레이션 |
| ly/how-to-run-a-blog-study-in-line-plus | 4,764 | 제외/회고·문화·행사 | - | 0/0 | 너, 블로그 저자가 돼라! 블로그 스터디 운영 후기 |
| ly/improve-openchat-recommendation-model-with-offline-and-online-ab-test | 9,684 | 추출/문제 해결형 | case_1336 | 0/10 | 오프라인과 온라인 A/B 테스트를 통해 오픈챗 추천 모델 개선하기 |
| ly/how-to-develop-font-customizing-function-in-android-app | 9,184 | 추출/문제 해결형 | case_1344, case_1345 | 1/20 | LINE Android 앱에 폰트 커스터마이징 기능 적용하기 |
| ly/abc-user-feedback | 6,188 | 추출/실험·활용기 | case_1341, case_1342, case_1343 | 1/17 | 사용자의 피드백을 잘 관리하고 활용하기 위한 서비스, ABC User Feedback |
| ly/docusaurus-as-a-technical-document-website | 11,119 | 추출/기술 선택·도입형 | case_1335 | 0/13 | 기술 문서 사이트로 Docusaurus 활용하기 |
| ly/about-atlassian-jira-ranking-algorithm-lexorank | 9,203 | 추출/문제 해결형 | case_1332 | 0/10 | Jira의 이슈 정렬 방식이 Integer 방식이 아니라고?! |
| ly/demaecan-3rd-recode-react-native-to-flutter | 12,385 | 추출/기술 선택·도입형 | case_1331 | 1/12 | Flutter 전환의 마침표 - 일본 1위 배달 앱, 세 번째 Recode |
| ly/20231216a | 9,110 | 제외/개념·튜토리얼 | - | 0/0 | 메모리 모델 입문 - Sequential Consistency와 Total Store Order 이해하기 |
| ly/5-year-effort-to-put-abc-user-feedback-on-track | 14,313 | 추출/실험·활용기 | case_1333, case_1334 | 0/19 | 5년간 첫 삽만 5번 뜬 오픈소스 ABC User Feedback 궤도에 오르기까지 |
| ly/increase-vm-performance-to-reduce-global-warming | 23,391 | 추출/문제 해결형 | case_1327 | 1/14 | 가상 머신의 성능을 높이는 것도 지구 온난화에 도움이 될까요? |
| ly/using-ast-to-verify-the-code-after-code-linting | 16,155 | 추출/문제 해결형 | case_1322 | 0/9 | 린트 적용으로 코드 대량 변경 시 AST를 이용해 검증하기 |
| ly/ly-tech-blog-fy23-retrospective | 938 | 제외/회고·문화·행사 | - | 0/0 | LY Tech Blog에서 FY23 회고를 진행합니다 |
| ly/running-redis-at-scale | 8,980 | 추출/문제 해결형 | case_1325, case_1326 | 1/19 | 대규모 Redis를 운영하며 살아남기 |
| ly/experience-in-migrating-order-db-on-ecommerce-platform | 8,732 | 추출/문제 해결형 | case_1328, case_1329, case_1330 | 1/26 | 이커머스 플랫폼의 주문 DB 마이그레이션 경험기 |
| ly/make-seamless-screen-transition-in-line-ios-app | 14,958 | 추출/문제 해결형 | case_1321 | 0/9 | 물 흐르듯 자연스러운 화면 전환을 향한 여정 |
| ly/develop-hitbasehandler-to-manage-apache-hbase-cluster | 16,394 | 추출/기술 선택·도입형 | case_1320 | 0/14 | HBase 오픈소스 전환을 위한 HBH(HitBase Handler) 개발기 |
| ly/turn-invisible-logic-into-readable-document | 8,914 | 추출/문제 해결형 | case_1316 | 0/11 | 보이지 않는 로직, 읽을 수 있는 문서로 만들기! |
| ly/automate-streaming-pipeline-validation-with-kubernetes-native-workflows-1 | 7,415 | 추출/문제 해결형 | case_1323, case_1324 | 1/17 | 쿠버네티스 네이티브 워크플로를 이용한 대용량 스트리밍 파이프라인 검증 자동화 - 1편 |
| ly/a-formular-for-prioritizing | 14,866 | 추출/실험·활용기 | case_1319 | 0/10 | 우선순위에 시달리다 공식을 만들었다 |
| ly/building-a-messaging-queuing-system-with-redis-streams | 11,441 | 추출/기술 선택·도입형 | case_1315 | 0/18 | 실시간 추천 서비스를 위해 메시지 큐잉 도입하기(with Redis Streams) |
| ly/tpm-retrospective-on-global-collaboration-process-improvement | 9,662 | 제외/회고·문화·행사 | - | 0/0 | LINE SHOPPING JP, 글로벌 협업 프로세스 개선 회고 |
| ly/one-year-retrospective-of-platform-team-at-demaecan | 8,918 | 제외/회고·문화·행사 | - | 0/0 | 플랫폼 팀의 1년, 일본 최대 규모의 배달 서비스에 안착하기까지 |
| ly/automate-streaming-pipeline-validation-with-kubernetes-native-workflows-2 | 13,132 | 추출/문제 해결형 | case_1313 | 0/11 | 쿠버네티스 네이티브 워크플로를 이용한 대용량 스트리밍 파이프라인 검증 자동화 - 2편 |
| ly/moving-large-scale-cassandra-to-a-new-cluster | 13,655 | 추출/문제 해결형 | case_1317 | 0/15 | 개발자가 손수 대규모 Cassandra를 신규 클러스터로 이전하기 |
| ly/api-document-integration-and-documentation-automation | 15,995 | 추출/문제 해결형 | case_1318 | 0/13 | 모두가 행복해지는 API 문서 통합과 자동화 |
| ly/automate-streaming-pipeline-validation-with-kubernetes-native-workflows-3 | 33,525 | 추출/실험·활용기 | case_1314 | 0/12 | 쿠버네티스 네이티브 워크플로를 이용한 대용량 스트리밍 파이프라인 검증 자동화 - 3편 |
| ly/internal-event-for-technical-writing-and-document-engineering | 24,354 | 제외/회고·문화·행사 | - | 0/0 | 문서 작성 및 관리 노하우를 알리는 행사, Technical Documentation Day 참석 후기 |
| ly/migrate-mysql-with-read-only-mode | 6,059 | 추출/문제 해결형 | case_1312 | 0/11 | 읽기 전용 설정으로 MySQL 이전하기 |
| ly/monorepo-structure-for-abc-user-feedback | 9,965 | 추출/기술 선택·도입형 | case_1310 | 0/11 | 오픈소스 ABC User Feedback에 적용한 모노리포 구조 소개 |
| ly/how-platform-developers-handle-questions | 19,158 | 추출/기술 선택·도입형 | case_1309 | 0/11 | 질문에 대처하는 어느 플랫폼 개발자의 이야기 |
| ly/headver-new-versioning-system-for-product-teams | 15,185 | 추출/기술 선택·도입형 | case_1311 | 0/12 | HeadVer - 기민한 프로덕트 팀을 위한 새로운 버저닝 시스템 |
| ly/offline-meetup-for-line-developers-push-and-pull | 6,691 | 제외/회고·문화·행사 | - | 0/0 | LINE 개발자를 위한 오프라인 밋업, Push&Pull |
| ly/req-saver-for-thundering-herd-problem-in-cache | 9,322 | 추출/문제 해결형 | case_1305 | 0/12 | req-shield로 캐시의 골칫거리 'Thundering Herd 문제' 쉽게 풀기! |
| ly/how-to-ux-research-and-renewal-for-overseas-users | 11,963 | 추출/실험·활용기 | case_1303 | 0/12 | 1,100km 떨어져 있는 사용자를 위한 UX 리서치부터 과감한 리뉴얼까지의 기록 |
| ly/how-to-measure-noise-suppression-performance-in-line-app | 10,125 | 추출/실험·활용기 | case_1304 | 1/10 | LINE 앱의 잡음 제거 기술 성능 측정 방법 |
| ly/from-traditional-cms-to-landpress-content | 9,138 | 추출/문제 해결형 | case_1302 | 0/12 | 전통적인 CMS에서 LandPress Content로 CMS를 옮기는 이유 |
| ly/using-custom-lint-in-flutter | 13,764 | 추출/실험·활용기 | case_1299 | 0/11 | Flutter에서 커스텀 린트 활용하기 |
| ly/multi-label-classification-model-for-openchat-hashtag-prediction | 19,261 | 추출/문제 해결형 | case_1306, case_1307, case_1308 | 2/25 | 오픈챗 해시태그 예측을 위한 다중 레이블 분류 모델 개발하기 |
| ly/code-review-culture-of-line-client-developers | 7,644 | 제외/회고·문화·행사 | - | 0/0 | LINE 클라이언트 개발자들이 만드는 '코드 리뷰 문화' |
| ly/how-to-efficiently-handle-massive-ai-real-time-embedding | 14,619 | 추출/문제 해결형 | case_1300, case_1301 | 0/20 | 대용량 AI 실시간 임베딩 데이터를 효율적으로 다루기 |
| ly/line-device-attestation-1 | 13,436 | 추출/실험·활용기 | case_1297 | 0/10 | 기기와 앱의 무결성 보장부터 서비스 요청 보호까지: LINE의 기기 증명 서비스 - 1편 |
| ly/change-data-capture-for-headless-cms | 4,600 | 추출/문제 해결형 | case_1296 | 0/9 | Headless CMS를 위한 변경 데이터 캡쳐(CDC) 기술 설계하기 |
| ly/improving-kubernetes-relay-api-server-performance-with-informer | 12,361 | 추출/문제 해결형 | case_1298 | 0/9 | Informer를 사용해 쿠버네티스 중계 API 서버의 성능 개선하기 |
| ly/increase-productivity-of-quality-activities-with-generative-ai | 7,807 | 추출/실험·활용기 | case_1293 | 0/12 | LY의 QA 엔지니어가 생성형 AI를 이용해 품질 활동의 생산성을 높이는 방법 |
| ly/using-topology-spread-constraints-to-spread-out-pods | 10,049 | 추출/실험·활용기 | case_1295 | 0/11 | 쿠버네티스에서 파드를 분산 처리하기 위한 토폴로지 분배 제약 조건 활용 사례 소개 |
| ly/migrating-large-data-with-kafka-and-etl | 23,093 | 추출/문제 해결형 | case_1294 | 0/11 | Kafka와 ETL을 활용해 대용량 데이터 마이그레이션하기 |
| ly/define-and-manage-kubernetes-custom-resources-with-controller | 8,174 | 추출/실험·활용기 | case_1291 | 1/9 | 쿠버네티스 커스텀 리소스 정의하고 관리하기(feat.컨트롤러) |
| ly/line-device-attestation-2 | 7,845 | 추출/문제 해결형 | case_1283 | 0/10 | 기기와 앱의 무결성 보장부터 서비스 요청 보호까지: LINE의 기기 증명 서비스 - 2편 |
| ly/improve-development-experience-with-flutter-web | 10,853 | 추출/문제 해결형 | case_1290 | 0/11 | Flutter Web을 활용해 제품 개발 환경 개선하기 |
| ly/introducing-fido2-client-sdk-open-source | 9,957 | 추출/기술 선택·도입형 | case_1292 | 0/11 | FIDO2 클라이언트 SDK 오픈소스 소개 |
| ly/pqc-to-protect-data-in-the-age-of-quantum-computers | 10,550 | 제외/개념·튜토리얼 | - | 0/0 | PQC로의 여정: 양자 컴퓨터 시대에 데이터 지키기 |
| ly/visiting-tokyo-for-tech-week-2024 | 4,949 | 제외/회고·문화·행사 | - | 0/0 | Tech Week 2024, 도쿄에 다녀왔습니다. |
| ly/three-ways-to-reform-legacy-systems | 9,103 | 추출/문제 해결형 | case_1287, case_1288, case_1289 | 0/26 | 과격하게 레거시를 쇄신하는 세 가지 방법과 그 사례 |
| ly/smart-monitoring-system-with-playwright-and-jira | 20,959 | 추출/기술 선택·도입형 | case_1282 | 0/17 | Playwright와 Jira로 만드는 스마트 장애/변경 알림 및 관리 시스템 |
| ly/recode_project | 10,467 | 추출/기술 선택·도입형 | case_1284, case_1285, case_1286 | 0/22 | 일본 최대 규모 음식 배달 서비스, 바닥부터 다시 짠다 - Recode 프로젝트 |
| ly/flutter-clean-architecture | 9,916 | 추출/기술 선택·도입형 | case_1275 | 0/10 | Flutter 클린 아키텍처: 작은 앱부터 대규모 프로젝트까지 맞춤 설계 |
| ly/tech-week-2024-hackathon-hack-day-recap | 5,923 | 제외/회고·문화·행사 | - | 0/0 | Tech Week 2024, 사내 해커톤 Hack Day에 참여했습니다! |
| ly/automating-llm-application-evaluation-with-harness | 21,297 | 추출/실험·활용기 | case_1281 | 0/10 | Harness를 이용해 LLM 애플리케이션 평가 자동화하기 |
| ly/python-multi-project-application-with-poetry | 13,556 | 추출/기술 선택·도입형 | case_1279, case_1280 | 1/17 | Poetry를 이용한 멀티 프로젝트 Python 애플리케이션 개발 방법 |
| ly/future-flutter-2024-recap | 4,952 | 제외/회고·문화·행사 | - | 0/0 | Future<Flutter> 2024에 다녀왔습니다 |
| ly/techniques-for-improving-code-quality-1 | 5,832 | 추출/문제 해결형 | case_1274 | 0/7 | 코드 품질 개선 기법 1편: 한 번 엎지른 <error>는 다시 주워 담지 못한다 |
| ly/techniques-for-improving-code-quality-list | 1,386 | 제외/회고·문화·행사 | - | 0/0 | 코드 품질 개선 기법 시리즈 소개 |
| ly/migrating-hbase-with-hbase-replication | 18,369 | 추출/문제 해결형 | case_1277, case_1278 | 1/19 | HBase 복제를 이용해 마이그레이션하기 |
| ly/about-java-virtual-thread-1 | 10,993 | 제외/개념·튜토리얼 | - | 0/0 | Java 가상 스레드, 깊이 있는 소스 코드 분석과 작동 원리 1편 - 생성과 시작 |
| ly/about-java-virtual-thread-2 | 13,755 | 제외/개념·튜토리얼 | - | 0/0 | Java 가상 스레드, 깊이 있는 소스 코드 분석과 작동 원리 2편 - 컨텍스트 스위칭 |
| ly/about-java-virtual-thread-3 | 9,452 | 제외/개념·튜토리얼 | - | 0/0 | Java 가상 스레드, 깊이 있는 소스 코드 분석과 작동 원리 3편 - 고정 이슈와 한계 |
| ly/analysis-and-resolution-of-the-ci-build-error | 24,419 | 추출/문제 해결형 | case_1276 | 0/14 | CI 빌드 오류의 원인 분석에서 해결까지의 여정 |
| ly/techniques-for-improving-code-quality-2 | 3,129 | 제외/개념·튜토리얼 | - | 0/0 | 코드 품질 개선 기법 2편: 확인 여부를 확인했나요? |
| ly/techniques-for-improving-code-quality-3 | 6,212 | 추출/문제 해결형 | case_1272 | 0/11 | 코드 품질 개선 기법 3편: 전략 없는 전략 |
| ly/a-flexible-design-system-using-3-tier-tokens | 8,708 | 추출/기술 선택·도입형 | case_1273 | 0/10 | 3단계로 완성하는 유연한 디자인 시스템 |
| ly/techniques-for-improving-code-quality-4 | 3,178 | 추출/실험·활용기 | case_1264 | 0/5 | 코드 품질 개선 기법 4편: 문을 없애고 테스트하기 |
| ly/maximizing-ad-revenue-while-preserving-usability | 6,330 | 추출/실험·활용기 | case_1266, case_1267 | 0/19 | 사용성을 지키면서 광고 매출 극대화하기, 가능할까요? |
| ly/techniques-for-improving-code-quality-5 | 3,276 | 추출/문제 해결형 | case_1265 | 1/9 | 코드 품질 개선 기법 5편: 나쁜 열거가 좋은 계층을 몰아낸다 |
| ly/building-a-development-environment-for-llm-apps-for-everyone | 17,212 | 추출/기술 선택·도입형 | case_1268 | 1/12 | 모두를 위한 LLM 애플리케이션 개발 환경 구축 사례 |
| ly/building-llmops-for-creating-testing-deploying-of-llm-apps | 7,143 | 추출/기술 선택·도입형 | case_1269 | 1/15 | LLM 앱의 제작에서 테스트와 배포까지, LLMOps 구축 사례 소개 |
| ly/sli-and-slo-for-improving-reliability-1 | 7,382 | 제외/개념·튜토리얼 | - | 0/0 | 신뢰성 향상을 위한 SLI/SLO 도입 1편 - 소개와 필요성 |
| ly/sli-and-slo-for-improving-reliability-2 | 9,047 | 추출/문제 해결형 | case_1263 | 0/13 | 신뢰성 향상을 위한 SLI/SLO 도입 2편 - 플랫폼 적용 사례 |
| ly/4-patterns-of-global-collaboration | 8,902 | 제외/회고·문화·행사 | - | 0/0 | 한국어 몰라요 - 글로벌 협업의 4가지 패턴 |
| ly/2024-frontend-global-workshop-recap | 2,154 | 제외/회고·문화·행사 | - | 0/0 | 2024 Frontend Global Workshop 참석 후기 |
| ly/techniques-for-improving-code-quality-6 | 3,957 | 추출/실험·활용기 | case_1258 | 0/5 | 코드 품질 개선 기법 6편: 마구 자를 것인가 반듯하게 자를 것인가 |
| ly/single-sourcing-for-multi-platform-documentation | 16,793 | 추출/실험·활용기 | case_1262 | 0/11 | 멀티플랫폼 문서를 관리하는 한 가지 방법, 싱글 소싱 |
| ly/how-to-evaluate-ai-generated-images-1 | 16,708 | 제외/개념·튜토리얼 | - | 0/0 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/techniques-for-improving-code-quality-7 | 2,740 | 제외/개념·튜토리얼 | - | 0/0 | 코드 품질 개선 기법 7편: 새것을 들일 때 옛것도 다시 살피자 |
| ly/efficiently-using-cpu-in-kubernetes | 12,961 | 추출/실험·활용기 | case_1270, case_1271 | 1/20 | 당신의 CPU는 열심히 일하고 있나요? |
| ly/techniques-for-improving-code-quality-8 | 3,940 | 제외/개념·튜토리얼 | - | 0/0 | 코드 품질 개선 기법 8편: 실상과 허상 |
| ly/state-of-ly-frontend-2024-report | 4,879 | 제외/회고·문화·행사 | - | 0/0 | LY Corporation의 프런트엔드 기술 동향을 알아보자! State of LY Frontend 2024 실시 보고서 |
| ly/techniques-for-improving-code-quality-9 | 3,730 | 추출/문제 해결형 | case_1255 | 0/8 | 코드 품질 개선 기법 9편: 왔던 길을 되돌아가 보자 |
| ly/introduction-to-mcp-and-building-mcp-server-using-line-messaging-api | 9,596 | 추출/실험·활용기 | case_1260 | 0/8 | MCP 개념 및 LINE Messaging API를 활용한 MCP 서버 구축 사례 소개 |
| ly/techniques-for-improving-code-quality-10 | 3,857 | 추출/문제 해결형 | case_1254 | 0/5 | 코드 품질 개선 기법 10편: 적절한 거리 유지에 신경 쓰자 |
| ly/how-to-evaluate-ai-generated-images-2-blackbox-optimization | 16,467 | 추출/실험·활용기 | case_1261 | 0/11 | AI로 생성한 이미지는 어떻게 평가할까요? (블랙박스 최적화 적용편) |
| ly/techniques-for-improving-code-quality-11 | 3,395 | 제외/개념·튜토리얼 | - | 0/0 | 코드 품질 개선 기법 11편: 반복되는 호출에 함수도 지친다 |
| ly/how-to-evaluate-ai-generated-images-3-inpainting | 12,313 | 추출/실험·활용기 | case_1259 | 0/11 | AI로 생성한 이미지는 어떻게 평가할까요? (인페인팅 적용편) |
| ly/techniques-for-improving-code-quality-12 | 4,238 | 추출/문제 해결형 | case_1253 | 0/9 | 코드 품질 개선 기법 12편: 세트 할인 |
| ly/rag-based-bot-for-streamlining-inquiry-responses | 6,441 | 추출/실험·활용기 | case_1249 | 0/8 | 문의 대응을 효율화하기 위한 RAG 기반 봇 도입하기 |
| ly/techniques-for-improving-code-quality-13 | 4,995 | 추출/문제 해결형 | case_1245 | 0/5 | 코드 품질 개선 기법 13편: 클론 가족 |
| ly/introduction-to-membership-authentication-system-renewal-case-study | 6,306 | 추출/문제 해결형 | case_1247, case_1248 | 0/13 | 복잡한 회원 인증 프로세스, 기본 원칙만 알면 쉽습니다 |
| ly/techniques-for-improving-code-quality-14 | 5,038 | 제외/개념·튜토리얼 | - | 0/0 | 코드 품질 개선 기법 14편: 책임을 부여하는 오직 하나의 책임 |
| ly/thailand-call-quality-report | 12,978 | 추출/문제 해결형 | case_1256, case_1257 | 1/11 | LINE 앱 영상 통화를 가장 많이 사용하는 나라, 태국에서 LINE 앱의 영상 통화 품질을 점검했습니다 |
| ly/techniques-for-improving-code-quality-15 | 3,530 | 제외/개념·튜토리얼 | - | 0/0 | 코드 품질 개선 기법 15편: 문법은 이름을 나타낸다 |
| ly/give-me-the-code-and-then-ai-and-i-will-provide-the-api-reference-for-you | 7,557 | 추출/실험·활용기 | case_1246 | 0/12 | AI와 글쟁이의 동행: 코드 주면 API 레퍼런스 써드려요 |
| ly/migrate-payment-system-db-to-vitess-1 | 12,200 | 추출/기술 선택·도입형 | case_1244 | 0/12 | 일 평균 30억 건을 처리하는 결제 시스템의 DB를 Vitess로 교체하기 - 1. 솔루션 선정기 |
| ly/intruoduction-to-tech-verse-2025 | 1,258 | 제외/회고·문화·행사 | - | 0/0 | 테크 컨퍼런스 Tech-Verse 2025를 개최합니다 |
| ly/techniques-for-improving-code-quality-16 | 4,455 | 제외/개념·튜토리얼 | - | 0/0 | 코드 품질 개선 기법 16편: 불이 'null'인 굴뚝에 연기가 'null'이 아닐 수 없다 |
| ly/techniques-for-improving-code-quality-17 | 5,262 | 추출/문제 해결형 | case_1237 | 0/5 | 코드 품질 개선 기법 17편: 사상누각 |
| ly/tech-verse-2025-recap | 3,363 | 제외/회고·문화·행사 | - | 0/0 | LY의 테크 컨퍼런스, 'Tech-Verse 2025' 후기 |
| ly/how-to-make-the-most-of-flutter-riverpod | 8,880 | 제외/개념·튜토리얼 | - | 0/0 | Flutter Riverpod 200% 활용하기 |
| ly/large-scale-vector-db-for-real-time-recommendation-in-line-voom | 13,544 | 추출/기술 선택·도입형 | case_1250, case_1251, case_1252 | 0/25 | Milvus: LINE VOOM의 실시간 추천 시스템을 위한 대규모 벡터 DB 구축기 |
| ly/applying-ddd-to-merchant-system-development | 5,212 | 추출/기술 선택·도입형 | case_1242 | 0/12 | DDD를 Merchant 시스템 구축에 활용한 사례를 소개합니다 |
| ly/migrate-payment-system-db-to-vitess-2 | 12,996 | 추출/문제 해결형 | case_1243 | 0/13 | 일 평균 30억 건을 처리하는 결제 시스템의 DB를 Vitess로 교체하기 - 2. 개발 및 운영기 |
| ly/flexible-multi-site-architecture-with-integrated-nginx-configuration-and-loki | 18,853 | 추출/문제 해결형 | case_1239, case_1240, case_1241 | 0/27 | Nginx 설정 통합과 Loki 연동으로 설계한 유연한 멀티사이트 아키텍처 |
| ly/hack-day-2025-recap | 7,268 | 제외/회고·문화·행사 | - | 0/0 | 자네, 해커가 되지 않겠나? Hack Day 2025에 다녀왔습니다! |
| ly/sharing-the-workflow-of-a-third-year-app-developer | 6,100 | 제외/회고·문화·행사 | - | 0/0 | 3년 차 앱 개발자가 일하는 순서를 공유합니다 |
| ly/tech-verse-2025-recap-current-state-of-ly-ai-tech | 6,918 | 제외/회고·문화·행사 | - | 0/0 | LY Corporation의 AI 기술의 현재, Tech-Verse 2025 후기 |
| ly/improving-video-playback-quality-in-line-call | 9,759 | 추출/문제 해결형 | case_1235 | 0/11 | LINE 통화의 영상 재생 품질 개선 사례 |
| ly/techniques-for-improving-code-quality-18 | 3,340 | 추출/문제 해결형 | case_1230 | 0/4 | 코드 품질 개선 기법 18편: 함수만 보고 관계는 보지 못한다 |
| ly/extracting-trending-keywords-from-openchat-messages | 14,017 | 추출/실험·활용기 | case_1238 | 1/15 | 오픈챗 메시지들로부터 트렌딩 키워드 추출하기 |
| ly/techniques-for-improving-code-quality-19 | 4,346 | 추출/문제 해결형 | case_1229 | 0/7 | 코드 품질 개선 기법 19편: 차일드 록 |
| ly/techniques-for-improving-code-quality-20 | 5,539 | 추출/문제 해결형 | case_1234 | 1/9 | 코드 품질 개선 기법 20편: 이례적인 예외 과대 포장 |
| ly/p-canvas-a-technique-for-understanding-your-team | 13,241 | 제외/회고·문화·행사 | - | 0/0 | P-Canvas, 팀을 이해하기 위한 엔지니어링 기법 |
| ly/pd1-ai-hackathon-recap | 4,153 | 제외/회고·문화·행사 | - | 0/0 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/finishing-a-1-month-assignment-in-5-days-with-vibe-coding | 8,669 | 추출/실험·활용기 | case_1231 | 1/10 | 한 달짜리 과제, 바이브 코딩으로 5일 만에!(ChatGPT·Cursor) |
| ly/iui-2025-recap | 7,842 | 제외/회고·문화·행사 | - | 0/0 | IUI 2025 참관기: AI의 지속성과 인간 중심의 AI에 대해서 |
| ly/outage-monitoring-for-app-success | 11,316 | 추출/실험·활용기 | case_1236 | 0/12 | 앱 성공을 위한 필수 요소: 장애 모니터링 |
| ly/techniques-for-improving-code-quality-21 | 5,349 | 추출/문제 해결형 | case_1219 | 0/6 | 코드 품질 개선 기법 21편: 생성자를 두드려 보고 건너라 |
| ly/risks-and-mitigations-in-ai-products-development | 11,404 | 추출/문제 해결형 | case_1223, case_1224, case_1225, case_1226, case_1227 | 0/21 | AI 제품 개발 중 마주칠 수 있는 보안 위협 사례와 대책 방안 |
| ly/techniques-for-improving-code-quality-22 | 4,178 | 제외/개념·튜토리얼 | - | 0/0 | 코드 품질 개선 기법 22편: To equal, or not to equal |
| ly/pushsphere-reliable-and-prompt-high-volume-push-notification | 10,113 | 추출/문제 해결형 | case_1221, case_1222 | 0/16 | Pushsphere: LINE 메신저의 빠르고 신뢰할 수 있는 대량 푸시 알림 비법 |
| ly/techniques-for-improving-code-quality-23 | 5,495 | 추출/실험·활용기 | case_1218 | 0/8 | 코드 품질 개선 기법 23편: 반환의 끝이 에지 케이스의 끝 |
| ly/connecting-thousands-of-services-with-central-dogma-control-plane | 8,894 | 추출/기술 선택·도입형 | case_1232, case_1233 | 1/16 | Central Dogma 컨트롤 플레인으로 LY Corporation의 수천 개 서비스를 연결하기 |
| ly/techniques-for-improving-code-quality-24 | 3,608 | 제외/개념·튜토리얼 | - | 0/0 | 코드 품질 개선 기법 24편: 유산의 가치 |
| ly/line-ctf-practical-security-knowledge-that-grows-with-community | 6,680 | 제외/회고·문화·행사 | - | 0/0 | 커뮤니티와 함께 성장하는 실무 보안 지식, LINE CTF |
| ly/techniques-for-improving-code-quality-25 | 2,550 | 추출/실험·활용기 | case_1217 | 0/4 | 코드 품질 개선 기법 25편: 요컨대... 무슨 말이죠? |
| ly/advanced-ab-test-system-with-dynamic-user-segmentation | 5,343 | 추출/실험·활용기 | case_1220 | 0/8 | 동적 사용자 분할을 활용한 새로운 A/B 테스트 시스템을 소개합니다 |
| ly/why-did-an-athenz-engineer-take-on-the-kubestronaut-challenge | 6,019 | 제외/회고·문화·행사 | - | 0/0 | Athenz 엔지니어는 왜 Kubestronaut에 도전했는가? |
| ly/techniques-for-improving-code-quality-26 | 3,963 | 제외/개념·튜토리얼 | - | 0/0 | 코드 품질 개선 기법 26편: 설명의 핵심은 첫 문장에 있다 |
| ly/safety-and-cost-saving-why-separate-guardrails-are-necessary | 20,308 | 추출/기술 선택·도입형 | case_1228 | 0/11 | 안전은 기본, 비용 절감은 덤: AI 서비스에 별도 가드레일이 필요한 이유 |
| ly/ai-campus-day-for-enhancing-ai-literacy-of-employees | 5,109 | 제외/회고·문화·행사 | - | 0/0 | 사내 AI 리터러시를 향상하기 위한 AI Campus Day를 개최했습니다 |
| ly/techniques-for-improving-code-quality-27 | 5,083 | 추출/실험·활용기 | case_1209 | 0/9 | 코드 품질 개선 기법 27편: 티끌이 모여 태산이 되듯 의존성도 쌓이면 |
| ly/a-business-trip-to-japan-only-after-1-week-joining | 6,967 | 제외/회고·문화·행사 | - | 0/0 | 입사 일주일 만에 일본 출장을? LINE Plus Developer Relations 뉴비의 바쁜 적응기 |
| ly/techniques-for-improving-code-quality-28 | 3,534 | 추출/문제 해결형 | case_1207 | 0/6 | 코드 품질 개선 기법 28편: 제약 조건에도 상속세가 발생한다 |
| ly/building-an-llm-service-for-enterprise-1-context-engineering | 9,464 | 추출/문제 해결형 | case_1213 | 0/12 | 엔터프라이즈 LLM 서비스 구축기 1: 컨텍스트 엔지니어링 |
| ly/techniques-for-improving-code-quality-29 | 6,100 | 추출/문제 해결형 | case_1206 | 0/7 | 코드 품질 개선 기법 29편: 고르디우스 변수 |
| ly/techniques-for-improving-code-quality-30 | 4,148 | 추출/문제 해결형 | case_1197 | 0/6 | 코드 품질 개선 기법 30편: (투명한) 운명의 붉은 실 |
| ly/the-evolution-of-the-ly-observability-platform | 9,147 | 추출/문제 해결형 | case_1210, case_1211, case_1212 | 1/25 | Scaling to Infinity: 한계를 넘어서는 LY Corporation의 관측 가능성 플랫폼 진화기 |
| ly/creating-the-cloud-of-the-future | 7,098 | 제외/기술 선택·도입형 | - | 0/0 | 미래의 클라우드를 창조하다 |
| ly/building-ai-code-review-platform-with-claude-code-action | 31,382 | 추출/기술 선택·도입형 | case_1214, case_1215, case_1216 | 1/28 | Claude Code Action: 조직 전반의 코드 품질을 지키는 AI 코드 리뷰 플랫폼화 |
| ly/solving-slow-queries-optimizing-bitwise-operation-queries-with-functional-indexes | 7,615 | 추출/문제 해결형 | case_1201 | 0/14 | 슬로우 쿼리 해결기: 함수형 인덱스로 비트 연산 쿼리 최적화하기 |
| ly/introducing-the-journey-of-the-line-dev-ai-reporters | 6,618 | 제외/회고·문화·행사 | - | 0/0 | LINE DEV AI 리포터즈의 여정을 공유합니다! |
| ly/on-device-image-model-trainer-for-messenger-1 | 18,040 | 추출/문제 해결형 | case_1205 | 0/18 | 메신저용 온디바이스 이미지 모델 학습기 1편: 지식 증류로 확장한 다국어 이미지 검색 |
| ly/on-device-image-model-trainer-for-messenger-2 | 16,165 | 추출/문제 해결형 | case_1208 | 2/15 | 메신저용 온디바이스 이미지 모델 학습기 2편: 초저지연 비자기회귀(non-autoregressive) 캡션 생성 전략 |
| ly/building-an-llm-service-for-enterprise-2-agent-engineering | 8,378 | 추출/기술 선택·도입형 | case_1198, case_1199, case_1200 | 0/20 | 엔터프라이즈 LLM 서비스 구축기 2: 에이전트 엔지니어링 |
| ly/journey-to-perfect-ai-guardrails-neurips-2025-recap | 22,682 | 제외/회고·문화·행사 | - | 0/0 | 완벽한 AI 가드레일을 향한 여정: NeurIPS 2025 최신 안전성 기술 분석 |
| ly/ly-corporation-next-generation-cloud-platform-flava-introduction | 7,017 | 추출/기술 선택·도입형 | case_1202, case_1203, case_1204 | 0/22 | LY Corporation의 클라우드 인프라 개편: 거대한 두 개의 클라우드를 통합한 차세대 플랫폼 Flava의 아키텍처 소개 |
| ly/unification-of-group-chat-on-the-line-app | 4,207 | 추출/기술 선택·도입형 | case_1196 | 1/10 | LINE 앱의 다자간 대화 기능 통합 |
| ly/a-large-scale-ios-configuration-system-implemented-with-an-attributedstring-structure | 15,841 | 추출/문제 해결형 | case_1192 | 0/11 | AttributedString 구조로 풀어낸 대규모 iOS 설정 시스템 |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 6,232 | 추출/실험·활용기 | case_1179, case_1180 | 0/16 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 및 서비스 상태 확인 도구 LINE Status 개발기 |
| ly/internalizing-without-specification-proving-equivalence-through-verification-logic | 14,041 | 추출/문제 해결형 | case_1193, case_1194, case_1195 | 0/21 | 기획서 없이 내재화하기: 검증 로직으로 동일함을 증명하다 |
| ly/reduce-repetitive-tasks-with-sre-bot | 12,509 | 추출/문제 해결형 | case_1191 | 1/16 | SRE 팀의 반복 작업을 10분의 1로 줄인 SRE 봇 개발기 |
| ly/advancing-guardrail-models-with-coding-agents | 9,345 | 추출/문제 해결형 | case_1178 | 0/10 | 코딩 에이전트를 활용한 취약점 수집·생성 자동화로 가드레일 모델 고도화 |
| ly/image-content-moderation-at-scale-with-multimodal-llm | 11,837 | 추출/문제 해결형 | case_1183, case_1184, case_1185 | 0/25 | 대규모 서비스 환경에서의 이미지 콘텐츠 모더레이션(feat. 멀티모달 LLM) |
| ly/processing-large-scale-data-with-spark-on-kubernetes | 13,225 | 추출/기술 선택·도입형 | case_1189, case_1190 | 0/21 | LINE 서비스의 대규모 광고 데이터를 처리하기 위한 Spark on Kubernetes 적용기 |
| ly/how-we-built-a-domain-agnostic-chat-platform | 12,338 | 추출/기술 선택·도입형 | case_1181, case_1182 | 0/20 | 도메인에 의존하지 않는 채팅 플랫폼은 어떻게 만들었을까? |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 19,601 | 추출/문제 해결형 | case_1186, case_1187, case_1188 | 1/28 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/start-orchestration-development-workshop | 2,582 | 제외/회고·문화·행사 | - | 0/0 | AI 활용의 열쇠는 '조직적 학습'에 있다 - Orchestration Development Workshop의 시작 |
| ly/orchestration-development-workshop-article-list | 1,592 | 제외/회고·문화·행사 | - | 0/0 | AI 활용 능력을 높이기 위한 사내 워크숍, 'Orchestration Development Workshop' 기사 목록 |
| ly/resolving-pr-review-bottlenecks-with-ai-and-transforming-review-culture | 12,772 | 추출/실험·활용기 | case_1174 | 0/11 | ODW #1: AI로 리뷰 정체를 해소하다 - PR 리뷰 지원과 사내 워크숍으로 리뷰 문화 바꾸기 |
| ly/developing-single-and-multi-agent-systems-with-adk-and-integrating-into-internal-systems | 9,631 | 제외/회고·문화·행사 | - | 0/0 | ODW #2: ADK로 싱글/멀티 에이전트를 개발해 사내 시스템과 통합 |
| ly/improving-development-efficiency-with-secure-mcp-servers | 6,698 | 제외/회고·문화·행사 | - | 0/0 | ODW #3: MCP 서버를 안전하게 활용해 개발 효율 높이기 |
| ly/sli-and-slo-for-improving-reliability-3 | 5,676 | 추출/실험·활용기 | case_1169 | 0/8 | 신뢰성 향상을 위한 SLO/SLI 도입 3편 - 서비스 적용 사례 |
| ly/from-copilot-to-pilot-agentic-coding-implementation-to-pr-automation | 8,339 | 제외/실험·활용기 | - | 0/0 | ODW #4: 코파일럿에서 파일럿으로, 에이전틱 코딩으로 구현부터 PR까지 자동화 |
| ly/id-jag-next-generation-authentication-ai-era | 10,457 | 제외/개념·튜토리얼 | - | 0/0 | AI 시대에 인증 과제를 해결할 차세대 표준 후보, ID-JAG |
| ly/building-rag-system-with-vector-db-and-agent-skills | 3,796 | 추출/실험·활용기 | case_1168 | 0/8 | ODW #5: 벡터 DB와 에이전트 스킬로 RAG 시스템 만들기 |
| ly/ai-augments-qa-rather-than-replacing-it | 16,602 | 추출/실험·활용기 | case_1177 | 0/13 | AI는 QA를 대체하지 않았다, 대신 확장했다 |
| ly/git-automation-mcp-vs-agent-skills-pros-and-cons | 13,859 | 추출/실험·활용기 | case_1176 | 1/9 | ODW #6: Git 자동화 관점에서 본 MCP와 에이전트 스킬의 장단점 |
| ly/cut-token-usage-40-percent-with-adk-context-engineering | 15,919 | 추출/실험·활용기 | case_1175 | 0/10 | ODW #7: 세 가지 방법으로 토큰 소비량 40% 절감! ADK를 이용한 컨텍스트 엔지니어링 |
| ly/introduction-of-messaginghub-inquirychat-service | 15,012 | 추출/기술 선택·도입형 | case_1167 | 0/16 | 도쿄에서 후쿠오카까지, 현장에서 답을 찾다 - CS InquiryChat 도입기 |
| ly/slack-mcp-faq-generation-and-incident-response-support | 7,340 | 제외/회고·문화·행사 | - | 0/0 | ODW #8: Slack MCP로 사고 대응과 FAQ 생성 작업 속도를 높이는 실습형 사내 워크숍 후기 |
| ly/legacy-to-ai-driven-project-ax-roadmap | 13,595 | 추출/기술 선택·도입형 | case_1165 | 0/11 | 레거시 프로젝트에서 AI 드리븐 프로젝트로 전환, AX 로드맵 |
| ly/id-jag-the-hard-way-learning-ai-agent-authz-through-failure | 6,882 | 추출/실험·활용기 | case_1166 | 0/12 | ID-JAG The Hard Way: 실패로 배우는 AI 에이전트 보안 핸즈온 |
| ly/techverse2026-105 | 10,694 | 추출/실험·활용기 | case_1158 | 0/10 | 분석 에이전트의 힘으로 분석을 하나로 연결하다! 전문 조직에서 도전하는 생성 AI 시대의 업무 혁신과 역할 전환 |
| ly/techverse2026-86 | 15,299 | 추출/실험·활용기 | case_1162, case_1163 | 0/17 | 코드형 인프라(IaC)로 자동화에서 AI까지: OpenTofu와 ChatOps 도입기 |
| ly/techverse2026-184 | 19,708 | 추출/문제 해결형 | case_1170, case_1171, case_1172, case_1173 | 0/32 | 총 용량 1EB 초과! 서로 역사가 다른 두 HDFS를 어떻게 연결할까? 데이터 플랫폼 연계 중 직면한 과제와 설계 결정 |
| ly/techverse2026-60 | 13,036 | 추출/실험·활용기 | case_1164 | 1/11 | 프롬프트 튜닝을 수작업에서 AI 튜닝으로: 유전 알고리즘 기반 자동 최적화와 고속화 |
| ly/techverse2026-231 | 12,286 | 제외/기술 선택·도입형 | - | 0/0 | Flava DBaaS 딥다이브: 아키텍처부터 마이그레이션, 그리고 미래까지 |
| ly/techverse2026-59 | 19,425 | 제외/회고·문화·행사 | - | 0/0 | 시멘틱 컨텍스트 OS 설계: 에이전트 시스템의 토큰 스터핑을 넘어 |
| ly/techverse2026-219 | 13,154 | 추출/실험·활용기 | case_1157 | 1/15 | AI 에이전트끼리 토론한다면? 멀티 에이전트 협업으로 재설계하는 개발 프로세스 |
| ly/techverse2026-223 | 18,684 | 추출/문제 해결형 | case_1159, case_1160, case_1161 | 0/23 | AI 시대의 개발 능력은 검증력으로 결정된다, Flava API Gateway 개발 중 배운 빠른 검증과 로컬 환경 구성 전략 |
| ly/techverse2026-10 | 22,943 | 추출/실험·활용기 | case_1156 | 0/12 | 프롬프팅에서 워크플로로, AI로 프런트엔드 개발 생산성 끌어올리기 |
| ly/techverse2026-62 | 6,551 | 추출/문제 해결형 | case_1151 | 0/10 | 임베딩 안정화로 검색 리랭킹의 콜드 스타트 문제를 해결하다: LINE Part Time Jobs 적용 사례 |
| ly/building-group-video-calls-inside-line-app-with-ai-and-line-planet | 22,428 | 추출/실험·활용기 | case_1150 | 0/10 | AI로 웹 엔지니어 없이 LINE 앱 안에서 그룹 영상 통화 서비스 만들기 |
| ly/applying-e2ee-to-apache-kafka-in-line-app | 10,617 | 추출/문제 해결형 | case_1152 | 0/15 | 초당 100만 건, LINE 앱에 Apache Kafka 종단 간 암호화 적용기 |
| ly/developing-harmfulness-detection-model-for-open-chat-metadata | 9,718 | 추출/문제 해결형 | case_1146 | 0/17 | 오픈챗 이름 및 설명 글로 유해성 판단하는 모델 개발하기 |
| ly/android-cli-for-ai-agents-at-scale | 25,994 | 추출/실험·활용기 | case_1153, case_1154, case_1155 | 0/28 | AI 에이전트를 위한 Android CLI: 대규모 모바일 개발 환경에 적용하기 |
| ly/analyzing-incident-root-causes-in-grafana-using-natural-language-with-llm-agent | 14,960 | 추출/문제 해결형 | case_1142 | 0/11 | Grafana에서 자연어로 장애 원인을 분석하기: LLM 에이전트 기반 SRELens 개발기 |
| ly/conditions-for-organizational-aidd-adoption | 6,255 | 제외/실험·활용기 | - | 0/0 | 개인 AI 활용의 다음 단계는 무엇인가 - LY Corporation에서 AIDD 워크숍을 통해 살펴본 AIDD 조직 도입의 조건 |
| ly/ai-agent-platform-sage-dev-log-part-1 | 19,908 | 추출/실험·활용기 | case_1147, case_1148, case_1149 | 1/32 | 보안 업무를 위한 AI 에이전트 플랫폼 「SAGE」 개발기 1편: 판단은 사람에게 남기는 설계 |
| ly/japanese-search-kuromoji-to-sudachi | 15,395 | 추출/기술 선택·도입형 | case_1136 | 0/12 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kuromoji에서 OpenSearch + Sudachi로 |
| ly/llm-wiki-code-driven-knowledge-ssot | 10,057 | 추출/실험·활용기 | case_1139 | 0/10 | LLM Wiki: 코드 기준으로 자동 최신화되는 도메인 지식 SSOT 만들기 |
| ly/building-sre-observer-for-alert-root-cause-analysis | 15,127 | 추출/문제 해결형 | case_1143, case_1144, case_1145 | 0/27 | 장애 Alert의 원인을 스스로 찾다: SRE Observer 개발기 |
| ly/tech-verse-2026-ai-driven-development-review | 5,266 | 제외/회고·문화·행사 | - | 0/0 | AI를 전제로 다시 설계하다, Tech-Verse 2026 참관기 |
| ly/ai-agent-ad-report-automation | 15,930 | 추출/실험·활용기 | case_1140, case_1141 | 0/20 | LLM에게 어디까지 맡길 것인가: AI 에이전트 기반 광고 분석 리포트 자동화 |
| oliveyoung/2023-08-31_circuitbreaker-inventory-squad | 16,937 | 추출/문제 해결형 | case_1596 | 0/11 | Circuitbreaker를 사용한 장애 전파 방지 |
| oliveyoung/2023-09-18_address-modal | 11,867 | 추출/기술 선택·도입형 | case_1594 | 0/9 | 새 배송지 추가 form 개발하기 |
| oliveyoung/2023-09-18_oliveyoung-coupon-rabbit | 2,012 | 추출/기술 선택·도입형 | case_1595 | 0/9 | 쿠폰 발급 RabbitMQ도입기 |
| oliveyoung/2023-09-25_oliveyoung-b2b-logistics-front-improvement | 3,258 | 추출/문제 해결형 | case_1597 | 0/13 | B2B 물류 스쿼드 백오피스 프론트엔드 성능 개선 |
| oliveyoung/2023-06-23_job-challenge-oliveyoung | 5,620 | 추출/실험·활용기 | case_1585 | 0/8 | 올리브영 잡 챌린지! 프론트엔드 개발자로의 전환 |
| oliveyoung/2023-09-27_oliveyoung-favorite-snack | 1,395 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자가 좋아하는 과자는? |
| oliveyoung/2023-10-04_inventory-project | 7,785 | 추출/기술 선택·도입형 | case_1590, case_1591, case_1592, case_1593 | 0/19 | 신규 재고 시스템 구축을 위한 개발 여정 |
| oliveyoung/2023-10-04_oliveyoung-b2b-msk-connect-introduction | 13,333 | 추출/실험·활용기 | case_1581 | 0/11 | AWS MSK Connect 효과적으로 운영하기 |
| oliveyoung/2023-10-04_useInfiniteQuery-scroll | 11,758 | 추출/문제 해결형 | case_1588, case_1589 | 0/14 | useInfiniteQuery로 무한스크롤 구현하기 |
| oliveyoung/2023-10-10_oliveyoung-pickup-cart | 2,926 | 추출/문제 해결형 | case_1586 | 1/9 | 픽업전용 장바구니 |
| oliveyoung/2023-10-11_developer-hobby | 1,871 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 개발자의 슬기로운 취미생활 |
| oliveyoung/2023-10-11_kotlin-detekt-reviewdog | 6,002 | 추출/기술 선택·도입형 | case_1578 | 0/9 | detekt와 reviewdog으로 코드 품질 향상 |
| oliveyoung/2023-10-11_offline-store-settlement | 1,938 | 제외/문제 해결형 | - | 0/0 | 올리브영 매장 정산 이야기 |
| oliveyoung/2023-10-17_oliveyoung-mall-home-new-architecture | 5,815 | 추출/문제 해결형 | case_1582, case_1583, case_1584 | 0/23 | 올리브영 온라인몰의 전시, 그리고 백엔드 여정 |
| oliveyoung/2023-10-11_settlement-floation-point | 5,616 | 제외/개념·튜토리얼 | - | 0/0 | 부동소수점 이야기 |
| oliveyoung/2023-10-20_claim-code | 2,218 | 추출/문제 해결형 | case_1587 | 0/11 | 잃어버린 클레임 데이터를 찾아서 |
| oliveyoung/2023-10-20_mouse | 7,378 | 추출/실험·활용기 | case_1580 | 0/8 | 마우스 드래그로 범위 지정과 리사이징 및 이동 구현하기 |
| oliveyoung/2023-10-28_oliveyoung-javascript-turbofan | 4,884 | 제외/개념·튜토리얼 | - | 0/0 | 자바스크립트 이렇게 짜면 외않되? |
| oliveyoung/2023-10-30_wcare-tdd-development | 10,183 | 추출/실험·활용기 | case_1577 | 0/10 | W CARE 서비스 프론트엔드를 TDD로 개발해본 후기 |
| oliveyoung/2023-11-07_ranking-system | 7,794 | 추출/기술 선택·도입형 | case_1579 | 0/12 | 랭킹 시스템 개편기 |
| oliveyoung/2023-11-11_qa | 6,554 | 추출/문제 해결형 | case_1576 | 0/7 | UI 테스트 자동화 구조 |
| oliveyoung/2023-11-15_swift-macro-part1 | 1,941 | 제외/개념·튜토리얼 | - | 0/0 | 스위프트 매크로_1탄, 스위프트 매크로가 뭐예요? |
| oliveyoung/2023-10-02_c10-problem | 4,689 | 제외/개념·튜토리얼 | - | 0/0 | 고전 돌아보기, C10K 문제 (C10K Problem) |
| oliveyoung/2023-11-30_journey-to-joining-oliveyoung | 5,192 | 제외/회고·문화·행사 | - | 0/0 | 주니어 개발자의 우당탕탕 입사기 |
| oliveyoung/2023-12-05_partner-platform-code-convention | 4,387 | 추출/실험·활용기 | case_1574 | 0/7 | 파트너플랫폼 스쿼드 코드 컨벤션 소개 🌼 |
| oliveyoung/2023-12-13_retail-platform-team-study | 2,641 | 제외/회고·문화·행사 | - | 0/0 | 팀 스터디, 1년간의 여정 |
| oliveyoung/2023-12-15_seller-service-1 | 5,156 | 추출/문제 해결형 | case_1572 | 0/11 | 외부셀러 - 외부 스파크성 트래픽으로부터 내부 시스템을 보호하는 방법 1탄 |
| oliveyoung/2023-12-18_data-export | 7,493 | 추출/문제 해결형 | case_1573 | 0/11 | 확장할 수 있는 데이터 추출 서비스 구축 경험 공유 |
| oliveyoung/2023-12-19_self-checkout | 2,877 | 추출/기술 선택·도입형 | case_1575 | 0/12 | 올리브영 셀프계산대 도입기 |
| oliveyoung/2023-11-29_why-the-retail-platform-team-refactored | 6,303 | 추출/문제 해결형 | case_1571 | 0/12 | 파트너오피스 리뉴얼, 왜 우리는 리팩터링을 하였는가? |
| oliveyoung/2024-01-05_oliveyoung-oci-transform-order | 3,683 | 추출/문제 해결형 | case_1570 | 0/9 | 오라클 클라우드 전환 - 올리브영 주문 서비스 사전 점검기 |
| oliveyoung/2024-01-15_swift-macro-part2 | 2,378 | 추출/실험·활용기 | case_1567 | 0/7 | 스위프트 매크로_2탄, 어떻게 쓰는건데요? |
| oliveyoung/2024-01-23_msw-frontend | 16,414 | 추출/문제 해결형 | case_1569 | 0/13 | Next.js에서 MSW(Mock Service Worker)로 네트워크 Mocking하기 |
| oliveyoung/2024-01-23_incident | 2,930 | 추출/문제 해결형 | case_1563 | 0/10 | 올리브영은 인시던트를 어떻게 관리하고 있는가? |
| oliveyoung/2024-03-11_msk-cdc-debezium | 13,073 | 추출/기술 선택·도입형 | case_1568 | 0/9 | 상품데이터 Pipeline을 위한 Debezium MSK Connect |
| oliveyoung/2024-03-29_oliveyoung-aws-reinvent2023 | 2,297 | 제외/회고·문화·행사 | - | 0/0 | AWS re:Invent 2023 방문기 |
| oliveyoung/2024-04-01_goods-detail-description-improvement | 5,285 | 추출/문제 해결형 | case_1566 | 0/9 | 상품 설명 영역 개선기 Part.1 |
| oliveyoung/2024-04-01_testcode-use-fixture-monkey | 11,669 | 추출/기술 선택·도입형 | case_1565 | 0/10 | TestFixture를 쉽게 생성해 주는 라이브러리가 있다? |
| oliveyoung/2024-04-02_app-improve-camera-scan | 6,580 | 추출/문제 해결형 | case_1561 | 0/8 | 올리브영 앱 스마트 스캐너 개선 |
| oliveyoung/2024-04-02_opensearch-efk | 17,576 | 추출/실험·활용기 | case_1562 | 0/11 | AWS OpenSearch 기반 EFK Stack 구축기 |
| oliveyoung/2024-04-11_Datadog_QA | 5,205 | 추출/실험·활용기 | case_1559 | 0/9 | 올리브영 QA는 Datadog을 어떻게 활용하고 있을까? |
| oliveyoung/2024-04-19_pos-modernization | 4,014 | 추출/문제 해결형 | case_1564 | 1/14 | 올리브영 POS 서버 Modernization |
| oliveyoung/2024-05-20_oliveyoung-qa-oncall | 4,015 | 추출/문제 해결형 | case_1558 | 0/10 | 올리브영 QA의 AWS Lambda를 통한 On call 도입기 |
| oliveyoung/2024-06-05_google-cloud-next-24-review | 3,796 | 제외/회고·문화·행사 | - | 0/0 | Google Cloud Next '24 방문기 |
| oliveyoung/2024-06-12_goods-detail-description-improvement-par2 | 4,317 | 추출/문제 해결형 | case_1555 | 0/11 | 상품 설명 영역 개선기 Part.2 |
| oliveyoung/2024-06-16_next-cdn-standalone | 2,824 | 추출/실험·활용기 | case_1556, case_1557 | 0/14 | NEXT.JS와 CDN, 그리고 도커 이미지 경량화 |
| oliveyoung/2024-06-25_oliveyoung-order-payment-part4 | 3,003 | 추출/실험·활용기 | case_1550 | 0/8 | 올리브영 결제 이야기 Part - 4 |
| oliveyoung/2024-07-04_image-upload-speed-optimization | 6,512 | 추출/문제 해결형 | case_1548 | 0/12 | 올리브영 셔터 이미지 업로드 성능 개선기 |
| oliveyoung/2024-07-31_oliveyoung-datadog-dash2024 | 4,385 | 제외/회고·문화·행사 | - | 0/0 | 뉴욕 DASH2024에서 전파한 올리브영의 데이터독 활용 사례 |
| oliveyoung/2024-08-02_olea-bo-template | 6,792 | 추출/기술 선택·도입형 | case_1545 | 0/9 | OLEA? Storybook을 활용한 올리브영의 디자인 시스템! |
| oliveyoung/2024-07-05_dash-2024-slide | 10,410 | 추출/실험·활용기 | case_1549 | 0/12 | DASH 2024,올리브영은 어떻게 Datadog으로 비즈니스를 모니터링하는가? |
| oliveyoung/2024-08-11_type-and-type-system-with-typescript | 11,673 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 타입과 타입 시스템 |
| oliveyoung/2024-09-06_introduce-oy-po | 8,064 | 제외/실험·활용기 | - | 0/0 | 올리브영이 커뮤니티와 콘텐츠를 만드는 진짜 이유 |
| oliveyoung/2024-09-11_introduce-oy-ai-bedrock | 5,664 | 추출/실험·활용기 | case_1560 | 0/14 | AWS Bedrock과 Claude 3.5 Sonnet을 활용한 자동 상품 이미지 검수 시스템 구축기 |
| oliveyoung/2024-09-30_oy-feconf-2024 | 8,894 | 제외/회고·문화·행사 | - | 0/0 | 올리브영에서는 프론트엔드 개발자들이 이런 고민을 하는군요? |
| oliveyoung/2024-10-16_oliveyoung-scm-oms-kafka | 11,362 | 추출/문제 해결형 | case_1551, case_1552, case_1553, case_1554 | 0/30 | Kafka 메시지 중복 및 유실 케이스별 해결 방법 |
| oliveyoung/2024-10-17_oy-delivery-mq | 4,642 | 추출/기술 선택·도입형 | case_1547 | 1/12 | 올리브영 물류시스템에서는 데이터를 어떻게 주고 받을까? |
| oliveyoung/2024-10-30_application_warmup_algorithm | 7,710 | 추출/문제 해결형 | case_1546 | 0/9 | 커스텀 어노테이션과 리플렉션으로 구현한 Spring Boot 웜업 로직 최적화 |
| oliveyoung/2024-11-01_planshop-renewal | 12,217 | 추출/문제 해결형 | case_1542, case_1543 | 0/15 | Front-end 개발자가 회고하는 기획전 개편 |
| oliveyoung/2024-11-06_who-caused-our-batch-to-stop | 6,789 | 추출/문제 해결형 | case_1544 | 1/11 | 그날, 우리의 배치는 왜 멈추었을까? |
| oliveyoung/2024-11-07_cdc-failover | 14,225 | 추출/문제 해결형 | case_1540, case_1541 | 0/15 | Debezium MSK Connect로 Failover 구현하여 서비스 안정성 높이기 |
| oliveyoung/2024-11-15_inventory-changed-stocks-function-with-redis-stream | 6,589 | 추출/문제 해결형 | case_1539 | 0/7 | 재고의 변동을 시계열 데이터로?! |
| oliveyoung/2024-11-28_gift-renewal | 3,647 | 추출/문제 해결형 | case_1536 | 0/8 | 올리브영은 왜 선물하기를 개편했을까? Part - 1 |
| oliveyoung/2024-11-22_designsystem-development | 8,615 | 추출/실험·활용기 | case_1535 | 0/8 | 올리브영 서비스에 사용되는 컴포넌트를 모아놓은 그곳! |
| oliveyoung/2024-12-02_oliveyoung-settlement-overhaul-resource-savings | 3,828 | 추출/문제 해결형 | case_1537 | 0/11 | 올리브영 온라인몰 정산개편 이야기 |
| oliveyoung/2024-12-06_sco-teamcity | 4,925 | 추출/문제 해결형 | case_1538 | 0/10 | TeamCity로 윈도우 클라이언트 배포 파이프라인 만들기 |
| oliveyoung/2024-12-08_kotlin-advantages | 14,234 | 제외/개념·튜토리얼 | - | 0/0 | Java를 주로 다루는 개발자가 생각하는 Kotlin 장점 🌼 |
| oliveyoung/2024-12-10_present-promotion-multi-layer-cache | 8,351 | 추출/문제 해결형 | case_1532 | 0/9 | 고성능 캐시 아키텍처 설계 - 로컬 캐시와 Redis로 대규모 증정 행사 관리 최적화 |
| oliveyoung/2024-12-11_oliveyoung-coupon-mess-issue | 3,832 | 추출/문제 해결형 | case_1530 | 0/8 | 올리브영 초대량 쿠폰 발급 시스템 개선기 |
| oliveyoung/2024-12-16_Design-System-Token-Automation | 17,955 | 추출/실험·활용기 | case_1526 | 0/9 | 디자인 시스템 중 디자인 토큰을 여러 도구를 이용하여 자동화 하는 방법 |
| oliveyoung/2024-12-17_catalog-mongo-transaction-2 | 11,450 | 추출/문제 해결형 | case_1524, case_1525 | 0/18 | Spring Boot MongoDB 트랜잭션 도입 실전 가이드 |
| oliveyoung/2024-12-22_member-upgrade-renewal | 4,812 | 추출/문제 해결형 | case_1533, case_1534 | 0/16 | 스마트 승급 시스템, 회원 승급 자동화의 혁신 스토리 |
| oliveyoung/2024-12-30_oliveyoung-order-pay-method | 4,636 | 추출/실험·활용기 | case_1519 | 0/7 | 올리브영 결제수단 연동, 이렇게만 하면 끝! |
| oliveyoung/2025-01-05_csp_auto_test | 6,527 | 추출/문제 해결형 | case_1531 | 0/14 | CSP를 중심으로 본 자동화 테스트 실전 사례 |
| oliveyoung/2025-01-24_store-service-journey-1 | 5,037 | 추출/기술 선택·도입형 | case_1520 | 0/9 | 10년 된 레거시를 현대화하다 - Part.1: 도메인 분리의 첫걸음 |
| oliveyoung/2025-01-24_store-service-journey-2 | 10,749 | 추출/기술 선택·도입형 | case_1521, case_1522, case_1523 | 0/20 | 10년 된 레거시를 현대화하다 - Part.2: 매장 도메인의 구현 여정 |
| oliveyoung/2025-02-03_monstache-journey | 4,428 | 추출/문제 해결형 | case_1518 | 0/9 | Monstache로 DocumentDB와 OpenSearch 동기화하기 |
| oliveyoung/2025-02-14_oy-global-mall-address | 4,978 | 추출/기술 선택·도입형 | case_1511 | 0/9 | 올리브영 글로벌몰 주소 자동완성 및 검증 솔루션 도입기 |
| oliveyoung/2025-02-26_letswift2024-review | 4,063 | 제외/회고·문화·행사 | - | 0/0 | Let'Swift 2024 X 올리브영: 기술과 경험을 나누는 특별한 만남 |
| oliveyoung/2025-02-28_oy-workshop-2024 | 9,815 | 제외/회고·문화·행사 | - | 0/0 | 사용자 경험 개선을 위한 올리브영 테크팀 아이디어톤 현장 전격 공개! |
| oliveyoung/2025-03-28_swift-docc | 9,741 | 추출/실험·활용기 | case_1512 | 0/9 | iOS 개발자를 위한 DocC 실무 튜토리얼 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 7,158 | 추출/문제 해결형 | case_1517 | 0/13 | Web Worker로 이미지 처리 최적화하기 |
| oliveyoung/2025-04-30_store-service-journey-3 | 8,555 | 추출/문제 해결형 | case_1513, case_1514, case_1515 | 0/20 | 10년 된 레거시를 현대화하다 - Part.3: 대고객 서비스로의 확장 |
| oliveyoung/2025-05-23_app-review-system | 13,320 | 추출/문제 해결형 | case_1516 | 0/12 | 유저의 소리를 듣는 법: 앱 리뷰 수신 시스템 개발기 |
| oliveyoung/2025-05-29_dplot-qa-docs | 4,970 | 추출/문제 해결형 | case_1509 | 0/10 | 1인 QA의 품질 관리 프로세스 구축 이야기 |
| oliveyoung/2025-05-29_short-form-content | 7,045 | 추출/문제 해결형 | case_1527, case_1528, case_1529 | 0/26 | HLS 기반 숏폼 스트리밍 구현기: iOS/Android 호환성 대응 사례 |
| oliveyoung/2025-06-02_itemlm | 6,012 | 추출/실험·활용기 | case_1508 | 0/10 | 올리브영 사용자 행동 데이터로 학습한 상품 유사도 언어 모델: 전통적 속성 기반 추천을 넘어선 의미론적 유사도 모델링 |
| oliveyoung/2025-06-10_chaos | 7,289 | 추출/문제 해결형 | case_1507 | 0/13 | 버그가 아니라 장애를 잡아라!! QA와 카오스 엔지니어링의 만남 |
| oliveyoung/2025-06-19_journey-to-joining-oliveyoung-qa | 8,355 | 제외/회고·문화·행사 | - | 0/0 | iOS 개발자가 올리브영 QA 엔지니어가 되기까지, 5개월간의 리얼 온보딩 |
| oliveyoung/2025-06-25_aws-summit-recap | 6,106 | 제외/회고·문화·행사 | - | 0/0 | AWS Summit Seoul 2025 발표 후기 - 소중한 우리의 시간을 위한 클라우드 스케일링 자동화 |
| oliveyoung/2025-06-27_adding-datadog-to-pos-system | 5,972 | 추출/문제 해결형 | case_1496 | 0/13 | 전국 3,500대 POS 실시간 모니터링 구축기 |
| oliveyoung/2025-06-30_purchase-order-service | 15,970 | 추출/문제 해결형 | case_1510 | 0/14 | 비동기 요청-응답 패턴으로 풀어낸 발주 서비스 개발기 |
| oliveyoung/2025-07-03_transaction-product-team-introduction | 6,007 | 제외/회고·문화·행사 | - | 0/0 | 올리브영의 트랜잭션프로덕트팀을 소개합니다 |
| oliveyoung/2025-07-09_w-care-product-evolution | 4,164 | 추출/문제 해결형 | case_1502 | 0/12 | “그날”을 그냥 넘기지 않기로 했어요 |
| oliveyoung/2025-07-22_what-is-MFE-part1 | 10,493 | 제외/개념·튜토리얼 | - | 0/0 | 대규모 프론트엔드 아키텍처의 새로운 패러다임 - Part 1. 마이크로프론트엔드 너 뭐야? |
| oliveyoung/2025-07-23_gms-open-story | 8,723 | 추출/문제 해결형 | case_1503, case_1504, case_1505, case_1506 | 0/27 | 제로베이스 WMS 구축기: Kafka 기반 분산 물류 시스템 설계와 Out-of-Order Events 해결 |
| oliveyoung/2025-07-23_redis-tips-for-developer | 6,442 | 추출/실험·활용기 | case_1493 | 0/9 | 개발자가 알면 좋은 Redis 꿀팁 모음 |
| oliveyoung/2025-07-30_scroll-restoration | 9,944 | 추출/문제 해결형 | case_1492 | 0/10 | 프론트엔드 개발자를 위한 5가지 스크롤 복구 시나리오와 실전 코드 팁 |
| oliveyoung/2025-07-30_squad-description | 3,693 | 제외/회고·문화·행사 | - | 0/0 | 우리 스쿼드에서 같이 일하실래요? |
| oliveyoung/2025-08-01_logistics-system | 8,475 | 추출/기술 선택·도입형 | case_1497, case_1498, case_1499, case_1500, case_1501 | 0/32 | 올리브영 물류 시스템의 진화 - 고객 경험의 시작과 끝을 함께하다 |
| oliveyoung/2025-08-04_gift-renewal-2 | 26,112 | 추출/문제 해결형 | case_1494, case_1495 | 0/16 | 올리브영은 왜 선물하기를 개편했을까? Part - 2 |
| oliveyoung/2025-08-07_po-onboarding-first-4-weeks | 3,698 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 PM 온보딩, 긴장 대신 설레임이 남았어요 |
| oliveyoung/2025-08-20_amazonq-vscode | 7,731 | 추출/실험·활용기 | case_1488 | 0/10 | Visual Studio Code를 Cursor처럼? Amazon Q로 AI 코딩 환경 업그레이드하기 |
| oliveyoung/2025-08-28_springcamp_2025 | 5,355 | 제외/회고·문화·행사 | - | 0/0 | 외부 백엔드 커뮤니티와 함께 한 올리브영의 SpringCamp 2025 참가 후기 |
| oliveyoung/2025-08-29_pos-pick-insights | 4,035 | 제외/회고·문화·행사 | - | 0/0 | PM’s Pick : 우리가 스크랩한 인사이트 |
| oliveyoung/2025-09-04_article-editor | 5,506 | 추출/기술 선택·도입형 | case_1486, case_1487 | 0/14 | 올리브영, 블록 기반 CMS로 콘텐츠 제작 시간을 99% 줄이다 |
| oliveyoung/2025-09-08_gms-qa-strategy | 8,591 | 추출/문제 해결형 | case_1489, case_1490, case_1491 | 0/23 | 빅뱅 배포, QA는 어떻게 살아 남았나: GMS 프로젝트 테스트 전략 백서 |
| oliveyoung/2025-09-24_API-testing-v1 | 13,748 | 추출/문제 해결형 | case_1485 | 0/11 | 메시징 시스템 QA, 정합성을 지켜낸 올리브영의 이야기 |
| oliveyoung/2025-09-24_wms-pda-web-app | 6,765 | 추출/문제 해결형 | case_1483 | 0/10 | "이 버튼 왜 안 눌려요?" 물류 현장의 목소리로 PDA 시스템 완성하기 |
| oliveyoung/2025-10-02_olip-session-specialist-or-generalist | 2,491 | 제외/회고·문화·행사 | - | 0/0 | [올리프 세션 스케치] 당신은 스페셜리스트인가요? 제너럴리스트인가요? |
| oliveyoung/2025-10-17_review-of-orderpay-squad | 5,747 | 제외/회고·문화·행사 | - | 0/0 | KPT 회고, 이렇게 했더니 스쿼드 문화가 바뀌었습니다: 올리브영 주문결제 스쿼드의 애자일 성장기 |
| oliveyoung/2025-10-28_coupon-mq-issue | 9,578 | 추출/문제 해결형 | case_1484 | 0/13 | RabbitMQ Classic Queue 메모리 장애와 Quorum Queue 전환기 |
| oliveyoung/2025-10-30_po-leadership-starting-point | 2,707 | 제외/회고·문화·행사 | - | 0/0 | PM의 리더십은 언제부터 시작될까? |
| oliveyoung/2025-11-04_server-driven-technical-exploration | 9,939 | 추출/기술 선택·도입형 | case_1482 | 0/14 | SDUI로 네이티브 운영 민첩성 높이기 |
| oliveyoung/2025-11-04_spring-cloud-config-server | 5,505 | 추출/기술 선택·도입형 | case_1478 | 0/9 | Spring Cloud Config & Bus-Refresh 도입기 |
| oliveyoung/2025-11-06_claim-Procedure | 4,558 | 추출/문제 해결형 | case_1468 | 0/10 | 7,000줄 PL/SQL 프로시저와의 결별: 클레임 로직 Java 모듈 이관기 |
| oliveyoung/2025-11-06_swiftui-developer-mode | 8,739 | 추출/문제 해결형 | case_1479, case_1480 | 0/14 | 하이브리드 앱에 구축하는 iOS 개발자모드 |
| oliveyoung/2025-11-06_what-is-MFE-part2 | 15,441 | 추출/실험·활용기 | case_1476 | 0/11 | 대규모 프론트엔드 아키텍처의 새로운 패러다임 - Part 2. 모듈 페더레이션 PoC |
| oliveyoung/2025-11-10_what-is-MFE-part3 | 11,404 | 제외/개념·튜토리얼 | - | 0/0 | 대규모 프론트엔드 아키텍처의 새로운 패러다임 - Part 3. Nx를 활용한 마이크로프론트엔드 |
| oliveyoung/2025-11-11_sdui_with_caffein | 7,851 | 추출/문제 해결형 | case_1467 | 0/10 | SDUI의 성능 병목을 넘어: 올리브영 로컬 캐시 기반 백엔드 최적화 성공기 |
| oliveyoung/2025-11-28_po-day-in-the-life | 2,159 | 제외/회고·문화·행사 | - | 0/0 | 올리브영 PM이 일하는 방식 — PM의 하루 구경하기 |
| oliveyoung/2025-12-01_o2o_delivery | 6,276 | 추출/문제 해결형 | case_1469, case_1470, case_1471 | 0/19 | 배달대행사 API 연동과 장애 대응 - 오늘드림 서비스 개발기 |
| oliveyoung/2025-12-08_creating-video-with-ai | 11,759 | 추출/실험·활용기 | case_1481 | 0/13 | QA 엔지니어가 AI로 만든 교육 영상, 25분짜리 인시던트 가이드 탄생기 |
| oliveyoung/2025-12-08_iframe-postmessage-authentication | 10,439 | 추출/문제 해결형 | case_1477 | 0/14 | iframe으로 웹앱 통합했더니 토큰 요청이 폭발했다 |
| oliveyoung/2025-12-15_fcfs-coupon | 8,292 | 추출/문제 해결형 | case_1466 | 0/11 | 올영세일 선착순 쿠폰, 미발급 0%를 향한 여정 |
| oliveyoung/2025-12-15_kafka-streams-for-out-of-stock | 8,553 | 추출/문제 해결형 | case_1465 | 0/10 | Kafka Streams 기반 EDA 구축 사례: 올리브영 품절 시스템 현대화 프로젝트 |
| oliveyoung/2025-12-17_QA-Conference-2025 | 9,265 | 제외/회고·문화·행사 | - | 0/0 | QA Built on Trust - 팀워크가 품질을 만든다 |
| oliveyoung/2025-12-24_amazon-connect | 9,265 | 추출/문제 해결형 | case_1472, case_1473, case_1474, case_1475 | 2/27 | 운영 비용을 95% 절감한 서버리스 온콜 시스템 구축기 |
| oliveyoung/2025-12-24_dev-prod-app-environment-separation | 8,329 | 추출/기술 선택·도입형 | case_1459 | 0/11 | 한 기기에 개발·운영 앱을 동시에 설치하는 방법: 올리브영 DEV/PROD 환경 분리 |
| oliveyoung/2025-12-26_protection-switch | 10,618 | 추출/문제 해결형 | case_1460 | 0/12 | 권한마다 보안 솔루션이 다르다면? 하이브리드 환경에서 우아하게 파일 보호하기 |
| oliveyoung/2025-12-29_campaign-worekr_review | 10,086 | 추출/문제 해결형 | case_1461, case_1462 | 0/19 | 올리브영의 실시간 캠페인 타겟팅을 위한 CDC 전환기 |
| oliveyoung/2025-12-30_alimtalk_improve_event_driven_architecture | 16,155 | 추출/문제 해결형 | case_1458 | 0/12 | SQS 기반 알림톡 처리에서 발생한 DB 커넥션 데드락 분석기 |
| oliveyoung/2025-12-31_cj-product-makers-day | 3,779 | 제외/회고·문화·행사 | - | 0/0 | CJ 계열사 PM/PO가 올리브영 N 성수에 모인 이유: CJ Product Makers Day |
| oliveyoung/2025-12-31_generics-and-parametric-polymorphism | 14,942 | 제외/개념·튜토리얼 | - | 0/0 | 올리브영 타입스크립트로 알아보는 제네릭과 매개변수 다형성 |
| oliveyoung/2026-01-21_oy_sllm | 14,577 | 추출/실험·활용기 | case_1463, case_1464 | 0/23 | T4 GPU 1장으로 일궈낸 올리브영의 Gemma 3 기반 sLLM 구축기 |
| oliveyoung/2025-10-28_oliveyoung-zero-downtime-oauth2-migration | 14,957 | 추출/문제 해결형 | case_1453, case_1454, case_1455 | 0/25 | 올리브영 대규모 트래픽 레거시 시스템의 무중단 OAuth2 전환기 |
| oliveyoung/2026-02-09_esl-series-1 | 6,080 | 추출/기술 선택·도입형 | case_1444 | 0/10 | 오프라인 매장에 코드를 배포하다 Part 1: 종이 없는 매장을 만드는 데이터 파이프라인 구축 |
| oliveyoung/2026-02-10_esl-series-2 | 4,574 | 추출/문제 해결형 | case_1448, case_1449 | 0/13 | 오프라인 매장에 코드를 배포하다 Part 2: 올리브영 전자라벨(ESL) 최적화 여정 |
| oliveyoung/2026-02-23_from-legacy-to-modern-architecture-journey | 7,966 | 추출/문제 해결형 | case_1445, case_1446 | 0/19 | Spring 트랜잭션 동기화로 레거시 알림톡 발송 시스템 한계 넘어서기 |
| oliveyoung/2026-02-27_2026-02-27-oliveyoung-store-journey-renewal-ux | 7,846 | 제외/실험·활용기 | - | 0/0 | 매장을 찾는 과정을 설계한 올영매장 고도화 여정 |
| oliveyoung/2026-03-06_delivery-optimization | 9,147 | 추출/기술 선택·도입형 | case_1442, case_1443 | 0/19 | 배송최적화 시스템 구축기 Part 01. 올리브영이 멀티 센터 체제로 배송 시간을 14시간 단축한 과정 |
| oliveyoung/2026-03-18_oy-store-data-interconnection-strategy | 5,708 | 추출/실험·활용기 | case_1456, case_1457 | 0/17 | 올영매장은 MSA 환경에서 흩어진 도메인 데이터를 어떻게 연동했을까? |
| oliveyoung/2026-03-30_chaos-host-level | 11,756 | 추출/실험·활용기 | case_1450, case_1451, case_1452 | 0/22 | QA가 서버를 죽여본 이유 – Host Level 카오스 엔지니어링 테스트 |
| oliveyoung/2026-04-08_product-center-connect-the-dots-workshop | 6,012 | 제외/회고·문화·행사 | - | 0/0 | 120개의 점을 잇다: 프로덕트센터 ‘Connect the Dots’ 워크숍 비하인드 |
| oliveyoung/2026-04-09_oy-tech-workshop | 11,934 | 제외/회고·문화·행사 | - | 0/0 | 하루 동안 디지털 마법사가 된 올리브영 개발자들, 2026년의 비전과 전략을 몸소 경험하다 |
| oliveyoung/2026-04-16_oliveyoung-tech-ai-dlc-workshop | 9,284 | 추출/실험·활용기 | case_1441 | 0/10 | AI와 협업하는 새로운 개발 프로세스, 올리브영은 어떻게 시작했을까 (feat. AI-DLC) |
| oliveyoung/2026-04-22_display-benefits-migration | 9,558 | 추출/문제 해결형 | case_1447 | 0/13 | 45분 배치에서 준실시간으로! 다수 도메인 데이터를 Kafka로 통합한 전환기 |
| oliveyoung/2026-04-24_global-center-tech-workshop | 8,702 | 제외/회고·문화·행사 | - | 0/0 | 150개국 K-뷰티 플랫폼 뒤의 팀, 올리브영 글로벌엔지니어링센터의 첫 번째 워크숍 이야기 |
| oliveyoung/2026-06-30_product-monitoring-evolution | 6,119 | 추출/문제 해결형 | case_1434 | 0/11 | 에러로그 하나에 깨던 새벽에서 벗어나기까지 — 상품 모니터링 진화기 |
| oliveyoung/2026-07-01_inventory-pipeline | 5,376 | 추출/문제 해결형 | case_1438, case_1439, case_1440 | 0/15 | 옴니채널 재고 정합성 한계에 대응하는 인벤토리 데이터 파이프라인 구축기 |
| oliveyoung/2026-07-14_building-integrated-backoffice-with-vue-web-components | 11,083 | 추출/기술 선택·도입형 | case_1433 | 0/13 | 프레임워크에 구애받지 않는 통합 백오피스 구축하기 |
| oliveyoung/2026-07-24_offline-payment-upgrade-phase1 | 5,591 | 추출/문제 해결형 | case_1432 | 0/12 | 고객의 1초를 줄이기 위해, POS 결제 구조를 다시 설계하다 |
| oliveyoung/2026-08-28_search-mcp | 18,611 | 추출/문제 해결형 | case_1435, case_1436, case_1437 | 0/22 | 프롬프트를 쓰는 PM과 AI를 이해시키려는 개발자 |
| oliveyoung/2026-08-31_a-lunch-that-builds-collaboration-culture | 4,359 | 제외/회고·문화·행사 | - | 0/0 | 한 끼의 점심이 협업 문화를 만든다면? |
| oliveyoung/2026-09-04_delivery-optimization-design-pattern | 10,940 | 추출/문제 해결형 | case_1430 | 0/10 | 배송최적화 시스템 구축기 Part 02. 복잡한 비즈니스 로직에 유연한 디자인 패턴 입히기 |
| oliveyoung/2026-09-14_global-store-new-way-of-working | 9,809 | 추출/문제 해결형 | case_1423 | 0/12 | 리드타임 3일, 글로벌 매장 개발자가 출장지에서 일하는 법 |
| oliveyoung/2026-09-18_oy_sllm_alignment | 15,441 | 추출/실험·활용기 | case_1424 | 0/12 | 측정할 수 없으면 개선할 수 없다 - AI Pick 추천 카드를 위한 sLLM 정렬 학습기 |
| oliveyoung/2026-09-23_order-cancellation-shipping-ready | 10,663 | 추출/문제 해결형 | case_1422 | 0/13 | 고객의 취소할 권리를 보장하다 |
| oliveyoung/2026-09-23_overengineering-message-system | 10,795 | 추출/문제 해결형 | case_1428, case_1429 | 0/25 | 때로는 오버엔지니어링이 필요합니다 |
| toss/isomorphic-javascript | 3,962 | 추출/문제 해결형 | case_0489 | 0/8 | 환경 고민없이 개발하기 |
| toss/slash23-security | 5,366 | 추출/기술 선택·도입형 | case_0492 | 0/11 | 금융사 최초의 Zero Trust 아키텍처 도입기 |
| toss/frontend-diving-club-agora | 2,605 | 제외/회고·문화·행사 | - | 0/0 | 프론트엔드 다이빙클럽에서 만나는 아고라: 다른 회사에선 테스트 코드 어떻게 짜요? |
| toss/slash23-data | 7,570 | 추출/문제 해결형 | case_0497, case_0498, case_0499 | 0/20 | 대규모 로그 처리도 OK! Elasticsearch 클러스터 개선기 |
| toss/slash23-devops | 6,543 | 추출/문제 해결형 | case_0490 | 0/11 | 유연하고 안전하게 배포 Pipeline 운영하기 |
| toss/slash23-server | 5,747 | 추출/실험·활용기 | case_0491 | 0/12 | 토스는 Gateway 이렇게 씁니다 |
| toss/engineering-note-1 | 6,456 | 추출/문제 해결형 | case_0488 | 0/12 | 웹에서 복잡한 퍼널 쉽게 관리하기 |
| toss/engineering-note-2 | 6,702 | 추출/문제 해결형 | case_0484 | 0/9 | null 리턴은 왜 나쁠까? |
| toss/engineering-note-3 | 7,996 | 추출/문제 해결형 | case_0485 | 0/9 | Feign 코드 분석과 서버 성능 개선 |
| toss/engineering-note-4 | 13,191 | 추출/문제 해결형 | case_0487 | 0/8 | 인자가 많은 메서드는 왜 나쁠까? |
| toss/reactor-netty-memory-leak | 5,795 | 추출/문제 해결형 | case_0482, case_0483 | 0/15 | Reactor Netty Memory Leak 이슈 탐방기 |
| toss/engineering-note-5 | 14,437 | 추출/문제 해결형 | case_0475 | 0/10 | 프론트엔드 로깅 신경 안 쓰기 |
| toss/engineering-note-6 | 6,960 | 추출/문제 해결형 | case_0486 | 0/11 | 브라우저용 번들링 플러그인, 직접 만들었어요 |
| toss/restructuring-planning | 7,037 | 추출/문제 해결형 | case_0481 | 0/12 | 달리는 기차의 바퀴 교체하기 1. Planning |
| toss/engineering-note-7 | 11,317 | 추출/문제 해결형 | case_0480 | 0/9 | Spring JDBC 성능 문제, 네트워크 분석으로 파악하기 |
| toss/tech-writer-1 | 3,954 | 제외/회고·문화·행사 | - | 0/0 | 그 많은 개발 문서는 누가 다 만들었을까 (1) 토스페이먼츠 테크니컬 라이터가 하는 일 |
| toss/tech-writer-2 | 3,465 | 추출/실험·활용기 | case_0469, case_0470 | 0/14 | 그 많은 개발 문서는 누가 다 만들었을까 (2) 개발자의 학습을 돕는 모든 것 |
| toss/25431 | 6,583 | 추출/문제 해결형 | case_0474 | 0/12 | GitHub Actions로 개선하는 코드 리뷰 문화 |
| toss/cache-traffic-tip | 3,649 | 제외/문제 해결형 | - | 0/0 | 캐시 문제 해결 가이드 - DB 과부하 방지 실전 팁 |
| toss/engineering-note-8 | 6,776 | 추출/문제 해결형 | case_0466 | 0/10 | OpenZFS로 성능과 비용, 두 마리 토끼 잡기 |
| toss/restructuring | 8,187 | 추출/문제 해결형 | case_0465 | 0/12 | 달리는 기차의 바퀴 교체하기 2. Restructuring |
| toss/engineering-note-9 | 7,076 | 추출/문제 해결형 | case_0464 | 0/12 | 프론트엔드 배포 시스템의 진화 (1) - 결제 SDK에 카나리 배포 적용하기 |
| toss/docs-engineering | 5,875 | 추출/기술 선택·도입형 | case_0467 | 0/9 | 더 자유롭고, 빠르고, 정확하게: 토스페이먼츠 API 문서 엔지니어링 |
| toss/react-native-2024 | 6,295 | 추출/기술 선택·도입형 | case_0471, case_0472, case_0473 | 0/22 | 토스가 꿈꾸는 React Native 기술의 미래 |
| toss/monitoring-traffic | 6,416 | 추출/문제 해결형 | case_0476, case_0477, case_0478, case_0479 | 1/32 | 서버 증설 없이 처리하는 대규모 트래픽 |
| toss/lightning-talks-package-manager | 10,221 | 추출/기술 선택·도입형 | case_0468 | 1/12 | 패키지 매니저의 과거, 토스의 선택, 그리고 미래 |
| toss/27750 | 4,859 | 추출/문제 해결형 | case_0462 | 0/10 | Transpiler, “사용”말고 “활용”하기 |
| toss/27752 | 5,980 | 추출/문제 해결형 | case_0461 | 0/9 | 드래그 앤 드롭은 사실 편한 UX가 아니다? |
| toss/framework-agnostic-library | 7,776 | 제외/개념·튜토리얼 | - | 0/0 | 여러 프레임워크에서 사용할 수 있는 라이브러리 만들기 |
| toss/frontent-package-migration | 5,061 | 추출/문제 해결형 | case_0459, case_0460 | 0/12 | 프로젝트 전체에서 사용되는 패키지, 어떻게 마이그레이션 할까? |
| toss/monorepo-pipeline | 5,897 | 추출/문제 해결형 | case_0456, case_0457, case_0458 | 0/21 | 200여개 서비스 모노레포의 파이프라인 최적화 |
| toss/firesidechat_frontend_1 | 519 | 제외/회고·문화·행사 | - | 0/0 | 토스에서 말하는 “가독성 좋은 코드” 란 무엇일까? \| EP1. 모닥불 |
| toss/secure-efficient-ai | 4,320 | 추출/문제 해결형 | case_0447 | 0/8 | 토스뱅크가 AI로 보안과 효율도 챙기는 방법 |
| toss/ssr-server | 7,737 | 추출/문제 해결형 | case_0463 | 0/12 | SSR 서버 최적화로 비용 아끼기 |
| toss/firesidechat_frontend_2 | 561 | 제외/회고·문화·행사 | - | 0/0 | 함수형 프로그래밍, 프론트엔드 개발에 진짜 도움 될까? \| EP.2 모닥불 |
| toss/toss-people-1 | 4,964 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플 #1: 테크 채용 브랜딩의 새로운 기준 |
| toss/firesidechat_frontend_3 | 547 | 제외/회고·문화·행사 | - | 0/0 | 프론트엔드 개발에서 테스트 자동화, 꼭 해야 할까? \| EP.3 모닥불 |
| toss/overseas-securities-server | 9,690 | 추출/문제 해결형 | case_0448, case_0449, case_0450 | 0/20 | 우리는 어떻게 해외주식 서비스 안정화를 이뤘는가 |
| toss/ksqldb-realtime-data | 9,481 | 추출/실험·활용기 | case_0451, case_0452, case_0453, case_0454, case_0455 | 0/29 | ksqlDB를 활용한 증권사의 실시간 데이터 처리하기 |
| toss/cdc_pipeline | 8,717 | 추출/문제 해결형 | case_0444, case_0445 | 0/16 | 대규모 CDC Pipeline 운영을 위한 Debezium 개선 여정 |
| toss/securities_llm_1 | 6,644 | 추출/기술 선택·도입형 | case_0443 | 0/11 | 고성능 GPU 클러스터 도입기 #1: 요리하라고 해서 왔는데 프라이팬이 없어요 |
| toss/intelligence_banner | 12,688 | 추출/문제 해결형 | case_0446 | 0/10 | 유연하고 확장 가능한 배너 기능 구현하기 |
| toss/tockerthon-1 | 6,511 | 제외/회고·문화·행사 | - | 0/0 | 제 1회 토스 해커톤, 토커톤(Tockerthon) |
| toss/nodejs_pipeline_plugin | 6,024 | 추출/기술 선택·도입형 | case_0442 | 0/9 | Node.js 라이브러리 배포 파이프라인에 플러그인 시스템 도입기 |
| toss/serverdeveloper_housing | 4,455 | 추출/문제 해결형 | case_0441 | 0/10 | 전세대출에서 대외기관 신용정보를 조회하는 방법 |
| toss/severdeveloper_dynamic_scraping | 8,256 | 추출/문제 해결형 | case_0438, case_0439, case_0440 | 0/20 | 다이내믹 스크래핑과 전월세대출 이동제의 실행 |
| toss/firesidechat_frontend_4 | 641 | 제외/회고·문화·행사 | - | 0/0 | 오픈소스에 기여하고 토스에 합격한.ssul \| EP.4 모닥불 |
| toss/ksqldb-realtime-data-2 | 11,129 | 추출/실험·활용기 | case_0433 | 0/11 | ksqlDB 실시간 Join으로 뉴스 추천 만들기 |
| toss/firesidechat_frontend_5 | 545 | 제외/회고·문화·행사 | - | 0/0 | 토스 개발자는 개발만 잘해도 될까 \| EP.5 모닥불 |
| toss/slash24 | 6,960 | 제외/회고·문화·행사 | - | 0/0 | 토스가 직접 소개하는 SLASH24 현장 A to Z |
| toss/securities_llm_2 | 8,090 | 추출/기술 선택·도입형 | case_0435, case_0436, case_0437 | 0/25 | 고성능 GPU 클러스터 도입기 #2: 이주하는 데이터 |
| toss/firesidechat_frontend_6 | 598 | 제외/개념·튜토리얼 | - | 0/0 | 프론트엔드 개발에서 Next.js, 꼭 써야 할까? \| EP.6 모닥불 |
| toss/test-strategy-server | 27,464 | 추출/실험·활용기 | case_0432 | 0/13 | 가치있는 테스트를 위한 전략과 구현 |
| toss/spark-analyzer | 4,005 | 추출/문제 해결형 | case_0434 | 0/10 | Spark Job 성능 모니터링과 최적화를 위한 Spark Analyzer 개발기 |
| toss/datalake-iceberg | 15,060 | 추출/문제 해결형 | case_0428 | 0/11 | 입수는 Datalake로! (feat. Iceberg) |
| toss/ts-pattern-usage | 5,369 | 추출/실험·활용기 | case_0427 | 0/7 | ts-pattern은 더 멋진 if문이 아니다 |
| toss/firesidechat_frontend_7 | 625 | 제외/회고·문화·행사 | - | 0/0 | 개발자 리더로서 성장당한 썰 \| EP.7 모닥불 |
| toss/react-native-without-cocoapods | 9,483 | 추출/실험·활용기 | case_0431 | 0/12 | CocoaPods 없이 React Native 개발하기 |
| toss/toss-frontend-ai-docs | 2,869 | 추출/실험·활용기 | case_0419 | 0/8 | 토스 프론트엔드 개발자들이 더 이상 문서를 찾지 않는 이유 |
| toss/llm-serving | 6,540 | 추출/기술 선택·도입형 | case_0425, case_0426 | 0/15 | LLM 쉽고 빠르게 서빙하기 |
| toss/firesidechat_frontend_8 | 622 | 제외/회고·문화·행사 | - | 0/0 | Next.js 그만 쓰세요! 면접관이 진짜 원하는 것!? \| EP.8 모닥불 |
| toss/use-funnel-1 | 6,806 | 추출/기술 선택·도입형 | case_0424 | 0/12 | @use-funnel 개발기 #1: 왜 기존 라이브러리를 두고 새로 만들었나? |
| toss/use-funnel-2 | 8,135 | 추출/문제 해결형 | case_0421, case_0422, case_0423 | 0/15 | @use-funnel 개발기 #2: 기존 라이브러리를 어떻게 뜯어 고칠 것인가? |
| toss/firesidechat_frontend_9 | 583 | 제외/회고·문화·행사 | - | 0/0 | 프론트엔드 서비스 최적화? 토스에서는 '이렇게' 합니다! \| EP.9 모닥불 |
| toss/kafka-distribution-1 | 6,499 | 추출/기술 선택·도입형 | case_0418 | 0/12 | 토스증권 Apache Kafka 데이터센터 이중화 구성 #1 |
| toss/toss-people-3 | 7,801 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 문과생에서 토스 개발 리더까지 |
| toss/kafka-distribution-2 | 4,882 | 추출/문제 해결형 | case_0429, case_0430 | 0/21 | 토스증권 Apache Kafka 데이터센터 이중화 구성 #2: 데이터 미러링 |
| toss/kafka-distribution-3 | 17,875 | 추출/문제 해결형 | case_0420 | 0/13 | 토스증권 Apache Kafka 데이터센터 이중화 구성 #3: Offset Sync |
| toss/firesidechat_frontend_10 | 786 | 제외/회고·문화·행사 | - | 0/0 | 무엇이든 물어보세요 (feat. 프론트엔드 코드, 디렉토리 관리) \| EP.10 캠프파이어 특집 상편 |
| toss/tosspeople-jimin | 4,881 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 길은 가면 뒤에 있다 |
| toss/firesidechat_frontend_10a | 878 | 제외/회고·문화·행사 | - | 0/0 | 무엇이든 물어보세요 (feat. 테스트 코드, ESLint Rule) \| EP.10 캠프파이어 특집 하편 |
| toss/frontend-esbuild-hmr | 10,415 | 추출/문제 해결형 | case_0417 | 0/9 | ESBuild를 위한 HMR, 직접 만들기 |
| toss/frontend-tree-structure | 7,435 | 추출/문제 해결형 | case_0416 | 0/10 | 자료구조를 활용한 복잡한 프론트엔드 컴포넌트 제작하기 |
| toss/firesidechat_frontend_11 | 808 | 제외/기술 선택·도입형 | - | 0/0 | 토스의 디자인 편집기 ‘데우스’, 이렇게 만들었어요! \| EP.11 |
| toss/rn-toss-bedrock | 10,360 | 추출/기술 선택·도입형 | case_0413 | 0/9 | React Native에서 타입 안전한 파일 기반 라우팅 구현하기 |
| toss/34481 | 8,833 | 추출/문제 해결형 | case_0415 | 0/10 | 캐시를 적용하기 까지의 험난한 길 (TPS 1만 안정적으로 서비스하기) |
| toss/frontend-apply-without-resume | 2,783 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드에 이력서 없이 리포지토리 링크로 지원하세요 (~5/31) |
| toss/toss-shopping-recommendation-system | 3,466 | 제외/개념·튜토리얼 | - | 0/0 | 🛒 토스 쇼핑 추천 시스템: 수백만 사용자와 상품을 잇는 멀티 스테이지 접근법 |
| toss/ads-ml | 3,508 | 제외/개념·튜토리얼 | - | 0/0 | 토스는 어떻게 광고를 보여줄까? 토스애즈 ML 톺아보기 |
| toss/firesidechat_frontend_12 | 713 | 제외/회고·문화·행사 | - | 0/0 | 코드 리뷰할 시간이 어딨어요? 모닥불 \| EP.12 |
| toss/flowise-llm-error-analysis-automation | 14,992 | 추출/실험·활용기 | case_0414 | 0/11 | Flowise와 LLM을 활용한 에러 분석 자동화 |
| toss/simplicity4-frontend-engineering | 2,743 | 추출/실험·활용기 | case_0410, case_0411, case_0412 | 0/18 | 뒤에 개발자 있어요 \| Simplicity 4 제작기 #2 |
| toss/toss-oss-committee | 2,224 | 제외/회고·문화·행사 | - | 0/0 | 토스 프론트엔드 챕터가 오픈소스를 통해 꿈꾸는 미래 |
| toss/credit-loan-partner-mock-server | 10,361 | 추출/문제 해결형 | case_0409 | 0/14 | 신용대출 찾기 서비스 제휴사 mock 서버 개발기 #1 |
| toss/msa-enum | 6,946 | 추출/문제 해결형 | case_0407 | 0/11 | 에러 0%, MSA에서의 Enum 관리 전략 |
| toss/tosspayments-mcp | 16,364 | 추출/문제 해결형 | case_0405 | 0/15 | 토스페이먼츠 결제 시스템 연동을 돕는 MCP 서버 구현기 |
| toss/toss-securities-gpu-mig | 13,794 | 추출/기술 선택·도입형 | case_0406 | 0/15 | GPU를 밀도 있게 쓰는 방법 - 토스증권의 GPU 가상화(MIG) 도입기 |
| toss/toss-bank-interns | 10,440 | 제외/회고·문화·행사 | - | 0/0 | 슬기로운 토스뱅크 개발 인턴 생활 |
| toss/undercover-silo-1 | 1,559 | 제외/회고·문화·행사 | - | 0/0 | ‘러닝 쉐어’의 새로운 실험, 토스가 두뇌 서바이벌을 만든 이유 |
| toss/undercover-silo-2 | 5,209 | 추출/실험·활용기 | case_0408 | 1/14 | “AI가 문제 냈어요?” 출제자 PO가 직접 답해드립니다 \| 언더커버 사일로 비하인드 1화: 인플로우 사일로 |
| toss/undercover-silo-3 | 5,000 | 추출/실험·활용기 | case_0400 | 0/9 | “토스 참 쪼잔하다”는 유저 말에 1억을 태운 이유 \| 언더커버 사일로 비하인드 2화: 만보기 사일로 |
| toss/toss-securities-visualize-lineage | 7,168 | 추출/문제 해결형 | case_0404 | 0/10 | 토스증권의 수천 개 실시간 데이터 파이프라인 운영방법 #1: Visualize Lineage |
| toss/38743 | 3,326 | 추출/문제 해결형 | case_0390 | 0/9 | 귀로 듣는 챗봇의 탄생 \| 접근성 업무일지 #3 |
| toss/A11y_Fundamentals | 4,241 | 제외/개념·튜토리얼 | - | 0/0 | 토스의 접근성 문서 A11y Fundamentals 을 소개합니다 (오픈 기념 이벤트 ~9/10) |
| toss/feature-store-trainkit | 11,900 | 추출/문제 해결형 | case_0401, case_0402, case_0403 | 0/27 | 토스가 다양한 ML 모델을 만드는 법: Feature Store & Trainkit |
| toss/undercover-silo-4 | 3,499 | 추출/문제 해결형 | case_0398, case_0399 | 0/11 | “왜 아무도 에러 메시지를 읽지 않을까?” \| 언더커버 사일로 비하인드 3화: 페이스페이 사일로 |
| toss/undercover-silo-5 | 3,611 | 추출/실험·활용기 | case_0389 | 0/10 | 성공이 가장 큰 위기일 때, 문제 없는 서비스 성장시키기 \| 언더커버 사일로 비하인드 4화: 고양이 사일로 |
| toss/credit-loan-partner-mock-server-2 | 11,389 | 추출/문제 해결형 | case_0395, case_0396 | 0/20 | 신용대출 찾기 서비스 제휴사 Mock 서버 개발기 #2 |
| toss/tosspeople-diko | 3,927 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플: 50살, 엔지니어로 살아남는 법 |
| toss/undercover-silo-6 | 4,919 | 추출/문제 해결형 | case_0387 | 0/8 | 1,000만 명이 들어와도 999만 명이 나가는 문제, 어떻게 해결했을까 \| 언더커버 사일로 비하인드 5화: 계좌 사일로 |
| toss/iceberg-cdc-1 | 14,846 | 추출/문제 해결형 | case_0385 | 0/10 | 토스증권 Iceberg 적용기 #1: CDC 환경은 왜 제대로 동작하지 않을까? |
| toss/MSA-observability | 14,209 | 추출/문제 해결형 | case_0397 | 0/16 | 토스증권의 수 천개 실시간 데이터 파이프라인 운영방법 #2: MSA 환경 Observability 높이기 |
| toss/payments-legacy-intro | 1,273 | 제외/회고·문화·행사 | - | 0/0 | 멈춰있던 PG의 시간, 토스페이먼츠가 다시 흐르게 합니다 |
| toss/data-analyst-ab-test | 3,229 | 추출/문제 해결형 | case_0388 | 0/9 | 진짜 A/B 테스트: 토스의 푸시 생태계를 데이터로 재설계한 방법 |
| toss/payments-legacy-1 | 11,274 | 추출/문제 해결형 | case_0391, case_0392, case_0393, case_0394 | 0/32 | 20년 레거시를 넘어 미래를 준비하는 시스템 만들기 |
| toss/payments-legacy-2 | 11,307 | 추출/문제 해결형 | case_0381, case_0382, case_0383, case_0384 | 0/25 | 가맹점은 변함없이, 결제창 시스템 전면 재작성하기 |
| toss/internal-mcp-server | 10,824 | 추출/문제 해결형 | case_0386 | 0/13 | API 연동 자동화를 위한 여정: 토스는 왜 사내 MCP 서버를 개발하였는가? with Spring-AI |
| toss/toss-pos-plugin | 6,456 | 추출/기술 선택·도입형 | case_0380 | 0/10 | 포스를 확장하는 가장 빠른 방법, 포스 플러그인 |
| toss/tosspeople-jhko | 5,162 | 제외/회고·문화·행사 | - | 0/0 | 토스 피플 : 데이터를 ‘이해하는’ 구조를 설계합니다 |
| toss/tossplace-qa-manager | 5,761 | 추출/실험·활용기 | case_0379 | 0/11 | 토스플레이스 사일로 QA로 일한다는 것 |
| toss/payments-legacy-3 | 19,675 | 추출/기술 선택·도입형 | case_0375 | 0/12 | 100년 가는 프론트엔드 코드, SDK |
| toss/toss-da-mtvi | 4,593 | 추출/기술 선택·도입형 | case_0370 | 0/9 | LTV를 넘어 서비스의 가치를 측정하는 새로운 지표, MTVi |
| toss/payments-legacy-4 | 20,582 | 추출/기술 선택·도입형 | case_0371 | 0/11 | 토스페이먼츠의 Open API 생태계 |
| toss/payments-legacy-5 | 6,669 | 추출/문제 해결형 | case_0372, case_0373, case_0374 | 0/31 | 레거시 결제 원장을 확장 가능한 시스템으로 |
| toss/income-qa-e2e-automation | 10,553 | 추출/문제 해결형 | case_0365 | 0/14 | 토스인컴 세금 환급 서비스 : 빠른 속도에서 품질을 지키기 위한 E2E 자동화 여정 |
| toss/toss-next-ml-challenge | 5,121 | 제외/회고·문화·행사 | - | 0/0 | 토스 Next ML Challenge - 광고 클릭 예측(PCTR) ML 경진대회 출제 후기 |
| toss/business-customer-data | 4,563 | 추출/실험·활용기 | case_0360 | 0/10 | 사업자 데이터 리터러시 높이기: BC Monthly Report 발행기 |
| toss/payments-legacy-6 | 17,635 | 추출/문제 해결형 | case_0366, case_0367, case_0368, case_0369 | 0/35 | 레거시 정산 개편기: 신규 시스템 투입 여정부터 대규모 배치 운영 노하우까지 |
| toss/tds-color-system-update | 13,423 | 추출/문제 해결형 | case_0361, case_0362, case_0363, case_0364 | 0/30 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| toss/payments-legacy-7 | 12,104 | 추출/기술 선택·도입형 | case_0376, case_0377, case_0378 | 0/27 | 고객은 절대 기다려주지 않는다: 빠른 데이터 서빙으로 고객 만족도를 수직 상승 시키는 법 |
| toss/neurIPS-FedLPA | 6,355 | 추출/문제 해결형 | case_0351 | 0/9 | 토스의 AI 기술력, 세계 최고 권위 NeurIPS 2025에서 인정받다: FedLPA 연구 |
| toss/ai-driven-ui-test-automation | 9,047 | 추출/실험·활용기 | case_0344, case_0345, case_0346 | 0/23 | 세금 환급 자동화 : AI-driven UI 테스트 자동화 일지 |
| toss/ast-funnel-visualization | 10,557 | 추출/문제 해결형 | case_0337 | 0/11 | AST로 Outdated 없는 퍼널 문서 만들기 |
| toss/vulnerability-analysis-automation-1 | 5,660 | 추출/문제 해결형 | case_0352, case_0353, case_0354 | 0/23 | LLM을 이용한 서비스 취약점 분석 자동화 #1 |
| toss/rethinking-design-system | 7,254 | 추출/기술 선택·도입형 | case_0338 | 0/11 | 디자인 시스템 다시 생각해보기 |
| toss/payments-legacy-8 | 12,961 | 추출/기술 선택·도입형 | case_0342, case_0343 | 0/17 | 수천 개의 API/BATCH 서버를 하나의 설정 체계로 관리하기 |
| toss/income-qa-platform | 4,970 | 추출/실험·활용기 | case_0333 | 0/7 | 토스인컴 QA Platform:  ‘누구나 테스트할 수 있는’ 도구의 시작 |
| toss/payments-legacy-9 | 12,900 | 추출/기술 선택·도입형 | case_0339, case_0340, case_0341 | 0/27 | 레거시 인프라 작살내고 하이브리드 클라우드 만든 썰 |
| toss/will-ai-replace-developers | 11,388 | 제외/실험·활용기 | - | 0/0 | 개발자는 AI에게 대체될 것인가 |
| toss/software-3-0-era | 9,814 | 제외/개념·튜토리얼 | - | 0/0 | 소프트웨어 3.0 시대를 맞이하며 |
| toss/payments-legacy-10 | 10,691 | 추출/문제 해결형 | case_0347, case_0348, case_0349, case_0350 | 0/35 | 경계 보안부터 제로트러스트 보안까지, 고도화 여정 |
| toss/harness-for-team-productivity | 7,018 | 제외/기술 선택·도입형 | - | 0/0 | Software 3.0 시대, Harness를 통한 조직 생산성 저점 높이기 |
| toss/toss-front-sdk | 7,804 | 추출/기술 선택·도입형 | case_0332 | 0/8 | 쓰기 쉬운 Toss Front SDK |
| toss/harness-for-team-productivity-eng | 15,730 | 제외/개념·튜토리얼 | - | 0/0 | Stepping into the Software 3.0 Era |
| toss/vulnerability-analysis-automation-2 | 16,963 | 추출/실험·활용기 | case_0355, case_0356, case_0357, case_0358, case_0359 | 0/29 | LLM을 이용한 서비스 취약점 분석 자동화 #2 |
| toss/place-metric-review | 4,542 | 제외/회고·문화·행사 | - | 0/0 | Metric Review, 실행을 이끌다 |
| toss/es-toolkit | 8,995 | 추출/실험·활용기 | case_0331 | 0/13 | 97% Smaller, 2x Faster: How es-toolkit Reached 10 Million Weekly Downloads |
| toss/flink-realtime-frequency-capping | 22,195 | 추출/문제 해결형 | case_0334, case_0335, case_0336 | 0/32 | Apache Flink + RocksDB 튜닝으로 광고 Frequency Capping 실시간 집계를 일주일까지 확장하기 |
| toss/da-assistant-panda | 5,697 | 추출/실험·활용기 | case_0327 | 0/11 | 토스플레이스 데이터봇 ‘판다(PANDA)’를 소개합니다 : 모든 팀원이 데이터 전문가처럼 일하는 방법 |
| toss/operating-starrocks-1 | 16,301 | 추출/문제 해결형 | case_0329 | 0/12 | StarRocks 운영기: Resource Group으로 멀티테넌트 워크로드 격리하기 |
| toss/post-quantum-cryptography | 9,122 | 추출/기술 선택·도입형 | case_0330 | 0/13 | 양자컴퓨터 시대에 대비한 양자내성암호 적용, 왜 10년 먼저 서비스에 적용했을까? |
| toss/post-quantum-cryptography-eng | 18,037 | 추출/기술 선택·도입형 | case_0328 | 0/13 | Why We Adopted Post-Quantum Cryptography a Decade Before Quantum Computers Arrive |
| toss/toss-tpm | 7,144 | 제외/회고·문화·행사 | - | 0/0 | AI 시대, 성과 내는 조직일수록 토스식 TPM이 필요한 이유 |
| toss/cross-functional-tpm-tip | 5,612 | 제외/회고·문화·행사 | - | 0/0 | Cross Functional 기술 문제 풀기 위한 역량 성장 Tip |
| toss/ai-surf-day | 8,043 | 제외/회고·문화·행사 | - | 0/0 | 토스팀이 AI 파도를 마주하는 방법: AI Surf Day |
| toss/skill-quality-rubric | 14,349 | 추출/문제 해결형 | case_0325 | 0/12 | Skill 품질 관리를 위한 Rubric 설계와 시스템 구현 |
| toss/history-of-face-recognition-facepay | 14,836 | 추출/기술 선택·도입형 | case_0326 | 0/10 | 얼굴 인식의 역사와 페이스페이의 미래 |
| toss/tam-connect-2025 | 4,446 | 제외/회고·문화·행사 | - | 0/0 | 빠르게 움직이는 조직에서, TAM은 어떻게 문제를 해결할까? |
| toss/tues | 5,460 | 추출/기술 선택·도입형 | case_0320 | 0/10 | 2,800만 MAU를 이해하는 유저 Segmentation, TUES |
| toss/spark-connect-on-kubernetes-1 | 14,096 | 추출/문제 해결형 | case_0322, case_0323 | 0/21 | Spark Connect on Kubernetes #1: 견고한 Spark Connect 만들기 |
| toss/technical-writing-1 | 3,872 | 제외/회고·문화·행사 | - | 0/0 | 1. 세상에 없던 직무를 만들어가기 |
| toss/technical-writing-2 | 4,271 | 추출/기술 선택·도입형 | case_0324 | 0/10 | 2. 전문성 밖으로 나아가기 |
| toss/50761 | 5,745 | 추출/기술 선택·도입형 | case_0318, case_0319 | 0/18 | es-toolkit, 사내 작은 라이브러리가 전세계적인 라이브러리가 되기까지 |
| toss/technical-writing-3 | 5,410 | 추출/문제 해결형 | case_0314 | 0/8 | 3. 우리 팀의 문서화는 왜 실패할까? (1) |
| toss/technical-writing-4 | 5,813 | 제외/회고·문화·행사 | - | 0/0 | 4. 우리 팀의 문서화는 왜 실패할까? (2) |
| toss/technical-writing-5 | 7,608 | 추출/실험·활용기 | case_0312 | 0/12 | 5. Technical Writer, 사라질 결심 |
| toss/technical-writing-6 | 6,454 | 추출/기술 선택·도입형 | case_0321 | 0/13 | 6. 도구를 넘어, 기준과 책임으로 |
| toss/50693 | 10,796 | 추출/기술 선택·도입형 | case_0308 | 0/11 | es-toolkit: How a Small Internal Library Became a Global Project |
| toss/50893 | 5,530 | 추출/기술 선택·도입형 | case_0313 | 0/13 | 누군가는 토스를 테스트하는 동안, 우리는 테스트하는 법을 만듭니다. |
| toss/device-farm-nebula | 10,253 | 추출/기술 선택·도입형 | case_0309, case_0310, case_0311 | 0/27 | 토스의 디바이스 팜 만들기 |
| toss/llm_context_topic | 10,699 | 추출/문제 해결형 | case_0307 | 0/13 | LLM은 똑똑한데, 왜 우리 회사 일은 모를까 |
| toss/ds-mle-cowork | 6,372 | 추출/기술 선택·도입형 | case_0306 | 0/13 | DS와 MLE가 함께 일하는 법 |
| toss/52209 | 11,506 | 추출/기술 선택·도입형 | case_0302 | 0/12 | 모노리포 희망편, 절망의 리포가 희망의 리포로 부활하기까지 걸린 1년 |
| toss/tossion | 9,712 | 추출/기술 선택·도입형 | case_0315, case_0316, case_0317 | 0/30 | 토스의 속도와 품질, 상용 도구로 충분한가 — 토션(Tossion) |
| toss/tech_talk_talk_1 | 8,621 | 추출/기술 선택·도입형 | case_0298 | 0/14 | AI에게 투자정보를 말하게 하기까지 |
| toss/games-in-ads | 12,980 | 추출/기술 선택·도입형 | case_0303, case_0304, case_0305 | 0/32 | 토스는 어떻게 광고 속에 게임을 넣었을까 |
| toss/ads_dashboard_fe | 12,467 | 추출/기술 선택·도입형 | case_0297 | 0/14 | 전체 데이터를 브라우저에 두는 광고 대시보드 만들기 |
| toss/tech_talk_talk_2 | 4,920 | 추출/문제 해결형 | case_0289 | 0/11 | LLM 서빙, 띄우는 것과 잘 띄우는 것 사이 |
| toss/tech_talk_talk_3 | 8,973 | 추출/실험·활용기 | case_0299, case_0300, case_0301 | 0/26 | 토스증권 추천과 검색은 어떻게 진화하고 있을까? |
| toss/qa_hotfix | 6,406 | 추출/문제 해결형 | case_0291, case_0292, case_0293 | 0/27 | 1%가 겪은 버그 고쳐야할까요? |
| toss/52885 | 11,738 | 추출/실험·활용기 | case_0285 | 0/12 | AI가 만든 코드가 어드민이 되기까지 |
| toss/technical-writing-1-eng | 8,266 | 제외/회고·문화·행사 | - | 0/0 | 1. Creating a Role That Didn’t Exist Before |
| toss/technical-writing-2-eng | 9,846 | 추출/기술 선택·도입형 | case_0283 | 0/11 | 2. Beyond Our Expertise |
| toss/toss-frontend-ai-docs-eng | 5,770 | 추출/실험·활용기 | case_0284 | 0/8 | How Documents Find Developers at Toss |
| toss/52631 | 12,679 | 추출/문제 해결형 | case_0287 | 0/14 | AI가 팀 규칙을 지키도록 하는 방법 |
| toss/52999 | 6,391 | 추출/기술 선택·도입형 | case_0288 | 0/13 | App Router의 장점은 우리에게도 장점일까요? |
| toss/gpu-native-cluster | 16,620 | 추출/문제 해결형 | case_0294, case_0295, case_0296 | 0/25 | 토스증권이 GPU-aware를 넘어 GPU-native 클러스터를 구축한 방법 |
| toss/toss-benchmark | 11,020 | 추출/기술 선택·도입형 | case_0290 | 0/12 | 리더보드 1등 LLM, 토스에서도 1등일까? - Toss Benchmark 구축기 |
| toss/toss-doctor | 5,029 | 추출/문제 해결형 | case_0286 | 0/10 | 쉼 없이 도는 테스트, 사람이 어디까지 돌봐야 할까요? - 토스닥터(Toss Doctor) |
| woowahan/13569 | 9,459 | 추출/문제 해결형 | case_0690 | 0/10 | 누구나 할 수 있는 10배 더 빠른 배치 만들기 |
| woowahan/13726 | 12,404 | 제외/회고·문화·행사 | - | 0/0 | 실험 0건인 조직에서, 가장 실험을 활발하게 하는 조직 되기 (B마트의 실험문화 빌드업 과정) |
| woowahan/13604 | 22,269 | 제외/회고·문화·행사 | - | 0/0 | 우아한테크코스 5기 크루들의 서비스 출시! |
| woowahan/13929 | 6,609 | 제외/회고·문화·행사 | - | 0/0 | 밤샘의 추억, 생성 AI 해커톤 “우아톤 2023” |
| woowahan/13429 | 25,477 | 추출/문제 해결형 | case_0691 | 0/13 | 로그 및 SQL 진입점 정보 추가 여정 |
| woowahan/12947 | 12,972 | 제외/회고·문화·행사 | - | 0/0 | [모여서 각자 글쓰기] 온라인 출판기념회 |
| woowahan/13977 | 4,180 | 제외/회고·문화·행사 | - | 0/0 | PM스터디 그것이 알고싶다. 오늘의 PM, 내일의 서비스 |
| woowahan/11392 | 13,954 | 추출/기술 선택·도입형 | case_0689 | 0/11 | Spring Boot에서 S3에 파일을 업로드하는 세 가지 방법 |
| woowahan/14224 | 85 | 제외/회고·문화·행사 | - | 0/0 | [모집 마감] 우아한스터디 2023 겨울시즌 |
| woowahan/14072 | 3,994 | 제외/회고·문화·행사 | - | 0/0 | [모집] 우아한테크코스 2024 신입생을 모집합니다 |
| woowahan/14107 | 6,612 | 추출/실험·활용기 | case_0685, case_0686, case_0687 | 0/21 | 레퍼런스 없이 000 만들기, 아이디어는 어디에서 왔을까? |
| woowahan/14301 | 6,451 | 추출/문제 해결형 | case_0692 | 0/11 | 굴러가는 자동차에 안전하게 타이어 교체하기(w. CMS 기능 개발) |
| woowahan/14513 | 1,326 | 제외/회고·문화·행사 | - | 0/0 | [다시 보기] 10월 우아한테크세미나: 글 쓰는 우아한 개발자 |
| woowahan/14484 | 5,518 | 추출/문제 해결형 | case_0684 | 0/9 | “일단 백로그에 넣어두고 여유 있을 때 보는 걸로 할까요?” : 백로그를 백로그로 두지 않는 법 |
| woowahan/14644 | 13 | 제외/회고·문화·행사 | - | 0/0 | 우아한테크콘퍼런스, WOOWACON 2023에 지금 등록하세요! |
| woowahan/13539 | 10,695 | 추출/문제 해결형 | case_0683 | 0/10 | 스토리지 최적의 스펙 관리 시스템 만들기 |
| woowahan/14671 | 6,108 | 제외/회고·문화·행사 | - | 0/0 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/14505 | 4,607 | 추출/기술 선택·도입형 | case_0688 | 0/9 | 따끈따끈한 전사 로그 시스템 전환기: ELK Stack에서 Loki로 전환한 이유 |
| woowahan/14550 | 9,875 | 추출/실험·활용기 | case_0671 | 0/10 | 너 혹시 T(Tester)야? : 테스트 효율을 높이는 Charles 툴 활용기 |
| woowahan/14874 | 33,747 | 추출/문제 해결형 | case_0679 | 0/14 | 서버사이드 테스트 파랑새를 찾아서 |
| woowahan/14969 | 8,519 | 제외/회고·문화·행사 | - | 0/0 | 우아한테크캠프 6기 교육생들의 최종 회고 |
| woowahan/15268 | 6,159 | 추출/실험·활용기 | case_0680, case_0681, case_0682 | 0/19 | 배민앱에서 대용량특가를 만나기까지 |
| woowahan/15084 | 28,934 | 추출/기술 선택·도입형 | case_0675, case_0676, case_0677, case_0678 | 0/32 | 웹프론트개발팀에서 배민 커머스 어드민을 개발하는 방법 |
| woowahan/15398 | 10,772 | 추출/실험·활용기 | case_0672 | 0/13 | Java의 미래, Virtual Thread |
| woowahan/15488 | 1,176 | 제외/회고·문화·행사 | - | 0/0 | [다시 보기] 12월 우아한테크세미나: WOOWACON 2023 리캡 |
| woowahan/15236 | 5,127 | 추출/문제 해결형 | case_0669, case_0670 | 0/16 | 결제는 계속된다: 결제 담당자가 장애에 대응하는 방법 |
| woowahan/15469 | 12,975 | 추출/문제 해결형 | case_0674 | 1/14 | [트러블슈팅기] CSR에서 동적 OG 메타태그 적용하기 |
| woowahan/15572 | 10,317 | 추출/기술 선택·도입형 | case_0673 | 0/14 | 표준 개발 환경 개선 되돌아보기 |
| woowahan/15541 | 6,445 | 제외/개념·튜토리얼 | - | 0/0 | 웹 접근성 준수를 통한 모두에게 배달되는 일상의 행복 |
| woowahan/15694 | 9,225 | 추출/실험·활용기 | case_0668 | 0/10 | 개발자 의식의 흐름대로 적용해보는 서킷브레이커 |
| woowahan/15764 | 9,265 | 추출/문제 해결형 | case_0667 | 0/12 | 고르곤졸라는 되지만 고르곤 졸라는 안 돼! 배달의민족에서 금칙어를 관리하는 방법 |
| woowahan/14041 | 11,074 | 추출/기술 선택·도입형 | case_0658 | 0/13 | 배달의민족 광고데이터 이관기 |
| woowahan/15983 | 1,159 | 제외/회고·문화·행사 | - | 0/0 | [다시 보기] 2월 우아한테크세미나: 글로벌 개발자로 성장하는 소프트웨어 실무 영어 |
| woowahan/15895 | 5,690 | 추출/문제 해결형 | case_0657 | 0/12 | 가입은 쉽게, 로그인은 실패 없이! 휴대폰번호로 계속하기 |
| woowahan/16158 | 4,814 | 추출/실험·활용기 | case_0656 | 0/9 | 사이드 프로젝트는 사이드가 아니다 |
| woowahan/16547 | 10,454 | 추출/실험·활용기 | case_0662, case_0663, case_0664 | 0/20 | 프론트엔드 개발자들의 즐거운 상상 🎈 – 쓰면글림체 사이드 프로젝트 이야기 |
| woowahan/15883 | 7,303 | 추출/문제 해결형 | case_0665 | 0/11 | 갤럭시 S24가 찾아준 배민커넥트 Android 성능 이슈 해결기(feat. React Native) |
| woowahan/16044 | 15,388 | 추출/실험·활용기 | case_0666 | 0/10 | 셸 스크립트를 몰라도 자동화는 하고 싶어, ChatGPT를 활용한 git flow 관리 스크립트 자동화 진행기 |
| woowahan/16021 | 15,532 | 추출/실험·활용기 | case_0659, case_0660, case_0661 | 0/23 | 셀프서비스, 챗봇에게 물어보세요 |
| woowahan/16979 | 2,550 | 제외/회고·문화·행사 | - | 0/0 | [모집 마감] 2024 우아한테크캠프 7기 |
| woowahan/16877 | 5,300 | 추출/실험·활용기 | case_0654 | 0/10 | 리뷰를 재료로 GPT가 뚝딱뚝딱 만들어낸 메뉴추천, 메뉴뚝딱AI |
| woowahan/16917 | 2,000 | 제외/회고·문화·행사 | - | 0/0 | 우아한형제들 PM들은 어떤 책을 읽을까? |
| woowahan/17081 | 8,547 | 추출/문제 해결형 | case_0653 | 0/12 | 우아한형제들 디자인 시스템에 시각적 회귀 테스트 적용하기 |
| woowahan/17163 | 1,110 | 제외/회고·문화·행사 | - | 0/0 | [다시 보기] 4월 우아한테크세미나: Java의 미래, Virtual Thread |
| woowahan/15903 | 25,916 | 추출/기술 선택·도입형 | case_0655 | 0/11 | 우리 팀을 위한 ESLint, Prettier 공유 컨피그 만들어보기 |
| woowahan/17221 | 16,046 | 추출/문제 해결형 | case_0652 | 0/9 | JPA에서 아이디를 자동증가 값으로 사용 시 하이버네이트의 @NaturalId 사용해 보기 |
| woowahan/17241 | 3,682 | 추출/실험·활용기 | case_0648 | 0/10 | 배민선물하기 AI 메시지 제작기: 생성 AI가 센스 있는 선물 메시지를 대신 쓰기까지 |
| woowahan/15660 | 5,639 | 제외/회고·문화·행사 | - | 0/0 | 우아한스터디 2023 여름시즌 후기: 쏙쏙 들어오는 함수형 코딩 |
| woowahan/17328 | 85 | 제외/회고·문화·행사 | - | 0/0 | [모집 마감] 우아한스터디 2024 여름시즌 |
| woowahan/16910 | 6,459 | 추출/실험·활용기 | case_0645 | 0/10 | 웹 애플리케이션 페이지를 패키지로 개발해 본 경험 |
| woowahan/17404 | 18,068 | 제외/개념·튜토리얼 | - | 0/0 | 코드와 함께 살펴보는 프론트엔드 단위 테스트 – Part 1. 이론 편 |
| woowahan/17466 | 6,056 | 추출/문제 해결형 | case_0647 | 0/9 | 운송 관리 시스템(TMS)의 탄생부터 현장에서 사용하기까지 |
| woowahan/17713 | 1,163 | 제외/회고·문화·행사 | - | 0/0 | [다시 보기] 6월 우아한테크세미나 : 글로벌 개발자로 성장하는 법 |
| woowahan/17416 | 9,133 | 추출/문제 해결형 | case_0643 | 0/11 | WMS 재고 이관을 위한 분산 락 사용기 |
| woowahan/17721 | 18,768 | 추출/실험·활용기 | case_0644 | 0/10 | 코드와 함께 살펴보는 프론트엔드 단위 테스트 – Part 2. 실전 편 |
| woowahan/17386 | 11,245 | 추출/실험·활용기 | case_0649, case_0650, case_0651 | 0/21 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/17710 | 13,491 | 추출/문제 해결형 | case_0642 | 0/10 | Vite로 구버전 브라우저 지원하기 |
| woowahan/17765 | 5,925 | 추출/문제 해결형 | case_0640, case_0641 | 0/15 | 마케팅 타깃팅 툴 BUDS 제작기, 탄생부터 수출 역군이 되기까지 |
| woowahan/17674 | 14,556 | 추출/실험·활용기 | case_0639 | 0/11 | 야, 너도 WireMock으로 테스트할 수 있어 |
| woowahan/17980 | 3,713 | 추출/기술 선택·도입형 | case_0634 | 0/9 | 맞춤형 콘텐츠, 배민은 사장님께 어떻게 제공할까? :  배민외식업광장 세그먼트 적용기 |
| woowahan/17911 | 4,799 | 추출/문제 해결형 | case_0646 | 0/14 | B마트 주문 유실을 없애보자: 네트워크 편 |
| woowahan/17383 | 9,739 | 추출/기술 선택·도입형 | case_0635 | 0/12 | 실시간 반응형 추천 개발 일지 1부: 프로젝트 소개 |
| woowahan/18254 | 3,733 | 추출/문제 해결형 | case_0630 | 0/10 | 실시간 배달 상황이 궁금해! 배달 인프라 레벨 구축 경험담 |
| woowahan/18144 | 10,861 | 추출/실험·활용기 | case_0631, case_0632 | 0/20 | AI 데이터 분석가 ‘물어보새’ 등장 – 1부. RAG와 Text-To-SQL 활용 |
| woowahan/17647 | 13,702 | 추출/기술 선택·도입형 | case_0636, case_0637 | 0/19 | 로봇을 위한 MLOps #1: Edge device와 K3s, Airflow |
| woowahan/17827 | 21,259 | 추출/실험·활용기 | case_0638 | 0/12 | 로봇을 위한 MLOps #2: 엣지 파이프라인의 구성 |
| woowahan/18632 | 15,299 | 추출/기술 선택·도입형 | case_0633 | 0/16 | Polars로 데이터 처리를 더 빠르고 가볍게 with 실무 적용기 |
| woowahan/18719 | 7,518 | 추출/문제 해결형 | case_0627 | 0/10 | B마트 테마관 개선기 : 오픈이 끝? No. 함께하는 동료들과 프로덕트 꾸준히 발전시키기 |
| woowahan/18486 | 26,966 | 추출/문제 해결형 | case_0626 | 0/13 | Elasticsearch 병렬 테스트를 향한 여정 |
| woowahan/18362 | 13,597 | 추출/실험·활용기 | case_0628 | 0/13 | AI 데이터 분석가 ‘물어보새’ 등장 – 2부. Data Discovery |
| woowahan/18980 | 17,117 | 추출/실험·활용기 | case_0629 | 0/10 | 로봇 ML 모델의 경량화 1부: 훈련 후 양자화 |
| woowahan/19317 | 1,157 | 제외/회고·문화·행사 | - | 0/0 | [다시 보기] 8월 우아한테크세미나: 생성AI로 똑똑하게 일하는 법 |
| woowahan/19370 | 12,513 | 추출/문제 해결형 | case_0623, case_0624, case_0625 | 0/29 | 우아한테크캠프 7기: 데모데이 1위 팀의 로그 매니저 프로젝트를 소개합니다! |
| woowahan/19415 | 13,095 | 추출/문제 해결형 | case_0621, case_0622 | 0/20 | 승인 프로세스 뒤에 숨겨진 일꾼들: 사장님 입점요청 승인툴 고도화 프로젝트 경험담 |
| woowahan/19470 | 600 | 제외/회고·문화·행사 | - | 0/0 | [신청 마감] WOOWACON 2024에 지금 등록하세요! |
| woowahan/19491 | 32,356 | 추출/기술 선택·도입형 | case_0615 | 0/14 | Spring Statemachine 도입기 |
| woowahan/19509 | 18,629 | 추출/실험·활용기 | case_0610 | 0/10 | 프론트엔드 통합 테스트로 더 안전한 웹 서비스 개발하기 |
| woowahan/19575 | 5,513 | 제외/회고·문화·행사 | - | 0/0 | 만드는 사람이 수고로우면 쓰는 사람이 편하다: 사용자경험관리TF 활동 이야기 |
| woowahan/19548 | 9,183 | 추출/문제 해결형 | case_0611, case_0612, case_0613, case_0614 | 0/26 | 제목은 안정적인 AI 서빙 시스템으로 하겠습니다. 근데 이제 자동화를 곁들인… |
| woowahan/19915 | 15,653 | 추출/기술 선택·도입형 | case_0609 | 0/12 | 생성형 AI 서비스: 게이트웨이로 쉽게 시작하기 |
| woowahan/20029 | 9,998 | 추출/문제 해결형 | case_0605 | 0/10 | ‘대략’이 아닌 ‘정확한’ 데이터로!:  생산성 측정 지표 개발기 |
| woowahan/19685 | 4,785 | 추출/문제 해결형 | case_0604 | 0/10 | 최적화된 인스턴스 추천을 위한 Rightsizing Recommendations 시스템 개발 여정 |
| woowahan/20078 | 20,224 | 추출/실험·활용기 | case_0606, case_0607, case_0608 | 0/21 | How Our Team Uses Kafka |
| woowahan/20154 | 9,210 | 추출/실험·활용기 | case_0602 | 0/12 | API 모킹으로 테스트를 더 편리하게, Mock Service GUI 소개 |
| woowahan/20142 | 1,542 | 추출/실험·활용기 | case_0600 | 0/5 | 우아콘 웹사이트에 사용된 폰트는 무엇일까? |
| woowahan/20228 | 4,780 | 추출/문제 해결형 | case_0599 | 0/10 | 왜 이미지만 700MB를 다운로드하는 거죠?: 배민우리동네 콘텐츠 피드 이미지 최적화 사례 |
| woowahan/20161 | 17,199 | 추출/문제 해결형 | case_0616, case_0617, case_0618, case_0619, case_0620 | 1/34 | 검색 성능 개선을 위한 Elasticsearch 인덱스 구조와 쿼리 최적화 |
| woowahan/20430 | 4,671 | 제외/회고·문화·행사 | - | 0/0 | WOOWACON 2024, 배달 기술의 모든 것을 담다 |
| woowahan/20386 | 5,426 | 추출/실험·활용기 | case_0594 | 0/13 | 이 과제의 성과는 뭔가요? 지표 중심 커뮤니케이션이 불러온 변화 |
| woowahan/20702 | 1,298 | 제외/회고·문화·행사 | - | 0/0 | [다시 보기] 12월 우아한테크세미나: 올해의 기술 콘퍼런스, 핵심만 골라봤습니다 – LLM 편 |
| woowahan/20627 | 12,670 | 추출/문제 해결형 | case_0603 | 1/13 | PM, 디자이너, 개발자가 함께한 배달의민족 입점 과정 개선기 |
| woowahan/20371 | 15,445 | 추출/문제 해결형 | case_0601 | 1/12 | postgres_fdw로 마이그레이션 생산성 높이기 |
| woowahan/20789 | 333 | 제외/회고·문화·행사 | - | 0/0 | WOOWACON 2024 발표 영상, 지금 바로 만나 보세요! |
| woowahan/20841 | 4,942 | 제외/회고·문화·행사 | - | 0/0 | 우아한히트텍: 직군을 넘어, 개발자를 하나로 잇다 |
| woowahan/20408 | 6,759 | 추출/문제 해결형 | case_0590 | 0/12 | 프롬프트 엔지니어링으로 메뉴 이미지 품질 검수하기: GPT 기반 업무 자동화 |
| woowahan/20938 | 19,661 | 추출/실험·활용기 | case_0595, case_0596, case_0597 | 0/30 | 2024 선물카드 제목 짓기 대회가 탄생하기까지: 운영, PM, 개발 이야기 |
| woowahan/20763 | 8,615 | 추출/기술 선택·도입형 | case_0591, case_0592 | 0/27 | 이젠 보내줄 때가 되었다. 대규모 트래픽의 C++ 시스템 Java로 전환하기 |
| woowahan/20156 | 19,966 | 추출/문제 해결형 | case_0598 | 1/14 | 카프카 컨슈머에 동적 쓰로틀링 적용하기 |
| woowahan/21027 | 25,102 | 추출/기술 선택·도입형 | case_0593 | 1/14 | 실시간 반응형 추천 개발 일지 2부: 벡터 검색, 그리고 숨겨진 요구사항과 기술 도입 의사 결정을 다루는 방법 |
| woowahan/21115 | 8,560 | 추출/실험·활용기 | case_0586 | 0/10 | 프로덕트 전략, 어떻게 시작해야 할까? |
| woowahan/21176 | 13,706 | 추출/실험·활용기 | case_0584 | 0/12 | 로봇 ML 모델의 경량화 2부: 양자화 인식 훈련 |
| woowahan/21240 | 11,396 | 추출/실험·활용기 | case_0580 | 0/10 | 코파일럿 “열일”하게 만드는 방법 |
| woowahan/21324 | 3,763 | 추출/문제 해결형 | case_0579 | 0/10 | RADIUS 인증 실패 분석 및 해결 사례 |
| woowahan/21353 | 6,940 | 추출/기술 선택·도입형 | case_0576, case_0577, case_0578 | 0/18 | 데이터카탈로그 PM이 ‘데이터 디스커버리’라는 가치를 풀어내는 방법 |
| woowahan/21434 | 6,896 | 추출/기술 선택·도입형 | case_0581, case_0582, case_0583 | 0/18 | 데이터카탈로그에서 DataHub를 이용하는 방법 |
| woowahan/21294 | 6,747 | 추출/문제 해결형 | case_0585 | 0/11 | GPT를 활용한 카탈로그 아이템 생성 |
| woowahan/21584 | 2,189 | 제외/회고·문화·행사 | - | 0/0 | 기술블로그를 책으로, “요즘 우아한 AI 개발” 출간! |
| woowahan/21647 | 4,542 | 제외/회고·문화·행사 | - | 0/0 | [모집] Hero Tech Course 2025, 글로벌 교육생을 모집합니다 |
| woowahan/21544 | 8,757 | 추출/문제 해결형 | case_0587, case_0588, case_0589 | 0/22 | GuardDuty 이벤트 분석으로 살펴보는 침해대응 아키텍처 고도화 사례 |
| woowahan/21604 | 14,192 | 추출/실험·활용기 | case_0571 | 0/12 | 선제적 장애 대응을 위한 Sentry 최적화 적용기 |
| woowahan/21850 | 9,617 | 추출/문제 해결형 | case_0572, case_0573, case_0574 | 0/20 | 디자인 생산성을 높이는 피그마 플러그인을 만들어보자 2부: 개발 편 |
| woowahan/21918 | 5,145 | 추출/실험·활용기 | case_0575 | 0/11 | 디자인 생산성을 높이는 피그마 플러그인을 만들어보자 1부: 디자인 편 |
| woowahan/21905 | 6,319 | 추출/실험·활용기 | case_0567 | 0/10 | Gemini와 삽질로 개발자의 뒤죽박죽, 뒤죽박죽 업무 메모 AI로 심폐소생시키기 |
| woowahan/21686 | 5,803 | 추출/문제 해결형 | case_0562 | 0/9 | IllegalArgumentException은 400 Bad Request인가? |
| woowahan/22127 | 7,909 | 추출/문제 해결형 | case_0566 | 0/12 | 타입 안전한 API 모킹으로 프론트엔드 생산성 높이기 |
| woowahan/22043 | 12,846 | 추출/문제 해결형 | case_0568, case_0569, case_0570 | 0/22 | 실시간 마케팅을 위한 PoC 개발기 |
| woowahan/22151 | 8,077 | 추출/문제 해결형 | case_0563 | 0/13 | 전체 서비스를 관통하는 도메인 모듈을 안전하게 분리하기 |
| woowahan/22211 | 2,837 | 제외/회고·문화·행사 | - | 0/0 | 우아한형제들 PM들이 추천하는 책(ver.2025) |
| woowahan/22246 | 6,348 | 추출/문제 해결형 | case_0561 | 0/11 | JavaScript Proxy를 활용한 상태 추적 도구 개발기 |
| woowahan/22263 | 12,411 | 추출/문제 해결형 | case_0564, case_0565 | 0/21 | B마트 OMS의 물류주문관리를 통한 출고 최적화 |
| woowahan/22342 | 12,627 | 제외/실험·활용기 | - | 0/0 | 우리 서비스와 연결된 MCP Server 빠르게 구현해보기: MCP 해커톤 후기 |
| woowahan/22396 | 15,036 | 추출/기술 선택·도입형 | case_0557 | 0/17 | 배차 정확도를 높이는 실거리 시스템 구축하기: OSRM, Kafka, 그리고 Redis |
| woowahan/22586 | 11,025 | 추출/기술 선택·도입형 | case_0553 | 0/15 | Java야…, 우리 그만 헤어져. Kotlin으로 환승연애 |
| woowahan/22767 | 14,199 | 추출/문제 해결형 | case_0549 | 0/12 | Spring Cache(@Cacheable) + Spring Data Redis 사용 시 record 직렬화 오류 원인과 해결 |
| woowahan/22828 | 1,095 | 제외/회고·문화·행사 | - | 0/0 | 우아한테크코스 8기: AI가 코드 짜는 시대, 그래도 개발자가 되시겠습니까? |
| woowahan/23037 | 409 | 제외/회고·문화·행사 | - | 0/0 | [마감] WOOWACON 2025에 지금 등록하세요! |
| woowahan/22855 | 49,033 | 추출/기술 선택·도입형 | case_0558, case_0559, case_0560 | 0/29 | 우아한 Cloud FinOps 여정 |
| woowahan/22839 | 20,014 | 추출/기술 선택·도입형 | case_0554, case_0555, case_0556 | 0/36 | LLMOps로 확장하는 AI플랫폼 2.0 |
| woowahan/23121 | 11,621 | 추출/문제 해결형 | case_0548 | 0/11 | Redis New Connection 증가 이슈 돌아보기 |
| woowahan/23273 | 20,097 | 추출/문제 해결형 | case_0551, case_0552 | 0/21 | AI 데이터 분석가 ‘물어보새’- 3부. Agent로 더 넓고 깊은 지식 공유하기 |
| woowahan/23377 | 12,941 | 추출/실험·활용기 | case_0550 | 1/12 | Jira Automation으로 반복 업무를 효율적으로 관리해보자 |
| woowahan/23343 | 6,919 | 추출/실험·활용기 | case_0544 | 0/7 | 우아한 디버깅 툴 1부: 웹뷰/웹페이지 원격으로 디버깅하기 |
| woowahan/23457 | 3,858 | 추출/실험·활용기 | case_0547 | 0/13 | 우아한 디버깅 툴 2부: 좀 더 편하게 일하기 위한 개선들 |
| woowahan/23199 | 15,736 | 추출/기술 선택·도입형 | case_0546 | 0/16 | Server-Sent Events로 실시간 알림 전달하기 |
| woowahan/23639 | 6,092 | 추출/문제 해결형 | case_0543 | 0/11 | 코드 리뷰 봇으로 시작된 팀 문화의 변화 |
| woowahan/23138 | 13,432 | 추출/문제 해결형 | case_0541 | 0/13 | 이제 Redis를 멈춰보겠습니다: @CacheEvict 파헤치기 |
| woowahan/23667 | 7,805 | 추출/기술 선택·도입형 | case_0542 | 0/10 | 복잡한 LLM 연동, GenAI SDK 하나로 끝내기 |
| woowahan/23836 | 10,344 | 추출/실험·활용기 | case_0545 | 0/14 | 안녕하세요! AI UX라이터 제민희입니다. 무엇을 도와드릴까요? |
| woowahan/24005 | 1,451 | 제외/회고·문화·행사 | - | 0/0 | [공지] 우아한형제들 기술블로그 개인정보처리방침 일부 변경에 관한 안내 |
| woowahan/23866 | 6,856 | 추출/문제 해결형 | case_0537 | 0/11 | Vite에서 CSS 우선순위를 지키는 법: 우아한공방의 문제 해결기 |
| woowahan/24165 | 8,521 | 추출/문제 해결형 | case_0540 | 0/16 | 웹과 네이티브, 조화로운 공존은 가능한가? 플로팅웹뷰 도입으로 찾은 희망 |
| woowahan/24289 | 4,690 | 제외/회고·문화·행사 | - | 0/0 | Delivering the Future, WOOWACON 2025 |
| woowahan/24066 | 9,674 | 추출/기술 선택·도입형 | case_0538 | 0/15 | 우리 팀엔 자바스크립트 상차만 하는 프런트엔드가 있었다 |
| woowahan/23625 | 10,290 | 추출/문제 해결형 | case_0539 | 0/14 | 장시간 비동기 작업, Kafka 대신 RDB 기반 Task Queue로 해결하기 |
| woowahan/24405 | 10,355 | 추출/문제 해결형 | case_0536 | 0/12 | 100만 TPS 로그 시스템, KEDA를 이용한 오토스케일링 적용기 |
| woowahan/24488 | 5,376 | 추출/문제 해결형 | case_0530 | 0/12 | 우아한형제들이 장애를 놓치지 않고 탐지하는 방법 |
| woowahan/24568 | 11,226 | 추출/실험·활용기 | case_0531 | 0/15 | AI와 함께하는 테스트 자동화: 플러그인 개발기 |
| woowahan/24251 | 20,205 | 제외/회고·문화·행사 | - | 0/0 | 기획부터 개발까지 전부 직접 했습니다 – 우테코 7기 크루 서비스 론칭! |
| woowahan/24605 | 4,985 | 추출/문제 해결형 | case_0524 | 0/9 | 잃어버린 접근성을 찾아서 |
| woowahan/24820 | 15,858 | 제외/회고·문화·행사 | - | 0/0 | 우리는 코드처럼 문화도 리팩토링한다 |
| woowahan/24434 | 15,179 | 추출/문제 해결형 | case_0527, case_0528 | 0/22 | “함께 구매하면 좋은 상품” 추천 모델 고도화 |
| woowahan/24337 | 17,013 | 추출/기술 선택·도입형 | case_0534, case_0535 | 0/18 | 배달의민족 주문접수 채널에 Flutter를 도입하며 고민한 것 |
| woowahan/24940 | 7,721 | 제외/회고·문화·행사 | - | 0/0 | Delivering the Future: 글로벌 해커톤 2025, 준비부터 운영까지 |
| woowahan/24999 | 12,341 | 추출/문제 해결형 | case_0532, case_0533 | 0/19 | WOOWACON 2025 미니게임 WOOWA POP! |
| woowahan/25049 | 15,238 | 추출/문제 해결형 | case_0525, case_0526 | 0/16 | 끊김 없는 사용 경험을 위하여 : 카카오톡 선물함 속 교환권을 배달의민족 주문으로 연결한 여정 |
| woowahan/25189 | 10,032 | 추출/문제 해결형 | case_0523 | 0/12 | 장애 대응의 성패를 가르는 First Action: 우아한형제들의 장애 관리 라이프사이클 |
| woowahan/25900 | 15,236 | 추출/실험·활용기 | case_0529 | 1/15 | RAG, 들어는 봤는데… 내 서비스엔 어떻게 쓰지? |
| woowahan/26034 | 8,243 | 제외/실험·활용기 | - | 0/0 | AI로 바뀐 건 업무가 아니라 사람이었습니다 |
| woowahan/25986 | 7,549 | 추출/기술 선택·도입형 | case_0515 | 0/11 | 흩어져 있는 AI 자산, ‘MCP stdio’로 헤쳐모여! |
| woowahan/25888 | 6,211 | 추출/실험·활용기 | case_0516 | 0/10 | 별점 뒤에 숨겨진 리뷰의 온도, LLM으로 한 끗 차이가 다른 추천 만들기 |
| woowahan/26128 | 11,900 | 추출/문제 해결형 | case_0518 | 0/13 | pnpm 모노레포에서 React 19 마이그레이션하기: 숨겨진 호이스팅 레이어가 만든 타입 충돌 트러블슈팅 |
| woowahan/26162 | 9,011 | 추출/문제 해결형 | case_0522 | 0/12 | 5년 동안 못 푼 배민 다국어 숙제, AI와 함께 한 달 만에 끝내기 |
| woowahan/26177 | 9,496 | 추출/실험·활용기 | case_0510 | 0/10 | 하네스 엔지니어링(harness engineering)으로 팀 맞춤형 AI 환경 구축하기 |
| woowahan/26319 | 14,745 | 추출/실험·활용기 | case_0512, case_0513, case_0514 | 0/25 | 우아한공방의 새로운 동료, 시스템 맥락을 가진 챗봇서비스 개발기(feat. RAG) |
| woowahan/26388 | 11,938 | 추출/문제 해결형 | case_0509 | 0/11 | 사람도 AI도 놓친 번역 누락, ESLint 플러그인을 만들어 해결하기 |
| woowahan/26379 | 11,606 | 추출/실험·활용기 | case_0508 | 0/12 | 한 번 성공하니 다음도 쉬울 줄 알았다: 최소주문금액바 4번의 A/B실험 |
| woowahan/26459 | 11,918 | 추출/문제 해결형 | case_0511 | 0/11 | AI가 내 프롬프트를 흘려듣는 이유: 원리부터 다시 본 컨텍스트 엔지니어링 |
| woowahan/26492 | 17,700 | 추출/문제 해결형 | case_0517 | 1/13 | 멀티 어카운트 NACL 차단 자동화 도구 운영 및 개선 경험 |
| woowahan/26624 | 10,287 | 추출/실험·활용기 | case_0519, case_0520, case_0521 | 1/33 | 기술이 없던 곳에 기술 더하기: 사내 해커톤 플랫폼 만들기 |
| woowahan/26507 | 12,005 | 추출/기술 선택·도입형 | case_0507 | 0/17 | BFF 서버에 SSE를 도입한 이유: 전시 서버의 통신 구조 재설계 |
| woowahan/26729 | 6,102 | 추출/기술 선택·도입형 | case_0506 | 0/12 | 배포 없이 앱과 로컬 웹을 잇다 |
| woowahan/26777 | 2,573 | 제외/회고·문화·행사 | - | 0/0 | 기술블로그 세 번째 책 《요즘 우아한 백엔드 개발》 출간 |
| woowahan/26876 | 7,671 | 제외/회고·문화·행사 | - | 0/0 | 옆 팀은 AI를 어떻게 쓸까? 첫 사내 기술 콘퍼런스 우아한테크데이 |
| woowahan/27268 | 14,121 | 추출/문제 해결형 | case_0501, case_0502 | 0/23 | AI에게 만드는 법 대신 실패하는 법을 묻다: 포토그래퍼의 수천 명 동시 접속 게임 만들기 |
| woowahan/27381 | 10,645 | 추출/실험·활용기 | case_0503, case_0504, case_0505 | 0/31 | AI가 분석한 리서치 결과, 어떻게 만들고 전달할까요? |
| woowahan/26835 | 6,778 | 추출/문제 해결형 | case_0495 | 0/10 | 문서로만 지키던 아키텍처 규칙, 테스트 코드로 강제하기 |
| woowahan/26832 | 21,114 | 추출/기술 선택·도입형 | case_0494 | 0/11 | 한꺼번에 짊어지던 배치를 내려놓고, 하나씩 흘려보내는 워크플로로 |
| woowahan/27640 | 14,496 | 제외/회고·문화·행사 | - | 0/0 | AI 전환, 우리가 도운 건 돕는 사람이었습니다 |
| woowahan/27330 | 7,910 | 추출/문제 해결형 | case_0493 | 0/16 | 집 나간 네트워크는 돌아왔는데 React.lazy는 왜 안 돌아올까 |
| woowahan/27604 | 12,881 | 추출/실험·활용기 | case_0500 | 0/14 | 배달의민족 전자계약서 화면 개편기: AI에게 맡긴 것과 사람이 챙긴 것 |
| woowahan/27678 | 22,921 | 추출/문제 해결형 | case_0496 | 0/16 | 사장님 입점신청 자동승인 주기를 10분에서 10초로 |
| woowahan/27782 | 456 | 제외/회고·문화·행사 | - | 0/0 | 우아한형제들의 기술 콘퍼런스, WOOWACON 2026이 열립니다! |
