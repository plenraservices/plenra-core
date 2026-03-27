from __future__ import annotations

from plenra.core.enums import DecisionAction, DecisionStatus, GateSeverity, PerformanceStatus
from plenra.core.types import DecisionGateInput, DecisionGateOutput
from plenra.rules.decision_rules import THRESHOLDS
from plenra.validators.decision_gate_validator import validate_decision_gate_input


def evaluate_decision_gate(data: DecisionGateInput) -> DecisionGateOutput:
    errors = validate_decision_gate_input(data)
    if errors:
        return DecisionGateOutput(
            vertical_id=data.vertical_id or "unknown",
            decision_status=DecisionStatus.MANUAL_REVIEW,
            decision_action=DecisionAction.SEND_TO_REVIEW,
            gate_severity=GateSeverity.DANGER,
            requires_manual_review=True,
            reason_codes=errors,
            debug_trace={"validation_failed": True},
        )

    reasons: list[str] = []
    debug = {
        "rolling_roi_value": data.rolling_roi_value,
        "profitability_score": data.profitability_score,
        "effective_cpc": data.effective_cpc,
        "share": data.share,
        "fake_winner_count": data.fake_winner_count,
    }

    cpc_jump_ratio = (
        data.effective_cpc / data.previous_effective_cpc
        if data.previous_effective_cpc > 0
        else 1.0
    )
    debug["cpc_jump_ratio"] = round(cpc_jump_ratio, 4)

    if data.is_fake_winner or data.fake_winner_count >= THRESHOLDS.fake_winner_penalty_count:
        reasons.append("fake_winner_detected")
        return DecisionGateOutput(
            vertical_id=data.vertical_id,
            decision_status=DecisionStatus.REDUCE,
            decision_action=DecisionAction.REDUCE_30,
            gate_severity=GateSeverity.DANGER,
            requires_manual_review=False,
            reason_codes=reasons,
            debug_trace=debug,
        )

    if data.performance_status == PerformanceStatus.TERMINATE:
        reasons.append("performance_status_terminate")
        return DecisionGateOutput(
            vertical_id=data.vertical_id,
            decision_status=DecisionStatus.STOP,
            decision_action=DecisionAction.PAUSE,
            gate_severity=GateSeverity.DANGER,
            requires_manual_review=True,
            reason_codes=reasons,
            debug_trace=debug,
        )

    if data.cooldown_cycles > THRESHOLDS.cooldown_cycle_limit:
        reasons.append("cooldown_limit_exceeded")
        return DecisionGateOutput(
            vertical_id=data.vertical_id,
            decision_status=DecisionStatus.COOLDOWN,
            decision_action=DecisionAction.START_COOLDOWN,
            gate_severity=GateSeverity.WARNING,
            requires_manual_review=False,
            reason_codes=reasons,
            debug_trace=debug,
        )

    if cpc_jump_ratio >= THRESHOLDS.dangerous_cpc_jump_ratio:
        reasons.append("dangerous_cpc_jump")
        return DecisionGateOutput(
            vertical_id=data.vertical_id,
            decision_status=DecisionStatus.REDUCE,
            decision_action=DecisionAction.REDUCE_15,
            gate_severity=GateSeverity.WARNING,
            requires_manual_review=False,
            reason_codes=reasons,
            debug_trace=debug,
        )

    if data.rolling_roi_value >= THRESHOLDS.min_scale_rolling_roi and data.profitability_score >= THRESHOLDS.profitability_warning_score:
        reasons.append("scale_conditions_met")
        return DecisionGateOutput(
            vertical_id=data.vertical_id,
            decision_status=DecisionStatus.PASS,
            decision_action=DecisionAction.SCALE_UP,
            gate_severity=GateSeverity.SAFE,
            requires_manual_review=False,
            reason_codes=reasons,
            debug_trace=debug,
        )

    if data.rolling_roi_value >= THRESHOLDS.min_hold_rolling_roi:
        reasons.append("hold_conditions_met")
        return DecisionGateOutput(
            vertical_id=data.vertical_id,
            decision_status=DecisionStatus.HOLD,
            decision_action=DecisionAction.MAINTAIN,
            gate_severity=GateSeverity.WARNING,
            requires_manual_review=False,
            reason_codes=reasons,
            debug_trace=debug,
        )

    reasons.append("sub_threshold_performance")
    return DecisionGateOutput(
        vertical_id=data.vertical_id,
        decision_status=DecisionStatus.REDUCE,
        decision_action=DecisionAction.REDUCE_15,
        gate_severity=GateSeverity.WARNING,
        requires_manual_review=False,
        reason_codes=reasons,
        debug_trace=debug,
    )
