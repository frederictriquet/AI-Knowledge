---
title: "Augmented language models (Weng's taxonomy)"
type: "Concept"
theme: agent-fundamentals
level: 🔴
source_url: https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/
source_title: "Prompt Engineering"
---

# Augmented language models (Weng's taxonomy)

**In one sentence** — the sourced genealogy of tool-using agents: before packaged "function calling," three families of techniques (retrieval, code execution, API calls) were already augmenting a frozen LLM through the prompt alone.

## What the source says
Weng draws on the *Augmented Language Models* survey by Mialon et al. (2023) to structure three categories. **Retrieval**: for knowledge after the cutoff or private knowledge, you retrieve then inject into the prompt (RAG-style); Lazaridou et al. (2022) use Google Search with TF-IDF ranking of paragraphs, and Liu et al. (2022) show that an "internal retrieval" — generating the knowledge before answering — also helps. **Programming language**: PAL (Gao et al. 2022) and PoT (Chen et al. 2022) have the LLM generate code executed by a Python interpreter, decoupling computation from reasoning. **External APIs**: TALM (Parisi et al. 2022) generates `|tool-call`/`tool input` calls and loops through self-play; Toolformer (Schick et al. 2023) learns in a self-supervised way, from a few demonstrations, to call a calculator, Q&A, search engine, translation and calendar, filtering calls by whether they reduce the loss of predicting future tokens.

## Example
Toolformer's toolkit fits in five APIs: calculator, Q&A system, search engine, translator, calendar. The annotation encodes a call as `<API>name(input)→result</API>`. The self-supervised filter is mechanistic: you run the call, compute the cross-entropy over the following tokens with and without the result, and keep the call only if `L⁻ − L⁺` exceeds a threshold — i.e. only if it reduces the prediction loss. At inference, decoding stops at the "→" token, the signal that the model expects an API response.

## Why it matters
Weng exposes the research lineage of tool calling (TALM → Toolformer) and the underlying self-supervised learning mechanism, beyond the functional description alone.

## Primary sources
- Mialon et al., *Augmented Language Models: a Survey* (2023)
- Gao et al., *PAL: Program-aided language models* (2022)
- Chen et al., *Program of Thoughts Prompting* (2022)
- Parisi et al., *TALM: Tool Augmented Language Models* (2022)
- Schick et al., *Toolformer* (2023)

## See also
- [Tool calling](tool-calling.md) · [CodeAct, including PAL](codeact.md)
- [Prompt chaining](prompt-chaining.md)
- [full post](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)
