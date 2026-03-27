from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DecisionThresholds:
    min_scale_rolling_roi: float = 1.30
    min_hold_rolling_roi: float = 1.00
    fake_winner_penalty_count: int = 1
    dominant_share_threshold: float = 0.10
    dangerous_cpc_jump_ratio: float = 1.25
    profitability_warning_score: float = 55.0
    profitability_danger_score: float = 40.0
    min_conversion_rate: float = 0.015
    cooldown_cycle_limit: int = 2


@dataclass(frozen=True, slots=True)
class ControllerRules:
    learning_allowed_only_if_validation_ok: bool = True
    blocked_if_high_risk_normalization: bool = True
    downgrade_on_normalization: bool = True


@dataclass(frozen=True, slots=True)
class ToolRules:
    external_call_default: str = "block"
    delete_high_sensitivity_default: str = "hold"
    read_locked_scope_default: str = "allow"
    write_requires_validation: bool = True


THRESHOLDS = DecisionThresholds()
CONTROLLER_RULES = ControllerRules()
TOOL_RULES = ToolRules()
