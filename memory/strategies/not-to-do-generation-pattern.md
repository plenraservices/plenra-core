---
id: not-to-do-generation-pattern
type: strategy
status: active
related_to:
  - user-not-to-do-guidance
  - decision-logic
  - decision-outputs
  - system-not-to-do-rules
---

# Not-To-Do Generation Pattern

## Purpose
Define when and how Plenra generates a contextual not-to-do list for both the system and the user.

## Trigger Conditions
- HOLD output
- STOP output
- COOLDOWN output
- elevated risk
- unstable signal environment
- conflicting signals
- incomplete confidence

## Generation Rules
- generate only context-specific items
- do not generate generic warnings
- keep the list short and action-relevant
- separate system not-to-do items from user not-to-do items
- use actual decision context, not abstract policy language

## Output Structure

### System Layer
Internal prohibited actions for the system itself.

### User Layer
Risky actions the user should avoid.

## Constraints
- do-not-do generation is part of decision output design
- not an optional explanation layer
- must be deterministic and context-bound
