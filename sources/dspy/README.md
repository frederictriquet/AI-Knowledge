# DSPy — base de connaissances (source externe)

Papier fondateur **DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines** (Khattab et al., 2023), pour approfondir le « programmer, pas prompter » au-delà du glossaire IBM.

| # | Document | Mots | Source |
|---|---|---|---|
| 1 | [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](md/dspy-paper.md) | 25872 | [arXiv:2310.03714](https://arxiv.org/abs/2310.03714) |

> Note de sourcing : le rendu HTML natif d'arXiv (`arxiv.org/html/2310.03714`) renvoie « No HTML / not available » (404, ~11 ko) pour toutes les versions. Extraction réalisée depuis le miroir **ar5iv** (`ar5iv.labs.arxiv.org/html/2310.03714`, 200, 123 ko), via `extract_generic.py` (selector `article`). La source canonique citée reste `arxiv.org/abs/2310.03714`.

## Fiches de synthèse (ce que DSPy ajoute vs IBM)

Cross-linkées vers la base [`prompt-engineering`](../ibm-guide-prompt-engineering/).

- 🔴 [DSPy : signatures, modules, optimiseurs](../../fiches/dspy-signatures-modules-optimiseurs.md) — les trois abstractions cœur (signatures déclaratives typées, modules paramétrés type ChainOfThought/ReAct, teleprompters).
- 🔴 [DSPy : compilation & bootstrapping](../../fiches/dspy-compilation-bootstrap.md) — mécanique du compilateur en trois étapes, BootstrapFewShot, et résultats chiffrés (GSM8K, HotPotQA, T5-770M).
