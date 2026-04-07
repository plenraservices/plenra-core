---
id: learning-eligibility-rules
type: policy
status: active
related_to:
  - dataset-builder
  - decision-intelligence-engine
---

# Learning Eligibility Rules

## Purpose
Define which data is allowed to enter the learning system.

## Rules
- only complete event chains are eligible
- must include decision, execution, and outcome
- must meet minimum data quality threshold
- must not include corrupted or partial records
- low-confidence data is excluded

## Constraints
- fail closed on missing linkage
- no raw events allowed without validation
