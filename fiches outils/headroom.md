---
outil: "Headroom"
titre: "Headroom"
type: "CLI / Proxy / Serveur MCP / Bibliothèque"
url: https://github.com/headroomlabs-ai/headroom
modele_economique: "Open-source"
cout_llm: "Intégré"
---

# Headroom

**En une phrase** — couche de **compression de contexte** open-source (Apache 2.0) qui réduit de 60–95 % les tokens envoyés aux LLM (sorties d'outils, logs, chunks RAG, fichiers, historique de conversation) **avant** l'appel, par compression déterministe — sans LLM propre ni clé.

## Type & intégration
Multi-format, à brancher au plus près de ton usage :
- **Bibliothèque** Python/TypeScript : `compress(messages)`.
- **Proxy** agnostique au langage : `headroom proxy --port 8787` (zéro changement de code, pour tout client compatible OpenAI).
- **Wrapper CLI** d'agents de codage : `headroom wrap claude|codex|cursor|aider|copilot`.
- **Serveur MCP** : outils `headroom_compress`, `headroom_retrieve`, `headroom_stats`.
- **Middleware** pour frameworks (agno, langchain…).

Install : `pip install "headroom-ai[all]"` (Python 3.10+, options granulaires `[proxy]`/`[mcp]`/`[ml]`/`[code]`/`[memory]`…), `npm install headroom-ai`, ou `docker pull ghcr.io/chopratejas/headroom:latest`.

## Modèle économique
**Open-source, gratuit**, sous licence **Apache 2.0**. Tourne en local (« your data stays here ») — pas d'offre payante ni de service hébergé identifié à la source.

## Coût LLM
**🟢 Intégré.** La compression est **déterministe / heuristique, sans appel LLM** : moteurs `SmartCrusher` (JSON), `CodeCompressor` (AST-aware : Python, JS, Go, Rust, Java, C++), et un modèle `Kompress-base` (modèle HuggingFace **local**, pas un service API). En mode wrapper/proxy, Headroom **se place devant la clé/l'abonnement existant** de l'agent (Claude Code, Cursor, Aider…) et n'exige **pas de clé propre** — il ne revend pas de tokens, il en *réduit le volume*. Le bénéfice est sur la facture de **ton** fournisseur, en aval.

## À quoi ça sert
Faire entrer plus d'info utile dans la fenêtre de contexte et **baisser la facture LLM** des agents : compresser les gros payloads (sorties de tools volumineuses, logs, RAG, fichiers, historique) avant l'envoi au modèle. Voisin de [RTK](rtk.md) et [Tokenade](tokenade.md), mais couvre plus de surfaces (lib + proxy + MCP + wrapper + middleware) et de modalités (JSON, code AST, conversation, image).

## Notes / à creuser
- Annonce « 60–95 % » : ordre de grandeur éditeur, à mesurer sur ses propres payloads (qualité de réponse vs taux de compression).
- Compression déterministe ≠ résumé LLM : pas de perte « sémantique » par hallucination, mais le gain dépend de la structure des données (JSON/code très compressibles, prose moins).
- Org GitHub `headroomlabs-ai`, images publiées sous `ghcr.io/chopratejas/*` (auteur Tejas Chopra).

## Source
- Repo : https://github.com/headroomlabs-ai/headroom — README (mécanique de compression, modes d'intégration, install), licence Apache 2.0. *(vérifié le 2026-06-23)*
