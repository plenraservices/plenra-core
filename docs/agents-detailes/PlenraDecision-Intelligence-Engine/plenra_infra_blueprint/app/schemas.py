from pydantic import BaseModel, Field

from app.core.enums import ConfidenceLevel, EvaluationResult, LearningEligibility, PerformanceStatus


class EvaluationSchema(BaseModel):
    result: EvaluationResult
    delta_roi: float
    delta_profit: float
    confidence: ConfidenceLevel


class IntelligenceRecord(BaseModel):
    decision_id: str
    learning_eligibility: LearningEligibility
    performance_status: PerformanceStatus
    rolling_roi_value: float
    share: float
    effective_cpc: float
    decision_action: str
    evaluation: EvaluationSchema


class IntelligenceInput(BaseModel):
    records: list[IntelligenceRecord]


class DecisionScore(BaseModel):
    decision_id: str
    decision_score: float


class PatternSchema(BaseModel):
    pattern_id: str
    performance_status: str
    rolling_roi_range: str
    share_bucket: str
    cpc_behavior: str
    sample_size: int
    success_rate: float
    avg_delta_roi: float
    avg_delta_profit: float
    dominant_action: str
    pattern_status: str


class RecommendedAdjustment(BaseModel):
    pattern_id: str
    action_bias: str


class DebugTrace(BaseModel):
    total_records_received: int
    eligible_records_used: int
    blocked_records_excluded: int
    invalid_records_excluded: int


class IntelligenceOutput(BaseModel):
    status: str
    decision_scores: list[DecisionScore] = Field(default_factory=list)
    patterns: list[PatternSchema] = Field(default_factory=list)
    recommended_adjustments: list[RecommendedAdjustment] = Field(default_factory=list)
    debug_trace: DebugTrace | None = None
    reason_code: str | None = None
