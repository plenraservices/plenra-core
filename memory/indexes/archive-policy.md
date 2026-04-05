---
id: archive-policy
type: policy
status: active
related_to:
  - source-priority-rules
  - memory-system-definition
---

# Archive Policy

## Purpose
Define when a Plenra memory file remains active, becomes deprecated, or moves to archive

## Status Types
- draft
- active
- locked
- deprecated
- archived

## Rules

### draft
Used for incomplete entities that are not yet trusted for execution-facing use

### active
Used for current working entities that may evolve

### locked
Used for stable entities that should not change without explicit review

### deprecated
Used for entities that are no longer current but still useful as reference

### archived
Used for historical entities that must not be used as active source material

## Archive Triggers
- Entity replaced by a newer active or locked version
- Entity no longer reflects current system logic
- Entity preserved only for historical traceability
- Raw material no longer suitable as source of truth

## Constraints
- Archived files must never override active files
- Deprecated files must not be used for execution-facing logic
- Locked files require explicit review before change
- Raw chat dumps belong in archive only, not active memory

## Handling Rules
- Do not delete historically important files
- Prefer deprecated before archived when reference value still exists
- Mark status explicitly before moving files
- Preserve file relationships when archiving if they matter historically
