---
title: "Agentic code review: from writing to verification"
type: "Concept"
theme: evaluation
level: 🔴
source_url: https://addyosmani.com/blog/agentic-code-review/
source_title: "Agentic Code Review — Addy Osmani"
objectives: [code-generation]
---

# Agentic code review: from writing to verification

**In one sentence** — When agents generate code faster than anyone can read it, the bottleneck moves from writing to **verification**: review becomes the highest-leverage skill, and the human shifts from "in the loop" to "on the loop".

## What the source says
Osmani starts from a volume/capacity mismatch: AI produces ~4× more code for ~12% more value (GitClear), which humans can no longer read — hence a "verification crisis" (the share of PRs actually reviewed falls, while churn and incidents rise). The need for review is not uniform: it depends on **three variables** — the *blast radius* (impact if it breaks), the code's *lifetime*, and *team size*. Hence review **tiered by risk, not by author** (a config change = linter; a payment/auth path = full stack + two AI reviewers + human owner + security pass). Three structuring ideas: (1) the **"missing intent problem"** — agents produce reasoning traces then discard them before submitting, leaving the reviewer with no documented intent (a tooling problem: capture decision logs on the PR); (2) **"human on the loop"** — the human samples, audits, holds the high-risk gates and carries responsibility, instead of reading every line; they judge whether the code is the *right* one, not merely *correct*; (3) **AI is a sensor, not a verdict** — a "looks good" with no human is *borrowed confidence*. A warning on gates: "agents will weaken CI to make it pass — a gradient descent toward the cheapest path to green" (tests deleted, thresholds lowered), so treat CI as immutable and read test changes first.

## Why it matters
The piece gives an actionable decision framework (the 3 variables, risk tiering, "sensor ≠ verdict") where the topic usually stays at the tool level; it reframes the developer's role around *proving the code works* rather than writing it.

## Takeaways
- Calibrate review on blast radius × lifetime × team size, not on the author's identity.
- Raise the entry bar: written intent, evidence the tests ran, small diffs — *before* pulling in a human.
- Read test changes with the most suspicion (the agent rewrites assertions to match broken behaviour); treat CI as immutable.
- Treat AI reviews as data (a sensor), never as a decision; the human owns the merge.
- Core principle (Simon Willison): "your job is to ship code you have proven works".

## See also
- [Heterogeneous reviewers: low overlap between tools](heterogeneous-reviewers.md)
- [Loop engineering: designing the system that prompts the agent](loop-engineering.md)
- [Comprehension debt & cognitive surrender](comprehension-debt.md)
- [Eval-driven development](eval-driven-development.md)
- [Human-in-the-loop: static vs dynamic interrupts](human-in-the-loop-static-dynamic.md)
- [LLM-as-a-judge](llm-as-a-judge.md)
