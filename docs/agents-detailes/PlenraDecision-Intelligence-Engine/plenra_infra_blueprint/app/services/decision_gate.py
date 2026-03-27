from typing import Any


def evaluate_decision_gate(payload: dict[str, Any]) -> dict[str, Any]:
    required = [
        "vertical_id",
        "traffic_allocation",
        "share",
        "roi_value",
        "rolling_roi_value",
        "rolling_roi_score",
        "profitability_score",
        "performance_status",
        "is_fake_winner",
        "is_dominant",
        "cooldown_cycles",
        "effective_cpc",
        "effective_conversion_rate",
        "previous_rolling_roi_value",
        "previous_effective_cpc",
        "portfolio_rolling_roi_value",
        "fake_winner_count",
    ]
    missing = [field for field in required if field not in payload]
    if missing:
        return {
            "status": "invalid_input",
            "reason_code": "missing_required_fields",
            "missing_fields": missing,
        }

    rolling_roi = float(payload["rolling_roi_value"])
    profitability = float(payload["profitability_score"])
    fake_winner = bool(payload["is_fake_winner"])
    cooldown_cycles = int(payload["cooldown_cycles"])

    if fake_winner:
        decision_status = "hold"
        decision_action = "maintain"
        reason_codes = ["fake_winner_detected"]
    elif cooldown_cycles > 0:
        decision_status = "cooldown"
        decision_action = "maintain"
        reason_codes = ["active_cooldown"]
    elif rolling_roi >= 1.5 and profitability >= 70:
        decision_status = "pass"
        decision_action = "scale_up"
        reason_codes = ["strong_roi_and_profitability"]
    elif rolling_roi < 0.5:
        decision_status = "reduce"
        decision_action = "reduce_15"
        reason_codes = ["weak_rolling_roi"]
    else:
        decision_status = "hold"
        decision_action = "maintain"
        reason_codes = ["mixed_signals"]

    return {
        "status": "computed",
        "vertical_id": payload["vertical_id"],
        "decision_status": decision_status,
        "decision_action": decision_action,
        "reason_codes": reason_codes,
        "debug_trace": {
            "engine": "decision_gate_v0",
            "rolling_roi_value": rolling_roi,
            "profitability_score": profitability,
            "is_fake_winner": fake_winner,
            "cooldown_cycles": cooldown_cycles,
        },
    }
