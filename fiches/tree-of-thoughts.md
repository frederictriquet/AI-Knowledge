---
titre: "Tree of Thoughts (ToT)"
theme: raisonnement-planification
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/tree-of-thoughts
source_titre: "Qu’est-ce que l’arbre des pensées ?"
source_primaire: "arXiv:2305.10601"---

# Tree of Thoughts (ToT)

> Fiche du glossaire prompting · Pertinence 🔴 substance · Provenance ✅ présent · Sources corpus : [../md/06-tree-of-thoughts.md](../sources/ibm-guide-prompt-engineering/md/06-tree-of-thoughts.md)

**En une phrase** — généraliser la CoT en arbre : générer plusieurs « pensées » par étape, les évaluer, et explorer l'espace de solutions par recherche (BFS/DFS) avec backtracking.

## Ce que dit le corpus
Le fichier 06 est le plus complet du corpus sur ce thème et le seul à fournir une vraie bibliographie. IBM décrit le cadre ToT en quatre composants : décomposition de la pensée, génération des pensées (échantillonnage ou proposition), évaluation des états (valeur scalaire ou vote), et algorithme de recherche (BFS qui explore tous les nœuds d'un niveau, DFS qui creuse une branche avant de backtracker). Une auto-évaluation par le LLM valide chaque étape et permet de revenir à un nœud antérieur en cas d'impasse. Le corpus cite l'extension TouT (Tree of Uncertain Thoughts, Monte Carlo Dropout pour quantifier l'incertitude). Limites : surcharge de calcul, complexité de mise en œuvre (agent prompteur, vérificateur, mémoire, contrôleur), et surtout une critique d'efficacité : le ToT explore des chemins à faible valeur, faute de prioriser les branches prometteuses. IBM mentionne l'alternative « Thought of Search » qui intègre heuristiques de planification et gain d'information. Études de cas : sudoku, Puzzle 24, écriture créative, mots croisés 5×5.

## Tradeoff / insight pour un senior
ToT augmente le taux de réussite sur les problèmes à forte combinatoire (puzzles, planification) au prix d'une explosion des appels LLM qui croît avec largeur × profondeur. Le ToT « vanilla » gaspille du budget sur des branches mortes : la critique d'efficacité (Thought of Search) suggère que des heuristiques de recherche bien choisies battent souvent l'exploration arborescente naïve.

## Source primaire
Citée par IBM : Yao et al. 2023, « Tree of Thoughts: Deliberate Problem Solving with Large Language Models », arXiv:2305.10601 ; dépôt [princeton-nlp/tree-of-thought-llm](https://github.com/princeton-nlp/tree-of-thought-llm) ; Mo & Xin 2023 (TouT, arXiv:2309.07694) ; Katz et al. 2024 (Thought of Search, NeurIPS vol. 37).

## Voir aussi
- [Chain-of-Thought (CoT)](chain-of-thought.md)
- [Self-Consistency](self-consistency.md)
- [LATS (Language Agent Tree Search)](lats.md) — côté agents, ToT est la toile de fond conceptuelle de LATS
