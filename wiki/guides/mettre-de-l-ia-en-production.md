---
type: guide
titre: "Mettre de l'IA en production"
objectif: mise-en-prod
description: "Parcours transverse : passer d'un prototype LLM à un système en production — architecture, RAG, robustesse, amélioration continue."
---

# 🚀 Mettre de l'IA en production

> **Guide par objectif (L3)** — comment passer d'un prototype LLM à un produit fiable en production ?
> Concepts/pratiques ci-dessous ; **outils** (RAG, frameworks, LLMOps, passerelles…) en **section Outils** en bas de page.

## En bref

Mettre un LLM en production, c'est moins une affaire de modèle que de **système** : choisir l'architecture (RAG vs fine-tuning vs prompt), garantir des **sorties exploitables**, encaisser les pannes (**résilience**), protéger l'utilisateur (**UX défensive**), et installer la **boucle d'amélioration** (évals + feedback + observabilité) qui fait progresser le produit.

## Parcours de lecture conseillé

1. **Cadrer l'architecture** — [Patterns pour systèmes LLM en production](../concepts/llm-system-patterns.md), [RAG vs fine-tuning vs prompt engineering](../concepts/rag-vs-fine-tuning-vs-prompt-engineering.md).
2. **RAG, si pertinent** — [RAG](../concepts/rag.md), [RAG agentique](../concepts/rag-agentique.md), [améliorer son RAG systématiquement](../concepts/systematically-improving-rag.md). Alternative à considérer : [LLM Wiki (Karpathy)](../concepts/llm-wiki-karpathy.md).
3. **Sorties exploitables** — [sorties structurées (instructor / Pydantic)](../concepts/structured-outputs-instructor.md).
4. **Encaisser les pannes** — [résilience & fallback LLM](../concepts/resilience-fallback-llm.md).
5. **Protéger l'utilisateur** — [UX défensive pour produits LLM](../concepts/defensive-ux-for-llm.md).
6. **Installer la boucle d'amélioration** — [eval-driven development](../concepts/eval-driven-development.md), [data flywheel](../concepts/data-flywheel-feedback.md), [observabilité LLM](../concepts/llm-observability-best-practices.md).

## Toutes les fiches de cet objectif

<!-- AUTO:objectif=mise-en-prod -->
> ⚙️ **Generated index** — 0 fiche(s) taguée(s) `objectives: [mise-en-prod]`, régénéré par `tools/build_index.py`. La prose ci-dessus est curée à la main.
<!-- /AUTO -->

## Outils pour cet objectif

<!-- AUTO-OUTILS:objectif=mise-en-prod -->
> _(aucun outil rattaché à cet objectif pour l'instant)_
<!-- /AUTO-OUTILS -->
