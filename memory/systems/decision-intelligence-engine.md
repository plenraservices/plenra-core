---
id: decision-intelligence-engine
type: system
status: active
related_to:
  - dataset-builder
  - weight-update-engine
  - meta-controller
  - decision-event
  - outcome-event
---

# Decision Intelligence Engine

## Purpose
Transform validated decision outcomes into structured learning signals that improve future decisions.

## Core Functions
- analyze decision outcomes
- compute decision effectiveness
- generate learning signals
- prepare updates for decision weights

## Constraints
- must use only validated dataset entries
- must not mutate historical data
- must operate under meta-controller approval
- fail closed on invalid input
