# Plenra Infrastructure Blueprint

## What this package is

This package is a production-oriented blueprint for rebuilding the core Plenra decision infrastructure in your own environment using Python.

It translates the logic discussed in this chat into:

- a clear system architecture
- a phased implementation plan
- production guardrails
- agent and engine prompts
- Python service scaffolds for the core deterministic engines
- API and orchestration skeletons
- testing and deployment foundations

This package is not a toy demo.
It is a serious starting point for a controlled, auditable, fail-closed decision system.

## Strategic truth

The right architecture for Plenra is **not** “LLM everywhere”.
That would weaken trust, increase variance, and make debugging harder.

The right architecture is:

- deterministic core for rules, scoring, state, safety, and auditability
- LLM layer only where ambiguity actually exists
- hard separation between decision authority and language generation
- strict contracts between engines
- full observability and replayability

In practice:

- **Python** runs services, orchestration, APIs, validation, persistence, and async workers.
- **LangChain** is optional and should be limited to intake normalization, extraction, summarization, and operator tooling.
- **Pydantic** defines contracts.
- **FastAPI** exposes internal and external APIs.
- **PostgreSQL** stores immutable event streams and learning datasets.
- **Redis** supports queues, idempotency, locks, and short-lived state.
- **Celery/RQ/Dramatiq** runs async jobs.
- **OpenTelemetry + structured logs** provide auditability.

## Core design principle

Plenra is a **Decision Intelligence System**, not a generic chatbot.

That means the system must:

- fail closed on unsafe execution paths
- never learn from blocked or untrusted data
- treat every decision as an auditable event
- separate execution from learning
- separate deterministic logic from probabilistic AI

## Recommended production stack

### Application layer
- Python 3.12+
- FastAPI
- Pydantic v2
- Uvicorn / Gunicorn
- SQLAlchemy 2.x
- Alembic

### Async and orchestration
- Redis
- Celery or Dramatiq
- APScheduler for internal periodic jobs if needed

### Data layer
- PostgreSQL
- JSONB for snapshots, traces, and model outputs
- optional S3-compatible object storage for large artifacts

### LLM and agent layer
- LangChain for intake pipelines and optional operator tools
- direct provider SDKs for production-critical LLM calls
- prompt versioning stored in code and database

### Observability
- OpenTelemetry
- Prometheus
- Grafana
- Sentry
- structured JSON logging

### Security
- Vault or cloud secrets manager
- signed internal service requests
- RBAC for operator tools
- PII minimization

## Project structure

```text
plenra_infra_blueprint/
├─ README.md
├─ pyproject.toml
├─ .env.example
├─ Dockerfile
├─ docker-compose.yml
├─ docs/
│  ├─ architecture.md
│  ├─ implementation_plan.md
│  └─ prompts.md
├─ app/
│  ├─ main.py
│  ├─ config.py
│  ├─ logging_config.py
│  ├─ db.py
│  ├─ schemas.py
│  ├─ models.py
│  ├─ prompts/
│  │  └─ intake_budget_increase.txt
│  ├─ api/
│  │  └─ routes.py
│  ├─ core/
│  │  ├─ enums.py
│  │  ├─ utils.py
│  │  └─ idempotency.py
│  └─ services/
│     ├─ decision_gate.py
│     ├─ meta_controller.py
│     ├─ dataset_builder.py
│     ├─ decision_ledger.py
│     ├─ counterfactual_engine.py
│     ├─ decision_intelligence.py
│     ├─ weight_update.py
│     └─ orchestrator.py
├─ scripts/
│  └─ seed_demo_data.py
└─ tests/
   ├─ test_decision_gate.py
   └─ test_decision_intelligence.py
```

## What to build first

Do not start with the full multi-agent dream.
Start with the smallest credible production slice.

### Phase 1
Build the deterministic decision path only:

1. intake contract
2. decision gate
3. meta controller
4. ledger event logging
5. API endpoint
6. database persistence
7. test coverage

### Phase 2
Add the learning-safe layer:

1. dataset builder
2. counterfactual engine
3. decision intelligence engine
4. weight update engine
5. dashboards and audits

### Phase 3
Add LLM-assisted intake and operator workflows:

1. free-text intake parser
2. ambiguity detection
3. human review tools
4. prompt registry
5. replay + QA tooling

## What LangChain should and should not do

### Use LangChain for
- intake extraction from messy text
- classification of free-form operator notes
- explanation generation for humans
- document Q&A for internal teams
- evaluation workflows around prompts

### Do not use LangChain for
- final decision authority
- safety gates
- learning eligibility
- event deduplication
- weight changes
- canonical state transitions

## Production rules that must stay locked

1. Deterministic engines remain deterministic.
2. LLM outputs are never trusted without validation.
3. All externally-triggered actions get idempotency keys.
4. Every decision gets a decision_id.
5. Every event is append-only.
6. Blocked data never reaches learning.
7. Safe fallback is allowed on input.
8. Fail-closed is mandatory on execution and learning.

## Files included

- `docs/architecture.md` - deep architecture and boundaries
- `docs/implementation_plan.md` - phased production plan
- `docs/prompts.md` - recommended prompt strategy and examples
- `app/services/*.py` - Python scaffolds for core engines
- `app/main.py` - FastAPI entrypoint
- `app/api/routes.py` - core API routes
- `app/schemas.py` - typed request/response contracts
- `tests/` - starter tests

## Recommended next move

Build this in three parallel tracks:

- **Track A**: deterministic backend engines
- **Track B**: data and observability
- **Track C**: LLM intake and operator UX

Do not merge Track C into core decision logic.
That separation is what will keep Plenra trustworthy.
