---
title: "Catalog of prompting techniques"
type: "Concept"
theme: prompting
level: 🟢
source_url: https://www.ibm.com/think/topics/prompt-engineering-techniques
source_title: "Prompt engineering techniques"
migrated_from: techniques-catalogue
---

# Catalog of prompting techniques

**In one sentence** — an index of prompt-structuring strategies, applied to a single task ("explain climate change") to compare their behaviors.

## In detail
First, three ways to structure a prompt are distinguished: direct instructions (a precise command), open instructions (creative exploration) and task-specific instructions (translation, summarization, calculation). Then ~18 techniques are walked through, illustrated on the same task: zero-shot, few-shot, chain-of-thought (CoT), meta-prompting, self-consistency, generated knowledge prompting, prompt chaining, tree-of-thoughts (ToT), RAG, automatic reasoning and tool-use (ART), automatic prompt engineering (APE), active prompting, directional stimulus prompting (DSP), program-aided models (PAL/PALM), ReAct, Reflexion, multimodal CoT, graph prompting. The cited challenges: hallucination, difficulty producing reliable outputs, the generality/specialization balance.

## Example
Three prompts from the source show how the same "climate" task specializes depending on the technique. RAG: `Using the global temperature datasets from NASA GISS (GISTEMP)... explain climate change`. DSP (directional stimulus): `Explain... from an environmentalist's perspective, focusing on the need for immediate action`. PAL/PALM: `Write Python code to visualize the increase in global temperatures over time. Then explain how this data relates to climate change`. Same objective, but the source of truth (external dataset), tone (bias) and execution (code) diverge radically depending on the prompt.

## Tradeoff / insight (for a senior)
The value of this page is pedagogical: seeing 18 techniques on a single task shows that they are not competing but composable (RAG + few-shot, CoT + self-consistency). Watch for translation approximations and the conflation of "PALM" with PAL.

## Primary source
Each technique points to numbered footnotes, but with no bibliography resolved in the text — references not made explicit.

## See also
- [zero-shot-prompting](zero-shot-prompting.md)
- [few-shot-prompting](few-shot-prompting.md)
- [chain-of-thought](chain-of-thought.md)
- [meta-prompting](meta-prompting.md)
