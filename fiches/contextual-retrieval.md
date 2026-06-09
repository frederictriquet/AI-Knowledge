---
titre: "Contextual Retrieval"
theme: evaluation
niveau: 🟡
source_url: https://www.anthropic.com/news/contextual-retrieval
source_titre: "Introducing Contextual Retrieval — Anthropic"---

# Contextual Retrieval

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. Glossaire · Pertinence 🟡 tradeoff

**En une phrase** — préfixer chaque chunk d'un court contexte (situant le chunk dans son document) *avant* l'embedding, pour réduire les échecs de récupération dus à des chunks ambigus.

## L'idée
Découper un document détruit le contexte : un chunk « le chiffre d'affaires a augmenté de 3 % » ne dit ni de quelle entreprise ni de quel trimestre il s'agit, et s'embede mal. Contextual Retrieval demande à un LLM de générer, pour chaque chunk, une ou deux phrases le resituant dans le document complet, puis préfixe le chunk de ce contexte avant de calculer l'embedding et l'index BM25. La récupération porte ainsi sur des chunks *auto-suffisants*. Le prompt caching rend le passage du document entier abordable.

## Tradeoff / quand l'utiliser
Réduit nettement les échecs de récupération sur des corpus fragmentés (rapports, contrats). Coût : un appel LLM contextualisant par chunk à l'indexation. Combinable avec un reranker pour cumuler les gains. À privilégier quand les chunks isolés perdent leur sens.

## Source primaire
Anthropic, 2024, *Introducing Contextual Retrieval* (billet d'ingénierie ; pas d'arXiv).

## Voir aussi
- [reranking](reranking.md) (hors-corpus sœur)
- [agentic-chunking](agentic-chunking.md) (corpus)
