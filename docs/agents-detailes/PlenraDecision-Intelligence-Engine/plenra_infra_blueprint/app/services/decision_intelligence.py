from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Any

from app.core.enums import ConfidenceLevel, EvaluationResult, LearningEligibility
from app.core.utils import is_finite_number, mean


CONFIDENCE_WEIGHTS: dict[ConfidenceLevel, float] = {
    ConfidenceLevel.HIGH: 1.0,
    ConfidenceLevel.MEDIUM: 0.6,
    ConfidenceLevel.LOW: 0.3,
}


@dataclass(frozen=True)
class ValidatedRecord:
    decision_id: str
    learning_eligibility: str
    performance_status: str
    rolling_roi_value: float
    share: float
    effective_cpc: float
    decision_action: str
    evaluation_result: str
    delta_roi: float
    delta_profit: float
    confidence: str


def _rolling_roi_range(value: float) -> str:
    if value < 0:
        return "negative"
    if value < 0.5:
        return "low"
    if value < 1.5:
        return "mid"
    return "high"


def _share_bucket(value: float) -> str:
    if value < 0.05:
        return "small"
    if value < 0.12:
        return "medium"
    return "large"


def _cpc_behavior(value: float) -> str:
    if value < 2:
        return "stable"
    if value < 4:
        return "rising"
    return "spiking"


def _decision_score(result: str, confidence: str) -> float:
    base = {
        EvaluationResult.CORRECT.value: 1.0,
        EvaluationResult.INCORRECT.value: -1.0,
        EvaluationResult.NEUTRAL.value: 0.0,
    }[result]
    weight = CONFIDENCE_WEIGHTS[ConfidenceLevel(confidence)]
    return base * weight


REQUIRED_PATHS = [
    ("decision_id",),
    ("learning_eligibility",),
    ("performance_status",),
    ("rolling_roi_value",),
    ("share",),
    ("effective_cpc",),
    ("decision_action",),
    ("evaluation", "result"),
    ("evaluation", "delta_roi"),
    ("evaluation", "delta_profit"),
    ("evaluation", "confidence"),
]


def _get_path(obj: dict[str, Any], path: tuple[str, ...]) -> Any:
    current: Any = obj
    for part in path:
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def _validate_record(record: Any) -> ValidatedRecord | None:
    if not isinstance(record, dict):
        return None

    for path in REQUIRED_PATHS:
        if _get_path(record, path) is None:
            return None

    numeric_values = [
        record["rolling_roi_value"],
        record["share"],
        record["effective_cpc"],
        record["evaluation"]["delta_roi"],
        record["evaluation"]["delta_profit"],
    ]
    if not all(is_finite_number(v) for v in numeric_values):
        return None

    if record["performance_status"] not in {"scale", "observe", "iterate", "cooldown", "terminate"}:
        return None
    if record["evaluation"]["result"] not in {"correct", "incorrect", "neutral"}:
        return None
    if record["evaluation"]["confidence"] not in {"low", "medium", "high"}:
        return None
    if record["learning_eligibility"] not in {"eligible", "blocked"}:
        return None

    return ValidatedRecord(
        decision_id=str(record["decision_id"]),
        learning_eligibility=str(record["learning_eligibility"]),
        performance_status=str(record["performance_status"]),
        rolling_roi_value=float(record["rolling_roi_value"]),
        share=float(record["share"]),
        effective_cpc=float(record["effective_cpc"]),
        decision_action=str(record["decision_action"]),
        evaluation_result=str(record["evaluation"]["result"]),
        delta_roi=float(record["evaluation"]["delta_roi"]),
        delta_profit=float(record["evaluation"]["delta_profit"]),
        confidence=str(record["evaluation"]["confidence"]),
    )


def compute_decision_intelligence(payload: dict[str, Any]) -> dict[str, Any]:
    records = payload.get("records")
    if not isinstance(records, list):
        return {"status": "invalid_input", "reason_code": "invalid_input_envelope"}

    valid_records: list[ValidatedRecord] = []
    invalid_records = 0
    blocked_records = 0

    for raw in records:
        validated = _validate_record(raw)
        if validated is None:
            invalid_records += 1
            continue
        if validated.learning_eligibility != LearningEligibility.ELIGIBLE.value:
            blocked_records += 1
            continue
        valid_records.append(validated)

    decision_scores = [
        {
            "decision_id": record.decision_id,
            "decision_score": _decision_score(record.evaluation_result, record.confidence),
        }
        for record in valid_records
    ]

    grouped: dict[str, list[ValidatedRecord]] = defaultdict(list)
    pattern_fields: dict[str, dict[str, str]] = {}

    for record in valid_records:
        roi_range = _rolling_roi_range(record.rolling_roi_value)
        share_bucket = _share_bucket(record.share)
        cpc_behavior = _cpc_behavior(record.effective_cpc)
        pattern_id = f"{record.performance_status}_{roi_range}_{share_bucket}_{cpc_behavior}"
        grouped[pattern_id].append(record)
        pattern_fields[pattern_id] = {
            "performance_status": record.performance_status,
            "rolling_roi_range": roi_range,
            "share_bucket": share_bucket,
            "cpc_behavior": cpc_behavior,
        }

    patterns: list[dict[str, Any]] = []
    recommended_adjustments: list[dict[str, str]] = []

    for pattern_id in sorted(grouped.keys()):
        items = grouped[pattern_id]
        sample_size = len(items)
        correct_count = sum(1 for item in items if item.evaluation_result == EvaluationResult.CORRECT.value)
        total_count = sum(
            1
            for item in items
            if item.evaluation_result
            in {
                EvaluationResult.CORRECT.value,
                EvaluationResult.INCORRECT.value,
                EvaluationResult.NEUTRAL.value,
            }
        )
        success_rate = correct_count / total_count if total_count else 0.0
        avg_delta_roi = mean([item.delta_roi for item in items])
        avg_delta_profit = mean([item.delta_profit for item in items])

        action_counts = Counter(item.decision_action for item in items)
        dominant_action = sorted(action_counts.items(), key=lambda x: (-x[1], x[0]))[0][0]
        pattern_status = "usable" if sample_size >= 2 else "insufficient_data"

        if pattern_status == "insufficient_data":
            action_bias = "hold"
        elif success_rate >= 0.7:
            action_bias = "increase_weight"
        elif success_rate <= 0.4:
            action_bias = "decrease_weight"
        else:
            action_bias = "hold"

        patterns.append(
            {
                "pattern_id": pattern_id,
                **pattern_fields[pattern_id],
                "sample_size": sample_size,
                "success_rate": success_rate,
                "avg_delta_roi": avg_delta_roi,
                "avg_delta_profit": avg_delta_profit,
                "dominant_action": dominant_action,
                "pattern_status": pattern_status,
            }
        )
        recommended_adjustments.append({"pattern_id": pattern_id, "action_bias": action_bias})

    return {
        "status": "computed",
        "decision_scores": decision_scores,
        "patterns": patterns,
        "recommended_adjustments": recommended_adjustments,
        "debug_trace": {
            "total_records_received": len(records),
            "eligible_records_used": len(valid_records),
            "blocked_records_excluded": blocked_records,
            "invalid_records_excluded": invalid_records,
        },
    }
