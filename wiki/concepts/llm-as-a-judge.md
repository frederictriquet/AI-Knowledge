---
title: "LLM-as-a-judge"
type: "Concept"
theme: evaluation
level: 🟡
source_url: https://www.ibm.com/think/topics/ai-agent-evaluation
source_title: "What is AI agent evaluation?"
objectives: [reliability]
---

# LLM-as-a-judge

**In one sentence** — using an LLM, guided by a rubric of criteria, to automatically score an agent's outputs when there is no ground truth to compare against.

## In detail
LLM-as-a-judge is "an automated evaluation system that assesses the performance of AI agents using predefined criteria and metrics. Instead of relying solely on human reviewers, an LLM as a judge applies algorithms, heuristics, or AI-based scoring models to evaluate the responses, decisions, or actions of an AI agent." It is mobilized when there are no predefined success criteria, and for the semantic evaluation of tool-calling. A concrete implementation: a travel agent scored on three criteria (accuracy, helpfulness, coherence) via a structured `evaluation_prompt` requesting a motivated `/5` score — `eval_input = evaluation_prompt.format(...)` then `agent.invoke(eval_input)`.

## Example
In IBM's eval pipeline, the LLM judge activates at step 4 ("Analyze the results") through an explicit fork: you compare against predefined success criteria *if there are any*; otherwise you switch to the LLM judge. It answers the four canonical questions — did the agent choose the right tool, call the right function, pass the right info in the right context, produce a factually correct answer? For text quality alone, less expensive alternatives exist: BLEU and ROUGE compare the output to a human reference text, where the LLM judge scores without reference data.

## Tradeoff / insight (for a senior)
To be calibrated: the literature documents biases (self-preference, sensitivity to position/order, to verbosity) that make the score non-neutral. Above all, the implementation presented is methodologically questionable: it reuses *the same* tool-equipped `agent` as judge (`agent.invoke(eval_input)`) instead of a separate evaluator — an agent that scores itself combines self-preference and context leakage. In production, separate the judge model from the evaluated model and fix a versioned rubric.

## Primary source
No formal academic reference — the "LLM-as-a-judge" pattern from the state of the art.

## See also
- [taxonomie-erreurs-appel-fonction](function-calling-error-taxonomy.md)
- [evaluation-trajectoire](trajectory-evaluation.md)
