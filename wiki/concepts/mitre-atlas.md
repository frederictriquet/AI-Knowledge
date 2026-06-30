---
title: "MITRE ATLAS"
type: "Concept"
theme: security
level: 🔴
source_url: https://atlas.mitre.org/
---

# MITRE ATLAS

**In one sentence** — the matrix of adversarial tactics and techniques against AI systems, modeled on MITRE ATT&CK and backed by real-world case studies.

## What the source says

**MITRE ATLAS** is a knowledge base of adversarial behaviors observed or plausible against AI systems, modeled on the **MITRE ATT&CK** framework, of which it is the AI counterpart. It is organized into **tactics** (the "why": the goal of each stage) broken down into **techniques** (the "how"), and documents **case studies** (real incidents and red-team exercises).

Volume of the canonical **ATLAS.yaml v5.6.0** data: **16 tactics**, **101 techniques** (`AML.Txxxx`), **57 case studies** (`AML.CSxxxx`).

> ⚠️ **Frozen snapshot.** The local file [`md/ATLAS.yaml`](../../sources/security-references/md/ATLAS.yaml) is a **v5.6.0** copy whose first line carries the official warning: _"This version of the ATLAS data is deprecated and is no longer being updated"_. Handy for querying techniques offline (grep/script), but to be re-checked against [atlas.mitre.org](https://atlas.mitre.org/) for any up-to-date version.

The 16 tactics (ID `AML.TAxxxx`, descriptions summarized from the official YAML), in matrix order:

1. **Reconnaissance** (`AML.TA0002`) — gather information on the target AI system to plan operations.
2. **Resource Development** (`AML.TA0003`) — create, buy or compromise resources (AI artifacts, infrastructure, accounts).
3. **Initial Access** (`AML.TA0004`) — gain a first foothold in the AI system.
4. **AI Model Access** (`AML.TA0000`) — access the model itself (public API, indirect access via a product, or internal knowledge).
5. **Execution** (`AML.TA0005`) — run malicious code embedded in AI artifacts or software.
6. **Persistence** (`AML.TA0006`) — maintain access (poisoned data, tampered models left in place).
7. **Privilege Escalation** (`AML.TA0012`) — obtain higher permissions.
8. **Defense Evasion** (`AML.TA0007`) — evade detection by AI-powered security tools.
9. **Credential Access** (`AML.TA0013`) — steal credentials and passwords.
10. **Discovery** (`AML.TA0008`) — explore the AI environment and internal network.
11. **Lateral Movement** (`AML.TA0015`) — move to other components (model registries, vector stores, pipelines, agents).
12. **Collection** (`AML.TA0009`) — gather AI artifacts and information useful to the objective.
13. **AI Attack Staging** (`AML.TA0001`) — prepare the tailored attack (proxy models, poisoning, adversarial data).
14. **Command and Control** (`AML.TA0014`) — communicate with compromised AI systems to control them.
15. **Exfiltration** (`AML.TA0010`) — steal AI artifacts or information about the system.
16. **Impact** (`AML.TA0011`) — manipulate, interrupt, erode trust in or destroy AI systems and data.

> Note: most tactics carry an `ATT&CK-reference` (an explicit pointer to the corresponding ATT&CK tactic), confirming the alignment. The **AI Model Access** and **AI Attack Staging** tactics are specific to ATLAS (no ATT&CK equivalent), being specific to the ML lifecycle. **Lateral Movement** explicitly names AI agents as a high-value target (permissions often above a standard user account) — a recent addition (2025).

## Key techniques (extracted from ATLAS.yaml)

A selection of 14 `AML.Txxxx` techniques relevant to LLMs and agents, extracted verbatim (id + name) from the canonical `md/ATLAS.yaml` v5.6.0 file; the one-line description takes the first sentence of each technique's official `description`.

- **AML.T0051** — LLM Prompt Injection: malicious prompts as input to an LLM push it to act in unintended ways.
- **AML.T0054** — LLM Jailbreak: induce an LLM to ignore, bypass or override its alignment/safety behaviors and guardrails to obtain outputs it should withhold.
- **AML.T0056** — Extract LLM System Prompt: attempt to extract an LLM's system prompt.
- **AML.T0057** — LLM Data Leakage: craft prompts that lead the LLM to disclose sensitive information.
- **AML.T0020** — Poison Training Data: poison the datasets used by a model by modifying the underlying data or its labels.
- **AML.T0070** — RAG Poisoning: inject malicious content into the data indexed by a RAG system to contaminate a future thread via search results.
- **AML.T0053** — AI Agent Tool Invocation: use access to an AI agent to invoke the tools the agent has access to.
- **AML.T0080** — AI Agent Context Poisoning: manipulate the context used by an AI agent's LLM to influence its responses or the actions it takes.
- **AML.T0086** — Exfiltration via AI Agent Tool Invocation: invoke write-capable agent tools to exfiltrate data to an adversary.
- **AML.T0110** — AI Agent Tool Poisoning: obtain persistence by poisoning AI agents' tools, including built-in tools or those exposed via Model Context Protocol (MCP) connections.
- **AML.T0061** — LLM Prompt Self-Replication: use a prompt injection designed so that the LLM replicates the prompt in its own output.
- **AML.T0068** — LLM Prompt Obfuscation: hide or obscure prompt injections or retrieval content to evade detection (humans, LLM guardrails, other mechanisms).
- **AML.T0010** — AI Supply Chain Compromise: gain initial access by compromising the portions specific to the AI supply chain.
- **AML.T0029** — Denial of AI Service: target AI-powered systems with a flood of requests to degrade or stop the service.

## Example
A real case documented in ATLAS.yaml — **AML.CS0003, "Bypassing Cylance's AI Malware Detection"** (Skylight Cyber, 2019). The kill chain chains tactics: *Reconnaissance* (reading public talks and Cylance patents), *AI Model Access*, then *Discovery* via the **verbose logging** that exposes the model's reputation scoring and ensembling. The researchers discover a **second override model** whose positive verdicts take precedence over the main model; by merging the attributes of clean files into malware, they forge a **universal string** that, simply appended to a malicious file, makes it pass as benign.

## Why it matters

Where OWASP names *risks*, ATLAS supplies the **attack chain**: a tactics→techniques grammar that places each threat within an adversary's lifecycle (from reconnaissance to impact), with documented real-world incidents. This "AI kill-chain" view lets you map an agentic guardrail against a precise adversarial technique.

## Key points

- The AI counterpart of **MITRE ATT&CK** (same tactics + AI-specific extensions).
- **16 tactics**, **101 techniques**, **57 case studies** (v5.6.0 data).
- Two AI-specific tactics: **AI Model Access** and **AI Attack Staging**.
- 2025 agent-oriented tactics: **Lateral Movement** targets model registries, vector stores, pipelines and agents.
- A threat-modeling and red-teaming tool, backed by real cases.

## See also

- [Agentic security](agentic-security.md)
- [Adversarial attacks](adversarial-attacks-llm.md)
- [OWASP Top 10 LLM](owasp-llm-top-10.md) · [NIST AI 100-2](nist-ai-100-2.md)
- Official link: <https://atlas.mitre.org/>
