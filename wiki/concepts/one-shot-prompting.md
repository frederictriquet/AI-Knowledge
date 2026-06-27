---
title: "One-shot prompting"
type: "Concept"
theme: prompting
level: 🟢
source_url: https://www.ibm.com/think/topics/one-shot-prompting
source_title: "What is one-shot learning?"
migrated_from: one-shot-prompting
---

# One-shot prompting

**In one sentence** — give the model a single well-crafted example so it generalizes a task, halfway between zero-shot and few-shot.

## In detail
One-shot relies on a single prompt-example to obtain the desired result, useful when collecting large volumes of training data is impractical. The GPT-3/GPT-4 and Granite LLMs are examples of this. Notably, the topic leans heavily toward vision: you find image/video-oriented mechanisms — in-context visual prompting (segmentation masks, bounding boxes, keypoints), adaptive feature projection (temporal variations in video action recognition), attention zooming (support/query cross-attention) — alongside the more general knowledge-based prompting. Benefits: efficiency (less data), fast deployment, flexibility. Limits: risk of biases inherited from pre-training data, variable accuracy on complex tasks. Use cases: chatbots, content creation, personalized recommendations, video action recognition.

## Example
Task: summarize a French document into English and fold the output into a specific API format. With a single prompt-example — "Summarize this French text into English using the API template `{Title}`, `{Key Points}`, `{Summary}`" — the LLM mobilizes its multilingual abilities and adaptive feature projection to directly produce the expected structure. In Python, you chain it through: the model's response, already in `{Title, Key Points, Summary}` format, is injected as-is into the API workflow, with no post-processing or training set.

## Tradeoff / insight
The drift toward vision is revealing: "one-shot" on the NLP side means one example in the prompt, but that sense often gets mixed up with computer vision's one-shot learning (segmentation, detection), two distinct research lineages. For textual LLM use, keep only the "one example in the context" mechanism and ignore the specialized vision sections.

## See also
- [Zero-shot prompting](zero-shot-prompting.md)
- [Few-shot prompting](few-shot-prompting.md)
