---
titre: "Semantic Kernel"
type: "Concept"
theme: frameworks-outillage
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks
source_titre: "Cadres d’agents d’IA : choisir de bonnes bases pour votre entreprise"
---

# Semantic Kernel

**En une phrase** — le SDK d'agents de Microsoft, avec deux types d'agents intégrés (chat-completion et assistant) et un Process Framework pour orchestrer des workflows par étapes.

## En détail
Semantic Kernel est un kit de développement open source de Microsoft pour créer des applications d'IA générative d'entreprise. Son cadre d'agents, annoncé comme expérimental, fournit des abstractions de base pour la construction d'agents. Il propose deux implémentations intégrées : un agent de complétion de chat (chat-completion) et un agent assistant plus avancé. Plusieurs agents peuvent être orchestrés via des discussions de groupe, ou en utilisant le *Process Framework* (également marqué comme expérimental) pour des workflows plus complexes. Un processus se compose d'étapes qui représentent les tâches assignées aux agents d'IA et décrivent comment les données circulent entre elles. Semantic Kernel est accessible sur GitHub.

## Exemple
Process de traitement d'un ticket support : une étape `Classifier` (agent chat-completion) lit le message et émet la catégorie ; les données circulent vers une étape `Résoudre` (agent assistant, plus avancé, avec accès aux plugins) qui interroge la base de connaissances ; une troisième étape `Rédiger` formule la réponse. Si la catégorie est « cas complexe », le Process Framework route plutôt vers une discussion de groupe où plusieurs agents délibèrent. Chaque étape déclare explicitement les tâches assignées et la circulation des données entre elles — c'est le step, pas un graphe libre.

## Tradeoff / insight pour un senior
Pur vocabulaire pour qui connaît déjà l'écosystème Microsoft : « plugins/kernel » côté outillage, « Process Framework » côté orchestration par étapes (proche conceptuellement des steps d'autres cadres). Le double statut « expérimental » du framework d'agents et du Process Framework est l'unique vrai signal d'ingénierie : à ne pas poser en fondation d'une production sans veille sur les ruptures d'API.

## Source primaire
Voir la documentation Microsoft Semantic Kernel et le dépôt GitHub.

## Voir aussi
- [llamaindex](llamaindex.md)
- [orchestration-types](orchestration-types.md)
