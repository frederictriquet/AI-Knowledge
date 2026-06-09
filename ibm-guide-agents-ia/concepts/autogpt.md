# AutoGPT

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [42-autogpt](../md/42-autogpt.md)

**En une phrase** — le démonstrateur de 2023 qui décompose un objectif de haut niveau en sous-tâches et tourne en boucle création/priorisation/exécution avec mémoire vectorielle ; surtout une valeur historique.

## Ce que dit le corpus
IBM décrit AutoGPT comme une plateforme open source lancée le 30 mars 2023 par Toran Bruce Richards (Significant Gravitas). Elle s'appuie sur les modèles GPT d'OpenAI (GPT-4o mini, GPT-4, GPT-3.5) pour comprendre un objectif de haut niveau, le décomposer en sous-tâches et automatiser leur exécution. Le workflow type : entrée utilisateur, création de tâches, hiérarchisation des tâches, exécution, évaluation de l'avancement et amélioration du workflow, finalisation. Des agents dédiés créent, priorisent et exécutent les tâches, et communiquent en temps réel pour ajuster la suite. AutoGPT accède à Internet via des plug-ins et dispose d'une mémoire à court et long terme grâce aux bases de données vectorielles. Le corpus est explicite sur les limites : l'outil reste expérimental, sa fiabilité n'est pas garantie ; il peut se laisser distraire, halluciner puis se baser sur ces hallucinations, mal interpréter les données et finir par échouer. AutoGPT n'est pas une IAG.

## Tradeoff / insight pour un senior
Importance d'abord historique : AutoGPT a popularisé l'idée d'auto-prompting (l'agent génère ses propres prompts vers l'objectif, sans relance humaine), mais le corpus documente sa fragilité (dérive, hallucinations cumulatives, coûts de tokens, installation/auto-hébergement complexes via Docker). À connaître comme jalon, pas comme socle de production.

## Source primaire
Non citée formellement par IBM ; attribuée à Toran Bruce Richards (2023). Voir le dépôt GitHub Significant-Gravitas/AutoGPT (hors-corpus).

## Voir aussi
- [babyagi](babyagi.md)
- [taxonomie-5-types-agents](taxonomie-5-types-agents.md)
