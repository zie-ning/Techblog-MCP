# 추출 run 비교: baseline-gpt-5-mini-medium vs v2-gpt-5-mini-medium vs v3-gpt-5-mini-medium

| 지표 | baseline-gpt-5-mini-medium | v2-gpt-5-mini-medium | v3-gpt-5-mini-medium |
| --- | --- | --- | --- |
| 모델 (effort) | gpt-5-mini (medium) | gpt-5-mini (medium) | gpt-5-mini (medium) |
| 프롬프트 버전 | d2178d29df58 | 44b7d89476c5 | 17bac37197a4 |
| 글 수 | 80 | 80 | 80 |
| 사례 글 | 62 (78%) | 58 (72%) | 58 (72%) |
| 인사이트 글 | 2 (2%) | 3 (4%) | 0 (0%) |
| 제외 글 | 16 (20%) | 19 (24%) | 22 (28%) |
| 항목 수 (사례/인사이트) | 95 (93/2) | 83 (80/3) | 77 (77/0) |
| 글당 항목 수 (제외 빼고) | 1.48 | 1.36 | 1.33 |
| 짧은 글(<1,500자)에서 항목 만든 글 | 3 / 8 | 1 / 8 | 1 / 8 |
| 발췌 원문 존재율 | 97.3% (25/921 탈락) | 99.1% (8/887 탈락) | 99.1% (7/822 탈락) |
| 재시도한 글 | 27 | 20 | 16 |
| 사전에 없는 기술명 (종류 / 항목당) | 380 / 4.27 | 148 / 2.07 | 156 / 2.30 |
| 버린 대안 (기술/설계 방식) | 75 (3/72) | 92 (58/34) | 91 (44/47) |
| 가장 많은 주 문제 유형 | 개발 생산성 23% | 개발 생산성 23% | 개발 생산성 21% |
| 가장 많은 도메인 | 사내 플랫폼·개발 도구 40% | 사내 플랫폼·개발 도구 39% | 사내 플랫폼·개발 도구 39% |
| 비용 (편당 / 전체 추정) | $1.30 ($0.0162 / $20.5) | $1.32 ($0.0165 / $20.8) | $1.21 ($0.0152 / $19.2) |

- 사전에 없는 기술명은 현재 기술 사전으로 다시 정규화해 센다.
- 버린 대안 유형이 없는 이전 run은 사전에 있으면 기술, 없으면 설계 방식으로 추정한다.

## 구조화 유형·항목 수가 달라진 글 23편 (모든 run에 있는 글 기준)

| 글 | baseline-gpt-5-mini-medium | v2-gpt-5-mini-medium | v3-gpt-5-mini-medium | 제목 |
| --- | --- | --- | --- | --- |
| d2/1155434 | 제외 0개 | 사례 1개 | 사례 1개 | C++ std::bit_cast와 reinterpret_cast — 언제 |
| d2/3461887 | 사례 1개 | 제외 0개 | 제외 0개 | App Crash? 0.1초 만에 분석해 드릴게요, 고품질 고성능 Cra |
| d2/3814947 | 사례 3개 | 사례 1개 | 사례 1개 | 생산성을 높이는 Android SDK 배포 전략 살펴보기 |
| d2/8366976 | 사례 2개 | 사례 4개 | 사례 4개 | 호텔 검색, 어떻게 달라졌을까요? 1편 - 문제와 해결 |
| d2/9290861 | 인사이트 1개 | 제외 0개 | 제외 0개 | Inside VictoriaMetrics |
| kakao/761 | 사례 2개 | 인사이트 1개 | 제외 0개 | 실패를 장려하는 실험적 문화 |
| kakao/785 | 인사이트 1개 | 인사이트 1개 | 제외 0개 | if(kakao)25 Krew Day AI Talk Lounge: AI  |
| kakao/804 | 사례 2개 | 사례 1개 | 사례 1개 | 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개 |
| kakao/822 | 사례 2개 | 사례 2개 | 사례 5개 | 메시징 서버의 스트레스 테스트 노하우와 AI가 덜어 준 부분 |
| kakaopay/ifkakao2024-devrel | 사례 1개 | 제외 0개 | 제외 0개 | 카카오페이의 if(kakaoAI)2024 A to Z: 개발자 컨퍼런스  |
| kakaopay/kakaopayins-envelope-encryption | 사례 1개 | 사례 2개 | 사례 1개 | 우리는 암호화하는데 왜 키를 사용할까? |
| kakaopay/kakaopayins-fe-common-component | 사례 3개 | 사례 3개 | 사례 1개 | 공통 컴포넌트를 건강하게 기르기 위한 고민 |
| kakaopay/tech-strategy-tpm | 사례 1개 | 제외 0개 | 제외 0개 | 카카오페이 TPM은 어떤 일을 하나요? |
| kurly/claude-code-redesign-my-day | 사례 3개 | 사례 3개 | 사례 1개 | 클로드 코드로 개발 팀장의 하루를 재설계한 이야기 |
| ly/how-to-use-chatops-to-automate-devops-tasks-feat-slack-hubot | 사례 3개 | 사례 2개 | 사례 2개 | ChatOps를 통한 업무 자동화(feat. Slack Hubot) |
| ly/japanese-search-kuromoji-to-sudachi | 사례 3개 | 사례 1개 | 사례 1개 | 일본어 상품 검색 정확도 높이기: Elasticsearch + Kurom |
| ly/pd1-ai-hackathon-recap | 제외 0개 | 인사이트 1개 | 제외 0개 | PD1 AI 해커톤, 그 뜨거웠던 열기 속으로! |
| ly/using-sli-slo-for-improving-reliability-1-developing-framework-and-line-status | 사례 2개 | 사례 1개 | 사례 2개 | 신뢰성 향상을 위한 SLI/SLO 활용 1편 - SLI/SLO 프레임워크 |
| oliveyoung/2025-04-25_web-worker-for-image-processing | 사례 1개 | 사례 1개 | 사례 2개 | Web Worker로 이미지 처리 최적화하기 |
| toss/tds-color-system-update | 사례 3개 | 사례 1개 | 사례 1개 | 달리는 기차 바퀴 칠하기: 7년만의 컬러 시스템 업데이트 |
| woowahan/14671 | 사례 3개 | 제외 0개 | 제외 0개 | 요즘 협업 잘하는 팀은 이렇게 일합니다. |
| woowahan/17386 | 사례 3개 | 사례 3개 | 사례 1개 | 우리 팀은 카프카를 어떻게 사용하고 있을까 |
| woowahan/24999 | 사례 2개 | 사례 2개 | 사례 1개 | WOOWACON 2025 미니게임 WOOWA POP! |
