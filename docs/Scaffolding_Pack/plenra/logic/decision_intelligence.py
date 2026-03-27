from __future__ import annotations


def summarize_decision_quality(records: list[dict]) -> dict:
    eligible = [r for r in records if r.get("learning_eligibility") == "eligible"]
    correct = [
        r for r in eligible
        if (r.get("evaluation") or {}).get("result") == "correct"
    ]
    avg_delta_roi = (
        sum((r.get("evaluation") or {}).get("delta_roi", 0.0) for r in correct) / len(correct)
        if correct else 0.0
    )
    return {
        "eligible_records": len(eligible),
        "correct_records": len(correct),
        "avg_delta_roi": round(avg_delta_roi, 4),
        "recommendation": "scale_learning" if len(correct) >= 3 else "observe_more",
    }
