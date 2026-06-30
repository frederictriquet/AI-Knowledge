---
title: "Learning agent (AIMA model)"
type: "Concept"
theme: agent-fundamentals
level: 🟢
source_url: https://www.ibm.com/think/topics/ai-agent-learning
source_title: "What is a learning AI agent?"
---

# Learning agent (AIMA model)

**In one sentence** — an agent that decomposes into four internal roles so it can loop over its own mistakes and improve over time.

## In detail
A learning agent improves its performance over time by adapting to new experiences and data, where other agents rely on predefined rules or models. It decomposes into four main elements: the **performance element** (makes decisions from a knowledge base), the **learning element** (adjusts and improves the knowledge based on feedback and experience), the **critic** (evaluates actions and provides feedback in the form of rewards or penalties), and the **problem generator** (suggests exploratory actions to discover new strategies). Reinforcement learning is its canonical illustration: the agent explores, receives rewards and penalties, and refines its policy. It relies on machine learning (supervised, unsupervised, reinforcement, continual).

## Example
The source walks through a multi-agent case in a hospital network: an advanced learning agent equipped with generative AI supervises simpler agents (reflex or goal-based), each carrying a role or task within the healthcare system, to improve patient outcomes and operational efficiency. The useful nuance: feedback (the critic's role) is not the whole of learning. The source distinguishes its regime by technique — rewards/penalties in RL, comparison to ground truth via a loss function in supervised learning, self-generated pseudo-labels in self-supervised learning.

## Tradeoff / insight (for a senior)
Pure vocabulary, but useful: the quartet performance / learning / critic / problem generator is exactly the breakdown of an RL loop (policy, update, reward function, exploration). The "problem generator" formalizes the exploration/exploitation tradeoff that other agent types ignore — it is what distinguishes an agent that improves from a frozen one.

## Primary source
The four-component model comes from Russell & Norvig, *AIMA* (chap. 2, learning agent).

## See also
- [Taxonomy of the 5 agent types](five-agent-types-taxonomy.md)
- [Reactive / deliberative / cognitive architectures](reactive-deliberative-cognitive-architectures.md)
