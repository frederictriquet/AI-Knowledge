---
title: "Role prompting (persona)"
type: "Concept"
theme: prompting
level: 🟢
source_url: https://www.ibm.com/think/tutorials/using-role-prompting-with-watsonx-and-granite
source_title: "Using role prompting with IBM watsonx and Granite"
migrated_from: role-prompting
---

# Role prompting (persona)

**In one sentence** — assign the model an explicit role or persona ("You are a compassionate veterinarian…") to steer the tone, style and behavior of the response.

## In detail
The hands-on part relies on watsonx.ai + Granite (granite-3-8b-instruct, via langchain_ibm). Role prompting (or persona prompting) consists of asking the model to assume a specific role. Two examples illustrate it: rewriting "Twinkle, Twinkle, Little Star" as a Shakespearean sonnet (role = William Shakespeare), and comparing a bare system prompt to a system prompt with the role of a "compassionate, professional, and experienced veterinarian" for a veterinary-clinic assistant. The response with a role is more nuanced, more empathetic and better contextualized. Multi-agent frameworks like ChatDev also use role prompting (a "self-attention mechanism"), and Granite models, trained on enterprise data, take on roles well. The evaluation remains purely qualitative: no metric, no figure.

## Example
On granite-3-8b-instruct, the bare prompt "My pet cat has been sneezing a lot lately and is licking her paws what should I do?" returns a flat list of tips, indistinguishable from a search-engine result. Prefixed with "You are a compassionate, professional, and experienced veterinarian.", the same model adopts an empathetic, contextualized tone without losing accuracy — a purely qualitative difference, at `TEMPERATURE: 0.7` and `MAX_NEW_TOKENS: 500`. The other demo, "You are William Shakespeare, rewrite 'Twinkle, Twinkle, Little Star' as a sonnet," does produce a sonnet in pentameter.

## Tradeoff / insight
A near-zero-cost technique with a real effect on tone, but the effect on factual accuracy is inconsistent and not measured here. A persona can induce hallucinations "in character" (a more assertive "expert" is not more accurate). Treat it as a style and UX lever, not a reasoning mechanism.

## Primary source
No bibliography. See the literature on persona/role prompting.

## See also
- [Zero-shot prompting](zero-shot-prompting.md)
- [Techniques catalogue](techniques-catalog.md)
