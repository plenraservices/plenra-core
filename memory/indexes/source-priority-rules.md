---
id: source-priority-rules
type: policy
status: active
related_to:
  - memory-system-definition
  - plenra-core-principles
  - core-map
---

# Source Priority Rules

## Purpose
Define which source wins when multiple Plenra files conflict

## Priority Order
1. Locked canon
2. Active system definitions in memory
3. Active schemas in memory
4. Active decision logic and decision outputs
5. Active decision gates
6. Active relationship maps
7. Active chat summaries
8. Legacy docs under /docs
9. Archived files

## Rules
- Higher priority source overrides lower priority source
- Locked canon cannot be overridden by summaries or legacy docs
- Docs are reference material, not final source of truth
- Archived files must never override active files
- If two active files conflict at the same priority level, resolve explicitly and do not guess

## Resolution Policy
- Detect conflict
- Identify higher priority source
- Mark lower priority source as reference only or update it
- If unresolved, block execution-facing use until clarified

## Constraints
- No silent conflict resolution
- No guessing across conflicting sources
- No execution based on deprecated or archived material
