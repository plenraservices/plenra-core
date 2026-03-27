# Plenra Implementation Plan

## Phase 0 - Non-negotiable foundation

Before building anything complex, lock these decisions:

1. canonical schemas
2. enum registry
3. event naming
4. idempotency strategy
5. logging format
6. decision_id generation rule
7. service versioning format

### Deliverables
- Pydantic schemas
- shared enums module
- API spec
- Alembic baseline migration
- env contract

## Phase 1 - Core decision API

### Goal
Ship a reliable decision service that accepts structured input and returns deterministic decisions.

### Build
- FastAPI app
- `/v1/decision/evaluate`
- decision gate service
- meta controller service
- PostgreSQL persistence
- request/response logging
- idempotency middleware

### Done criteria
- 95%+ unit coverage on decision logic
- contract tests pass
- repeated identical request with same idempotency key is safe
- all outputs are deterministic

## Phase 2 - Event chain and auditability

### Goal
Track decisions as lifecycle events.

### Build
- decision event persistence
- execution event ingestion
- outcome event ingestion
- ledger service
- event replay endpoint

### Done criteria
- full event chain can be reconstructed by decision_id
- incomplete chains are marked but not misclassified
- replay results match original outputs

## Phase 3 - Learning-safe data pipeline

### Goal
Create a clean path from event streams to learning datasets.

### Build
- dataset builder
- trust-level classification
- blocked/eligible separation
- learning dataset materialization
- audit tags

### Done criteria
- blocked records never enter learning dataset
- invalid input never breaks the pipeline
- trust classification visible in logs and DB

## Phase 4 - Impact measurement

### Goal
Compute whether decisions actually helped.

### Build
- counterfactual engine
- actual vs baseline computation
- decision gain
- prevented loss
- confidence calculation

### Done criteria
- math is deterministic
- missing optional counterfactual returns safe fallback, not failure
- results can be re-run and match exactly

## Phase 5 - Intelligence aggregation

### Goal
Turn evaluated decisions into pattern signals.

### Build
- decision intelligence engine
- pattern grouping
- sample size handling
- recommendation generation

### Done criteria
- blocked records excluded
- invalid records excluded without killing batch
- pattern IDs and outputs deterministic

## Phase 6 - Controlled adaptation

### Goal
Support bounded improvements without letting the system self-corrupt.

### Build
- weight update engine
- max delta clamp
- human approval workflow
- release registry for rule versions

### Done criteria
- no direct self-modification in production
- all proposed changes bounded and auditable
- rollback supported

## Phase 7 - LLM intake layer

### Goal
Let users submit free text without contaminating the core.

### Build
- intake prompt
- LangChain extraction pipeline
- parser + validator
- ambiguity classifier
- manual review path

### Done criteria
- raw free text stored separately
- parsed payload validated before use
- confidence below threshold routes to review

## Phase 8 - Operator console

### Goal
Make the system operable by humans.

### Build
- search by decision_id
- event timeline view
- replay run
- blocked learning inspector
- prompt version viewer

## Recommended team split

### Backend engineer
- FastAPI
- services
- DB
- workers

### Data engineer
- event models
- analytics queries
- materialized views
- dashboards

### AI engineer
- prompt design
- intake parsing
- evals
- LangChain integration

### DevOps
- CI/CD
- observability
- secrets
- staging/prod infra

## CI/CD plan

### On every PR
- lint
- type check
- unit tests
- contract tests

### On main branch
- build image
- run migrations in staging
- run replay test suite
- deploy to staging

### Production release gate
- manual approval
- canary deployment
- health checks
- rollback on error threshold

## Risk register

### Risk 1 - Too much LLM dependence
Mitigation:
- keep LLM outside authority path

### Risk 2 - Learning corruption
Mitigation:
- strict eligibility firewall
- immutable audit paths

### Risk 3 - Silent schema drift
Mitigation:
- shared schema package
- contract tests
- prompt version pinning

### Risk 4 - Bad observability
Mitigation:
- mandatory structured logs
- decision_id everywhere

## Best build order

1. schemas and enums
2. decision gate
3. meta controller
4. persistence
5. event chain
6. dataset builder
7. counterfactual
8. intelligence
9. weight updates
10. LLM intake
11. operator console
