---
titre: "ReWOO"
theme: raisonnement-planification
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/rewoo
source_titre: "Qu’est-ce que ReWOO ?"
---

# ReWOO

**En une phrase** — « Reasoning Without Observation » : planifier toute la chaîne de raisonnement en interne d'abord, puis exécuter les outils, puis synthétiser, sans réinjecter chaque observation.

## En détail
ReWOO supprime l'étape d'observation de ReAct et dissocie le raisonnement des observations externes. Il s'articule en trois modules : Planner (décompose la tâche en sous-questions, établit le schéma directeur), Worker (appelle les outils externes pour collecter preuves sans rappeler le LLM pour « réfléchir ») et Solver (synthétise plans et preuves en réponse finale). Comme chaque appel d'outil de ReAct ré-inclut tout l'historique, ReWOO économise environ 80 % de tokens à performance équivalente ou légèrement supérieure. Exemple chiffré sur HotpotQA : ReWOO atteint 42,4 % de précision avec 2 000 tokens contre 40,8 % avec 10 000 tokens pour ReAct. ReWOO est aussi plus robuste en cas de défaillance d'un outil (réponse partielle au lieu d'une boucle infinie). Il échoue toutefois sur les tâches exploratoires/peu structurées (ex. débogage Python), face aux « inconnues inconnues ».

## Tradeoff / insight pour un senior
Le gain en tokens vient de la perte de réactivité : le plan est figé avant toute observation, donc ReWOO excelle sur preuves prévisibles (« inconnues connues ») et échoue dès que les résultats intermédiaires devraient réorienter le plan. À réserver aux pipelines déterministes ; pour l'exploratoire, ReAct reste préférable malgré son coût.

## Source primaire
Binfeng Xu et al., 2023, implémentation « officielle » disponible sur GitHub (sans n° arXiv dans la source).

## Voir aussi
- [ReAct](react.md)
- [Chain-of-Thought (CoT)](chain-of-thought.md)
