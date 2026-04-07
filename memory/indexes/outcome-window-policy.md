---
id: outcome-window-policy
type: policy
status: active
related_to:
  - outcome-event
  - decision-event
  - dataset-builder
---

# Outcome Window Policy

## Purpose
Define when outcomes are measured, valid, and eligible for learning.

## Supported Windows
- instant
- 24h
- 72h
- 7d
- 30d

## Rules

### Window Assignment
Each decision type must define a valid outcome window.

### Valid Outcome
- outcome must be recorded within defined window
- outcome outside window is marked as stale

### Missing Outcome
- if no outcome within window → chain marked incomplete
- incomplete chain is not eligible for learning

### Late Outcome
- late outcome may be logged
- but excluded from learning

### Constraints
- fail closed if window is undefined
- no learning without valid outcome window
