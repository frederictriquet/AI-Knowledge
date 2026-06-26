---
outil: "CodeGraph"
titre: "CodeGraph"
themes: [rag-contexte]
type: "Serveur MCP / CLI"
url: https://colbymchenry.github.io/codegraph/
modele_economique: "Open-source (MIT), gratuit"
cout_llm: "Aucun coût LLM propre — n'utilise pas de LLM, tourne dans l'agent (réduit la conso de tokens)"
objectifs: [generer-code]
famille: "Connaissance du code : graphes, recherche & mémoire"
eco_icones: "🔓"
cout_icones: "🟢"
resume: "Indexe une codebase en graphe de connaissances local (tree-sitter + SQLite) exposé aux agents via MCP ; déterministe, sans LLM, réduit tool calls et tokens"
---

# CodeGraph

**En une phrase** — outil open-source qui transforme n'importe quelle codebase en graphe de connaissances local et interrogeable, exposé aux agents de codage IA via MCP, pour qu'ils explorent le code avec beaucoup moins d'appels d'outils et de tokens.

## Type & intégration
À la fois **CLI** (`npx @colbymchenry/codegraph`) et **serveur MCP**, compatible avec Claude Code, Cursor, Codex CLI, OpenCode, Gemini, etc. Il parse le code avec **tree-sitter**, stocke symboles / arêtes / fichiers dans **SQLite (FTS5)**, et expose ce graphe (symboles, call graph, structure) aux agents par MCP. Auto-sync via les file watchers natifs de l'OS. Installation npm (`@colbymchenry/codegraph`). 19+ langages supportés, détection de routes « framework-aware » pour ~13 frameworks.

## Modèle économique
**Open-source, licence MIT**, gratuit. Pas d'offre payante apparente — projet communautaire sur GitHub.

## Coût LLM
**Aucun coût LLM propre** 🟢. C'est un cas particulier de la catégorie « Intégré » : CodeGraph **n'appelle aucun LLM** — l'extraction est *déterministe*, dérivée de l'AST (pas de résumé par LLM), et tourne **100 % en local sans clé API**. Mieux : il *fait baisser* la facture LLM de l'agent qui l'utilise, en remplaçant les coûteux scans de fichiers par des requêtes sur le graphe pré-indexé.

Bénéfice mesuré (benchmarks annoncés sur 6 codebases réelles) : ~**92 % de tool calls en moins** et ~**71 % d'exploration plus rapide** en moyenne → donc moins de tokens consommés côté agent.

## À quoi ça sert
Donner à un agent de codage une carte structurée du dépôt : navigation symboles/références, **analyse d'impact** (tracer comment un changement se propage), compréhension rapide d'un gros codebase — sans relire les fichiers à chaque fois. Complémentaire des agents comme [Kilo Code](kilo-code.md) ou de Claude Code : c'est une couche d'indexation, pas un agent.

## Notes / à creuser
- Déterministe (AST) ≠ recherche sémantique par embeddings : pas d'« approximation » LLM, mais pas non plus de similarité de sens.
- 100 % local → bon pour la confidentialité (aucune donnée envoyée à un tiers).
- Se branche en MCP : intéressant à coupler avec n'importe quel agent MCP-compatible pour réduire les coûts/latence.
- ⚠️ Benchmarks « ~92 % de tool calls en moins / ~71 % plus rapide » auto-déclarés par l'auteur (non reproduits indépendamment) ; la qualité dépend de la couverture tree-sitter du langage — à mesurer sur ton propre repo.

## Source
- Site/landing : https://colbymchenry.github.io/codegraph/
- Dépôt : https://github.com/colbymchenry/codegraph

*(vérifié le 2026-06-15 — landing officielle + GitHub + recherche web)*
