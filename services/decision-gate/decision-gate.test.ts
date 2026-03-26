import { createDecisionGate } from "./decision-gate.service";
import type { RuleService } from "../rules/rule.service";

const mockRuleService: RuleService = {
  async getRules(verticalId: string, env: string) {
    return [
      {
        rule_id: "rule_001",
        vertical_id: verticalId,
        priority: 100,
        condition: {
          performance_status: "scale",
          is_fake_winner: false,
        },
        output: {
          decision_status: "pass",
          decision_action: "scale_up",
          decision_reason_code: "strong_unit_economics",
          budget_delta_percent: 15,
          gate_severity: "low",
          requires_manual_review: false,
        },
      },
    ];
  },
};

async function run() {
  const decisionGate = createDecisionGate(mockRuleService);

  const result = await decisionGate.evaluate({
    vertical_id: "v01_home_services",
    environment: "dev",
    payload: {
      performance_status: "scale",
      is_fake_winner: false,
    },
  });

  console.log("Decision Gate Result:");
  console.log(JSON.stringify(result, null, 2));
}

run().catch((error) => {
  console.error("Decision Gate Test Failed:");
  console.error(error);
});
