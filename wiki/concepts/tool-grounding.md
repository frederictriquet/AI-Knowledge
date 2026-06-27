---
title: "Tool grounding"
type: "Concept"
theme: tools-function-calling
level: 🟡
source_url: https://www.ibm.com/think/tutorials/use-lm-studio-to-build-automatic-tool-calling-granite
source_title: "Use LM Studio to build automatic tool calling with Granite"
migrated_from: tool-grounding
---

# Tool grounding

**In one sentence** — giving the agent tools that expose the verifiable legal state (e.g. legal chess moves) to prevent it from hallucinating its decisions.

## In detail
The idea is illustrated on two cases with LM Studio. First, calculation: an LLM alone does not return the exact quotient of `26.97 / 6.28` because "it cannot compute the quotient on its own"; it is given `add`, `subtract`, `divide`... functions that it chooses via `model.act()`. Then chess: a chatbot "often goes off the rails after several turns, making illegal or irrational moves". It is then equipped with tools — `legal_moves()`, `possible_captures()`, `possible_checks()`, `get_move_history()`, `get_book_moves()`, `make_ai_move()` — that expose the real and legal state of the board. The takeaway: "It's not much, but it's enough for the model to play a complete game of chess without hallucinating and to use intelligent reasoning to ground its decisions." The idea to remember: the tool lets the LLM ground its answers in factual data or precise operations.

## Example
The letter-counting case: "How many Bs are in the word 'blackberry'?" trips up the LLM alone (almost all pre-2024 models hallucinate "2 R" on strawberry). One defines `get_letter_frequency(word)` which returns a dict of frequencies, then calls `model.act("How many Bs…", [get_letter_frequency], on_message=print)`. The LM Studio trace shows a `ToolCallRequest` targeting the tool with `arguments={"word": "blackberry"}`, then the `AssistantResponse` gives the exact count. Same mechanism for `26.97 / 6.28` via `[add, subtract, multiply, divide, exp]`.

## Tradeoff / insight (for a senior)
Grounding does not remove the LLM's reasoning, it constrains it to a space of valid decisions. Rather than asking "what is your move?" (a free, hallucinable answer), you ask "among these legal moves, which one?". The system prompt indeed tells the model to use its chess knowledge as the primary method and the tools as assistants — grounding frames, it does not replace.

## Citation
"It's not much, but it's enough for the model to play a complete game of chess without hallucinating and to use intelligent reasoning to ground its decisions." ([use-lm-studio…](../../sources/ibm-guide-agents-ia/md/21-use-lm-studio-to-build-automatic-tool-calling-granite.md))

## See also
- [Tool calling / function calling](tool-calling.md)
- [Source verification](source-verification.md)
