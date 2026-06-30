---
title: "Agentic security"
type: "Concept"
theme: security
level: 🔴
source_url: https://www.ibm.com/think/topics/ai-agent-security
source_title: "What is AI agent security?"
objectives: [reliability]
---

# Agentic security

**In one sentence** — an agent's attack surface (autonomous decision + tool calling) is much wider than that of an LLM alone, and calls for Zero Trust, least-privilege and sandbox countermeasures.

## In detail
An agent's attack surface breaks down into two parts: manipulating the agent's behavior, or attacking the tool itself (e.g. SQL injection). The threat landscape: a widened surface, fast autonomous actions, unpredictable inference (probabilistic, hence non-predictable), lack of transparency. Vulnerabilities listed: **prompt injection** both direct and **indirect** (a malicious prompt hidden in the data source, triggered on retrieval — multimodal agents are particularly exposed), **tool and API manipulation**, **data poisoning**, **memory poisoning** (corrupting persistent memory to shape later behavior), **privilege compromise**, **authentication spoofing**, **RCE**, **cascading failures** (a compromised agent's output degrades the next one until the system fails). **Slopsquatting** (a portmanteau of "AI slop" + "typosquatting"): registering a library name close to a legitimate one so the model pulls code from the fake lib — a supply-chain exploit. Countermeasures: **Zero Trust** (never trust, always verify), **least privilege** (RBAC/ABAC), contextual authentication, encryption (AES-256), microsegmentation and a **sandbox** for code execution, prompt hardening and validation, adversarial training (still immature).

## Example
A customer-service agent interacts with a user then connects to the internal database to read their purchase history: if its privileges are not revoked after the task, an attacker who spoofs its credentials inherits those same rights (read sensitive data, run transactions, grant itself more permissions) and progresses through lateral movement. On the supply-chain side, slopsquatting illustrates the blind spot: a coding agent pulls code from a fake lib with a name close to a legitimate one, and injects it into the deliverable without any input validation catching it.

## Tradeoff / insight
The taxonomy overlaps the OWASP Top 10 for LLM/Agentic (prompt injection, leakage, supply-chain). The non-trivial point: probabilistic inference makes the defense different from classic cybersecurity — you cannot enumerate behaviors, hence the importance of runtime controls (sandbox, least privilege) rather than input validation alone.

## Primary source
No academic reference; taxonomy close to the OWASP Top 10 for LLM Applications.

## See also
- [guardrail-noeud-entree](entry-node-guardrail.md)
- [ethique-gouvernance](ethics-governance.md)
