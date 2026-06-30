---
description: Critical analysis of an article (writing nothing), linked to the corpus.
argument-hint: <url>
---
Analyze the following article: $ARGUMENTS

> **Schema** (corpus map, tool families): `process/SCHEMA.md` §2 & §4.

Goal: an **analysis**, not a mere summary — and **nothing is written** by default.

1. Fetch the **exact content** of the page — **never** via `WebFetch` (which only returns a summary produced by a small model, a source of omissions and hallucinations). Download the raw page and read it **yourself**:
   ```bash
   curl -sL -A "Mozilla/5.0" "$ARGUMENTS" | pandoc -f html -t gfm-raw_html
   ```
   Read the full output: it is the author's real text, with their exact figures, names and quotes. If `curl`/`pandoc` fails (paywall, JS, 403), **flag it explicitly** and do not analyze blindly — never fall back on a small-model summary.
2. Render faithfully: central thesis, problem, **coined concepts/terms** (with their names), frameworks/taxonomies/steps, recommendations, cited tools, notable quotes.
3. **Critical evaluation**: what is solid vs to be qualified; the **blind spots** (in particular the **cost** in tokens, the project's cross-cutting concern).
4. **Link to the corpus**: which existing `wiki/concepts/` notes it overlaps with or complements, and which census tools/families it touches.
5. **Propose** (without executing it): the concept note(s) to create via `/kb:ingest`, and/or tools to add via `/kb:tool`. Wait for my go-ahead.
