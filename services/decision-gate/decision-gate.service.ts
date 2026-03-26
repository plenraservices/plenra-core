
import type { RuleService } from "../rules/rule.service";
import { evaluateRules } from "./rule-engine";
import type {
  DecisionGateInput,
  DecisionGateOutput,
} from "./decision-gate.types";
import {
  validateDecisionGateInput,
  buildInvalidInputFallback,
  buildFallback,
} from "./decision-gate.validator";

export function createDecisionGate(ruleService: RuleService) {
  return {
    async evaluate(input: unknown): Promise<DecisionGateOutput> {
      if (!validateDecisionGateInput(input)) {
        return buildInvalidInputFallback();
      }

      const safeInput = input as DecisionGateInput;

      const rules = await ruleService.getRules(
        safeInput.vertical_id,
        safeInput.environment
      );

      if (!rules.length) {
        return buildFallback("no_rules_found");
      }

      const result = evaluateRules(rules, safeInput.payload);

      if (!result) {
        return buildFallback("no_matching_rule");
      }

      return result;
    },
  };
}
