import { Rule } from "../rules/rule.service";

export function evaluateRules(
  rules: Rule[],
  input: Record<string, any>
) {
  for (const rule of rules) {
    if (matchesCondition(rule.condition, input)) {
      return rule.output;
    }
  }

  return null;
}

function matchesCondition(
  condition: Record<string, any>,
  input: Record<string, any>
): boolean {
  for (const key in condition) {
    if (input[key] !== condition[key]) {
      return false;
    }
  }

  return true;
}
