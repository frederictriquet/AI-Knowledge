---
title: "MRKL Systems"
type: "Concept"
theme: tools-function-calling
level: 🟡
source_url: https://arxiv.org/abs/2205.00445
primary_source: "arXiv:2205.00445"
migrated_from: mrkl
---

# MRKL Systems

**In one sentence** — a **routing** architecture where an LLM directs each request to a set of expert modules (symbolic: calculator, database, API; or neural).

## The idea
MRKL (*Modular Reasoning, Knowledge and Language*, pronounced "miracle") casts the LLM as a **router/controller** in front of specialized modules, instead of doing everything internally. The model decides *which module* to invoke and *with what arguments*, then integrates the answer. It is the direct conceptual ancestor of tool-using agents.

## How the routing is expressed
A point often misunderstood: in MRKL, **the router is neural, not hard-wired rules** — delegating the decision to a model (the `MR` = *Modular Reasoning*) is precisely what distinguishes the pattern from a symbolic `if/else`. The paper stays agnostic on the exact mechanism, which can be (1) **prompting**: describe each module (name + description) in the context, the LLM emits the choice — the dominant form today, which is what ReAct and [function calling](tool-calling.md) became; or (2) a **learned decision**: a classifier / fine-tuning that knows how to route (their example: detect arithmetic → calculator in Jurassic-X). Conversely, **deterministic rule-based routing** (scores, `if/else` in a skill) belongs to the [conditional logic / heuristic](conditional-heuristic-logic.md) pattern — the anti-MRKL. The *target modules* themselves can be symbolic (calculator, DB, API) — hence "neuro-symbolic" — but the **routing decision** stays neural.

## Example
The paper illustrates routing with a *calculator test* on Jurassic-X: the LLM only extracts the operands and the operation, the calculator does the math. Trained solely on **single-digit** operands (`5 + 3`), the system reaches **100% accuracy up to 9 digits** (Table 1), whereas GPT-3 — which synthesizes arithmetic from its weights — drops from 0.804 (3 digits) to 0.093 (5 digits). The authors justify the pattern by an LM's intrinsic limits: it does not know today's date, the dollar↔Moroccan dirham rate, or the price of AAPL.

## Tradeoff / when to use it
Mostly a **lineage reference**: ReAct, function calling and the "routing agents" of agentic RAG are descendants of it. Knowing MRKL helps you see that "routing to tools" is a pattern formalized back in 2022, not a novelty.

## Primary source
Karpas et al., 2022, *MRKL Systems: A modular, neuro-symbolic architecture…*, arXiv:2205.00445 (AI21 Labs). *(arXiv verified — HTTP 200 + title)*

## See also
- [Agentic RAG subtypes](agentic-rag-subtypes.md)
- [Tool calling](tool-calling.md)
