# Roadmap

Steering document (not published to the site).
Statuses: 🔜 ready to start · 🧊 deferred (trigger on real need).

## Corpus goals

1. **Knowledge base for colleagues** — onboarding newcomers, deepening, discovering topics. Expected access along **several axes**: by **subject**, by knowledge **level**, by **content type** (note, link, video…). Shareable as **"tip of the day" / "knowledge nugget"** (consumable without reading a full note).
2. **Training paths** — paths differentiated by need/level (**SCORM**), **assessment** (quizzes, MCQs). Requires knowledge **structured for training** and **expert-validated**.

## Work items (aligned with the goals)

- 🔜 **Content-type axis** — today: concept notes + tool notes only. Add **link** / **video** (content type + dedicated access).
- 🔜 **By-level access** — a generated "by level" page/view (🔴/🟡/🟢), beyond the Dataview queries in `home`.
- 🔜 **Nuggets / tip-of-the-day** — tool the sharing (rotation, export) beyond `kb_post.py` (random preview).
- 🔜 **Expert validation** — validation metadata (who / when / status) on notes; a prerequisite for training paths.
- 🔜 **New objectives (subject pages)** — mechanism in place: add to `OBJECTIVES`, tag notes **and** tools, create the subject file. Candidates: `security`, `advanced-prompting`, and filling in `non-coder-practices`.
- 🧊 **Training paths / SCORM** — sequencing, prerequisites, SCORM export (large effort, depends on expert validation).
- 🧊 **Quizzes / MCQs** — generate and assess knowledge by subject.
- 🧊 **Shared `tools/kb_fetch.py`** — factor out `curl | pandoc` **if** JS/SPA pages or 403s show up. Inline for now.
- 🧊 **`/kb:query` — broaden/narrow** — suggest "broader / narrower" in the answers.
