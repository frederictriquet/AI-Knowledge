---
titre: "Comportements d'essaim (flocking / swarming)"
type: "Concept"
theme: frameworks-outillage
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/multiagent-system
source_titre: "Qu’est-ce qu’un système multi-agent ?"
---

# Comportements d'essaim (flocking / swarming)

**En une phrase** — coordonner une foule d'agents par quelques règles locales bio-inspirées, sans contrôleur central.

## En détail
Les comportements des agents dans un système multi-agent reflètent souvent ceux observés dans la nature (oiseaux, poissons, humains) et s'appliquent aux agents logiciels comme robotiques. Le **regroupement** (flocking) concerne la synchronisation directionnelle et se décrit par trois heuristiques : **séparation** (éviter les collisions avec les agents proches), **alignement** (atteindre la vitesse des agents proches), **cohésion** (rester proche des autres agents). La gestion de réseaux de transport (systèmes ferroviaires) est un contexte logiciel représentatif. L'**essaimage** (swarming) désigne l'auto-organisation et l'agrégation émergentes parmi des agents logiciels avec un **contrôle décentralisé** ; son avantage est qu'un seul opérateur peut être formé à gérer tout un essaim, ce qui est moins coûteux en calcul et plus fiable que de former un opérateur par agent.

## Tradeoff / insight pour un senior
Les trois règles séparation/alignement/cohésion sont les boids de Reynolds : un comportement global cohérent émerge de règles purement locales, sans état global ni coordinateur. Compromis : robustesse et passage à l'échelle massif (des milliers d'agents) contre absence de garantie sur le résultat global et difficulté à contraindre l'émergence. À retenir : c'est une réponse au coût de coordination quand le nombre d'agents explose.

## Source primaire
Les heuristiques séparation/alignement/cohésion proviennent de Craig Reynolds, « Flocks, Herds, and Schools: A Distributed Behavioral Model » (boids, SIGGRAPH 1987).

## Voir aussi
- [Structures multi-agents : hiérarchique / holonique / coalition / équipe](structures-multi-agents.md)
- [Réseaux centralisés vs décentralisés](reseaux-centralises-decentralises.md)
