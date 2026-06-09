---
titre: "Décodage contraint / sortie structurée"
theme: efficacite-cout
niveau: 🟡
source_url: https://arxiv.org/abs/2307.09702---

# Décodage contraint / sortie structurée

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. Glossaire · Pertinence 🟡 tradeoff

**En une phrase** — forcer la sortie à respecter une grammaire/schéma (JSON, regex) en masquant les tokens invalides au décodage ; garantit un format parsable (≠ « demander gentiment » du JSON).

## L'idée
Plutôt que d'espérer un JSON valide via le prompt, le décodage contraint agit *pendant* la génération : à chaque pas, un automate dérivé d'une grammaire ou d'un schéma calcule l'ensemble des tokens autorisés et **masque** (logit bias à −∞) tous les autres. Le modèle ne peut littéralement pas produire de sortie malformée. Outlines compile la grammaire/regex en un automate fini parcouru token par token, sans surcoût d'inférence notable.

## Tradeoff / quand l'utiliser
Indispensable dès qu'une sortie machine-parsable est requise : appels d'outils, extraction structurée, pipelines. Garantit la *forme*, pas la *justesse* du contenu. Contraindre trop fort peut dégrader le raisonnement (le modèle ne peut plus « réfléchir à voix haute » avant de structurer). Nécessite un moteur d'inférence exposant les logits.

## Source primaire
Willard & Louf, 2023, *Efficient Guided Generation for Large Language Models* (Outlines), arXiv:2307.09702 *(arXiv vérifié — HTTP 200 + titre)* ; Microsoft guidance ; JSON mode des API (OpenAI, etc.).

## Voir aussi
- [tool-calling](tool-calling.md) (corpus)
