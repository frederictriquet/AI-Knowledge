---
tool: "Cursor BugBot"
title: "Cursor BugBot"
themes: [evaluation]
type: "Web service (GitHub app)"
url: https://cursor.com/bugbot
pricing_model: "Proprietary (Anysphere) — subscription → switching to usage-based"
llm_cost: "Included (frontier + in-house models provided in the price)"
objectives: [code-generation, reliability]
family: "AI code review"
eco_icons: "🔒🔁💳"
llm_cost_icons: "📦"
summary: "AI PR reviewer from Anysphere (Cursor) targeting **logic bugs** with few false positives (**precision**-oriented); frontier + in-house models. Historically $40/user/month → **switching to usage-based** (~$1–1.50/run, post 8 June 2026). Cursor account required"
migrated_from: cursor-bugbot
---

# Cursor BugBot

**In one sentence** — AI PR reviewer from Anysphere (Cursor) that targets **hard logic bugs** with a low false-positive rate, and comments directly in GitHub.

## Type & integration
Application connected to GitHub: automatic PR review, comments on potential issues and fix suggestions. Tied to the Cursor ecosystem (Cursor account required). Uses "a combination of frontier and in-house models". Favours **precision** (few false positives) over volume of findings.

## Pricing model
Proprietary (Anysphere), in pricing transition (observed 2026-06-17):
- **Historical**: $40/user/month ($32 annual), 200 PRs/month, unlimited reviews.
- **New model**: **usage-based billing** (Teams and Individuals, from renewal after 8 June 2026) — seat fees removed; a run costs on average ~$1.00–1.50 depending on PR size/complexity. Billed per author of a reviewed PR (external contributors included).
- 14-day trial.

## LLM cost
**Included (📦)**: the models (frontier + in-house) are provided by Cursor in the price — no BYOK, no tokens billed separately. The "usage-based" price remains a product charge (per run), not a resale of raw tokens.

## What it's for
A **precision**-oriented AI review pass on GitHub: surfacing real logic bugs with little noise, complementing a more recall-oriented tool (architecture/context).

## Notes
- Pricing in flux: check the model in force at adoption time (seat vs usage).
- Low overlap with other reviewers → good candidate for a multi-tool strategy.

## Source
https://cursor.com/bugbot · https://cursor.com/blog/may-2026-bugbot-changes *(verified on 2026-06-17)*
