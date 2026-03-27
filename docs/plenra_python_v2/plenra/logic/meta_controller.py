from __future__ import annotations

from plenra.core.enums import LearningEligibility, TrustLevel
from plenra.core.types import MetaControllerInput, MetaControllerOutput
from plenra.rules.decision_rules import CONTROLLER_RULES


def evaluate_meta_controller(data: MetaControllerInput) -> MetaControllerOutput:
    reasons: list[str] = []

    if data.validation_failed:
        reasons.append("validation_failed")
        return MetaControllerOutput(
            controller_status="protect_execution",
            allow_learning_updates=False,
            trust_level=TrustLevel.LOW,
            learning_eligibility=LearningEligibility.BLOCKED,
            reason_codes=reasons,
        )

    if data.high_risk_normalization and CONTROLLER_RULES.blocked_if_high_risk_normalization:
        reasons.append("high_risk_normalization_detected")
        return MetaControllerOutput(
            controller_status="protect_learning",
            allow_learning_updates=False,
            trust_level=TrustLevel.LOW,
            learning_eligibility=LearningEligibility.BLOCKED,
            reason_codes=reasons,
        )

    if data.normalization_applied and CONTROLLER_RULES.downgrade_on_normalization:
        reasons.append("normalized_input_detected")
        return MetaControllerOutput(
            controller_status="observe_only",
            allow_learning_updates=False,
            trust_level=TrustLevel.MEDIUM,
            learning_eligibility=LearningEligibility.REVIEW,
            reason_codes=reasons,
        )

    reasons.append("input_trusted")
    return MetaControllerOutput(
        controller_status="allow_updates",
        allow_learning_updates=True,
        trust_level=TrustLevel.HIGH,
        learning_eligibility=LearningEligibility.ELIGIBLE,
        reason_codes=reasons,
    )
