from pprint import pprint

from app.services.decision_intelligence import compute_decision_intelligence


if __name__ == "__main__":
    sample = {
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
            }
        ]
    }
    pprint(compute_decision_intelligence(sample))
