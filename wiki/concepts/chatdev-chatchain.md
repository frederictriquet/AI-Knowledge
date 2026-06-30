---
title: "ChatDev: ChatChain, CAMEL, communicative dehallucination"
type: "Concept"
theme: security
level: 🔴
source_url: https://www.ibm.com/think/topics/chatdev
source_title: "What is ChatDev?"
---

# ChatDev: ChatChain, CAMEL, communicative dehallucination

**In one sentence** — a framework that simulates a waterfall software company (design/coding/testing) through a two-agent dialogue per phase, where the assistant deliberately reverses roles to demand clarifications before coding.

## In detail
ChatDev (OpenBMB) applies AI to the waterfall model and orchestrates its agents through **ChatChain**: the process is segmented into sequential phases (Demand Analysis, Language Choosing, Coding, CodeCompleteAll, CodeReview, Test, EnvironmentDoc, Manual). Each phase is a **two-agent dialogue** — an instructor who directs, an assistant who executes — continued over multiple turns until completion or consensus. To limit coding hallucinations, ChatDev introduces **communicative dehallucination**: the assistant "proactively seeks more information" (dependency names, GitHub repository) by adopting a deliberate "role reversal" — playing the instructor to ask for clarifications — before delivering its formal answer. ChatDev is built on the **CAMEL** framework, which manages roles, tasks and the agents' interactions with the models; the agents communicate via structured JSON messages acting as a shared memory buffer. The watsonx.ai tutorial illustrates the integration via Llama-4-Maverick and a CodeReview loop capped at 10 iterations.

## Example
ChatDev positions its LLMs as agents playing explicit social roles — CEO, CTO, software engineer, designer, tester — who prompt one another through "inception prompting". On dehallucination: faced with a vague instruction, rather than hallucinating, the assistant plays the instructor and demands the precise name of an external dependency or the exact GitHub repository to modify; it only refines its answer after the instructor has replied. An evaluation against GPT-Engineer (single-agent) and MetaGPT separates them on completeness, executability, consistency and quality: ChatDev clearly outperforms MetaGPT on quality thanks to communication mixing natural language and code.

## Tradeoff / insight
Non-trivial insight: "role reversal" formalises "ask questions before coding". Rather than letting the assistant hallucinate missing details, the protocol forces it to interrogate the instructor — anti-hallucination through interaction, where MetaGPT does it through schematisation.

## Primary source
The OpenBMB/ChatDev repository and the founding paper; communicative dehallucination and MacNet are described there without an explicit DOI in the text (see the ChatDev / MacNet paper for the exact reference).

## See also
- [metagpt-pattern](metagpt-pattern.md)
- [macnet](macnet.md)
