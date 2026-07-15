---
title: "Agentic autonomy levels: agency × orchestration and calibrated autonomy"
type: "Concept"
theme: governance-alignment-ops
level: 🔴
source_url: https://addyosmani.com/blog/agentic-autonomy-levels/
source_title: "Agentic Autonomy Levels — Addy Osmani"
objectives: [code-generation, production]
---

# Agentic autonomy levels: agency × orchestration and calibrated autonomy

**In one sentence** — Autonomy in agentic engineering should be split into two axes — *agency* (how far a single agent goes) and *orchestration* (how many agents run and who coordinates them) — and the level you grant should follow the **available verification**, not the task, because verification is the bottleneck.

## What the source says
Addy Osmani argues the usual single-axis "autonomy ladder" (Steve Yegge's) conflates two questions. He separates **agency** — low (suggest & wait) → mid (scoped, reports back with evidence, you keep steering) → high (works toward a goal: experiments, gets blocked, asks, returns evidence) — from **orchestration** — low (one agent, one thread) → mid (several agents in isolated worktrees) → high (an orchestrator turning a backlog/queue into continuous work; *"management by exception"*). Pragmatically he collapses them into **six levels across three eras**:
- *Assisted* — **L0 Assist** (suggestions; you decide; local verification); **L1 Supervised action** (acts but asks before anything consequential; failure mode = *approval fatigue*; Codex Auto-review delegates the final approval to a reviewer agent).
- *Agent-led* — **L2 Scoped task delegation** (bounded task with a "done" definition; verification shifts from you to **evidence**: passing tests, types, screenshots, repro steps); **L3 Goal-driven autonomy** (plan→act→test→review until a **measurable, automatable** stopping condition; demands specific goals, not "improve UX in general").
- *Orchestration* — **L4 Parallel delegation** (parallel agents on isolated slices; bottleneck = **decomposition**; failure = *false parallelism* → merge conflicts; per-agent **token cost** scales with concurrency, plus a human *orchestration tax*); **L5 Managed-by-exception orchestration** (a **manager agent** wakes on triggers, dispatches workers, verifies continuously, retries, escalates, aggregates; a "factory" whose input is the backlog; cites OpenAI's **Symphony** spec with a Linear board; needs **independent verification** — separate implementers, reviewers, test runners, security).

Three tests for genuine high autonomy: **how fast will we know we're wrong? how cleanly can we undo? what would prove we're right?** (if "not quickly / with great difficulty / by trusting the summary" → it isn't high autonomy). Every run should be preceded by a **contract**: goal, scope, non-goals, tools/permissions, stopping condition, **evidence**, escalation, and **budget** (time, attempts, parallelism, **tokens**). He lists per-level metrics (mean time between interventions, auto-approve %, **token cost per accepted change**, rework and defect-escape rates…) and four anti-patterns: **autonomy as status**, **permission laundering**, **summary substitution**, **fleet cosplay**.

## Why it matters
The two-axis split is a real conceptual upgrade over a single ladder: multi-agent skill is orthogonal to how far you trust one agent. The governing principle — *"the autonomy level should follow the verification process, not the task name"* (**calibrated autonomy**) — is defensible and operational, and the per-run **contract** plus the three questions make it actionable. It is grounded in first-party practice and Anthropic usage data, and it treats the **token budget as a first-class variable** (rare among such pieces). Punchline: **"Verification will always be the bottleneck."**

## Limits & blind spots (critical read)
- **Internal tension**: having argued that one axis is insufficient, he re-flattens the two axes into a single 0–5 climb ("orchestration only kicks in near the top") — L0–3 = agency, L4–5 = orchestration, i.e. effectively a ladder again.
- **Prescriptive, not validated**: no evidence the levels or metrics improve outcomes; the "calibration exercise" is self-assessment.
- **Second-hand statistics**: the Anthropic figures (~400K sessions / ~235K people, Oct 2025–Apr 2026; "≈70% of planning decisions by humans, ≈80% of execution by Claude"; clarification-vs-interrupt rates) are cited from other studies — verify at source before reuse.
- **Vendor-dated framing**: the Claude Code / Codex feature lists will age fast; "hundreds or thousands of agents" is aspirational.
- **Cost named but not quantified**: token budget, per-agent token cost and "orchestration tax" are named, with no absolute numbers.

## Takeaways
- Separate **agency** (one agent's reach) from **orchestration** (how many agents and who coordinates) — don't score them on one ladder.
- Six levels / three eras: Assist → Supervised → Scoped → Goal-driven → Parallel → Managed-by-exception.
- Choose the level from **risk × reversibility × available verification**, not the task name; **climb one axis at a time**, naming each new failure mode (drift, context rot, false parallelism, silent token spend, alert fatigue).
- Precede every run with a **contract** (goal / scope / non-goals / tools / stopping condition / evidence / escalation / **budget incl. tokens**); avoid the four anti-patterns.
- **Verification is the bottleneck** — high autonomy means humans deciding *which direction*, not doing every step.

## See also
- [Loop engineering: designing the system that prompts the agent](loop-engineering.md)
- [Comprehension debt & cognitive surrender](comprehension-debt.md)
- [Human-in-the-loop: static vs dynamic interrupts](human-in-the-loop-static-dynamic.md)
- [Agentic code review: from writing to verification](agentic-code-review.md)
