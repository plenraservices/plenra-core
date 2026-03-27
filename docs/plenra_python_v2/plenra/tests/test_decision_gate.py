from plenra.core.enums import PerformanceStatus, DecisionStatus
from plenra.core.types import DecisionGateInput
from plenra.logic.decision_gate import evaluate_decision_gate


def test_decision_gate_scale_path():
    result = evaluate_decision_gate(
        DecisionGateInput(
            vertical_id="v1",
            traffic_allocation=100,
            share=0.1,
            roi_value=1.2,
            rolling_roi_value=1.4,
            rolling_roi_score=90,
            profitability_score=60,
            performance_status=PerformanceStatus.SCALE,
            is_fake_winner=False,
            is_dominant=True,
            cooldown_cycles=0,
            effective_cpc=2.0,
            effective_conversion_rate=0.03,
            previous_rolling_roi_value=1.2,
            previous_effective_cpc=1.9,
            portfolio_rolling_roi_value=1.1,
            fake_winner_count=0,
        )
    )
    assert result.decision_status == DecisionStatus.PASS
