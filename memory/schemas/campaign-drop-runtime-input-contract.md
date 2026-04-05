---
id: campaign-drop-runtime-input-contract
type: schema
status: active
related_to:
  - campaign-drop-decision-gate
  - decision-logic
  - signals-definition
---

# Campaign Drop Runtime Input Contract

## Purpose
Define the exact runtime inputs required by the Campaign Drop Decision Gate

## Required Fields

### campaign_id
- type: string
- required: true

### roas_current
- type: number
- required: true

### roas_baseline
- type: number
- required: true

### cpc_current
- type: number
- required: true

### cpc_baseline
- type: number
- required: true

### conversion_rate_current
- type: number
- required: true

### conversion_rate_baseline
- type: number
- required: true

### last_change_timestamp
- type: string
- required: true
- format: ISO-8601

### last_change_type
- type: string
- required: true
- allowed_values:
  - budget_change
  - bid_change
  - targeting_change
  - creative_change
  - placement_change
  - unknown

## Validation Rules
- All numeric fields must be finite numbers
- Baseline fields must be greater than zero
- Current fields must be greater than or equal to zero
- last_change_timestamp must be a valid ISO-8601 datetime
- last_change_type must match allowed values

## Failure Rules
- Missing required field -> fail closed
- Invalid type -> fail closed
- Invalid value -> fail closed
