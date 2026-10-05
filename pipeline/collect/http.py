"""수집 예절을 지키는 공통 HTTP 클라이언트.

모든 수집기는 이 클라이언트로만 요청한다.
- 누가 왜 수집하는지 밝히는 User-Agent를 쓰고 브라우저로 위장하지 않는다.
- 요청 전에 robots.txt를 확인해 금지된 경로는 요청하지 않는다.
- 같은 호스트에 대한 요청 사이에 간격을 둔다.
- 봇 확인은 원칙적으로 우회하지 않는다. 운영 측 허락을 받은 호스트만 `CURL_HOSTS`에 두고
  시스템 curl로 요청한다 (위 세 원칙은 그대로 적용).
"""

import time
from urllib.parse import urlsplit
from urllib.robotparser import RobotFileParser

import httpx

from pipeline.collect.curl_transport import CurlTransport

USER_AGENT = "TechblogCaseBot/0.1 (+https://github.com/zie-ning/Techblog-MCP)"

# WAF가 Python TLS 클라이언트를 막아 curl로 요청하는 호스트.
# 운영 측 허락을 받은 곳만 추가한다 (docs/기획.md "수집 예절")
CURL_HOSTS = {
    "techblog.woowahan.com",  # 2026-09-30 허락
}


class DisallowedByRobots(Exception):
    """robots.txt가 금지한 URL을 요청하려 할 때 발생한다."""


class PoliteClient:
    def __init__(self, delay: float = 1.0, timeout: float = 30.0):
        self._delay = delay
        self._client = httpx.Client(
            headers={"User-Agent": USER_AGENT},
            timeout=timeout,
            follow_redirects=True,
            mounts={f"https://{host}": CurlTransport(timeout) for host in CURL_HOSTS},
        )
        self._robots: dict[str, RobotFileParser] = {}
        self._last_request_at: dict[str, float] = {}

    def __enter__(self) -> "PoliteClient":
        return self

    def __exit__(self, *exc) -> None:
        self._client.close()

    def get(self, url: str) -> httpx.Response:
        """robots.txt를 확인하고 간격을 둔 뒤 GET 요청한다. 2xx가 아니면 예외를 던진다."""
        if not self._robots_for(url).can_fetch(USER_AGENT, url):
            raise DisallowedByRobots(url)
        response = self._request(url)
        response.raise_for_status()
        return response

    def _request(self, url: str) -> httpx.Response:
        host = urlsplit(url).netloc
        elapsed = time.monotonic() - self._last_request_at.get(host, float("-inf"))
        if elapsed < self._delay:
            time.sleep(self._delay - elapsed)
        try:
            return self._client.get(url)
        finally:
            self._last_request_at[host] = time.monotonic()

    def _robots_for(self, url: str) -> RobotFileParser:
        parts = urlsplit(url)
        origin = f"{parts.scheme}://{parts.netloc}"
        if origin not in self._robots:
            self._robots[origin] = self._fetch_robots(origin)
        return self._robots[origin]

    def _fetch_robots(self, origin: str) -> RobotFileParser:
        parser = RobotFileParser()
        response = self._request(f"{origin}/robots.txt")
        # RFC 9309: 4xx면 제한 없음으로, 5xx 등 서버 오류면 전체 금지로 본다
        if response.is_success:
            parser.parse(response.text.splitlines())
        elif 400 <= response.status_code < 500:
            parser.allow_all = True
        else:
            parser.disallow_all = True
        return parser
