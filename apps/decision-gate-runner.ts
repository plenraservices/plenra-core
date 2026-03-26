import { db } from "../services/db";
import { createDecisionGate } from "../services/decision-gate/decision-gate.service";
import type { RuleService } from "../services/rules/rule.service";

const ruleService: RuleService = {
  async getRules(verticalId: string, environment: string) {
    const result = await db.query(
      `
      SELECT rule_json
      FROM decision_rules
      WHERE vertical_id = $1
        AND environment = $2
        AND is_active = true
      ORDER BY priority DESC
      `,
      [verticalId, environment]
    );

    return result.rows.map((row) => row.rule_json);
  },
};

async function run() {
  const decisionGate = createDecisionGate(ruleService);

  const input = {
    vertical_id: "v01_home_services",
    environment: "dev",
    payload: {
      performance_status: "scale",
      is_fake_winner: false,
    },
  };

  const result = await decisionGate.evaluate(input);

  console.log("=== Decision Result ===");
  console.log(JSON.stringify(result, null, 2));
}

run().catch((err) => {
  console.error("Runner failed:");
  console.error(err);
});
