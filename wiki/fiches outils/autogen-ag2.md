---
outil: "AutoGen / AG2"
titre: "AutoGen / AG2"
themes: [multi-agents, frameworks-outillage]
type: "Framework Python multi-agents conversationnels (deux lignées + un successeur)"
url: https://microsoft.github.io/autogen/
modele_economique: "Open-source (AutoGen MIT, AG2 Apache 2.0)"
cout_llm: "🔑 BYOK — orchestre, ne facture pas les tokens"
objectifs: [mise-en-prod]
famille: "Frameworks multi-agents généralistes (pour développeurs)"
eco_icones: "🔓"
cout_icones: "🔑"
resume: "Agents **conversationnels** (GroupChat). ⚠️ **3 lignées** : AutoGen (Microsoft, MIT, **maintenance mode**) → successeur **Microsoft Agent Framework** (GA avr. 2026) ; **AG2** (fork communautaire, Apache 2.0, actif). Choisir selon l'écosystème. Concept : [📄 notion](../fiches/autogen-ag2.md)"
---

# AutoGen / AG2

**En une phrase** — Framework Python d'agents **conversationnels** (des agents LLM qui dialoguent entre eux et avec l'humain via GroupChat) — mais le projet s'est **scindé en trois lignées** qu'il faut démêler avant de choisir.

> 📄 Concept détaillé : [fiche notion AutoGen/AG2](../fiches/autogen-ag2.md). Ici : l'état du projet, les licences et le coût (angle produit).

## ⚠️ Trois lignées à ne pas confondre (vérifié le 2026-06-16)
- **AutoGen (Microsoft)** — désormais en **maintenance mode** (plus de nouvelles fonctions ; dernière release python-v0.7.5, sept. 2025). PyPI : `autogen-agentchat`/`-core`/`-ext` + `pyautogen`.
- **Microsoft Agent Framework (MAF)** — le **successeur officiel** Microsoft (fusion Semantic Kernel + AutoGen), **GA le 3 avril 2026** (.NET + Python, MIT, support long terme). C'est la voie « production » Microsoft.
- **AG2** — le **fork communautaire** des créateurs originaux (Chi Wang, Qingyun Wu), **toujours actif** (v0.13.4, juin 2026, « vers la v1.0 »). PyPI : `ag2` (et l'alias `autogen`).

## Modèle économique
Tout est open-source : **AutoGen (Microsoft) = MIT** (code) ; **AG2 = Apache 2.0** (conserve l'historique MIT d'AutoGen). Pas d'offre commerciale self-service ; AG2 annonce une plateforme hébergée **AgentOS** en **liste d'attente** (prix/GA non publiés).

## Coût LLM
**🔑 BYOK** pour les deux : aucun ne bundle ni ne facture l'usage LLM. Config par variables d'env / `OAI_CONFIG_LIST` (OpenAI, Azure, Anthropic, Gemini, Mistral, Groq… + modèles locaux Ollama/LM Studio/LiteLLM).

## À quoi ça sert
Patterns hérités : agents conversationnels (`ConversableAgent`/`AssistantAgent`), `UserProxyAgent` (human-in-the-loop), et surtout **GroupChat** (plusieurs agents, un manager choisit qui parle). La réécriture **AutoGen v0.4** (janv. 2025) a introduit une architecture **événementielle/asynchrone** en 3 couches (`autogen-core` runtime acteurs + tracing OTel, `autogen-agentchat` haut niveau, `autogen-ext`), équipes RoundRobin/Selector/Magentic-One, et **AutoGen Studio** (low-code, prototypage uniquement).

## Notes / à creuser
- **Risque réel = fragmentation** : pour un nouveau projet Microsoft, viser **MAF** (pas AutoGen legacy) ; pour rester proche de l'esprit communautaire d'origine, **AG2**. La confusion des noms PyPI (`autogen` = AG2, `pyautogen` = Microsoft) est un piège.
- Étoiles GitHub : microsoft/autogen ~59k (base historique restée là), ag2ai/ag2 ~4–5k (peu d'étoiles ont suivi le fork).
- Vs [LangGraph](langgraph.md) (graphe/état) et [CrewAI](crewai.md) (rôles) : axe distinctif = **orchestration conversationnelle**.

## Source
github.com/microsoft/autogen (LICENSE-CODE MIT ; discussion maintenance mode) · github.com/ag2ai/ag2 (LICENSE Apache 2.0) · devblogs.microsoft.com (Microsoft Agent Framework 1.0 GA, 2026-04-03). *(vérifié le 2026-06-16 ; prix AG2 AgentOS non publiés)*
