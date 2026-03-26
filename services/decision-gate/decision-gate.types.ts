export type PerformanceStatus =
  | "scale"
  | "observe"
  | "iterate"
  | "cooldown"
  | "terminate";

export interface DecisionPayload {
  performance_status: PerformanceStatus;
  is_fake_winner: boolean;
  [key: string]: unknown;
}

export interface DecisionGateInput {
  vertical_id: string;
  environment: string;
  payload: DecisionPayload;
}

export interface DecisionGateFallbackOutput {
  decision_status: "hold";
  decision_reason_code: "no_rules_found" | "no_matching_rule" | "invalid_input";
}

export interface DecisionGateRuleOutput {
  decision_status: string;
  decision_action: string;
  decision_reason_code: string;
  budget_delta_percent: number;
  gate_severity: string;
  requires_manual_review: boolean;
}

export type DecisionGateOutput =
  | DecisionGateFallbackOutput
  | DecisionGateRuleOutput;
