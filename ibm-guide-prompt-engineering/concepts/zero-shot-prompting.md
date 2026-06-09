# Zero-shot prompting

> Fiche du [glossaire prompting](../GLOSSAIRE-PROMPTING.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [../md/08-zero-shot-prompting.md](../md/08-zero-shot-prompting.md)

**En une phrase** — demander une tâche à un LLM sans lui fournir d'exemple, en s'appuyant uniquement sur ses connaissances pré-entraînées.

## Ce que dit le corpus
Le zero-shot est une méthode de prompt engineering où le modèle ne reçoit aucun exemple de sortie. IBM illustre avec granite-3-8b-instruct sur une tâche de classification (urgence d'un problème IT en « Élevé / Moyen / Faible »), exécutée dans watsonx.ai Prompt Lab en mode Freeform. Le corpus décompose les composants d'un prompt : instruction, contexte, données d'entrée et indicateur de sortie (ce dernier optionnel). Avantages : simplicité, facilité d'usage (aucune donnée requise), flexibilité. Limites : variabilité des performances selon la complexité de la tâche, et forte dépendance à la qualité du modèle pré-entraîné. Deux leviers d'amélioration sont décrits : le réglage des instructions (instruction tuning) et le RLHF. Applications : classification de texte, extraction d'informations, réponse aux questions, synthèse, génération, conversation.

## Tradeoff / insight pour un senior
Le corpus cite un résultat contre-intuitif : Reynolds & McDonell (2021) ont montré qu'avec une meilleure structure de prompt, le zero-shot peut surpasser le few-shot. Autrement dit, ajouter des exemples n'est pas toujours rentable ; soigner la formulation de l'instruction peut valoir mieux que consommer du contexte avec des démonstrations. Le corpus note que Schulhoff et al. (2024) trouvent des résultats différents — le débat reste ouvert.

## Source primaire
Reynolds et McDonell (2021), cités par IBM comme constatant que le zero-shot peut surpasser le few-shot avec de meilleures structures de prompts ; Schulhoff et al. (2024) cités en contrepoint.

## Voir aussi
- [one-shot-prompting](one-shot-prompting.md)
- [few-shot-prompting](few-shot-prompting.md)
- [in-context-learning](in-context-learning.md)
