---
titre: "LLM Compiler (parallel function calling)"
theme: outils-function-calling
niveau: 🟡
provenance: ➕
base: ibm-guide-agents-ia/hors-corpus
source_url: https://arxiv.org/abs/2312.04511
---

# LLM Compiler (parallel function calling)

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. Glossaire · Pertinence 🟡 tradeoff

**En une phrase** — planifier un **DAG d'appels d'outils** et exécuter en parallèle ceux qui sont indépendants, au lieu de les enchaîner séquentiellement comme ReAct.

## L'idée
Inspiré des compilateurs : un *planner* décompose la tâche en appels avec leurs dépendances (graphe), une *task-fetching unit* lance en **parallèle** tout ce qui ne dépend de rien, un *joiner* agrège les résultats. On supprime les allers-retours séquentiels du schéma penser-agir-observer quand les sous-tâches sont indépendantes.

## Comment s'exprime le plan et l'exécution
Contrairement à MRKL (où la décision est entièrement neuronale), LLM Compiler est un **partage explicite en deux couches** — c'est le cœur de l'analogie avec les compilateurs. La **décision sémantique** est confiée au LLM par **prompting** : le *planner* (few-shot) émet le DAG, le *joiner* (LLM) décide si c'est terminé ou s'il faut re-planifier. Mais la **mécanique d'exécution** — ordonnancement, parallélisme, résolution des dépendances — est sortie du LLM et confiée à du **code déterministe** (la *task-fetching unit*), exactement comme un CPU exécute dans l'ordre des dépendances.

Concrètement, le planner émet par prompting une **syntaxe de plan** où chaque tâche est numérotée et référence les sorties précédentes via des placeholders (`$1`, `$2`…) :

```
1. search("météo Paris")
2. search("météo Lyon")
3. compare($1, $2)        # dépend de 1 et 2
```

Le runtime voit que `1` et `2` ne dépendent de rien → les lance **en parallèle**, puis substitue `$1`/`$2` par les résultats réels et débloque `3`. Cette substitution de variables et cet ordonnancement *out-of-order* sont **mécaniques** (du code, zéro appel LLM) — c'est ce découplage qui achète la latence et le coût.

## Tradeoff / quand l'utiliser
Gain de **latence et de coût** quand plusieurs outils peuvent tourner en parallèle (ex. interroger trois API météo). Même intuition que le *parallel tool calling* natif des API récentes et que le découplage de ReWOO. Inutile, voire contre-productif, si les étapes sont intrinsèquement séquentielles (chaque appel dépend du précédent).

## Source primaire
Kim et al., 2023, *An LLM Compiler for Parallel Function Calling*, arXiv:2312.04511 (UC Berkeley). *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [rewoo](rewoo.md) (corpus)
- [decomposition-first-vs-interleaved](decomposition-first-vs-interleaved.md) (corpus)
