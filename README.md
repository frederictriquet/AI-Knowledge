# AI corpus — agents & prompt engineering

Condensed, **sourced** knowledge base on agentic AI and prompt engineering, built from the **IBM Think** hubs then enriched with reference external sources (Lilian Weng, Anthropic, Hamel Husain, Eugene Yan, Simon Willison, The Prompt Report, DeepSeek, OWASP/NIST/MITRE…).

## What it's for

1. **Skill up** — one dense note per concept, with a link to the primary source to dig deeper.
2. **Produce short posts** (internal messaging) — each note fits in a hook ("In one sentence") + a "dig deeper" link.
3. **Assert expertise** (LinkedIn) — same material, public format.

## Where to start

- **[home](wiki/home.md)** — landing note for browsing in **Obsidian** (usage modes, entry points, Dataview queries). On GitHub, this README is the entry point.
- **[themes-index](wiki/themes-index.md)** — the entry point: all notes arranged by **theme** (both corpora), with level, provenance and source link. ⚙️ generated.
- **[corpus-report](wiki/corpus-report.md)** — corpus health: coverage by theme, notes without a source, duplicates. ⚙️ generated.
- **[log](wiki/log.md)** — append-only journal of operations on the corpus (ingest / tool / struct / lint…), inspired by the *LLM Wiki* pattern.

## Structure

```
wiki/concepts/   169 flat notes — the knowledge base. Structure carried by the frontmatter.
wiki/tools/      93 tool notes — the AI-tool census.
sources/         raw materials the notes were built from:
                 ├ ibm-guide-agents-ia/, ibm-guide-prompt-engineering/  (md + html of the IBM hubs)
                 ├ lilian-weng/, hamel-husain/, …                       (md + README per external source)
                 └ SOURCES-PRIMAIRES.md, SOURCES-COMPLEMENTAIRES.md, METHODOLOGIE-IBM-THINK.md
tools/           build_index.py (generates the indexes) + the kb_*.py toolchain
```

## Anatomy of a note

Each note `wiki/concepts/<slug>.md` starts with a **frontmatter** that carries all the structure:

```yaml
---
title: ReAct
theme: reasoning-planning              # one of the 14 categories (see themes-index)
level: 🟢                             # 🔴 substance · 🟡 tradeoff · 🟢 overview
source_url: https://www.ibm.com/think/topics/react-agent
source_title: "What is a ReAct agent? — IBM Think"
primary_source: "Yao et al. (arXiv:2210.03629)"   # optional: original paper
---
```

Then the body: **In one sentence** (the hook for a post) · what the source says · **Example** (a concrete sourced case that makes the note self-contained) · tradeoff/insight · primary source · see also.

## Add or update a note

### Tooled process (recommended) — from a URL / article

The **[process/ENRICHMENT.md](process/ENRICHMENT.md)** process ingests a
source while guaranteeing **duplicate detection** (semantic embeddings) and
**quality** (structure, verified sources, human review). Driven by the
Claude Code slash-command `/kb:ingest <url>`. One-time prerequisites:

```bash
python3 -m venv tools/.venv && tools/.venv/bin/pip install -r tools/requirements.txt
tools/.venv/bin/python tools/kb_embed.py
```

Deterministic tools, reusable standalone:

```bash
tools/.venv/bin/python tools/kb_dedup.py "a concept's text"     # semantic duplicates
tools/.venv/bin/python tools/kb_lint.py --all                   # structural conformance
tools/.venv/bin/python tools/kb_check_sources.py wiki/concepts/x.md    # real URL + arXiv
tools/.venv/bin/python tools/kb_post.py                         # post preview (random note)
python3 tools/kb_staleness.py                                   # tool notes to re-verify (verified > 90 d ago)
```

### By hand

1. Create/edit `wiki/concepts/<slug>.md` with the frontmatter above (`source_url` is **mandatory**).
2. Regenerate the indexes:

```bash
python3 tools/build_index.py
```

The report flags any note without a `source_url`, thinly-covered themes and title duplicates.

## Commands (slash-commands)

The process is tooled by Claude Code slash-commands (`.claude/commands/kb/`, `kb` namespace):

| Command | Role |
|----------|------|
| `/kb:ingest <url>` | Ingest a source into concept note(s) — `process/ENRICHMENT.md` pipeline (dedup, gates, human review) |
| `/kb:tool <name/url>` | Add a tool to the census: verify at source → `wiki/tools/` note (frontmatter) → regenerate tables (`build_index.py`) → log |
| `/kb:analyze <url>` | Critical analysis of an article (writing nothing), linked to the corpus + proposals |
| `/kb:query <question>` | Answer from the wiki, with note citations |
| `/kb:lint` | Health checks (structure, sources, freshness, duplicates) + optional contradiction audit |
| `/kb:refresh [tool\|--stale\|--all]` | Re-verify tool(s) at source and propagate the update everywhere (note + tables + log); deprecate if needed. "Mixed" level (auto if mechanical, your OK if factual). Run on demand |
| `/kb:log [TYPE] <msg>` | Add an entry to the `wiki/log.md` journal (append-only) |

The corpus **schema** (structure, conventions, file map) is in [`process/SCHEMA.md`](process/SCHEMA.md) — layer 3 of the pattern, referenced by every command.

These commands map to the operations of the *[LLM Wiki](wiki/concepts/llm-wiki-karpathy.md)* pattern: **ingest** (`/kb:ingest`, `/kb:tool`), **query** (`/kb:query`), **lint/maintenance** (`/kb:lint`, `/kb:refresh`), + journal (`/kb:log`).

> ⚠️ `.claude/` is gitignored → these commands are **local** to your machine. To version them with the project, replace `.claude/` with `.claude/*` + `!.claude/commands/` in `.gitignore`.

## The 14 themes

Agent fundamentals · Reasoning & planning · Prompting · Tools & function-calling · RAG & context · Memory · Multi-agent · Interop protocols · Frameworks & tooling · Evaluation · Benchmarks · Security · Efficiency & cost · Governance, alignment & ops.
