Plenra Freelancer Execution Order

Objective

Build a working Decision Gate system using Plenra architecture and tools.

You are NOT designing the system.
You are executing a predefined build.

---

Tools You MUST Use

- Cursor (code generation and refactoring)
- GitHub (source of truth)
- Plenra prompts (for structured generation only)

You are NOT allowed to:

- invent new architecture
- change logic
- add features outside scope

---

Step 1 - Environment Setup

- clone repository
- install dependencies
- configure .env

---

Step 2 - Decision Engine (CORE)

Use Cursor to generate:

- services/decision-engine/engine.py

Requirements:

- deterministic logic only
- no AI usage
- returns PASS / HOLD / STOP

---

Step 3 - API Layer

Use Cursor:

- build POST /decision/evaluate

Must:

- validate input
- call decision engine
- return structured response

---

Step 4 - Database

- setup PostgreSQL
- create tables:
  - users
  - decisions

---

Step 5 - Event Logging

Every decision must be stored.

Use:

- JSON snapshot
- timestamp
- decision_id

---

Step 6 - Free Limit Enforcement

Implement:

- max 3 free decisions
- return paywall flag after limit

---

Step 7 - Web UI

Use Cursor to build:

- simple page
- input form OR textarea
- submit button
- response display

No design work required.

---

Step 8 - Embed Widget

Create:

apps/embed/embed.js

Behavior:

- display button
- open Plenra gate
- pass source parameter

---

Step 9 - Testing

Use Cursor:

- test decision logic
- test API response
- test limit enforcement

---

Step 10 - Deployment

- backend → Render / Railway
- frontend → Vercel

---

DO NOT DO

- do not add AI to decision logic
- do not expand scope
- do not build extra features
- do not modify architecture

---

SUCCESS CRITERIA

- API works
- UI works
- decision returned
- events stored
- free limit enforced
- paywall triggered
- embed works

---

Important Rule

If something is unclear:
STOP and ask.

Do NOT guess.
