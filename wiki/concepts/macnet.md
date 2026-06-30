---
title: "MacNet: scaling multi-agent collaboration"
type: "Concept"
theme: multi-agent
level: 🔴
source_url: https://www.ibm.com/think/topics/chatdev
source_title: "What is ChatDev?"
---

# MacNet: scaling multi-agent collaboration

**In one sentence** — the extension of ChatDev that structures more than a thousand agents into an acyclic graph (DAG) and has them reason in topological order, with a law governing how quality grows with the number of agents.

## In detail
ChatDev implements a way to scale LLM-based multi-agent collaboration with **multi-agent collaboration networks (MacNet)**. MacNet draws on the principle of neural scaling — increasing the number of neurons makes capabilities emerge — and applies it to increasing the number of agents. Concretely, MacNet "uses acyclic graphs to structure agents and improve their interactive reasoning through topological ordering." Solutions are derived from the agents' interactions. This process consistently outperforms baseline models, fosters effective collaboration across different network topologies, and "enables cooperation among more than a thousand agents." Through this application, ChatDev identified a **collaborative scaling law** showing that solution quality improves following a **logistic growth model** as the number of agents increases.

## Example
The transposition is direct: just as adding neurons to a network makes capabilities emerge, MacNet structures the agents into a DAG and brings solutions up through the topological order of the interactions — and this process "consistently outperforms baseline models" across varied network topologies, not just one. Concretely, where ChatChain caps at two agents per phase, MacNet has more than a thousand agents cooperate on the same task, exceeding what no single agent could produce. It is the observation of this scaling that allowed the logistic growth law of quality to be identified.

## Tradeoff / insight (for a senior)
A real insight: the DAG + topological order transposes dependency scheduling (already known from pipelines) to LLM collaboration, which makes scaling deterministic. The logistic law implies diminishing returns — beyond a certain number of agents, the quality gain plateaus; stacking agents is not free indefinitely.

## Primary source
Described without a DOI in the source text — see the MacNet paper from the ChatDev/OpenBMB team for the exact reference.

## See also
- [chatdev-chatchain](chatdev-chatchain.md)
- [orchestration-types](orchestration-types.md)
