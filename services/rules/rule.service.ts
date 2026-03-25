export interface Rule {
  rule_id: string;
  vertical_id: string;
  priority: number;
  condition: Record<string, unknown>;
  output: {
    decision_status: string;
    decision_action: string;
    decision_reason_code: string;
    budget_delta_percent: number;
    gate_severity: string;
    requires_manual_review: boolean;
  };
}

export interface RuleService {
  getRules(verticalId: string, env: string): Promise<Rule[]>;
}

export function createRuleService(db: any): RuleService {
  return {
    async getRules(verticalId, env) {
      const result = await db.query(
        `
        SELECT rule_json
        FROM decision_rules
        WHERE vertical_id = $1
          AND environment = $2
          AND is_active = true
        ORDER BY priority DESC
        `,
        [verticalId, env]
      );

      if (!result.rows.length) {
        return [];
      }

      return result.rows.map((row: any) => row.rule_json);
    },
  };
}
