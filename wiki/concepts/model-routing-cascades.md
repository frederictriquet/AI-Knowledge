---
title: "Model routing & cascades"
type: "Concept"
theme: efficiency-cost
level: 🟡
source_url: https://arxiv.org/abs/2305.05176
primary_source: "arXiv:2305.05176"
objectives: [cost-control]
migrated_from: model-routing-cascades
---

# Model routing & cascades

**In one sentence** — route each request to the cheapest model CAPABLE of handling it, or chain from small to large (cascade) with a confidence judge; sharply reduces cost at near-constant quality.

## The idea
Not every call needs the biggest model. Two strategies. **Routing** classifies the request upfront and sends it to the right model (small for the trivial, large for the hard). The **cascade** first tries a cheap model, then evaluates the response via a confidence score or a judge; if confidence is insufficient, it *escalates* to the larger model. You only pay for the big model on the fraction of requests that warrant it.

## Example
FrugalGPT demonstrates the cascade by chaining heterogeneous APIs from cheapest to most expensive — e.g. J1-Jumbo, then ChatGPT, then GPT-4 — with a *scorer* deciding at each tier whether the response is reliable enough to stop there. The paper reports **up to 98% cost reduction** while matching GPT-4's performance, or even **+4% accuracy** at equivalent cost. The lever: only the fraction of genuinely hard requests escalates to the big model.

## Tradeoff / when to use it
Ideal on high-volume traffic with heterogeneous difficulty: massive savings at near-constant quality. The cost shifts to the **router/judge** (itself fallible) and the latency of cascade escalations adds up. The confidence threshold is a cost/quality dial to calibrate.

## Primary source
Chen et al., 2023, *FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance*, arXiv:2305.05176 *(arXiv verified — HTTP 200 + title)*; RouteLLM (LMSYS, 2024).

## See also
- [LLM-as-a-judge](llm-as-a-judge.md)
- [Semantic caching](semantic-caching.md)
