---
title: "Integrated prompt environments — give prompts to domain experts"
type: "Concept"
theme: prompting
level: 🔴
source_url: https://hamel.dev/blog/posts/field-guide/
source_title: "A Field Guide to Rapidly Improving AI Products"
---

# Integrated prompt environments — give prompts to domain experts

**In one sentence** — prompts "are just English": the most effective teams give domain experts the tools to write and iterate on prompts **directly**, in the context of the application, instead of routing their expertise through engineers.

## What the source says
Hamel describes a recurring anti-pattern: a domain expert (instructional designer, lawyer, doctor…) formalizes their knowledge in a PowerPoint, which engineers then "re-translate" into prompts. But **a prompt is English**: this round trip creates needless friction and dilutes the expertise. The best teams invert the model.

Two levels of tooling:
1. **Prompt playgrounds** (Arize Phoenix, LangSmith, Braintrust) — a good starting point: test prompts, inject example sets, compare results.
2. **Integrated prompt environments** — the step most teams miss. A real AI application is not just a prompt: RAG over a knowledge base, agent orchestration, business logic. Instead of an isolated playground, you build an **"admin mode" of the real interface** that exposes prompt editing **within its application context** (same data, same RAG, same logic as what the end user sees). The example given: a real-estate assistant where the agent UI gets an "admin mode" letting the product team edit the prompt and debug in real conditions.

**A side barrier — jargon.** Wrapping the work in technical vocabulary ("we're building an agent," "RAG," "prompt injection") excludes the real domain experts, who think they are incompetent when the actual task is… writing a prompt. Hamel offers a translation table: "RAG" → "making sure the model has the right context"; "prompt injection" → "preventing people from tricking the AI into ignoring our rules"; "hallucination" → "sometimes the AI makes things up, you have to check its answers."

## Example
At an edtech startup, Hamel observes engineers, product managers, and learning specialists talking past each other in meetings: engineers keep saying "we'll build an agent that does XYZ" when the real job was… writing a prompt. The concrete consequence: the learning specialists, who were the real domain experts, felt unable to contribute because they did not understand "agents." The jargon had erected an artificial barrier that excluded exactly the people best placed to improve the product. Hamel notes the same pattern among the lawyers, psychologists, and doctors of his clients.

## Why it matters
Putting the domain expert at the center of the iteration loop, in the real application context, is an often-neglected lever for product improvement: most AI-tooling guides focus on engineering/platform and never address **who** writes the prompts.

## Takeaways
- Prompts are English: have domain experts write and iterate **directly**, not through a re-translation by engineers.
- Playground = starting point; **integrated prompt environment** (admin mode of the real UI, with RAG/agents/business logic in place) = the step teams forget.
- Ban the jargon that excludes experts: describe the task in plain language, not technical terms.

## See also
- [Error analysis: look at your data](error-analysis.md)
- [Eval-driven development](eval-driven-development.md)
- [AgentOps](agentops.md)
- [full post](../../sources/hamel-husain/md/field-guide.md)
