---
tool: "GSD (Get Shit Done)"
title: "GSD (Get Shit Done)"
themes: [prompting]
type: "Meta-prompting / spec-driven development framework for coding agents (a layer on top of Claude Code & others)"
url: https://github.com/open-gsd/gsd-core
pricing_model: "Open-source (MIT), free — ⚠️ original creator (TÂCHES) tied to a crypto rug-pull; use the community continuation open-gsd"
llm_cost: "Built-in (🟢) — runs INSIDE your existing agent (Claude Code, Gemini CLI, Codex…), no dedicated LLM API key required; cost = that of your client"
objectives: [code-generation]
family: "Workflow, methodology & spec-driven development"
eco_icons: "🔓"
llm_cost_icons: "🟢"
summary: "Open-source (MIT) task-based spec-driven dev framework: fights context degradation by spawning fresh-context sub-agents; BYOK. **⚠️ Original creator (TÂCHES) tied to a $GSD crypto rug-pull + original npm packages abandoned → only use the community continuation `open-gsd` (see page)**"
---

# GSD (Get Shit Done)

> ## ⚠️ WARNING — read before installing
> According to several community and press sources (Reddit r/ClaudeAI, AI Weekly, Skool "security heads-up"), GSD's **original creator** — **TÂCHES / Lex Christopherson** — is associated with a **rug pull** on a crypto token **$GSD** (≈ May 2026): value drained, social accounts deleted, creator gone unreachable.
> - **Concrete risk = supply chain**: the **original npm packages remain published with no maintainer**. A future flaw or compromise would be fixed by no one. Experts recommend **uninstalling / avoiding the original packages**.
> - **The code itself** (MIT) is not accused of containing malware: the issue is the **abandonment** + the **dubious crypto history** of the original maintainer (reputation, longevity, trust).
> - ✅ **Safe path**: the **community continuation** under the **`open-gsd`** organization (launched as *get-shit-done-redux*, a bit-for-bit MIT mirror **with no reference to the token**, community security audit; current canonical repo **`open-gsd/gsd-core`**, install `npx @opengsd/gsd-core@latest`).
>
> *(rug pull = a scam where a project/token promoter abruptly withdraws the funds and disappears. Warning based on community/press reports — not confirmed by a judicial source; the original repo's official redirect does not mention the affair.)*

**In one sentence** — Open-source meta-prompting and spec-driven development system that fights the "context rot" of coding agents by having thin orchestrators spawn fresh-context sub-agents (clean ~200K windows) for each significant operation.

## Type & integration
It is not an autonomous agent nor a hosted product: it is a **method / framework layer** (installed via `npx @opengsd/gsd-core@latest`, a Node.js package) that installs on top of an existing coding agent. Multi-runtime: Claude Code, OpenCode, Gemini CLI, Kimi CLI, Kilo, Codex, GitHub Copilot, Cursor, Windsurf, and others (the docs mention ~14 runtimes). It structures work along a phase loop (discuss → plan → execute → verify → ship) and about 15 specialized agents (research, planning, execution, verification). The orchestrators stay thin (10-15% of context) and delegate to disposable sub-agents; state is persisted in file artifacts (e.g. `STATE.md`, `CONTEXT.md`) recombined via git commits.

## Pricing model
**Open-source project under the MIT license**, free. Created by the developer **TÂCHES**, launched in December 2025, very popular (the historical repo `gsd-build/get-shit-done` exceeded ~64k★ before migration). No resale, no subscription of the framework's own. ⚠️ But **trust model compromised**: parallel monetization via a **$GSD crypto token** whose creator allegedly rug-pulled (see warning at the top). The **`open-gsd`** continuation has stayed purely open-source, with no token.

## LLM cost
**Built-in 🟢 — no dedicated LLM API key** (verified: 0 mention of a key/BYOK in the README). GSD is a Markdown meta-prompting framework that **drives the agent you already use**; the token cost is that of your runtime (Claude Code subscription, Gemini access, etc.), via **that client**, with no key of GSD's own. Note: the architecture multiplies fresh-context sub-agents, which can increase total token consumption in exchange for better quality maintained over long sessions.

## What it's for
Maintaining code-generation quality over long sessions by avoiding "context rot" (shortening responses, forgotten instructions, incoherent code as the window fills up). GSD breaks work into atomic plans, runs each in a clean-context sub-agent, keeps the main session around 30-40% occupancy, and recombines the results. Target: spec-driven development, structured research/planning/verification rather than a monolithic prompt.

## Notes
- **⚠️ Name clash resolved**: "GSD" is a common acronym. The right tool is indeed **Get Shit Done by TÂCHES** (spec-driven framework for coding agents), not to be confused with other "GSD" (e.g. "Git. Ship. Done", getting-things-done-style task managers, etc.).
- **⚠️ Repo migration — and the popularity stayed on the compromised repo**: the historical repo `gsd-build/get-shit-done` (~64k★, by TÂCHES) is **no longer the active home** and redirects to the canonical **`open-gsd/gsd-core`**. Yet this "safe" canonical repo only has **~5k★** (GitHub API, 2026-06-24): the ~64k★ that make "GSD"'s reputation belong to the rug-pulled repo, **not** the recommended lineage. To weigh heavily: you adopt a young, low-starred community fork, not the 64k★ phenomenon.
- **⚠️ The rug-pull affair (see warning at the top)**: distinguish two things — (1) the **technical migration** to `open-gsd`, which is clean; (2) the **$GSD crypto affair** of the original creator, which is exactly why you should **only use the `open-gsd` lineage** (no token, audited) and **avoid the original npm packages** left without a maintainer.
- Positioning vs [Liza](liza.md): in Liza's survey, GSD is presented as the archetype of "LLM orchestrators that delegate to sub-agents", as opposed to Liza's *Go-on-LLM* architecture where **deterministic** supervisors mechanically enforce guarantees that the agents cannot bypass. Liza also notes that *file-path passing* and plan-to-context sizing are common practices, not innovations specific to GSD.
- Conceptually comparable to other methodology overlays on agents (specs, sub-agents) — to cross-check with the other overlay/orchestrator pages.

## Source
- Canonical repo: https://github.com/open-gsd/gsd-core *(verified on 2026-06-15)*
- Historical repo (superseded, by TÂCHES, ~64k★): https://github.com/gsd-build/get-shit-done *(verified on 2026-06-15)*
- Liza survey: https://github.com/liza-mas/liza/tree/main/specs/architecture/competition-survey (mas-survey.md) *(verified on 2026-06-15)*
- ⚠️ **Rug-pull warning**: Reddit r/ClaudeAI (post "if you use the Get Shit Done (GSD) AI tool you need to…") — direct fetch blocked; AI Weekly "Get-Shit-Done creator rug-pulls $GSD token, vanishes" (aiweekly.co/alerts); "Security heads-up: the GSD tool" (skool.com/ai-automation-society) *(consulted via web search on 2026-06-15)*
- Articles: augmentcode.com/learn/gsd-58k-stars-claude-code ; dev.to (GSD guides) *(verified on 2026-06-15)*
