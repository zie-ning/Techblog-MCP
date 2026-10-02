# 추출 run 비교: v4-gpt-5-mini-medium vs v4r2-gpt-5-mini-medium

| 지표 | v4-gpt-5-mini-medium | v4r2-gpt-5-mini-medium |
| --- | --- | --- |
| 모델 (effort) | gpt-5-mini (medium) | gpt-5-mini (medium) |
| 프롬프트 버전 | 5bafd9ddcc5d | 5bafd9ddcc5d |
| 글 수 | 80 | 80 |
| 추출 글 | 60 (75%) | 61 (76%) |
| 제외 글 | 20 (25%) | 19 (24%) |
| 항목 수 | 74 | 82 |
| 글당 항목 수 (제외 빼고) | 1.23 | 1.34 |
| 짧은 글(<1,500자)에서 항목 만든 글 | 1 / 8 | 1 / 8 |
| 발췌 원문 존재율 | 98.9% (9/793 탈락) | 98.4% (14/852 탈락) |
| 재시도한 글 | 12 | 15 |
| 사전에 없는 기술명 (종류 / 항목당) | 199 / 3.05 | 183 / 2.61 |
| 버린 대안 (기술/설계 방식) | 86 (47/39) | 94 (50/44) |
| 가장 많은 문제 유형 (항목 대비) | 개발 생산성 50% | 개발 생산성 49% |
| 가장 많은 도메인 (항목 대비) | 사내 플랫폼·개발 도구 57% | 사내 플랫폼·개발 도구 51% |
| 비용 (편당 / 전체 추정) | $1.10 ($0.0138 / $17.4) | $1.06 ($0.0132 / $16.7) |

- 사전에 없는 기술명은 현재 기술 사전으로 다시 정규화해 센다.
- 버린 대안 유형이 없는 이전 run은 사전에 있으면 기술, 없으면 설계 방식으로 추정한다.
- 사례·인사이트로 분류한 이전 run은 둘 다 추출로 읽는다.

## 추출 여부·항목 수가 달라진 글 14편 (모든 run에 있는 글 기준)

| 글 | v4-gpt-5-mini-medium | v4r2-gpt-5-mini-medium | 제목 |
| --- | --- | --- | --- |
| d2/3461887 | 추출 1개 | 제외 0개 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Cra |
| d2/3814947 | 추출 1개 | 추출 3개 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/6512234 | 추출 1개 | 추출 7개 | 스마트스토어센터 Oracle에서 MySQL로의 무중단 전환기 |
| d2/8366976 | 추출 3개 | 추출 4개 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/8992409 | 제외 0개 | 추출 1개 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| kakao/761 | 추출 1개 | 제외 0개 | 실패를 장려하는 실험적 문화 |
| kakao/785 | 제외 0개 | 추출 1개 | if(kakao)25 Krew Day AI Talk Lounge: AI  |
| kakaopay/kakaopayins-envelope-encryption | 추출 2개 | 추출 1개 | 우리는 암호화하는데 왜 키를 사용할까? |
| kurly/claude-code-redesign-my-day | 추출 3개 | 추출 1개 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| kurly/tech-spec-adoption-with-ai-automation | 추출 1개 | 추출 3개 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 추출 2개 | 추출 1개 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/japanese-search-kuromoji-to-sudachi | 추출 1개 | 추출 2개 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kurom |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 추출 2개 | 추출 1개 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 |
| woowahan/14671 | 제외 0개 | 추출 1개 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
