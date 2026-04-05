---
id: chat-2026-04-05-memory-layer-setup
type: chat_summary
status: active
related_to:
  - memory-system-definition
  - plenra-core-architecture
  - decision-outputs
  - decision-logic
  - signals-definition
  - decision-gate-template
  - campaign-drop-decision-gate
  - campaign-drop-runtime-input-contract
  - decision-event-schema
  - chat-extraction-template
---

# Chat Summary - Memory Layer Setup

## Chat Metadata
- chat_id: chat-2026-04-05-memory-layer-setup
- chat_title: Plenra Memory Layer Setup
- source: current_chat
- date: 2026-04-05
- status: extracted

## Context
This chat established the first structured memory layer for Plenra inside GitHub and prepared the system for future use inside Cursor.

## Key Decisions
- Memory must live at repo root under `/memory`
- Raw chats should not be copied directly into memory as a first step
- Chat knowledge must enter through summaries and extracted entities
- Markdown with YAML metadata is the default storage format
- Decision logic, outputs, signals, schemas, and gates must become separate entities

## Created Entities
- system: memory-system-definition
- system: plenra-core-architecture
- canon: plenra-core-principles
- relationship map: core-map
- decision schema: decision-outputs
- decision logic: decision-logic
- system: signals-definition
- decision gate: decision-gate-template
- decision gate: campaign-drop-decision-gate
- schema: campaign-drop-runtime-input-contract
- schema: decision-event-schema
- template: chat-extraction-template

## Locked Rules
- No raw chat storage as primary memory
- Every memory file must include YAML metadata
- Memory must not sit under docs
- Memory entities must be separated by type
- Decision systems must remain deterministic and fail-closed

## Rejected Paths
- Storing memory under `/docs`
- Dumping raw chats directly into GitHub as the main memory layer
- Mixing architecture docs with operational memory entities
- Using chat text as source of truth without extraction

## Open Items
- Expand relationships across all current memory entities
- Extract additional Plenra chats into structured summaries
- Convert more existing docs into standalone memory entities
- Define source priority and archive policy more explicitly

## Related Files
- memory/systems/memory-system-definition.md
- memory/systems/plenra-core-architecture.md
- memory/canon/core-principles.md
- memory/relationships/core-map.yaml
- memory/decisions/decision-outputs.md
- memory/decisions/decision-logic.md
- memory/systems/signals-definition.md
- memory/decisions/decision-gate-template.md
- memory/decisions/campaign-drop-gate.md
- memory/schemas/campaign-drop-runtime-input-contract.md
- memory/schemas/decision-event-schema.md
- memory/chat-summaries/chat-extraction-template.md

## Extraction Notes
This chat should be treated as the foundation chat for the Plenra Memory Layer.
