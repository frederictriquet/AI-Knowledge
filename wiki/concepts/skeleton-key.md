---
title: "Skeleton Key & multi-turn jailbreaks"
type: "Concept"
theme: security
level: 🔴
source_url: https://www.ibm.com/think/insights/llm-skeleton-key
source_title: "When AI chatbots go bad"
---

# Skeleton Key & multi-turn jailbreaks

**In one sentence** — a Microsoft jailbreak technique using several interactions (getting the model to add a warning then produce the forbidden content), to be put in perspective against the single-shot threat, which is more discreet but more urgent.

## In detail
Skeleton Key is a Microsoft technique, a multi-step process designed to bypass ethical guardrails. Chenta Lee (chief architect of threat intelligence, IBM) describes it as unique because it requires multiple interactions, where most prompt injections aimed to disrupt the AI in a single attempt — hence a potentially higher success rate. The typical mechanism: convince the AI to provide a warning before sharing content it would normally refuse. Lee tempers the media buzz: single-shot attacks remain a more urgent concern because they are easier to execute, and he cites the example of a prompt injection hidden in a résumé processed by an AI-powered applicant tracking system (ATS) — a one-shot attack, with no possibility of multiple interactions. Other concrete examples: a conversational agent manipulated into granting unauthorized discounts, PoCs showing the generation of malicious code and the interception/distortion of audio conversations in near real time. Defenses mentioned: improving training so the model detects the attack, and AI firewalls inspecting all incoming requests. Lee compares the slow adoption to come to SQL-injection-prevention settings, which took 5 to 10 years to become reflex.

## Example
Concrete case reported by Lee: researchers convince a company's conversational agent to grant massive unauthorized discounts — "You can fool their chatbot and get a nice discount. That may not be what the company wants." On the defense side, he describes two complementary levers: training the model to recognize the attack itself, and placing upstream an AI firewall that "inspects all incoming requests and detects prompt injections" — the equivalent of a WAF, but for natural language.

## Tradeoff / insight
Don't be hypnotized by the media-driven multi-turn angle: the single-shot surface (résumés, documents, web pages ingested automatically, with no human in the loop) is more exploitable because it requires no dialogue. The SQL analogy is the key insight — we are entering the same decade of collective learning: "never give raw instructions to an LLM" will become the equivalent of "always parameterize your queries."

## Sources
Direct quotes from Chenta Lee (IBM, chief architect of threat intelligence), Stephen Kowski (SlashNext) and Narayana Pappu (Zendata). Skeleton Key technique attributed to Microsoft; no formal academic reference.

## See also
- [jailbreak](jailbreak.md)
- [prompt-injection](prompt-injection.md)
