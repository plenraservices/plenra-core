import { RuleService } from "../rules/rule.service";
import { evaluateRules } from "./rule-engine";

export interface DecisionGateInput {
  vertical_id: string;
  environment: string;
  payload: Record<string, any>;
}

export function createDecisionGate(ruleService: RuleService) {
  return {
    async evaluate(input: DecisionGateInput) {
      const rules = await ruleService.getRules(
        input.vertical_id,
        input.environment
      );

      if (!rules.length) {
        return {
          decision_status: "hold",
          decision_reason_code: "no_rules_found",
        };
      }

      const result = evaluateRules(rules, input.payload);

      if (!result) {
        return {
          decision_status: "hold",
          decision_reason_code: "no_matching_rule",
        };
      }

      return result;
    },
  };
}
