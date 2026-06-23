---
titre: "Catalogue des techniques de prompting"
type: "Concept"
theme: prompting
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/prompt-engineering-techniques
source_titre: "Techniques de prompt engineering"
---

# Catalogue des techniques de prompting

**En une phrase** — un index des stratégies de structuration de prompts, appliquées à une tâche unique (« expliquer le changement climatique ») pour comparer leurs comportements.

## En détail
On distingue d'abord trois façons de structurer un prompt : instructions directes (commande précise), instructions ouvertes (exploration créative) et instructions spécifiques à une tâche (traduction, synthèse, calcul). Sont ensuite déroulées ~18 techniques illustrées sur la même tâche : zero-shot, few-shot, chaîne de pensées (CoT), meta-prompting, cohérence propre (self-consistency), génération de prompts de connaissances, prompt chaining, arbre des pensées (ToT), RAG, raisonnement et utilisation automatiques des outils (ART), prompt engineering automatique (APE), prompting actif, prompt de stimulation directionnelle (DSP), modèles assistés par programmation (PAL/PALM), ReAct, Reflexion, CoT multimodale, graph prompting. Les défis cités : hallucination, difficulté à produire des sorties fiables, équilibre généralité/spécialisation.

## Tradeoff / insight pour un senior
La valeur de cette page est pédagogique : voir 18 techniques sur une seule tâche montre qu'elles ne sont pas concurrentes mais composables (RAG + few-shot, CoT + self-consistency). Attention aux approximations de traduction (« cohérence propre » = self-consistency, « PALM » conflé avec PAL).

## Source primaire
Chaque technique renvoie à des notes de bas de page numérotées, mais sans bibliographie résolue dans le texte — références non explicitées.

## Voir aussi
- [zero-shot-prompting](zero-shot-prompting.md)
- [few-shot-prompting](few-shot-prompting.md)
- [chain-of-thought](chain-of-thought.md)
- [meta-prompting](meta-prompting.md)
