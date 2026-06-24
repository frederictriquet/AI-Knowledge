---
outil: "Pydantic AI"
titre: "Pydantic AI"
themes: [frameworks-outillage]
type: "Framework d'agents Python type-safe"
url: https://ai.pydantic.dev/
modele_economique: "Open-source (MIT) + Pydantic Logfire (observabilité, freemium)"
cout_llm: "🔑 BYOK, model-agnostic — ne facture pas les tokens"
---

# Pydantic AI

**En une phrase** — Framework d'agents Python **type-safe** par l'équipe Pydantic : sorties structurées validées, ergonomie « that FastAPI feeling » (erreurs déplacées du runtime vers l'écriture), injection de dépendances, observabilité native via Logfire.

## Type & intégration
Framework open-source Python, construit par les créateurs de **Pydantic** (la brique de validation utilisée par les SDK OpenAI/Anthropic/Google ADK, LangChain, LlamaIndex, CrewAI, Instructor…). Maturité confirmée : **> v1.0** (v1.107, juin 2026, ~17,8k★). Support **MCP**, interopérabilité **A2A**, exécution durable.

## Modèle économique
- **Framework : open-source MIT**, gratuit.
- **Pydantic Logfire** (observabilité OTel, optionnelle mais intégrée nativement) = l'offre commerciale **freemium** : **Personal** gratuit (10M spans, 30 j) → **Team** 49 $/mois (+2 $/M) → **Growth** 249 $/mois → **Enterprise** sur devis (self-host, SSO, SLA).

## Coût LLM
**🔑 BYOK et model-agnostic** : « supports virtually every model and provider » (OpenAI, Anthropic, Gemini, DeepSeek, Mistral, Cohere, Groq, Ollama, Bedrock, OpenRouter, LiteLLM…). Le framework MIT **ne facture aucun token** ; tu paies le fournisseur du modèle.

## À quoi ça sert
Le choix quand la **fiabilité des sorties** prime : validation Pydantic au runtime (structured outputs typés et streamés), DI type-safe pour customiser les agents, et suivi coût/perf via Logfire/OpenTelemetry. Crédibilité forte (Pydantic est déjà sous le capot de la plupart des SDK IA).

## Notes / à creuser
- Projet **récent mais monté très vite**, désormais mûr (>1.0).
- Positionnement (sources tierces) : vs [LangGraph](langgraph.md) (routing/état complexes, plus de boilerplate), vs [CrewAI](crewai.md) (multi-agents/rôles), vs [OpenAI Agents SDK](openai-agents-sdk.md) (léger) — Pydantic AI mise sur le **typage et la validation**.
- Souvent combiné avec d'autres frameworks plutôt qu'opposé.

## Source
https://ai.pydantic.dev/ · github.com/pydantic/pydantic-ai (LICENSE MIT, providers, v1.107) · https://pydantic.dev/pricing (Logfire). *(vérifié le 2026-06-16)*
