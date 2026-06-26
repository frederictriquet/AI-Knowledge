---
type: index
titre: "Thème — Mémoire"
theme: memoire
---

# 💾 Mémoire

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Mémoire court/long terme et persistance entre sessions._

## Concepts (5)

### 🔴 Substance / cœur
- **[Generative Agents — memory stream](../fiches/generative-agents-memory-stream.md)** — un journal horodaté d'observations, relu par un score combinant **récence + importance + pertinence** ; la fonction de scoring est l'idée transférable pour une mémoire d'agent.
- **[MemGPT (Letta)](../fiches/memgpt.md)** — gérer la mémoire d'un LLM comme un système d'exploitation : pagination entre un contexte « RAM » limité et un stockage externe « disque », le modèle décidant lui-même quoi charger.

### 🟡 Tradeoff / intermédiaire
- **[Mémoire à base d'entités / graphe](../fiches/entity-memory.md)** — structurer la mémoire long-terme comme un **graphe d'entités et de relations** (qui / quoi / lien) plutôt qu'un simple store vectoriel.
- **[Mémoire épisodique / sémantique / procédurale](../fiches/memoire-episodique-semantique-procedurale.md)** — trois sous-types de mémoire long terme calqués sur la psychologie : traces d'événements vécus (épisodique), faits structurés (sémantique), savoir-faire automatisé (procédural).

### 🟢 Survol / introductif
- **[Mémoire court terme vs long terme](../fiches/memoire-court-long-terme.md)** — la mémoire court terme est la fenêtre de contexte/buffer de la session courante ; la long terme est un store externe persistant relu à la demande.

## Outils (10)

- **[Cavemem](../fiches%20outils/cavemem.md)** — _Serveur MCP / CLI (+ hooks IDE)_
- **[Chroma (ChromaDB)](../fiches%20outils/chroma.md)** — _Base de données vectorielle (bibliothèque + serveur + Cloud SaaS)_
- **[GraphMind](../fiches%20outils/graphmind.md)** — _Application desktop / Serveur MCP / CLI_
- **[LanceDB](../fiches%20outils/lancedb.md)** — _Base vectorielle embarquée open-source (Apache 2.0) + cloud/Enterprise_
- **[Milvus](../fiches%20outils/milvus.md)** — _Base vectorielle open-source (Apache 2.0) distribuée + cloud managé (Zilliz)_
- **[pgvector](../fiches%20outils/pgvector.md)** — _Extension PostgreSQL open-source (recherche vectorielle)_
- **[Pinecone](../fiches%20outils/pinecone.md)** — _Service web (base vectorielle managée, propriétaire)_
- **[Qdrant](../fiches%20outils/qdrant.md)** — _Base vectorielle open-source (Apache 2.0, Rust) self-host + cloud managé_
- **[turbopuffer](../fiches%20outils/turbopuffer.md)** — _Service web (recherche vectorielle + full-text serverless, propriétaire)_
- **[Weaviate](../fiches%20outils/weaviate.md)** — _Base vectorielle open-source (BSD-3, Go) self-host + cloud managé_
