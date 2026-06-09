---
titre: "Voyager & bibliothèque de compétences"
theme: outils-function-calling
niveau: 🔴
source_url: https://arxiv.org/abs/2305.16291
---

# Voyager & bibliothèque de compétences

**En une phrase** — un agent à apprentissage continu qui **acquiert, stocke et réutilise** des compétences sous forme de code, se constituant une mémoire procédurale auto-construite.

## L'idée
Voyager explore un monde ouvert (démontré sur Minecraft) sans objectif figé. Quand il résout une tâche, il écrit la solution comme une **fonction (skill) réutilisable** et l'archive dans une *skill library* indexée. Pour une nouvelle tâche, il **récupère** les compétences pertinentes et les compose, au lieu de repartir de zéro. Une boucle de curriculum automatique propose des objectifs croissants, et un mécanisme d'auto-vérification corrige le code défaillant. L'agent **accumule** ainsi des capacités de plus en plus complexes au fil du temps.

## Tradeoff / quand l'utiliser
Pertinent pour des agents long-terme dans des environnements répétitifs où l'on veut **capitaliser** plutôt que réapprendre. Contrepartie : nécessite un environnement exécutable et vérifiable ; la bibliothèque peut accumuler des compétences obsolètes ou de mauvaise qualité sans curation.

## Source primaire
Wang et al., 2023, *Voyager: An Open-Ended Embodied Agent with Large Language Models*, arXiv:2305.16291 *(arXiv vérifié — HTTP 200 + titre)*.

## Voir aussi
- [agent-apprenant](agent-apprenant.md)
- [codeact](codeact.md)
