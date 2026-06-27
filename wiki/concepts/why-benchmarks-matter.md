---
title: "Why agent benchmarks matter"
type: "Concept"
theme: benchmarks
level: 🟡
source_url: https://arxiv.org/abs/2310.06770
source_title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
migrated_from: pourquoi-les-benchmarks-comptent
---

# Why agent benchmarks matter

**In one sentence** — public agent benchmarks (SWE-bench, τ-bench, GAIA, WebArena) are the quantified, reproducible reminder that on **real, long-horizon, tool-using** tasks, frontier agents still fail by a wide margin — and they define *where* to look in order to improve.

## What the sources say

- **SWE-bench** — on real GitHub bugs, the best model of the time (Claude 2) resolves only **1.96%** of issues. Fixing a real bug requires coordinating multi-file changes, executing code, and digesting long contexts.
- **τ-bench** — facing a simulated user and business rules, even gpt-4o succeeds on **fewer than 50%** of tasks and stays highly **inconsistent** (pass^8 < 25% in retail). Reliability, not just one-off success, is measured via **pass^k**.
- **GAIA** — on questions "easy for a human," the gap is brutal: **92% (humans) vs 15% (GPT-4 + plugins)**.
- **WebArena** — on long-horizon web tasks, the best GPT-4 agent plateaus at **14.41%** against **78.24%** for humans. Evaluation targets **functional correctness**, not surface resemblance.

## Why it matters

These benchmarks provide the **external reference point** that internal evaluation often lacks:

- **absolute scores** comparable from paper to paper, which defuse optimism ("our agent works");
- **end-state evaluation protocols** (τ-bench compares the database state, WebArena functional correctness) rather than the produced text — directly transposable to a business eval;
- a **reliability metric** (pass^k) that formalizes the idea that an agent that succeeds *sometimes* is not deployable;
- a **human bound** (GAIA, WebArena) to situate the agent honestly.

## Key points

- Measure on **realistic, long-horizon** tasks, not synthetic micro-tasks.
- Evaluate the **end state / functional correctness**, not surface similarity.
- Measure **consistency across several attempts** (pass^k), not just first-shot success.
- Keep a **human bound** as an honest reference.
- The numbers are dated: they hold as **method** and as a reminder of humility, not as a frozen ranking.

## See also

- [Trajectory evaluation](evaluation-trajectoire.md) · [Computer-use & GUI agents](computer-use-gui-agents.md) · [Error analysis](error-analysis.md)
