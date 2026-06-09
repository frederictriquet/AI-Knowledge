# Prompt caching

> Fiche du [glossaire prompting](../GLOSSAIRE-PROMPTING.md) · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [../md/19-implement-prompt-caching-langchain.md](../md/19-implement-prompt-caching-langchain.md)

**En une phrase** — réutiliser une réponse déjà calculée pour un prompt identique, mais attention : le tutoriel implémente un cache de réponses exact-match côté client (LangChain `SQLiteCache`), pas le prompt caching de préfixe (KV-cache) côté fournisseur.

## Ce que dit le corpus
IBM décrit la mise en cache des prompts comme une « mémoire » de l'application : si la même entrée est rencontrée à nouveau, la réponse stockée est récupérée au lieu de relancer un appel d'API, d'où latence réduite, sorties cohérentes, moins de pression sur les rate limits et plus de résilience. Le tutoriel branche concrètement `set_llm_cache(SQLiteCache(database_path=".langchain.db"))` sur un `WatsonxLLM` (Granite 3-8B) : le cache stocke les réponses dans une base SQLite locale et n'est touché que sur correspondance exacte du prompt. Les mesures montrent un temps CPU très faible mais un temps réel dominé par les I/O et l'attente réseau. La conclusion élargit le sujet au prompt caching côté fournisseur, qui met en cache tokens d'entrée/sortie, embeddings, préfixes et messages système, et évoque TTL, cache-hit rate, lecture/écriture en cache — c'est une couche distincte du `SQLiteCache` exact-match présenté.

## Tradeoff / insight pour un senior
Deux mécanismes à ne pas confondre. (1) Cache de réponses exact-match (ce tutoriel) : gain maximal mais hit rate fragile — la moindre variation du prompt fait un miss ; utile pour des requêtes répétées à l'identique (tests, FAQ figées). (2) Prompt caching de préfixe / KV-cache côté fournisseur : réutilise le calcul du préfixe partagé (système + contexte), facturé moins cher, et tolère une queue de prompt variable. Pour de la similarité sémantique (et non l'égalité stricte), il faut un caching sémantique, troisième mécanisme encore différent.

## Source primaire
Page IBM citée (think/tutorials/implement-prompt-caching-langchain). Aucune référence académique ; documentation produit LangChain/watsonx.

## Voir aussi
- [Prompt caching](../../ibm-guide-agents-ia/concepts/hors-corpus/prompt-caching.md) (base agents, hors-corpus)
- [Semantic caching](../../ibm-guide-agents-ia/concepts/semantic-caching.md) (base agents)
