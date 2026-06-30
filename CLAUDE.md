# Project instructions — AI knowledge base

## MANDATORY: everything in this project is in English

This project is **English-only**, overriding any global "comments in French" rule.
Everything — file contents, prose, code **comments and docstrings**, **file and
directory names**, frontmatter **keys and values**, generated output — must be in
**English**. Commit messages too (already the convention).

The only exceptions are domain identifiers that are intentionally language-neutral
(theme/objective slugs, icons) and historical entries already written in `wiki/log.md`
(append-only — do not rewrite history).

## FORBIDDEN: recording history inside file contents

Comments, docstrings and file bodies (code **as well as** notes) document
**what the thing IS and DOES**, in the timeless present — never the story of how it was built.

**Banned** from a file's contents:
- narrating the problem a change just fixed
  ("the missing link", "what was missing until now", "henceforth", "now");
- justifying a past choice or before/after comparison
  ("unlike before", "no regression", "now we also index…", "new axis");
- any trace of the development journey.

Write as if the code/note had always been this way.

**Keeping a history of decisions or choices is the user's call**, not an
initiative. When wanted, it goes in a file **meant for it** — `wiki/log.md` (append-only
journal) or a dedicated ADR — **never** in code comments/docstrings or in notes.

## MANDATORY: honest notes that serve decision-making

The base exists to **make choices**. A note (tool **as well as** concept) must **help decide, not sell**. Tell the truth without embellishing, **even if the tool is popular**. For every note, by default:

- **state the limits, blind spots, and who / when the tool is NOT a fit**;
- **weight hype and self-reported figures** (stars, "production-ready", in-house benchmarks/tests, "used by X"): **attribute them to their source** and flag when they are **not independently verified**;
- **compare to alternatives** when a simpler, leaner or safer peer exists;
- **never repeat the vendor's pitch as-is**; verify facts at the source (license/price/cost/maturity), cf. the cost-verification rule (`process/SCHEMA.md` §4).

Cost (in tokens and money) is a **cross-cutting concern**: make it explicit, including the tool's own cost (not just what it saves).
