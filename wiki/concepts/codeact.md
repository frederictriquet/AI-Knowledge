---
title: "CodeAct (code as action space)"
type: "Concept"
theme: tools-function-calling
tags: [tools, code, agents]
level: 🔴
source_url: https://arxiv.org/abs/2402.01030
source_title: "Executable Code Actions Elicit Better LLM Agents — Wang et al., 2024"
primary_source: "PAL: Program-aided Language Models, Gao et al. (arXiv:2211.10435)"
objectives: [code-generation]
migrated_from: codeact
---

# CodeAct (code as action space)

**In one sentence** — the agent emits **executable Python code** as its action, instead of rigid JSON tool calls.

## The idea
In classic function calling, each action is a structured call (name + JSON arguments), one per turn. CodeAct unifies the action space into a single abstraction: **code**. The agent writes a Python snippet that can chain several tools, use loops, conditionals, intermediate variables and compose results, then the environment executes it and returns the output (including errors) for the next iteration. Wang et al. show that this format improves the success rate over JSON, because it leverages LLMs' massive familiarity with code.

## Example
Figure 1 of the paper: to apply the same tool chain to N inputs, the CodeAct agent emits a single action — a Python `for`-loop that passes one tool's output into the next via variables — where JSON/text require one call per input. On M3ToolEval (**82 curated multi-tool tasks**), gpt-4-1106 reaches **74.4% success in CodeAct against 52.4% in JSON and 53.7% in text**, in ~28% fewer turns (5.5 vs 7.7). The open CodeActAgent model is fine-tuned on CodeActInstruct, **7,139 multi-turn trajectories** (HotpotQA, MATH, ALFWorld...) starting from Llama-2-7B and Mistral-7B.

## Tradeoff / when to use it
Ideal for multi-tool tasks where **composition** matters (data, orchestration). The flip side: it requires a **sandboxed interpreter** and management of the risk of arbitrary code execution; debugging and guardrails are heavier than with constrained JSON.

## Ancestor — PAL (Program-Aided Language models)
Before making code the full **action space** of an agent, PAL (Gao et al., 2022) established the founding reflex on reasoning alone: on arithmetic/logic tasks, the LLM errs at **execution** even when the reasoning is correct, so it is made to **translate** the problem into a program (often Python) and delegate the computation to an **interpreter** for an exact answer. An almost identical variant: Program of Thoughts (PoT, Chen et al., 2022). Transferable principle: as soon as a step is deterministic (maths, dates, data manipulation), delegate it to executed code, not to the model. CodeAct generalises this reflex from a one-off sub-computation to the **whole set** of an agent's actions.

## Primary source
Wang et al., 2024, *Executable Code Actions Elicit Better LLM Agents*, arXiv:2402.01030 *(arXiv verified — HTTP 200 + title)*. Ancestor: Gao et al., 2022, *PAL: Program-aided Language Models*, arXiv:2211.10435; Chen et al., 2022, *Program of Thoughts (PoT)* *(arXiv verified — HTTP 200 + title)*.

## See also
- [computer-use-gui-agents](computer-use-gui-agents.md)
- [tool-calling](tool-calling.md)
- [tool-grounding](tool-grounding.md)
- [chain-of-thought](chain-of-thought.md)
