# CodeGuild Core Concepts 🧠⚔️

This document explains CodeGuild’s ideas **before code**. If you understand this file, you understand the system.

We move from **easy → harder concepts**.

---

## 1. Tasks (Easy)

A **Task** is a single goal you give CodeGuild.

Examples:

* Add authentication to my bot
* Refactor this file for clarity
* Fix failing tests
* Generate documentation

A task should:

* Describe *what* you want
* Not describe *how* to code it

CodeGuild handles the how.

---

## 2. Specs (Easy)

A **Spec** is a structured version of a task.

It contains:

* The goal
* Relevant files
* Constraints
* Success criteria

Think of a Spec as a **quest scroll** 📜.

Tasks become Specs.
Specs guide agents.

---

## 3. Agents (Medium)

Agents are AI workers with **clear roles**.

They do not think freely.
They follow responsibilities.

### Core Agents

* **Planner Agent**

  * Breaks a spec into steps
  * Identifies risks

* **Builder Agent**

  * Writes or edits code
  * Follows the plan strictly

* **Validator Agent**

  * Runs tests
  * Checks formatting and logic

Agents never merge code on their own.

---

## 4. Human-in-the-Loop (Medium)

CodeGuild is **not fully automatic**.

Humans:

* Approve plans
* Review changes
* Decide what gets merged

AI proposes.
Humans dispose.

This prevents:

* Silent breaking changes
* Unexplainable behavior

---

## 5. Modes (Medium)

CodeGuild supports two execution modes.

### Cloud Mode (Default)

* Uses free-tier cloud models
* Minimal setup
* Rate limited
* Best for beginners

### Local Mode (Advanced)

* Uses local AI models
* Unlimited usage
* Higher hardware cost
* Optional

Both modes behave the same logically.
Only execution differs.

---

## 6. Safety Boundaries (Hard)

Agents operate inside strict boundaries:

* Project directory only
* Read/write rules
* No system-level access

Agents cannot:

* Install random software
* Access secrets without permission
* Modify unrelated files

Safety > speed.

---

## 7. Git as the Source of Truth (Hard)

Every change:

* Happens on a branch
* Is committed
* Is reviewable

No direct edits to main.
No hidden changes.

Git is the **ledger of the guild**.

---

## 8. Extensibility (Very Hard)

CodeGuild is designed to grow.

Future additions:

* New agent types
* New model providers
* Custom workflows

Core rule:

> Extensions should not break defaults.

---

## Final Rule

If a feature:

* Hides learning
* Forces payment
* Removes control

It does not belong in CodeGuild.
