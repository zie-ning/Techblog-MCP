<h1 align="center"><img src="docs/assets/sonbae-wordmark.svg" alt="sonbae" width="240"></h1>

국내 IT 기업 기술 블로그의 해결 사례와 실무 경험을 코딩 에이전트(Claude Code, Cursor 등)가 찾아 쓰게 하는 MCP 서버입니다.

동시성, 캐싱, 메시징, 장애 대응, LLM 활용처럼 선택지가 있는 설계를 시작하기 전에, 에이전트가 국내 기업들이 비슷한 문제를 어떻게 풀었는지 찾아보고 출처와 함께 소개합니다.

- **대상**: 토스, 우아한형제들, 카카오, 카카오페이, 네이버 D2, LY, 컬리, 올리브영 기술 블로그의 2023-09 이후 글 1,262편 (2026-09-30 수집)
- **데이터**: 글마다 문제 상황 / 해결 방법 / 성능·운영 포인트 / 버린 대안을 LLM으로 뽑은 항목 1,315개. 필드마다 원문 근거 발췌가 붙어 있고, 발췌가 원문에 실제로 있는지 코드로 검증했습니다.
- **방식**: 로컬에서 실행되는 stdio MCP 서버입니다. 검색 DB는 PC에 내려받아 씁니다. [Voyage AI](https://www.voyageai.com/) API 키를 설정하면 검색어를 Voyage로 보내 **뜻으로** 찾고(같은 뜻의 다른 표현도 찾음), 키가 없으면 PC 안에서 **단어로** 찾습니다.

## 제공하는 도구

| 도구 | 하는 일 | 예시 질문 |
| --- | --- | --- |
| `search` | 문제 상황·주제로 사례 검색 (최대 10건). 문제 유형·도메인·기술 필터 지원 | "선착순 쿠폰 발급 동시성 어떻게 처리해?" |
| `get_details` | 사례 ID로 전체 내용과 근거 발췌, 원문 링크 조회 (한 번에 5건) | "그 사례 자세히 보여줘" |
| `aggregate` | 기술·문제 유형·도메인·회사·버린 대안별 건수 집계 | "메시징 문제에 어떤 기술 사례가 많아?" |
| `/sonbae` (prompt) | 주제를 주면 사례를 찾아 "참고 사례"와 "제안"으로 나눠 답하게 하는 지시문 | `/mcp__sonbae__sonbae 선착순 쿠폰` |

에이전트가 알아서 도구를 고르므로 보통은 평소처럼 질문하면 됩니다.

## 설치

[uv](https://docs.astral.sh/uv/getting-started/installation/)와 [Git](https://git-scm.com/downloads)이 필요합니다(uv가 GitHub에서 코드를 받을 때 Git을 씁니다). Python은 uv가 알아서 준비합니다.

### 1. 서버 설치

```bash
uv tool install git+https://github.com/zie-ning/sonbae
```

`sonbae` 명령이 생깁니다. 설치 끝에 "not on your PATH" 경고가 나오면 아래 명령을 실행하고 터미널과 클라이언트를 다시 시작하세요.

```bash
uv tool update-shell
```

### 2. 클라이언트에 등록

**Claude Code**

```bash
claude mcp add --scope user sonbae -- sonbae
```

- `--scope user`는 모든 프로젝트에서 쓰는 설정입니다. 지금 프로젝트에서만 쓰려면 빼세요.
- Claude Code에서 `/mcp`를 입력해 `sonbae`가 연결됐는지 확인합니다.

**Cursor**: `~/.cursor/mcp.json`(모든 프로젝트) 또는 프로젝트의 `.cursor/mcp.json`에 추가합니다.

```json
{
  "mcpServers": {
    "sonbae": {
      "command": "sonbae"
    }
  }
}
```

**다른 MCP 클라이언트**: stdio 서버를 지원하면 `sonbae` 명령을 등록하면 됩니다. 클라이언트가 명령을 찾지 못하면 `uv tool dir --bin`이 알려 주는 폴더의 전체 경로(Windows는 `sonbae.exe`)를 쓰세요.

### 3. Voyage API 키 설정 (권장)

키가 있으면 검색어와 뜻이 같은 사례를 찾고, DB에 없는 주제는 "결과 없음"으로 더 잘 거릅니다(평가셋 기준 상위 5건 안 정답 비율 0.55 → 0.75). 키가 없어도 단어로 찾는 검색은 그대로 됩니다.

1. [Voyage AI 대시보드](https://dashboard.voyageai.com/)에서 가입하고 API keys에서 키를 만듭니다. 계정마다 무료 토큰(2억)이 있고, 검색 한 번에 약 3만 토큰(무료 한도를 넘으면 약 $0.0015)을 씁니다. 결제 수단을 등록하지 않으면 분당 호출이 제한돼 검색이 키 없는 방식으로 대체될 수 있습니다.
2. 클라이언트에 등록할 때 `VOYAGE_API_KEY` 환경 변수로 넣습니다.

**Claude Code** (1단계의 등록 명령 대신)

```bash
claude mcp add --scope user sonbae -e VOYAGE_API_KEY=<키> -- sonbae
```

**Cursor**

```json
{
  "mcpServers": {
    "sonbae": {
      "command": "sonbae",
      "env": { "VOYAGE_API_KEY": "<키>" }
    }
  }
}
```

> 키를 설정하면 `search`의 검색어와 후보 항목 요약(DB에 있는 요약문)이 Voyage API로 전송됩니다. 대화 내용이나 작업 중인 코드는 보내지 않습니다. 검색 한 번은 1~2초 걸리고, Voyage 호출이 실패하거나 8초 넘게 걸리면 단어로 찾는 방식으로 대신 검색하고 결과에 그 사실을 표시합니다.

> 설치해 두고 실행하므로 서버를 켤 때 인터넷이 필요 없습니다(검색 DB를 처음 받을 때만 필요). `uvx --from git+…`로 등록하는 방법도 있지만, 켤 때마다 GitHub를 확인해 기동이 2~3초 느리고 오프라인에서는 켜지지 않아 권하지 않습니다.

## 처음 쓸 때 알아 둘 것

- **첫 실행은 조금 걸립니다.** 검색 DB(약 15MB)를 내려받느라 첫 질문의 답이 10초 정도 늦을 수 있습니다. 한 번만 그렇고, 이후에는 서버가 켜진 뒤 2~3초 안에 검색 준비가 끝납니다.
- **도구 호출 허용**: 도구를 쓸 때마다 허용 여부를 묻습니다. 세 도구 모두 검색 DB를 읽기만 하므로 "항상 허용"을 골라도 됩니다(`search`는 Voyage 키가 있으면 검색어를 Voyage API로 보냅니다).
  - Claude Code에서는 허용 창에서 "Yes, and don't ask again"을 고르거나, `settings.json`의 `permissions.allow`에 `"mcp__sonbae"`를 넣으면 이 서버의 도구를 모두 허용합니다.
- **`/sonbae` prompt**는 MCP prompt를 지원하는 클라이언트에서만 쓸 수 있습니다. Claude Code CLI와 Cursor는 지원하고, Claude 데스크톱 앱의 Code 탭에서는 실행되지 않습니다. 이 경우에는 그냥 질문하면 됩니다.

## 에이전트 지시문 (선택)

도구 설명만으로도 에이전트가 필요할 때 호출하지만, 프로젝트의 `CLAUDE.md`나 Cursor rules에 아래 내용을 넣으면 더 꾸준히 씁니다.

```markdown
## 기술 블로그 사례 참고
동시성, 캐싱, 메시징, 장애 대응, LLM 활용처럼 선택지가 있는 설계를 시작하기 전에
sonbae MCP의 search 도구로 국내 기업 사례를 먼저 확인한다.
검색어는 한 주제의 짧은 명사구로 쓰고, 여러 하위 주제는 나눠서 검색한다.
사례를 인용할 때는 회사명과 원문 링크를 밝히고, 결과에 없는 사례는 만들어내지 않는다.
사례는 참고 자료로 소개하고, 이 프로젝트의 상황과 다른 점을 짚어 내 제안과 구분한다.
```

## 검색의 한계

- **결과 수는 관련도 기준으로 정합니다.** Voyage 키가 있으면 리랭커가 검색어에 답이 되는 정도를 점수로 매겨, 가장 관련 있는 항목도 기준에 못 미치면 "결과 없음"을 돌려줍니다. 비슷하지만 다른 주제(예: "스마트 TV 앱 성능"에 모바일 앱 성능 글)가 가끔 결과로 나오고, 반대로 사례가 있는데 결과 없음이 되는 경우도 있습니다. 에이전트는 결과가 없으면 사례를 지어내지 말고 없다고 답하도록 안내받습니다.
- **키가 없으면 단어로 찾습니다.** 같은 내용이라도 글에 쓰인 표현과 검색어가 다르면 안 찾힐 수 있습니다. 항목마다 예상 검색어와 다른 표기를 미리 넣어 두었지만, 결과가 없으면 검색어를 나누거나 다른 표현(한국어/영어 표기 등)으로 다시 찾게 하세요.
- **집계는 블로그에 쓴 사례 수입니다.** 회사의 실제 기술 도입 현황이나 업계 전체를 대표하지 않습니다.
- **매주 월요일 새 글을 반영한 DB를 배포합니다.** 서버가 하루 한 번 새 DB가 있는지 확인해 받아 두고 다음 실행부터 씁니다. 코드를 업데이트하지 않아도 새 데이터를 받습니다.

## 업데이트와 문제 해결

- **새 버전으로 업데이트**: 데이터는 자동으로 갱신됩니다. 서버 코드(도구 기능)를 새 버전으로 바꾸려면 아래 명령 후 클라이언트를 다시 시작합니다. DB 구조가 바뀐 업데이트라면 이때 새 구조의 DB를 받습니다.

  ```bash
  uv tool upgrade sonbae
  ```

- **삭제**: `uv tool uninstall sonbae`. 검색 DB는 아래 폴더를 지우면 됩니다.

- **옛 이름(`techblog-mcp`)으로 설치했다면**: 이름이 `sonbae`로 바뀌었습니다. `uv tool uninstall techblog-mcp`로 지우고 위 설치·등록을 다시 하세요. 옛 검색 DB 폴더(`techblog-mcp`)는 더 쓰지 않으니 지워도 됩니다. 환경 변수도 `TECHBLOG_MCP_*`에서 `SONBAE_*`로 바뀌었습니다.

- **검색 DB 위치**: Windows `%LOCALAPPDATA%\sonbae`, macOS `~/Library/Caches/sonbae`, Linux `~/.cache/sonbae`. 내려받은 파일은 체크섬으로 검증하며, 지워도 다음 실행 때 다시 받습니다.
- **환경 변수**
  - `SONBAE_DB`: 이미 가진 DB 파일 경로를 쓸 때 (내려받지 않음)
  - `SONBAE_CACHE_DIR`: DB를 받을 폴더를 바꿀 때
- **"검색 DB를 내려받지 못했습니다"**: 첫 실행에는 GitHub에 접속할 수 있어야 합니다. 네트워크를 확인하고 다시 질문하면 다시 시도합니다.
- **클라이언트에서 `sonbae`를 찾지 못함**: `uv tool update-shell` 후 클라이언트를 완전히 다시 시작하거나, 등록할 때 `uv tool dir --bin` 폴더의 전체 경로를 쓰세요.
- **Windows에서 설치 중 `Filename too long`**: uv 캐시 경로가 길면 Windows 경로 길이 제한에 걸릴 수 있습니다. Git의 긴 경로 지원을 켜고 다시 시도하세요.

  ```bash
  git config --global core.longpaths true
  ```

## 데이터 출처와 저작권

- 원문의 저작권은 각 회사에 있습니다. 이 저장소와 배포 DB에는 원문 전체가 없고, LLM이 쓴 요약, 필드당 1~2문장의 원문 발췌, 원문 링크만 있습니다. 에이전트가 사례를 소개할 때는 회사명과 원문 링크를 함께 밝히도록 안내합니다.
- 수집할 때는 크롤러임을 밝히는 User-Agent를 쓰고, robots.txt를 지키며, 요청 사이에 간격을 두었습니다.
- **삭제 요청**: 블로그 운영 측에서 자사 글이 포함되지 않기를 원하면 [GitHub 이슈](https://github.com/zie-ning/sonbae/issues)로 알려 주세요. 해당 항목을 배포 DB에서 빼겠습니다.

## 라이선스

코드는 [MIT 라이선스](LICENSE)입니다. 블로그 글에서 나온 데이터(요약, 발췌, 링크)는 MIT 라이선스 대상이 아니며, 원문의 권리는 각 회사에 있습니다.

## 개발

문서와 진행 현황은 [docs/README.md](docs/README.md)에서 시작하세요. 기획은 [docs/기획.md](docs/기획.md), 구현 계획은 [docs/구현계획.md](docs/구현계획.md)에 있습니다.

```bash
uv sync           # 의존성 설치
uv run pytest     # 테스트
uv run ruff check # 린트
```

데이터 파이프라인:

```bash
uv run python -m pipeline.collect all          # 원문 수집 → data/raw/ (블로그 이름으로 골라 받기 가능)
uv run python -m pipeline.extract <블로그>     # 구조화 → data/entries.jsonl (OpenAI API 키 필요)
uv run python -m pipeline.normalize            # 기술 사전에 없는 이름 리포트
uv run python -m pipeline.expand               # 문서 확장 → data/expansions.jsonl (OpenAI API 키 필요)
uv run python -m pipeline.embed                # 항목 임베딩 → data/embeddings.npz (Voyage API 키 필요)
uv run python -m pipeline.build_index          # 검색 DB → data/techblog.sqlite
uv run python -m pipeline.release_db --upload  # 검색 DB를 GitHub Release로 배포 (gh 로그인 필요)
uv run python -m pipeline.update               # 새 글만 수집→추출→확장→임베딩→빌드 (매주 GitHub Actions가 실행)
```

OpenAI·Voyage API 키는 `.env.example`을 `.env`로 복사해 `OPENAI_API_KEY`, `VOYAGE_API_KEY`를 넣거나 환경 변수로 설정합니다. 서버(`sonbae`)는 `.env`를 읽지 않으므로 서버의 키는 클라이언트 등록 때 환경 변수로 넣습니다.

저장소의 코드로 서버를 실행하려면(저장소의 `data/techblog.sqlite`를 씁니다):

```bash
claude mcp add sonbae -- uv run --directory "<저장소 절대 경로>" sonbae
```
