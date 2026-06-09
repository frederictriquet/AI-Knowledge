# CrewAI

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [48-crew-ai](../md/48-crew-ai.md)

**En une phrase** — un cadre multi-agents bâti sur LangChain qui organise des agents en « équipe » via rôles, tâches et processus (séquentiel ou hiérarchique à manager auto-généré).

## Ce que dit le corpus
CrewAI est un cadre d'orchestration multi-agents open source créé par **João Moura**, basé sur Python et **construit sur LangChain** selon un principe de conception modulaire. Ses composants : **agents** (unité autonome dotée d'un rôle, d'un objectif et d'un profil/backstory) ; **outils** (CrewAI et LangChain, avec gestion d'erreurs et cache) ; **tâches** (description, agent, résultat attendu, exécution asynchrone possible) ; **processus** ; et **équipes** (crews). Trois processus sont décrits : **séquentiel** (tâches dans l'ordre, sortie d'une tâche servant de contexte à la suivante) ; **hiérarchique** (CrewAI génère de manière autonome un agent manager qui supervise, attribue les tâches et évalue les sorties) ; et **consensuel**, « planifié » mais — précise le corpus — **pas actuellement implémenté dans la base de code**. CrewAI se connecte à n'importe quel LLM (GPT-4 par défaut, IBM Granite, Ollama) et combine, selon IBM, la flexibilité conversationnelle d'AutoGen et l'approche structurée de ChatDev.

## Tradeoff / insight pour un senior
Pur vocabulaire (rôles/tâches/process = répartition d'équipe). Point à retenir : le processus hiérarchique repose sur un manager LLM auto-généré — pratique mais c'est un orchestrateur non déterministe ; et le consensuel n'existe que sur le papier.

## Source primaire
Non citée académiquement par IBM — voir la documentation CrewAI et le dépôt crewAI-examples de Moura (hors-corpus).

## Voir aussi
- [langchain](langchain.md)
- [autogen-ag2](autogen-ag2.md)
