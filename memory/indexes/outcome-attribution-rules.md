---
id: outcome-attribution-rules
type: policy
status: active
related_to:
  - outcome-event
  - execution-event
  - decision-event
---

# Outcome Attribution Rules

## Purpose
Define how outcomes are linked to decisions and executions.

## Attribution Types

### Direct Attribution
- outcome clearly results from the executed action
- no intermediate conflicting actions

### Conditional Attribution
- outcome likely influenced by execution
- but external factors exist

### Weak Attribution
- outcome linked but confidence is low

## Rules
- only direct or high-confidence conditional attribution enters learning
- weak attribution is logged but excluded from learning
- conflicting executions invalidate attribution

## Constraints
- fail closed if attribution is unclear
- no learning from ambiguous causality
