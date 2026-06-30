---
tool: "ECC"
title: "ECC"
themes: [frameworks-tooling, governance-alignment-ops, security, efficiency-cost]
type: "Agent harness system (skills/agents/hooks/rules) — multi-platform, OSS + GitHub App"
url: https://github.com/affaan-m/ECC
pricing_model: "Open-source (MIT) free; ECC Pro (GitHub App, private repos) $19/seat/month + free tier; GitHub sponsoring from $5/month"
llm_cost: "🟢🔑 mixed — drives the host harness with no key; multi-provider BYOK (Anthropic/OpenAI/local Ollama) for the autonomous modules"
objectives: [code-generation]
family: "Workflow, methodology & spec-driven development"
eco_icons: "🔓🎁🔁"
llm_cost_icons: "🟢🔑"
summary: "All-in-one \"operator system\" (MIT): 261 skills, 67 agents, hooks, learned instincts, memory, AgentShield, multi-harness (Claude Code/Cursor/Codex…). ECC Pro $19/seat/month (private repos). ⚠️ Very young (created 2026-01) despite the \"production\" pitch; **maximalist**, in tension with its own \"<10 MCP/<80 tools\" rule; single maintainer; 220k★ in 5 months = hype ≠ proven value; self-declared internal metrics. More focused peers (Superpowers, Spec Kit) often preferable"
---

# ECC

**In one sentence** — open-source "operator system" that stacks onto your existing agent (Claude Code, Cursor, Codex, OpenCode…) a complete infrastructure — skills, sub-agents, hooks, learned *instincts*, persistent memory, security scanner — to standardize agentic work across harnesses.

## Type & integration
**Multi-platform harness overlay** (by `affaan-m`). Installs on top of the host agent (`/plugin install ecc@ecc`, or `./install.sh --profile [full|core|minimal]`). Announces **67 agents, 261 skills, 92 legacy command shims, 15 hook events, 6 MCP servers**, 12+ language ecosystems. Named blocks: **Skills** (the main surface, replaces slash-commands), **Agents** (delegated sub-agents), **Hooks** (event-driven automations), **Rules** (per-language guidelines), **Instincts** (learned patterns with *confidence scoring*, "Continuous Learning v2"), **AgentShield** (security audit, separate repo). Adapter pattern (`adapter.js`) to reuse scripts across harnesses.

## Pricing model
**Open-source MIT** (*"MIT-licensed forever"*), free. Commercial layer: **ECC Pro** = hosted GitHub App for **private repos**, **$19/seat/month**, with free/pro/enterprise tiers on the GitHub Marketplace ("ECC Tools"). OSS funding via **GitHub Sponsors from $5/month** (sponsorship tiers up to $3,700/month = logo placement, *not* product access). *(observed 2026-06-24)*

## LLM cost
**🟢🔑 mixed.** The **core** (skills, hooks, rules, YAML instincts, context injection, `/learn`) runs **in your host session** → consumes your existing subscription/agent, **with no key of its own** (🟢). But ECC bundles a **real multi-provider LLM layer** (`src/llm/providers/`: Anthropic, OpenAI, **local Ollama**, …) used by the **autonomous modules** — `security-scan`/**AgentShield** ("Requires ANTHROPIC_API_KEY"), `autonomous-agent-harness` (`curl api.anthropic.com`) — which require **your key** (🔑 BYOK; local Ollama option = free). Includes a `cost-tracker.js` that instruments token cost (consistent with its optimization pitch).

## What it's for
Standardizing and tooling multi-agent work: same skills/hooks/rules/security across Claude Code, Cursor, Codex, OpenCode. Targets the dev who juggles several harnesses and wants a common base + persistent learning (instincts) + safeguards (`beforeShellExecution`, AgentShield).

## Notes
- **Family 4 (workflow/methodology)**: peer of [Superpowers](superpowers.md), [gstack](gstack.md), [BMAD-METHOD](bmad-method.md), [GSD](gsd.md), [Cavekit](cavekit.md) and of the meta-harness [Ruflo](ruflo.md). The most **maximalist** positioning of the group ("all-in-one operator system") where the peers are more focused.
- ⚠️ **Young despite the "production" pitch**: repo **created on 2026-01-18** (~5 months), but presents itself as *"production-ready"* "evolved over 10+ months" — wording to take with caution. **v2.0.0** (June 2026).
- ⚠️ **Hype ≠ proven value**: **220.8k★ / 33.8k forks** (confirmed via GitHub API) reached in ~5 months. This is in the upper range for harnesses (Superpowers ~237k, gstack ~114k) — so *not* an anomaly, but a high star count remains a **signal of virality/promotion, not proof of production use**. No external benchmark.
- ⚠️ **Self-declared internal metrics, unverified**: "997+ tests", "AgentShield 1282 tests / 98% coverage / 102 rules", "261 skills" — README figures, not audited.
- ⚠️ **Tension with its own message**: preaches context frugality ("keep under 10 MCPs, under 80 tools"; one MCP tool description eats into the 200k window → ~70k) while shipping 261 skills + 67 agents + 6 MCP + SessionStart injection (8000 chars) → risk of the very **context bloat** it warns against; install in the `core`/`minimal` profile rather than `full`.
- ⚠️ **Single maintainer**: *"a single maintainer ships weekly across 7 harnesses"* → sustainability/bus-factor risk for "production" use.
- **For a decision**: real interest if you want a *unified multi-harness* base with built-in learning + security. But for most needs, a **focused** peer (Superpowers for methodology, Spec Kit for spec-driven) is simpler, more context-frugal and less risky than a young, bulky all-in-one system.

## Source
- Repo: https://github.com/affaan-m/ECC (MIT license, JavaScript) · Pricing: https://ecc.tools/pricing · AgentShield: https://github.com/affaan-m/agentshield
- Stats & code verified via the GitHub API and file reading (`src/llm/providers/`, `.cursor/hooks/`, `SPONSORING.md`, README).

*(verified on 2026-06-24 — GitHub API + code reading + README)*
