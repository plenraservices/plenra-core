from typing import Any


ORDER = {"decision_event": 1, "execution_event": 2, "outcome_event": 3}


class DecisionLedger:
    def __init__(self) -> None:
        self._events: dict[str, list[dict[str, Any]]] = {}

    def ingest(self, event: dict[str, Any]) -> dict[str, Any]:
        decision_id = event.get("decision_id")
        event_type = event.get("event_type")
        if not decision_id or event_type not in ORDER:
            return {"status": "safe_fallback", "reason_code": "invalid_event"}

        self._events.setdefault(decision_id, []).append(event)
        ordered = sorted(self._events[decision_id], key=lambda e: ORDER[e["event_type"]])
        event_types = [e["event_type"] for e in ordered]

        if event_types == ["decision_event", "execution_event", "outcome_event"]:
            lifecycle_status = "evaluated"
        elif event_types == ["decision_event"]:
            lifecycle_status = "decision_recorded"
        elif event_types == ["decision_event", "execution_event"]:
            lifecycle_status = "awaiting_outcome"
        else:
            lifecycle_status = "incomplete_or_out_of_order"

        return {
            "status": lifecycle_status,
            "decision_id": decision_id,
            "events_seen": event_types,
        }
