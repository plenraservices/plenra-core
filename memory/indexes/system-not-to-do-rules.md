---
id: system-not-to-do-rules
type: policy
status: active
related_to:
  - decision-gate-template
  - route-policy
  - execution-gateway
  - decision-outputs
---

# System Not-To-Do Rules

## Purpose
Define prohibited execution patterns and unsafe system behaviors inside Plenra.

## Rules
- no execution without explicit decision
- no action under uncertainty
- no reaction to a single signal
- no panic-based execution
- no bypass of validation
- no routing of unresolved mixed-domain tasks
- no execution from incomplete event chain
- no learning from unvalidated data

## Constraint
System restraint is a valid and required behavior.

## Notes
These rules apply to the system itself, not to user-facing guidance.
