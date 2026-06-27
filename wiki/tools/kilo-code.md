---
tool: "Kilo Code"
title: "Kilo Code"
themes: [frameworks-tooling]
type: "IDE extension / CLI"
url: https://kilo.ai/
pricing_model: "Open-source + pay-as-you-go (zero-margin gateway) + optional subscriptions"
llm_cost: "BYOK or usage-resold (at cost, no markup)"
objectives: [code-generation]
family: "Coding agents & IDEs"
eco_icons: "🔓🎁💳"
llm_cost_icons: "🔑💸"
summary: "Open-source AI coding agent (VS Code, JetBrains, CLI); 500+ models, tokens at cost via gateway or BYOK"
migrated_from: kilo-code
---

# Kilo Code

**In one sentence** — open-source AI coding agent (VS Code/JetBrains extension, CLI, Slack, cloud) giving access to 500+ models, either with your own API keys or via a gateway that bills tokens at cost.

## Type & integration
Open-source "agentic engineering" platform, primarily an **IDE extension** (VS Code, also on the Open VSX Registry, and JetBrains), with a **CLI**, a Slack integration and a cloud offering. Licenses: Apache 2.0 for the extensions, MIT for the CLI → auditable and self-hostable. Descended from the Roo Code / Cline lineage of agents.

## Pricing model
- **Free, open-source software**: the extension/CLI costs nothing to install and use.
- **Monetization via the Kilo Gateway** (pay-as-you-go) and optional **Kilo Pass** plans to smooth out monthly spend:
  - Starter ~$19/month, Pro ~$49/month, Expert ~$199/month (bonus credits vs the price, annual/loyalty bonus).
  - Team/Enterprise offerings from ~$15/user/month (centralized billing, SSO, audit logs).
- $20 in free credits on sign-up.

## LLM cost
The LLM is not included — two paths, your choice:
- **BYOK** 🔑 — plug in your Anthropic, OpenAI, Google, Azure, AWS Bedrock… keys, or **local** models via Ollama / LM Studio (zero cost). You then pay the provider directly.
- **Usage-resold** 💸 via the Kilo Gateway — **at cost, no markup** (central sales claim: rates match exactly those of the providers).

Order of magnitude: fully dependent on the chosen model. Free with local/free models; for large models (Claude Opus, GPT-5.5…) the cost follows the provider's token rate, potentially high on large volumes — but with no Kilo surcharge.

## What it's for
Coding in agent mode in the IDE: generation, refactor, autocompletion, multi-step task execution, all while keeping model choice and cost control (no markup, BYOK possible). Open-source alternative to proprietary agents, with access to a large model catalog.

## Notes
- 500+ models advertised (GPT-5.5, Claude Opus 4.7, Sonnet 4.6, Gemini 3.1 Pro…).
- The "no markup" point is the differentiator against competitors that take a commission on tokens.
- Self-hostable / auditable thanks to the open licenses — relevant in an enterprise context.
- Close competitors: Cline, Roo Code, Cursor, Continue.

## Source
- Official site: https://kilo.ai/ (`kilocode.ai` redirects to this domain) — pricing page https://kilo.ai/pricing
- Repository: https://github.com/Kilo-Org/kilocode

*(verified on 2026-06-15 — official site + pricing page + GitHub)*
