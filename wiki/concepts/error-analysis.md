---
title: "Error analysis: look at your data"
type: "Concept"
theme: evaluation
level: 🔴
source_url: https://hamel.dev/blog/posts/field-guide/
source_title: "A Field Guide to Rapidly Improving AI Products"
objectives: [reliability]
---

# Error analysis: look at your data

**In one sentence** — Before any metric, manually read your product's traces, annotate undesirable behaviors, then build a taxonomy of failure modes and count their frequency.

## What the source says
Hamel presents error analysis as "the single most valuable activity in AI development" and the highest-ROI activity. Teams' most common mistake is the "tools first" mindset: piling up dashboards and generic metrics instead of understanding what works. He contrasts two approaches: "top-down" (starting from metrics like hallucination or toxicity, which misses domain-specific problems) and the more effective "bottom-up", which forces you to look at the real data and lets metrics emerge. The concrete process at NurtureBoss: a simple viewer, an open note per conversation, then an LLM to build a taxonomy of failure modes, finally a mapping of each row to a label and a frequency count. Result: three issues covered over 60% of the problems, and date handling went from 33% to 95% success.

## Example
Hamel opens on a real scene: a client proudly shows him an eval dashboard full of generic metrics. The trap: a team celebrates a "helpfulness score" gaining 10% while its users still fail at basic tasks — like optimizing the site's load time when the checkout funnel is broken. Conversely, at NurtureBoss, open annotation surfaces three named failure modes: conversation flow (missing context, clumsy answers), handoff failures (not knowing when to transfer to a human), and rescheduling (date handling). Date handling failed 66% of the time on phrasings like "let's plan a visit in two weeks".

## Why it matters
Hamel provides the concrete operational protocol (annotate, taxonomize, count) that precedes any automation — where most resources stay at the conceptual level.

## Takeaways
- Start by reading real traces, not by picking a tool or a metric.
- Annotate in open notes (bottom-up), not with categories imposed in advance.
- Use an LLM to synthesize the taxonomy of failure modes from the notes.
- Map each trace to a failure mode and count: target the 20% of causes that produce 60-80% of errors.
- Derive targeted tests directly and measure improvement on those failure modes.

## See also
- [Trajectory evaluation](trajectory-evaluation.md)
- [Function-calling error taxonomy](function-calling-error-taxonomy.md)
- [Prompt engineering is empirical](prompt-engineering-is-empirical.md)
- [full post](https://hamel.dev/blog/posts/field-guide/)
