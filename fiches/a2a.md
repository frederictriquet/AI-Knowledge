---
titre: "A2A (Agent2Agent)"
theme: protocoles-interop
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/agent2agent-protocol
source_titre: "Qu’est-ce que le protocole A2A (Agent2Agent) ?"
---

# A2A (Agent2Agent)

**En une phrase** — le protocole agent↔agent (Google, avril 2025, désormais Linux Foundation) où chaque agent publie une Agent Card découvrable, puis dialogue en JSON-RPC 2.0 sur HTTPS avec SSE pour le streaming.

## En détail
A2A est un protocole de communication ouvert pour systèmes multi-agents, lancé par Google en avril 2025 et hébergé par la Linux Foundation. Il agit comme un niveau de messagerie permettant à des agents d'architectures distinctes de « parler » entre eux ; complémentaire du MCP (A2A pour l'inter-agents, MCP pour modèle↔outils). Composants : client A2A (agent client qui délègue), serveur A2A (agent distant exposant un point HTTP), **Fiche d'agent** (JSON de métadonnées : nom, description, version, URL, modalités, authentification), Tâche (cycle de vie : envoyée, active, entrée requise, terminée, échouée), Message, Artéfact et Partie (TextPart, FilePart, DataPart). Workflow en trois étapes : **découverte** (récupération des fiches d'agents distants), **authentification** (schémas OpenAPI : clés API, OAuth 2.0, OpenID Connect), **communication** (HTTPS + JSON-RPC 2.0). Tâches longues : notifications push vers webhook ; sorties volumineuses : streaming SSE. En pratique, la fiche est exposée à `/.well-known/agent-card.json`, et BeeAI fournit des adaptateurs A2AServer/A2AAgent.

## Tradeoff / insight pour un senior
A2A traite les agents comme **opaques** (pas d'exposition de la mémoire ni de la logique propriétaire) : bon pour la confidentialité inter-organisations, mais la découverte repose entièrement sur la qualité de l'Agent Card. Compromis vs ACP : A2A est en JSON-RPC/HTTPS et « optimisé pour l'écosystème Google » ; ACP vise REST léger et neutralité. Les deux ont fusionné sous la Linux Foundation.

## Source primaire
Lancé par Google (avril 2025), Linux Foundation, site officiel a2aproject.github.io/A2A/ et exemples github.com/a2aproject/a2a-samples.

## Voir aussi
- [acp](acp.md)
- [mcp](mcp.md)
