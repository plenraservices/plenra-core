---
id: meta-controller
type: system
status: active
related_to:
  - decision-intelligence-engine
  - weight-update-engine
---

# Meta Controller

## Purpose
Control and approve learning updates to prevent unsafe or incorrect system changes.

## Core Functions
- approve or block weight updates
- detect unsafe learning patterns
- enforce learning rules

## Constraints
- no update allowed without explicit approval
- block updates from low-confidence data
- fail closed on uncertainty
