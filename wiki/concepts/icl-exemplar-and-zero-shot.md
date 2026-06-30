---
title: "ICL: exemplar selection & zero-shot techniques"
type: "Concept"
theme: prompting
level: 🔴
source_url: https://arxiv.org/abs/2406.06608
source_title: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
---

# ICL: exemplar selection & zero-shot techniques

**In one sentence** — In few-shot, the choice of examples, their order and their quantity matter as much as the prompt content; in zero-shot, several simple rephrasings of the instruction are enough to improve the output.

## What the source says
The report (§2.2.1) presents In-Context Learning: the model learns a task via exemplars and/or instructions in the prompt, with no weight update. It isolates six few-shot design decisions. Exemplar quantity generally helps (especially on large models), with sometimes diminishing benefits beyond 20. Exemplar order can make accuracy vary from under 50% to over 90% on certain tasks (Lu et al., 2021). Also matter: the distribution and quality of labels, the format, and similarity to the test case. To select exemplars, K-Nearest Neighbor (Liu et al.) keeps those closest to the test, and Vote-K (Su et al.) proposes candidates to annotate in two steps while guaranteeing diversity. On the zero-shot side, it names Role Prompting, Style Prompting, Emotion Prompting, System 2 Attention (S2A), SimToM, Rephrase and Respond (RaR), Re-reading (RE2) and Self-Ask.

## Example
The sixth decision, Exemplar Label Quality, gives a counterintuitive result: Min et al. (2022) show that providing exemplars with *incorrect* labels does not necessarily degrade performance — label accuracy sometimes seems secondary, with large models even absorbing wrong or off-topic labels (Wei et al.). Conversely, distribution biases the model: 10 exemplars of one class against 2 of the other pushes the model to over-predict the first. On the zero-shot side, S2A (Weston and Sukhbaatar) unfolds in two steps: a first prompt rewrites the question by removing irrelevant information, and only this stripped-down version is resubmitted to answer.

## Why it matters
Beyond the few-shot and zero-shot principles, this report quantifies empirical sensitivity (order, quantity, similarity) and names precise zero-shot techniques (S2A, SimToM, RaR, RE2, Self-Ask) rarely documented elsewhere.

## Key points
- Exemplar Ordering: order alone can drop or raise accuracy by more than 40 points.
- Exemplar Quantity: more exemplars help, but sometimes with diminishing benefits beyond 20.
- KNN / Vote-K: selecting exemplars similar to the test case (KNN costly; Vote-K adds diversity).
- Role / Style / Emotion Prompting: assign a role, a style, or a psychologically charged phrase.
- S2A, SimToM, RaR, RE2, Self-Ask: rephrase, filter the context or self-question before answering.

## See also
- [Few-shot](few-shot-prompting.md)
- [Zero-shot](zero-shot-prompting.md)
- [In-context learning](in-context-learning.md)
- [Role prompting](role-prompting.md)
- [full paper](https://arxiv.org/abs/2406.06608)
