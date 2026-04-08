---
id: not-to-do-generation-pattern
type: strategy
status: active
related_to:
  - user-not-to-do-guidance
  - decision-logic
  - decision-outputs
---

# Not-To-Do Generation Pattern

## Purpose
Define when and how Plenra generates a contextual do-not-do list for the user.

## Trigger Conditions
- HOLD output
- STOP output
- COOLDOWN output
- high-risk decision contexts
- unstable signal environments

## Rules
- generate only context-specific items
- do not generate generic fear-based warnings
- list must be short, clear, and action-relevant
- the list must reduce risky behavior
