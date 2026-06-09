# Catalogue des techniques de prompting

> Fiche du [glossaire prompting](../GLOSSAIRE-PROMPTING.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [../md/02-prompt-engineering-techniques.md](../md/02-prompt-engineering-techniques.md)

**En une phrase** — un index des stratégies de structuration de prompts, appliquées à une tâche unique (« expliquer le changement climatique ») pour comparer leurs comportements.

## Ce que dit le corpus
IBM distingue d'abord trois façons de structurer un prompt : instructions directes (commande précise), instructions ouvertes (exploration créative) et instructions spécifiques à une tâche (traduction, synthèse, calcul). Le corpus déroule ensuite ~18 techniques illustrées sur la même tâche : zero-shot, few-shot, chaîne de pensées (CoT), meta-prompting, cohérence propre (self-consistency), génération de prompts de connaissances, prompt chaining, arbre des pensées (ToT), RAG, raisonnement et utilisation automatiques des outils (ART), prompt engineering automatique (APE), prompting actif, prompt de stimulation directionnelle (DSP), modèles assistés par programmation (PAL/PALM), ReAct, Reflexion, CoT multimodale, graph prompting. Les défis cités : hallucination, difficulté à produire des sorties fiables, équilibre généralité/spécialisation.

## Tradeoff / insight pour un senior
La valeur de cette page est pédagogique : voir 18 techniques sur une seule tâche montre qu'elles ne sont pas concurrentes mais composables (RAG + few-shot, CoT + self-consistency). Attention aux approximations de traduction du corpus (« cohérence propre » = self-consistency, « PALM » conflé avec PAL).

## Source primaire
Chaque technique renvoie à des notes de bas de page numérotées dans le corpus, mais sans bibliographie résolue dans le texte lu — références non explicitées par IBM ici (hors-corpus pour le détail).

## Voir aussi
- [zero-shot-prompting](zero-shot-prompting.md)
- [few-shot-prompting](few-shot-prompting.md)
- [chain-of-thought](chain-of-thought.md)
- [meta-prompting](meta-prompting.md)
