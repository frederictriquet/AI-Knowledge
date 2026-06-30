---
title: "Workflows vs agents: Anthropic's architectural distinction"
type: "Concept"
theme: agent-fundamentals
level: 🔴
source_url: https://www.anthropic.com/engineering/building-effective-agents
source_title: "Building effective agents"
objectives: [code-generation]
---

# Workflows vs agents: Anthropic's architectural distinction

**In one sentence** — distinguish **workflows** (LLMs and tools orchestrated by predefined code paths) from **agents** (the LLM dynamically directs its own process), instead of calling everything "agentic".

## What the source says
Everything is lumped under "agentic systems", but a clear distinction is warranted: a **workflow** follows predefined code paths; an **agent** retains control of *how* it accomplishes the task (it plans, chooses its tools, loops on environment feedback). Central recommendation: seek the simplest solution and add complexity only if it *measurably* improves the outcome — often, optimizing a single LLM call (retrieval + in-context examples) is enough. Agentic systems trade **latency and cost** for performance; agents should be reserved for open-ended problems where you cannot code a fixed path, in trusted environments.

## Example
Customer support is an ideal ground for an open-ended agent: the exchange follows a conversational thread but requires actions — tools to pull customer data, order history, knowledge-base articles, and to trigger a refund or update a ticket. Success is measurable (resolution as defined by the user), to the point that some companies charge **only for successful resolutions** — a trust bet that no fixed-path workflow would allow across this spectrum of requests.

## Why it matters
The distinction provides an explicit **decision criterion** and an anti-hype warning: many applications do not need an agent, and contrasting workflow and agent avoids over-complicating by default.

## Takeaways
- Workflow = predictability/consistency (well-defined tasks); agent = flexibility/model-driven decision, at scale.
- Autonomy = higher costs and **compounding errors** → test in a sandbox, guardrails, stopping condition (max iterations).

## See also
- [Canonical agent framework](canonical-agent-architecture.md)
- [Orchestration types](orchestration-types.md) · [ReAct](react.md)
- [full post](https://www.anthropic.com/engineering/building-effective-agents)
