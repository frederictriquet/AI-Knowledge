---
title: "ACI: designing the agent-computer interface"
type: "Concept"
theme: agent-fundamentals
level: 🔴
source_url: https://www.anthropic.com/engineering/building-effective-agents
source_title: "Building effective agents"
objectives: [code-generation]
---

# ACI: designing the agent-computer interface

**In one sentence** — give as much care to tool definitions (names, descriptions, formats) as to prompts: the agent-computer interface (ACI) is, for an agent, what the human-computer interface is for a person.

## The essentials
**Tool definitions deserve as much prompt engineering as the prompts themselves.** Choose formats the model writes *easily* — avoid diffs (which require counting lines in advance) or code inside JSON (escaping quotes and newlines); leave the model tokens to "think" before locking itself in; **poka-yoke** the tools (make mistakes structurally hard). Put usage examples, edge cases and input formats in the description — "like a good docstring for a junior developer." A SWE-bench anecdote: they spent **more time optimizing the tools than the overall prompt**; enforcing **absolute paths** fixed, in one stroke, the relative-path errors that occurred after a directory change.

## Example
To have the agent edit a file, two formats are equivalent for the machine but not for the model: the **diff** forces writing the hunk header (`@@ -12,7 +12,9 @@`) by counting lines *before* writing the code — the model gets stuck. **Code inside JSON** forces escaping newlines and quotes. Prefer a full rewrite in markdown, close to what the model has seen on the web: zero counting, zero escaping, hence fewer errors.

## Why it matters
Tool interface design is a first-order reliability lever, as important as the prompt itself.

## Takeaways
- Invest in the **ACI** as much as in the human-computer interface; test the tools on real inputs (a workbench) and iterate.
- Put yourself "in the model's shoes": does the description make the usage obvious?

## See also
- [Tool calling](tool-calling.md) · [Tool grounding](tool-grounding.md)
- [Augmented language models](augmented-language-models.md)
- [full post](https://www.anthropic.com/engineering/building-effective-agents)
