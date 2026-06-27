---
tool: "Mergify"
title: "Mergify"
themes: [governance-alignment-ops]
type: "SaaS platform — merge queue & CI (flaky-test detection)"
url: https://mergify.com/
pricing_model: "Proprietary SaaS, freemium (free for open-source; paid per contributor — exact prices to verify)"
llm_cost: "Included (📦) — core mostly deterministic; any AI (flaky detection/fix) is bundled, no key/BYOK"
objectives: [code-generation, production]
family: "CI/CD, delivery & AI-assisted operations"
eco_icons: "🎁🔁"
llm_cost_icons: "📦"
summary: "Merge queue (\"keep main green\") + CI Insights (auto-retry) + Test Insights (detects/quarantines/fixes **flaky** tests) + Stacks. Core mostly deterministic (light AI on flaky). Freemium (free OSS, paid per contributor — exact prices to verify)"
migrated_from: mergify
---

# Mergify

**In one sentence** — **merge and CI** platform: merge queue ("keep main green"), CI Insights (observability + auto-retry), Test Insights (detects, quarantines and fixes **flaky tests**), Merge Protections and Stacks.

## Type & integration
**Proprietary SaaS**, plugged into your existing CI (35+ integrations) **without rewriting tests**. Components: **Merge Queue** (avoid breaking `main`), **CI Insights** (auto-retry transient failures), **Test Insights** (quarantine/fix flaky), **Merge Protections** (governance), **Stacks** (split large PRs). Scale: 2k+ orgs, 25k+ users, 75k+ PRs/month.

## Pricing model
**Proprietary, freemium**: historically **free for open-source / public repos**, paid offerings **per contributor** beyond that. ⚠️ Exact prices **not verified** here (`/pricing` page not detailed). *(observed 2026-06-18)*

## LLM cost
**Included (📦)** — Mergify is **mostly deterministic automation** (merge queue rules, retry, flaky quarantine); the "flaky detection/fix" part may use AI, **bundled in the service**. You neither bring nor pay for a separate LLM. *(So "AI" in the broad sense, not a token-hungry LLM agent.)*

## What it's for
Smoothing **delivery**: keep `main` green, prevent flaky tests from blocking merges (fewer reruns → cheaper CI), govern merges. Sits between **test** and **deploy** in the SDLC.

## Notes
- **[CI/CD, delivery & ops](../guides/generate-code-with-ai.md#fam-ci-cd-delivery-ai-assisted-operations) family**, **CI / merge / flaky** sub-space — vs the **AI SREs** [Cleric](cleric.md)/[Resolve.ai](resolve-ai.md)/[Traversal](traversal.md) (run/incident).
- More "AI-native" neighbors on the CI side (candidates, unverified): **Datadog Bits AI Dev Agent** (autonomous flaky fix → draft PR), **Aviator**, **Trunk** (flaky tests).
- To verify: exact pricing grid, real depth of the "AI" (vs rule-based automation).
- ⚠️ Adoption figures ("2k+ orgs, 25k+ users, 75k+ PRs/month") = unverified publisher communication; the core is **deterministic** (merge queue/CI), the "AI" part stays marginal — don't expect an agent.

## Source
- Site: https://mergify.com/ (and /pricing)

*(verified on 2026-06-18 — official site + curl; exact prices to confirm)*
