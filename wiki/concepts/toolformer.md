---
title: "Toolformer"
type: "Concept"
theme: tools-function-calling
level: 🔴
source_url: https://arxiv.org/abs/2302.04761
migrated_from: toolformer
---

# Toolformer

**In one sentence** — an LLM *fine-tuned* to decide on its own when and how to call a tool, without few-shot examples or an orchestration prompt.

## The idea
Instead of learning tool use through prompting (ReAct, function calling), Toolformer learns it through **self-supervision**: the model is allowed to insert candidate API calls into a large corpus, these calls are executed, and **only the calls that reduce the perplexity** of the continuation are kept in the training data. The model thus internalizes when a tool (calculator, search, translation, calendar) actually helps.

## Example
In the text, a call is inserted inline: "The number in the next term is 18 + 12 x 3 = [Calculator(18 + 12 * 3)] 54." The tool set covers calculator, Q&A, two search engines, translation and calendar. Result: despite 26× fewer parameters, Toolformer (6.7B) outperforms GPT-3 175B — LAMA T-REx 53.5 vs 39.8, ASDiv 40.4 vs 14.0, SVAMP 29.4 vs 10.0.

## Tradeoff / when to use it
A **training** approach, not a prompting one — relevant if you *build/fine-tune* a model, not if you consume an API. Advantage: native tool decision, without an orchestration prompt. Drawback: costly (data generation + fine-tuning), frozen to the tool set seen at training. In practice, the native function calling of recent APIs has made this route less necessary for most application use cases.

## Primary source
Schick et al., 2023, *Toolformer: Language Models Can Teach Themselves to Use Tools*, arXiv:2302.04761 (Meta AI). *(arXiv verified — HTTP 200 + title)*

## See also
- [tool-calling](tool-calling.md)
- [react](react.md)
