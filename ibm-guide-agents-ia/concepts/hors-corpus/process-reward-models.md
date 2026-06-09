# Process Reward Models (PRM)

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. [Glossaire](../../GLOSSAIRE-PATTERNS.md) · Pertinence 🔴 substance

**En une phrase** — un modèle de récompense qui note **chaque étape** d'un raisonnement, pas seulement la réponse finale.

## L'idée
Un *Outcome Reward Model* (ORM) ne juge que le résultat : il récompense parfois un raisonnement faux qui tombe juste par chance. Le **Process Reward Model** attribue un score à chaque pas intermédiaire de la chaîne de raisonnement, donnant un signal plus dense et localisé. Lightman et al. montrent que la supervision par processus surpasse la supervision par résultat sur les problèmes de maths, et publient PRM800K, un jeu d'annotations pas-à-pas. Le PRM sert ensuite à guider la recherche (best-of-N vérifié, arbre de raisonnement) ou à entraîner le modèle.

## Tradeoff / quand l'utiliser
Brique sous-jacente des modèles de raisonnement et du best-of-N vérifié. Avantage : meilleure fiabilité, détection des étapes fautives. Coût : annotation par étape onéreuse et risque de *reward hacking* sur le scoring intermédiaire.

## Source primaire
Lightman et al., 2023, *Let's Verify Step by Step*, arXiv:2305.20050 (OpenAI, jeu PRM800K) *(arXiv vérifié — HTTP 200 + titre)*.

## Voir aussi
- [inference-time-scaling](inference-time-scaling.md) (hors-corpus sœur)
- [evaluation-trajectoire](../evaluation-trajectoire.md) (corpus)
