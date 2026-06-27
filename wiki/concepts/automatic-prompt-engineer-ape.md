---
title: "Automatic Prompt Engineer (APE) & automatic prompt design"
type: "Concept"
theme: prompting
level: 🟡
source_url: https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/
source_title: "Prompt Engineering"
migrated_from: automatic-prompt-engineer-ape
---

# Automatic Prompt Engineer (APE) & automatic prompt design

**In one sentence** — a prompt is not a text to write by hand but an object to optimize: you have the LLM generate candidate instructions, then keep the best one according to a measurable scoring function.

## What the source says
Weng sets the frame: a prompt is a sequence of prefix tokens that increases the probability of the desired output, so it can be treated as optimizable parameters. On the embedding-space side, she cites AutoPrompt (Shin et al. 2020), Prefix-Tuning (Li & Liang 2021), P-tuning and Prompt-Tuning, noting a trend toward gradual simplification of the setup. **APE** (Automatic Prompt Engineer; Zhou et al. 2022) operates in natural language: (1) have the LLM generate candidate instructions from a few input-output pairs; (2) search for the instruction ρ that maximizes a scoring function f per sample, such as execution accuracy or log-probability; (3) refine through an iterative Monte Carlo search that proposes semantically close variants. Weng also cites Shum et al. (2023) — augment-prune-select — and Zhang et al. (2023) — clustering questions by k-means — to automatically build chain-of-thought prompts.

## Example
APE's bootstrapping prompts are literal. To generate the candidates, you condition on input-output pairs then end with `{{Given desired input-output pairs}}\n\nThe instruction is`: the LLM completes the instruction that would have produced these examples. For the Monte Carlo phase, the mutation prompt is `Generate a variation of the following instruction while keeping the semantic meaning.\n\nInput: ...\n\nOutput: ...`. The score f is typically execution accuracy `1[LM(·|ρ,x)=y]`, measurable without a human.

## Why it matters
Weng provides the founding formulation: the prompt as a variable of a search driven by an execution score — the theoretical basis for tooled approaches like DSPy.

## Primary sources (cited by Weng)
- Zhou et al., *Large Language Models Are Human-Level Prompt Engineers* (APE, ICLR 2023)
- Shin et al., *AutoPrompt* (2020)
- Shum et al., *Automatic Prompt Augmentation and Selection with CoT from Labeled Data* (2023)
- Zhang et al., *Automatic chain of thought prompting* (2022)

## See also
- [Prompt optimization](prompt-optimization.md) · [DSPy](dspy.md)
- [full post](../../sources/lilian-weng/md/2023-03-15-prompt-engineering.md)
