from fastapi import APIRouter

from app.services.decision_gate import evaluate_decision_gate
from app.services.decision_intelligence import compute_decision_intelligence

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/decision/evaluate")
def evaluate_decision(payload: dict) -> dict:
    return evaluate_decision_gate(payload)


@router.post("/learning/intelligence")
def run_intelligence(payload: dict) -> dict:
    return compute_decision_intelligence(payload)
