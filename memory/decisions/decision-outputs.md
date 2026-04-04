---
id: decision-outputs
type: decision_schema
status: active
related_to:
  - plenra-core-architecture
---

# Decision Outputs

## Allowed Outputs
- PASS
- HOLD
- REDUCE
- STOP
- COOLDOWN
- MANUAL_REVIEW

## Definitions

### PASS
Action is allowed without restriction

### HOLD
Action is paused pending further validation

### REDUCE
Action is allowed with reduced scope or intensity

### STOP
Action is blocked completely

### COOLDOWN
Action is delayed for a defined period

### MANUAL_REVIEW
Action requires human approval before execution

## Constraints
- One output per decision
- No undefined outputs allowed
- Output must be deterministic
