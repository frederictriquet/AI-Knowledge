---
titre: "ReWOO"
theme: raisonnement-planification
niveau: 🟡
provenance: ✅
base: ibm-guide-agents-ia
source_url: https://www.ibm.com/fr-fr/think/topics/rewoo
source_titre: "Qu’est-ce que ReWOO ?"
---

# ReWOO

> Fiche du glossaire des patterns · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [../md/30-rewoo.md](../sources/ibm-guide-agents-ia/md/30-rewoo.md), [../md/18-agentic-reasoning.md](../sources/ibm-guide-agents-ia/md/18-agentic-reasoning.md), [../md/31-build-rewoo-reasoning-agent-granite.md](../sources/ibm-guide-agents-ia/md/31-build-rewoo-reasoning-agent-granite.md)

**En une phrase** — « Reasoning Without Observation » : planifier toute la chaîne de raisonnement en interne d'abord, puis exécuter les outils, puis synthétiser, sans réinjecter chaque observation.

## Ce que dit le corpus
ReWOO supprime l'étape d'observation de ReAct et dissocie le raisonnement des observations externes (30). Il s'articule en trois modules : Planner (décompose la tâche en sous-questions, établit le schéma directeur), Worker (appelle les outils externes pour collecter preuves sans rappeler le LLM pour « réfléchir ») et Solver (synthétise plans et preuves en réponse finale) (30, 31). Comme chaque appel d'outil de ReAct ré-inclut tout l'historique, ReWOO économise environ 80 % de tokens à performance équivalente ou légèrement supérieure (30). Exemple chiffré sur HotpotQA : ReWOO atteint 42,4 % de précision avec 2 000 tokens contre 40,8 % avec 10 000 tokens pour ReAct (30). ReWOO est aussi plus robuste en cas de défaillance d'un outil (réponse partielle au lieu d'une boucle infinie). Il échoue toutefois sur les tâches exploratoires/peu structurées (ex. débogage Python), face aux « inconnues inconnues » (30).

## Tradeoff / insight pour un senior
Le gain en tokens vient de la perte de réactivité : le plan est figé avant toute observation, donc ReWOO excelle sur preuves prévisibles (« inconnues connues ») et échoue dès que les résultats intermédiaires devraient réorienter le plan. À réserver aux pipelines déterministes ; pour l'exploratoire, ReAct reste préférable malgré son coût.

## Source primaire
Citée par IBM : Binfeng Xu et al., 2023, implémentation « officielle » disponible sur GitHub (le corpus ne donne pas de n° arXiv).

## Voir aussi
- [ReAct](react.md)
- [Chain-of-Thought (CoT)](chain-of-thought.md)
