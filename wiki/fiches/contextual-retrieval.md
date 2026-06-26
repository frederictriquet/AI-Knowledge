---
titre: "Contextual Retrieval"
type: "Concept"
theme: evaluation
niveau: 🟡
source_url: https://www.anthropic.com/news/contextual-retrieval
source_titre: "Introducing Contextual Retrieval — Anthropic"
---

# Contextual Retrieval

**En une phrase** — préfixer chaque chunk d'un court contexte (situant le chunk dans son document) *avant* l'embedding, pour réduire les échecs de récupération dus à des chunks ambigus.

## L'idée
Découper un document détruit le contexte : un chunk « le chiffre d'affaires a augmenté de 3 % » ne dit ni de quelle entreprise ni de quel trimestre il s'agit, et s'embede mal. Contextual Retrieval demande à un LLM de générer, pour chaque chunk, une ou deux phrases le resituant dans le document complet, puis préfixe le chunk de ce contexte avant de calculer l'embedding et l'index BM25. La récupération porte ainsi sur des chunks *auto-suffisants*. Le prompt caching rend le passage du document entier abordable.

## Exemple
Chunk brut : « The company's revenue grew by 3% over the previous quarter. » — inexploitable isolé. Le prompt contextualisant (« give a short succinct context to situate this chunk within the overall document ») produit le préfixe : « This chunk is from an SEC filing on ACME corp's performance in Q2 2023; the previous quarter's revenue was $314 million. » Résultats cumulés sur les échecs de récupération top-20 (baseline 5,7 %) : embeddings contextuels seuls −35 % (→ 3,7 %), +BM25 contextuel −49 % (→ 2,9 %), +reranking −67 % (→ 1,9 %). Coût d'indexation : 1,02 $ par million de tokens de documents grâce au prompt caching.

## Tradeoff / quand l'utiliser
Réduit nettement les échecs de récupération sur des corpus fragmentés (rapports, contrats). Coût : un appel LLM contextualisant par chunk à l'indexation. Combinable avec un reranker pour cumuler les gains. À privilégier quand les chunks isolés perdent leur sens.

## Source primaire
Anthropic, 2024, *Introducing Contextual Retrieval* (billet d'ingénierie ; pas d'arXiv).

## Voir aussi
- [reranking](reranking.md)
- [agentic-chunking](agentic-chunking.md)
