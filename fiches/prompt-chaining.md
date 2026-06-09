---
titre: "Prompt chaining"
theme: prompting
niveau: 🟡
provenance: ✅
base: ibm-guide-prompt-engineering
source_url: https://www.ibm.com/fr-fr/think/topics/prompt-chaining
source_titre: "Qu'est-ce que le prompt chaining ?"
---

# Prompt chaining

> Fiche du glossaire prompting · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [../md/04-prompt-chaining.md](../sources/ibm-guide-prompt-engineering/md/04-prompt-chaining.md), [../md/05-prompt-chaining-langchain.md](../sources/ibm-guide-prompt-engineering/md/05-prompt-chaining-langchain.md)

**En une phrase** — décomposer une tâche complexe en une séquence de prompts simples où la sortie de chaque étape alimente la suivante.

## Ce que dit le corpus
Le prompt chaining enchaîne plusieurs prompts pour produire une sortie cohérente et contrôlable. Le corpus (04) part de l'opposition prompts simples / prompts complexes et donne une méthode de décomposition (identifier l'objectif, le découper en sous-tâches, un prompt par sous-tâche, tester, itérer), illustrée par un cas traduction espagnol→anglais→extraction→espagnol. Avantages : cohérence (ton, style, format), contrôle renforcé, taux d'erreur réduit. Le tutoriel LangChain (05) énumère neuf sous-types : séquentiel, ramifié (branches), itératif, hiérarchique, conditionnel, multimodal, dynamique, récursif, inverse — avec une grille de décision (complexité, dépendance, adaptabilité, modalité). Il implémente un pipeline de traitement de commentaires clients (extraction de mots-clés → résumé de sentiments → affinement) avec watsonx.ai et granite-3-8b-instruct, via PromptTemplate, LLMChain et SequentialChain.

## Tradeoff / insight pour un senior
Le chaining échange des appels LLM contre de la fiabilité : chaque étape isolée hallucine moins, mais on multiplie latence et coût, et les erreurs se propagent en cascade. Réserve technique : le tutoriel 05 utilise `LLMChain` / `SequentialChain`, API LangChain legacy dépréciée — pour un guide 2026, préférer LCEL (LangChain Expression Language) et les `Runnable`. Pour les workflows agentiques, le découplage planification/exécution rejoint les motifs comme ReWOO.

## Source primaire
Non citée nommément par IBM — notes de bas de page numérotées non résolues dans le texte lu (hors-corpus pour le détail).

## Voir aussi
- [ReWOO](rewoo.md)
- [chain-of-thought](chain-of-thought.md)
