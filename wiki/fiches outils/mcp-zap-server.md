---
outil: "MCP ZAP Server"
titre: "MCP ZAP Server"
themes: [securite]
type: "Serveur MCP — opérateur OWASP ZAP"
url: https://github.com/dtkmn/mcp-zap-server
modele_economique: "Open-source (Apache 2.0), gratuit — par dtkmn (non affilié à OWASP)"
cout_llm: "Aucun LLM propre — pont/opérateur ; BYO client MCP (Claude Desktop, Cursor, Open WebUI…)"
---

# MCP ZAP Server

**En une phrase** — serveur MCP qui donne aux agents IA un opérateur **OWASP ZAP** sûr et auto-hébergé pour mener des scans de sécurité web guidés (spider, scan actif/passif), analyser les résultats et générer des rapports.

> 🔐 **Cadre d'usage** : sécurité offensive — tests **autorisés** uniquement, en environnement maîtrisé.

## Type & intégration
**Application Spring Boot (Java ~95 %)** qui expose **OWASP ZAP** comme **serveur MCP** en HTTP streamable. Compatible avec tout client MCP (Claude Desktop, Cursor, Open WebUI — ce dernier bundlé pour tests locaux). Outils MCP « guidés » (spider, scan actif/passif, import OpenAPI, findings, rapports) + contrôles ZAP bas niveau pour workflows avancés. Déploiement **Docker Compose** (local) et **Helm/Kubernetes** (prod).

Posture sécurité soignée : **auth API-key ou JWT**, scopes d'outils, **runtime policy bundles**, **rate limits**, **audit events**, file d'attente de scans, **état durable Postgres**. Défauts conservateurs (clé API par défaut, binding localhost).

## Modèle économique
**Open-source, licence Apache 2.0**, gratuit. Maintenu par **dtkmn (Daniel Tse)** ; contributions via GitHub. ⚠️ **Non affilié** au projet OWASP/ZAP (projet indépendant qui *pilote* ZAP).

## Coût LLM
**Aucun LLM propre** 🟢 — opérateur/pont : le LLM vient de ton client MCP (BYO abonnement/clé). Pas de coût côté serveur. Comme [MCP Kali Server](mcp-kali-server.md) et [Burp Suite MCP Server (PortSwigger)](burp-mcp-server.md), le coût LLM est celui de l'agent qui orchestre.

## À quoi ça sert
Laisser un agent piloter des scans ZAP de façon conversationnelle mais **encadrée** (scopes, quotas, audit), analyser les résultats structurés et produire des rapports lisibles — sans scripts de glue fragiles ni accès brut/non sûr au scanner. Pensé pour une adoption jusqu'en production (guardrails, état persistant).

## Notes / à creuser
- **Famille 9b (sécurité offensive — outils via MCP)** : équivalent open-source/OWASP de [Burp Suite MCP Server (PortSwigger)](burp-mcp-server.md) (Burp, commercial) ; sibling de [MCP Kali Server](mcp-kali-server.md) (arsenal Kali). À distinguer des **agents autonomes** [AIDA (AI-Driven Security Assessment)](aida.md)/[Shannon (Keygraph)](shannon.md) (famille 10).
- Se démarque par ses **garde-fous « production »** (auth, scopes, rate limits, audit, Postgres) — plus mûr côté ops que beaucoup de MCP sécurité communautaires.
- ⚠️ Reste un outil de scan actif (peut perturber une cible) → scope autorisé, isolation réseau.

## Source
- Dépôt : https://github.com/dtkmn/mcp-zap-server · annuaires : glama.ai, mcpservers.org

*(vérifié le 2026-06-15 — README GitHub + recherche web)*
