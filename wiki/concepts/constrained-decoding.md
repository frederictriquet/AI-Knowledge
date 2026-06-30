---
title: "Constrained decoding / structured output"
type: "Concept"
theme: efficiency-cost
level: 🟡
source_url: https://arxiv.org/abs/2307.09702
objectives: [cost-control]
---

# Constrained decoding / structured output

**In one sentence** — force the output to respect a grammar/schema (JSON, regex) by masking invalid tokens at decoding time; guarantees a parsable format (≠ "politely asking" for JSON).

## The idea
Rather than hoping for valid JSON via the prompt, constrained decoding acts *during* generation: at each step, an automaton derived from a grammar or schema computes the set of allowed tokens and **masks** (logit bias to −∞) all the others. The model literally cannot produce malformed output. Outlines compiles the grammar/regex into a finite automaton walked token by token, with no notable inference overhead.

## Example
The paper illustrates with the float regex `([0-9]*)?\.?[0-9]*` over a toy vocabulary `{"A", ".", "42", ".2", "1"}`: in the initial state the automaton masks `"A"` (not accepted); then, after sampling `".2"`, only `"42"` and `"1"` remain as valid completions. The key to the "little overhead": a pre-computed index outside inference (a hash-map from FSM state → valid tokens) brings masking down to O(1) per token instead of the naive O(N) that scans the whole vocabulary. On the Outlines API side, `generate.regex(model, r"\s*([Yy]es|[Nn]o|[Nn]ever|[Aa]lways)")` forces GPT2-medium to answer with one of these four words to "Is 1+1=2?".

## Tradeoff / when to use it
Indispensable whenever a machine-parsable output is required: tool calls, structured extraction, pipelines. It guarantees the *form*, not the *correctness* of the content. Constraining too hard can degrade reasoning (the model can no longer "think out loud" before structuring). Requires an inference engine that exposes the logits.

## Primary source
Willard & Louf, 2023, *Efficient Guided Generation for Large Language Models* (Outlines), arXiv:2307.09702 *(arXiv verified — HTTP 200 + title)*; Microsoft guidance; the JSON mode of various APIs (OpenAI, etc.).

## See also
- [tool-calling](tool-calling.md)
