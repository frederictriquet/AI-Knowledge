---
type: index
title: "Theme — Prompting"
theme: prompting
---

# ✍️ Prompting

> ⚙️ **Generated file** by `tools/build_index.py` — do not edit by hand.

_Crafting and optimizing prompts (techniques, in-context learning)._

## Concepts (22)

### 🔴 Substance / core
- **[Decomposition techniques](../concepts/decomposition-techniques.md)** — explicitly break a complex problem into simpler sub-problems, then solve them one by one, to make the final answer more reliable.
- **[Directional Stimulus Prompting (DSP)](../concepts/directional-stimulus-prompting.md)** — train a small policy model that generates, per instance, stimuli (keywords, hints) steering a large frozen black-box LLM — you optimise the policy model, never the LLM.
- **[Ensembling techniques](../concepts/ensembling-techniques.md)** — Solve the same problem through several prompts/reasoning paths, then aggregate the outputs (often by majority vote) to reduce variance, at the cost of N calls.
- **[ICL: exemplar selection & zero-shot techniques](../concepts/icl-exemplar-and-zero-shot.md)** — In few-shot, the choice of examples, their order and their quantity matter as much as the prompt content; in zero-shot, several simple rephrasings of the instruction are enough to improve the output.
- **[In-context learning (ICL)](../concepts/in-context-learning.md)** — an LLM's ability to learn a task from the demonstrations placed in its prompt, with no update to its weights.
- **[Integrated prompt environments — give prompts to domain experts](../concepts/integrated-prompt-environments.md)** — prompts "are just English": the most effective teams give domain experts the tools to write and iterate on prompts **directly**, in the context of the application, instead of routing their expertise through engineers.
- **[Prompt engineering is empirical (case study)](../concepts/prompt-engineering-is-empirical.md)** — a real case study (detecting "entrapment" in suicide-risk texts) shows that prompt engineering is an iterative, sensitive, and poorly transferable process, where even reputed techniques do not always win.
- **[Prompt tuning (soft prompts)](../concepts/prompt-tuning.md)** — a PEFT method that trains, by gradient descent, a small set of continuous vectors ("soft prompts" / virtual tokens) injected at the input, with the backbone kept frozen — not to be confused with textual prompt engineering.
- **[Self-criticism techniques](../concepts/self-criticism-techniques.md)** — have the model evaluate, verify and correct its own output, looping if needed, to make the answer more reliable without human intervention.

### 🟡 Tradeoff / intermediate
- **[Automatic Prompt Engineer (APE) & automatic prompt design](../concepts/automatic-prompt-engineer-ape.md)** — a prompt is not a text to write by hand but an object to optimize: you have the LLM generate candidate instructions, then keep the best one according to a measurable scoring function.
- **[Decomposition-first vs interleaved](../concepts/decomposition-first-vs-interleaved.md)** — plan everything up front then execute without re-reasoning (ReWOO) versus planning and revising at every observation (ReAct).
- **[Meta-prompting](../concepts/meta-prompting.md)** — give the LLM a reusable reasoning template for a class of tasks (structure and steps), rather than a throwaway prompt for a single case.
- **[Prompt caching](../concepts/prompt-caching.md)** — reusing an already-computed response for an identical prompt, but beware: the tutorial implements an exact-match response cache on the client side (LangChain `SQLiteCache`), not provider-side prefix prompt caching (KV-cache).
- **[Prompt chaining](../concepts/prompt-chaining.md)** — breaking a complex task into a sequence of simple prompts where the output of each step feeds the next.
- **[Prompt optimization](../concepts/prompt-optimization.md)** — automatically (or semi-automatically) refining existing prompts through iteration, metric-based evaluation, and feedback loops, to be distinguished from manual prompt engineering, which designs them from scratch.
- **[Taxonomy of prompting techniques (The Prompt Report)](../concepts/prompting-techniques-taxonomy.md)** — the systematic, sourced version of the prompting catalog: ~58 text-based techniques classified into 5 families (ICL, Thought Generation, Decomposition, Ensembling, Self-Criticism), each attributed to its originating paper.

### 🟢 Overview / introductory
- **[Catalog of prompting techniques](../concepts/techniques-catalog.md)** — an index of prompt-structuring strategies, applied to a single task ("explain climate change") to compare their behaviors.
- **[Few-shot prompting](../concepts/few-shot-prompting.md)** — provide a few labeled examples in the prompt to guide the model, leveraging its pretrained knowledge without retraining.
- **[One-shot prompting](../concepts/one-shot-prompting.md)** — give the model a single well-crafted example so it generalizes a task, halfway between zero-shot and few-shot.
- **[Role prompting (persona)](../concepts/role-prompting.md)** — assign the model an explicit role or persona ("You are a compassionate veterinarian…") to steer the tone, style and behavior of the response.
- **[What is prompt engineering](../concepts/prompt-engineering.md)** — the discipline of designing and iteratively refining the text instructions given to an LLM to steer its output.
- **[Zero-shot prompting](../concepts/zero-shot-prompting.md)** — asking an LLM to perform a task without providing any example, relying solely on its pre-trained knowledge.

## Tools (3)

- **[GitHub Spec Kit](../tools/spec-kit.md)** — _CLI toolkit (spec-driven development)_
- **[GSD (Get Shit Done)](../tools/gsd.md)** — _Meta-prompting / spec-driven development framework for coding agents (a layer on top of Claude Code & others)_
- **[Ponytail](../tools/ponytail.md)** — _Skill / Plugin (multi-agent)_
