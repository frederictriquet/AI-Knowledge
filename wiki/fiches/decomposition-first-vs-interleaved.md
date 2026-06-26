---
titre: "Décomposition anticipée vs au fil de l'eau"
type: "Concept"
theme: prompting
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-planning
source_titre: "Qu’est-ce que la planification par agent d’IA ?"
---

# Décomposition anticipée vs au fil de l'eau

**En une phrase** — tout planifier d'avance puis exécuter sans re-raisonner (ReWOO) versus planifier et réviser à chaque observation (ReAct).

## En détail
ReAct est une méthodologie pensée-action-observation où le raisonnement génère une séquence d'étapes ; ReWOO, RAISE et Reflexion sont des cadres émergents « chacun ayant ses propres avantages et inconvénients ». ReAct suit un cycle penser-agir-observer : le système observe ce qu'il génère avant de recommencer à y réfléchir, mais chaque appel d'outil doit ré-inclure tout l'historique, d'où une forte consommation de tokens. ReWOO (« reasoning without observation ») dissocie le raisonnement des observations : le module **Planner** établit tout le plan d'avance, le **Worker** exécute les appels d'outils sans re-réflexion coûteuse, le **Solver** synthétise. Résultat cité : précision équivalente à ReAct (42,4 % vs 40,8 % sur HotpotQA) avec ~80 % de tokens en moins (2 000 vs 10 000). ReWOO est aussi plus robuste à la défaillance d'un outil, mais échoue sur les problèmes imprévisibles (« inconnues inconnues », ex. débogage Python itératif).

## Exemple
Cas ReWOO favorable : une question HotpotQA multi-hop (« dans quelle ville est né le réalisateur du film X ? »). Le Planner pose d'avance le plan — chercher le réalisateur, puis sa ville natale ; le Worker exécute les deux recherches ; le Solver synthétise. Aucune ré-injection d'historique entre étapes. Cas défavorable cité : le débogage Python itératif, une « inconnue inconnue » où le message d'erreur de l'étape N redéfinit l'étape N+1 — là, le plan figé d'avance s'effondre et seul ReAct, qui re-raisonne après chaque observation, tient.

## Tradeoff / insight pour un senior
Le tradeoff structurant de la planification agentique. Décomposer tout d'avance est imbattable en coût et robustesse quand les preuves nécessaires sont régulières et prévisibles ; planifier au fil de l'eau coûte plus de tokens mais reste seul viable face à l'exploratoire, où chaque observation invalide le plan précédent.

## Source primaire
ReWOO décrit par Binfeng Xu et al., 2023 (implémentation de référence sur GitHub) ; prompt d'amorce cité : « Pour la tâche suivante, élaborer des plans qui peuvent résoudre le problème étape par étape. »

## Voir aussi
- [Planification : objectif / état / séquençage](planification-goal-state-action.md)
- [Planification probabiliste](planification-probabiliste.md)
