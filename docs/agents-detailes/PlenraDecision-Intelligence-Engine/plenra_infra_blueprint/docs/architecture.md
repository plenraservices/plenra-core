# Plenra Production Architecture

## 1. System purpose

Plenra is an execution-aware decision infrastructure.

Its job is to receive structured or semi-structured decision context, apply deterministic rules and safety logic, emit an authoritative recommendation, log that recommendation as an event, and later learn only from trusted outcomes.

This architecture is designed for:

- decision quality
- explainability
- auditability
- safe learning
- replayability
- scalable extension to multiple verticals

## 2. High-level architecture

```text
Client / UI / External Trigger
        |
        v
Intake Layer
- structured form OR free-text LLM parser
        |
        v
Validation Layer
- schema validation
- enum validation
- numeric sanity checks
        |
        v
Decision Layer
- decision gate
- meta controller guardrails
        |
        v
Persistence Layer
- decision event
- input snapshot
- debug trace
        |
        v
Execution / Return Layer
- API response
- async queues
- operator review if needed
        |
        v
Post-Decision Learning Layer
- execution event
- outcome event
- ledger evaluation
- dataset builder
- counterfactual engine
- decision intelligence
- weight update engine
```

## 3. Layer responsibilities

### 3.1 Intake layer

This layer converts inbound information into a canonical contract.

Sources:
- direct API JSON
- UI form
- webhooks from other systems
- LLM-parsed natural language

Rules:
- never let free text directly touch the decision engine
- every LLM-parsed output must pass a strict schema validator
- keep original raw intake for audit

### 3.2 Validation layer

This is the first hard gate.

Responsibilities:
- enforce required fields
- reject invalid enums
- reject non-finite numeric values
- produce safe fallback responses where policy allows
- attach `validation_passed`, `validation_errors`, and `normalization_applied`

### 3.3 Decision layer

This is the core authority layer.

Components:
- `Decision Gate`
- `Meta Controller`

Decision Gate responsibilities:
- evaluate the decision request using deterministic rules
- return `pass | hold | reduce | stop | cooldown | manual_review`
- return action and reason codes
- produce traceable outputs

Meta Controller responsibilities:
- classify input integrity
- protect learning from contaminated input
- enforce no-learning-on-untrusted-input
- allow safe execution fallback while blocking unsafe learning

### 3.4 Persistence layer

Every meaningful system event must be stored as an append-only record.

Core tables:
- `decision_events`
- `dataset_records`
- `learning_dataset`

Optional future tables:
- `execution_events`
- `outcome_events`
- `audit_logs`
- `operator_reviews`
- `prompt_versions`

### 3.5 Learning layer

Learning is downstream only.
Learning never controls real-time execution directly without a separate release process.

Flow:
1. event chain is completed
2. ledger validates chain integrity
3. dataset builder classifies eligibility and trust
4. counterfactual engine computes impact deltas
5. decision intelligence groups patterns
6. weight update proposes bounded changes
7. a release process approves or rejects rule updates

## 4. Deterministic vs probabilistic boundary

This boundary is critical.

### Deterministic zone
Must stay deterministic:
- validation
- gating
- scoring
- eligibility
- event linking
- counterfactual math
- pattern grouping
- weight clamping
- state transitions

### Probabilistic zone
May use LLMs:
- intake extraction
- text explanation
- summary generation
- operator assistance
- anomaly triage suggestions

### Mandatory rule
Probabilistic outputs must become inert until validated and normalized.

## 5. Service map

### Decision Gate
Input:
- canonical decision request

Output:
- decision_status
- decision_action
- reason codes
- debug trace

### Meta Controller
Input:
- inbound envelope and validation results

Output:
- controller_status
- trust classification
- learning permission
- enforcement flags

### Dataset Builder
Input:
- event envelope + meta controller output

Output:
- storage target
- trust level
- dataset inclusion
- learning eligibility
- audit tag

### Decision Ledger
Input:
- decision / execution / outcome events

Output:
- lifecycle completeness state
- evaluation readiness

### Counterfactual Engine
Input:
- decision + actual outcome + optional baseline / counterfactual

Output:
- decision_gain
- prevented_loss
- counterfactual confidence

### Decision Intelligence
Input:
- evaluated eligible records

Output:
- decision scores
- pattern performance summaries
- weight-adjustment recommendations

### Weight Update Engine
Input:
- meta controller output + pattern recommendations + current weights

Output:
- bounded recommended weight deltas

## 6. API design

Recommended endpoints:

- `POST /v1/decision/evaluate`
- `POST /v1/intake/parse`
- `POST /v1/events/execution`
- `POST /v1/events/outcome`
- `POST /v1/learning/run-counterfactual`
- `POST /v1/learning/run-intelligence`
- `POST /v1/learning/run-weight-update`
- `GET /v1/health`
- `GET /v1/decision/{decision_id}`

## 7. Database strategy

### Principles
- append-only for core events
- immutable snapshots
- JSONB for traces and flexible envelopes
- clear separation between trusted and blocked learning paths

### Example partitions
If volume grows:
- partition by month on `created_at`
- optional partition by `vertical_id`

### Indexing targets
- `decision_id`
- `vertical_id`
- `created_at`
- `decision_status`
- GIN index on JSONB fields that matter operationally

## 8. Queue and worker design

Use async workers for:
- event persistence
- ledger evaluation
- counterfactual computation
- intelligence aggregation
- periodic reporting
- notification fanout

Worker rules:
- idempotency key required
- persist before triggering next queue
- retries only for transient failures
- poison messages moved to dead letter queue

## 9. Security model

### Identity and auth
- JWT or service-to-service signed tokens
- internal service scopes
- least privilege access

### Data protection
- no raw PII in learning datasets
- store secrets in Vault or cloud secret manager
- encrypt backups and database storage

### Operator safety
- all manual overrides logged
- delete operations gated
- high-sensitivity actions require human approval

## 10. Observability model

Every service should emit:
- request_id
- decision_id
- idempotency_key
- service_name
- version
- latency_ms
- result_status
- reason_codes

Metrics:
- decision volume
- safe fallback rate
- invalid input rate
- blocked learning rate
- counterfactual coverage
- pattern sample depth
- weight update approval rate

## 11. Release strategy

### Stage 1
- local docker
- deterministic engine tests
- contract tests

### Stage 2
- staging with synthetic data
- replay tests
- audit validation

### Stage 3
- shadow mode in production
- compare live human decisions vs Plenra decisions

### Stage 4
- limited production activation
- outcome tracking
- weekly intelligence review

## 12. What “production-ready” means here

It does not mean “many features”.
It means:
- typed contracts
- deterministic outputs
- migrations
- retries
- monitoring
- replayability
- tests
- rollback path
- versioned prompts
- versioned rules
- bounded learning updates
