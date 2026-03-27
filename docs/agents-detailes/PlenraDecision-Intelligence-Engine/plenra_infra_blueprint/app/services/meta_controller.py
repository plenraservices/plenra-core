from math import isfinite
from typing import Any


REQUIRED_FIELDS = ["decision_id", "event_type", "timestamp"]


def evaluate_meta_controller(payload: dict[str, Any]) -> dict[str, Any]:
    validation_failed = False
    missing_fields = [field for field in REQUIRED_FIELDS if field not in payload]
    if missing_fields:
        validation_failed = True

    normalization_applied = False
    high_risk_normalization = False

    for key, value in payload.items():
        if isinstance(value, float) and not isfinite(value):
            validation_failed = True

    if validation_failed:
        controller_status = "safe_fallback"
        trust_level = "low_trust"
        allow_learning = False
        failure_classification = "invalid_input_envelope"
    elif high_risk_normalization:
        controller_status = "safe_fallback"
        trust_level = "quarantine"
        allow_learning = False
        failure_classification = "high_risk_normalization_detected"
    elif normalization_applied:
        controller_status = "safe_fallback"
        trust_level = "low_trust"
        allow_learning = False
        failure_classification = "normalized_input_detected"
    else:
        controller_status = "accepted"
        trust_level = "trusted"
        allow_learning = True
        failure_classification = "none"

    return {
        "status": controller_status,
        "controller_status": controller_status,
        "trust_level": trust_level,
        "learning_eligibility": "eligible" if allow_learning else "blocked",
        "enforcement": {"allow_weight_updates": allow_learning},
        "debug_trace": {
            "missing_fields": missing_fields,
            "validation_failed": validation_failed,
            "normalization_applied": normalization_applied,
            "high_risk_normalization": high_risk_normalization,
            "failure_classification": failure_classification,
        },
    }
