---
title: "Agent & LLM benchmarks (reference)"
type: "Concept"
theme: benchmarks
level: 🟡
source_url: https://arxiv.org/abs/2310.06770
migrated_from: benchmarks-agents
---

# Agent & LLM benchmarks (reference)

**In one sentence** — four reference benchmarks (SWE-bench, τ-bench, GAIA, WebArena) that measure agents on realistic, long, tool-using tasks — and where, consistently, they remain far below human performance.

> Compiled from the source papers (links below).
> For each benchmark: what it measures, how, and the headline finding (scores reported faithfully).
>
> SOURCING NOTE: only WebArena had a complete arXiv HTML rendering (full excerpt). For SWE-bench, τ-bench and GAIA the arXiv HTML rendering was unavailable (404) or truncated; the findings below therefore come from the official abstract (and for those, only the figures present in the abstract are reported).

## SWE-bench

- **Measures**: a model's ability to resolve real software bugs/issues — actual software engineering as a testbed, well beyond plain code generation.
- **Method**: an evaluation framework of **2,294 software-engineering problems** drawn from real GitHub issues and their pull requests, across **12 popular Python repositories**. The model is given a codebase plus the description of an issue to resolve; it must edit the codebase to fix the problem. Resolving an issue often requires coordinating changes across several functions, classes and files, interacting with execution environments and handling extremely long contexts.
- **Finding**: state-of-the-art proprietary models, like the authors' fine-tuned model (SWE-Llama), only resolve the simplest issues. **The best model, Claude 2, resolves just 1.96% of issues.** (Figures from the original abstract; rankings have shifted substantially since.)
- Source: https://arxiv.org/abs/2310.06770

## τ-bench

- **Measures**: **agent–tool–user** interaction — an agent's ability to converse with a human user and follow domain-specific business rules (policy). Two dimensions ignored by classic benchmarks but vital in production.
- **Method**: dynamic conversations between a user (simulated by an LLM) and an agent equipped with **API tools** and **domain-specific policy guidelines**. Evaluation compares the **final database state** against an annotated target state (faithful, efficient evaluation). A new **pass^k** metric measures the **reliability** of behaviour across several trials.
- **Finding**: even state-of-the-art function-calling agents (such as gpt-4o) succeed on **fewer than 50% of tasks**, and are very **inconsistent**: **pass^8 < 25% in the retail domain**. The stated need is for agents able to act consistently and follow rules reliably.
- Source: https://arxiv.org/abs/2406.12045

## GAIA

- **Measures**: the capabilities of a **general AI assistant** — reasoning, multimodality, web browsing, and tool-use proficiency. Questions that are "conceptually simple for a human but difficult for AIs".
- **Method**: **466 real questions** with their answers. The answers to **300 of them** are kept secret to power a leaderboard. The philosophy reverses the benchmark trend: aim for tasks that are easy for humans rather than ever harder ones.
- **Finding**: **humans answer 92% of questions correctly, against 15% for GPT-4 equipped with plugins.** This gap contrasts with LLMs' tendency to surpass humans on expert tasks (law, chemistry). The authors posit that AGI depends on the ability to reach robustness comparable to the average human on such questions.
- Source: https://arxiv.org/abs/2311.12983

## WebArena

- **Measures**: the ability of language-guided agents to accomplish **realistic, long-horizon web tasks**, evaluated on the **functional correctness** of the result (not on surface similarity).
- **Method**: a **highly realistic and reproducible** web environment made of fully functional sites across **four domains** (e-commerce, social forum, collaborative software development, content management), enriched with tools (e.g. a map) and external knowledge bases (e.g. manuals, Wikipedia). The benchmark holds **812 tasks** (intents) instantiated from **241 templates** (on average 3.3 examples per template). The baseline agents tested integrate recent techniques such as "reason before acting".
- **Finding**: solving complex tasks remains hard. **The best GPT-4-based agent reaches only a 14.41% end-to-end success rate**, far from the **78.24% human performance** (GPT-3.5: 6.41%). A result that underscores the need for robust agents.
- Source: https://arxiv.org/abs/2307.13854

## Example
A typical SWE-bench instance (Figure 1 of the paper): a scikit-learn issue "data leak in GBDT due to warm start" + a snapshot of the `sklearn/` repo; the model must produce a patch editing `gradient_boosting.py` and `helper.py`, validated by the `fail-to-pass` tests (here `dstack_struct_col`, `matrix_transform`...). The figures in Table 1 capture the needle-in-a-haystack nature: average codebase of **3,010 files / 438K lines**, an issue of **195 words**, but a gold patch of only **32.8 lines across 1.7 files** — hence the need for a BM25 retriever (contexts exceed 100K tokens). Distribution dominated by django (850 tasks), sympy (386), scikit-learn (229).

## Cross-cutting summary

| Benchmark   | Domain                           | Tasks   | Best reported agent     | Human  |
|-------------|----------------------------------|---------|-------------------------|--------|
| SWE-bench   | Real GitHub bugs (code)          | 2,294   | Claude 2: 1.96%         | —      |
| τ-bench     | Agent–tool–user (rules)          | —       | gpt-4o: < 50%           | —      |
| GAIA        | General assistant                | 466     | GPT-4+plugins: 15%      | 92%    |
| WebArena    | Long-horizon web tasks           | 812     | GPT-4: 14.41%           | 78.24% |

The constant: on **realistic, long, tool-using** tasks, state-of-the-art agents remain **far below human performance** — that gap is the central message of each of these papers.

## See also

- [Trajectory evaluation](evaluation-trajectoire.md) · [Eval-driven development](eval-driven-development.md)
