---
outil: "Microsoft Learn MCP"
type: "Serveur MCP distant (doc Microsoft officielle)"
url: https://learn.microsoft.com/training/support/mcp
modele_economique: "Propriétaire (service hébergé Microsoft) — gratuit, sans auth"
cout_llm: "Intégré (source de doc ; ne génère pas de LLM)"
---

# Microsoft Learn MCP

**En une phrase** — Serveur MCP **officiel Microsoft** servant la documentation Microsoft/Azure officielle et à jour directement à l'agent (le service « Ask Learn » qui alimente Copilot for Azure).

## Type & intégration
Serveur MCP **distant** (HTTP streamable), connectable depuis GitHub Copilot, VS Code, Visual Studio, Copilot Studio et autres agents. Trois usages : rechercher dans la doc, récupérer un article complet, chercher des exemples de code. Le service de connaissances se rafraîchit en continu (full refresh quotidien).

## Modèle économique
**Propriétaire** (service hébergé par Microsoft), mais **gratuit** et **sans authentification** — publiquement accessible, aucun coût d'usage du serveur MCP.

## Coût LLM
**🟢 Intégré** : source de doc — pas de génération LLM ; tourne dans ton agent.

## À quoi ça sert
Coder juste sur l'**écosystème Microsoft/Azure/.NET** en s'appuyant sur la doc officielle à jour plutôt que sur la mémoire (potentiellement périmée) du modèle. Équivalent « vendeur » de Context7, côté Microsoft.

## Notes / à creuser
- Service hébergé Microsoft → pas self-hostable, mais gratuit et sans clé.
- Pendant côté AWS : [AWS Documentation MCP](aws-documentation-mcp.md).

## Source
https://learn.microsoft.com/training/support/mcp · https://learn.microsoft.com/en-us/training/support/mcp-developer-reference. *(vérifié le 2026-06-17)*
