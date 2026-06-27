---
title: "LLM Wiki: an LLM-maintained wiki instead of RAG"
type: "Concept"
theme: rag-context
level: 🟡
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
source_title: "LLM Wiki — Andrej Karpathy (gist)"
objectives: [production]
migrated_from: llm-wiki-karpathy
---

# LLM Wiki: an LLM-maintained wiki instead of RAG

**In one sentence** — rather than re-synthesizing from raw sources on every question (classic RAG), you have the LLM maintain a **persistent wiki** (interconnected markdown): a *compiled* knowledge layer whose value accumulates with each ingested source.

## What the source says
Karpathy proposes a pattern for building a personal knowledge base with an LLM. The idea: extract the knowledge from a source **once**, integrate it into pages, update the cross-references, note contradictions — instead of rebuilding everything on every query. **Three layers**: (1) immutable **raw sources** (articles, papers); (2) **the wiki** owned by the LLM (summary, concept, entity, synthesis pages); (3) **the schema** (`CLAUDE.md`) that dictates structure and workflows. **Three operations**: *ingest* (read → discuss the takeaways → write a summary → update 10-15 pages + cross-refs), *query* (search the pages → answer with citations → fold the exploration back in), *lint* (periodic health check: contradictions, stale claims, orphan pages, missing cross-references). Plus an `index.md` (catalog) and a `log.md` (append-only journal). The key insight: "the painful part of a knowledge base is not reading or thinking — it's the **bookkeeping**"; the LLM excels precisely at this maintenance that humans abandon (the curatorial work to the human, the administrative to the machine). Claimed lineage: Vannevar Bush's **Memex** (1945), whose maintenance problem the pattern finally solves.

## Why it matters
The pattern reframes RAG: no longer "retrieve then generate on the fly," but **compile and maintain** an intermediate layer that improves over time. It provides a vocabulary (3 layers, ingest/query/lint) and a checklist directly applicable to a corpus of markdown sheets — *exactly* the form of this knowledge base.

## Where the LLM part is (operator, not component)
The wiki is **passive**: inert markdown files. The LLM is not *stored* in it — it is its **operator** (a librarian, not a shelf). All the intelligent work is in the operations, especially **ingest**: deciding what to extract, writing in the house format, and — the most painful part — **finding and updating the existing pages** + the cross-references (the "bookkeeping"). Consequence: the LLM's effort is **shifted from read-time to write-time**. Where RAG makes the LLM work *on every question* (retrieve + synthesize on the fly), the wiki makes it work *once at ingest* (compile), and the query becomes a simple consultation of an already-curated layer. The split is **hybrid**: deterministic for what can be computed (dedup embeddings, structure lint, index), LLM for what must be judged (extraction, merge vs new, writing, meaning contradictions).

## Key points
- *Maintained* wiki (cumulative value) vs RAG *recomputed* on every query.
- 3 layers: immutable raw sources · wiki owned by the LLM · schema (`CLAUDE.md`).
- 3 operations: ingest · query · lint (+ `index.md`, `log.md`).
- The bottleneck of a KB = the **bookkeeping**; that is what the LLM automates.
- Stays **abstract by choice**: "instantiate your version with your agent."

## See also
- [Reports rather than RAG](reports-over-rag.md)
- [RAG vs fine-tuning vs prompt engineering](rag-vs-fine-tuning-vs-prompt-engineering.md)
- [Episodic / semantic / procedural memory](episodic-semantic-procedural-memory.md)
- [AgentOps](agentops.md)
