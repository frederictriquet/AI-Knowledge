---
title: "Agent ethics & governance"
type: "Concept"
theme: governance-alignment-ops
level: 🔴
source_url: https://www.ibm.com/think/insights/ai-agent-ethics
source_title: "New ethical risks from AI agents? Researchers weigh in"
---

# Agent ethics & governance

**In one sentence** — align agents on natural-language policy documents and organize oversight where the human decides while the AI questions, all framed by governance agents, ethical sandboxes and a kill switch.

## In detail
Via Kush Varshney (IBM Research). **Alignment Studio** "aligns large language models with the rules and values described in natural-language policy documents, such as government regulations or a company's own ethical guidelines", with a continuous cycle so that models "actually adopt the desired behaviors" and not just the vocabulary. **Granite Guardian 3.1** "detects function-calling hallucinations by agents before unintended consequences occur". **RADAR** (Chinese University of Hong Kong + IBM Research): an AI-text detector based on adversarial learning between two models. **Adversarial collaboration** inverts the usual roles: "the human makes the final decision; the algorithm is not designed to compete in that role, but to question and […] refine the recommendations of the human agent" — preserving dignity. Reference to the paperclip maximizer scenario (Bostrom). **Governance**: an ethical **sandbox** (simulated environments, "moral stress tests"), agent-to-agent monitoring, **governance agents** "designed to monitor and evaluate other agents" (model-drift detection), a **human approval** request for certain actions, and an **emergency stop mechanism** (kill switch) for immediate deactivation in high-risk environments.

## Example
The cited mishaps are not theoretical: leaks of confidential data, insulting messages and, in one case, a recipe for deadly chlorine gas, all attributed to chatbots gone wrong. On the agentic side, Varshney describes agents sending inappropriate emails or starting/stopping machines outside their intended scope — hence the listing of "autonomy" as a risk by the DHS (April 2024 report) for critical infrastructure. The paperclip maximizer illustrates the upper limit: an ASI maximizing paperclips would consume all the planet's resources, the autonomy becoming manifestly excessive.

## Tradeoff / insight
The non-trivial point is the **inversion** of adversarial collaboration: the AI does not assist the human, it challenges them — the human stays the decision-maker, the AI plays devil's advocate. And the idea of **governance agents** (an agent that audits other agents) shifts control to runtime rather than pre-deployment.

## Primary source
Alignment Studio, *IEEE Internet Computing*, September 2024; paperclip scenario, Nick Bostrom; "autonomy" risk, DHS report, April 2024; disinformation warning, Google DeepMind, April 2024; adversarial collaboration, August 2024 research paper.

## See also
- [securite-agentique](agentic-security.md)
- [guardrail-noeud-entree](entry-node-guardrail.md)
- [taxonomie-erreurs-appel-fonction](function-calling-error-taxonomy.md)
