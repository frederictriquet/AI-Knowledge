---
title: "LLM nested inside a tool"
type: "Concept"
theme: tools-function-calling
level: 🟡
source_url: https://www.ibm.com/think/tutorials/local-tool-calling-ollama-granite
source_title: "Tool calling with Ollama"
---

# LLM nested inside a tool

**In one sentence** — a tool called by the agent itself uses an LLM call internally (e.g. a yes/no relevance classifier).

## In detail
A `search_text_files(keyword)` tool scans the files of a local folder. Rather than a simple string match, the function uses Granite 3.2 to determine whether the keyword describes the document's text. Concretely, the tool reads the document into `document_text`, then calls `ollama.chat` with the prompt: `"Respond only 'yes' or 'no', do not add any additional information. Is the following text about " + keyword + "? " + document_text`. If the model answers "yes," the tool returns the file name. The second tool, `search_image_files`, applies the same principle via Granite 3.2 Vision to describe each image and search it for the keyword. Of note: "one of the strengths of using Ollama is that you can easily build multi-agent systems to call one model with another."

## Example
User request "Information about dogs." Granite 3.2 Dense extracts the keyword `dogs` and triggers both tools in parallel: `search_text_files(keyword="dogs")` iterates over `./files/`, and for each PDF/`.txt` launches an `ollama.chat(model="granite3.2:8b", ...)` call with the prompt "Respond only 'yes' or 'no'…" — it returns `./files/File4.pdf` on the first "Yes." `search_image_files(keyword="dogs")` has each image described by `granite3.2-vision` and returns `None`. The results are reinjected into the model, which concludes: "The keyword "dogs" was found in File4.pdf."

## Tradeoff / insight (for a senior)
The orchestration LLM (Granite 3.2 Dense) selects the tool and generates its arguments; a second LLM call, encapsulated in the tool, does the fine-grained semantic classification. You pay one call per scanned document — expensive and slow at scale — but you gain a match by meaning rather than by literal string. The pattern turns "function calling" into a tree of nested LLM calls, to watch for latency and token cost.

## Primary source
"As Ollama makes it easy to call local LLMs, `research_text_files` will use Granite 3.2 to determine whether the keyword describes the document's text." ([source](../../sources/ibm-guide-agents-ia/md/20-local-tool-calling-ollama-granite.md))

## See also
- [Tool calling / function calling](tool-calling.md)
- [Agentic RAG](agentic-rag.md)
