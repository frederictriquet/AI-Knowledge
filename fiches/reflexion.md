---
titre: "Autoréflexion / Reflexion"
theme: raisonnement-planification
niveau: 🟡
provenance: ✅
base: ibm-guide-agents-ia
source_url: https://www.ibm.com/fr-fr/think/topics/agentic-reasoning
source_titre: "Qu’est-ce que le raisonnement agentique ?"
---

# Autoréflexion / Reflexion

> Fiche du glossaire des patterns · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [../md/18-agentic-reasoning.md](../sources/ibm-guide-agents-ia/md/18-agentic-reasoning.md), [../md/17-ai-agent-planning.md](../sources/ibm-guide-agents-ia/md/17-ai-agent-planning.md), [../md/28-react-agent.md](../sources/ibm-guide-agents-ia/md/28-react-agent.md)

**En une phrase** — après un échec, l'agent rédige une critique de ce qui n'a pas marché et rejoue la tâche avec cette critique gardée en mémoire.

## Ce que dit le corpus
Le corpus présente l'autoréflexion comme un mécanisme par lequel l'IA agentique évalue et perfectionne ses capacités de raisonnement (18). Il l'illustre via LATS, qui intègre une étape d'autoréflexion combinant les observations de l'agent et les commentaires d'un modèle de langage pour identifier les erreurs de raisonnement et recommander des alternatives ; ces erreurs et réflexions sont stockées en mémoire comme contexte pour les tâches ultérieures (18). Le fichier 17 cite Reflexion comme cadre émergent aux côtés de ReWOO et RAISE, « chacun ayant ses propres avantages et inconvénients ». Le fichier 28 indique que ReAct a contribué à des avancées ultérieures « telles que Reflexion, qui a conduit aux modèles de raisonnement modernes ».

## Tradeoff / insight pour un senior
La boucle réflexive ajoute des cycles LLM (donc latence et coût) pour gagner en taux de succès sur les tâches où l'agent peut détecter ses propres erreurs. Elle suppose un signal d'échec exploitable (test, feedback) ; sans verdict fiable, la « critique » risque de renforcer une mauvaise piste. Le corpus reste vague sur Reflexion en propre et le rattache surtout à LATS.

## Source primaire
Non citée nommément par IBM pour Reflexion — voir Shinn et al. 2023, « Reflexion: Language Agents with Verbal Reinforcement Learning » (hors-corpus). Le corpus cite l'article LATS comme support de la description de l'autoréflexion.

## Voir aussi
- [LATS (Language Agent Tree Search)](lats.md)
- [ReAct](react.md)
- [RAISE](raise.md)
