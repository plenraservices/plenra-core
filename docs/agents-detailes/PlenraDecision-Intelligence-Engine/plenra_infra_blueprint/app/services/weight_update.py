from typing import Any


WEIGHT_KEYS = ["roi_weight", "profitability_weight", "cpc_weight", "conversion_weight"]


def compute_weight_updates(payload: dict[str, Any]) -> dict[str, Any]:
    meta = payload.get("meta_controller", {})
    allow_updates = meta.get("enforcement", {}).get("allow_weight_updates", False)
    if not allow_updates:
        return {"status": "blocked", "reason_code": "meta_controller_blocked_updates"}

    current_weights = payload.get("current_weights", {})
    max_change = float(payload.get("stability_rule", {}).get("max_weight_change_per_cycle", 0.05))
    recommendations = payload.get("recommended_adjustments", [])

    score = 0
    for item in recommendations:
        if item.get("action_bias") == "increase_weight":
            score += 1
        elif item.get("action_bias") == "decrease_weight":
            score -= 1

    delta = max(-max_change, min(max_change, score * 0.01))
    new_weights = {}
    for key in WEIGHT_KEYS:
        base = float(current_weights.get(key, 0.25))
        new_weights[key] = max(0.0, min(1.0, base + delta if key == "roi_weight" else base - delta / 3))

    total = sum(new_weights.values())
    normalized = {key: value / total for key, value in new_weights.items()} if total else new_weights

    return {
        "status": "computed",
        "recommended_weights": normalized,
        "applied_delta": delta,
    }
