---
title: "CrewAI"
type: "Concept"
theme: frameworks-tooling
level: 🟢
source_url: https://www.ibm.com/think/topics/crew-ai
source_title: "What is CrewAI?"
---

# CrewAI

**In one sentence** — a multi-agent framework built on LangChain that organises agents into a "crew" via roles, tasks and processes (sequential or hierarchical with an auto-generated manager).

## In detail
CrewAI is an open-source multi-agent orchestration framework created by **João Moura**, Python-based and **built on LangChain** following a modular design principle. Its components: **agents** (an autonomous unit with a role, a goal and a profile/backstory); **tools** (CrewAI and LangChain ones, with error handling and caching); **tasks** (description, agent, expected output, optional asynchronous execution); **processes**; and **crews**. Three processes exist: **sequential** (tasks in order, one task's output serving as context for the next); **hierarchical** (CrewAI autonomously generates a manager agent that supervises, assigns tasks and evaluates outputs); and **consensual**, "planned" but **not currently implemented in the codebase**. CrewAI connects to any LLM (GPT-4 by default, IBM Granite, Ollama) and combines AutoGen's conversational flexibility with ChatDev's structured approach.

## Example
An `Agent(role='Customer support', goal='Handle customer requests and issues', backstory='You are a customer-support specialist for a restaurant…')` and a `data_science_agent` are brought together in `Crew(agents=[…], tasks=[…], process=Process.sequential)`. The `Task(description='Gather data from customer interactions, transaction history and tickets', expected_output='An organised dataset ready to be preprocessed', agent=data_science_agent)` has its output serve as context for the next task. A real case from Moura's crewAI-examples repo: stock analysis where agents with distinct roles collaborate to produce investment recommendations, configured on GPT-3.5 rather than the default GPT-4.

## Tradeoff / insight
Pure vocabulary (roles/tasks/process = team distribution). The point to remember: the hierarchical process relies on an auto-generated LLM manager — convenient but a non-deterministic orchestrator; and the consensual process exists only on paper.

## Primary source
See the CrewAI documentation and Moura's crewAI-examples repository.

## See also
- [langchain](langchain.md)
- [autogen-ag2](autogen-ag2.md)
