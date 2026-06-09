---
titre: "Planification probabiliste"
theme: raisonnement-planification
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-planning
source_titre: "Qu’est-ce que la planification par agent d’IA ?"
---

# Planification probabiliste

**En une phrase** — décider sous incertitude en évaluant plusieurs résultats possibles et en choisissant l'action à l'utilité attendue la plus élevée.

## En détail
Présentée comme une méthode d'optimisation et d'évaluation de la planification, aux côtés de la recherche heuristique et de l'apprentissage par renforcement. Dans des scénarios concrets, les agents d'IA opèrent souvent dans des environnements incertains où les résultats ne sont pas déterministes ; les méthodes de planification probabiliste tiennent compte de l'incertitude en évaluant plusieurs résultats possibles et en sélectionnant les actions présentant l'utilité attendue la plus élevée. Dans le contexte de la collaboration basée sur des modèles, cette approche s'appuie sur les processus de décision markoviens (MDP) et le raisonnement bayésien : les agents construisent des modèles internes probabilistes ou appris, mettent à jour leurs croyances et prédisent les résultats, ce qui leur permet de collaborer sans visibilité complète. Avantages/inconvénients : grande flexibilité et capacités décisionnelles solides, mais complexité importante et coût computationnel élevé.

## Tradeoff / insight pour un senior
La planification probabiliste est la voie privilégiée pour gérer la visibilité partielle et le non-déterminisme. Le compromis est net : le cadre MDP/bayésien apporte des décisions robustes sous incertitude mais explose en coût de modélisation et de calcul ; on ne le sort que lorsque l'environnement est réellement stochastique, pas pour des workflows déterministes où une heuristique suffit.

## Source primaire
Non rattaché à une source nommée ; les MDP et le raisonnement bayésien sont cités comme méthodes sous-jacentes.

## Voir aussi
- [Planification : objectif / état / séquençage](planification-goal-state-action.md)
- [Décomposition anticipée vs au fil de l'eau](decomposition-first-vs-interleaved.md)
