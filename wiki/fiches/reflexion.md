---
titre: "Autoréflexion / Reflexion"
type: "Concept"
theme: raisonnement-planification
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/agentic-reasoning
source_titre: "Qu’est-ce que le raisonnement agentique ?"
objectifs: [generer-code]
---

# Autoréflexion / Reflexion

**En une phrase** — après un échec, l'agent rédige une critique de ce qui n'a pas marché et rejoue la tâche avec cette critique gardée en mémoire.

## En détail
L'autoréflexion est un mécanisme par lequel l'IA agentique évalue et perfectionne ses capacités de raisonnement. LATS l'illustre concrètement : il intègre une étape d'autoréflexion combinant les observations de l'agent et les commentaires d'un modèle de langage pour identifier les erreurs de raisonnement et recommander des alternatives ; ces erreurs et réflexions sont stockées en mémoire comme contexte pour les tâches ultérieures. Reflexion figure parmi les cadres émergents aux côtés de ReWOO et RAISE, « chacun ayant ses propres avantages et inconvénients ». ReAct a contribué à des avancées ultérieures « telles que Reflexion, qui a conduit aux modèles de raisonnement modernes ».

## Exemple
Une boucle ReAct chargée de répondre à une question interactive tourne en rond : elle régénère le même raisonnement et les mêmes actions, jusqu'à la boucle infinie décrite comme principal défaut de ReAct. L'autoréflexion brise ce cycle : après l'échec, l'agent confronte ses propres observations au commentaire d'un LLM-critique, qui diagnostique « tu réinterroges la même source sans succès, change d'angle ». Cette réflexion est rangée en mémoire et réinjectée comme contexte au rejeu suivant, empêchant la répétition de l'erreur — le mécanisme exact qu'incarne LATS dans la littérature agentique.

## Tradeoff / insight pour un senior
La boucle réflexive ajoute des cycles LLM (donc latence et coût) pour gagner en taux de succès sur les tâches où l'agent peut détecter ses propres erreurs. Elle suppose un signal d'échec exploitable (test, feedback) ; sans verdict fiable, la « critique » risque de renforcer une mauvaise piste. Reflexion reste principalement décrit à travers LATS dans la littérature agentique.

## Source primaire
Shinn et al. 2023, « Reflexion: Language Agents with Verbal Reinforcement Learning ». Dans la littérature agentique, l'autoréflexion est principalement abordée à travers LATS.

## Voir aussi
- [LATS (Language Agent Tree Search)](lats.md)
- [ReAct](react.md)
- [RAISE](raise.md)
