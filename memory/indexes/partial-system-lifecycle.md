---
id: partial-system-lifecycle
type: policy
status: active
related_to:
  - memory-qa-checklist
  - source-priority-rules
  - archive-policy
---

# Partial System Lifecycle

## Purpose
Define how partially complete systems are managed safely inside Plenra memory and future Cursor work.

## Definition
A system is PARTIAL when:
- core structure exists
- major logic is known
- one or more critical components are missing
- production use would be unsafe or incomplete

## Rules
- PARTIAL systems must not be treated as production-ready
- PARTIAL systems must not be used as execution-facing truth without closure
- every PARTIAL system must have a closure plan
- closure plan must define blockers, missing components, and readiness criteria

## Lifecycle

### 1. Extract
Create the system entity in memory

### 2. Score
Assess:
- determinism
- completeness
- production readiness
- safety

### 3. Mark
If not ready, mark as PARTIAL in system readiness context

### 4. Create Closure Plan
Create:
- missing components
- blockers
- required modules
- next implementation step
- readiness criteria

### 5. Build in Cursor
Close gaps through structured implementation work

### 6. QA
Validate:
- logic completeness
- explicit constraints
- relationship correctness
- execution safety

### 7. Re-score
Reassess readiness:
- READY
- PARTIAL
- BLOCKED

## Constraints
- no silent promotion from PARTIAL to READY
- no execution-facing use without explicit closure
- no skipped closure plan for core systems
