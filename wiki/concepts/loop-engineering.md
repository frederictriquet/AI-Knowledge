---
title: "Loop engineering: designing the system that prompts the agent"
type: "Concept"
theme: governance-alignment-ops
level: 🔴
source_url: https://addyosmani.com/blog/loop-engineering/
source_title: "Loop Engineering — Addy Osmani"
objectives: [code-generation]
---

# Loop engineering: designing the system that prompts the agent

**In one sentence** — The leverage shifts from prompt engineering to *loop engineering*: instead of prompting the agent by hand, you design an autonomous system that discovers the work, distributes it to agents, verifies, documents and decides what comes next — with no human between cycles.

## What the source says
Osmani describes a shift: prompting = write a prompt, read the output, write the next one — it does not scale. **Loop engineering** replaces this manual orchestration with a self-feeding **recursive loop** (the **"Factory Model"**). He distinguishes **agent harness engineering** (designing the environment of a **single** agent) from loop engineering (orchestrating the loop itself). A loop is made of ~6 building blocks, which he maps onto Codex *and* Claude Code: (1) **Automations** — scheduled triggering (`/loop`, `/goal`, GitHub Actions); (2) **Worktrees** — isolating parallel work (`git worktree`); (3) **Skills** — codifying project knowledge (`SKILL.md` format); (4) **Plugins/Connectors** — external tools via **MCP**; (5) **Sub-agents** — separating **ideation** and **verification**; (6) persistent **State/Memory** **on disk** — the often-forgotten block, because "the model forgets everything between runs". Example: a daily automation launches a triage skill (CI failures + issues), spawns one worktree per finding, a sub-agent fixes, another verifies against the skills and tests, connectors open the PR and update the ticket, and state files preserve progress for the next cycle.

## Why it matters
The article provides a **unified reading grid** for agentic tooling (the 6 components = as many tool categories), names the shift in leverage (from the prompt to loop design) and stays honest: "prompting your agents directly works too; loops are not universally superior".

## Takeaways
- Loop engineering = orchestrating an autonomous loop; agent harness engineering = tooling a single agent.
- The 6 blocks: automations · worktrees · skills · plugins/MCP · sub-agents · **on-disk memory** (the most overlooked).
- Separate **ideation** and **verification** into distinct sub-agents.
- Guardrails: verification stays **your** responsibility; watch the **token cost** (an unmonitored loop burns a lot); "build the loop, but build it like someone who intends to stay the engineer".
- Don't over-engineer: for many tasks, direct prompting is enough.

## See also
- [Agentic code review: from writing to verification](agentic-code-review.md)
- [Comprehension debt & cognitive surrender](comprehension-debt.md)
- [AgentOps](agentops.md)
- [Human-in-the-loop: static vs dynamic interrupts](human-in-the-loop-static-dynamic.md)
