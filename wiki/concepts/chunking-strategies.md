---
title: "Chunking strategies"
type: "Concept"
theme: rag-context
level: 🟢
source_url: https://www.ibm.com/think/topics/agentic-chunking
source_title: "What is agentic chunking?"
---

# Chunking strategies

**In one sentence** — four families of chunking, from the most mechanical (fixed size) to the most costly (semantic, agentic), to be chosen according to the document's structure.

## In detail
Four main methods are catalogued. **Fixed-size chunking** splits the text into equal pieces by a predefined number of characters or tokens; to avoid fragmenting sentences, an overlap is often added that repeats the end of one chunk at the start of the next. Simple and lightweight, but rigid. **Recursive chunking** relies on a hierarchical list of natural separators (paragraphs, sentences, words, even class/function definitions in Python); it produces more coherent pieces and Markdown helps the chunker. The reference tool is LangChain's `RecursiveCharacterTextSplitter`. **Semantic chunking** creates per-sentence embeddings and groups similar sentences, opening a new segment when the semantics change; more compute-intensive. **Agentic chunking** combines these approaches under the steering of an agent.

## Example
On a Python file, the `RecursiveCharacterTextSplitter` exploits structural separators — class and function definitions — so as not to cut a function in two; in Markdown, it relies on `#` headings. Fixed-size chunking, by contrast, cuts blindly at 500 characters and risks splitting a sentence, hence the overlap that repeats the end of a chunk. Semantic chunking shows its inverse limit: on a paragraph covering two topics, a poorly calibrated threshold cuts too early or too late and degrades retrieval — so the pragmatic default remains recursive on structured text.

## Tradeoff / insight
Compute cost grows with semantic quality: fixed < recursive < semantic < agentic. Recursive chunking is the pragmatic default for structured text; semantic is justified on multi-topic documents where a bad cutting threshold degrades retrieval.

## Primary source
Semantic chunking is attributed to Greg Kamradt (GitHub discussion). The other strategies are not tied to an author.

## See also
- [Agentic chunking](agentic-chunking.md)
