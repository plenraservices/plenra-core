---
id: campaign-drop-decision-gate
type: decision_gate
status: active
related_to:
  - decision-logic
  - decision-outputs
  - signals-definition
  - plenra-core-architecture
---

# Campaign Drop Decision Gate

## Purpose
Evaluate sudden drops in campaign performance before allowing action

## Required Signals
- roas_current
- roas_baseline
- cpc_current
- cpc_baseline
- conversion_rate_current
- conversion_rate_baseline
- last_change_timestamp
- last_change_type

## Thresholds

### ROAS Drop
- significant_drop: ≥ 20%
- severe_drop: ≥ 40%

### CPC Increase
- moderate_increase: ≥ 25%
- extreme_increase: ≥ 50%

### Conversion Instability
- unstable: variance ≥ 30%

### Recent Change
- recent: within last 24 hours

## Decision Rules

### STOP
- severe ROAS drop AND extreme CPC increase
- OR severe ROAS drop AND unstable conversion

### HOLD
- significant ROAS drop
- OR moderate CPC increase
- OR unstable conversion
- OR recent change detected

### REDUCE
- moderate drop with stable conversion

### PASS
- no significant anomalies detected

## Constraints
- Missing required signal → HOLD
- Conflicting signals → HOLD
- No heuristic decisions allowed

## Output
One of:
PASS | HOLD | REDUCE | STOP | COOLDOWN | MANUAL_REVIEW
