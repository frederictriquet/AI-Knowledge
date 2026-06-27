---
type: guide
titre: "Générer du code avec l'IA"
objectif: generer-code
description: "Parcours transverse : concepts et pratiques pour produire du code avec des agents IA, du cadrage à la vérification."
---

# 🧑‍💻 Générer du code avec l'IA

> **Guide par objectif (L3)** — un parcours transverse aux thèmes pour répondre à : *comment produire du code efficacement avec l'IA ?*
> Cette page réunit les **concepts/pratiques** (parcours ci-dessous) et les **outils** (section en bas de page).

## En bref

L'écriture de code n'est plus le goulot : l'agent en produit beaucoup, vite. Le travail se déplace vers **cadrer, orchestrer, et surtout vérifier**. Bien utiliser l'IA pour coder, c'est concevoir le **système** autour de l'agent (le contexte, la boucle, les garde-fous) et garder la **compréhension** de ce qui est produit — pas piloter chaque ligne.

## Parcours de lecture conseillé

1. **Changer de posture** — le centre de gravité passe de l'écriture à la vérification et au jugement. Commencer par [Revue de code agentique](../fiches/revue-de-code-agentique.md), puis la [Dette de compréhension](../fiches/dette-de-comprehension.md) (le risque à ne pas céder), et [Loop engineering](../fiches/loop-engineering.md) (concevoir le système plutôt que prompter à la main).
2. **Comprendre comment l'agent code** — [le cadre canonique de l'agent](../fiches/agent-architecture-canonique.md), [CodeAct](../fiches/codeact.md) (le code comme espace d'action), l'[interface agent-ordinateur (ACI)](../fiches/aci-agent-computer-interface.md) et le pattern [Deep Agents](../fiches/deep-agents.md).
3. **Cadrer & décomposer le travail** — choisir la bonne forme avec [workflows vs agents](../fiches/workflows-vs-agents.md) et les [patterns de workflow](../fiches/patterns-de-workflow.md), puis découper via les [techniques de décomposition](../fiches/decomposition-techniques.md) et le [prompt chaining](../fiches/prompt-chaining.md).
4. **Orchestrer plusieurs agents** — quand on passe à la flotte : [types d'orchestration](../fiches/orchestration-types.md) et [structures multi-agents](../fiches/structures-multi-agents.md).
5. **Vérifier & fiabiliser** — le cœur du métier désormais : [reviewers hétérogènes](../fiches/reviewers-heterogenes.md), [Chain-of-Verification](../fiches/chain-of-verification.md), [eval-driven development](../fiches/eval-driven-development.md), [Reflexion](../fiches/reflexion.md) et le [human-in-the-loop statique vs dynamique](../fiches/hitl-statique-dynamique.md).
6. **Garder le contrôle** — [hooks déterministes vs mémoire probabiliste](../fiches/hooks-deterministes-vs-memoire-probabiliste.md) pour ancrer les invariants hors du jugement du modèle.

## Toutes les fiches de cet objectif

<!-- AUTO:objectif=generer-code -->
> ⚙️ **Generated index** — 0 fiche(s) taguée(s) `objectives: [generer-code]`, régénéré par `tools/build_index.py`. La prose ci-dessus est curée à la main.
<!-- /AUTO -->

## Outils pour cet objectif

<!-- AUTO-OUTILS:objectif=generer-code -->
> _(aucun outil rattaché à cet objectif pour l'instant)_
<!-- /AUTO-OUTILS -->
