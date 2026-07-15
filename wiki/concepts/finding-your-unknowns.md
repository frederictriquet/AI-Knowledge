---
title: "Finding your unknowns: the map–territory gap in agentic coding"
type: "Concept"
theme: prompting
level: 🔴
source_url: https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns
source_title: "A field guide to Claude Fable 5: Finding your unknowns — Thariq Shihipar (Anthropic)"
objectives: [code-generation]
---

# Finding your unknowns: the map–territory gap in agentic coding

**In one sentence** — With a strong enough model, work quality is no longer bottlenecked by the model but by your ability to surface and clarify your *unknowns* — the gap between the "map" (your prompts and context) and the "territory" (the codebase and its real constraints).

## What the source says
Thariq Shihipar (Anthropic) frames agentic coding around a **map vs territory** distinction: the map is what you give Claude (prompts, skills, context); the territory is where the work actually happens. Their gap is what he calls **unknowns** — each one forces the agent to *guess* your intent, and more work means more unknowns. He classifies them with Rumsfeld's 2×2: **known knowns** (what's in your prompt), **known unknowns** (what you know you haven't figured out), **unknown knowns** (the obvious-but-unwritten you'd recognize on sight), **unknown unknowns** (never considered). Thesis: *"reducing and planning for your unknowns is the **skill** of agentic coding"* — a skill you improve by working with Claude. Instructing is a balance: too **specific** → the agent won't pivot when it should; too **vague** → it falls back on generic best practices that may not fit.

He catalogs prompting patterns to surface unknowns across three phases:
- **Pre-implementation** — *Blind spot pass* (literally ask for a "blind spot pass" on your "unknown unknowns", giving your background); *Brainstorms & prototypes* (cheap ways to flush out *unknown knowns* early — e.g. "4 wildly different design directions" as an HTML mock to react to); *Interviews* ("interview me one question at a time… prioritize questions where my answer would change the architecture"); *References* (the best reference is **source code**, not a screenshot); *Implementation plan* (lead with the decisions most likely to change — data models, type interfaces, UX flows — bury mechanical refactors).
- **During** — *Implementation notes*: start a **fresh session** with the planning artifacts, and have the agent keep an `implementation-notes.md` logging any **"Deviations"** from the plan (pick the conservative option, log it, keep going).
- **Post** — *Pitches & explainers* (one doc to get buy-in); *Quizzes* (Claude quizzes you on the diff — *"I only merge after I pass the quiz perfectly"*).

## Why it matters
It reframes prompt quality as **unknown-management** and gives a concrete, phase-structured playbook with real example prompts. The economic logic is sound: surfacing unknowns via cheap artifacts (brainstorms, prototypes, references) costs far less *in rework* than discovering them mid-implementation, where small spec changes cascade into code that is hard to revert. The quiz-before-merge ritual directly targets comprehension debt, and "fresh session + passed artifacts" is good context hygiene.

## Limits & blind spots (critical read)
- **Token cost is entirely ignored.** The method *multiplies* token spend: blind-spot passes, multiple design variations, prototypes, interviews, HTML reports, quizzes, and fresh sessions that reload the artifacts. The article's "cheap" means **human time / avoided rework, not tokens**; the net token-vs-value trade-off is asserted, never measured. Budget the discovery artifacts explicitly.
- **Marketing framing**: this is a Fable 5 launch companion. "The first model where quality is bottlenecked by my ability to clarify unknowns" is a self-serving, unfalsifiable capability claim.
- **n=1, no evaluation**: a single author's anecdote (a launch video), no comparison or metric. The "ideal" operators cited (Boris, Jarred) are experts — a novice may not tell "good" from "bad" even after a blind-spot pass.
- The 2×2 is **borrowed from Rumsfeld**; the contribution is the *application* (which the article doesn't hide).

## Takeaways
- With a strong model, the lever is **surfacing your unknowns**, not more raw prompting.
- Four unknowns: known-knowns / known-unknowns / **unknown-knowns** (prototype to flush them early) / **unknown-unknowns** (blind spot pass).
- Discover cheap **before** implementation gets expensive; keep a **Deviations** log during; **quiz yourself before merging** (anti-comprehension-debt).
- Mind the **token bill**: the source's "cheap" is human time, not tokens — the discovery artifacts are not free.

## See also
- [Agentic code review: from writing to verification](agentic-code-review.md)
- [Comprehension debt & cognitive surrender](comprehension-debt.md)
- [Loop engineering: designing the system that prompts the agent](loop-engineering.md)
- [Human-in-the-loop: static vs dynamic interrupts](human-in-the-loop-static-dynamic.md)
