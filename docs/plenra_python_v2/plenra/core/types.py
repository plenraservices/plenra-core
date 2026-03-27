from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from .enums import (
    DecisionAction,
    DecisionStatus,
    GateSeverity,
    LearningEligibility,
    PerformanceStatus,
    TrustLevel,
)


@dataclass(slots=True)
class DecisionGateInput:
    vertical_id: str
    traffic_allocation: float
    share: float
    roi_value: float
    rolling_roi_value: float
    rolling_roi_score: float
    profitability_score: float
    performance_status: PerformanceStatus
    is_fake_winner: bool
    is_dominant: bool
    cooldown_cycles: int
    effective_cpc: float
    effective_conversion_rate: float
    previous_rolling_roi_value: float
    previous_effective_cpc: float
    portfolio_rolling_roi_value: float
    fake_winner_count: int


@dataclass(slots=True)
class DecisionGateOutput:
    vertical_id: str
    decision_status: DecisionStatus
    decision_action: DecisionAction
    gate_severity: GateSeverity
    requires_manual_review: bool
    reason_codes: list[str] = field(default_factory=list)
    debug_trace: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class MetaControllerInput:
    validation_failed: bool = False
    normalization_applied: bool = False
    high_risk_normalization: bool = False
    source_event_count: int = 0


@dataclass(slots=True)
class MetaControllerOutput:
    controller_status: str
    allow_learning_updates: bool
    trust_level: TrustLevel
    learning_eligibility: LearningEligibility
    reason_codes: list[str] = field(default_factory=list)


@dataclass(slots=True)
class DatasetRecord:
    decision_id: str
    event_type: str
    record_payload: dict[str, Any]
    dataset_inclusion: bool
    trust_level: TrustLevel
    learning_eligibility: LearningEligibility
    audit_tag: str
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass(slots=True)
class CounterfactualInput:
    decision_id: str
    traffic_allocation: float
    effective_cpc: float
    effective_conversion_rate: float
    avg_ticket: float
    outcome_revenue: float
    outcome_cost: float


@dataclass(slots=True)
class CounterfactualOutput:
    decision_id: str
    baseline_revenue: float
    baseline_cost: float
    actual_revenue: float
    actual_cost: float
    decision_gain: float
    prevented_loss: float
    confidence: str


@dataclass(slots=True)
class ToolRequest:
    tool_name: str
    scope: str
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ToolResult:
    tool_name: str
    status: str
    output: dict[str, Any] = field(default_factory=dict)
