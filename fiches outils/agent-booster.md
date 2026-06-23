---
outil: "Agent Booster"
titre: "Agent Booster"
type: "Serveur MCP / CLI"
url: https://github.com/sseshachala/agent-booster
modele_economique: "Open-source"
cout_llm: "Intégré"
---

# Agent Booster

**En une phrase** — serveur MCP open-source (MIT, Python) qui indexe une codebase en **symboles** (tree-sitter + embeddings **locaux**) et, quand l'agent veut lire un fichier, ne renvoie que les **symboles pertinents** au lieu du fichier entier → 60–90 % de tokens en moins (5–15× de réduction de coût annoncée), **sans LLM ni clé propres**.

## Type & intégration
**Serveur MCP** + **CLI**. `booster init <platform>` écrit des **hooks** qui redirigent les opérations *Read* de l'agent vers l'outil `smart_read`, lequel fait une recherche vectorielle par fichier et ne retourne que les fonctions/classes correspondantes (par plage de lignes). Plateformes : **Claude Code, Cursor, Windsurf, OpenAI Codex**.

Commandes : `init` (configurer l'outil) · `index` (parser/extraire les symboles) · `embed` (construire les embeddings) · `search` (recherche par mot-clé) · `route` (recommande la taille de modèle haiku/sonnet/opus) · `serve` (démarrer le serveur MCP) · `gain` (suivi des économies de tokens).

## Modèle économique
**Open-source, gratuit**, licence **MIT** (© 2026 conductai). Pas d'offre commerciale identifiée.

## Coût LLM
**🟢 Intégré.** Agent Booster **n'utilise aucun LLM** et **ne prend pas de clé** : il optimise la conso de **ton agent existant** (dont tu fournis déjà la clé/abonnement à sa plateforme). Les embeddings sont **locaux et hors-ligne** : *« Uses `all-MiniLM-L6-v2` (local, no data leaves your machine) »* via `sentence-transformers`, construits à l'étape `booster embed`. Aucun appel réseau payant pour l'indexation. Cas typique du « pilote l'agent existant » → 🟢, pas 🔑.

## À quoi ça sert
Réduire le contexte que l'agent charge à chaque lecture : au lieu d'avaler des fichiers entiers, il ne reçoit que les symboles sémantiquement utiles → moins de tokens, moins de « context rot », coût agent plus bas. Voisin de [CodeGraph](codegraph.md) et [Polaris](polaris.md) (index de code local, déterministe, réduit les tokens) ; le bonus `route` ajoute une recommandation de taille de modèle.

## Notes / à creuser
- ⚠️ **Homonymie** : ne pas confondre avec l'autre **`agent-booster`** (ruvnet, Rust/WASM, accélérateur d'*application* d'éditions de code) — produit différent, même nom.
- ⚠️ **Friction read-before-write (surtout Claude Code)** : le hook `PreToolUse` **bloque le `Read` natif** sur les fichiers indexés et force l'outil MCP `smart_read`. Or sur Claude Code, `Edit`/`Write` exigent un **`Read` natif préalable** du fichier (sinon « File has not been read yet ») — une lecture partielle `offset`/`limit` suffit, mais un outil MCP **ne pose pas** ce flag. Donc `smart_read` couvre surtout les lectures **d'exploration/compréhension** (l'essentiel des lectures d'un agent) ; le cycle **lire-pour-éditer** se heurte à cette précondition, et le fallback « full Read » prévu en cas d'absence de match retombe sur un `Read`… lui-même bloqué. Le README **n'adresse pas** ce point. Les agents à édition par *diff/patch* (Cursor/Windsurf/Codex) ont un modèle différent → friction surtout côté Claude Code. *(vérifié au README, 2026-06-23)*
- Annonces « 60–90 % » / « 5–15× » : ordres de grandeur éditeur, à mesurer sur son repo (`booster gain`).
- Granularité symbole : pertinent surtout sur des langages bien couverts par tree-sitter ; qualité du `smart_read` dépend de la qualité des embeddings MiniLM (modèle léger).

## Source
- Repo : https://github.com/sseshachala/agent-booster — README (mécanique hooks/`smart_read`, embeddings locaux `all-MiniLM-L6-v2`, commandes, plateformes), LICENSE (MIT, © 2026 conductai). *(vérifié le 2026-06-23)*
