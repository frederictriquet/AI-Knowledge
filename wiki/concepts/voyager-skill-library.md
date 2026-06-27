---
title: "Voyager & skill library"
type: "Concept"
theme: tools-function-calling
level: 🔴
source_url: https://arxiv.org/abs/2305.16291
migrated_from: voyager-skill-library
---

# Voyager & skill library

**In one sentence** — a continually-learning agent that **acquires, stores and reuses** skills as code, building itself a self-constructed procedural memory.

## The idea
Voyager explores an open world (demonstrated on Minecraft) with no fixed objective. When it solves a task, it writes the solution as a **reusable function (skill)** and archives it in an indexed *skill library*. For a new task, it **retrieves** the relevant skills and composes them, instead of starting from scratch. An automatic curriculum loop proposes increasingly challenging objectives, and a self-verification mechanism corrects faulty code. The agent thus **accumulates** increasingly complex capabilities over time.

## Example
The skill library stores executable functions like `craftStoneShovel()` or `combatZombieWithSword()`, indexed by description embedding for retrieval. In 160 iterations, Voyager discovers 63 unique items (3.3× more than AutoGPT/ReAct/Reflexion) and unlocks wooden tools 15.3× faster. Above all, it is the only one to reach the diamond (baselines 0/3) and generalizes in zero-shot to a fresh world (diamond pickaxe in 19±3 iterations).

## Tradeoff / when to use it
Relevant for long-term agents in repetitive environments where you want to **capitalize** rather than relearn. Downside: it requires an executable and verifiable environment; the library can accumulate obsolete or poor-quality skills without curation.

## Primary source
Wang et al., 2023, *Voyager: An Open-Ended Embodied Agent with Large Language Models*, arXiv:2305.16291 *(arXiv verified — HTTP 200 + title)*.

## See also
- [learning-agent](learning-agent.md)
- [codeact](codeact.md)
