from app.services.decision_intelligence import compute_decision_intelligence


def test_decision_intelligence_excludes_blocked_records() -> None:
    payload = {
        "records": [
            {
                "decision_id": "dec_001",
                "learning_eligibility": "eligible",
                "performance_status": "scale",
                "rolling_roi_value": 0.8,
                "share": 0.07,
                "effective_cpc": 2.5,
                "decision_action": "scale_up",
                "evaluation": {
                    "result": "correct",
                    "delta_roi": 0.5,
                    "delta_profit": 300,
                    "confidence": "medium",
                },
            },
            {
                "decision_id": "dec_002",
                "learning_eligibility": "blocked",
                "performance_status": "scale",
                "rolling_roi_value": 0.9,
                "share": 0.08,
                "effective_cpc": 2.6,
                "decision_action": "scale_up",
                "evaluation": {
                    "result": "correct",
                    "delta_roi": 0.4,
                    "delta_profit": 250,
                    "confidence": "high",
                },
            },
        ]
    }
    result = compute_decision_intelligence(payload)
    assert result["status"] == "computed"
    assert result["debug_trace"]["eligible_records_used"] == 1
    assert result["debug_trace"]["blocked_records_excluded"] == 1
