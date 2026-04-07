---
id: outcome-event
type: schema
status: active
related_to:
  - decision-event
  - execution-event
  - dataset-builder
---

# Outcome Event

## Purpose
Capture the result of the executed decision.

## Fields
- outcome_id
- decision_id
- result_value
- outcome_status
- measured_at

## Rules
- must be linked to decision_id
- must be measurable
- no outcome without execution
