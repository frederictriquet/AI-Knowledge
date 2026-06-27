---
title: "Tool retrieval (RAG over tools)"
type: "Concept"
theme: evaluation
level: 🟡
source_url: https://arxiv.org/abs/2305.15334
migrated_from: tool-retrieval
---

# Tool retrieval (RAG over tools)

**In one sentence** — when you have hundreds of tools, **dynamically retrieve** a relevant subset per query instead of exposing them all in the prompt.

## The idea
Putting hundreds of tool definitions in the context saturates the window, drives up cost and **degrades selection** (the model picks the wrong tool). Tool retrieval treats the tool catalog as a database to index: at each query, a retriever (embeddings over the API descriptions) **retrieves** the few most relevant tools, which alone are presented to the model. Gorilla applies this idea to a massive API call, coupling the LLM with a documentation retriever to reduce API hallucinations and track signature changes.

## Example
APIBench indexes 95 TorchHub, 696 TensorHub and 925 HuggingFace APIs. On "find an API that can classify pedestrians, cars... from an image", Gorilla returns `torch.hub.load('datvuthanh/hybridnets', 'hybridnets', pretrained=True)`; GPT-4 invents a nonexistent model, Claude picks the wrong library. In zero-shot, Gorilla beats GPT-4 by 20.43 points and reduces TorchHub hallucinations from 36.55 to 6.98 errors (~81%).

## Tradeoff / when to use it
Indispensable beyond a few dozen tools. Advantage: short prompt, more reliable selection, extensible catalog. Downside: a **retrieval stage** to maintain, and the risk that a relevant tool is excluded by a poor retrieval score.

## Primary source
Patil et al., 2023, *Gorilla: Large Language Model Connected with Massive APIs*, arXiv:2305.15334 *(arXiv verified — HTTP 200 + title)*.

## See also
- [tool-calling](tool-calling.md)
- [agentic-rag-subtypes](agentic-rag-subtypes.md)
