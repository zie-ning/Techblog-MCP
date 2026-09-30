"""시스템 curl로 요청을 보내는 httpx 전송 계층.

일부 사이트의 WAF가 Python TLS 클라이언트(httpx)를 막고 curl은 통과시킨다.
운영 측 허락을 받은 호스트에 한해 이 전송 계층을 쓴다 (docs/기획.md "수집 예절").
User-Agent 등 요청 헤더는 httpx가 만든 그대로 보내며 브라우저로 위장하지 않는다.
"""

import subprocess
import tempfile
from pathlib import Path

import httpx

# curl이 스스로 정하거나, 받은 본문을 그대로 넘기기 위해 빼는 헤더
_SKIP_HEADERS = {"host", "connection", "accept-encoding", "content-length"}


def parse_header_block(raw: bytes) -> tuple[int, list[tuple[str, str]]]:
    """curl `--dump-header` 출력에서 마지막 응답의 상태 코드와 헤더를 꺼낸다."""
    blocks = [b for b in raw.replace(b"\r\n", b"\n").split(b"\n\n") if b.strip()]
    lines = blocks[-1].decode("latin-1").split("\n")
    status = int(lines[0].split()[1])  # 예: "HTTP/1.1 200 OK", "HTTP/2 403"
    headers = []
    for line in lines[1:]:
        name, sep, value = line.partition(":")
        if sep:
            headers.append((name.strip(), value.strip()))
    return status, headers


class CurlTransport(httpx.BaseTransport):
    def __init__(self, timeout: float = 30.0):
        self._timeout = timeout

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        if request.method != "GET":
            raise NotImplementedError("CurlTransport는 GET만 지원한다")
        with tempfile.TemporaryDirectory() as tmp:
            header_path, body_path = Path(tmp) / "headers", Path(tmp) / "body"
            command = [
                "curl", "--silent", "--show-error", "--max-time", str(self._timeout),
                "--dump-header", str(header_path), "--output", str(body_path),
            ]  # fmt: skip
            for name, value in request.headers.items():
                if name.lower() not in _SKIP_HEADERS:
                    command += ["--header", f"{name}: {value}"]
            command.append(str(request.url))

            result = subprocess.run(command, capture_output=True, check=False)
            if result.returncode != 0:
                message = result.stderr.decode(errors="replace").strip()
                raise httpx.TransportError(f"curl 실패 ({result.returncode}): {message}")
            status, headers = parse_header_block(header_path.read_bytes())
            # 본문은 이미 풀린 상태로 넘기므로 압축·길이 헤더는 뺀다
            headers = [
                (k, v) for k, v in headers
                if k.lower() not in {"content-encoding", "transfer-encoding", "content-length"}
            ]  # fmt: skip
            return httpx.Response(
                status, headers=headers, content=body_path.read_bytes(), request=request
            )
