---
titre: "AutoGPT"
type: "Concept"
theme: fondamentaux-agents
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/autogpt
source_titre: "Qu’est-ce qu’AutoGPT ?"
---

# AutoGPT

**En une phrase** — le démonstrateur de 2023 qui décompose un objectif de haut niveau en sous-tâches et tourne en boucle création/priorisation/exécution avec mémoire vectorielle ; surtout une valeur historique.

## En détail
AutoGPT est une plateforme open source lancée le 30 mars 2023 par Toran Bruce Richards (Significant Gravitas). Elle s'appuie sur les modèles GPT d'OpenAI (GPT-4o mini, GPT-4, GPT-3.5) pour comprendre un objectif de haut niveau, le décomposer en sous-tâches et automatiser leur exécution. Le workflow type : entrée utilisateur, création de tâches, hiérarchisation des tâches, exécution, évaluation de l'avancement et amélioration du workflow, finalisation. Des agents dédiés créent, priorisent et exécutent les tâches, et communiquent en temps réel pour ajuster la suite. AutoGPT accède à Internet via des plug-ins et dispose d'une mémoire à court et long terme grâce aux bases de données vectorielles. Les limites sont documentées : l'outil reste expérimental, sa fiabilité n'est pas garantie ; il peut se laisser distraire, halluciner puis se baser sur ces hallucinations, mal interpréter les données et finir par échouer. AutoGPT n'est pas une IAG.

## Exemple
En outil de développement commercial, on fixe à AutoGPT un objectif unique du type « identifie de nouveaux prospects et prépare un plan réseaux sociaux » : sans relance humaine, il génère lui-même la file de sous-tâches, navigue sur le web via plug-ins pour analyser articles d'actualité et contenus sociaux, en résume les tendances, puis esquisse jusqu'à une saison entière d'épisodes de podcast ou débogue le code d'un site. Revers documenté du laisser-tourner : il peut se laisser distraire par une tâche non essentielle, halluciner, puis bâtir les sous-tâches suivantes sur cette hallucination jusqu'à l'échec.

## Tradeoff / insight pour un senior
Importance d'abord historique : AutoGPT a popularisé l'idée d'auto-prompting (l'agent génère ses propres prompts vers l'objectif, sans relance humaine), mais sa fragilité est documentée (dérive, hallucinations cumulatives, coûts de tokens, installation/auto-hébergement complexes via Docker). À connaître comme jalon, pas comme socle de production.

## Source primaire
Attribuée à Toran Bruce Richards (2023). Voir le dépôt GitHub Significant-Gravitas/AutoGPT.

## Voir aussi
- [babyagi](babyagi.md)
- [taxonomie-5-types-agents](taxonomie-5-types-agents.md)
