from typing import Any


def compute_counterfactual(payload: dict[str, Any]) -> dict[str, Any]:
    required = [
        "decision_id",
        "traffic_allocation",
        "effective_cpc",
        "effective_conversion_rate",
        "avg_ticket",
        "outcome_event",
    ]
    missing = [field for field in required if field not in payload]
    if missing:
        return {"status": "invalid_input", "reason_code": "missing_required_fields", "missing": missing}

    traffic = float(payload["traffic_allocation"])
    cpc = float(payload["effective_cpc"])
    conversion_rate = float(payload["effective_conversion_rate"])
    avg_ticket = float(payload["avg_ticket"])
    actual_revenue = float(payload["outcome_event"]["revenue"])
    actual_cost = float(payload["outcome_event"]["cost"])

    baseline_cost = traffic * cpc
    baseline_revenue = traffic * conversion_rate * avg_ticket
    baseline_profit = baseline_revenue - baseline_cost
    actual_profit = actual_revenue - actual_cost
    decision_gain = actual_profit - baseline_profit
    prevented_loss = max(0.0, decision_gain)

    return {
        "status": "computed",
        "decision_id": payload["decision_id"],
        "baseline_cost": baseline_cost,
        "baseline_revenue": baseline_revenue,
        "baseline_profit": baseline_profit,
        "actual_profit": actual_profit,
        "decision_gain": decision_gain,
        "prevented_loss": prevented_loss,
        "counterfactual_confidence": "medium",
    }
