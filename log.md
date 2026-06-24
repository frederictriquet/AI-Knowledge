# Journal du corpus (log)

Journal **append-only** des opérations sur la base de connaissances — inspiré du pattern *[LLM Wiki](fiches/llm-wiki-karpathy.md)* (Karpathy). Une ligne par événement, **la plus récente en bas**. On **ajoute**, on ne réécrit jamais (l'historique git existe en plus ; ce log est la vue *orientée connaissance*, lisible sans git).

**Format** : `AAAA-MM-JJ  TYPE  message`

Préfixes `TYPE` (parsables) :

| Préfixe | Sens |
|---------|------|
| `INGEST` | source intégrée → fiche(s) concept dans `fiches/` |
| `TOOL` | outil ajouté/mis à jour dans le recensement (`fiches outils/`, Q1/Q2) |
| `STRUCT` | changement de structure (familles, fichiers, index, ancres) |
| `UPDATE` | mise à jour d'un fait (prix, licence, statut) |
| `DEPRECATE` | outil/fiche déprécié, racheté ou retiré |
| `LINT` | passe de contrôle (fraîcheur, contradictions, doublons, liens) |
| `NOTE` | décision ou remarque |

---

2026-06-15  STRUCT  Recensement d'outils éclaté en 3 fichiers par question (Q1 produire du code / Q2 IA dans un produit / Q3 autres métiers) + `outils IA.md` devient l'index.
2026-06-15  TOOL  Q2 fam.8 LLMOps (éval & observabilité) : Langfuse, LangSmith, Braintrust, Helicone, Phoenix/Arize.
2026-06-16  TOOL  Q2 fam.9 Passerelles / routeurs LLM : OpenRouter, LiteLLM, Portkey, Requesty (+ fiche concept observabilite-llm-best-practices).
2026-06-17  INGEST  Addy Osmani « Agentic Code Review » → fiches revue-de-code-agentique, reviewers-heterogenes.
2026-06-17  TOOL  Q1 fam.7 Revue de code par IA : CodeRabbit, Greptile, Sentry Seer, Cursor BugBot.
2026-06-17  TOOL  Q1 fam.1a/1b/4 : Continue, Crystal, Sculptor, GitHub Spec Kit, Task Master, Pheromind ; Q2 fam.4 : Flowise, Sim, Gumloop, Relay.app.
2026-06-17  TOOL  Q1 fam.8 Documentation & sources MCP externes : Ref, Context7, GitMCP, Exa MCP, Microsoft Learn MCP, AWS Documentation MCP.
2026-06-17  DEPRECATE  Continue racheté par Cursor (avr. 2026) ; Crystal déprécié → Nimbalyst (fév. 2026) ; AutoGen en maintenance mode — notés dans fiches + tableaux.
2026-06-17  INGEST  Addy Osmani « Loop Engineering » → fiches loop-engineering, dette-de-comprehension ; grille composants→familles dans l'index.
2026-06-17  STRUCT  Ancres HTML `#fam-N` sur tous les titres de famille (Q1/Q2) ; index « Familles par question » et grille rendus cliquables.
2026-06-17  INGEST  Karpathy « LLM Wiki » → fiche llm-wiki-karpathy.
2026-06-17  STRUCT  Ajout de ce journal `log.md` + de l'outil `tools/kb_staleness.py` (lint de fraîcheur des fiches outils).
2026-06-17  LINT  Audit contradictions/liens (agent) : 0 lien cassé, 0 ancre cassée, 0 fait périmé non propagé ; 3 icônes corrigées — Chroma +🎁, LanceDB −🎁 (free tier Cloud non confirmé en source), Task Master coût LLM +🟢 (mode hébergé Hamster).
2026-06-17  STRUCT  Slash-commands du process créées dans `.claude/commands/kb/` : /kb:ingest, /kb:tool, /kb:analyze, /kb:query, /kb:lint, /kb:log (documentées dans le README).
2026-06-17  UPDATE  Fiche llm-wiki-karpathy enrichie : section « Où est la partie LLM » (opérateur pas composant ; effort déplacé read-time → write-time ; partage hybride déterministe/LLM).
2026-06-17  NOTE  Décision : liens internes en **markdown** (pas wikilinks) → compatibles GitHub ET Obsidian (graphe/backlinks). Obsidian-ready via note d'accueil `Accueil.md` (MOC + requêtes Dataview), pas via `[[ ]]`.
2026-06-17  STRUCT  Création de `process/SCHEMA.md` (couche 3 Karpathy : source unique structure/conventions/carte des fichiers, anti-drift par renvoi aux sources canoniques). Les 6 commandes `/kb:*` y sont ancrées ; correctifs : `tool.md` ne redéfinit plus la légende (→ `outils IA.md`), préflight venv dans `ingest`/`lint`, `allowed-tools` de `lint` élargi (audit + corrections).
2026-06-17  STRUCT  Nouvelle commande `/kb:refresh` (maintenance update/deprecate : re-vérif à la source → propagation cohérente fiche+tableaux+log ; niveau « mixte » auto/OK ; lancée à la demande, pas de cron). Ajoutée au README et à `SCHEMA.md` §5.
2026-06-17  STRUCT  Rappel de fraîcheur sans cron : `tools/kb_reminder.py` (one-liner, réutilise kb_staleness) + hook `SessionStart` dans `.claude/settings.json` (rappel à l'ouverture du projet) + nudge de clôture dans `/kb:query` et `/kb:tool`. Le refresh reste déclenché par l'humain.
2026-06-17  LINT  Correctif Obsidian : lien cassé (cible = phrase URL-encodée de 355 car., artefact HTML→md) retiré dans sources/ibm-guide-agents-ia/md/27-multi-agent-collaboration.md → supprime un nœud ENAMETOOLONG du graphe.
2026-06-18  STRUCT  Vue transversale `SDLC - outils IA par phase.md` : diagramme Mermaid SDLC (plan→spec→coder→tester→revoir→sécuriser→opérer) mappé aux familles Q1/Q2 + table de liens. Gap assumé phase 7 (déploiement/ops). Reliée depuis le hub `outils IA.md`.
2026-06-18  TOOL  Q1 fam.9 « CI/CD, livraison & ops (IA) » créée (comble la phase 7 du SDLC) : Mergify (merge queue/flaky, 🎁🔁/📦) + AI SRE Cleric · Resolve.ai · Traversal (🔒/📦, enterprise/sur devis). Diagramme SDLC mis à jour (phase 7 remplie, note « gap » levée) ; candidats restants (Datadog Bits AI, Aviator, Trunk, Rootly, PagerDuty AIOps, Pulumi AI) ajoutés à `outils candidats.md`.
2026-06-23  TOOL  Q1 fam.3 (Optimisation tokens) : Headroom (Apache 2.0, 🔓/🟢) — couche de compression de contexte multi-format (lib Py/TS, proxy, wrapper d'agents, MCP, middleware), compression déterministe sans LLM ni clé propre, voisin de RTK/Tokenade.
2026-06-23  TOOL  Q1 fam.3 (comportement de l'agent) : dupehound (MIT, 🔓/🟢) — détecteur de code dupliqué (Rust, tree-sitter+winnowing, sans LLM) pour bases écrites par l'IA : scan/history/check (gate CI + slop score) + mode MCP pour réutiliser au lieu de réécrire. ⚠️ Jeune (v0.1.2). Famille discutable (qualité/anti-duplication ≠ tokens) — rangé en fam.3 par l'angle « réduire le périmètre du code produit », à isoler si d'autres outils du genre arrivent.
2026-06-23  TOOL  Q1 fam.2 (connaissance du code) : Agent Booster (MIT, 🔓/🟢) — serveur MCP/CLI (Python, conductai) qui indexe la codebase en symboles (tree-sitter + embeddings locaux all-MiniLM-L6-v2) et détourne les Read de l'agent pour ne renvoyer que les symboles pertinents (60–90 % de tokens en moins) ; hooks Claude Code/Cursor/Windsurf/Codex, sans LLM ni clé. ⚠️ Homonyme du agent-booster de ruvnet (autre produit).
2026-06-23  NOTE  Fiche agent-booster enrichie (Notes) : friction read-before-write — le hook PreToolUse bloque le Read natif et force smart_read (MCP), mais Edit/Write de Claude Code exigent un Read natif préalable → smart_read couvre surtout les lectures d'exploration, pas le cycle lire-pour-éditer ; README muet sur ce point. Vérifié à la source.
2026-06-23  STRUCT  Conformité OKF (Open Knowledge Format) adoptée comme couche de compatibilité, schéma maison conservé comme sur-ensemble strict (cf. SCHEMA.md §9). Passe minimale : `type` ajouté au frontmatter des 169 fiches concept (= "Concept") + règle dans `kb_lint.py` ; 150 wikilinks Obsidian `[[slug]]` convertis en liens markdown `[Nom](slug.md)` dans 45 fiches outils ; `index.md` (point d'entrée réservé OKF) généré par `build_index.py`. Non adopté : renommage clés FR→EN, chemins absolus (casseraient Obsidian).
2026-06-23  INGEST  Fiche concept `hooks-deterministes-vs-memoire-probabiliste` (gouvernance-alignement-ops, 🟡) : triade Skills=conseil / Memory(CLAUDE.md)=rappel / Hooks=loi, articulée sur la nature d'exécution (LLM probabiliste vs commande shell déterministe). Sourcée sur la doc Claude Code (memory + hooks-guide + skills, archivée dans `sources/claude-code-docs/`), pas sur le post Reddit d'origine. Insight senior ajouté : critère coût-de-contexte × fiabilité (Hook = 0 token, CLAUDE.md = chargé chaque tour). Dédup NOUVEAU (max 0.63). Voir aussi loop-engineering, guardrail-noeud-entree, dual-llm-pattern.
2026-06-24  STRUCT  Pont concepts↔outils. Axe topique partagé : champ `themes: [...]` (sous-ensemble des 14 thèmes) ajouté aux 92 fiches outils + `_TEMPLATE.md`, orthogonal à la famille Q. Pages-hub `MOC/<theme>.md` générées par `build_index.py` (concepts + outils par thème) ; `INDEX-THEMATIQUE.md` devient leur sommaire. Recherche hybride locale `tools/kb_search.py` (lexical TF-IDF + sémantique fastembed, 0 LLM) sur les deux corpus ; `kb_embed.py` indexe désormais concepts + outils, `kb_dedup.py` reste concepts-only. Graphe Obsidian : 3 groupes colorés (concepts/outils/MOC), hubs masqués, forces resserrées. SCHEMA.md §2/§4/§6 et `/kb:tool` mis à jour.
2026-06-24  NOTE  Règle gravée dans `CLAUDE.md` (projet) : interdit de consigner de l'historique/justification de changement dans le contenu des fichiers (commentaires, docstrings, fiches) — présent intemporel uniquement ; l'historique de décisions va dans `log.md` ou un ADR, sur décision de l'utilisateur.
