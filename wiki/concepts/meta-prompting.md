---
title: "Meta-prompting"
type: "Concept"
theme: prompting
level: 🟡
source_url: https://www.ibm.com/think/topics/meta-prompting
source_title: "What is meta-prompting?"
---

# Meta-prompting

**In one sentence** — give the LLM a reusable reasoning template for a class of tasks (structure and steps), rather than a throwaway prompt for a single case.

## In detail
Meta-prompting is an advanced technique that gives the LLM a reusable step-by-step template for solving a whole category of tasks, focusing on structure, syntax and reasoning schema rather than the instance. The technique is grounded in category and type theory: a category of tasks T, a category of structured prompts P, and a meta-prompting functor M that translates each task into its prompt while preserving the logical structure. Three types are distinguished: user-supplied (a hand-written template), recursive (RMP, the LLM generates its own meta-prompt in two passes) and conductor (a model orchestrates multiple multi-agent specialists). Meta-prompting is set against zero-shot, few-shot (tied to examples) and CoT (which elicits reasoning without structuring it by type). Benchmarks are reported (MATH 46.3% with Qwen-72B vs 42.5% for GPT-4; Python puzzles 32.7 → 45.8%; sonnets 62 → 79.6%), with no verifiable reference attached.

## Example
For "solve any system of two linear equations", the functor generates a prompt-template applied to `2x + 3y = 12` and `x - y = 4`: "As a math teacher, explain step by step… 1: identify coefficients a1,b1,c1 and a2,b2,c2; 2: choose substitution or elimination; 3-4: line up and subtract to eliminate a variable; 5-6: solve then back-substitute; 7: check in both equations; 8: state the result (x, y)." Changing the numbers does not change the structure: the reasoning skeleton is reused as-is.

## Tradeoff / insight
The category/functor formalism is dressing: the operational idea is to capture a reasoning skeleton per problem type. Gain: consistency and reusability at scale; cost: you must invest expertise to write the template (supplied variant) or accept that quality depends on the self-generated prompt (RMP). The conductor mode multiplies calls and compute.

## Primary source
Suzgun & Kalai 2024, "Meta-Prompting".

## See also
- [Techniques catalogue](techniques-catalog.md)
- [Prompt optimization](prompt-optimization.md)
