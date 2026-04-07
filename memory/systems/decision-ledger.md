---
id: decision-ledger
type: system
status: active
related_to:
  - decision-event
  - execution-event
  - outcome-event
---

# Decision Ledger

## Purpose
Maintain the full lifecycle of each decision.

## Structure
decision_event → execution_event → outcome_event

## Rules
- must preserve event order
- must link all events via decision_id
- fail closed on missing step
