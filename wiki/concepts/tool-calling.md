---
title: "Tool calling / function calling"
type: "Concept"
theme: tools-function-calling
level: 🟢
source_url: https://www.ibm.com/think/topics/tool-calling
source_title: "What is function calling?"
---

# Tool calling / function calling

**In one sentence** — the model emits a structured call (JSON + tool_call_id) that your code executes, then whose result it feeds back in.

## In detail
Tool calling (also called function calling) refers to the ability of an LLM to interact with external tools, APIs or systems to go beyond its pre-acquired knowledge: querying a database, fetching real-time data, executing code. The cycle breaks down into steps: recognizing the need for a tool, selecting the tool (each tool carries metadata — name, description, parameters, types), building a structured request, receiving and processing the response. A unique identifier links each request to its result. The LangChain examples show that the LLM returns only the tool's `name` and its `arguments` in `tool_calls`; actual execution remains the responsibility of the code, and each `ToolMessage` carries a `tool_call_id`. IBM Granite, Llama 3, Mistral and Claude all expose this capability, handled differently.

## Example
A user asks "What's the weather in San Francisco?". The model recognizes that it needs real-time data absent from its training and emits `get_weather(city="San Francisco")`, together with a unique `tool_call_id` that links the request to its result. **It executes nothing**: your code calls the weather API, receives a JSON `{temp: 14, humidity: 80, wind: 12}`, then feeds that result back to the model, which phrases it in natural language. Chained (LangChain-style), a second tool follows on from the first: weather → recommend suitable clothing.

## Tradeoff / insight (for a senior)
Key distinction: emitting the call and executing it are two separable steps. `bind_tools` produces the JSON without executing anything; an agent (or your loop) is needed to close the cycle. Reliability depends entirely on the quality of the tool and parameter `description`s, passed to the model for selection and argument filling.

## Primary source
"Tool calling, sometimes called function calling, is a key enabler of agentic AI." ([source](https://www.ibm.com/think/topics/tool-calling))

## See also
- [ReAct vs function calling](react-vs-function-calling.md)
- [Tool grounding](tool-grounding.md)
- [LLM nested in a tool](llm-in-a-tool.md)
