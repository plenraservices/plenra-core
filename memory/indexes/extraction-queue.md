---
id: extraction-queue
type: index
status: active
related_to:
  - chat-extraction-template
  - memory-system-definition
---

# Extraction Queue

## Purpose
Define which chats should be extracted into structured memory and in what order

## Rules
- Extract only high-impact chats
- Do not extract duplicate or low-signal chats
- Each extracted chat must produce entities or decisions
- No raw chat dumping into memory

## Priority Levels

### P0 - Foundation (Critical)
- Memory system creation
- Core architecture
- Core principles
- Decision system definitions

### P1 - Core Systems
- Decision gates
- Runtime contracts
- Schemas
- Signals systems

### P2 - Expansion
- Agents
- Strategies
- Distribution systems

### P3 - Optional
- Experiments
- Iterations
- Low-impact discussions

## Current Queue

### P0
- [x] chat-2026-04-05-memory-layer-setup

### P1
- [ ] campaign-drop-decision-chat
- [ ] decision-intelligence-agent-chat

### P2
- [ ] distribution-engine-chat
- [ ] affiliate-system-chat

### P3
- [ ] experimental-ideas-chat

## Extraction Workflow
1. Select next chat from queue
2. Create summary using template
3. Identify entities
4. Create missing entities in memory
5. Update relationships
6. Link chat summary to entities
