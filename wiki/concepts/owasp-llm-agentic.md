---
title: "OWASP Top 10 LLM & agentic threats"
type: "Concept"
theme: security
level: 🟡
source_url: https://genai.owasp.org/llm-top-10/
---

# OWASP Top 10 LLM & agentic threats

**In one sentence** — the de facto standard security reference: a shared taxonomy of LLM risks, extended by a section specific to agentic threats.

## The idea
The OWASP Top 10 for LLM Applications provides a common nomenclature of risks: **prompt injection**, sensitive information disclosure, training data poisoning, insecure output handling, excessive consumption, supply chain vulnerabilities, etc. The *Agentic AI – Threats and Mitigations* document extends this grid to the properties specific to agents: poisoned persistent memory, tool abuse, agent cascades, excessive autonomy and lack of traceability. It is a review language, not an implementation.

## Example
The Agentic Security Initiative explicitly names eight threat categories specific to agents: **Memory Poisoning**, **Tool Misuse**, **Privilege Compromise**, **Cascading Hallucinations**, **Intent Breaking**, **Goal Manipulation**, **Rogue Agents** and **Human Manipulation**. To make Goal Manipulation tangible, OWASP provides a **"FinBot" Capture The Flag**: a financial agent whose objective is hijacked mid-execution, showing that an autonomous agent can be redirected to an unintended action without compromising its code or its model.

## Tradeoff / when to use it
Use it as a threat-modeling checklist and to align the vocabulary between security and AI teams; it places each guardrail against a named threat. Limit: it is a generic awareness framework, not prescriptive on the precise technical countermeasures, which must be designed case by case.

## Primary source
OWASP, *Top 10 for LLM Applications* (2023/2025) and *OWASP Agentic AI – Threats and Mitigations* (2025) — references published by OWASP.

## See also
- [Spotlighting](spotlighting.md)
- [Ethics & governance](ethics-governance.md)
