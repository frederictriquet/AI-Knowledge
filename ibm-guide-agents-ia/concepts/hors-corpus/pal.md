# PAL (Program-Aided Language models)

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. [Glossaire](../../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff

**En une phrase** — faire générer au LLM un **programme** (souvent Python) comme chaîne de raisonnement, puis déléguer le calcul à un interpréteur plutôt qu'au modèle.

## L'idée
Sur les tâches arithmétiques/logiques, le LLM se trompe dans l'exécution même quand le raisonnement est correct. PAL sépare les rôles : le modèle **traduit** le problème en code (c'est le « raisonnement »), et un **interpréteur** l'exécute pour produire la réponse exacte. Variante très proche : Program of Thoughts (PoT).

## Tradeoff / quand l'utiliser
Toujours pertinent : dès qu'une étape est déterministe (maths, dates, manipulation de données), délègue-la à du code exécuté, pas au LLM. C'est la généralisation du réflexe « ne demande pas au modèle de calculer ». Limite : suppose un environnement d'exécution de code **sandboxé** et sûr.

## Source primaire
Gao et al., 2022, *PAL: Program-aided Language Models*, arXiv:2211.10435. Voir aussi Chen et al., 2022, *Program of Thoughts (PoT)*. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [tool-grounding](../tool-grounding.md) (corpus)
- [chain-of-thought](../chain-of-thought.md) (corpus)
