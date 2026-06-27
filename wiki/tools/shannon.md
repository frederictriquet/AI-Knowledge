---
tool: "Shannon (Keygraph)"
title: "Shannon (Keygraph)"
themes: [security]
type: "Autonomous CLI agent (white-box AI pentester)"
url: https://github.com/KeygraphHQ/shannon
pricing_model: "Open-core: Shannon Lite (AGPL-3.0, open-source, no Keygraph backend) + Shannon Pro (commercial, PUBLIC price from $50/dev/month)"
llm_cost: "LLM credentials required BUT not just a raw key: Claude subscription OAuth OK (🟢) or API key/Bedrock/Vertex (🔑) → 🟢🔑"
objectives: [production]
family: "Domain-specialized autonomous agents"
eco_icons: "🔓🔒"
llm_cost_icons: "🟢🔑"
summary: "Autonomous **white-box** open-core AI pentester (Shannon Lite AGPL-3.0) by Keygraph: analyzes source code + runs real exploits (proof by exploitation) on web/API; multi-agent recon→analysis→exploitation→reporting, 96% on the XBOW Benchmark. LLM credentials required but Claude subscription OAuth OK (not just a raw key). Public Pro from $50/dev/month. No Keygraph backend for Lite. ⚠️ Never against production, disposable environment"
migrated_from: shannon
---

# Shannon (Keygraph)

**In one sentence** — an autonomous *white-box* AI pentester that analyzes your source code, identifies attack vectors and **runs real exploits** to prove vulnerabilities before production. If it can't exploit it, it doesn't report it.

> 🔐 **Usage scope**: offensive security. ⚠️ **Never run it against production** or unauthorized targets — Shannon **mutates application state** (creates users, triggers requests). Run in a **sandbox / staging / disposable** environment only, against authorized targets.

## Type & integration
**Autonomous CLI agent** (launched via `npx` + Docker), with **orchestrated multi-agent workflows**, written in **TypeScript** (~95%). **White-box** approach: requires access to the **source code**. Four phases: **reconnaissance → vulnerability analysis (parallel) → exploitation (parallel) → reporting**. Targets actively exploitable flaws: injection, XSS, SSRF, broken authentication/authorization. Generates **"proof-by-exploitation" reports** (reproducible PoC) rather than speculative findings.

## Pricing model
**Open-core**, by the company **Keygraph**:
- **Shannon Lite**: **open-source AGPL-3.0 core** (on GitHub), for strictly authorized tests.
- **Shannon Pro**: an all-in-one commercial AppSec platform — black-box, **agentic SAST**, **SCA with reachability analysis**, secrets detection, business-logic testing, **CI/CD** integration, enterprise features. **Public price: from $50/dev/month** (+ add-ons), self-hosted Enterprise on quote; free community program (nonprofits/startups ≤20 devs).

✅ Verified (source-code grep): **no Keygraph backend/account/telemetry required for Lite** — no `api.keygraph.io` call, no posthog/sentry; the "login" references in the code concern the **target** app being tested.

Argument: filling the "364 days" between two annual pentests by integrating continuous testing.

## LLM cost
**🟢🔑 — LLM credentials required, but NOT necessarily a paid API key.** Verified in the code: the preflight fails without one of `ANTHROPIC_API_KEY` / `CLAUDE_CODE_OAUTH_TOKEN` / `ANTHROPIC_AUTH_TOKEN` (or Bedrock/Vertex). But the setup offers an **OAuth Token** method + "subscription" retry presets → Shannon Lite **can run on a Claude/Claude Code subscription (OAuth), without a raw API key** (🟢), or via BYOK key/Bedrock/Vertex (🔑). Cost depends on **complexity**; a scan takes ~**1–1.5 h** → potentially **significant** token usage (code analysis + multi-agent exploitation).

## What it's for
Finding and **proving** exploitable vulnerabilities continuously (CI/CD, before production), with a low false-positive rate thanks to validation by exploitation. Highlighted performance: **96.15%** success on the **XBOW Benchmark** (no hints, source-aware).

## Notes
- **Family 10 (domain-specialized autonomous agents)**: the second autonomous pentester alongside [AIDA (AI-Driven Security Assessment)](aida.md). Differences: **Shannon = white-box** (analyzes source code) + **open-core** (Lite AGPL / Pro commercial) + strong benchmark, Claude/BYOK-centric; **AIDA = a 400+ toolbox via MCP**, AGPL, alpha, model-agnostic. Complementary approaches (white-box vs tooling).
- ⚠️ An agent that **runs real exploits** → environment guardrails are essential (disposable, isolated, authorized).
- Third-party variants seen: `unicodeveloper/shannon` (a "Automated Pentesting from Keygraph Shannon" skill), fork `IgorOffline/KeygraphHQ-shannon`. Official = `KeygraphHQ/shannon`.

## Source
- Repo: https://github.com/KeygraphHQ/shannon · open-source: https://keygraph.io/open-source

*(verified on 2026-06-15 — GitHub README + Keygraph site + web search)*
