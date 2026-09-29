# techblog-mcp

국내 IT 기업 기술 블로그의 실제 해결 사례와 실무 인사이트를 코딩 에이전트(Claude Code, Cursor 등)에 제공하는 MCP 서버.

> 개발 중입니다. 기획은 [docs/기획.md](docs/기획.md), 구현 계획은 [docs/구현계획.md](docs/구현계획.md)를 참고하세요.

## 개발 환경

[uv](https://docs.astral.sh/uv/)가 필요합니다.

```bash
uv sync
uv run pytest
uv run ruff check
```

## 데이터 파이프라인 (개발용)

```bash
uv run python -m pipeline.collect oliveyoung                                   # 원문 수집 → data/raw/
uv run python -m pipeline.extract oliveyoung --post-ids-file eval/m1_posts.txt # 구조화 → data/entries.jsonl
uv run python -m pipeline.normalize                                            # 기술 사전에 없는 이름 리포트
uv run python -m pipeline.build_index                                          # 검색 DB → data/techblog.sqlite
```

추출에는 OpenAI API 키가 필요합니다. `.env.example`을 `.env`로 복사해 `OPENAI_API_KEY`를 넣거나 환경 변수로 설정하세요.

## Claude Code에 연결 (개발용)

검색 DB를 만든 뒤 저장소 루트에서:

```bash
claude mcp add techblog -- uv run --directory "<저장소 절대 경로>" techblog-mcp
```

Claude Code에서 `/mcp`로 연결 상태를 확인하고, `/mcp__techblog__techblog <주제>` prompt로 사례 비교를 요청할 수 있습니다.
