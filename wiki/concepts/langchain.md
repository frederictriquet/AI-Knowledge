---
title: "LangChain"
type: "Concept"
theme: frameworks-tooling
level: 🟢
source_url: https://www.ibm.com/think/topics/langchain
source_title: "What is LangChain?"
migrated_from: langchain
---

# LangChain

**In one sentence** — an open-source orchestration framework that provides modular abstractions (chains, indexes, memory, tools, agents) to build LLM-driven applications, pluggable onto almost any model.

## In detail
LangChain is an open-source orchestration framework (Python and JavaScript libraries) that simplifies building LLM-driven applications. Its core is **abstraction**: representing complex processes as named components, "chainable" to reduce the code required. The main building blocks: **chains** (LLMChain, SimpleSequentialChain) that link model and prompt; **indexes** (document loaders, vector stores, text splitters, retrieval/RAG); **memory** (full conversation, summary, last n exchanges); **tools** (Wolfram Alpha, Google Search, Wikipedia…); and **agents** that give the LLM the ability to decide, plan, and act step by step. Launched by **Harrison Chase in October 2022**, LangChain was, as of June 2023, the fastest-growing open-source project on GitHub. Note the **watsonx** integration (langchain_ibm package, WatsonxLLM and ChatWatsonx classes); LangGraph and LangSmith are the natural extensions.

## Example
The simplest chain fits in two lines: after registering a prompt as `ExamplePrompt`, you write `chain_example = LLMChain(llm=flan-t5, prompt=ExamplePrompt)` then `chain_example.run("input")` — the Flan-T5 model is called without plumbing. To chain, `SimpleSequentialChain` passes the output of one function as the input of the next, each able to change prompt, tool, or even model. On the prompt side, a `PromptTemplate` formalizes context and instructions ("do not use technical terms"), an output format, and few-shot examples, reusable once named.

## Tradeoff / insight (for a senior)
Pure vocabulary for anyone already coding LLM pipelines. Worth remembering: abstraction speeds up prototyping but "limits the degree of customization" — the classic framework vs low-level control tradeoff.

## Primary source
See the LangChain documentation and GitHub repository.

## See also
- [langgraph](langgraph.md)
- [crewai](crewai.md)
