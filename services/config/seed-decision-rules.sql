INSERT INTO decision_rules (
  rule_id,
  vertical_id,
  environment,
  priority,
  is_active,
  rule_json
)
VALUES 
(
  'rule_scale_strong',
  'v01_home_services',
  'dev',
  100,
  true,
  '{
    "rule_id": "rule_scale_strong",
    "vertical_id": "v01_home_services",
    "priority": 100,
    "condition": {
      "performance_status": "scale",
      "is_fake_winner": false
    },
    "output": {
      "decision_status": "pass",
      "decision_action": "scale_up",
      "decision_reason_code": "strong_unit_economics",
      "budget_delta_percent": 20,
      "gate_severity": "low",
      "requires_manual_review": false
    }
  }'::jsonb
),
(
  'rule_fake_winner_block',
  'v01_home_services',
  'dev',
  200,
  true,
  '{
    "rule_id": "rule_fake_winner_block",
    "vertical_id": "v01_home_services",
    "priority": 200,
    "condition": {
      "is_fake_winner": true
    },
    "output": {
      "decision_status": "hold",
      "decision_action": "reduce_30",
      "decision_reason_code": "fake_winner_detected",
      "budget_delta_percent": -30,
      "gate_severity": "high",
      "requires_manual_review": false
    }
  }'::jsonb
),
(
  'rule_low_performance_stop',
  'v01_home_services',
  'dev',
  300,
  true,
  '{
    "rule_id": "rule_low_performance_stop",
    "vertical_id": "v01_home_services",
    "priority": 300,
    "condition": {
      "performance_status": "terminate"
    },
    "output": {
      "decision_status": "stop",
      "decision_action": "pause",
      "decision_reason_code": "performance_terminate_signal",
      "budget_delta_percent": -100,
      "gate_severity": "critical",
      "requires_manual_review": true
    }
  }'::jsonb
);
