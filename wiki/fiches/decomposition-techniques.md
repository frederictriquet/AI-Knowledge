---
titre: "Techniques de décomposition"
type: "Concept"
theme: prompting
niveau: 🔴
source_url: https://arxiv.org/abs/2406.06608
source_titre: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
---

# Techniques de décomposition

**En une phrase** — Casser explicitement un problème complexe en sous-problèmes plus simples, puis les résoudre un à un, pour fiabiliser la réponse finale.

## Ce que dit la source
La famille Decomposition (§2.2.3) regroupe les techniques qui décomposent un problème complexe en sous-questions plus simples. Le rapport souligne que, si CoT décompose souvent naturellement, le faire de manière explicite améliore encore la capacité de résolution. Least-to-Most Prompting (Zhou et al.) demande d'abord de découper le problème en sous-problèmes sans les résoudre, puis les résout séquentiellement en accumulant les réponses. Decomposed Prompting / DECOMP (Khot et al.) montre au LLM, en few-shot, comment appeler des fonctions (split de chaîne, recherche web...) pour traiter les sous-problèmes. Plan-and-Solve (Wang et al.) est un Zero-Shot CoT amélioré demandant d'élaborer un plan avant de l'exécuter pas à pas. Tree-of-Thought / ToT (Yao et al., Long) construit une recherche arborescente en générant et évaluant plusieurs pensées. Recursion-of-Thought (Lee et Kim) délègue chaque sous-problème à un nouvel appel. Program-of-Thoughts (Chen et al.) génère du code exécuté par un interpréteur ; Faithful Chain-of-Thought (Lyu et al.) mêle langage naturel et symbolique ; Skeleton-of-Thought (Ning et al.) parallélise via un squelette de réponse.

## Exemple
DECOMP (Khot et al.) illustre concrètement le routage : en few-shot, on montre au modèle des fonctions atomiques (`split`, `str_pos`, recherche internet), chacune souvent implémentée comme un appel LLM séparé. Face à une tâche de manipulation symbolique, le modèle ne résout pas tout d'un bloc : il décompose en appels de fonctions et délègue, surpassant Least-to-Most sur certaines tâches. Recursion-of-Thought pousse plus loin en émettant un token spécial qui envoie chaque sous-problème dans un nouvel appel dont la réponse est réinsérée, ce qui permet de traiter un problème dépassant la fenêtre de contexte (gains rapportés sur tâches arithmétiques et algorithmiques).

## Pourquoi c'est utile
Cette famille formalise tout un éventail de stratégies de découpage explicite (Least-to-Most, DECOMP, Plan-and-Solve, Program-of-Thoughts), y compris le recours à du code et à des appels de fonctions externes, au-delà du Tree of Thoughts et du prompt chaining.

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
- [Tree of Thoughts](tree-of-thoughts.md)
- [Prompt chaining](prompt-chaining.md)
- [CodeAct (incluant PAL)](codeact.md)
- [papier complet](../sources/prompt-report/md/prompt-report.md)
