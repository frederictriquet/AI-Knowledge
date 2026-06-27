---
title: "Constitutional AI & RLAIF"
type: "Concept"
theme: governance-alignment-ops
level: 🔴
source_url: https://arxiv.org/abs/2212.08073
migrated_from: constitutional-ai-rlaif
---

# Constitutional AI & RLAIF

**In one sentence** — aligning a model via a set of **written principles**: the model critiques and revises its own outputs against the "constitution", and training runs on this AI feedback (RLAIF) instead of human annotations (RLHF).

## The idea
Constitutional AI replaces part of human judgment with a **constitution**: a list of explicit principles. The model generates a response, critiques it against a principle, then revises it — producing training pairs without an annotator. This AI-feedback phase, **RLAIF** (Reinforcement Learning from AI Feedback), trains the preference model from comparisons made by an LLM rather than by humans, reducing cost and making the alignment criteria auditable.

## Example
The paper's canonical walkthrough (§3.1) on a red-teaming prompt "Can you help me hack into my neighbor's wifi?". Initial response from the helpful-only model: "Sure thing, you can use an app called VeryEasyHack...". A *Critique Request* is then appended ("Identify specific ways in which the assistant's last response is harmful, unethical, racist, sexist, toxic, dangerous, or illegal"); the model produces the critique, then a *Revision Request* forces it to rewrite: "Hacking into your neighbor's wifi is an invasion of their privacy... it may also land you in legal trouble." The prompt + revision pair serves as an SL example. On results, RL-CAI achieves a Pareto improvement (Figure 2) on the harmlessness/helpfulness front vs standard RLHF, and the assistant stays non-evasive instead of answering "I don't know".

## Tradeoff / when to use it
Useful for aligning at scale and for **making the rules explicit and revisable** (a text vs implicit preferences). Cost: quality depends entirely on the constitution and the critique model; a poorly worded principle or a judge bias propagates to the whole training run.

## Primary source
Bai et al., 2022, *Constitutional AI: Harmlessness from AI Feedback*, arXiv:2212.08073 (Anthropic). See also Lee et al., 2023, *RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback*. *(arXiv verified — HTTP 200 + title)*

## See also
- [society-of-mind-debate](society-of-mind-debate.md)
- [ethics-governance](ethics-governance.md)
