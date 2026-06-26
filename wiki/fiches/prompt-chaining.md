---
titre: "Prompt chaining"
type: "Concept"
theme: prompting
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/prompt-chaining
source_titre: "Qu'est-ce que le prompt chaining ?"
objectifs: [generer-code]
---

# Prompt chaining

**En une phrase** — décomposer une tâche complexe en une séquence de prompts simples où la sortie de chaque étape alimente la suivante.

## En détail
Le prompt chaining enchaîne plusieurs prompts pour produire une sortie cohérente et contrôlable. La méthode part de l'opposition prompts simples / prompts complexes et propose une décomposition (identifier l'objectif, le découper en sous-tâches, un prompt par sous-tâche, tester, itérer), illustrée par un cas traduction espagnol→anglais→extraction→espagnol. Avantages : cohérence (ton, style, format), contrôle renforcé, taux d'erreur réduit. Un tutoriel LangChain énumère neuf sous-types : séquentiel, ramifié (branches), itératif, hiérarchique, conditionnel, multimodal, dynamique, récursif, inverse — avec une grille de décision (complexité, dépendance, adaptabilité, modalité). Il implémente un pipeline de traitement de commentaires clients (extraction de mots-clés → résumé de sentiments → affinement) avec watsonx.ai et granite-3-8b-instruct, via PromptTemplate, LLMChain et SequentialChain.

## Exemple
La source déroule la décomposition d'un prompt complexe (« Considère le texte espagnol, traduis-le en anglais, extrais toutes les statistiques et faits en puces, retraduis-les en espagnol ») en cinq prompts simples chaînés : 1) « Lire le texte espagnol donné », 2) « Traduire le texte en anglais », 3) « Récupérer les statistiques et les faits du texte », 4) « Créer une liste à puces de tous ces faits », 5) « Les traduire en espagnol ». Chaque sortie alimente le prompt suivant : isoler chaque étape réduit le risque d'erreurs qu'un prompt monolithique cumulerait.

## Tradeoff / insight pour un senior
Le chaining échange des appels LLM contre de la fiabilité : chaque étape isolée hallucine moins, mais on multiplie latence et coût, et les erreurs se propagent en cascade. Réserve technique : ce tutoriel utilise `LLMChain` / `SequentialChain`, API LangChain legacy dépréciée — pour un guide 2026, préférer LCEL (LangChain Expression Language) et les `Runnable`. Pour les workflows agentiques, le découplage planification/exécution rejoint les motifs comme ReWOO.

## Voir aussi
- [ReWOO](rewoo.md)
- [chain-of-thought](chain-of-thought.md)
