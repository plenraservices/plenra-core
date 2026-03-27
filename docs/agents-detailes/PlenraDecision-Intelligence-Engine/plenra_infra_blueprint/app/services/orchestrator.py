from typing import Any

from app.services.decision_gate import evaluate_decision_gate
from app.services.meta_controller import evaluate_meta_controller


class DecisionOrchestrator:
    def run(self, decision_input: dict[str, Any]) -> dict[str, Any]:
        decision_result = evaluate_decision_gate(decision_input)
        meta_payload = {
            "decision_id": decision_input.get("vertical_id", "unknown"),
            "event_type": "decision_event",
            "timestamp": decision_input.get("timestamp", "generated"),
        }
        meta_result = evaluate_meta_controller(meta_payload)
        return {
            "decision": decision_result,
            "meta_controller": meta_result,
        }
