Plenra MVP Build Lock

Purpose

This document defines the exact boundaries of the MVP.

Anything not listed here is NOT allowed to be built.

---

Locked Vertical

Ad budget scaling decision only.

---

Required Input

- current_budget
- target_budget
- rolling_roi_value
- effective_cpc
- effective_conversion_rate
- trend
- portfolio_rolling_roi_value

---

Allowed Output

- PASS
- HOLD
- STOP

---

Required System Behavior

- Validate input
- Run deterministic decision logic
- Return structured response
- Persist decision event
- Enforce free usage limit
- Return paywall when needed

---

Required Surfaces

1. Hosted UI
2. External embed widget

---

Required Persistence

Each decision must store:

- decision_id
- input_snapshot
- output
- timestamp
- source (web / embed)
- user_id (if exists)

---

Free Limit Rule

- Max free decisions: 3
- After limit: return paywall flag

---

LLM Constraints

Allowed:

- intake parsing
- explanation generation

Forbidden:

- decision logic
- risk evaluation
- output authority

---

Fail Conditions

System must BLOCK or HOLD when:

- ROI too low
- trend negative
- scaling too aggressive
- input invalid

---

Non-Negotiable Rules

- deterministic logic only
- no probabilistic decisions
- no silent fallbacks
- no hidden logic
- all outputs explainable

---

Out of Scope

- learning engines
- optimization loops
- dynamic weights
- multi-agent orchestration
- analytics dashboards (beyond logs)

---

Definition of DONE

System is complete when:

- API returns valid decision
- UI displays decision
- decision is logged
- free limit enforced
- paywall triggered
- embed opens gate
