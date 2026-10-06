# 에이전트 평가 과제셋

M7 에이전트 A/B 평가용 과제 28개. 파일은 [tasks.toml](tasks.toml), 형식은 [../agent_tasks.py](../agent_tasks.py)의 `Task`다. 평가 조건(`mcp`·`none`·`web`)과 결정 근거는 [docs/기획.md "에이전트 평가 (M7)"](../../docs/기획.md#에이전트-평가-m7), 진행 기록은 [docs/milestones/M7.md](../../docs/milestones/M7.md)에 있다.

```bash
uv run python eval/agent_tasks.py   # 검증 후 과제 목록과 관련 사례 수 출력
```

## 필드

| 필드 | 뜻 |
| --- | --- |
| `id` | `t01`~ |
| `category` | 과제 분류 (아래 표) |
| `prompt` | 에이전트에게 그대로 넣는 입력. 도구를 쓰라거나 사례를 찾으라는 말은 넣지 않는다(`absent` 일부는 사용자가 사례를 직접 요청하는 경우를 일부러 넣음) |
| `expect_call` | `required`(불러야 함) / `forbidden`(부르면 안 됨) / `optional`(호출 여부만 관찰). 분류마다 고정이며 로더가 검사한다 |
| `expect_tool` | 특정 도구를 기대할 때만 (`aggregate` 과제) |
| `search_refs` | 관련 사례 라벨을 가져올 [검색 평가셋](../search/queries.toml) 질의 id. 여러 질의의 라벨은 등급이 높은 쪽으로 합친다 |
| `source`, `check` | 출처, 이 과제에서 특히 볼 것 |

## 분류

| 분류 | 개수 | 기대 호출 | 보는 것 |
| --- | --- | --- | --- |
| `design` | 15 | required | 사례를 찾아 출처와 함께 소개하고, 자기 제안과 구분하는가. 문제 유형 21개 중 사례가 많은 주제를 고르게 담았다 |
| `few` | 1 | required | 사례가 적다는 사실을 밝히는가 |
| `noise` | 2 | required | 검색 잡음이 알려진 주제(M6에서 넘어온 "대기열"·"캐시")에서 무관 카드를 걸러 내는가 |
| `aggregate` | 2 | required | `aggregate`를 쓰고 모수를 해석하는가 |
| `absent` | 4 | optional | DB에 없는 주제에서 사례를 지어내거나 일부 관련 카드를 사례처럼 소개하지 않는가 |
| `no_call` | 3 | forbidden | 코드 수정·단순 CRUD·버그 수정에서 부르지 않는가 |
| `concept` | 1 | optional | 개념 질문에서의 호출 비율 (정답 없음) |

M1 실사용 시나리오 중 9개(1~6, 7, 7-b, 7-c, 8)는 문구를 그대로 썼다. 시나리오 6-b와 9는 prompt(`/mcp__techblog__techblog`)를 직접 부르는 경우라 `none`·`web` 조건과 비교할 수 없어 뺐다.

## 관련 사례 라벨의 한계

라벨은 M5에서 검색 결과 후보를 판정한 것이다. 에이전트가 판정되지 않은 사례를 인용할 수 있으므로, 채점할 때 라벨 밖의 인용은 미판정으로 따로 센다. `search_refs`가 비어 있는 과제(`aggregate` t20, `no_call`, `concept`)는 라벨을 쓰지 않는다.
