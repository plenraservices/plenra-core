---
id: relationship-update-rules
type: policy
status: active
related_to:
  - core-map
  - memory-qa-checklist
  - naming-convention-rules
---

# Relationship Update Rules

## Purpose
Define when and how memory relationships must be updated so the system remains a usable graph instead of disconnected files.

## Rules

### When to Update core-map
Update relationships when:
- a new system is added
- a new agent is added
- a new schema constrains or validates another entity
- a new decision gate depends on existing logic, outputs, or signals
- a chat summary documents newly created entities
- ownership or dependency changes

### Minimum Relationship Types
Use only explicit relationship meanings such as:
- depends_on
- connects_to
- constrains
- emits
- validates
- documents
- supports
- feeds
- replaces
- used_by

### Relationship Discipline
- do not add guessed relationships
- do not add decorative relationships
- add only meaningful structural links
- use exact entity ids or stable entity names
- do not leave major entities orphaned

### Conflict Handling
If a relationship is unclear:
- do not invent it
- mark as unresolved
- resolve before relying on it in execution-facing work

### Required Standard
A new core entity is not considered integrated until:
- its file exists
- its purpose is explicit
- its key relationships are added to core-map

## QA Rule
Before commit:
- verify all newly added core entities are linked
- verify no broken references were introduced
- verify no outdated entity is still presented as active dependency
