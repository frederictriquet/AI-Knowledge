---
title: "AutoGPT"
type: "Concept"
theme: agent-fundamentals
level: 🟢
source_url: https://www.ibm.com/think/topics/autogpt
source_title: "What is AutoGPT?"
---

# AutoGPT

**In one sentence** — the 2023 demonstrator that decomposes a high-level goal into subtasks and runs a create/prioritize/execute loop with vector memory; mostly of historical value.

## In detail
AutoGPT is an open-source platform launched on 30 March 2023 by Toran Bruce Richards (Significant Gravitas). It relies on OpenAI's GPT models (GPT-4o mini, GPT-4, GPT-3.5) to understand a high-level goal, break it into subtasks and automate their execution. The typical workflow: user input, task creation, task prioritization, execution, progress evaluation and workflow improvement, finalization. Dedicated agents create, prioritize and execute the tasks, and communicate in real time to adjust what comes next. AutoGPT accesses the internet through plug-ins and has short- and long-term memory thanks to vector databases. The limitations are documented: the tool remains experimental, its reliability is not guaranteed; it can get distracted, hallucinate then build on those hallucinations, misinterpret data and end up failing. AutoGPT is not an AGI.

## Example
As a business-development tool, you give AutoGPT a single goal such as "identify new leads and prepare a social-media plan": without human prompting, it generates its own queue of subtasks, browses the web via plug-ins to analyze news articles and social content, summarizes the trends, then sketches out as much as a whole season of podcast episodes or debugs a website's code. The documented downside of letting it run: it may get distracted by a non-essential task, hallucinate, then build the next subtasks on that hallucination until failure.

## Tradeoff / insight (for a senior)
Importance is primarily historical: AutoGPT popularized the idea of auto-prompting (the agent generates its own prompts toward the goal, without human re-prompting), but its fragility is documented (drift, cumulative hallucinations, token costs, complex installation/self-hosting via Docker). Worth knowing as a milestone, not as a production foundation.

## Primary source
Attributed to Toran Bruce Richards (2023). See the Significant-Gravitas/AutoGPT GitHub repository.

## See also
- [babyagi](babyagi.md)
- [taxonomie-5-types-agents](five-agent-types-taxonomy.md)
