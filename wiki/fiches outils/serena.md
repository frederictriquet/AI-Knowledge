---
outil: "Serena"
titre: "Serena"
themes: [frameworks-outillage, outils-function-calling]
type: "Serveur MCP / toolkit d'agent de codage"
url: https://github.com/oraios/serena
modele_economique: "Open-source (MIT), gratuit ; plugin JetBrains payant en option (essai gratuit)"
cout_llm: "Aucun LLM propre — outil pour LLM, BYO client ; s'appuie sur LSP (déterministe), pas d'inférence"
objectifs: [generer-code]
famille: "Connaissance du code : graphes, recherche & mémoire"
eco_icones: "🔓"
cout_icones: "🟢"
resume: "Toolkit MCP (Python, Oraios) donnant aux agents des capacités IDE via LSP : recherche **et édition/refactoring** sémantiques au niveau symbole sur 40+ langages (pas du grep). MIT open-source (plugin JetBrains payant en option), BYO client"
---

# Serena

**En une phrase** — « l'IDE de ton agent » : un toolkit MCP qui donne aux agents de codage des capacités de niveau IDE — recherche, édition, refactoring et débogage **sémantiques au niveau symbole** via le Language Server Protocol — au lieu d'une simple recherche textuelle.

## Type & intégration
**Serveur MCP** (et CLI), écrit en **Python** (~90 %), par **Oraios AI**. Se branche sur les clients compatibles MCP en fournissant une commande de lancement ou une URL HTTP : Claude Code, Claude Desktop, Cursor, Cline, extensions VS Code, JetBrains, outils de terminal… Supporte **40+ langages** via des backends **LSP** (ou l'analyse des IDE JetBrains). Intégration **Agno** également (pour l'utiliser avec des modèles open-weights).

## Modèle économique
- **Core open-source, licence MIT**, gratuit.
- **Plugin JetBrains payant** (avec essai gratuit) pour des capacités renforcées.

Modèle « open-core léger » : l'essentiel est gratuit/MIT, l'extension JetBrains est l'option commerciale.

## Coût LLM
**Aucun LLM propre** 🟢 — Serena est un **outil *pour* les LLM**, pas un modèle : il faut un LLM (via ton client) pour orchestrer l'usage des outils. Aucun coût LLM côté Serena ; tu apportes ton client (Claude Code, Cursor…). Le travail d'analyse repose sur **LSP** (déterministe, symbol-level), pas sur des embeddings ni de l'inférence. À noter : dispo même avec le tier gratuit de Claude (support MCP), et utilisable avec des modèles open-weights via Agno.

## À quoi ça sert
Combler le manque de compréhension « niveau IDE » des agents : naviguer le code par symboles, trouver définitions/références, éditer et refactorer précisément, déboguer — y compris sur de gros projets complexes, là où le grep/RAG textuel patine. Exploite la **structure relationnelle** du code (symboles, références) plutôt que le texte brut.

## Notes / à creuser
- **Famille 2 (connaissance du code)**, mais angle distinct : Serena = **LSP, symbol-level, avec édition/refactoring** ; [CodeGraph](codegraph.md) et [GraphMind](graphmind.md) = graphe tree-sitter (surtout lecture/navigation) ; [Polaris (polarismcp.com)](polaris.md) = recherche sémantique de docs ; [Cavemem](cavemem.md) = mémoire. Serena est le plus « IDE actif » (il modifie le code, pas seulement le comprendre).
- LSP-based → précision sur le code réel (pas d'approximation), au prix de dépendre d'un serveur de langage par langage.
- Très répandu comme MCP « couteau suisse » de compréhension de code pour agents.

## Source
- Dépôt : https://github.com/oraios/serena
- Docs/lobehub, mcpservers.org, apidog (guides Serena MCP)

*(vérifié le 2026-06-15 — README GitHub + recherche web)*
