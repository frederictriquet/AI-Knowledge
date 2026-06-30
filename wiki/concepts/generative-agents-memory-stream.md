---
title: "Generative Agents — memory stream"
type: "Concept"
theme: memory
level: 🔴
source_url: https://arxiv.org/abs/2304.03442
---

# Generative Agents — memory stream

**In one sentence** — a timestamped log of observations, re-read through a score combining **recency + importance + relevance**; the scoring function is the transferable idea for agent memory.

## The idea
Each agent keeps a *memory stream*: a chronological list of natural-language observations, each timestamped. To act, the agent does not re-read everything: it retrieves the most useful memories via a score combining **recency** (temporal decay), **importance** (rated by the model) and **relevance** (semantic similarity to the current situation). On top of this, a *reflection* mechanism periodically synthesizes memories into higher-level conclusions, themselves fed back into the stream.

## Example
The demo runs in Smallville, a Sims-like sandbox populated by 25 agents. From a single instruction given to one agent ("organize a Valentine's Day party"), social behaviors emerge without scripting: over two simulated days, agents spread the invitations through their network, form new relationships, plan dates around the event and coordinate their arrival to be present at the same time. This propagation is coded nowhere: it follows from the observation → planning → reflection loop applied to each agent's memory stream.

## Tradeoff / when to use it
The recency+importance+relevance scoring function is directly reusable for any **long-running agent memory**: it prioritizes better than a plain vector search. Cost: rating importance requires one LLM call per observation, and the stream grows indefinitely without compaction.

## Primary source
Park et al., 2023, *Generative Agents: Interactive Simulacra of Human Behavior*, arXiv:2304.03442 (Stanford). *(arXiv verified — HTTP 200 + title)*

## See also
- [memgpt](memgpt.md)
- [memoire-episodique-semantique-procedurale](episodic-semantic-procedural-memory.md)
