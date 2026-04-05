---
id: naming-convention-rules
type: policy
status: active
related_to:
  - memory-system-definition
  - source-priority-rules
  - archive-policy
---

# Naming Convention Rules

## Purpose
Define consistent naming for all Plenra memory entities

## General Rules
- Use lowercase only
- Use hyphens, not spaces or underscores
- File names must reflect entity purpose clearly
- Avoid vague names like final, new, updated, test
- One entity per file

## File Naming by Type

### systems
Format:
`[domain]-[entity].md`

Examples:
- plenra-core-architecture.md
- memory-system-definition.md
- signals-definition.md

### decisions
Format:
`[decision-name].md`

Examples:
- decision-outputs.md
- decision-logic.md
- campaign-drop-gate.md

### schemas
Format:
`[entity]-schema.md`
or
`[entity]-runtime-input-contract.md`

Examples:
- decision-event-schema.md
- campaign-drop-runtime-input-contract.md

### canon
Format:
`[concept].md`

Examples:
- core-principles.md

### chat summaries
Format:
`chat-[yyyy-mm-dd]-[short-description].md`

Examples:
- chat-2026-04-05-memory-layer-setup.md

### relationships
Format:
`[map-name].yaml`

Examples:
- core-map.yaml

## ID Rules
- id should match file purpose, not necessarily file name exactly
- id must be unique across memory
- id must be stable once referenced by other entities

## Constraints
- Do not rename referenced files casually
- Do not create duplicate names for different meanings
- Do not use temporary labels in active memory
