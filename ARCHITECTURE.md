# CodeGuild Architecture 🏗️⚔️

This document explains **how CodeGuild is structured**.

No implementation details.
No framework lock-in.
Just clear responsibility boundaries.

We move from **simple → complex**.

---

## 1. High-Level View (Easy)

At a high level, CodeGuild has four layers:

1. Interface Layer (CLI / UI)
2. Orchestration Layer (Task + Agent control)
3. Execution Layer (Cloud or Local models)
4. Persistence Layer (Git + logs)

Each layer has **one job**.
No layer reaches across responsibilities.

---

## 2. Interface Layer (Easy)

The Interface Layer is how humans talk to CodeGuild.

Examples:

* CLI (`codeguild run`)
* Future desktop or web UI

Responsibilities:

* Accept user input
* Display plans and results
* Never execute AI logic directly

This layer is intentionally thin.

---

## 3. Orchestration Layer (Medium)

This is the **brain of CodeGuild**.

Responsibilities:

* Convert Tasks → Specs
* Assign agents
* Enforce execution order
* Pause for human approval

This layer:

* Does NOT care which AI model is used
* Does NOT edit files directly

It only coordinates.

---

## 4. Agent Layer (Medium)

Agents are isolated workers.

Each agent:

* Receives a Spec
* Performs one responsibility
* Returns structured output

Agents cannot:

* Talk to each other directly
* Modify git state
* Escalate permissions

This prevents cascade failures.

---

## 5. Execution Layer (Hard)

The Execution Layer is where **AI models live**.

CodeGuild supports multiple providers:

### Cloud Provider

* Free-tier cloud models
* Rate-limited
* No local hardware usage

### Local Provider

* Locally running AI models
* Unlimited usage
* Hardware-dependent

Both providers expose the same interface.

The rest of the system does not know the difference.

---

## 6. Provider Abstraction (Hard)

All models must implement a shared contract:

* send(prompt)
* receive(response)
* report usage / errors

This allows:

* Swapping models easily
* Community providers
* Future expansion

No provider-specific logic leaks upward.

---

## 7. Persistence Layer (Hard)

Persistence is intentionally simple.

Sources of truth:

* Git (code changes)
* Logs (agent output)
* Specs (task definitions)

No hidden databases required.

Git is the final authority.

---

## 8. Safety Boundaries (Very Hard)

Safety is architectural, not optional.

Boundaries:

* Agents operate only inside the project directory
* All writes go through controlled file operations
* Commands are allow-listed

If a task violates boundaries:

* Execution stops
* Human intervention is required

---

## 9. Failure Philosophy (Very Hard)

Failure is expected.

When failure happens:

* State is preserved
* No partial merges occur
* Errors are visible

CodeGuild prefers:

> Loud failure over silent damage.

---

## Final Architecture Principle

**Every layer should be replaceable without rewriting the system.**

If a layer becomes special or untouchable,
architecture has failed.
