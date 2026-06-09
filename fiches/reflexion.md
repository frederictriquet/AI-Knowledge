---
titre: "Autoréflexion / Reflexion"
theme: raisonnement-planification
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/agentic-reasoning
source_titre: "Qu’est-ce que le raisonnement agentique ?"
---

# Autoréflexion / Reflexion

**En une phrase** — après un échec, l'agent rédige une critique de ce qui n'a pas marché et rejoue la tâche avec cette critique gardée en mémoire.

## En détail
L'autoréflexion est un mécanisme par lequel l'IA agentique évalue et perfectionne ses capacités de raisonnement. LATS l'illustre concrètement : il intègre une étape d'autoréflexion combinant les observations de l'agent et les commentaires d'un modèle de langage pour identifier les erreurs de raisonnement et recommander des alternatives ; ces erreurs et réflexions sont stockées en mémoire comme contexte pour les tâches ultérieures. Reflexion est cité comme cadre émergent aux côtés de ReWOO et RAISE, « chacun ayant ses propres avantages et inconvénients ». ReAct a contribué à des avancées ultérieures « telles que Reflexion, qui a conduit aux modèles de raisonnement modernes ».

## Tradeoff / insight pour un senior
La boucle réflexive ajoute des cycles LLM (donc latence et coût) pour gagner en taux de succès sur les tâches où l'agent peut détecter ses propres erreurs. Elle suppose un signal d'échec exploitable (test, feedback) ; sans verdict fiable, la « critique » risque de renforcer une mauvaise piste. Reflexion reste principalement décrit à travers LATS dans la littérature agentique.

## Source primaire
Shinn et al. 2023, « Reflexion: Language Agents with Verbal Reinforcement Learning ». L'article LATS sert de support principal à la description de l'autoréflexion.

## Voir aussi
- [LATS (Language Agent Tree Search)](lats.md)
- [ReAct](react.md)
- [RAISE](raise.md)
