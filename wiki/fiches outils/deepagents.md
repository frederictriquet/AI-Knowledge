---
outil: "deepagents (Deep Agents)"
titre: "deepagents (Deep Agents)"
themes: [frameworks-outillage, fondamentaux-agents]
type: "Bibliothèque Python (+ JS/TS) — harness d'agents"
url: https://github.com/langchain-ai/deepagents
modele_economique: "Open-source (MIT), gratuit — par LangChain"
cout_llm: "BYOK (🔑) — model-agnostic : tout LLM à tool-calling (frontier API, open-weight, local) ; tu fournis le modèle/la clé"
objectifs: [mise-en-prod]
famille: "Frameworks multi-agents généralistes (pour développeurs)"
eco_icones: "🔓"
cout_icones: "🔑"
resume: "**Harness haut niveau « batteries-included »** (LangChain, MIT, ~25k★) bâti sur LangGraph/`create_agent` : agents **long-horizon** clés en main — outil de **planification**, **sous-agents** à contexte isolé, **système de fichiers virtuel**, gestion/résumé auto du contexte, mémoire cross-session, human-in-the-loop, skills. Model-agnostic (frontier/open-weight/local), BYOK"
---

# deepagents (Deep Agents)

**En une phrase** — « the batteries-included agent harness » : une bibliothèque qui te donne, clés en main, les briques d'un agent **long-horizon** (planification, sous-agents, système de fichiers, gestion de contexte) au-dessus de LangGraph.

## Type & intégration
**Bibliothèque Python** (`pip`, ~25k★, Python 99 %), avec une version **JS/TS** (`deepagentsjs`). Éditée par **LangChain**. Model-agnostic via les chat models LangChain. Briques fournies :
- **Outil de planification** (todo / décomposition),
- **Sous-agents** à **contexte isolé** (délégation de tâches),
- **Système de fichiers virtuel** (read/write/edit/search) + exécution shell sandboxée,
- **Gestion/résumé automatique du contexte**, **mémoire cross-session**,
- **Human-in-the-loop** (portes d'approbation), skills/outils custom.

## Position dans la pile LangChain (important)
> « **LangGraph** = le *runtime* graphe. **`create_agent`** de LangChain = un harness minimal au-dessus. **Deep Agents** = un harness **plus opinionated** au-dessus de `create_agent` — mêmes briques, mais avec filesystem, sous-agents, gestion de contexte et skills *intégrés*. »

Donc trois couches, à choisir selon le besoin :
- **deepagents** → tu veux le **harness complet** (planning + contexte + délégation) prêt à l'emploi.
- **`create_agent`** (LangChain) → harness **léger** sans le middleware groupé.
- **[LangGraph](langgraph.md)** → quand la **boucle d'agent elle-même** doit être custom (graphe sur mesure).

## Modèle économique
**Open-source, licence MIT**, gratuit. Pas d'offre propre : la monétisation LangChain est ailleurs (LangSmith / LangGraph Platform). Intégration naturelle avec **LangSmith** pour le tracing.

## Coût LLM
**BYOK 🔑** — deepagents n'embarque ni ne revend de LLM. Tu branches **n'importe quel modèle à tool-calling** : API frontier (OpenAI, Anthropic, Google), open-weight (Baseten, Fireworks…), ou **local** (Ollama, vLLM, llama.cpp). Le coût = celui de ton fournisseur/à ton usage. ⚠️ Comme tout harness « deep agent » (planning + sous-agents + gros system prompt + relectures de contexte), la **consommation de tokens peut être élevée** sur des tâches longues — c'est le prix de l'autonomie long-horizon.

## À quoi ça sert
Construire rapidement des agents autonomes **multi-étapes / long-horizon** (recherche approfondie, refactors, workflows métier) sans réécrire la plomberie planning/contexte/délégation. C'est l'implémentation « produit » du **pattern deep-agents** (planner + sub-agents + virtual FS + system prompt détaillé) popularisé par Claude Code / Deep Research.

## Notes / à creuser
- **Famille [frameworks multi-agents généralistes](../guides/mettre-de-l-ia-en-production.md#fam-frameworks-multi-agents-generalistes-pour-developpeurs)** : couche **haut niveau** complémentaire de [LangGraph](langgraph.md) (bas niveau) — même éditeur. À distinguer aussi de [CrewAI](crewai.md) (rôles/équipes), OpenAI Agents SDK (minimaliste). N'est **pas** un outil de codage clé en main (ne pas confondre avec les [orchestrateurs de codage](../guides/generer-du-code-avec-l-ia.md#fam-orchestrateurs-systemes-multi-agents-de-codage)).
- Le **pattern « deep agents »** lui-même (planning tool + sub-agents + virtual file system + detailed system prompt) a sa **fiche conceptuelle** : [`fiches/deep-agents.md`](../fiches/deep-agents.md) (architecture, indépendante de ce produit).
- Version JS/TS : `langchain-ai/deepagentsjs`. Doc : docs.langchain.com/deepagents.

## Source
- Dépôt : https://github.com/langchain-ai/deepagents (MIT, ~25k★, vérifié API GitHub le 2026-06-17) · JS/TS : https://github.com/langchain-ai/deepagentsjs · doc : https://docs.langchain.com/deepagents

*(vérifié le 2026-06-17 — API GitHub [licence MIT] + README)*
