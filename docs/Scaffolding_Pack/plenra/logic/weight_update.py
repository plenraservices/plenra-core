from __future__ import annotations


def compute_weight_update(current_weights: dict[str, float], recommended_adjustments: list[dict], max_delta: float = 0.05) -> dict:
    score = {"increase_weight": 1, "decrease_weight": -1, "hold": 0}
    net_bias = sum(score.get(item.get("action_bias", "hold"), 0) for item in recommended_adjustments)
    keys = list(current_weights.keys())
    if not keys:
        return {"updated_weights": {}, "reason": "no_weights"}

    primary_key = keys[0]
    updated = current_weights.copy()
    updated[primary_key] = max(0.1, min(1.0, updated[primary_key] + max(-max_delta, min(max_delta, net_bias * 0.01))))

    total = sum(updated.values()) or 1.0
    updated = {k: round(v / total, 6) for k, v in updated.items()}
    return {"updated_weights": updated, "net_bias": net_bias}
