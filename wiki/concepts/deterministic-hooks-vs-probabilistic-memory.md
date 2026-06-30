---
title: "Deterministic hooks vs probabilistic memory (Skills / Memory / Hooks)"
type: "Concept"
theme: governance-alignment-ops
level: 🟡
source_url: https://code.claude.com/docs/en/memory
source_title: "Claude Code Docs — How Claude remembers your project (memory) & Automate actions with hooks"
objectives: [code-generation]
---

# Deterministic hooks vs probabilistic memory (Skills / Memory / Hooks)

**In one sentence** — For a coding agent to honor a rule, the mechanism matters more than the wording: an instruction in memory (CLAUDE.md) is **probabilistic context** the model *may* follow, whereas a **hook** is a shell command run deterministically at a lifecycle point, which *guarantees* the action whatever the model decides — hence the triad "Skills = advice, Memory = reminder, Hooks = law".

## In detail
The Claude Code docs distinguish three levers to steer an agent, by **increasing strength of commitment**:

- **Skills** (`SKILL.md`) — *advice loaded on demand.* "Claude uses skills when relevant, or you can invoke one directly with `/skill-name`"; above all "a skill's body loads only when it's used": the procedure costs context only when it serves. This is *optional* capability, triggered by the model's judgment (or explicitly by the human).
- **Memory / CLAUDE.md** — *reminder.* Loaded at the start of each session, but "Claude treats [it] as context, not enforced configuration": delivered "as a user message after the system prompt (…) there's no guarantee of strict compliance, especially for vague or conflicting instructions". Memory *inclines* behavior; it does not constrain it.
- **Hooks** — *law.* "Hooks are user-defined shell commands that execute at specific points in Claude Code's lifecycle. They provide **deterministic control** (…) ensuring certain actions **always happen rather than relying on the LLM to choose** to run them." A `PreToolUse` hook can **block** an action (e.g. editing a protected file, or "check Gmail before drafting an email"): "To block an action regardless of what Claude decides, use a PreToolUse hook instead."

The dividing line is the **nature of execution**, not the tone of the instruction: Skills and Memory go through the LLM (probabilistic, can be ignored under context drift); a Hook is an external program (deterministic, always applies). Operational corollary given by the docs: if an instruction *must* run at a precise moment (before every commit, after every edit), it does not go in CLAUDE.md — it is written as a hook.

## Tradeoff / insight
- **Don't write in memory what must be guaranteed.** Any high-stakes "always do X / never do Y" rule (security, secrets, protected branch, quality gate) entrusted to CLAUDE.md *will eventually* be violated — not through model negligence, but because the instruction is probabilistic by construction. Promote it to a hook. Conversely, putting in a hook what is a matter of taste (style, preferences) needlessly rigidifies things.
- **Context cost = a selection criterion, not only reliability.** CLAUDE.md is loaded *in full* every session and consumes tokens every turn (target < 200 lines); a Skill costs only on use; a Hook consumes **no** context token (it lives outside the model). So: a long, occasional procedure → Skill; a cross-cutting guarantee → Hook; a fact the model gets wrong without it → CLAUDE.md. Piling up "just in case" rules in CLAUDE.md degrades both cost *and* adherence ("Longer files (…) reduce adherence").
- **CLAUDE.md writing filter**: keep only what the model gets wrong without it (public knowledge — React, SQL… — is a waste of tokens). The counterintuitive part: the "obvious" style line is often the one the model already knows, and the obscure invariant you hesitate to keep is the only load-bearing line.
- **Guardrail ≠ alignment by prompt.** The hook is, on the coding-agent side, the embodiment of the [entry-node guardrail](entry-node-guardrail.md) principle and of the [Dual LLM pattern](dual-llm-pattern.md): security holds because it is *outside* the LLM, not because it was politely requested.

## See also
- [Loop engineering: designing the system that prompts the agent](loop-engineering.md)
- [Entry-node guardrail (Granite Guardian)](entry-node-guardrail.md)
- [The Dual LLM pattern](dual-llm-pattern.md)
- [Human-in-the-loop: static vs dynamic interrupts](human-in-the-loop-static-dynamic.md)
- [LLM Wiki: a wiki maintained by the LLM rather than RAG](llm-wiki-karpathy.md)
