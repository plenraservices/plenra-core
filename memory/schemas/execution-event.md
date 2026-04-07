---
id: execution-event
type: schema
status: active
related_to:
  - decision-event
  - outcome-event
---

# Execution Event

## Purpose
Capture what actually happened after a decision was made.

## Fields
- execution_id
- decision_id
- action_taken
- execution_status
- executed_at

## Rules
- must reference decision_id
- must reflect real action
- fail closed on mismatch
