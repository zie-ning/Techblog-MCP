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
