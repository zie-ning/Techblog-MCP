# 추출 run 비교: v3-gpt-5-mini-medium vs v4-gpt-5-mini-medium

| 지표 | v3-gpt-5-mini-medium | v4-gpt-5-mini-medium |
| --- | --- | --- |
| 모델 (effort) | gpt-5-mini (medium) | gpt-5-mini (medium) |
| 프롬프트 버전 | 17bac37197a4 | 5bafd9ddcc5d |
| 글 수 | 80 | 80 |
| 추출 글 | 58 (72%) | 60 (75%) |
| 제외 글 | 22 (28%) | 20 (25%) |
| 항목 수 | 77 | 74 |
| 글당 항목 수 (제외 빼고) | 1.33 | 1.23 |
| 짧은 글(<1,500자)에서 항목 만든 글 | 1 / 8 | 1 / 8 |
| 발췌 원문 존재율 | 99.1% (7/822 탈락) | 98.9% (9/793 탈락) |
| 재시도한 글 | 16 | 12 |
| 사전에 없는 기술명 (종류 / 항목당) | 156 / 2.30 | 199 / 3.05 |
| 버린 대안 (기술/설계 방식) | 91 (44/47) | 86 (47/39) |
| 가장 많은 문제 유형 (항목 대비) | 개발 생산성 31% | 개발 생산성 50% |
| 가장 많은 도메인 (항목 대비) | 사내 플랫폼·개발 도구 39% | 사내 플랫폼·개발 도구 57% |
| 비용 (편당 / 전체 추정) | $1.21 ($0.0152 / $19.2) | $1.10 ($0.0138 / $17.4) |

- 사전에 없는 기술명은 현재 기술 사전으로 다시 정규화해 센다.
- 버린 대안 유형이 없는 이전 run은 사전에 있으면 기술, 없으면 설계 방식으로 추정한다.
- 사례·인사이트로 분류한 이전 run은 둘 다 추출로 읽는다.

## 추출 여부·항목 수가 달라진 글 16편 (모든 run에 있는 글 기준)

| 글 | v3-gpt-5-mini-medium | v4-gpt-5-mini-medium | 제목 |
| --- | --- | --- | --- |
| d2/3461887 | 제외 0개 | 추출 1개 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Cra |
| d2/8366976 | 추출 4개 | 추출 3개 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/8992409 | 추출 1개 | 제외 0개 | DBT, Airflow를 활용한 데이터 계보 중심 파이프라인 만들기 |
| kakao/761 | 제외 0개 | 추출 1개 | 실패를 장려하는 실험적 문화 |
| kakao/822 | 추출 5개 | 추출 2개 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakaopay/kakaopayins-envelope-encryption | 추출 1개 | 추출 2개 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/kakaopayins-opensearch-analyzer | 추출 3개 | 추출 1개 | OpenSearch Analyzer를 활용한 검색기능 알아보기 |
| kakaopay/katfun-joy-kotlin | 추출 4개 | 추출 1개 | 코틀린, 저는 이렇게 쓰고 있습니다 |
| kurly/claude-code-redesign-my-day | 추출 1개 | 추출 3개 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| kurly/tech-spec-adoption-with-ai-automation | 추출 2개 | 추출 1개 | 개발자의 시간을 벌어주는 두 가지 도구: 잘 쓴 테크 스펙, 그리고 AI |
| ly/from-hive-to-iceberg-12x-faster-data-updates | 추출 1개 | 추출 2개 | Hive에서 Iceberg로: 데이터 반영 속도 12배 향상의 비밀 |
| ly/how-to-evaluate-ai-generated-images-1 | 제외 0개 | 추출 1개 | AI로 생성한 이미지는 어떻게 평가할까요? (기본편) |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 추출 2개 | 추출 1개 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 추출 2개 | 추출 1개 | Web Worker로 이미지 처리 최적화하기 |
| woowahan/17386 | 추출 1개 | 추출 3개 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/24999 | 추출 1개 | 추출 2개 | WOOWACON 2025 미니게임 WOOWA POP! |
