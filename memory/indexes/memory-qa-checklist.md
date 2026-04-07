---
id: memory-qa-checklist
type: policy
status: active
related_to:
  - memory-system-definition
  - source-priority-rules
  - archive-policy
  - naming-convention-rules
---

# Memory QA Checklist

## Purpose
Define the minimum quality checks required before new memory entities are accepted as valid system assets.

## Required Checks

### Structure
- file is placed in the correct memory folder
- file name follows naming convention
- one entity per file
- file has valid YAML header
- YAML includes id, type, and status

### Content
- entity purpose is explicit
- constraints are explicit if relevant
- no vague placeholders remain
- no raw chat dump is stored as active memory
- no mixed domains are merged into one file unless explicitly intended

### Relationships
- entity is linked in core-map if relationship relevance exists
- dependencies are explicit
- related entities are named correctly
- no orphan entity is created without system context

### Priority and Truth
- file does not conflict with higher-priority source
- if conflict exists, it is resolved explicitly before acceptance
- deprecated or archived material is not used as active source of truth

### Execution Safety
- partial systems have closure plan
- blocked or unresolved logic is not treated as runtime-ready
- no execution-facing file is accepted with missing required logic

## Acceptance Rule
A memory file is accepted only if:
- structure is valid
- content is explicit
- relationships are not broken
- no unresolved truth conflict remains

## Rejection Rule
Reject or revise if:
- YAML is missing
- file placement is wrong
- entity duplicates existing meaning
- entity conflicts with canon or source priority
- file creates ambiguity in active memory
