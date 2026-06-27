---
type: index
title: "Theme — Evaluation"
theme: evaluation
---

# 📊 Evaluation

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Measuring quality: evals, LLM judges, error analysis._

## Concepts (14)

### 🔴 Substance / core
- **[Agentic code review: from writing to verification](../concepts/agentic-code-review.md)** — When agents generate code faster than anyone can read it, the bottleneck moves from writing to **verification**: review becomes the highest-leverage skill, and the human shifts from "in the loop" to "on the loop".
- **[Data flywheel: collecting feedback](../concepts/data-flywheel-feedback.md)** — production data is the only durable asset of an LLM product: capturing user feedback (explicit and implicit) creates a *flywheel* that feeds evals, fine-tuning and guardrails alike — the competitive advantage that cannot be copied.
- **[Error analysis: look at your data](../concepts/error-analysis.md)** — Before any metric, manually read your product's traces, annotate undesirable behaviors, then build a taxonomy of failure modes and count their frequency.
- **[Eval-driven development](../concepts/eval-driven-development.md)** — Building an evaluation system specific to your domain is the foundation of an AI product: it creates the data → evals → improvement flywheel and unlocks everything else.
- **[Evaluating LLMs (task-specific evals)](../concepts/evaluating-llms.md)** — Off-the-shelf evals correlate poorly with application performance; Eugene proposes concrete evals, calibrated per task (classification, summarization, translation, toxicity), without ever giving up human evaluation.
- **[LLM-as-a-judge: doing it right](../concepts/llm-as-judge-correct.md)** — an LLM-as-a-judge is only valuable if it is aligned with the binary pass/fail judgment of a domain expert through an iterative protocol ("Critique Shadowing"), not through arbitrary 1-5 scores.
- **[Patterns for LLM systems in production](../concepts/llm-system-patterns.md)** — seven practical patterns to turn an LLM demo into a reliable product, organized along two axes: improve performance vs reduce cost/risk, and close to the data vs close to the user.
- **[Trajectory evaluation](../concepts/evaluation-trajectoire.md)** — evaluate the sequence of decisions, tool calls and intermediate steps the agent took, not just the quality of its final answer.

### 🟡 Tradeoff / intermediate
- **[Contextual Retrieval](../concepts/contextual-retrieval.md)** — prefix each chunk with a short context (situating the chunk in its document) *before* embedding, to reduce retrieval failures caused by ambiguous chunks.
- **[Heterogeneous reviewers: low overlap between tools](../concepts/heterogeneous-reviewers.md)** — AI code reviewers overlap very little: rather than hunting for "the best" tool, run several with complementary strengths, like an ensemble.
- **[LLM-as-a-judge](../concepts/llm-as-a-judge.md)** — using an LLM, guided by a rubric of criteria, to automatically score an agent's outputs when there is no ground truth to compare against.
- **[LLM-evaluators (LLM judges) — Eugene's view](../concepts/llm-evaluators.md)** — a synthesis of two dozen papers on LLM-as-a-Judge: when and how to use them, their known biases, and how to align them with human criteria.
- **[Tool retrieval (RAG over tools)](../concepts/tool-retrieval.md)** — when you have hundreds of tools, **dynamically retrieve** a relevant subset per query instead of exposing them all in the prompt.

### 🟢 Overview / introductory
- **[RAG (Retrieval-Augmented Generation)](../concepts/rag.md)** — instead of answering from its training memory alone, the LLM **retrieves relevant passages from an external store** and injects them into the context to ground its answer on sources.

## Tools (0)

- _(aucun)_
