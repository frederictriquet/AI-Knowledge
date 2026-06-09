---
titre: "Taxonomie des 5 types d'agents"
theme: fondamentaux-agents
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-types
source_titre: "Types d'agents d'IA"
---

# Taxonomie des 5 types d'agents

**En une phrase** — l'échelle de sophistication classique des agents, du `if/then` câblé jusqu'à l'agent qui s'améliore par feedback.

## En détail
On distingue cinq principaux types d'agents IA, classés par niveau d'intelligence et de processus décisionnel : agents réflexes simples, agents réflexes basés sur des modèles, agents basés sur des objectifs, agents basés sur l'utilité et agents apprenants. Le réflexe simple applique des règles condition-action sans mémoire ni anticipation (thermostat, feux de circulation). Le réflexe basé sur un modèle ajoute un modèle interne du monde pour gérer un environnement partiellement observable. L'agent basé sur des objectifs planifie et raisonne pour atteindre un but. L'agent basé sur l'utilité évalue plusieurs résultats via une fonction d'utilité et arbitre des objectifs concurrents. L'agent apprenant met à jour son comportement à partir des retours d'expérience. Ces cinq types peuvent être déployés ensemble dans un système multi-agents, chacun se spécialisant sur la sous-tâche pour laquelle il est le mieux adapté.

## Tradeoff / insight pour un senior
Pur vocabulaire pédagogique. La hiérarchie réflexe → modèle → objectif → utilité → apprenant correspond à un coût/complexité croissant : on ne « monte » d'un cran que si l'environnement l'exige (mémoire, planification, arbitrage, adaptation). L'exemple de l'usine montre que combiner les cinq donne des couches : réflexe pour la sécurité instantanée, utilité pour l'arbitrage, apprenant pour l'optimisation continue.

## Source primaire
Taxonomie issue de Russell & Norvig, *Artificial Intelligence: A Modern Approach* (AIMA, chap. 2).

## Voir aussi
- [Agent apprenant (modèle AIMA)](agent-apprenant.md)
- [Architectures réactive / délibérative / cognitive](archi-reactif-deliberatif-cognitif.md)
