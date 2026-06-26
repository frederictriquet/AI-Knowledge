---
outil: "GitMCP"
titre: "GitMCP"
themes: [rag-contexte]
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
**Gratuit**, open-source (repo `idosal/git-mcp`, **licence Apache-2.0**, ~8,2k★).

## Coût LLM
**🟢 Intégré** : source de contexte — pas de génération LLM propre ; tourne dans ton agent.

## À quoi ça sert
Donner à l'agent la **doc/le code d'un projet GitHub précis** sans cloner ni charger tout le repo dans le contexte. Complémentaire de Context7/Ref (qui indexent un large catalogue de libs) quand on cible **un** repo donné.

## Notes / à creuser
- ⚠️ **Service hébergé tiers** (gitmcp.io) → dépendance externe + envoi du contexte du repo à un service que tu ne contrôles pas ; pour du privé/sensible, préférer un MCP local.
- Lit surtout `llms.txt`/`readme.md` : sur un repo **sans** fichiers de contexte soignés, l'utilité chute (il ne « comprend » pas le code, il sert ce qui est exposé).

## Source
https://gitmcp.io/ · https://github.com/idosal/git-mcp (Apache-2.0). *(vérifié le 2026-06-24 — API GitHub : licence Apache-2.0, ~8,2k★)*
