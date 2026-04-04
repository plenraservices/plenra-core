---
id: plenra-core-architecture
type: system
status: active
source: docs/plenra-HLD.md
---

# Plenra Core Architecture

## Identity
Plenra is a Decision Authorization Infrastructure

## System Type
- Deterministic
- Fail-Closed
- Signal-Based

## Core Function
System that decides whether an action is allowed to happen

## Outputs
- PASS
- HOLD
- REDUCE
- STOP
- COOLDOWN
- MANUAL_REVIEW

## Core Layers
- Decision Layer
- Validation Layer
- Execution Layer
- Memory Layer

## Flow
Input → Validation → Decision → Execution → Outcome → Memory Update

## Constraints
- Fail-closed always
- No execution without decision
- No heuristics
