---
title: "Case-based reasoning"
type: "Concept"
theme: reasoning-planning
level: 🟡
source_url: https://www.ibm.com/think/topics/ai-agent-memory
source_title: "What is AI agent memory?"
---

# Case-based reasoning

**In one sentence** — deciding by reusing similar past cases rather than reasoning from scratch.

## In detail
Case-based reasoning draws directly on episodic memory: "This type of memory is useful for case-based reasoning, where an AI learns from past events in order to make better decisions in the future." The episodic memory that feeds it is implemented by recording key events, actions and their outcomes in a structured format the agent can access when making decisions. The canonical example is an AI-powered financial advisor that remembers a user's past investment choices to provide better recommendations. The mechanism also applies to robotics and autonomous systems, where the agent must remember past actions to navigate effectively.

## Example
The source contrasts two thermostats to make the mechanism tangible: a basic thermostat "doesn't need to remember yesterday's temperature" (a reflex agent without memory), whereas a smart thermostat stores and analyses past data to identify trends, adapt to user behaviour and optimise energy efficiency — exactly case-based reasoning. On the implementation side, the source ties the underlying episodic memory to the RAG family: retrieving the relevant cases from a knowledge base to enrich the decision, while keeping low-latency processing.

## Tradeoff / insight
Reusing a past case is cheaper and more explainable than full generative reasoning, but quality depends entirely on the similarity measure and the representativeness of the stored cases: a biased case corpus reproduces its biases, and an "almost similar" case can drive a wrong decision with false confidence. Frame it as retrieval over episodic memory, not as generalisation.

## Primary source
Not tied to a named source; presented as an application of the episodic memory described in CoALA (Princeton, 2024). Case-based reasoning as a discipline predates it.

## See also
- [Episodic / semantic / procedural memory](episodic-semantic-procedural-memory.md)
