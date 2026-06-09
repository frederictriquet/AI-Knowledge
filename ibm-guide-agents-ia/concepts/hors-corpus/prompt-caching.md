# Prompt caching (réutilisation de cache KV)

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. [Glossaire](../../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff

**En une phrase** — mettre en cache le préfixe de prompt (système, contexte, outils) côté fournisseur pour ne pas le recalculer à chaque appel ; baisse latence et coût quand on réutilise un grand préfixe stable.

## L'idée
À l'inférence, le modèle calcule un cache KV (clés/valeurs d'attention) pour chaque token du prompt. Quand un long préfixe est identique d'un appel à l'autre — instructions système, définitions d'outils, gros document de contexte — le fournisseur conserve ce cache KV et reprend le calcul juste après le préfixe. Seuls les tokens nouveaux sont traités. Les tokens en cache sont facturés à tarif réduit. NB : distinct du **semantic caching**, qui met en cache des RÉPONSES finales indexées par similarité de requête.

## Tradeoff / quand l'utiliser
Gain net dès qu'un gros préfixe stable est réutilisé : agents avec long system prompt + outils, RAG sur document fixe, conversations longues. Le cache a une **durée de vie courte** (quelques minutes) et impose un préfixe *exactement* identique : il faut ordonner le prompt du plus stable au plus variable pour maximiser les hits.

## Source primaire
Anthropic, *Prompt caching* (2024, documentation produit) ; OpenAI, *Prompt caching* (2024, documentation produit). Pas d'arXiv.

## Voir aussi
- [semantic-caching](../semantic-caching.md) (corpus)
