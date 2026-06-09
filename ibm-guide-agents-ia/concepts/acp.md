# ACP (Agent Communication Protocol)

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [33-agent-communication-protocol](../md/33-agent-communication-protocol.md), [34-acp-ai-agent-interoperability-building-multi-agent-workflows](../md/34-acp-ai-agent-interoperability-building-multi-agent-workflows.md), [32-ai-agent-protocols](../md/32-ai-agent-protocols.md)

**En une phrase** — le protocole agent↔agent de BeeAI/IBM, fondé sur REST/HTTP léger (vs JSON-RPC), asynchrone par défaut, avec découverte hors-ligne ; il a fusionné avec A2A sous la Linux Foundation.

## Ce que dit le corpus
IBM présente l'ACP comme une norme ouverte de communication entre agents, introduite par BeeAI d'IBM et désormais sous la Linux Foundation. Composants : un client ACP et un serveur ACP ; le client envoie des requêtes via une API RESTful sur HTTP, et le serveur héberge un ou plusieurs agents derrière un point HTTP unique, routant les tâches. Fonctionnalités clés : **communication REST** (conventions HTTP standard, utilisable avec cURL, Postman ou un navigateur ; SDK disponible mais non requis), **découverte hors-ligne** (métadonnées intégrées aux paquets de distribution, adaptée aux environnements scale-to-zero ; découverte en ligne possible via manifestes à des URL bien connues), **asynchrone par défaut** (synchrone pris en charge) et acceptation de types de messages variés (audio, images, texte, vidéos, binaire). Le corpus oppose explicitement ACP au MCP : JSON-RPC plus complexe vs conception REST plus légère. Le tutoriel 34 illustre un workflow multi-agents BeeAI + crewAI où ACP sert de couche de messagerie partagée (JSON + métadonnées) via l'`acp-sdk`.

## Tradeoff / insight pour un senior
Conçu délibérément léger et neutre fournisseur : REST + async par défaut convient aux tâches longues et aux contextes inter-organisations décentralisés. La découverte hors-ligne (metadata dans le paquet) est le détail rare et utile : un agent reste découvrable même éteint. Point d'attention : ACP s'est associé à A2A sous la Linux Foundation — surveiller la convergence des SDK.

## Source primaire
Citée par IBM : introduit par BeeAI d'IBM, site officiel agentcommunicationprotocol.dev, dépôt github.com/i-am-bee/acp.

## Voir aussi
- [beeai](beeai.md)
- [a2a](a2a.md)
