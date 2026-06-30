---
title: "The 5 composable workflow patterns (Anthropic)"
type: "Concept"
theme: agent-fundamentals
level: 🔴
source_url: https://www.anthropic.com/engineering/building-effective-agents
source_title: "Building effective agents"
objectives: [code-generation]
---

# The 5 composable workflow patterns (Anthropic)

**In one sentence** — a catalog of composable patterns, from simplest to most complex, to assemble yourself rather than delegate to a framework.

## What the source says
Building block: the **augmented LLM** (LLM + retrieval + tools + memory). Then five patterns, by increasing complexity:
- **Prompt chaining** — split into sequential steps, each call processing the previous one's output; you can insert "gates" (programmatic checks) between steps. Trades latency for accuracy.
- **Routing** — classify the input and direct it to specialized handling (separates concerns; e.g. route easy questions to Haiku, hard ones to Sonnet).
- **Parallelization** — *sectioning* (independent subtasks in parallel) and *voting* (run the same task N times to gain confidence; e.g. several prompts review a piece of code).
- **Orchestrator-workers** — a central LLM decomposes **dynamically**, delegates to workers, synthesizes. Difference from parallelization: the subtasks are not predefined, they depend on the input.
- **Evaluator-optimizer** — one LLM generates, another evaluates and gives feedback in a loop; relevant when clear evaluation criteria exist.

## Example
*Sectioning* as a guardrail: one instance handles the user request while a second, in parallel, filters inappropriate content. Separating the two does better than entrusting guardrails and response to the same call — each instance stays focused. Same logic for **automating evals**: one LLM call per evaluated aspect. On the *voting* side, several distinct prompts review the same code for vulnerabilities; a single flag is enough to raise the alert.

## Why it matters
A **clean, named** catalog of composable patterns: *parallelization-voting* and *evaluator-optimizer* are distinct, reusable patterns here, often missing from general overviews of orchestration.

## Takeaways
- These patterns **combine**; measure performance and add complexity only if it improves the result.

## See also
- [Prompt chaining](prompt-chaining.md)
- [Multi-agent structures](multi-agent-structures.md) · [Mixture-of-Agents](mixture-of-agents.md)
- [Ensembling techniques](ensembling-techniques.md)
- [full post](../../sources/anthropic-effective-agents/md/building-effective-agents.md)
