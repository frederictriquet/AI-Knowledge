---
titre: "Zero-shot prompting"
type: "Concept"
theme: prompting
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/zero-shot-prompting
source_titre: "Qu’est-ce que l’apprentissage zero-shot ?"
---

# Zero-shot prompting

**En une phrase** — demander une tâche à un LLM sans lui fournir d'exemple, en s'appuyant uniquement sur ses connaissances pré-entraînées.

## En détail
Le zero-shot est une méthode de prompt engineering où le modèle ne reçoit aucun exemple de sortie. Exemple illustratif : granite-3-8b-instruct sur une tâche de classification (urgence d'un problème IT en « Élevé / Moyen / Faible »), exécutée dans watsonx.ai Prompt Lab en mode Freeform. Les composants d'un prompt : instruction, contexte, données d'entrée et indicateur de sortie (ce dernier optionnel). Avantages : simplicité, facilité d'usage (aucune donnée requise), flexibilité. Limites : variabilité des performances selon la complexité de la tâche, et forte dépendance à la qualité du modèle pré-entraîné. Deux leviers d'amélioration : le réglage des instructions (instruction tuning) et le RLHF. Applications : classification de texte, extraction d'informations, réponse aux questions, synthèse, génération, conversation.

## Exemple
Sans aucun exemple résolu, on donne à granite-3-8b-instruct l'instruction « Définis le nom de classe pour le problème décrit : Élevé, Moyen ou Faible », suivie des seules définitions des trois classes, puis du cas « Problème : les utilisateurs signalent qu'ils ne sont pas en mesure de télécharger des fichiers ». L'indicateur de sortie « Classe : » amorce la réponse. Le modèle infère **Élevé** et justifie : impossibilité de télécharger → blocage de nombreux utilisateurs, fort coût commercial. Aucune démonstration n'a été fournie, seulement les définitions et le bon découpage instruction/contexte/entrée.

## Tradeoff / insight pour un senior
Reynolds & McDonell (2021) ont montré qu'avec une meilleure structure de prompt, le zero-shot peut surpasser le few-shot. Autrement dit, ajouter des exemples n'est pas toujours rentable ; soigner la formulation de l'instruction peut valoir mieux que consommer du contexte avec des démonstrations. Schulhoff et al. (2024) trouvent des résultats différents — le débat reste ouvert.

## Source primaire
Reynolds et McDonell (2021), constatant que le zero-shot peut surpasser le few-shot avec de meilleures structures de prompts ; Schulhoff et al. (2024) en contrepoint.

## Voir aussi
- [one-shot-prompting](one-shot-prompting.md)
- [few-shot-prompting](few-shot-prompting.md)
- [in-context-learning](in-context-learning.md)
