---
outil: "GraphMind"
titre: "GraphMind"
type: "Application desktop / Serveur MCP / CLI"
url: https://getgraphmind.com/
modele_economique: "Open-source (MIT) freemium + abonnements (9–19 €/mois)"
cout_llm: "🟢🔑 — aucun LLM génératif ; embeddings locaux gratuits par défaut (🟢) ; embeddings distants Voyage AI/OpenAI sur tiers payants = clé requise (🔑 ; BYOK vs inclus dans l'abonnement = ambigu)"
---

# GraphMind

**En une phrase** — transforme une codebase en graphe de connaissances interrogeable par l'IA, avec une mémoire persistante qui garde l'assistant au courant des décisions d'une session à l'autre — jusqu'à 5 700× moins de tokens que la recherche brute.

> ⚠️ Homonymie : « GraphMind » désigne plusieurs produits sans rapport (app de mind-mapping, base de données graphe, etc.). Cette fiche concerne **getgraphmind.com** (graphe de code pour assistants IA, « Made in Paris »).

## Type & intégration
Triple forme, même moteur :
- **Application desktop** (Mac & Windows) — sans terminal : on pointe vers un dossier, l'app configure automatiquement les outils IA et démarre le serveur MCP.
- **CLI** (`graphmind index .`, `graphmind setup`) — install via **Homebrew** (`brew install aouicher/graphmind/graphmind`) ou **Cargo** (Rust).
- **Serveur MCP** exposant **25 outils** à Claude Desktop, Claude Code, Cursor, Windsurf…

Parse chaque fichier avec **tree-sitter**, construit un graphe de symboles dans **DuckDB**, détecte les dépendances cross-projet. 30+ langages.

## Modèle économique
**Freemium**, cœur **open-source MIT** :
- **Free — 0 €** (dispo) : graphe local, projets illimités, 25 outils MCP, store de mémoire SQLite, embeddings locaux (minilm), MIT.
- **Embeddings — 9 €/mois** (bientôt) : recherche sémantique distante via embeddings **Voyage AI**.
- **Pro — 19 €/mois** (bientôt) : API + serveur MCP distants, sans install locale, depuis n'importe quelle machine.
- **Team — 19 €/mois/siège** (bientôt, min. 3) : graphe et mémoires partagés, `gm_team_who_knows`, auto-sync.
- −20 % en annuel.

## Coût LLM
**🟢🔑 — aucun LLM *génératif*** (pas de chat/completion ; extraction déterministe tree-sitter/AST, ranking hybride FTS + sémantique + graphe).
- **Par défaut** : embeddings **locaux** (minilm) → **gratuit, sans clé** (🟢).
- **Tiers payants** : embeddings **distants Voyage AI / OpenAI** → **clé requise** (🔑). ⚠️ Le code exige une clé (BYOK) alors que la page /pricing présente « Voyage AI embeddings » comme un **service inclus** dans le tier à 9 € → **modèle réel (BYOK vs revente incluse) ambigu**, à confirmer.

Effet net : GraphMind *réduit* massivement les tokens de l'agent — ~10 M tokens économisés par session sur 5–10 recherches, jusqu'à 5 700× moins que grep (benchmark sur codebase de 31K symboles).

## À quoi ça sert
Donner à un agent une compréhension structurelle du code **plus une mémoire durable** :
- `gm_search` (recherche par sens, < 300 tokens), `gm_fn` (symbole + callers/callees en un appel), `gm_fn_impact` (rayon d'impact d'un refactor), `gm_dead_code`, `gm_diff_impact` (revue de PR), `gm_similar` (détection de duplication), `gm_cross_links`, `gm_cycles`…
- `gm_memory_add` : mémoire persistante des décisions d'architecture et conventions, rappelées à chaque session.

## Notes / à creuser
- **Synthèse du cluster « réduction de tokens »** : GraphMind réunit en un produit ce que font séparément [CodeGraph](codegraph.md) (graphe de code), [Polaris (polarismcp.com)](polaris.md) (recherche sémantique de docs) et [Cavemem](cavemem.md) (mémoire persistante) — mais en offre commerciale packagée (desktop app + SaaS), là où les autres sont des projets purement open-source/CLI.
- Cœur MIT mais monétisation via embeddings distants + hébergement → modèle « open-core ».
- Écrit en Rust (dispo via Cargo), DuckDB pour le graphe.

## Source
- Site officiel : https://getgraphmind.com/ (et /pricing, /docs) — fetch automatisé bloqué (403), contenu récupéré via curl le 2026-06-15

*(vérifié le 2026-06-15 — landing officielle via curl UA navigateur)*
