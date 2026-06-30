---
title: "Agentic chunking"
type: "Concept"
theme: rag-context
level: 🟡
source_url: https://www.ibm.com/think/topics/agentic-chunking
source_title: "What is agentic chunking?"
---

# Agentic chunking

**In one sentence** — an LLM splits the text by unit of meaning and tags each piece with metadata, instead of applying mechanical fixed-size cuts.

## In detail
Agentic chunking uses AI to dynamically segment long inputs into semantically coherent blocks fitted to the LLM's context window. It is a case of agentic automation: the agent decides on its own how to divide and tag the text. The typical workflow has four steps: preparing/cleaning the text, recursive splitting, the chunking step where the LLM combines and enriches each piece with a title and a summary as metadata, then embedding and storage in a vector database. The technique draws on earlier methods (overlapping sections, recursive splitting) and remains "at the exploratory stages." Cited benefits: efficient retrieval, accurate answers, flexibility across various document types, preservation of meaning. In practice, however, the implementation reduces the technique to a single prompt (`agentic_chunking`) asking Granite-3.0-8B-Instruct to divide the text into meaningful blocks, followed by a `split("\n\n")`.

## Example
On a technical PDF, the workflow runs: extraction then cleaning (removing page numbers, footers → raw text), recursive pre-splitting with overlap, then the LLM (Granite, GPT) recombines the small pieces into semantically complete blocks and enriches each with a title and a summary. A "Termination terms" chunk thus gets tagged with title="Early termination" + a short summary; for the query "how do I terminate?", the retriever matches on this metadata rather than on the body text alone, speeding up RAG retrieval compared to a mechanical fixed-size cut.

## Tradeoff / insight (for a senior)
Metadata enrichment (a title + summary per chunk) improves RAG search, but the LLM cost per document and the variability of the outputs (the separation remains a fragile `split`) weigh against a deterministic `RecursiveCharacterTextSplitter`. The distance between the concept and its trivial implementation signals a still-immature area.

## Primary source
Semantic chunking, which agentic chunking draws on, is attributed to Greg Kamradt (GitHub). Agentic chunking itself is not tied to any specific author.

## See also
- [Chunking strategies](chunking-strategies.md)
