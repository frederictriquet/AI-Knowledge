---
outil: "Exa MCP"
titre: "Exa MCP"
themes: [rag-contexte]
type: "Serveur MCP (recherche web / neuronale)"
url: https://github.com/exa-labs/exa-mcp-server
modele_economique: "Serveur MCP open-source (MIT) + API Exa payante à l'usage"
cout_llm: "Intégré côté LLM (mais clé Exa payante à l'usage pour la recherche)"
---

# Exa MCP

**En une phrase** — Serveur MCP donnant à l'agent la **recherche web** (et code, et recherche d'entreprises) via l'API de **recherche neuronale Exa** — plus large que la doc de librairies : le web ouvert.

## Type & intégration
Serveur MCP exposant `web_search_exa` (recherche web) et `web_fetch_exa` (récupération de page complète). En local ou via l'endpoint hébergé `https://mcp.exa.ai/mcp` (clé API passée en paramètre/variable d'env). Compatible Claude, Cursor, etc.

## Modèle économique
**Serveur MCP open-source — MIT** et gratuit. **Mais** il requiert une **clé API Exa** : Exa est une **API de recherche payante à l'usage** (par requête ; tier gratuit/crédits de départ disponibles). Le coût réel n'est donc pas dans le serveur MCP mais dans l'**API Exa** consommée.

## Coût LLM
**🟢 côté LLM** : Exa MCP ne génère pas de tokens LLM. ⚠️ En revanche il consomme des **crédits de recherche Exa** (BYO clé Exa, facturée à la requête) — un coût *à l'usage* distinct du LLM, à ne pas oublier.

## À quoi ça sert
Donner à l'agent un **accès web de qualité** (recherche sémantique/neuronale) pour de la recherche en temps réel, pas seulement de la doc de libs. Utile quand le besoin déborde la documentation technique.

## Notes / à creuser
- Seul de la famille à avoir un **coût à l'usage** propre (l'API Exa), vs Context7/GitMCP/MS Learn/AWS docs gratuits.
- Vérifier le pricing Exa courant avant un usage intensif.

## Source
https://github.com/exa-labs/exa-mcp-server (MIT) · https://exa.ai/. *(vérifié le 2026-06-17 ; pricing Exa à reconfirmer à la source)*
