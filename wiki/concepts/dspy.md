---
title: "DSPy"
type: "Concept"
theme: governance-alignment-ops
level: 🔴
source_url: https://www.ibm.com/think/topics/dspy
source_title: "What is DSPy?"
---

# DSPy

**In one sentence** — "programming, not prompting": you declare signatures and modules in Python, and optimisers automatically compile the prompts against a metric, instead of writing and tinkering with them by hand.

## In detail
DSPy (open-source Python toolkit, StanfordNLP) replaces prompt hacking with a programmatic approach. Key vocabulary it exposes: **Signature** (a class defining a module's input/output types, e.g. question → reasoning + answer), **Module**, **Compilation** (translating the Python program into executable prompts, which updates the internal parameters: LM weights, instructions, demonstrations), **Optimiser** (formerly "teleprompter", e.g. BootstrapFewShot, BootstrapFewShotWithRandomSearch, BootstrapFinetune, LabeledFewShot), **Pipeline** and **Metrics** (exact match, semantic F1, custom metrics). The process resembles an evolutionary algorithm: DSPy has the LLM generate prompts, tests them against a metric, and rejects those that do not improve. A tutorial builds a RAG on watsonx (Llama 3 + ColBERTv2, HotPotQA dataset, dspy.ChainOfThought, BootstrapFewShot): the compiled version corrects a wrong answer ("France" → "Turkey, Orhan Pamuk"). Guidelines: BootstrapFewShot for ~10 examples, RandomSearch beyond 50, Finetune for performance.

## Example
A multi-hop HotPotQA-style question: "In what year did Bill Nelson first fly as a payload specialist aboard a space shuttle?" A single query is not enough: you must first retrieve that Nelson flew on Columbia, then that Columbia flew in 1981. You declare the signature `class GenerateAnswer(dspy.Signature): context = dspy.InputField(desc="may contain relevant facts"); question = dspy.InputField(); answer = dspy.OutputField(desc="often between 1 and 5 words")` — and compilation by `BootstrapFewShot` builds the few-shot demonstrations on its own, without writing a single text prompt.

## Tradeoff / insight
DSPy treats the prompt as a compiled artifact, decoupled from the underlying model: switching LLM or data → recompile, instead of rewriting fragile prompt chains. Cost: the framework's learning curve, the need for a reliable training set and metric, and the opacity of the generated prompts (to be inspected via inspect_history). The auto-generated optimisation can overfit the trainset.

## Primary source
The [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) repository (open source, documentation and tutorials); HotPotQA dataset ([hotpotqa.github.io](https://hotpotqa.github.io/)).

## See also
- [Prompt optimization](prompt-optimization.md)
- [In-context learning](in-context-learning.md)
