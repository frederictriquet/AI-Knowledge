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
2026-06-17  LINT  Correctif Obsidian : lien cassé (cible = phrase URL-encodée de 355 car., artefact HTML→md) retiré dans sources/ibm-guide-agents-ia/md/27-multi-agent-collaboration.md → supprime un nœud ENAMETOOLONG du graphe.
