from pipeline.collect.curl_transport import parse_header_block


def test_parse_header_block():
    raw = b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nX-WP-TotalPages: 2\r\n\r\n"
    status, headers = parse_header_block(raw)
    assert status == 200
    assert ("X-WP-TotalPages", "2") in headers


def test_parse_header_block_uses_last_response():
    raw = b"HTTP/1.1 100 Continue\r\n\r\nHTTP/2 403\r\nserver: cloudflare\r\n\r\n"
    status, headers = parse_header_block(raw)
    assert status == 403
    assert headers == [("server", "cloudflare")]
