from plenra.agents import CentralAgent
from plenra.core.enums import PerformanceStatus
from plenra.core.types import DecisionGateInput, MetaControllerInput, CounterfactualInput
from plenra.logic.counterfactual_engine import evaluate_counterfactual
from plenra.logic.decision_gate import evaluate_decision_gate
from plenra.logic.meta_controller import evaluate_meta_controller


def run_demo() -> None:
    agent = CentralAgent()
    print(agent.run({"surface": "budget_increase"}))

    gate_input = DecisionGateInput(
        vertical_id="v01_home_services",
        traffic_allocation=800,
        share=0.10,
        roi_value=1.30,
        rolling_roi_value=1.40,
        rolling_roi_score=85,
        profitability_score=52,
        performance_status=PerformanceStatus.SCALE,
        is_fake_winner=False,
        is_dominant=True,
        cooldown_cycles=0,
        effective_cpc=2.5,
        effective_conversion_rate=0.03,
        previous_rolling_roi_value=1.2,
        previous_effective_cpc=2.4,
        portfolio_rolling_roi_value=0.5,
        fake_winner_count=0,
    )
    print(evaluate_decision_gate(gate_input))

    controller_input = MetaControllerInput(
        validation_failed=False,
        normalization_applied=False,
        high_risk_normalization=False,
        source_event_count=3,
    )
    print(evaluate_meta_controller(controller_input))

    cf_input = CounterfactualInput(
        decision_id="dec_001",
        traffic_allocation=1000,
        effective_cpc=2,
        effective_conversion_rate=0.02,
        avg_ticket=200,
        outcome_revenue=4000,
        outcome_cost=2000,
    )
    print(evaluate_counterfactual(cf_input))


if __name__ == "__main__":
    run_demo()
