---
outil: "GitMCP"
type: "Serveur MCP distant (repo GitHub → MCP)"
url: https://gitmcp.io/
modele_economique: "Gratuit (open-source, idosal/git-mcp)"
cout_llm: "Intégré (source de contexte ; ne génère pas de LLM)"
---

# GitMCP

**En une phrase** — Transforme **n'importe quel repo GitHub** en serveur MCP distant : il suffit de remplacer `github.com` par `gitmcp.io` dans l'URL pour donner à l'agent le contexte d'un projet (doc, code).

## Type & intégration
Serveur MCP **distant**, sans installation locale : on convertit l'URL du repo (`github.com/x/y` → `gitmcp.io/x/y`) et on pointe l'agent dessus. Lit en priorité les fichiers de contexte du repo (`llms.txt`, `llms-full.txt`, `readme.md`). Compatible Claude, Cursor, Windsurf, VS Code, Cline…

## Modèle économique
**Gratuit**, open-source (repo `idosal/git-mcp`). ⚠️ Licence exacte **non confirmée à la source** (à vérifier dans le dépôt avant usage commercial).

## Coût LLM
**🟢 Intégré** : source de contexte — pas de génération LLM propre ; tourne dans ton agent.

## À quoi ça sert
Donner à l'agent la **doc/le code d'un projet GitHub précis** sans cloner ni charger tout le repo dans le contexte. Complémentaire de Context7/Ref (qui indexent un large catalogue de libs) quand on cible **un** repo donné.

## Notes / à creuser
- Service hébergé tiers (gitmcp.io) → dépendance externe ; pour du privé/sensible, préférer un MCP local.
- Licence à confirmer (point ci-dessus).

## Source
https://gitmcp.io/ · https://github.com/idosal/git-mcp. *(vérifié le 2026-06-17 ; licence non confirmée à la source)*
