from math import isfinite
from typing import Any


def is_finite_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and isfinite(value)


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0
