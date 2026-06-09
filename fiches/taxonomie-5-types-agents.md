---
titre: "Taxonomie des 5 types d'agents"
theme: fondamentaux-agents
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-types
source_titre: "Types d'agents d'IA"---

# Taxonomie des 5 types d'agents

> Fiche du glossaire des patterns · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [08-ai-agent-types](../sources/ibm-guide-agents-ia/md/08-ai-agent-types.md), [09-simple-reflex-agent](../sources/ibm-guide-agents-ia/md/09-simple-reflex-agent.md), [69-ai-agent-use-cases](../sources/ibm-guide-agents-ia/md/69-ai-agent-use-cases.md)

**En une phrase** — l'échelle de sophistication classique des agents, du `if/then` câblé jusqu'à l'agent qui s'améliore par feedback.

## Ce que dit le corpus
IBM distingue cinq principaux types d'agents IA, classés par niveau d'intelligence et de processus décisionnel : agents réflexes simples, agents réflexes basés sur des modèles, agents basés sur des objectifs, agents basés sur l'utilité et agents apprenants. Le réflexe simple applique des règles condition-action sans mémoire ni anticipation (thermostat, feux de circulation). Le réflexe basé sur un modèle ajoute un modèle interne du monde pour gérer un environnement partiellement observable. L'agent basé sur des objectifs planifie et raisonne pour atteindre un but. L'agent basé sur l'utilité évalue plusieurs résultats via une fonction d'utilité et arbitre des objectifs concurrents. L'agent apprenant met à jour son comportement à partir des retours d'expérience. IBM précise que ces cinq types peuvent être déployés ensemble dans un système multi-agents, chacun se spécialisant sur la sous-tâche pour laquelle il est le mieux adapté.

## Tradeoff / insight pour un senior
Pur vocabulaire pédagogique. La hiérarchie réflexe → modèle → objectif → utilité → apprenant correspond à un coût/complexité croissant : on ne « monte » d'un cran que si l'environnement l'exige (mémoire, planification, arbitrage, adaptation). L'exemple de l'usine montre que combiner les cinq donne des couches : réflexe pour la sécurité instantanée, utilité pour l'arbitrage, apprenant pour l'optimisation continue.

## Source primaire
Non citée par IBM — taxonomie issue de Russell & Norvig, *Artificial Intelligence: A Modern Approach* (AIMA, chap. 2), jamais référencée dans le corpus (hors-corpus).

## Voir aussi
- [Agent apprenant (modèle AIMA)](agent-apprenant.md)
- [Architectures réactive / délibérative / cognitive](archi-reactif-deliberatif-cognitif.md)
