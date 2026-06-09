---
titre: "ACI : concevoir l'interface agent-ordinateur"
theme: fondamentaux-agents
niveau: 🔴
source_url: https://www.anthropic.com/engineering/building-effective-agents
source_titre: "Building effective agents"
---

# ACI : concevoir l'interface agent-ordinateur

**En une phrase** — soigner la définition des outils (noms, descriptions, formats) avec autant d'attention que les prompts : l'interface agent-ordinateur (ACI) est, pour un agent, l'équivalent de l'IHM pour un humain.

## L'essentiel
Les **définitions d'outils méritent autant de prompt engineering que les prompts**. Choisir des formats que le modèle écrit *facilement* — éviter le diff (qui exige de compter les lignes à l'avance) ou le code dans du JSON (échappement de guillemets/retours à la ligne) ; laisser au modèle des tokens pour « réfléchir » avant de s'enfermer ; **poka-yoke** les outils (rendre l'erreur structurellement difficile). Mettre dans la description des exemples d'usage, cas limites et formats d'entrée — « comme une bonne docstring pour un développeur junior ». Anecdote SWE-bench : ils ont passé **plus de temps à optimiser les outils que le prompt global** ; imposer des **chemins absolus** a corrigé d'un coup les erreurs de chemins relatifs après changement de répertoire.

## Pourquoi c'est utile
La conception de l'interface d'outils est un levier de fiabilité de premier ordre, aussi important que le prompt lui-même.

## À retenir
- Investir dans l'**ACI** autant que dans l'IHM ; tester les outils sur de vraies entrées (workbench) et itérer.
- Se mettre « à la place du modèle » : la description rend-elle l'usage évident ?

## Voir aussi
- [Tool calling](tool-calling.md) · [Tool grounding](tool-grounding.md)
- [Modèles de langage augmentés](augmented-language-models.md)
- [post complet](../sources/anthropic-effective-agents/md/building-effective-agents.md)
