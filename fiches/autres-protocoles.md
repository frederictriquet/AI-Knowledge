---
titre: "Autres protocoles : ANP / AG-UI / Agora / LMOS"
theme: protocoles-interop
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-protocols
source_titre: "Que sont les protocoles des agents IA ?"---

# Autres protocoles : ANP / AG-UI / Agora / LMOS

> Fiche du glossaire des patterns · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [32-ai-agent-protocols](../sources/ibm-guide-agents-ia/md/32-ai-agent-protocols.md)

**En une phrase** — quatre protocoles émergents au-delà du trio MCP/A2A/ACP : ANP (P2P + identité W3C DID), AG-UI (UI temps réel orientée événements), Agora (négociation de protocole en langage naturel) et LMOS (Internet of Agents d'Eclipse).

## Ce que dit le corpus
IBM décrit quatre protocoles additionnels. **ANP (Agent Network Protocol)** vise à être « le HTTP de l'ère agentique » : transport HTTP, formatage JSON-LD, architecture pair-à-pair en trois couches (identité avec chiffrement de bout en bout et authentification décentralisée W3C DID, méta-protocole de négociation, protocole d'application pour capacités et découverte). **AG-UI (Agent-User Interaction)** normalise la connexion entre agents back-end et applications front-end : architecture orientée événements (messages, appel d'outils, exécution de tâches), interaction homme-agent en temps réel, middleware multi-transport (SSE, webhooks, WebSockets). **Agora** est un protocole inter-agents alimenté par LLM : les agents décrivent leurs propres protocoles en texte brut (métadonnées + mode de communication en langage naturel et code) puis négocient de manière autonome ; HTTPS + JSON, identifiants par hachage. **LMOS (Language Model Operating System)**, de l'Eclipse Foundation, vise un Internet des agents (IoA) : trois couches (identité/sécurité avec W3C DID et OAuth 2.0, transport adaptable, application en JSON-LD avec sous-protocole WebSocket), découverte dynamique ou décentralisée.

## Tradeoff / insight pour un senior
Le corpus prévient : ces protocoles sont jeunes, peu déployés à grande échelle, spécifications mouvantes — prévoir l'adaptation. À retenir comme axes de différenciation : décentralisation/identité (ANP, LMOS via W3C DID), couche UI temps réel (AG-UI, qui adresse un besoin orthogonal à A2A/ACP), et négociation dynamique de protocole en langage naturel (Agora, pari conceptuel le plus singulier).

## Source primaire
Citée par IBM : agent-network-protocol.com (ANP), docs.ag-ui.com (AG-UI), agoraprotocol.org (Agora), eclipse.dev/lmos (LMOS).

## Voir aussi
- [a2a](a2a.md)
- [acp](acp.md)
