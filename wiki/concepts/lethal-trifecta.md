---
title: The "lethal trifecta"
type: "Concept"
theme: security
tags: [security, prompt-injection, agents, exfiltration]
level: 🔴
source_url: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
source_title: "The lethal trifecta for AI agents — Simon Willison, 2025"
migrated_from: lethal-trifecta
---

# The "lethal trifecta"

**In one sentence** — prompt injection becomes a real data leak only when an agent combines three capabilities at once; removing a single one neutralizes the whole class of attack.

## The idea
Simon Willison formalizes why certain agent assemblies are catastrophic. The danger is not prompt injection alone, but the conjunction of **three ingredients**: (1) access to private data, (2) exposure to untrusted content (emails, web pages, third-party documents), (3) outbound communication capability enabling exfiltration. Combined, they let an attacker inject an instruction via the untrusted content, read the private data, then send it back. The framework is diagnostic: you inspect an agent and check the three boxes.

## Example
The GitHub MCP case combines all three legs in a single tool: it reads public issues (untrusted content, which an attacker can freely deposit), accesses private repositories (sensitive data), and creates pull requests (outbound channel). The attack unfolds: deposit a public issue containing hidden instructions; when the agent processes it, it follows the injection, reads the victim's private repositories, and exfiltrates their content into a PR pushed to the attacker's account. No single link is hacked individually — it is their conjunction that creates the full chain.

## Tradeoff / when to use it
An architecture-review tool: breaking the trifecta by removing one vertex (cutting off exfiltration, isolating private data, or only processing trusted content) is more robust than trying to "filter" injection, which remains unsolved to date. Cost: you amputate useful features (an agent that can send nothing loses value).

Two warnings from Willison: (1) **guardrails do not save you** — a product that blocks "95% of attacks" is a failure in application security, because the attacker targets precisely the remaining 5%; (2) **MCP worsens** the risk by encouraging the mixing of tools from different sources, which combines the three legs without one realizing it. On the user side, the only safe countermeasure is to avoid the combination entirely: providers will not save you.

## Primary source
Simon Willison, 2025, *The lethal trifecta for AI agents* (blog post, simonwillison.net; no arXiv). Willison is the reference primary source on **prompt injection**: he coined the term and the notion of the lethal trifecta.

## See also
- [dual-llm-camel](dual-llm-camel.md)
- [securite-agentique](agentic-security.md)
