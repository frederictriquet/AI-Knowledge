---
titre: "LLM Wiki : un wiki maintenu par le LLM plutôt que du RAG"
type: "Concept"
theme: rag-contexte
niveau: 🟡
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
source_titre: "LLM Wiki — Andrej Karpathy (gist)"
objectifs: [mise-en-prod]
---

# LLM Wiki : un wiki maintenu par le LLM plutôt que du RAG

**En une phrase** — Plutôt que de re-synthétiser depuis les sources brutes à chaque question (RAG classique), on fait maintenir au LLM un **wiki persistant** (markdown interconnecté) : une couche de connaissance *compilée* dont la valeur se cumule à chaque source ingérée.

## Ce que dit la source
Karpathy propose un pattern pour bâtir un knowledge base personnel avec un LLM. L'idée : extraire le savoir d'une source **une seule fois**, l'intégrer dans des pages, mettre à jour les renvois, noter les contradictions — au lieu de tout reconstruire à chaque requête. **Trois couches** : (1) **sources brutes** immuables (articles, papiers) ; (2) **le wiki** possédé par le LLM (pages de résumé, de concept, d'entité, de synthèse) ; (3) **le schéma** (`CLAUDE.md`) qui dicte structure et workflows. **Trois opérations** : *ingest* (lire → discuter les takeaways → écrire un résumé → mettre à jour 10-15 pages + cross-refs), *query* (chercher les pages → répondre avec citations → reverser l'exploration), *lint* (santé périodique : contradictions, claims périmés, pages orphelines, renvois manquants). Plus un `index.md` (catalogue) et un `log.md` (journal append-only). L'insight clé : « la partie pénible d'un knowledge base, ce n'est pas lire ou penser — c'est la **paperasse** (bookkeeping) » ; le LLM excelle justement à cette maintenance que les humains abandonnent (à l'humain le curatorial, à la machine l'administratif). Filiation revendiquée : le **Memex** de Vannevar Bush (1945), dont le pattern résout enfin le problème de maintenance.

## Pourquoi c'est utile
Le pattern reformule le RAG : non plus « récupérer puis générer à chaud », mais **compiler et entretenir** une couche intermédiaire qui se bonifie. Il fournit un vocabulaire (3 couches, ingest/query/lint) et une checklist directement applicables à un corpus de fiches markdown — *exactement* la forme de cette base.

## Où est la partie LLM (opérateur, pas composant)
Le wiki est **passif** : des fichiers markdown inertes. Le LLM n'y est pas *stocké* — il en est l'**opérateur** (un bibliothécaire, pas une étagère). Tout le travail intelligent est dans les opérations, surtout l'**ingest** : décider quoi extraire, rédiger au format maison, et — le plus pénible — **trouver et mettre à jour les pages existantes** + les renvois croisés (le « bookkeeping »). Conséquence : l'effort du LLM est **déplacé du read-time vers le write-time**. Là où le RAG fait travailler le LLM *à chaque question* (récupérer + synthétiser à chaud), le wiki le fait travailler *une fois à l'ingest* (compiler), et la requête devient une simple consultation d'une couche déjà curée. Le partage est **hybride** : déterministe pour ce qui se calcule (embeddings de dédup, lint de structure, index), LLM pour ce qui se juge (extraction, fusion vs nouveau, rédaction, contradictions de sens).

## Points clés
- Wiki *maintenu* (valeur cumulative) vs RAG *recalculé* à chaque requête.
- 3 couches : sources brutes immuables · wiki possédé par le LLM · schéma (`CLAUDE.md`).
- 3 opérations : ingest · query · lint (+ `index.md`, `log.md`).
- Le goulot d'un KB = le **bookkeeping** ; c'est ce que le LLM automatise.
- Reste **abstrait par choix** : « instancie ta version avec ton agent ».

## Voir aussi
- [Des rapports plutôt que du RAG](rapports-plutot-que-rag.md)
- [RAG vs fine-tuning vs prompt engineering](rag-vs-fine-tuning-vs-prompt-engineering.md)
- [Mémoire épisodique / sémantique / procédurale](memoire-episodique-semantique-procedurale.md)
- [AgentOps](agentops.md)
