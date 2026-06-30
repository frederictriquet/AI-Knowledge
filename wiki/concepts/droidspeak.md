---
title: "DroidSpeak"
type: "Concept"
theme: multi-agent
level: 🔴
source_url: https://www.ibm.com/think/topics/ai-agent-communication
source_title: "What is AI agent communication?"
---

# DroidSpeak

**In one sentence** — instead of having two LLMs converse in text, the KV cache is shared directly between them to speed up inter-agent communication, with an accuracy loss reported as minimal.

## In detail
DroidSpeak is a Microsoft solution that aims to let agents communicate faster with minimal accuracy loss. The principle fits the general observation that "when agents have the ability to communicate with each other, an agentic system becomes more than the sum of its parts", but latency remains a challenge (real-time communication slowed by the network and compute constraints).

## Example
The source situates the stakes on real-time systems where DroidSpeak makes the most sense: a self-driving car whose agents must instantly fuse camera, sensor and GPS data — "any delay in data exchange could lead to poor navigation decisions". Routing that inter-agent flow through natural-language round-trips adds a serialisation latency that is prohibitive at the fraction-of-a-second scale; sharing the KV cache directly removes this detour through text and the re-encoding on the receiving agent's side.

## Tradeoff / insight
The technical gem: DroidSpeak short-circuits natural-language serialisation by sharing the KV cache (the already-computed attention states) between distinct LLMs. It is a latency/accuracy trade: you gain communication speed against a degradation judged minimal. The mechanism assumes compatible models (close architectures) so that one LLM's cache is reusable by another. The source's exact title ("Cross-LLM Communication and Multi-LLM Serving") also points to a multi-LLM serving pooling concern, not just inter-agent communication.

## Primary source
*Droidspeak: KV Cache Sharing for Cross-LLM Communication and Multi-LLM Serving*, Liu *et al*, University of Chicago, Microsoft, 19 December 2024.

## See also
- [kqml-fipa-acl](kqml-fipa-acl.md)
