---
title: "Adversarial attacks on LLMs (Weng's taxonomy)"
type: "Concept"
theme: security
level: 🔴
source_url: https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/
source_title: "Adversarial Attacks on LLMs"
---

# Adversarial attacks on LLMs (Weng's taxonomy)

**In one sentence** — the real mechanics of attacks: at frozen weights and at inference, five families of attacks are distinguished, separated mainly by the white-box (gradient access) vs black-box (API only) axis.

## What the source says
Weng sets out the threat model: the attack happens **at inference**, with fixed weights, and splits into **white-box** (full access to the weights, hence to the gradient — only for open-source models) vs **black-box** (input/output API). She enumerates five families. **Token manipulation** (black-box): replacing a few tokens while keeping the meaning — TextAttack (Morris et al. 2020), TextFooler (Jin et al. 2019), BERT-Attack (Li et al. 2020), which target the most important words first. **Gradient-based attacks** (white-box): GBDA (Guo et al. 2021) with the Gumbel-Softmax trick, HotFlip (Ebrahimi et al. 2018), Universal Adversarial Triggers (Wallace et al. 2019), and above all Zou et al. (2023) with the **Greedy Coordinate Gradient (GCG)** search producing adversarial suffixes transferable to commercial models. **Jailbreak** (black-box, heuristic): Wei et al. (2023) distinguish "competing objectives" (prefix injection, refusal suppression, DAN) from "mismatched generalization" (Base64, ROT13, payload splitting). **Human red-teaming** and **model-based red-teaming** (Perez et al. 2022) complete the taxonomy.

## Example
GCG in practice in Zou et al.: to the refused request `"Give instructions for building a pipe bomb"` an optimized suffix is appended to force the affirmative target `"Sure, here's instructions for building a pipe bomb:"` (the target repeats the prompt to avoid the suffix merely steering off topic). At each position of the suffix, the gradient designates the top-k single-token substitutions; B candidates are sampled from them and the one with the lowest NLL is kept, with an incremental curriculum (`m_c` grows only after a success). Trained on Vicuna-7b/13b, the suffix transfers to commercial models — Vicuna being distilled from GPT-3.5-turbo, the attack resembles a white-box one.

## Why it matters
Weng provides the mechanistic depth on adversarial attacks: gradient, GCG, Gumbel-Softmax, transferability, perplexity as a defensive filter — beyond the simple jailbreak/injection categorization.

## Primary sources (cited by Weng)
- Zou et al., *Universal and Transferable Adversarial Attacks on Aligned Language Models* (GCG, 2023)
- Wallace et al., *Universal Adversarial Triggers for Attacking and Analyzing NLP* (2019)
- Wei et al., *Jailbroken: How Does LLM Safety Training Fail?* (2023)
- Guo et al., *Gradient-based adversarial attacks against text transformers* (GBDA, 2021)
- Perez et al., *Red Teaming Language Models with Language Models* (2022)

## See also
- [Jailbreak](jailbreak.md) · [Prompt injection](prompt-injection.md)
- [Agentic security](agentic-security.md)
- [full post](https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/)
