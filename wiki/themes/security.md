---
type: index
title: "Theme — Security"
theme: security
---

# 🔐 Security

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Threats, injections and defense of LLM systems._

## Concepts (21)

### 🔴 Substance / core
- **[AI injections: direct and indirect prompt injection](../concepts/ai-injections-basics.md)** — sending untrusted data to an LLM is the modern equivalent of SQL injection or XSS: the attacker reprograms the AI's "persona" and objective.
- **[ASCII Smuggling: hiding instructions via Unicode Tags](../concepts/unicode-tags-smuggling.md)** — a block of Unicode characters (the Unicode Tags Block) that mirrors ASCII stays invisible to humans in the UI, but LLMs interpret it — hence a prompt injection undetectable to the eye.
- **[Adversarial attacks on LLMs (Weng's taxonomy)](../concepts/adversarial-attacks-llm.md)** — the real mechanics of attacks: at frozen weights and at inference, five families of attacks are distinguished, separated mainly by the white-box (gradient access) vs black-box (API only) axis.
- **[Agentic security](../concepts/agentic-security.md)** — an agent's attack surface (autonomous decision + tool calling) is much wider than that of an LLM alone, and calls for Zero Trust, least-privilege and sandbox countermeasures.
- **[ChatDev: ChatChain, CAMEL, communicative dehallucination](../concepts/chatdev-chatchain.md)** — a framework that simulates a waterfall software company (design/coding/testing) through a two-agent dialogue per phase, where the assistant deliberately reverses roles to demand clarifications before coding.
- **[Dual-LLM pattern & CaMeL](../concepts/dual-llm-camel.md)** — defend against injection *by design* by separating roles: a privileged LLM plans without ever reading untrusted content, while a quarantined LLM processes that content with no privileges.
- **[Jailbreak](../concepts/jailbreak.md)** — convincing an LLM to ignore its alignment guardrails to produce forbidden content, distinct from injection (which disguises instructions rather than bypassing ethical protections).
- **[MITRE ATLAS](../concepts/mitre-atlas.md)** — the matrix of adversarial tactics and techniques against AI systems, modeled on MITRE ATT&CK and backed by real-world case studies.
- **[Microsoft 365 Copilot: from injection to email exfiltration](../concepts/m365-copilot-exfil.md)** — a complete exploitation chain on M365 Copilot, started by a simple prompt injection in an email, that steals the victim's emails and personal data.
- **[NIST AI 100-2: a taxonomy of adversarial ML](../concepts/nist-ai-100-2.md)** — the official US taxonomy of *adversarial machine learning*, which separates predictive AI from generative AI and classifies attacks (evasion, poisoning, privacy breaches, direct/indirect prompt injection) along five axes.
- **[OWASP Top 10 for LLM Applications](../concepts/owasp-llm-top-10.md)** — the de facto community reference that names the ten most critical security risks of LLM-based applications, now extended by an "Agentic AI" section.
- **[Preventing prompt injection](../concepts/prevent-prompt-injection.md)** — a catalogue of partial defenses against prompt injection, to be stacked as defense-in-depth, none of them being foolproof (the only absolute guarantee would be to not use an LLM at all).
- **[Prompt injection](../concepts/prompt-injection.md)** — making an LLM execute malicious instructions disguised as legitimate input, an irreducible flaw because the system prompt and user input share the same type: natural language.
- **[Prompt injection: why it matters (and why naive defenses fail)](../concepts/prompt-injection-why-it-matters.md)** — the fundamental problem (instructions and data share the same channel and are inseparable), the data-exfiltration scenarios, and why filtering or escaping is not enough: "in security, 99% is not enough."
- **[Skeleton Key & multi-turn jailbreaks](../concepts/skeleton-key.md)** — a Microsoft jailbreak technique using several interactions (getting the model to add a warning then produce the forbidden content), to be put in perspective against the single-shot threat, which is more discreet but more urgent.
- **[Taxonomy of \"prompt hacking\](../concepts/prompt-hacking-taxonomy.md)** — the report structures prompting security into three blocks: attack types (injection vs jailbreak), concrete risks, and hardening measures — none of them fully reliable.
- **[The "lethal trifecta](../concepts/lethal-trifecta.md)** — prompt injection becomes a real data leak only when an agent combines three capabilities at once; removing a single one neutralizes the whole class of attack.
- **[The Dual LLM pattern](../concepts/dual-llm-pattern.md)** — A defensive architecture: a Privileged LLM (with tools and privileges, NEVER sees untrusted content) plus a Quarantined LLM (processes untrusted content, no privileges); the privileged one manipulates symbolic references, not the untrusted text.

### 🟡 Tradeoff / intermediate
- **[Entry-node guardrail (Granite Guardian)](../concepts/entry-node-guardrail.md)** — place a moderation detector (HAP/PII via Granite Guardian) as the very first node of the graph, and route through a conditional edge to block undesirable content BEFORE it reaches the LLM and the tools.
- **[OWASP Top 10 LLM & agentic threats](../concepts/owasp-llm-agentic.md)** — the de facto standard security reference: a shared taxonomy of LLM risks, extended by a section specific to agentic threats.
- **[Spotlighting](../concepts/spotlighting.md)** — explicitly mark untrusted data in the prompt so the model distinguishes "instructions" from "data" and does not execute injected content.

## Tools (7)

- **[AIDA (AI-Driven Security Assessment)](../tools/aida.md)** — _Autonomous pentest agent (CLI + web dashboard)_
- **[Burp Suite MCP Server (PortSwigger)](../tools/burp-mcp-server.md)** — _MCP server / Burp Suite extension (Kotlin)_
- **[ECC](../tools/ecc.md)** — _Agent harness system (skills/agents/hooks/rules) — multi-platform, OSS + GitHub App_
- **[MCP Kali Server](../tools/mcp-kali-server.md)** — _MCP server (command-execution bridge to Kali Linux)_
- **[MCP ZAP Server](../tools/mcp-zap-server.md)** — _MCP server — OWASP ZAP operator_
- **[Shannon (Keygraph)](../tools/shannon.md)** — _Autonomous CLI agent (white-box AI pentester)_
- **[Snyk MCP (the Snyk CLI's MCP server)](../tools/snyk-mcp.md)** — _MCP server (built into the Snyk CLI) — defensive security / AppSec_
