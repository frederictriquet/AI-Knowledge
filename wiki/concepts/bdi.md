---
title: "BDI architecture (Belief-Desire-Intention)"
type: "Concept"
theme: agent-fundamentals
level: 🟡
source_url: https://www.ibm.com/think/topics/agentic-architecture
source_title: "What is an agentic architecture?"
---

# BDI architecture (Belief-Desire-Intention)

**In one sentence** — a breakdown of an agent's reasoning into three registers (what it knows, what it wants, what it decides to do), predating LLMs.

## In detail
The BDI architecture is a model (or framework) designed to model rational decision-making in intelligent agents, based on the belief-desire-intention framework. It models human reasoning from three components: **Beliefs (B)**, the agent's knowledge about the world and sensory data ("The door is closed."); **Desires (D)**, top-level goals or objectives, which are not necessarily actions ("I want to enter the room."); **Intentions (I)**, the plan of action the agent actively commits to while accounting for its beliefs and desires ("I will open the door to enter."). BDI is placed among cognitive architectures, considered the most advanced type of agentic architecture.

## Example
The course of human reasoning modeled by the source, register by register. **Belief (B)** — raw sensory data: "The door is closed." **Desire (D)** — a top-level goal, which is not yet an action: "I want to enter the room." **Intention (I)** — the committed plan, derived by confronting beliefs and desires: "I will open the door to enter." The key point is this D→I derivation: a desire remains an abstract goal as long as no intention attaches to it, and once the intention is taken the agent persists in it rather than revising it at each new perception — hence the plan stability that distinguishes BDI from a reactive loop.

## Tradeoff / insight (for a senior)
The tradeoff: BDI explicitly separates goals (desires) from the committed plan (intentions), which prevents an agent from changing its goal at each new perception — it "persists" in an intention. This is a response to the problem of plan stability in a changing environment, a problem that naive ReAct loops handle poorly. A pre-LLM model (1990s, Rao & Georgeff) recycled as a reading grid for modern agents.

## Primary source
Bandura A., "Social cognitive theory: an agentic perspective", *Annual Review of Psychology* 2001;52:1-26, doi:10.1146/annurev.psych.52.1.1 — which grounds the notion of agency, not the BDI formalism itself (due to Rao & Georgeff).

## See also
- [Reactive / deliberative / cognitive architectures](reactive-deliberative-cognitive-architectures.md)
- [Taxonomy of the 5 agent types](five-agent-types-taxonomy.md)
