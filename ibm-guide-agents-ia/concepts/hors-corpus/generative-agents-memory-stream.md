# Generative Agents — memory stream

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. [Glossaire](../../GLOSSAIRE-PATTERNS.md) · Pertinence 🔴 substance

**En une phrase** — un journal horodaté d'observations, relu par un score combinant **récence + importance + pertinence** ; la fonction de scoring est l'idée transférable pour une mémoire d'agent.

## L'idée
Chaque agent tient un *memory stream* : une liste chronologique d'observations en langage naturel, chacune horodatée. Pour agir, l'agent ne relit pas tout : il récupère les souvenirs les plus utiles via un score combinant **récence** (décroissance temporelle), **importance** (notée par le modèle) et **pertinence** (similarité sémantique à la situation courante). Par-dessus, un mécanisme de *réflexion* synthétise périodiquement des souvenirs en conclusions de plus haut niveau, elles-mêmes réinjectées dans le stream.

## Tradeoff / quand l'utiliser
La fonction de scoring récence+importance+pertinence est directement réutilisable pour toute **mémoire d'agent au long cours** : elle hiérarchise mieux qu'une simple recherche vectorielle. Coût : noter l'importance demande un appel LLM par observation, et le stream grossit indéfiniment sans compaction.

## Source primaire
Park et al., 2023, *Generative Agents: Interactive Simulacra of Human Behavior*, arXiv:2304.03442 (Stanford). *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [memgpt](memgpt.md) (hors-corpus sœur)
- [memoire-episodique-semantique-procedurale](../memoire-episodique-semantique-procedurale.md) (corpus)
