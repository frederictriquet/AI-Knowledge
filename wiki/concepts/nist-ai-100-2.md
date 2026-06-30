---
title: "NIST AI 100-2: a taxonomy of adversarial ML"
type: "Concept"
theme: security
level: 🔴
source_url: https://csrc.nist.gov/pubs/ai/100/2/e2025/final
---

# NIST AI 100-2: a taxonomy of adversarial ML

**In one sentence** — the official US taxonomy of *adversarial machine learning*, which separates predictive AI from generative AI and classifies attacks (evasion, poisoning, privacy breaches, direct/indirect prompt injection) along five axes.

## What the source says

The report *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations* (NIST Trustworthy and Responsible AI) proposes a **common taxonomy and terminology** of AML, organized by ML method types, lifecycle stages, and the attacker's goals/capabilities/knowledge (abstract verbatim from the CSRC page).

The report **classifies each attack along five axes** (verbatim from the Executive Summary): (i) the **type of AI system**, (ii) the **stage of the ML lifecycle** at which the attack is mounted, (iii) the **attacker's goals and objectives** (the system properties they seek to violate), (iv) the attacker's **capabilities and access**, (v) the **knowledge** they have of the learning process.

Structure of the taxonomy (table of contents verbatim from the PDF):

**2. Predictive AI (PredAI) Taxonomy**
- 2.1 Classification: stages of learning; attacker goals & objectives; capabilities; knowledge; data modality.
- 2.2 **Evasion Attacks** — white-box, black-box, transferability, real world, mitigations.
- 2.3 **Poisoning Attacks** — availability poisoning, targeted, backdoor, **model poisoning**, real world.
- 2.4 **Privacy Attacks** — data reconstruction, membership inference, property inference, model extraction.

**3. Generative AI (GenAI) Taxonomy**
- 3.1 Classification: GenAI stages of learning; attacker goals & objectives; capabilities.
- 3.2 **Supply Chain Attacks** — data poisoning, model poisoning.
- 3.3 **Direct Prompting Attacks** — attack techniques, **information extraction**, mitigations.
- 3.4 **Indirect Prompt Injection Attacks** — availability, integrity, **privacy compromise**, mitigations.
- 3.5 **Security of Agents**.
- 3.6 Benchmarks for AML Vulnerabilities.

**4. Key Challenges and Discussion** — including the trade-offs between the attributes of Trustworthy AI.

> Structuring distinction (Executive Summary, verbatim): the taxonomy separates **predictive** and **generative** systems, and considers the AI system's components (data, model, training/test/deployment process, software context) — notably the cases where a GenAI model has access to **private data** or is **equipped with tools acting on the real world**.
>
> On the axes of attacker knowledge, the report uses **white-box**, **black-box** and **gray-box** *(presence confirmed in the text; the detail of each definition to be checked in the body of the report)*. The report relies on the **NIST AI Risk Management Framework** for the notions of security, resilience and robustness, without recommending a risk-tolerance threshold.

## Example
The report grounds the taxonomy in real cases. On the GenAI evasion side, it cites the **ASCII-art attack**: an ASCII illustration of a banned term makes the chatbot produce the harmful information when it would correctly censor the plain-text word — "the semantic distance between the two prompts is exactly zero." On the real poisoning side, it documents **Tay.AI** (Microsoft chatbot poisoned in under 24 h in 2016 via online learning), the campaigns of millions of emails against Gmail's spam filter, and an incident on VirusTotal (variants of a ransomware submitted to skew its classification).

## Why it matters

This is the **official reference report** for adversarial AI security. It provides the fine-grained grid: evasion vs poisoning vs privacy for predictive, and — on the generative side, the most relevant for agents — the clear separation between **direct prompting** and **indirect prompt injection**, plus a dedicated **Security of Agents** section. Normative vocabulary, aligned with the AI RMF.

## Key points

- Two families: **PredAI** and **GenAI**, each with its own taxonomy.
- 5 classification axes: system type, lifecycle stage, goals, capabilities, knowledge.
- PredAI: **evasion**, **poisoning** (availability / targeted / backdoor / model), **privacy** (reconstruction, membership/property inference, model extraction).
- GenAI: **supply chain**, **direct prompting**, **indirect prompt injection** (availability / integrity / privacy), **Security of Agents**, benchmarks.
- Anchored in the **NIST AI Risk Management Framework**; no prescription of a risk tolerance.

## See also

- [Prompt injection](prompt-injection.md)
- [Injection: why it matters](prompt-injection-why-it-matters.md)
- [OWASP Top 10 LLM](owasp-llm-top-10.md) · [MITRE ATLAS](mitre-atlas.md)
- Official link: <https://csrc.nist.gov/pubs/ai/100/2/e2025/final> · DOI: <https://doi.org/10.6028/NIST.AI.100-2e2025>
