---
title: "Structural limitations of LLM agents (per Weng)"
type: "Concept"
theme: agent-fundamentals
level: 🟡
source_url: https://lilianweng.github.io/posts/2023-06-23-agent/
source_title: "LLM Powered Autonomous Agents"
migrated_from: agent-limites-weng
---

# Structural limitations of LLM agents (per Weng)

**In one sentence** — the three common limitations Weng identifies after surveying agent demonstrators: finite context, brittle long-horizon planning, and an unreliable natural-language interface.

## What the source says
In her conclusion, Weng notes three recurring limitations. **Finite context length**: the restricted capacity limits the inclusion of history, detailed instructions and the context of API calls; vector stores and retrieval broaden access to knowledge but their representational power remains inferior to full attention. **Challenges in long-term planning and decomposition**: planning over a long history and exploring the solution space efficiently remains hard; LLMs struggle to adjust their plans in the face of unexpected errors, so they are less robust than humans who learn by trial and error. **Reliability of the natural-language interface**: the agent relies on natural language as the interface between the LLM and external components, but the outputs may contain formatting errors or "rebellious" behavior (refusing an instruction) — which is why a large part of the demos' code is devoted to parsing outputs.

## Example
ChemCrow (Bran et al. 2023) illustrates the fragility of LLM-based evaluation, a corollary of the unreliable interface: an evaluation run by GPT-4 itself judges GPT-4 and ChemCrow to be nearly equivalent, whereas expert chemists judging actual chemical correctness see ChemCrow clearly outperform GPT-4. Without domain expertise, the LLM does not perceive its own flaws and cannot judge correctness. On long-horizon planning, the agent of Boiko et al. chains four steps well to "design an anticancer drug" but without robustness in the face of unexpected errors.

## Why it matters
Weng delivers an honest, structural critique (three named challenges) that balances the enthusiasm: it anchors the limitations in precise technical causes (finite attention, planning robustness, parsing), with a diagnostic rather than a solution orientation.

## Primary sources (cited by Weng)
- Weng, Lilian (Jun 2023). "LLM-powered Autonomous Agents", Lil'Log — personal synthesis of the limitations.
- AutoGPT (Significant-Gravitas) — illustration of the reliability problems of the natural-language interface and of parsing.

## See also
- [Short-/long-term memory](short-vs-long-term-memory.md)
- [ReAct](react.md)
- [full post](../../sources/lilian-weng/md/2023-06-23-agent.md)
