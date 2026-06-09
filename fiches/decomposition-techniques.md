---
titre: "Techniques de décomposition"
theme: prompting
niveau: 🔴
source_url: https://arxiv.org/abs/2406.06608
source_titre: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"---

# Techniques de décomposition

> Fiche **source : The Prompt Report (Schulhoff et al., 2024)** · [papier](../sources/prompt-report/md/prompt-report.md) · Pertinence 🔴 substance

**En une phrase** — Casser explicitement un problème complexe en sous-problèmes plus simples, puis les résoudre un à un, pour fiabiliser la réponse finale.

## Ce que dit la source
La famille Decomposition (§2.2.3) regroupe les techniques qui décomposent un problème complexe en sous-questions plus simples. Le rapport souligne que, si CoT décompose souvent naturellement, le faire de manière explicite améliore encore la capacité de résolution. Least-to-Most Prompting (Zhou et al.) demande d'abord de découper le problème en sous-problèmes sans les résoudre, puis les résout séquentiellement en accumulant les réponses. Decomposed Prompting / DECOMP (Khot et al.) montre au LLM, en few-shot, comment appeler des fonctions (split de chaîne, recherche web...) pour traiter les sous-problèmes. Plan-and-Solve (Wang et al.) est un Zero-Shot CoT amélioré demandant d'élaborer un plan avant de l'exécuter pas à pas. Tree-of-Thought / ToT (Yao et al., Long) construit une recherche arborescente en générant et évaluant plusieurs pensées. Recursion-of-Thought (Lee et Kim) délègue chaque sous-problème à un nouvel appel. Program-of-Thoughts (Chen et al.) génère du code exécuté par un interpréteur ; Faithful Chain-of-Thought (Lyu et al.) mêle langage naturel et symbolique ; Skeleton-of-Thought (Ning et al.) parallélise via un squelette de réponse.

## Ce que ça ajoute vs IBM
Au-delà du Tree of Thoughts et du prompt chaining d'IBM, cette famille formalise tout un éventail de stratégies de découpage explicite (Least-to-Most, DECOMP, Plan-and-Solve, Program-of-Thoughts), y compris le recours à du code et à des appels de fonctions externes.

## Techniques clés
- Least-to-Most Prompting (Zhou et al.) — découper puis résoudre séquentiellement.
- Decomposed Prompting / DECOMP (Khot et al.) — sous-problèmes routés vers des fonctions.
- Plan-and-Solve Prompting (Wang et al.) — planifier avant d'exécuter pas à pas.
- Tree-of-Thought / ToT (Yao et al., Long) — recherche arborescente de pensées.
- Recursion-of-Thought (Lee et Kim) — sous-problème délégué à un nouvel appel.
- Program-of-Thoughts (Chen et al.) — code généré et exécuté comme raisonnement.
- Faithful Chain-of-Thought (Lyu et al.) — raisonnement naturel + symbolique.
- Skeleton-of-Thought (Ning et al.) — squelette puis résolution parallélisée.

## Voir aussi
- (IBM) [Tree of Thoughts](tree-of-thoughts.md)
- (IBM) [Prompt chaining](prompt-chaining.md)
- (agents hors-corpus) [CodeAct (incluant PAL)](codeact.md)
- [papier complet](../sources/prompt-report/md/prompt-report.md)
