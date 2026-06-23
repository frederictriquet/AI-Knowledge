# Index thématique du corpus IA

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

169 fiches · niveau : 🔴 substance · 🟡 tradeoff · 🟢 survol

## Sommaire

- [🧱 Fondamentaux des agents](#fondamentaux-des-agents) — 14
- [🧠 Raisonnement & planification](#raisonnement--planification) — 22
- [✍️ Prompting](#prompting) — 22
- [🔧 Outils & function-calling](#outils--function-calling) — 11
- [📚 RAG & contexte](#rag--contexte) — 15
- [💾 Mémoire](#mémoire) — 5
- [👥 Multi-agents](#multi-agents) — 9
- [🔌 Protocoles & interopérabilité](#protocoles--interopérabilité) — 5
- [🛠️ Frameworks & outillage](#frameworks--outillage) — 11
- [📊 Évaluation](#évaluation) — 14
- [🏁 Benchmarks](#benchmarks) — 2
- [🔐 Sécurité](#sécurité) — 21
- [⚡ Efficacité & coût](#efficacité--coût) — 5
- [⚖️ Gouvernance, alignement & ops](#gouvernance-alignement--ops) — 13


## 🧱 Fondamentaux des agents

- 🔴 **[ACI : concevoir l'interface agent-ordinateur](fiches/aci-agent-computer-interface.md)** → [source](https://www.anthropic.com/engineering/building-effective-agents)
- 🔴 **[Les 5 patterns de workflow composables (Anthropic)](fiches/patterns-de-workflow.md)** → [source](https://www.anthropic.com/engineering/building-effective-agents)
- 🔴 **[Modèles de langage augmentés (taxonomie de Weng)](fiches/augmented-language-models.md)** → [source](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)
- 🔴 **[Taxonomie des erreurs d'appel de fonction](fiches/taxonomie-erreurs-appel-fonction.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-evaluation)
- 🔴 **[Workflows vs agents : la distinction architecturale d'Anthropic](fiches/workflows-vs-agents.md)** → [source](https://www.anthropic.com/engineering/building-effective-agents)
- 🟡 **[Architecture BDI (Belief-Desire-Intention)](fiches/bdi.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agentic-architecture)
- 🟡 **[Architectures verticale / horizontale / hybride](fiches/archi-vertical-horizontal-hybride.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agentic-architecture)  ·  papier : arXiv:2404.11584
- 🟡 **[Deep Agents (pattern)](fiches/deep-agents.md)** → [source](https://blog.langchain.com/deep-agents/)
- 🟡 **[Limites structurelles des agents LLM (selon Weng)](fiches/agent-limites-weng.md)** → [source](https://lilianweng.github.io/posts/2023-06-23-agent/)
- 🟢 **[Agent apprenant (modèle AIMA)](fiches/agent-apprenant.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-learning)
- 🟢 **[AutoGPT](fiches/autogpt.md)** → [source](https://www.ibm.com/fr-fr/think/topics/autogpt)
- 🟢 **[BabyAGI](fiches/babyagi.md)** → [source](https://www.ibm.com/fr-fr/think/topics/babyagi)
- 🟢 **[Logique conditionnelle & heuristique](fiches/logique-conditionnelle-heuristique.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agentic-reasoning)
- 🟢 **[Taxonomie des 5 types d'agents](fiches/taxonomie-5-types-agents.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-types)

## 🧠 Raisonnement & planification

- 🔴 **[Auto-réflexion des agents (ReAct, Reflexion, CoH, AD)](fiches/self-reflection-agents.md)** → [source](https://lilianweng.github.io/posts/2023-06-23-agent/)
- 🔴 **[DeepSeek-R1 : le RL fait émerger le raisonnement](fiches/deepseek-r1-rl-raisonnement.md)** → [source](https://arxiv.org/abs/2501.12948)
- 🔴 **[Graph of Thoughts (GoT)](fiches/graph-of-thoughts.md)** → [source](https://arxiv.org/abs/2308.09687)
- 🔴 **[LATS (Language Agent Tree Search)](fiches/lats.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agentic-reasoning)
- 🔴 **[Modèles de raisonnement & test-time compute](fiches/inference-time-scaling.md)** → [source](https://arxiv.org/abs/2501.12948)
- 🔴 **[Process Reward Models (Let's Verify Step by Step)](fiches/process-reward-models.md)** → [source](https://arxiv.org/abs/2305.20050)
- 🔴 **[Test-time compute : « penser » comme du calcul à l'inférence](fiches/test-time-compute-thinking.md)** → [source](https://lilianweng.github.io/posts/2025-05-01-thinking/)
- 🔴 **[Tree of Thoughts (ToT)](fiches/tree-of-thoughts.md)** → [source](https://www.ibm.com/fr-fr/think/topics/tree-of-thoughts)  ·  papier : arXiv:2305.10601
- 🔴 **[Vérification de source (anti-contamination contexte)](fiches/verification-de-source.md)** → [source](https://www.ibm.com/fr-fr/think/tutorials/build-corrective-rag-agent-granite-tavily)
- 🟡 **[Autoréflexion / Reflexion](fiches/reflexion.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agentic-reasoning)
- 🟡 **[Chain-of-Verification (CoVe)](fiches/chain-of-verification.md)** → [source](https://arxiv.org/abs/2309.11495)
- 🟡 **[Least-to-Most prompting](fiches/least-to-most.md)** → [source](https://arxiv.org/abs/2205.10625)
- 🟡 **[Planification probabiliste](fiches/planification-probabiliste.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-planning)
- 🟡 **[Raisonnement par cas (case-based reasoning)](fiches/case-based-reasoning.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-memory)
- 🟡 **[ReWOO](fiches/rewoo.md)** → [source](https://www.ibm.com/fr-fr/think/topics/rewoo)
- 🟡 **[Self-Consistency](fiches/self-consistency.md)** → [source](https://www.ibm.com/fr-fr/think/topics/prompt-engineering-techniques)
- 🟡 **[Self-Refine](fiches/self-refine.md)** → [source](https://arxiv.org/abs/2303.17651)
- 🟡 **[Step-Back prompting](fiches/step-back.md)** → [source](https://arxiv.org/abs/2310.06117)
- 🟢 **[Architectures réactive / délibérative / cognitive](fiches/archi-reactif-deliberatif-cognitif.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agentic-architecture)  ·  papier : arXiv:2404.11584
- 🟢 **[Chain-of-Thought (CoT)](fiches/chain-of-thought.md)** → [source](https://www.ibm.com/fr-fr/think/topics/chain-of-thoughts)
- 🟢 **[Planification : objectif / état / séquençage](fiches/planification-goal-state-action.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-planning)
- 🟢 **[ReAct](fiches/react.md)** → [source](https://www.ibm.com/fr-fr/think/topics/react-agent)  ·  papier : Yao et al., ReAct: Synergizing Reasoning and Acting in Language Models (arXiv:2210.03629)

## ✍️ Prompting

- 🔴 **[Directional Stimulus Prompting (DSP)](fiches/directional-stimulus-prompting.md)** → [source](https://www.ibm.com/fr-fr/think/topics/directional-stimulus-prompting)
- 🔴 **[ICL : sélection d'exemples & techniques zero-shot](fiches/icl-exemplar-et-zero-shot.md)** → [source](https://arxiv.org/abs/2406.06608)
- 🔴 **[In-context learning (ICL)](fiches/in-context-learning.md)** → [source](https://www.ibm.com/fr-fr/think/topics/in-context-learning)
- 🔴 **[Integrated prompt environments — donner les prompts aux experts métier](fiches/integrated-prompt-environments.md)** → [source](https://hamel.dev/blog/posts/field-guide/)
- 🔴 **[Le prompt engineering est empirique (étude de cas)](fiches/prompt-engineering-est-empirique.md)** → [source](https://arxiv.org/abs/2406.06608)
- 🔴 **[Prompt tuning (soft prompts)](fiches/prompt-tuning.md)** → [source](https://www.ibm.com/fr-fr/think/topics/prompt-tuning)
- 🔴 **[Techniques d'auto-critique](fiches/self-criticism-techniques.md)** → [source](https://arxiv.org/abs/2406.06608)
- 🔴 **[Techniques d'ensembling](fiches/ensembling-techniques.md)** → [source](https://arxiv.org/abs/2406.06608)
- 🔴 **[Techniques de décomposition](fiches/decomposition-techniques.md)** → [source](https://arxiv.org/abs/2406.06608)
- 🟡 **[Automatic Prompt Engineer (APE) & design automatique de prompts](fiches/automatic-prompt-engineer-ape.md)** → [source](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)
- 🟡 **[Décomposition anticipée vs au fil de l'eau](fiches/decomposition-first-vs-interleaved.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-planning)
- 🟡 **[Méta-prompting](fiches/meta-prompting.md)** → [source](https://www.ibm.com/fr-fr/think/topics/meta-prompting)
- 🟡 **[Optimisation des prompts](fiches/prompt-optimization.md)** → [source](https://www.ibm.com/fr-fr/think/topics/prompt-optimization)
- 🟡 **[Prompt caching](fiches/prompt-caching.md)** → [source](https://www.ibm.com/fr-fr/think/tutorials/implement-prompt-caching-langchain)
- 🟡 **[Prompt chaining](fiches/prompt-chaining.md)** → [source](https://www.ibm.com/fr-fr/think/topics/prompt-chaining)
- 🟡 **[Taxonomie des techniques de prompting (The Prompt Report)](fiches/taxonomie-techniques.md)** → [source](https://arxiv.org/abs/2406.06608)
- 🟢 **[Catalogue des techniques de prompting](fiches/techniques-catalogue.md)** → [source](https://www.ibm.com/fr-fr/think/topics/prompt-engineering-techniques)
- 🟢 **[Few-shot prompting](fiches/few-shot-prompting.md)** → [source](https://www.ibm.com/fr-fr/think/topics/few-shot-prompting)
- 🟢 **[One-shot prompting](fiches/one-shot-prompting.md)** → [source](https://www.ibm.com/fr-fr/think/topics/one-shot-prompting)
- 🟢 **[Qu'est-ce que le prompt engineering](fiches/prompt-engineering.md)** → [source](https://www.ibm.com/fr-fr/think/topics/prompt-engineering)
- 🟢 **[Role prompting (persona)](fiches/role-prompting.md)** → [source](https://www.ibm.com/fr-fr/think/tutorials/using-role-prompting-with-watsonx-and-granite)
- 🟢 **[Zero-shot prompting](fiches/zero-shot-prompting.md)** → [source](https://www.ibm.com/fr-fr/think/topics/zero-shot-prompting)

## 🔧 Outils & function-calling

- 🔴 **[CodeAct (le code comme espace d'action)](fiches/codeact.md)** → [source](https://arxiv.org/abs/2402.01030)  ·  papier : PAL: Program-aided Language Models, Gao et al. (arXiv:2211.10435)
- 🔴 **[Computer-use & agents GUI](fiches/computer-use-gui-agents.md)** → [source](https://arxiv.org/abs/2307.13854)
- 🔴 **[Le cadre canonique : Agent = LLM + Planification + Mémoire + Outils](fiches/agent-architecture-canonique.md)** → [source](https://lilianweng.github.io/posts/2023-06-23-agent/)
- 🔴 **[Toolformer](fiches/toolformer.md)** → [source](https://arxiv.org/abs/2302.04761)
- 🔴 **[Voyager & bibliothèque de compétences](fiches/voyager-skill-library.md)** → [source](https://arxiv.org/abs/2305.16291)
- 🟡 **[LLM Compiler (parallel function calling)](fiches/llm-compiler.md)** → [source](https://arxiv.org/abs/2312.04511)
- 🟡 **[LLM imbriqué dans un outil](fiches/llm-dans-un-outil.md)** → [source](https://www.ibm.com/fr-fr/think/tutorials/local-tool-calling-ollama-granite)
- 🟡 **[MRKL Systems](fiches/mrkl.md)** → [source](https://arxiv.org/abs/2205.00445)
- 🟡 **[ReAct vs function calling](fiches/react-vs-function-calling.md)** → [source](https://www.ibm.com/fr-fr/think/topics/react-agent)
- 🟡 **[Tool grounding](fiches/tool-grounding.md)** → [source](https://www.ibm.com/fr-fr/think/tutorials/use-lm-studio-to-build-automatic-tool-calling-granite)
- 🟢 **[Tool calling / function calling](fiches/tool-calling.md)** → [source](https://www.ibm.com/fr-fr/think/topics/tool-calling)

## 📚 RAG & contexte

- 🔴 **[Améliorer son RAG systématiquement](fiches/ameliorer-rag-systematiquement.md)** → [source](https://jxnl.co/writing/2024/05/22/systematically-improving-your-rag/)
- 🔴 **[GraphRAG](fiches/graphrag.md)** → [source](https://arxiv.org/abs/2404.16130)
- 🔴 **[Mémoire vectorielle : MIPS & ANN](fiches/memoire-vectorielle-mips-ann.md)** → [source](https://lilianweng.github.io/posts/2023-06-23-agent/)
- 🔴 **[Self-RAG](fiches/self-rag.md)** → [source](https://arxiv.org/abs/2310.11511)
- 🟡 **[Agentic chunking](fiches/agentic-chunking.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agentic-chunking)
- 🟡 **[Corrective RAG (cRAG)](fiches/corrective-rag.md)** → [source](https://www.ibm.com/fr-fr/think/tutorials/build-corrective-rag-agent-granite-tavily)
- 🟡 **[HyDE (Hypothetical Document Embeddings)](fiches/hyde.md)** → [source](https://arxiv.org/abs/2212.10496)
- 🟡 **[LLM Wiki : un wiki maintenu par le LLM plutôt que du RAG](fiches/llm-wiki-karpathy.md)** → [source](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- 🟡 **[RAG agentique](fiches/rag-agentique.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agentic-rag)
- 🟡 **[RAG vs fine-tuning vs prompt engineering](fiches/rag-vs-fine-tuning-vs-prompt-engineering.md)** → [source](https://www.ibm.com/fr-fr/think/topics/rag-vs-fine-tuning-vs-prompt-engineering)
- 🟡 **[RAPTOR](fiches/raptor.md)** → [source](https://arxiv.org/abs/2401.18059)
- 🟡 **[Reranking (cross-encoders)](fiches/reranking.md)** → [source](https://arxiv.org/abs/1901.04085)
- 🟡 **[Sous-types de RAG agentique](fiches/sous-types-rag-agentique.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agentic-rag)
- 🟢 **[Des rapports plutôt que du RAG (RAG comme feature, pas comme bénéfice)](fiches/rapports-plutot-que-rag.md)** → [source](https://jxnl.co/writing/2024/06/05/predictions-for-the-future-of-rag/)
- 🟢 **[Stratégies de chunking](fiches/strategies-de-chunking.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agentic-chunking)

## 💾 Mémoire

- 🔴 **[Generative Agents — memory stream](fiches/generative-agents-memory-stream.md)** → [source](https://arxiv.org/abs/2304.03442)
- 🔴 **[MemGPT (Letta)](fiches/memgpt.md)** → [source](https://arxiv.org/abs/2310.08560)
- 🟡 **[Mémoire à base d'entités / graphe](fiches/entity-memory.md)** → ⚠️ _source manquante_
- 🟡 **[Mémoire épisodique / sémantique / procédurale](fiches/memoire-episodique-semantique-procedurale.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-memory)
- 🟢 **[Mémoire court terme vs long terme](fiches/memoire-court-long-terme.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-memory)

## 👥 Multi-agents

- 🔴 **[DroidSpeak](fiches/droidspeak.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-communication)
- 🔴 **[MacNet : passage à l'échelle multi-agents](fiches/macnet.md)** → [source](https://www.ibm.com/fr-fr/think/topics/chatdev)
- 🔴 **[MetaGPT : communication structurée + feedback exécutable](fiches/metagpt-pattern.md)** → [source](https://www.ibm.com/fr-fr/think/topics/metagpt)  ·  papier : arXiv:2308.00352
- 🔴 **[Mixture-of-Agents (MoA)](fiches/mixture-of-agents.md)** → [source](https://arxiv.org/abs/2406.04692)
- 🔴 **[Multi-agent debate / Society of Mind](fiches/society-of-mind-debate.md)** → [source](https://arxiv.org/abs/2305.14325)
- 🟡 **[Réseaux centralisés vs décentralisés](fiches/reseaux-centralises-decentralises.md)** → [source](https://www.ibm.com/fr-fr/think/topics/multiagent-system)
- 🟡 **[Stratégies de collaboration : règles / rôles / modèles](fiches/strategies-collaboration.md)** → [source](https://www.ibm.com/fr-fr/think/topics/multi-agent-collaboration)
- 🟡 **[Structures multi-agents : hiérarchique / holonique / coalition / équipe](fiches/structures-multi-agents.md)** → [source](https://www.ibm.com/fr-fr/think/topics/multiagent-system)
- 🟡 **[Types d'orchestration des agents IA](fiches/orchestration-types.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-orchestration)

## 🔌 Protocoles & interopérabilité

- 🔴 **[MCP (Model Context Protocol)](fiches/mcp.md)** → [source](https://www.ibm.com/fr-fr/think/topics/model-context-protocol)
- 🟡 **[A2A (Agent2Agent)](fiches/a2a.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agent2agent-protocol)
- 🟡 **[ACP (Agent Communication Protocol)](fiches/acp.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agent-communication-protocol)
- 🟡 **[Autres protocoles : ANP / AG-UI / Agora / LMOS](fiches/autres-protocoles.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-protocols)
- 🟡 **[KQML & FIPA-ACL](fiches/kqml-fipa-acl.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-communication)

## 🛠️ Frameworks & outillage

- 🟡 **[Comportements d'essaim (flocking / swarming)](fiches/flocking-swarming.md)** → [source](https://www.ibm.com/fr-fr/think/topics/multiagent-system)
- 🟡 **[RAISE](fiches/raise.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-planning)
- 🟢 **[AutoGen & AG2](fiches/autogen-ag2.md)** → [source](https://www.ibm.com/fr-fr/think/topics/autogen)
- 🟢 **[BeeAI](fiches/beeai.md)** → [source](https://www.ibm.com/fr-fr/think/topics/beeai)
- 🟢 **[CrewAI](fiches/crewai.md)** → [source](https://www.ibm.com/fr-fr/think/topics/crew-ai)
- 🟢 **[LangChain](fiches/langchain.md)** → [source](https://www.ibm.com/fr-fr/think/topics/langchain)
- 🟢 **[LangFlow](fiches/langflow.md)** → [source](https://www.ibm.com/fr-fr/think/topics/langflow)
- 🟢 **[LangGraph](fiches/langgraph.md)** → [source](https://www.ibm.com/fr-fr/think/topics/langgraph)
- 🟢 **[LlamaIndex](fiches/llamaindex.md)** → [source](https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks)
- 🟢 **[OpenAI Swarm](fiches/openai-swarm.md)** → [source](https://www.ibm.com/fr-fr/think/topics/multi-agent-collaboration)
- 🟢 **[Semantic Kernel](fiches/semantic-kernel.md)** → [source](https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks)

## 📊 Évaluation

- 🔴 **[Data flywheel : collecte de feedback](fiches/data-flywheel-feedback.md)** → [source](https://eugeneyan.com/writing/llm-patterns/)
- 🔴 **[Error analysis : regarde tes données](fiches/error-analysis.md)** → [source](https://hamel.dev/blog/posts/field-guide/)
- 🔴 **[Eval-driven development](fiches/eval-driven-development.md)** → [source](https://hamel.dev/blog/posts/evals/)
- 🔴 **[LLM-as-a-judge : le faire correctement](fiches/llm-as-judge-correct.md)** → [source](https://hamel.dev/blog/posts/llm-judge/)
- 🔴 **[Patterns pour systèmes LLM en production](fiches/patterns-systemes-llm.md)** → [source](https://eugeneyan.com/writing/llm-patterns/)
- 🔴 **[Revue de code agentique : de l'écriture à la vérification](fiches/revue-de-code-agentique.md)** → [source](https://addyosmani.com/blog/agentic-code-review/)
- 🔴 **[Évaluation de trajectoire](fiches/evaluation-trajectoire.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-evaluation)
- 🔴 **[Évaluer les LLM (évals spécifiques à la tâche)](fiches/evaluer-les-llm.md)** → [source](https://eugeneyan.com/writing/evals/)
- 🟡 **[Contextual Retrieval](fiches/contextual-retrieval.md)** → [source](https://www.anthropic.com/news/contextual-retrieval)
- 🟡 **[LLM-as-a-judge](fiches/llm-as-a-judge.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-evaluation)
- 🟡 **[LLM-evaluators (juges LLM) — vue d'Eugene](fiches/llm-evaluators.md)** → [source](https://eugeneyan.com/writing/llm-evaluators/)
- 🟡 **[Reviewers hétérogènes : faible recouvrement entre outils](fiches/reviewers-heterogenes.md)** → [source](https://addyosmani.com/blog/agentic-code-review/)
- 🟡 **[Tool retrieval (RAG sur les outils)](fiches/tool-retrieval.md)** → [source](https://arxiv.org/abs/2305.15334)
- 🟢 **[RAG (Retrieval-Augmented Generation)](fiches/rag.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agentic-rag)

## 🏁 Benchmarks

- 🟡 **[Benchmarks d'agents & de LLM (référence)](fiches/benchmarks-agents.md)** → [source](https://arxiv.org/abs/2310.06770)
- 🟡 **[Pourquoi les benchmarks d'agents comptent 🔴](fiches/pourquoi-les-benchmarks-comptent.md)** → ⚠️ _source manquante_

## 🔐 Sécurité

- 🔴 **[ASCII Smuggling : cacher des instructions via les Unicode Tags](fiches/unicode-tags-smuggling.md)** → [source](https://embracethered.com/blog/posts/2024/hiding-and-finding-text-with-unicode-tags/)
- 🔴 **[Attaques adversariales sur les LLM (taxonomie de Weng)](fiches/attaques-adversariales-llm.md)** → [source](https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/)
- 🔴 **[ChatDev : ChatChain, CAMEL, déshallucination communicative](fiches/chatdev-chatchain.md)** → [source](https://www.ibm.com/fr-fr/think/topics/chatdev)
- 🔴 **[Dual-LLM pattern & CaMeL](fiches/dual-llm-camel.md)** → [source](https://arxiv.org/abs/2503.18813)
- 🔴 **[Injection de prompt](fiches/prompt-injection.md)** → [source](https://www.ibm.com/fr-fr/think/topics/prompt-injection)
- 🔴 **[Injection de prompt : pourquoi c'est grave (et pourquoi les défenses naïves échouent)](fiches/injection-pourquoi-cest-grave.md)** → [source](https://simonwillison.net/2023/Apr/14/worst-that-can-happen/)
- 🔴 **[Injections IA : prompt injection directe et indirecte](fiches/ai-injections-basics.md)** → [source](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/)
- 🔴 **[Jailbreak (débridage)](fiches/jailbreak.md)** → [source](https://www.ibm.com/fr-fr/think/insights/ai-jailbreak)
- 🔴 **[La « lethal trifecta »](fiches/lethal-trifecta.md)** → [source](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- 🔴 **[Le Dual LLM pattern](fiches/dual-llm-pattern.md)** → [source](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/)
- 🔴 **[MITRE ATLAS](fiches/mitre-atlas.md)** → [source](https://atlas.mitre.org/)
- 🔴 **[Microsoft 365 Copilot : de l'injection à l'exfiltration d'e-mails](fiches/m365-copilot-exfil.md)** → [source](https://embracethered.com/blog/posts/2024/m365-copilot-prompt-injection-tool-invocation-and-data-exfil-using-ascii-smuggling/)
- 🔴 **[NIST AI 100-2 : taxonomie de l'adversarial ML](fiches/nist-ai-100-2.md)** → [source](https://csrc.nist.gov/pubs/ai/100/2/e2025/final)
- 🔴 **[OWASP Top 10 for LLM Applications](fiches/owasp-llm-top-10.md)** → [source](https://genai.owasp.org/llm-top-10/)
- 🔴 **[Prévenir l'injection de prompt](fiches/prevent-prompt-injection.md)** → [source](https://www.ibm.com/fr-fr/think/insights/prevent-prompt-injection)
- 🔴 **[Skeleton Key & jailbreaks multi-tours](fiches/skeleton-key.md)** → [source](https://www.ibm.com/fr-fr/think/insights/llm-skeleton-key)
- 🔴 **[Sécurité agentique](fiches/securite-agentique.md)** → [source](https://www.ibm.com/fr-fr/think/topics/ai-agent-security)
- 🔴 **[Taxonomie du « prompt hacking »](fiches/prompt-hacking-taxonomie.md)** → [source](https://arxiv.org/abs/2406.06608)
- 🟡 **[Garde-fou en nœud d'entrée (Granite Guardian)](fiches/guardrail-noeud-entree.md)** → [source](https://www.ibm.com/fr-fr/think/tutorials/build-sql-agent-langgraph-mistral-medium-3-watsonx-ai)
- 🟡 **[OWASP Top 10 LLM & menaces agentiques](fiches/owasp-llm-agentic.md)** → [source](https://genai.owasp.org/llm-top-10/)
- 🟡 **[Spotlighting](fiches/spotlighting.md)** → [source](https://arxiv.org/abs/2403.14720)

## ⚡ Efficacité & coût

- 🟡 **[Décodage contraint / sortie structurée](fiches/constrained-decoding.md)** → [source](https://arxiv.org/abs/2307.09702)
- 🟡 **[Mise en cache sémantique](fiches/semantic-caching.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agentic-rag)
- 🟡 **[Routage & cascades de modèles](fiches/model-routing-cascades.md)** → [source](https://arxiv.org/abs/2305.05176)
- 🟡 **[Sorties structurées (instructor / Pydantic)](fiches/sorties-structurees-instructor.md)** → [source](https://python.useinstructor.com/)
- 🟡 **[Speculative decoding](fiches/speculative-decoding.md)** → [source](https://arxiv.org/abs/2211.17192)

## ⚖️ Gouvernance, alignement & ops

- 🔴 **[AgentOps](fiches/agentops.md)** → [source](https://www.ibm.com/fr-fr/think/topics/agentops)
- 🔴 **[Constitutional AI & RLAIF](fiches/constitutional-ai-rlaif.md)** → [source](https://arxiv.org/abs/2212.08073)
- 🔴 **[DSPy](fiches/dspy.md)** → [source](https://www.ibm.com/fr-fr/think/topics/dspy)
- 🔴 **[DSPy : compilation & bootstrapping](fiches/dspy-compilation-bootstrap.md)** → [source](https://arxiv.org/abs/2310.03714)
- 🔴 **[DSPy : signatures, modules, optimiseurs](fiches/dspy-signatures-modules-optimiseurs.md)** → [source](https://arxiv.org/abs/2310.03714)
- 🔴 **[Loop engineering : concevoir le système qui prompte l'agent](fiches/loop-engineering.md)** → [source](https://addyosmani.com/blog/loop-engineering/)
- 🔴 **[Observabilité LLM : best practices (indépendantes de l'outil)](fiches/observabilite-llm-best-practices.md)** → [source](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- 🔴 **[Résilience & fallback LLM](fiches/resilience-fallback-llm.md)** → [source](https://github.com/Portkey-AI/gateway)
- 🔴 **[UX défensive (Defensive UX) pour produits LLM](fiches/ux-defensive-llm.md)** → [source](https://eugeneyan.com/writing/llm-patterns/)
- 🔴 **[Éthique & gouvernance des agents](fiches/ethique-gouvernance.md)** → [source](https://www.ibm.com/fr-fr/think/insights/ai-agent-ethics)
- 🟡 **[Dette de compréhension & cognitive surrender](fiches/dette-de-comprehension.md)** → [source](https://addyosmani.com/blog/loop-engineering/)
- 🟡 **[Hooks déterministes vs mémoire probabiliste (Skills / Memory / Hooks)](fiches/hooks-deterministes-vs-memoire-probabiliste.md)** → [source](https://code.claude.com/docs/en/memory)
- 🟡 **[Human-in-the-loop : interruptions statiques vs dynamiques](fiches/hitl-statique-dynamique.md)** → [source](https://www.ibm.com/fr-fr/think/tutorials/human-in-the-loop-ai-agent-langraph-watsonx-ai)
