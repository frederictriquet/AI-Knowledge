---
outil: "OpenAI Agents SDK"
titre: "OpenAI Agents SDK"
themes: [multi-agents, frameworks-outillage]
type: "SDK Python + TypeScript (agents légers)"
url: https://openai.github.io/openai-agents-python/
modele_economique: "Open-source (MIT) — gratuit"
cout_llm: "🔑 BYOK — gratuit ; tu paies l'API du modèle utilisé"
objectifs: [mise-en-prod]
famille: "Frameworks multi-agents généralistes (pour développeurs)"
eco_icones: "🔓"
cout_icones: "🔑"
resume: "**Minimaliste** (MIT) : Agents, Handoffs, Guardrails, Sessions + tracing gratuit. Successeur en production de **Swarm**. Provider-agnostic (100+ LLM via LiteLLM). Pré-1.0. Bon point d'entrée léger"
---

# OpenAI Agents SDK

**En une phrase** — Framework d'agents **minimaliste** d'OpenAI (peu d'abstractions : Agents, Handoffs, Guardrails, Sessions + tracing intégré), **successeur en production** de l'expérimentation Swarm — et, malgré son nom, **provider-agnostic** (100+ modèles).

> 📄 Concept lié : [Swarm](../fiches/openai-swarm.md), le prédécesseur expérimental déprécié.

## Type & intégration
**SDK Python** (≥ 3.10, `openai-agents`) **et TypeScript/JS** (`@openai/agents`). Encore **pré-1.0** (Python v0.17.x, API susceptible d'évoluer). Primitives : **Agents** (LLM + instructions + outils), **Handoffs** (délégation entre agents / agents-as-tools), **Guardrails** (validation I/O), **Sessions** (mémoire/contexte), + human-in-the-loop et realtime.

## Modèle économique
**Open-source MIT**, gratuit. **Provider-agnostic** confirmé verbatim : supporte les APIs OpenAI Responses & Chat Completions **+ 100+ autres LLM** via l'extension **LiteLLM** (`openai-agents[litellm]`, marquée « beta/best-effort »).

## Coût LLM
**🔑 BYOK** : le SDK est gratuit ; tu paies l'API du modèle utilisé (OpenAI ou autre). **Tracing OpenAI gratuit** et activé par défaut — astuce documentée : une clé OpenAI permet le tracing gratuit dans le dashboard OpenAI **même avec des modèles non-OpenAI**. Désactivable (`OPENAI_AGENTS_DISABLE_TRACING=1`).

## À quoi ça sert
Le choix « **léger et lisible** » quand on veut composer quelques agents sans la machinerie d'un gros framework. Tracing intégré pour debug/éval. Bon point d'entrée, surtout si l'on est déjà dans l'écosystème OpenAI.

## Notes / à creuser
- **Lock-in léger** : le tracing par défaut pousse vers le dashboard OpenAI (désactivable ; intégrations tierces — Langfuse, AgentOps…).
- Pré-1.0 : API mouvante ; multi-modèle via LiteLLM en beta.
- Vs [LangGraph](langgraph.md) (graphe/état, plus de contrôle) et [AutoGen/AG2](autogen-ag2.md)/[CrewAI](crewai.md) : positionnement « minimaliste » (appréciation tierce, pas de comparatif officiel OpenAI).

## Source
https://openai.github.io/openai-agents-python/ (+ /tracing, /models) · github.com/openai/openai-agents-python (LICENSE MIT) · github.com/openai/swarm (déprécié → Agents SDK). *(vérifié le 2026-06-16)*
