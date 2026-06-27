---
title: "Self-RAG"
type: "Concept"
theme: rag-context
level: 🔴
source_url: https://arxiv.org/abs/2310.11511
migrated_from: self-rag
---

# Self-RAG

**In one sentence** — an LLM trained to decide *when* to retrieve and to *self-critique* the relevance and factual support of what it retrieves and generates, via "reflection tokens."

## The idea
Classic RAG retrieves systematically and trusts the passages. Self-RAG trains the model to emit special **reflection tokens** that: (1) decide whether a retrieval is needed for the current segment, (2) rate each passage's relevance, (3) check whether the generation is actually *supported* by the passage, (4) assess overall usefulness. Retrieval becomes **conditional and self-evaluated**.

## Example
Four concrete reflection tokens (Table 1): `Retrieve` ∈ {yes, no, continue}, `IsRel` ∈ {relevant, irrelevant}, `IsSup` ∈ {fully, partially, no support}, `IsUse` ∈ {1..5}. The model first emits `Retrieve=yes`, rates each passage with `IsRel`, verifies that its sentence is `fully supported`, then gives itself an `IsUse=5`. Results (Table 2): on PopQA, Self-RAG 7B reaches **54.9%** versus **29.3%** for ChatGPT; on PubHealth, 74.5% (13B) vs 70.1%. It stays below ChatGPT on ARC-Challenge (73.1 vs 75.3).

## Tradeoff / when to use it
Reduces hallucinations and over-retrieval. Requires a model trained/fine-tuned to emit these tokens (≠ a simple prompt). Same objective as Corrective RAG (cRAG), but achieved through **learning** rather than an external grader: Self-RAG = quality in the weights, cRAG = quality in the pipeline.

## Primary source
Asai et al., 2023, *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection*, arXiv:2310.11511. *(arXiv verified — HTTP 200 + title)*

## See also
- [corrective-rag](corrective-rag.md)
- [rag-agentique](rag-agentique.md)
