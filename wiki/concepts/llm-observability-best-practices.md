---
title: "LLM observability: best practices (tool-agnostic)"
type: "Concept"
theme: governance-alignment-ops
level: 🔴
source_url: https://opentelemetry.io/docs/specs/semconv/gen-ai/
source_title: "OpenTelemetry — GenAI semantic conventions"
objectives: [reliability, production]
migrated_from: observabilite-llm-best-practices
---

# LLM observability: best practices (tool-agnostic)

**In one sentence** — instrumenting an LLM app is not wiring up a dashboard: it is deciding *what* to trace (a span per chain step), *how* to evaluate quality without going broke or fooling yourself (a calibrated, sampled judge), and *what not to ingest* (PII) — the tool is merely the receptacle.

## In detail
The three underlying questions, often glossed over behind "just turn on the feature":

**1. What to trace — span granularity.** One user request = one *trace*; each LLM call, retrieval, function-call, parse = a *span*. The de facto standard is **OpenTelemetry GenAI semantic conventions**: normalized attributes (`gen_ai.request.model`, `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, `gen_ai.request.temperature`…). Tracing at the span level lets you attribute latency and cost *to the responsible step* — the only way to arbitrate multi-model routing (cf. [agentops](agentops.md)). Best practice: instrument via OTel, not a proprietary SDK → no vendor lock-in, the app stays portable across observability backends.

**2. The 4 signals to correlate.** (a) *Operational*: latency p50/p95/p99 per step, error rate, time-to-first-token; (b) *Cost*: tokens in/out per request, cost/request, and above all cost *per business feature* (not an unusable global aggregate); (c) *Quality*: "failure to answer" rate, toxicity, sentiment, relevance — see the pitfall below; (d) *Security*: prompt injection attempts, PII leakage on input *and* output. Value comes from the **correlation**: a p95 latency spike correlated with a cluster of prompts on the same topic > three isolated dashboards.

**3. Define SLOs before dashboards.** "98% success rate" means nothing without a definition of success. Best practice: write the objectives (p95 < X ms, cost/request < Y, hallucination rate < Z% on a golden set) *before* instrumenting, and alert on the **drift** of those SLOs, not on frozen absolute thresholds.

**4. Close the observability → eval → fix loop.** Production traces are the fuel for golden sets: requests that fail in prod become test cases. This is the link with [eval-driven-development](eval-driven-development.md) — observability without a re-injection loop is decoration.

## Tradeoff / insight
The four pitfalls rarely spelled out — and that decide the real ROI:

- **The LLM judge is neither free nor reliable.** Evaluating quality "out-of-the-box" via LLM-as-judge *doubles* inference cost (one eval call per business call) and inherits the judge's biases: position bias, verbosity bias, self-preference, poor calibration. Best practice: **sample** the eval (1–10%, not 100%), calibrate the judge against human labels before trusting it, and prefer a judge model different from the evaluated model. Cf. [llm-as-judge-correct](llm-as-judge-correct.md) and [llm-evaluators](llm-evaluators.md).
- **False positives from automatic checks.** "Toxicity", "negative sentiment", "failure to answer" are fallible classifiers: a *legitimate* negative sentiment (the user describing a problem) is not a failure. Without a calibrated threshold, you drown the real signals in noise and the team ends up ignoring the alerting.
- **Sampling = an observability/cost tradeoff.** Tracing 100% of requests with full payloads blows up ingestion *and* storage cost (prompts/responses are bulky). Best practice: head-sampling on nominal traffic, tail-sampling 100% on errored or slow traces — keep what informs.
- **Privacy: observability is an exfiltration surface.** Ingesting prompts and responses duplicates potentially sensitive data (PII, secrets, customer data) into a third-party system, often outside the EU. Best practice: **scrub PII at the source, before export** (not "by default in the tool", which means it has already transited), set a short retention, and treat the observability backend as an asset subject to the same GDPR/DLP as prod. Security link: [prompt-injection](prompt-injection.md), [prevent-prompt-injection](prevent-prompt-injection.md).

Insight: the differentiator between two LLM observability platforms is neither the number of dashboards nor semantic clustering — it is the **quality of the eval layer** (judge calibration, false positives) and the **command of the cost/privacy tradeoff of ingestion**. That is where the real ROI is decided, and what product demos show least.

## Primary source
- **OpenTelemetry GenAI semantic conventions** (opentelemetry.io/docs/specs/semconv/gen-ai/) — instrumentation standard.
- **OWASP Top 10 for LLM Applications** (owasp.org) — for the security pillar (LLM01 Prompt Injection, LLM06 Sensitive Information Disclosure).

## See also
- [AgentOps](agentops.md) — the ops/DevOps framing of agents (OTel session/trace/span).
- [Eval-driven development](eval-driven-development.md) — the loop that closes observability.
- [llm-as-judge-correct](llm-as-judge-correct.md) · [llm-evaluators](llm-evaluators.md) — automatic eval and its biases.
- [prompt-injection](prompt-injection.md) · [prevent-prompt-injection](prevent-prompt-injection.md) — security pillar.
