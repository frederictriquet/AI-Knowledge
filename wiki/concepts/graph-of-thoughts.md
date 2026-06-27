---
title: "Graph of Thoughts (GoT)"
type: "Concept"
theme: reasoning-planning
level: 🔴
source_url: https://arxiv.org/abs/2308.09687
migrated_from: graph-of-thoughts
---

# Graph of Thoughts (GoT)

**In one sentence** — reasoning is modeled as an arbitrary graph of thoughts where you can not only branch but also **merge** several thoughts, loop and refine, where Tree-of-Thoughts is limited to a tree.

## The idea
GoT represents each intermediate thought as a node in a graph; edges encode transformations. Beyond simple tree expansion, it allows operations impossible in a tree: **aggregation** (merging several partial solutions into a better one), **refinement** (an improvement loop on the same node) and generation. A controller orchestrates these operations and scores the nodes. This structure better captures problems where sub-solutions must be recombined (sorting, document merging, aggregation).

## Example
The demonstration task is sorting lists: the list is split into separately sorted sublists, then GoT's own **aggregation** operation merges these partial solutions into a sorted list — exactly the kind of recombination a ToT tree cannot model. On this benchmark, GoT improves sorting quality by 62% over Tree-of-Thoughts while reducing costs by more than 31%: the gain does not come from more exploration but from a structure that captures the "merge two sorted halves" dependency.

## Tradeoff / when to use it
More **expressive** than ToT: it models dependencies a tree cannot (branch merging). In return, it is more costly and complex to orchestrate — you must define the graph, the merge operations and the scoring function. Reserve it for tasks where recombining partial solutions yields a measurable gain; for purely divergent exploration, ToT suffices and costs less.

## Primary source
Besta et al., 2023, *Graph of Thoughts: Solving Elaborate Problems with Large Language Models*, arXiv:2308.09687. *(arXiv verified — HTTP 200 + title)*

## See also
- [tree-of-thoughts](tree-of-thoughts.md)
- [lats](lats.md)
