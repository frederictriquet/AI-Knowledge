---
titre: "Semantic Kernel"
theme: frameworks-outillage
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks
source_titre: "Cadres d’agents d’IA : choisir de bonnes bases pour votre entreprise"---

# Semantic Kernel

> Fiche du glossaire des patterns · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [39-top-ai-agent-frameworks](../sources/ibm-guide-agents-ia/md/39-top-ai-agent-frameworks.md)

**En une phrase** — le SDK d'agents de Microsoft, avec deux types d'agents intégrés (chat-completion et assistant) et un Process Framework pour orchestrer des workflows par étapes.

## Ce que dit le corpus
IBM décrit Semantic Kernel comme un kit de développement open source de Microsoft pour créer des applications d'IA générative d'entreprise. Son cadre d'agents, annoncé comme expérimental, fournit des abstractions de base pour la construction d'agents. Il propose deux implémentations intégrées : un agent de complétion de chat (chat-completion) et un agent assistant plus avancé. Plusieurs agents peuvent être orchestrés via des discussions de groupe, ou en utilisant le *Process Framework* de Semantic Kernel (également marqué comme expérimental) pour des workflows plus complexes. Le corpus précise qu'un processus se compose d'étapes, qui représentent les tâches assignées aux agents d'IA, et décrivent comment les données circulent entre les étapes. Semantic Kernel est accessible sur GitHub.

## Tradeoff / insight pour un senior
Pur vocabulaire pour qui connaît déjà l'écosystème Microsoft : « plugins/kernel » côté outillage, « Process Framework » côté orchestration par étapes (proche conceptuellement des steps d'autres cadres). Le double statut « expérimental » du framework d'agents et du Process Framework est l'unique vrai signal d'ingénierie : à ne pas poser en fondation d'une production sans veille sur les ruptures d'API.

## Source primaire
Non citée par IBM — voir la documentation Microsoft Semantic Kernel et le dépôt GitHub (hors-corpus).

## Voir aussi
- [llamaindex](llamaindex.md)
- [orchestration-types](orchestration-types.md)
