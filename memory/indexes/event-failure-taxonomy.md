---
id: event-failure-taxonomy
type: policy
status: active
related_to:
  - dataset-builder
  - decision-ledger
  - outcome-event
---

# Event Failure Taxonomy

## Purpose
Define standardized failure types across the event lifecycle.

## Failure Types

- missing_execution
- missing_outcome
- stale_outcome
- duplicate_event
- broken_linkage
- invalid_order
- low_confidence_chain

## Rules
- every failure must be classified
- no silent failure allowed
- failures must be logged

## Constraints
- fail closed on unknown failure type
- invalid chains are blocked from learning
