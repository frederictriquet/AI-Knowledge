---
title: "Structured outputs (instructor / Pydantic)"
type: "Concept"
theme: efficiency-cost
level: 🟡
source_url: https://python.useinstructor.com/
source_title: "Instructor: Top Multi-Language Library for Structured LLM Outputs"
objectives: [cost-control, production]
---

# Structured outputs (instructor / Pydantic)

**In one sentence** — get typed and validated data from an LLM (via Pydantic models) rather than parsing free text, with automatic validation and retries.

## What the source says
*instructor* is a library (Python first, but also TypeScript, Go, Ruby, Elixir, Rust) built on **Pydantic** to extract **structured outputs** from an LLM. You define a `BaseModel` describing exactly the desired fields, pass it as `response_model`, and the library guarantees a structured and validated output. Four pillars: *structured outputs* (the Pydantic schema), *automatic retries* (re-querying the model when validation fails — "reasking"), *data validation* (via Pydantic validators, e.g. `field_validator`, constraints `min_length`/`gt`), and *streaming* (partial and iterable objects). The `from_provider` interface is unified: the same code for OpenAI, Anthropic, Google, Ollama, DeepSeek and 15+ providers, sync or async. The docs position *instructor* as specialized in extraction ("Instructor for extraction, PydanticAI for agents"): it does one thing — provide reliable, validated data — and does it well, with full control over the prompt and type inference for the IDE.

## Example
You declare a nested schema: `class Ticket(BaseModel)` with `title: str = Field(..., min_length=5, max_length=100)`, `priority: Priority` (an `Enum` low/medium/high/critical), `estimated_hours: Optional[float] = Field(None, gt=0, le=100)`, plus a `@field_validator('estimated_hours')` that raises `ValueError` if the hour is not a multiple of 0.5. A `CustomerSupport` aggregates `tickets: List[Ticket] = Field(..., min_items=1)`. Call: `client.create(response_model=CustomerSupport, messages=[...], max_retries=3)` — if the LLM returns `estimated_hours=2.3`, the validator fails and instructor automatically re-queries the model until it gets a compliant typed object.

## Why it matters
*instructor* brings the *application* layer on the client side, complementary to constrained decoding and tool calling at the model level: declarative Pydantic schema, **validation retries** when the output violates constraints, and partial streaming — an approach portable across providers, independent of native constrained decoding.

## Key points
- Declarative Pydantic schema as the output contract (type safety, IDE support).
- Automatic validation + retries ("reasking") on constraint failure.
- Streaming of partial/iterable objects; `create_partial`, `create_iterable`.
- `from_provider`: a single multi-provider interface (sync/async).
- Deliberately narrow scope: structured extraction, not an agent framework.

## See also
- [Constrained decoding / structured output](constrained-decoding.md)
- [Tool calling](tool-calling.md)
- [LLM-as-judge (done right)](llm-as-judge-correct.md)
- [full post](../../sources/jason-liu/md/instructor-home.md)
