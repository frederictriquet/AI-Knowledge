# Corpus journal (log)

**Append-only** journal of operations on the knowledge base — inspired by the *[LLM Wiki](concepts/llm-wiki-karpathy.md)* pattern (Karpathy). One line per event, **the most recent at the bottom**. We **append**, we never rewrite (the git history exists in addition; this log is the *knowledge-oriented* view, readable without git).

**Format**: `YYYY-MM-DD  TYPE  message`

`TYPE` prefixes (parsable):

| Prefix | Meaning |
|---------|------|
| `INGEST` | source integrated → concept note(s) in `concepts/` |
| `TOOL` | tool added/updated in the census (`tools/`) |
| `STRUCT` | structure change (families, files, index, anchors) |
| `UPDATE` | update of a fact (price, license, status) |
| `DEPRECATE` | tool/note deprecated, acquired or retired |
| `LINT` | control pass (freshness, contradictions, duplicates, links) |
| `NOTE` | decision or remark |

---

2026-06-15  STRUCT  Tool census split into 3 files by question (Q1 produce code / Q2 AI in a product / Q3 other professions) + `outils IA.md` becomes the index.
2026-06-15  TOOL  Q2 fam.8 LLMOps (eval & observability): Langfuse, LangSmith, Braintrust, Helicone, Phoenix/Arize.
2026-06-16  TOOL  Q2 fam.9 LLM gateways / routers: OpenRouter, LiteLLM, Portkey, Requesty (+ concept fiche observabilite-llm-best-practices).
2026-06-17  INGEST  Addy Osmani "Agentic Code Review" → fiches revue-de-code-agentique, reviewers-heterogenes.
2026-06-17  TOOL  Q1 fam.7 AI code review: CodeRabbit, Greptile, Sentry Seer, Cursor BugBot.
2026-06-17  TOOL  Q1 fam.1a/1b/4: Continue, Crystal, Sculptor, GitHub Spec Kit, Task Master, Pheromind; Q2 fam.4: Flowise, Sim, Gumloop, Relay.app.
2026-06-17  TOOL  Q1 fam.8 Documentation & external MCP sources: Ref, Context7, GitMCP, Exa MCP, Microsoft Learn MCP, AWS Documentation MCP.
2026-06-17  DEPRECATE  Continue acquired by Cursor (Apr. 2026); Crystal deprecated → Nimbalyst (Feb. 2026); AutoGen in maintenance mode — noted in fiches + tables.
2026-06-17  INGEST  Addy Osmani "Loop Engineering" → fiches loop-engineering, dette-de-comprehension; components→families grid in the index.
2026-06-17  STRUCT  HTML anchors `#fam-N` on all family titles (Q1/Q2); "Families by question" index and grid made clickable.
2026-06-17  INGEST  Karpathy "LLM Wiki" → fiche llm-wiki-karpathy.
2026-06-17  STRUCT  Added this `log.md` journal + the `tools/kb_staleness.py` tool (freshness lint of tool fiches).
2026-06-17  LINT  Contradiction/link audit (agent): 0 broken links, 0 broken anchors, 0 outdated unpropagated fact; 3 icons corrected — Chroma +🎁, LanceDB −🎁 (Cloud free tier not confirmed in source), Task Master LLM cost +🟢 (Hamster hosted mode).
2026-06-17  STRUCT  Process slash-commands created in `.claude/commands/kb/`: /kb:ingest, /kb:tool, /kb:analyze, /kb:query, /kb:lint, /kb:log (documented in the README).
2026-06-17  UPDATE  Fiche llm-wiki-karpathy enriched: "Where is the LLM part" section (operator not component; effort shifted read-time → write-time; hybrid deterministic/LLM sharing).
2026-06-17  NOTE  Decision: internal links in **markdown** (not wikilinks) → compatible with GitHub AND Obsidian (graph/backlinks). Obsidian-ready via the `Accueil.md` welcome note (MOC + Dataview queries), not via `[[ ]]`.
2026-06-17  STRUCT  Creation of `process/SCHEMA.md` (Karpathy layer 3: single source of structure/conventions/file map, anti-drift via reference to canonical sources). The 6 `/kb:*` commands are anchored there; fixes: `tool.md` no longer redefines the legend (→ `outils IA.md`), venv preflight in `ingest`/`lint`, `allowed-tools` of `lint` widened (audit + corrections).
2026-06-17  STRUCT  New command `/kb:refresh` (update/deprecate maintenance: re-verify at source → consistent propagation fiche+tables+log; "mixed" auto/OK level; run on demand, no cron). Added to the README and to `SCHEMA.md` §5.
2026-06-17  STRUCT  Freshness reminder without cron: `tools/kb_reminder.py` (one-liner, reuses kb_staleness) + `SessionStart` hook in `.claude/settings.json` (reminder when opening the project) + closing nudge in `/kb:query` and `/kb:tool`. The refresh remains human-triggered.
2026-06-17  LINT  Obsidian fix: broken link (target = 355-char URL-encoded sentence, HTML→md artifact) removed in sources/ibm-guide-agents-ia/md/27-multi-agent-collaboration.md → eliminates an ENAMETOOLONG node from the graph.
2026-06-18  STRUCT  Cross-cutting view `SDLC - outils IA par phase.md`: Mermaid SDLC diagram (plan→spec→code→test→review→secure→operate) mapped to Q1/Q2 families + link table. Assumed gap on phase 7 (deployment/ops). Linked from the `outils IA.md` hub.
2026-06-18  TOOL  Q1 fam.9 "CI/CD, delivery & ops (AI)" created (fills phase 7 of the SDLC): Mergify (merge queue/flaky, 🎁🔁/📦) + AI SRE Cleric · Resolve.ai · Traversal (🔒/📦, enterprise/quote-based). SDLC diagram updated (phase 7 filled, "gap" note lifted); remaining candidates (Datadog Bits AI, Aviator, Trunk, Rootly, PagerDuty AIOps, Pulumi AI) added to `outils candidats.md`.
2026-06-23  TOOL  Q1 fam.3 (Token optimization): Headroom (Apache 2.0, 🔓/🟢) — multi-format context compression layer (Py/TS lib, proxy, agent wrapper, MCP, middleware), deterministic compression with no LLM or own key, neighbor of RTK/Tokenade.
2026-06-23  TOOL  Q1 fam.3 (agent behavior): dupehound (MIT, 🔓/🟢) — duplicated-code detector (Rust, tree-sitter+winnowing, no LLM) for AI-written codebases: scan/history/check (CI gate + slop score) + MCP mode to reuse instead of rewrite. ⚠️ Young (v0.1.2). Debatable family (quality/anti-duplication ≠ tokens) — placed in fam.3 via the "reduce the scope of produced code" angle, to be isolated if other tools of the kind arrive.
2026-06-23  TOOL  Q1 fam.2 (code knowledge): Agent Booster (MIT, 🔓/🟢) — MCP/CLI server (Python, conductai) that indexes the codebase into symbols (tree-sitter + local embeddings all-MiniLM-L6-v2) and intercepts the agent's Reads to return only the relevant symbols (60–90% fewer tokens); Claude Code/Cursor/Windsurf/Codex hooks, no LLM or key. ⚠️ Namesake of ruvnet's agent-booster (different product).
2026-06-23  NOTE  Fiche agent-booster enriched (Notes): read-before-write friction — the PreToolUse hook blocks the native Read and forces smart_read (MCP), but Claude Code's Edit/Write require a prior native Read → smart_read mainly covers exploration reads, not the read-to-edit cycle; README silent on this point. Verified at source.
2026-06-23  STRUCT  OKF (Open Knowledge Format) conformance adopted as a compatibility layer, in-house schema kept as a strict superset (cf. SCHEMA.md §9). Minimal pass: `type` added to the frontmatter of the 169 concept fiches (= "Concept") + rule in `kb_lint.py`; 150 Obsidian wikilinks `[[slug]]` converted to markdown links `[Name](slug.md)` across 45 tool fiches; `index.md` (OKF-reserved entry point) generated by `build_index.py`. Not adopted: renaming keys FR→EN, absolute paths (would break Obsidian).
2026-06-23  INGEST  Concept fiche `hooks-deterministes-vs-memoire-probabiliste` (gouvernance-alignement-ops, 🟡): triad Skills=advice / Memory(CLAUDE.md)=reminder / Hooks=law, articulated on the nature of execution (probabilistic LLM vs deterministic shell command). Sourced on the Claude Code docs (memory + hooks-guide + skills, archived in `sources/claude-code-docs/`), not on the original Reddit post. Senior insight added: context-cost × reliability criterion (Hook = 0 token, CLAUDE.md = loaded every turn). Dedup NEW (max 0.63). See also loop-engineering, guardrail-noeud-entree, dual-llm-pattern.
2026-06-24  STRUCT  Concepts↔tools bridge. Shared topical axis: `themes: [...]` field (subset of the 14 themes) added to the 92 tool fiches + `_TEMPLATE.md`, orthogonal to the Q family. Hub pages `MOC/<theme>.md` generated by `build_index.py` (concepts + tools per theme); `INDEX-THEMATIQUE.md` becomes their table of contents. Local hybrid search `tools/kb_search.py` (lexical TF-IDF + semantic fastembed, 0 LLM) over both corpora; `kb_embed.py` now indexes concepts + tools, `kb_dedup.py` remains concepts-only. Obsidian graph: 3 colored groups (concepts/tools/MOC), hubs hidden, tightened forces. SCHEMA.md §2/§4/§6 and `/kb:tool` updated.
2026-06-24  NOTE  Rule etched in `CLAUDE.md` (project): forbidden to log history/justification of change in file content (comments, docstrings, fiches) — timeless present only; decision history goes in `log.md` or an ADR, at the user's decision.
2026-06-24  TOOL  ECC (affaan-m/ECC) added to Q1 fam.4 (workflow/methodology), themes [frameworks-outillage, gouvernance-alignement-ops, securite, efficacite-cout]. Multi-platform harness "operator system" (MIT, 🔓🎁🔁; ECC Pro $19/seat/month). LLM cost 🟢🔑: core in the host harness without a key, BYOK multi-provider (Anthropic/OpenAI/Ollama local) for AgentShield/security-scan & autonomous-harness (verified in `src/llm/providers/` + `.cursor/hooks/`). Deliberately critical fiche: created 2026-01-18 (young) despite "production"/"10+ months" rhetoric; maximalist (261 skills/67 agents) in tension with its own "<10 MCP/<80 tools" rule; single maintainer; 220.8k★ in 5 months = hype ≠ proven value; self-declared internal metrics. Focused peers (Superpowers, Spec Kit) often preferable.
2026-06-30  STRUCT  English-only migration. The whole repository switched to English — concept notes (169) and tool notes (93) translated (file names, frontmatter keys **and** values, body markers), the 14 theme slugs and 5 objective slugs anglicized, the `tools/*.py` toolchain (identifiers, strings, comments) ported to an English API (`CONCEPTS`/`TOOLS`/`load_notes`/`note_body`/…), internal docs (`SCHEMA.md`, `ENRICHMENT.md`, `/kb:*` commands), `README.md`, `CLAUDE.md` (new rule: everything English), CI and this journal. Generated marker `AUTO-OUTILS` → `AUTO-TOOLS`. Only `sources/` kept verbatim (raw materials) and references to externally-named artifacts (memory slugs); historical file names already recorded above are left as-is (append-only). Verified: 169-note lint clean, indexes regenerated, search/dedup/staleness smoke-tested.
