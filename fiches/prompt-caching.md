---
titre: "Prompt caching"
theme: prompting
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/tutorials/implement-prompt-caching-langchain
source_titre: "Implémenter la mise en cache des prompts avec LangChain pour créer des applications LLM efficaces"
---

# Prompt caching

**En une phrase** — réutiliser une réponse déjà calculée pour un prompt identique, mais attention : le tutoriel implémente un cache de réponses exact-match côté client (LangChain `SQLiteCache`), pas le prompt caching de préfixe (KV-cache) côté fournisseur.

## En détail
La mise en cache des prompts se présente comme une « mémoire » de l'application : si la même entrée est rencontrée à nouveau, la réponse stockée est récupérée au lieu de relancer un appel d'API, d'où latence réduite, sorties cohérentes, moins de pression sur les rate limits et plus de résilience. Le tutoriel branche concrètement `set_llm_cache(SQLiteCache(database_path=".langchain.db"))` sur un `WatsonxLLM` (Granite 3-8B) : le cache stocke les réponses dans une base SQLite locale et n'est touché que sur correspondance exacte du prompt. Les mesures montrent un temps CPU très faible mais un temps réel dominé par les I/O et l'attente réseau. La conclusion élargit le sujet au prompt caching côté fournisseur, qui met en cache tokens d'entrée/sortie, embeddings, préfixes et messages système, et évoque TTL, cache-hit rate, lecture/écriture en cache — c'est une couche distincte du `SQLiteCache` exact-match présenté.

## Tradeoff / insight pour un senior
Deux mécanismes à ne pas confondre. (1) Cache de réponses exact-match (ce tutoriel) : gain maximal mais hit rate fragile — la moindre variation du prompt fait un miss ; utile pour des requêtes répétées à l'identique (tests, FAQ figées). (2) Prompt caching de préfixe / KV-cache côté fournisseur : réutilise le calcul du préfixe partagé (système + contexte), facturé moins cher, et tolère une queue de prompt variable. Pour de la similarité sémantique (et non l'égalité stricte), il faut un caching sémantique, troisième mécanisme encore différent.

## Le KV-cache de préfixe en détail (Anthropic / OpenAI)
À l'inférence, le modèle calcule un cache KV (clés/valeurs d'attention) par token. Quand un long préfixe est identique d'un appel à l'autre — système, définitions d'outils, gros document — le fournisseur conserve ce cache et reprend le calcul juste après le préfixe ; seuls les tokens nouveaux sont traités, et les tokens en cache sont facturés à tarif réduit. Deux contraintes pratiques : le cache a une **durée de vie courte** (quelques minutes) et exige un préfixe **exactement** identique — d'où la règle : **ordonner le prompt du plus stable au plus variable** pour maximiser les hits.

## Source primaire
Page IBM citée (think/tutorials/implement-prompt-caching-langchain) pour le cache exact-match LangChain/watsonx. Pour le KV-cache de préfixe : Anthropic, *Prompt caching* (2024, doc produit) ; OpenAI, *Prompt caching* (2024, doc produit). Aucune référence académique.

## Voir aussi
- [Semantic caching](semantic-caching.md)
