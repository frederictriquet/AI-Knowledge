---
type: index
titre: "Thème — RAG & contexte"
theme: rag-contexte
---

# 📚 RAG & contexte

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Augmenter le modèle par récupération et gérer le contexte._

## Concepts (15)

### 🔴 Substance / cœur
- **[Améliorer son RAG systématiquement](../fiches/ameliorer-rag-systematiquement.md)** — Traiter un système RAG comme un produit mesurable qu'on améliore par itérations guidées par des métriques, et non comme une recette figée.
- **[GraphRAG](../fiches/graphrag.md)** — construire un graphe de connaissances et des résumés de communautés à partir du corpus, pour répondre aux questions *globales* que le RAG vectoriel échoue à traiter.
- **[Mémoire vectorielle : MIPS & ANN](../fiches/memoire-vectorielle-mips-ann.md)** — la mémoire long terme d'un agent s'implémente comme une recherche par produit interne maximal (MIPS) dans un magasin vectoriel, accélérée par des algorithmes de plus proches voisins approchés (ANN).
- **[Self-RAG](../fiches/self-rag.md)** — un LLM entraîné à décider *quand* récupérer et à *auto-critiquer* la pertinence et le support factuel de ce qu'il récupère et génère, via des « tokens de réflexion ».

### 🟡 Tradeoff / intermédiaire
- **[Agentic chunking](../fiches/agentic-chunking.md)** — un LLM découpe le texte par unité de sens et étiquette chaque morceau de métadonnées, au lieu d'appliquer des coupes mécaniques à taille fixe.
- **[Corrective RAG (cRAG)](../fiches/corrective-rag.md)** — un grader LLM note les passages récupérés ; si mauvais → fallback recherche web (Tavily) + réécriture de requête, sinon refus explicite plutôt qu'hallucination.
- **[HyDE (Hypothetical Document Embeddings)](../fiches/hyde.md)** — générer une réponse *hypothétique* à la question, puis chercher les documents proches de cette réponse (et non de la question) pour améliorer la récupération zero-shot.
- **[LLM Wiki : un wiki maintenu par le LLM plutôt que du RAG](../fiches/llm-wiki-karpathy.md)** — Plutôt que de re-synthétiser depuis les sources brutes à chaque question (RAG classique), on fait maintenir au LLM un **wiki persistant** (markdown interconnecté) : une couche de connaissance *compilée* dont la valeur se cumule à chaque source ingérée.
- **[RAG agentique](../fiches/rag-agentique.md)** — un agent placé devant la récupération qui décide s'il faut chercher, où chercher, reformule et itère, au lieu d'un pipeline RAG réactif fixe.
- **[RAG vs fine-tuning vs prompt engineering](../fiches/rag-vs-fine-tuning-vs-prompt-engineering.md)** — comparatif des trois leviers d'optimisation d'un LLM sur quatre axes (approche, objectifs, ressources, applications), présentés comme complémentaires et souvent combinés.
- **[RAPTOR](../fiches/raptor.md)** — clustering et résumés *hiérarchiques* récursifs des chunks (un arbre), permettant de récupérer à différents niveaux d'abstraction.
- **[Reranking (cross-encoders)](../fiches/reranking.md)** — re-classer les top-k passages récupérés avec un cross-encoder (requête et passage passent *ensemble* dans le modèle) ; le levier qualité le plus rentable en pratique, au prix de la latence.
- **[Sous-types de RAG agentique](../fiches/sous-types-rag-agentique.md)** — quatre familles d'agents pour la RAG : routage, planification de requêtes, ReAct, et plan-and-execute.

### 🟢 Survol / introductif
- **[Des rapports plutôt que du RAG (RAG comme feature, pas comme bénéfice)](../fiches/rapports-plutot-que-rag.md)** — Liu prédit un glissement du RAG « question-réponse » vers la **génération de rapports**, parce que la valeur d'un rapport (aide à la décision) dépasse largement le temps gagné à trouver une réponse.
- **[Stratégies de chunking](../fiches/strategies-de-chunking.md)** — quatre familles de découpage, du plus mécanique (taille fixe) au plus coûteux (sémantique, agentique), à choisir selon la structure du document.

## Outils (21)

- **[Agent Booster](../fiches%20outils/agent-booster.md)** — _Serveur MCP / CLI_
- **[Ansvar Compliance MCP (suite)](../fiches%20outils/ansvar-compliance-mcp.md)** — _Suite de serveurs MCP (sources de données réglementaires / juridiques)_
- **[AWS Documentation MCP](../fiches%20outils/aws-documentation-mcp.md)** — _Serveur MCP local (doc AWS officielle)_
- **[Chroma (ChromaDB)](../fiches%20outils/chroma.md)** — _Base de données vectorielle (bibliothèque + serveur + Cloud SaaS)_
- **[CodeGraph](../fiches%20outils/codegraph.md)** — _Serveur MCP / CLI_
- **[Context7](../fiches%20outils/context7.md)** — _Serveur MCP (doc de librairies) — open-source + hébergé_
- **[Exa MCP](../fiches%20outils/exa-mcp.md)** — _Serveur MCP (recherche web / neuronale)_
- **[GitMCP](../fiches%20outils/gitmcp.md)** — _Serveur MCP distant (repo GitHub → MCP)_
- **[Graphify](../fiches%20outils/graphify.md)** — _Skill (assistants de codage IA / Claude Code)_
- **[GraphMind](../fiches%20outils/graphmind.md)** — _Application desktop / Serveur MCP / CLI_
- **[LanceDB](../fiches%20outils/lancedb.md)** — _Base vectorielle embarquée open-source (Apache 2.0) + cloud/Enterprise_
- **[LlamaIndex](../fiches%20outils/llamaindex.md)** — _Framework Python + TS (data/RAG + agents) + plateforme managée LlamaCloud/LlamaParse_
- **[Microsoft Learn MCP](../fiches%20outils/microsoft-learn-mcp.md)** — _Serveur MCP distant (doc Microsoft officielle)_
- **[Milvus](../fiches%20outils/milvus.md)** — _Base vectorielle open-source (Apache 2.0) distribuée + cloud managé (Zilliz)_
- **[pgvector](../fiches%20outils/pgvector.md)** — _Extension PostgreSQL open-source (recherche vectorielle)_
- **[Pinecone](../fiches%20outils/pinecone.md)** — _Service web (base vectorielle managée, propriétaire)_
- **[Polaris (polarismcp.com)](../fiches%20outils/polaris.md)** — _Serveur MCP / CLI_
- **[Qdrant](../fiches%20outils/qdrant.md)** — _Base vectorielle open-source (Apache 2.0, Rust) self-host + cloud managé_
- **[Ref (ref.tools)](../fiches%20outils/ref.md)** — _Serveur MCP (documentation technique à jour)_
- **[turbopuffer](../fiches%20outils/turbopuffer.md)** — _Service web (recherche vectorielle + full-text serverless, propriétaire)_
- **[Weaviate](../fiches%20outils/weaviate.md)** — _Base vectorielle open-source (BSD-3, Go) self-host + cloud managé_
