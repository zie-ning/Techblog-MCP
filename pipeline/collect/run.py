"""여러 블로그를 차례로 수집한다.

수집 명령(`pipeline.collect`)과 자동 갱신(`pipeline.update`)이 함께 쓴다.
"""

import sys
from collections.abc import Callable, Collection, Mapping
from dataclasses import dataclass, field
from pathlib import Path

import httpx

from pipeline.collect import d2, kakao, kakaopay, kurly, ly, oliveyoung, raw, toss, woowahan
from pipeline.collect.common import CollectResult
from pipeline.collect.http import DisallowedByRobots, PoliteClient

Collector = Callable[..., CollectResult]

COLLECTORS: dict[str, Collector] = {
    d2.SOURCE: d2.collect,
    kakao.SOURCE: kakao.collect,
    kakaopay.SOURCE: kakaopay.collect,
    kurly.SOURCE: kurly.collect,
    ly.SOURCE: ly.collect,
    oliveyoung.SOURCE: oliveyoung.collect,
    toss.SOURCE: toss.collect,
    woowahan.SOURCE: woowahan.collect,
}


@dataclass
class CollectReport:
    results: dict[str, CollectResult] = field(default_factory=dict)
    source_failures: dict[str, str] = field(default_factory=dict)  # 목록 요청부터 실패한 블로그

    @property
    def failed(self) -> bool:
        return bool(self.source_failures) or any(r.failures for r in self.results.values())


def collect_sources(
    client: PoliteClient,
    sources: list[str],
    raw_dir: Path = raw.RAW_DIR,
    refresh: bool = False,
    known: Mapping[str, Collection[str]] | None = None,
    collectors: Mapping[str, Collector] = COLLECTORS,
) -> CollectReport:
    """블로그별로 수집하고 요약을 출력한다. `known`은 블로그 → 이미 추출한 글의 post_id.

    목록 요청 자체가 막히면 그 블로그만 실패로 두고 나머지는 계속 수집한다.
    """
    known = known or {}
    report = CollectReport()
    for source in sources:
        try:
            result = collectors[source](
                client, raw_dir=raw_dir, refresh=refresh, known=known.get(source, frozenset())
            )
        except (httpx.HTTPError, DisallowedByRobots, ValueError) as e:
            report.source_failures[source] = f"{type(e).__name__}: {e}"
            print(f"{source}: 수집 실패 ({type(e).__name__}: {e})", file=sys.stderr)
            continue
        report.results[source] = result
        print(_summary(source, result))
        for url, reason in result.failures:
            print(f"  실패 {url}: {reason}", file=sys.stderr)
    return report


def _summary(source: str, result: CollectResult) -> str:
    oldest = min((p.published_at for p in result.saved), default=None)
    summary = f"{source}: {len(result.saved)}편 저장"
    if oldest:
        summary += f" (가장 오래된 글: {oldest.astimezone(raw.KST):%Y-%m-%d})"
    if result.skipped:
        summary += f", 캐시·추출 기록 {result.skipped}편 건너뜀"
    if result.out_of_period:
        summary += f", 기간 밖 {result.out_of_period}편"
    return summary
