from __future__ import annotations

from plenra.core.types import CounterfactualInput, CounterfactualOutput


def evaluate_counterfactual(data: CounterfactualInput) -> CounterfactualOutput:
    baseline_cost = data.traffic_allocation * data.effective_cpc
    baseline_revenue = data.traffic_allocation * data.effective_conversion_rate * data.avg_ticket
    actual_revenue = data.outcome_revenue
    actual_cost = data.outcome_cost
    decision_gain = actual_revenue - baseline_revenue
    prevented_loss = max(0.0, baseline_cost - actual_cost)
    confidence = "high" if data.traffic_allocation > 0 and data.avg_ticket > 0 else "low"

    return CounterfactualOutput(
        decision_id=data.decision_id,
        baseline_revenue=round(baseline_revenue, 2),
        baseline_cost=round(baseline_cost, 2),
        actual_revenue=round(actual_revenue, 2),
        actual_cost=round(actual_cost, 2),
        decision_gain=round(decision_gain, 2),
        prevented_loss=round(prevented_loss, 2),
        confidence=confidence,
    )
