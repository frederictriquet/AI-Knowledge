---
titre: "Décodage contraint / sortie structurée"
type: "Concept"
theme: efficacite-cout
niveau: 🟡
source_url: https://arxiv.org/abs/2307.09702
---

# Décodage contraint / sortie structurée

**En une phrase** — forcer la sortie à respecter une grammaire/schéma (JSON, regex) en masquant les tokens invalides au décodage ; garantit un format parsable (≠ « demander gentiment » du JSON).

## L'idée
Plutôt que d'espérer un JSON valide via le prompt, le décodage contraint agit *pendant* la génération : à chaque pas, un automate dérivé d'une grammaire ou d'un schéma calcule l'ensemble des tokens autorisés et **masque** (logit bias à −∞) tous les autres. Le modèle ne peut littéralement pas produire de sortie malformée. Outlines compile la grammaire/regex en un automate fini parcouru token par token, sans surcoût d'inférence notable.

## Exemple
Le papier illustre avec la regex de flottant `([0-9]*)?\.?[0-9]*` sur un vocabulaire jouet `{"A", ".", "42", ".2", "1"}` : à l'état initial l'automate masque `"A"` (non accepté), puis après avoir échantillonné `".2"` il ne reste que `"42"` et `"1"` comme complétions valides. La clé du « peu de surcoût » : un index pré-calculé hors inférence (hash-map état FSM → tokens valides) ramène le masquage à O(1) par token au lieu du O(N) naïf qui balaie tout le vocabulaire. Côté API Outlines, `generate.regex(model, r"\s*([Yy]es|[Nn]o|[Nn]ever|[Aa]lways)")` force GPT2-medium à répondre par l'un de ces quatre mots à « Is 1+1=2? ».

## Tradeoff / quand l'utiliser
Indispensable dès qu'une sortie machine-parsable est requise : appels d'outils, extraction structurée, pipelines. Garantit la *forme*, pas la *justesse* du contenu. Contraindre trop fort peut dégrader le raisonnement (le modèle ne peut plus « réfléchir à voix haute » avant de structurer). Nécessite un moteur d'inférence exposant les logits.

## Source primaire
Willard & Louf, 2023, *Efficient Guided Generation for Large Language Models* (Outlines), arXiv:2307.09702 *(arXiv vérifié — HTTP 200 + titre)* ; Microsoft guidance ; JSON mode des API (OpenAI, etc.).

## Voir aussi
- [tool-calling](tool-calling.md)
