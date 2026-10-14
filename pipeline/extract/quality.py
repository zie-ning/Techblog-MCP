"""발췌 탈락률 지표와 급등 판단 (docs/기획.md "자동 갱신").

탈락률 = 발췌 검증에 실패한 발췌 수 / 검증 전 발췌 수. 두 가지를 본다.
- 최종: 재시도 후 채택한 결과 기준. 실제로 버린 내용의 비율이다.
- 재시도 전: 첫 구조화 기준. 재시도가 메워 주는 품질 저하(모델 변경, 블로그 HTML 구조 변경,
  프롬프트 회귀)를 최종 탈락률보다 일찍 드러낸다. M8부터 기록해 이전 글에는 없다.

한 번 실행의 발췌가 적으면 한두 개만 탈락해도 비율이 크게 흔들리므로, 이번 실행 발췌가
`MIN_EVIDENCE`개 이상일 때만 판단한다. 탈락률이 절대 하한 이상이면서 누적 기준값의
`SPIKE_RATIO`배 이상이면 급등이다. 기준값은 이번 실행 전 기록에서 계산하고, 기록이 부족하면
하한만 본다.
"""

from collections.abc import Iterable
from dataclasses import dataclass

from pipeline.extract.schema import PostRecord

MIN_EVIDENCE = 50
SPIKE_RATIO = 3.0
# 누적 최종 탈락률 0.64%(M4 전체 추출), M3 평가 실행의 재시도 전 탈락률 1.6~3.6%를 보고 정했다
FINAL_FLOOR = 0.03
FIRST_ATTEMPT_FLOOR = 0.10


@dataclass(frozen=True)
class Rate:
    dropped: int = 0
    total: int = 0

    @property
    def value(self) -> float | None:
        return self.dropped / self.total if self.total else None

    def __str__(self) -> str:
        if self.value is None:
            return "-"
        return f"{self.dropped}/{self.total} ({self.value:.1%})"


def final_rate(records: Iterable[PostRecord]) -> Rate:
    records = list(records)
    return Rate(sum(r.dropped_evidence for r in records), sum(r.evidence_total for r in records))


def first_attempt_rate(records: Iterable[PostRecord]) -> Rate:
    known = [r for r in records if r.first_attempt_total is not None]
    return Rate(
        sum(r.first_attempt_dropped or 0 for r in known),
        sum(r.first_attempt_total or 0 for r in known),
    )


@dataclass(frozen=True)
class Check:
    name: str
    current: Rate
    baseline: Rate
    threshold: float | None  # None이면 이번 실행 발췌가 적어 판단하지 않음

    @property
    def spike(self) -> bool:
        value = self.current.value
        return self.threshold is not None and value is not None and value >= self.threshold

    def __str__(self) -> str:
        text = f"{self.name} 탈락률 {self.current}, 누적 기준 {self.baseline}"
        if self.threshold is None:
            return f"{text}, 발췌 {MIN_EVIDENCE}개 미만이라 판단 안 함"
        verdict = "급등" if self.spike else "정상"
        return f"{text}, 판단 기준 {self.threshold:.1%} 이상 → {verdict}"


def check(name: str, current: Rate, baseline: Rate, floor: float) -> Check:
    if current.total < MIN_EVIDENCE:
        threshold = None
    elif baseline.total < MIN_EVIDENCE or baseline.value is None:
        threshold = floor
    else:
        threshold = max(floor, SPIKE_RATIO * baseline.value)
    return Check(name, current, baseline, threshold)


def check_run(run: list[PostRecord], previous: Iterable[PostRecord]) -> list[Check]:
    """이번 실행에서 추출한 글의 탈락률을 이전 기록과 비교한다.

    이번 실행에서 다시 추출한 글의 옛 기록은 기준값에서 뺀다.
    """
    urls = {r.url for r in run}
    baseline = [r for r in previous if r.url not in urls]
    return [
        check("최종", final_rate(run), final_rate(baseline), FINAL_FLOOR),
        check(
            "재시도 전",
            first_attempt_rate(run),
            first_attempt_rate(baseline),
            FIRST_ATTEMPT_FLOOR,
        ),
    ]
