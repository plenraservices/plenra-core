---
id: dataset-builder
type: system
status: active
related_to:
  - decision-event
  - execution-event
  - outcome-event
---

# Dataset Builder

## Purpose
Control which events are eligible for learning.

## Core Functions
- validate event chain completeness
- filter invalid or low-trust data
- assign learning eligibility

## Rules
- no incomplete chain enters dataset
- no low-trust data enters learning
- fail closed on missing linkage
