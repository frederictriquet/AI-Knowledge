# Knowledge base enrichment process

A **robust and reproducible** process for adding knowledge to the corpus from a
URL, an article, or a website — with **duplicate detection** and a **quality
guarantee**. Versioned (it lives with the project); the Claude Code slash command
`/kb:ingest` runs this process.

## Principle

A 7-step pipeline, guarded by checks. **No note is written before step 6**
(human validation). Everything is reversible until then.

```
URL / article / site
  ├─[1] INGEST ........ fetch + extract clean text
  ├─[2] EXTRACT ....... split into candidate concepts + map to themes
  ├─[3] DEDUP ......... embeddings top-K → overlap judgment
  │         └─ verdict per concept: NEW / MERGE / DUPLICATE
  ├─[4] DRAFT ......... write the note in the format (or prepare a merge patch)
  ├─[5] QUALITY GATE .. structure + sources + density
  ├─[6] REVIEW ........ report + explicit user approval
  └─[7] COMMIT ........ write the note + regenerate the indexes
```

Role splitting is **hybrid**: the deterministic steps (dedup, lint, source
verification, indexes) are Python scripts; the judgment steps (extraction,
writing, assessment of overlap and density) are carried by the LLM.

## Prerequisites (one time)

```bash
python3 -m venv tools/.venv
tools/.venv/bin/pip install -r tools/requirements.txt
tools/.venv/bin/python tools/kb_embed.py        # builds the embeddings index
```

All `kb_*.py` scripts run with `tools/.venv/bin/python` from the `tools/` folder
(sibling imports) or via the module path. The embeddings cache (`tools/.cache/`)
and the venv (`tools/.venv/`) are gitignored.

---

## Step 1 — INGEST

Fetch the **exact content** of the source — **never** via `WebFetch` (which only
returns a summary produced by a small model: omissions, hallucinated figures and
quotes). Download the raw page and read it **directly**:

```bash
curl -sL -A "Mozilla/5.0" "<url>" | pandoc -f html -t gfm-raw_html
```

If `curl`/`pandoc` fails (paywall, JS, 403), **report it explicitly** and do not
ingest blindly — never fall back on a small-model summary. Then extract the
**useful text** (no menus, ads, navigation).

- Keep the **raw markdown** of the source in `sources/<hub>/` (a new subfolder
  named after the author/site), as for existing sources.
- Note the **canonical URL** and the page **title**: they will become
  `source_url` and `source_title`.

## Step 2 — EXTRACT

A rich source often covers **several concepts**. Split into **atomic** candidate
concepts (one concept = one potential note). For each one:

- phrase the concept in 1-2 dense sentences (this text will be used for dedup);
- propose a **theme** from the 14 in the taxonomy (cf. `tools/kb_common.py`);
- propose a **level**: 🔴 substance · 🟡 tradeoff · 🟢 overview;
- spot any **primary source** (founding arXiv paper).

Discard anything out of scope right away (the corpus covers AI agents & prompt
engineering).

**The 4 gates (anti-noise)** — a candidate only deserves a note if it passes all four:
1. **Referenceable by name** — it is a nameable entity/notion (a pattern, a technique, a concept), not a generality.
2. **Not meta** — discard intros, "getting started", marketing overviews, perishable news.
3. **Citation test** — you can write "see the *X* note" with *X* = a concrete name.
4. **Reuse test** — ≥ 2 other notes (existing or upcoming) would reference it, or 1 needs it as a foundation.
> When in doubt, **do not create**: prefer a MERGE into an existing note (step 3).

## Step 3 — DEDUP

For **each** candidate concept, run semantic detection:

```bash
tools/.venv/bin/python tools/kb_dedup.py --json "dense text of the concept"
```

Output: `verdict` (pre-filter) + the `candidats` (top-K nearby notes, scores).
Thresholds (calibrated for the model, cf. the header of `kb_dedup.py`):

| Best candidate score | Pre-verdict | Action |
|---|---|---|
| ≥ 0.85 | DUPLICATE | Read the candidate note. Likely duplicate → discard or **merge**. |
| 0.75 – 0.85 | OVERLAP | **Read** the candidate notes. Decide: complement (merge) or a genuinely new angle (new note). |
| < 0.75 | NEW | Likely original. Still glance at the top-1. |

> **The score is only a pre-filter.** The final verdict is a **judgment**:
> open the candidate notes (`wiki/concepts/<slug>.md`) and assess the real overlap.
> Verdict per concept: `NEW` · `MERGE into <slug>` · `DUPLICATE (discarded)`.

## Step 4 — DRAFT

For each `NEW` concept, write a note that **strictly** respects the corpus format
(cf. any note, e.g. `wiki/concepts/react.md`):

```yaml
---
title: "Short human title"
theme: <one of the 14 themes>
level: 🔴 | 🟡 | 🟢
source_url: https://…                      # REQUIRED
source_title: "Title of the source page"   # recommended
primary_source: "Author, Title (arXiv:XXXX.XXXXX)"   # if a founding paper
---

# Title

**In one sentence** — the hook, self-contained (serves as a post).

## In detail
A dense explanation of what the source says. Senior tech audience.

## Example
ONE concrete, striking case drawn from the source (a played-out scenario, code,
payload, figures, quote) — makes the note self-contained. 4-6 lines, no paraphrase
of the substance and no repeat of a figure already cited above.

## Tradeoff / insight for a senior
The non-trivial point: when to use it, limits, pitfall.

## Primary source
The founding paper, if it exists.

## See also
- [Related note](existing-slug.md)
```

- File slug: `kebab-case` of the concept, unique. One concept = one file.
- High density, no filler. No images or code (unless quoted).
- "See also" links must point to **existing notes** (the candidates from step 3
  are excellent links).

For a `MERGE` concept, prepare a **patch** of the target note (adding a paragraph
or a nuance), not a new note.

**Refine, don't rewrite** (merge rule): a patch **adds** or **clarifies**.
Preserve all existing section headers, **do not delete** sourced content,
**merge** lists (e.g. "See also", tags) by union rather than replacing them. If
the new contribution contradicts the existing one, flag it explicitly in the step
6 report — do not silently overwrite.

## Step 5 — QUALITY GATE

Three checks, to pass on each draft before proposing it.

**a. Structure conformance** (deterministic):
```bash
tools/.venv/bin/python tools/kb_lint.py wiki/concepts/<new-slug>.md
```
Fix every ❌ error (frontmatter, theme outside the taxonomy, level, missing hook,
broken wikilink). The ⚠️ warnings are to be examined, non-blocking.

**b. Factual source verification** (deterministic, network):
```bash
tools/.venv/bin/python tools/kb_check_sources.py wiki/concepts/<new-slug>.md
```
`source_url` must respond (HTTP < 400). If an arXiv is cited, its real title must
be consistent with the note. **Never invent an arXiv identifier**: if it is not
verifiable, remove the `primary_source` field.

**c. Density & non-redundancy** (LLM judgment):
- does the note bring non-trivial information **absent** from the dedup candidates?
- is it not a paraphrase of an existing note?
- is the senior writing level held (no hollow generalities)?

## Step 6 — REVIEW (mandatory human validation)

Present the user with a **synthetic report**:

- concepts extracted from the source;
- for each one: dedup verdict (with scores and candidate notes), decision
  (new / merge / discarded);
- the full drafts;
- results of the three gates (lint ✅/❌, sources ✅/❌, density score).

**Wait for explicit approval.** Nothing is written or committed without agreement.

## Step 7 — COMMIT

After agreement:

1. Write the validated notes to `wiki/concepts/` (and apply the merge patches).
2. Regenerate the indexes and the embeddings index:
   ```bash
   python3 tools/build_index.py
   tools/.venv/bin/python tools/kb_embed.py     # incremental: only encodes the new
   ```
3. Commit **only if the user asks for it** (project convention). Message in
   English, conventional commits: `feat: add <concept> note`.

---

## Guarantees offered

- **Duplicates**: every concept is semantically compared to the entire corpus
  (embeddings) then judged note-by-note. Also detects reworded duplicates.
- **Quality**: structure validated mechanically, sources verified factually
  (URL + real arXiv), density judged, and the **last word goes to the human**.
- **Reproducibility**: the critical parts are deterministic scripts, versioned,
  recalibratable.

## Maintenance

- Changing the embeddings model → adjust `MODELE` in `kb_embed.py` then
  **recalibrate** the `kb_dedup.py` thresholds (re-run the nearest-neighbor
  distribution analysis) and `kb_embed.py --rebuild`.
- The current dedup thresholds are calibrated for
  `paraphrase-multilingual-MiniLM-L12-v2` (nearest-neighbor median ≈ 0.70).
