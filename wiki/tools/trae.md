---
tool: "Trae"
title: "Trae"
themes: [frameworks-tooling]
type: "Application (IDE)"
url: https://www.trae.ai/
pricing_model: "Freemium + subscriptions (Lite/Pro/Ultra)"
llm_cost: "Included in the subscription (quotas / token pool)"
objectives: [code-generation]
family: "Coding agents & IDEs"
eco_icons: "🎁🔁"
llm_cost_icons: "📦💸"
summary: "ByteDance's AI IDE based on VS Code; premium models (Claude, GPT, DeepSeek) provided via a **credit** system (tokens × model rate, capped per tier), Lite/Pro/Pro+/Ultra subscriptions $3–100/month"
---

# Trae

**In one sentence** — ByteDance's standalone AI IDE, based on VS Code, where premium models (Claude, GPT, DeepSeek) are provided and billed within the subscription, with no API key to bring.

## Type & integration
**Standalone IDE application** (not a mere extension): a fork of VS Code, available on macOS and Windows, plus a browser-based Cloud IDE. Launched by ByteDance in January 2025. Two flagship modes: **Builder** (describe a project in natural language → code generation) and **Chat** (questions, debug, optimization). Comes in an international version and a Chinese version.

## Pricing model
**Freemium + subscriptions**:
- **Free**: $0 — autocompletions + access to premium models (quotas / queue).
- **Lite**: ~$3/month (≈ $5 of "Basic Usage").
- **Pro**: ~$10/month (≈ $20 of credits).
- **Pro+**: ~$30/month (≈ $90 of credits).
- **Ultra**: ~$100/month (≈ $400 of credits).

The exact cost and quotas evolve; check the up-to-date pricing page.

## LLM cost
**Included + resold by usage** 📦💸 — no API key to provide: ByteDance **provides the models** (Claude, GPT, DeepSeek…). But the billing is really a **credit system**: each tier grants a monthly "Basic Usage" allowance (in $), and consumption = **tokens × the model's API rate**, debited from that allowance (then subsidized "Bonus Usage"). So *included up to the credit cap*, with a **usage-resale** logic by the vendor. Cost capped by the plan as long as you stay within the allowance; model choices/limits dictated by the vendor. (Still no key to manage, unlike the BYOK of [Kilo Code](kilo-code.md).)

Order of magnitude: from $0 (free, with tight quotas) to $100/month (Ultra). Very good claimed value for access to high-end models.

## What it's for
Developing in a full IDE driven by AI: end-to-end project generation (Builder), code assistance, debug, refactor. Targets developers who want a "turnkey" IDE with models included, without managing keys or usage-based costs.

## Notes
- ⚠️ **Privacy**: a ByteDance product — the policy states that code snippets and interaction data *may* be used for training/improvement, with data transfers between servers worldwide. A strong point of attention in a professional/sensitive context.
- Based on VS Code → familiar extension ecosystem.
- Competitors: Cursor, Windsurf; Trae stands out for aggressive pricing and included models.

## Source
- Official site: https://www.trae.ai/
- 2026 reviews (pricing, Builder Mode): aibase, vibecoding.app, ohaiknow

*(verified on 2026-06-15 — official site + web search; prices to reconfirm as they evolve)*
