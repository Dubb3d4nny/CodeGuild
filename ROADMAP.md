# CodeGuild Roadmap 🗺️⚔️

This roadmap defines **what CodeGuild will build, and in what order**.

The goal is sustainability, clarity, and steady progress — not feature bloat.

---

## Guiding Rules

* Ship small, usable milestones
* No paid APIs required to start
* No breaking changes without discussion
* Learning and transparency over speed

---

## v0.1 — Guild Formation (Foundation)

**Goal:** A minimal, usable CodeGuild that proves the core idea.

### Scope

* CLI-only interface
* Single-task execution
* Cloud mode only (free-tier model)
* Human-in-the-loop approval

### Features

* Initialize CodeGuild inside a git repo
* Create a Task → Spec
* Planner Agent (basic)
* Builder Agent (basic)
* Dry-run mode (no file writes)
* Structured output (logs)

### Non-Goals

* No UI
* No parallel agents
* No local models
* No auto-merge

---

## v0.2 — Dual Mode (Stability)

**Goal:** Introduce the hybrid philosophy safely.

### Scope

* Cloud + Local execution modes
* Provider abstraction
* Safer file operations

### Features

* Local model support (Ollama / LocalAI)
* Provider switching via config
* Validator Agent
* Controlled file write permissions
* Git branch creation

### Non-Goals

* No background daemon
* No automatic merges
* No cloud hosting by maintainers

---

## v0.3 — Community Ready (Growth)

**Goal:** Enable collaboration and contributions.

### Scope

* Extensibility
* Contributor experience

### Features

* Plugin system for agents
* Community provider support
* Task templates
* Improved error reporting
* Example projects

### Non-Goals

* No enterprise features
* No hosted SaaS

---

## v0.4 — Quality & Safety (Future)

**Goal:** Increase reliability without complexity.

### Possible Features

* Parallel agents (opt-in)
* Better validation workflows
* Security hardening
* Optional UI

*This version is intentionally undefined.*

---

## Long-Term Ideas (Not Promises)

* Educational mode
* Visual task planning
* Agent replay and explanation
* Community-curated workflows

---

## Final Roadmap Principle

**If a feature increases cost, complexity, or dependency, it must justify itself clearly.**

CodeGuild grows by trust, not hype.
