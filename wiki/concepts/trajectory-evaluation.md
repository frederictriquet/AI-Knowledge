---
title: "Trajectory evaluation"
type: "Concept"
theme: evaluation
level: 🔴
source_url: https://www.ibm.com/think/topics/ai-agent-evaluation
source_title: "What is AI agent evaluation?"
objectives: [reliability]
---

# Trajectory evaluation

**In one sentence** — evaluate the sequence of decisions, tool calls and intermediate steps the agent took, not just the quality of its final answer.

## In detail
Generative agents "generally perform broader, more complex operations, such as multi-step reasoning, tool calling and interacting with external systems". Consequence: "even when the final output is text, it may be the result of intermediate actions such as querying a database or calling an API, each of which must be evaluated separately". In some cases, "the agent produces no text output at all" — success is measured by the correct execution of the task. Evaluation must "go beyond surface-level text quality". One should "plan every potential step of the workflow" and account for "the agent's overall approach throughout the workflow, that is, the path it follows to solve a multi-step problem". The key questions: did it pick the right tool, call the right function, pass the right information in the right context, produce a factually correct answer?

## Example
The five-step eval process makes the trajectory concrete. Step 2: you plan *every* potential step of the workflow — API call, passing info to a second agent, decision-making — to score each in isolation. Step 3: you run the agent in several environments, ideally with different LLMs, and monitor, for instance, its use of RAG to retrieve external data, or its response to an API call. This captures not just the "what" but the "why" of the decisions, the starting point for debugging at step 5 (rewriting prompts, adjusting architecture).

## Tradeoff / insight
The principle: break the workflow into individual steps and score the path, not just the result. Tradeoff: it is more costly to instrument than a final-output eval, but it is the only way to diagnose *why* an agent fails (wrong tool, wrong context) and to locate the point of failure in a non-deterministic chain.

## Primary source
No formal academic reference — concept close to the "trajectory evaluations" in the state of the art.

## See also
- [taxonomie-erreurs-appel-fonction](function-calling-error-taxonomy.md)
- [llm-as-a-judge](llm-as-a-judge.md)
- [agentops](agentops.md)
