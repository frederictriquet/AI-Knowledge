---
title: "Prompt caching"
type: "Concept"
theme: prompting
level: 🟡
source_url: https://www.ibm.com/think/tutorials/implement-prompt-caching-langchain
source_title: "Implement prompt caching with LangChain to build efficient LLM applications"
objectives: [cost-control]
---

# Prompt caching

**In one sentence** — reusing an already-computed response for an identical prompt, but beware: the tutorial implements an exact-match response cache on the client side (LangChain `SQLiteCache`), not provider-side prefix prompt caching (KV-cache).

## In detail
Prompt caching is presented as a "memory" for the application: if the same input is seen again, the stored response is retrieved instead of re-issuing an API call, hence reduced latency, consistent outputs, less pressure on rate limits, and more resilience. The tutorial concretely wires `set_llm_cache(SQLiteCache(database_path=".langchain.db"))` onto a `WatsonxLLM` (Granite 3-8B): the cache stores responses in a local SQLite database and is hit only on an exact prompt match. The measurements show very low CPU time but wall-clock time dominated by I/O and network wait. The conclusion broadens the topic to provider-side prompt caching, which caches input/output tokens, embeddings, prefixes, and system messages, and mentions TTL, cache-hit rate, cache read/write — a layer distinct from the exact-match `SQLiteCache` presented.

## Example
The tutorial sends Granite 3-8B the prompt `"System: You are a helpful assistant.\nUser: Why did Paul Graham start YC?\nAssistant:"`. First call: 22 ms of CPU time but 1.43 s of wall-clock time — the gap reveals that the cost is dominated by I/O and network wait, not by computation. With `set_llm_cache(SQLiteCache(database_path=".langchain.db"))` active, the re-call consumes only ~7 ms CPU: the response is read back from the local `.langchain.db` instead of being regenerated. Corollary: even a slightly modified prompt misses the exact-match cache and pays full price again.

## Tradeoff / insight
Two mechanisms not to be confused. (1) Exact-match response cache (this tutorial): maximal gain but fragile hit rate — the slightest prompt variation causes a miss; useful for requests repeated identically (tests, frozen FAQs). (2) Provider-side prefix prompt caching / KV-cache: reuses the computation of the shared prefix (system + context), billed at a lower rate, and tolerates a variable prompt tail. For semantic similarity (rather than strict equality), you need semantic caching, a third and still-different mechanism.

## Prefix KV-cache in detail (Anthropic / OpenAI)
At inference, the model computes a KV cache (attention keys/values) per token. When a long prefix is identical from one call to the next — system, tool definitions, large document — the provider keeps this cache and resumes computation right after the prefix; only the new tokens are processed, and cached tokens are billed at a reduced rate. Two practical constraints: the cache has a **short lifetime** (a few minutes) and requires an **exactly** identical prefix — hence the rule: **order the prompt from most stable to most variable** to maximize hits.

## Primary source
Tutorial *Implement prompt caching with LangChain* ([source](https://www.ibm.com/think/tutorials/implement-prompt-caching-langchain)) for the LangChain/watsonx exact-match cache. For the prefix KV-cache: Anthropic, *Prompt caching* (2024, product doc); OpenAI, *Prompt caching* (2024, product doc). No academic reference.

## See also
- [Semantic caching](semantic-caching.md)
