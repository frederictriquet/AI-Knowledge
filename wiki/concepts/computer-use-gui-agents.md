---
title: "Computer-use & GUI agents"
type: "Concept"
theme: tools-function-calling
level: 🔴
source_url: https://arxiv.org/abs/2307.13854
---

# Computer-use & GUI agents

**In one sentence** — driving a browser or an OS like a human, via **screenshots** as input and **actions** (click, type, scroll) as output.

## The idea
Rather than dedicated APIs or tools, the GUI agent perceives the screen (pixels, sometimes the accessibility tree) and acts at **coordinates**: it clicks, types, scrolls. This opens up any software interface, even without an API. Anthropic Computer Use industrialises this perception–action loop; SeeAct (Zheng et al.) uses GPT-4V for web agents. Benchmarks such as WebArena (realistic sites) and OSWorld measure the success of multi-step tasks in real environments.

## Example
A representative multi-site WebArena task: "find the art museums of Pittsburgh on Wikipedia, locate their addresses on the map (optimising the route), then update the README of the appropriate repository" — a single intent chaining Wikipedia, OpenStreetMap and GitLab. Evaluation rests on the functional correctness of the final state, not on the text produced. A telling detail of prompt fragility: with a simple hint that "some tasks may be unachievable" in the system prompt, GPT-4 wrongly declares **54.9% of feasible tasks impossible** — an illustration of the perception–action loop's sensitivity to instruction phrasing.

## Tradeoff / when to use it
Useful when **no API exists** or to automate visual workflows. The flip side: fragile (changing UI, imprecise coordinate grounding), slow, and **risky** (destructive actions, capture of sensitive data); to be sandboxed and supervised.

## Primary source
Anthropic, 2024, *Computer Use* (product documentation); Zhou et al., 2023, *WebArena: A Realistic Web Environment for Building Autonomous Agents*, arXiv:2307.13854 *(arXiv verified — HTTP 200 + title)*; Zheng et al., 2024, *SeeAct* (GPT-4V web agent) *(arXiv verified — HTTP 200 + title)*.

## See also
- [codeact](codeact.md)
- [tool-calling](tool-calling.md)
