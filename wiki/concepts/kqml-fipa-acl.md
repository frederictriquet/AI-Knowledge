---
title: "KQML & FIPA-ACL"
type: "Concept"
theme: interop-protocols
level: 🟡
source_url: https://www.ibm.com/think/topics/ai-agent-communication
source_title: "What is AI agent communication?"
---

# KQML & FIPA-ACL

**In one sentence** — the two historical agent communication languages (ACLs) that standardized "communicative acts" (inform, request, query) long before LLMs, and that most current frameworks ignore in favor of natural language.

## In detail
KQML (Knowledge Query and Manipulation Language) and FIPA-ACL (Foundation for Intelligent Physical Agents – Agent Communication Language) are the two preferred protocols for communicating with agents. DARPA developed KQML in the 1990s, "laying the groundwork for communication between agents well before intelligent AI agents were developed." The FIPA developers continued this work "shortly after, bringing improvements in standardization and semantic clarity." These ACLs define standard "communicative acts" (for example, inform, request, query) to enable structured dialogue in dynamic environments. Of note, ChatDev "does not use a formal agent communication protocol": ChatChain ensures interoperability "through the natural capabilities of the LLM," via LLM-optimized conventions rather than formal ACLs.

## Example
The source illustrates the absence of a standardized protocol with smart cities: traffic management systems and autonomous vehicles use different communication protocols, which "prevents seamless coordination and data sharing." This is precisely the role that a formal ACL (KQML/FIPA-ACL) solves through its shared message syntax and semantics. Conversely, in natural language, a vague request like "I want to change my order" in a support chatbot can be misinterpreted and trigger a cancellation instead — the ambiguity that typed communicative acts (inform, request) sought to eliminate.

## Tradeoff / insight (for a senior)
The tradeoff is clear: the formal structure and semantic clarity of the historical ACLs versus the flexibility of LLM-optimized natural language. Modern LLM frameworks (ChatDev/ChatChain) abandon formal ACLs — gaining flexibility, losing format and semantic guarantees. Worth knowing to situate the "standardized protocols" debate, one of the open challenges of multi-agent interoperability.

## Primary source
*The Current context of Agent Communication Languages*, Labrou *et al*, University of Maryland, March 1999.

## See also
- [droidspeak](droidspeak.md)
