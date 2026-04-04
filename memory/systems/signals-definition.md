---
id: signals-definition
type: system
status: active
related_to:
  - decision-logic
  - plenra-core-architecture
---

# Signals Definition

## Purpose
Define the inputs used to evaluate decisions

## Signal Types
- performance signals
- risk signals
- validation signals
- anomaly signals

## Examples
- ROAS change
- CPC increase
- conversion drop
- anomaly detection
- missing data
- invalid input

## Rules
- Signals must be measurable
- Signals must be explicit
- No implicit signals allowed
- No decision without signals

## Constraints
- Missing critical signal → block PASS
- Conflicting signals → require HOLD or REVIEW
- Low-confidence signal → cannot produce PASS
