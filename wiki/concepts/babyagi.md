---
title: "BabyAGI"
type: "Concept"
theme: agent-fundamentals
level: 🟢
source_url: https://www.ibm.com/think/topics/babyagi
source_title: "What is BabyAGI?"
---

# BabyAGI

**In one sentence** — the minimal 2023 loop (Yohei Nakajima) of three agents — execution, creation, prioritization — backed by a vector memory; an "educational sandbox" more than a production tool.

## In detail
BabyAGI is an autonomous-agent framework shared by Yohei Nakajima in 2023, which generates and executes a sequence of tasks according to a user goal. It orchestrates a loop of creation, execution and prioritization using an LLM (typically GPT-4) and a vector memory store. The standard implementation is a Python script using the GPT models via API, a vector database (typically Pinecone; FAISS and Chroma in variants) and LangChain to structure the roles. The three-step loop: the execution agent runs a task with the context from the store; the creation agent generates follow-up tasks from the result; the prioritization agent reorders the queue by dependencies and relevance, until exhaustion or a stop condition. BabyAGI is described as an educational sandbox rather than a production application, and is not an AGI. In 2024, Nakajima launched BabyAGI 2, an experimental variant using a *functionz* framework to store functions and metadata in a database.

## Example
The canonical setup: you clone the repo, `pip install` the dependencies, copy the example `.env` and paste in an OpenAI API key and a Pinecone key. You then set the `OBJECTIVE` variable (e.g. "write a market study plan for EVs") plus an initial task, then `python babyagi.py`. The loop starts: the execution agent handles the task with the vector context, the creation agent generates the follow-ups, the prioritization agent reorders the queue by dependencies — iterating until the queue is empty or a stop condition is met. The whole config fits in a single `.env` file.

## Tradeoff / insight (for a senior)
Often compared to AutoGPT: BabyAGI runs a compact loop (creation/execution/prioritization + vector memory), whereas AutoGPT offers a richer framework for tool integration and scales better. BabyAGI remains a research tool: its pedagogical readability is its real value.

## Primary source
Attributed to Yohei Nakajima (2023). See the BabyAGI GitHub repository.

## See also
- [autogpt](autogpt.md)
- [taxonomie-5-types-agents](five-agent-types-taxonomy.md)
