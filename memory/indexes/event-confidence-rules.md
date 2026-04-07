---
id: event-confidence-rules
type: policy
status: active
related_to:
  - dataset-builder
  - outcome-event
  - decision-event
---

# Event Confidence Rules

## Purpose
Define the confidence level of event chains before entering learning.

## Confidence Levels

### High
- full chain exists
- valid timing
- clear attribution

### Medium
- full chain exists
- minor uncertainty

### Low
- partial uncertainty
- noisy attribution

### Invalid
- missing chain
- invalid order
- missing linkage

## Rules
- only High and Medium enter learning
- Low is logged only
- Invalid is rejected

## Constraints
- fail closed on undefined confidence
- no learning from invalid chains
