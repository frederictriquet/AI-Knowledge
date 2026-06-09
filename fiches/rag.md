---
titre: "RAG (Retrieval-Augmented Generation)"
theme: evaluation
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/agentic-rag
source_titre: "Qu’est-ce que la RAG agentique ?"
---

# RAG (Retrieval-Augmented Generation)

**En une phrase** — au lieu de répondre depuis sa seule mémoire d'entraînement, le LLM **récupère des passages pertinents dans une base externe** et les injecte dans le contexte pour ancrer sa réponse sur des sources.

## L'idée
RAG corrige trois limites du LLM seul : connaissances **figées** à la date d'entraînement (→ info fraîche/privée), **hallucinations** (→ réponse ancrée sur des sources vérifiables), et **absence d'accès aux données métier** (→ interrogeables sans réentraîner). Le flux canonique :

```
Question → [Retrieval] passages pertinents → [Augmentation] injectés dans le prompt
→ [Generation] le LLM répond en s'appuyant dessus (+ citations)
```

La récupération repose le plus souvent sur une **recherche sémantique** : les documents sont découpés en *chunks*, encodés en **embeddings** stockés dans une base vectorielle ; la question est vectorisée à son tour et on récupère les chunks les plus proches (top-K).

## Les briques
| Brique | Rôle |
|---|---|
| **Chunking** | Découper les docs ([stratégies](strategies-de-chunking.md) : fixe, récursif, sémantique, [agentique](agentic-chunking.md)) |
| **Embeddings + base vectorielle** | Indexer pour la recherche par similarité |
| **Retriever** | Ramener les top-K passages (souvent + un [reranking](reranking.md)) |
| **Generation** | Le LLM compose la réponse à partir du contexte récupéré |

## Tradeoff / insight pour un senior
RAG « classique » est **statique** : une seule passe récupération → génération, sans initiative. La qualité dépend entièrement du retrieval — un mauvais chunking ou un top-K hors-sujet plombe la réponse, sans que le modèle puisse se rattraper. C'est précisément ce que lèvent les variantes : le [RAG agentique](rag-agentique.md) place un agent *devant* la récupération (décider de chercher, reformuler, itérer, router), et le [corrective RAG](corrective-rag.md) ajoute un *grader* qui rejette les passages faibles et bascule sur une recherche web. Le surcoût (tokens, latence) n'est justifié que face à plusieurs sources ou des requêtes complexes ; pour une source unique et des questions simples, le RAG statique suffit.

## RAG : fonctionnalité produit ≠ à monter soi-même
RAG est une **architecture d'orchestration, jamais une capacité du modèle** — d'où une confusion fréquente selon le point de vue où l'on se place :

| Couche | RAG ? |
|---|---|
| Le **modèle** (Claude, GPT) via l'API brute | ❌ aucun RAG par défaut — à **toi** de monter le pipeline (chunking, embeddings, base vectorielle, retriever) |
| Le **produit** (Claude.ai, ChatGPT, Projects, recherche web) | ✅ le RAG est **déjà câblé par l'app** ; l'utilisateur final n'a rien à monter ni à prompter |

Autrement dit : sur Claude.ai tu *bénéficies* du RAG sans le savoir (l'app récupère et injecte les passages avant d'appeler le modèle) ; sur l'API tu pars d'une page blanche. Le modèle, lui, ne fait jamais la différence — il reçoit du contexte ordinaire.

**Nuance** : tout ce que fait une app grand public n'est pas du RAG. Un **petit fichier** est souvent collé en entier dans le contexte (*context stuffing*, pas de recherche sémantique) ; le **vrai RAG** ne se déclenche que quand le corpus dépasse la fenêtre de contexte. La bascule se fait sur la **taille** — RAG existe précisément parce qu'on ne peut pas tout mettre dans le contexte.

## Voir aussi
- [RAG agentique](rag-agentique.md) — un agent devant la récupération
- [Corrective RAG (cRAG)](corrective-rag.md) — grader + fallback web
- [Stratégies de chunking](strategies-de-chunking.md) · [Vérification de source](verification-de-source.md)
- [HyDE](hyde.md) · [GraphRAG](graphrag.md) · [Reranking](reranking.md) · [Contextual Retrieval](contextual-retrieval.md)
