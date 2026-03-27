from __future__ import annotations

from plenra.core.types import DecisionGateInput


def validate_decision_gate_input(data: DecisionGateInput) -> list[str]:
    errors: list[str] = []
    if not data.vertical_id:
        errors.append("vertical_id_required")
    if data.traffic_allocation < 0:
        errors.append("traffic_allocation_invalid")
    if not 0 <= data.share <= 1:
        errors.append("share_out_of_range")
    if data.effective_cpc < 0:
        errors.append("effective_cpc_invalid")
    if data.effective_conversion_rate < 0:
        errors.append("effective_conversion_rate_invalid")
    return errors
