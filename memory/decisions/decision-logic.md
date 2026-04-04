---
id: decision-logic
type: decision_logic
status: active
related_to:
  - decision-outputs
  - plenra-core-architecture
---

# Decision Logic

## Purpose
Define how Plenra chooses a valid decision output

## Rules
- Every decision must return exactly one output
- No undefined outputs allowed
- Decision must be deterministic
- Decision must be based on validated inputs only
- No execution without a decision
- No heuristic guessing allowed

## Evaluation Order
1. Validate input
2. Detect decision context
3. Evaluate signals
4. Apply decision rules
5. Return one output
6. Log decision event

## Allowed Outcomes
- PASS
- HOLD
- REDUCE
- STOP
- COOLDOWN
- MANUAL_REVIEW

## Constraints
- First valid rule wins
- Invalid input must fail closed
- Missing required signal must prevent PASS
- Logic must be explainable
