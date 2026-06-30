---
title: "Function-calling error taxonomy"
type: "Concept"
theme: agent-fundamentals
level: 🔴
source_url: https://www.ibm.com/think/topics/ai-agent-evaluation
source_title: "What is AI agent evaluation?"
---

# Function-calling error taxonomy

**In one sentence** — a concrete grid for evaluating tool-calling: five errors detectable by deterministic rules, plus two semantic checks delegated to an LLM judge.

## In detail
Two families stand out. The **rule-based indicators** (operational efficiency of AI-driven systems): **Incorrect function name** (the function exists but the name/spelling is wrong, execution failure); **Missing required parameters** (one or more necessary parameters omitted); **Incorrect parameter value type** (string/number/boolean not matching what is expected); **Allowed values** (value outside the accepted or predefined set); **Hallucinated parameter** (parameter neither defined nor supported by the function specification). The **LLM-as-a-judge semantic indicators**: **parameter value grounding** ("ensure that each parameter value is directly derived from the user text, context history... or the API specification's default values") and **unit transformation** ("checks unit or format conversions, beyond basic types, between the values in the context and the parameter values in the tool call").

## Example
Concretely: calling `gett_weather` instead of `get_weather` triggers "incorrect function name" (execution failure); omitting `city` raises "missing required parameter"; passing `city=14` (a number) falls under "incorrect type"; `unit="kelvin"` when the enum only admits `celsius`/`fahrenheit` violates "allowed values"; adding `country="FR"` absent from the schema is a "hallucinated parameter". The LLM judge takes over on the semantic side: if the user wrote "it's 80°F", grounding checks that the value indeed comes from the text, and unit transformation checks that `80°F` was correctly converted to `26.7°C` before the tool call.

## Tradeoff / insight (for a senior)
The rules/LLM-judge split is the right design: the first five errors are validated without a model (function schema parsing, type validation, enum checking) — fast, deterministic, free. You only call on the costly and fallible LLM judge for what rules cannot settle: the semantics (does the passed value really come from the context? was the unit converted correctly?). Reusable as-is as a tool-calling evaluation checklist.

## Primary source
No external reference — original taxonomy.

## See also
- [llm-as-a-judge](llm-as-a-judge.md)
- [trajectory-evaluation](trajectory-evaluation.md)
