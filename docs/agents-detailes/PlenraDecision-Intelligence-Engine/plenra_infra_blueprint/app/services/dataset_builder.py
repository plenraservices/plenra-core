from typing import Any


VALID_EVENT_TYPES = {"decision_event", "execution_event", "outcome_event"}


def build_dataset_record(payload: dict[str, Any]) -> dict[str, Any]:
    decision_id = payload.get("decision_id")
    event_type = payload.get("event_type")
    meta = payload.get("meta_controller", {})

    if not decision_id or event_type not in VALID_EVENT_TYPES:
        return {
            "status": "safe_fallback",
            "dataset_inclusion": False,
            "storage_target": "audit_only",
            "audit_tag": "invalid_input",
        }

    learning_eligibility = meta.get("learning_eligibility", "blocked")
    trusted = meta.get("trust_level", "low_trust")
    dataset_inclusion = learning_eligibility == "eligible" and trusted == "trusted"

    if dataset_inclusion:
        storage_target = "learning_dataset"
        audit_tag = "none"
    else:
        storage_target = "audit_only"
        audit_tag = "blocked_from_learning"

    return {
        "status": "stored",
        "decision_id": decision_id,
        "event_type": event_type,
        "dataset_inclusion": dataset_inclusion,
        "trust_level": trusted,
        "learning_eligibility": learning_eligibility,
        "storage_target": storage_target,
        "audit_tag": audit_tag,
    }
