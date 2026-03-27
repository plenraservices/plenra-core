from __future__ import annotations

from plenra.core.enums import LearningEligibility, TrustLevel
from plenra.core.types import DatasetRecord


def build_dataset_record(
    *,
    decision_id: str,
    event_type: str,
    payload: dict,
    trust_level: TrustLevel,
    learning_eligibility: LearningEligibility,
    audit_tag: str,
) -> DatasetRecord:
    include = (
        learning_eligibility == LearningEligibility.ELIGIBLE
        and trust_level == TrustLevel.HIGH
    )
    return DatasetRecord(
        decision_id=decision_id,
        event_type=event_type,
        record_payload=payload,
        dataset_inclusion=include,
        trust_level=trust_level,
        learning_eligibility=learning_eligibility,
        audit_tag=audit_tag,
    )
