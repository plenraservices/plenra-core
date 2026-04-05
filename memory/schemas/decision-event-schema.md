---
id: decision-event-schema
type: schema
status: active
related_to:
  - decision-logic
  - decision-outputs
  - campaign-drop-runtime-input-contract
  - campaign-drop-decision-gate
---

# Decision Event Schema

## Purpose
Define the event structure logged whenever a Plenra decision is made

## Required Fields

### schema_version
- type: string
- required: true

### decision_id
- type: string
- required: true

### event_type
- type: string
- required: true
- allowed_values:
  - decision_event

### gate_id
- type: string
- required: true

### decision_context
- type: string
- required: true

### decision_output
- type: string
- required: true
- allowed_values:
  - PASS
  - HOLD
  - REDUCE
  - STOP
  - COOLDOWN
  - MANUAL_REVIEW

### reason_code
- type: string
- required: true

### evaluated_at
- type: string
- required: true
- format: ISO-8601

### input_snapshot
- type: object
- required: true

### signals_snapshot
- type: object
- required: true

### rule_path
- type: array
- required: true

### execution_status
- type: string
- required: true
- allowed_values:
  - pending
  - allowed
  - blocked
  - delayed
  - review_required

## Validation Rules
- decision_output must match allowed values
- event_type must equal decision_event
- evaluated_at must be valid ISO-8601
- input_snapshot must contain validated runtime inputs
- signals_snapshot must contain evaluated signals
- rule_path must contain the logic path used to reach the decision

## Failure Rules
- Missing required field -> fail closed
- Invalid output -> fail closed
- Invalid timestamp -> fail closed
- Empty rule_path -> fail closed
