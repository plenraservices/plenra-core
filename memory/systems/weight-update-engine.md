---
id: weight-update-engine
type: system
status: active
related_to:
  - decision-intelligence-engine
  - meta-controller
---

# Weight Update Engine

## Purpose
Apply controlled updates to decision parameters based on learning signals.

## Core Functions
- compute weight adjustments
- enforce update bounds
- normalize values
- prevent instability

## Constraints
- no update without approval
- max change per cycle must be limited
- no overwrite of historical values
- fail closed on invalid update
