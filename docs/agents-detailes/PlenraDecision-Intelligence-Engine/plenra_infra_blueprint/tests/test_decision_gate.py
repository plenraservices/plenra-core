from app.services.decision_gate import evaluate_decision_gate


def test_decision_gate_passes_on_strong_roi() -> None:
    payload = {
        "vertical_id": "v01",
        "traffic_allocation": 1000,
        "share": 0.1,
        "roi_value": 1.7,
        "rolling_roi_value": 1.6,
        "rolling_roi_score": 90,
        "profitability_score": 80,
        "performance_status": "scale",
        "is_fake_winner": False,
        "is_dominant": True,
        "cooldown_cycles": 0,
        "effective_cpc": 2.1,
        "effective_conversion_rate": 0.03,
        "previous_rolling_roi_value": 1.4,
        "previous_effective_cpc": 2.0,
        "portfolio_rolling_roi_value": 1.0,
        "fake_winner_count": 0,
    }
    result = evaluate_decision_gate(payload)
    assert result["decision_status"] == "pass"
    assert result["decision_action"] == "scale_up"
