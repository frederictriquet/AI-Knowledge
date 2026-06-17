---
outil: "AWS Documentation MCP"
type: "Serveur MCP local (doc AWS officielle)"
url: https://github.com/awslabs/mcp
modele_economique: "Open-source (Apache 2.0) — gratuit"
cout_llm: "Intégré (source de doc ; ne génère pas de LLM)"
---

# AWS Documentation MCP

**En une phrase** — Serveur MCP **officiel AWS Labs** donnant à l'agent l'accès à la **documentation AWS officielle** à jour (docs, API references, What's New), pour coder juste sur AWS.

## Type & intégration
Serveur MCP **local** (transport stdio), à configurer dans l'agent (install 1-clic dans Kiro, Cursor, VS Code…). Permet de rechercher et lire la doc AWS, les références d'API et les nouveautés. C'est **l'un des nombreux serveurs MCP** du dépôt `awslabs/mcp` (qui couvre aussi d'autres capacités AWS).

## Modèle économique
**Open-source — Apache 2.0**, gratuit. Maintenu par **AWS Labs**.

## Coût LLM
**🟢 Intégré** : source de doc — pas de génération LLM ; tourne dans ton agent. (Le serveur de doc lui-même n'appelle pas de service AWS facturé.)

## À quoi ça sert
Coder juste sur l'**écosystème AWS** en s'appuyant sur la doc officielle à jour. Pendant côté Microsoft : [Microsoft Learn MCP](microsoft-learn-mcp.md).

## Notes / à creuser
- Self-hostable (local stdio) → pas de dépendance à un service tiers, contrairement à MS Learn MCP (remote).
- Le repo `awslabs/mcp` contient d'autres serveurs (API AWS, IaC…) — ici, seul le serveur **Documentation** est recensé.

## Source
https://github.com/awslabs/mcp (LICENSE = Apache 2.0, serveur `aws-documentation`). *(vérifié le 2026-06-17)*
