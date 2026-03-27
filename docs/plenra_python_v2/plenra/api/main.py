from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from plenra.core.enums import PerformanceStatus
from plenra.core.types import DecisionGateInput
from plenra.logic.decision_gate import evaluate_decision_gate
from plenra.logic.agent_runtime import run_agent


app = FastAPI(title="Plenra API", version="0.1.0")


class DecisionGateRequest(BaseModel):
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


class AgentRequest(BaseModel):
    agent_key: str
    context: dict = {}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/decision-gate")
def decision_gate(req: DecisionGateRequest) -> dict:
    output = evaluate_decision_gate(DecisionGateInput(**req.model_dump()))
    return output.__dict__


@app.post("/agents/run")
def agents_run(req: AgentRequest) -> dict:
    return run_agent(req.agent_key, req.context)
