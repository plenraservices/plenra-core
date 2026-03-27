# Prompt Strategy for Plenra

## Core rule

Prompts are support tools.
They are not the authority layer.

## Where prompts belong

### Good use cases
- parse free text into structured intake
- explain decision outcomes to humans
- summarize event chains for operators
- generate QA test cases

### Bad use cases
- final PASS/HOLD/STOP authority
- dataset inclusion decisions
- weight update approval
- trust-level upgrades

## Recommended intake prompt pattern

### System prompt

You are the Plenra Intake Normalizer.

Your only job is to extract structured decision input from user text.

Rules:
- return JSON only
- do not infer unavailable values
- if a value is missing, set it to null
- do not invent enums
- preserve uncertainty explicitly
- do not make decisions
- do not explain

### Required output schema

```json
{
  "current_budget": "number | null",
  "target_budget": "number | null",
  "rolling_roi_value": "number | null",
  "trend": "up | flat | down | null",
  "effective_cpc": "number | null",
  "effective_conversion_rate": "number | null",
  "portfolio_rolling_roi_value": "number | null",
  "fake_winner_count": "number | null",
  "missing_fields": ["string"],
  "ambiguity_flags": ["string"]
}
```

## Recommended explanation prompt pattern

### System prompt

You are the Plenra Decision Explainer.

You explain an already-computed decision to a human operator.

Rules:
- never change the decision
- never introduce new factors
- explain only from provided inputs and reason codes
- use concise operational language
- if data is incomplete, say so directly

## Prompt versioning rules

Store:
- prompt_id
- prompt_purpose
- version
- checksum
- owner
- created_at
- active_from
- retired_at

Never update a prompt silently.
Always version it.

## LangChain recommendation

Use LangChain as a wrapper and orchestration utility, not as your business logic container.

Recommended components:
- prompt templates
- output parsers
- retries with guardrails
- tracing
- model routing

Do not hide core policy logic inside chains.
