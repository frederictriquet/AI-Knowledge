---
titre: "CrewAI"
type: "Concept"
theme: frameworks-outillage
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/crew-ai
source_titre: "Qu’est-ce que CrewAI ?"
---

# CrewAI

**En une phrase** — un cadre multi-agents bâti sur LangChain qui organise des agents en « équipe » via rôles, tâches et processus (séquentiel ou hiérarchique à manager auto-généré).

## En détail
CrewAI est un cadre d'orchestration multi-agents open source créé par **João Moura**, basé sur Python et **construit sur LangChain** selon un principe de conception modulaire. Ses composants : **agents** (unité autonome dotée d'un rôle, d'un objectif et d'un profil/backstory) ; **outils** (CrewAI et LangChain, avec gestion d'erreurs et cache) ; **tâches** (description, agent, résultat attendu, exécution asynchrone possible) ; **processus** ; et **équipes** (crews). Trois processus existent : **séquentiel** (tâches dans l'ordre, sortie d'une tâche servant de contexte à la suivante) ; **hiérarchique** (CrewAI génère de manière autonome un agent manager qui supervise, attribue les tâches et évalue les sorties) ; et **consensuel**, « planifié » mais **pas actuellement implémenté dans la base de code**. CrewAI se connecte à n'importe quel LLM (GPT-4 par défaut, IBM Granite, Ollama) et combine la flexibilité conversationnelle d'AutoGen et l'approche structurée de ChatDev.

## Exemple
Un `Agent(role='Support client', goal='Gère les demandes et les problèmes des clients', backstory='Vous êtes spécialiste du support client pour un restaurant…')` et un `data_science_agent` sont réunis dans `Crew(agents=[…], tasks=[…], process=Process.sequential)`. La `Task(description='Recueillir des données à partir des interactions clients, de l'historique des transactions et des tickets', expected_output='Un ensemble organisé de données pouvant être prétraitées', agent=data_science_agent)` voit sa sortie servir de contexte à la tâche suivante. Cas réel du dépôt crewAI-examples de Moura : analyse boursière où des agents à rôles distincts collaborent pour produire des recommandations d'investissement, configurés sur GPT-3.5 plutôt que le GPT-4 par défaut.

## Tradeoff / insight pour un senior
Pur vocabulaire (rôles/tâches/process = répartition d'équipe). Point à retenir : le processus hiérarchique repose sur un manager LLM auto-généré — pratique mais c'est un orchestrateur non déterministe ; et le consensuel n'existe que sur le papier.

## Source primaire
Voir la documentation CrewAI et le dépôt crewAI-examples de Moura.

## Voir aussi
- [langchain](langchain.md)
- [autogen-ag2](autogen-ag2.md)
