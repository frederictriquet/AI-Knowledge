---
titre: "In-context learning (ICL)"
theme: prompting
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/in-context-learning
source_titre: "Qu’est-ce que l’apprentissage contextuel ?"
---

# In-context learning (ICL)

**En une phrase** — capacité d'un LLM à apprendre une tâche depuis les démonstrations placées dans son prompt, sans aucune mise à jour de ses poids.

## En détail
L'ICL conditionne un LLM sur un prompt contenant k paires entrée-sortie ; le modèle infère la tâche et applique le même mapping à une nouvelle entrée, en calculant argmax P(yⱼ | x, C) — les paramètres restent inchangés. Zero/one/few-shot et CoT sont des techniques internes à l'ICL, pas distinctes de lui. Deux cadrages théoriques coexistent : l'ICL comme inférence bayésienne (le modèle déduit un concept latent et gagne en assurance à mesure que des exemples s'ajoutent) et l'ICL comme descente de gradient implicite (les transformers simulent en interne un apprentissage, démontré sur la régression linéaire). À noter : même des étiquettes aléatoires améliorent la performance — le format et la distribution du prompt comptent autant que les étiquettes. Limites : sensibilité aux prompts, dépendance à l'échelle du modèle et à la qualité du pré-entraînement, biais, confidentialité. L'« ingénierie contextuelle » est présentée comme extension de l'ICL aux systèmes agentiques.

## Tradeoff / insight pour un senior
Le fait que des étiquettes aléatoires fonctionnent (le modèle apprend surtout le format et l'espace des classes, pas le mapping exact) recadre le débogage few-shot : un échec vient souvent d'un mauvais format ou d'un ordre d'exemples, pas d'étiquettes erronées. L'ICL est une adaptation à l'inférence — puissante, mais instable et non persistante d'une requête à l'autre.

## Source primaire
« Language Models are Few-Shot Learners » (article fondateur de GPT-3, Brown et al. 2020) — article qui introduit l'ICL.

## Voir aussi
- [few-shot-prompting](few-shot-prompting.md)
- [zero-shot-prompting](zero-shot-prompting.md)
- [prompt-tuning](prompt-tuning.md)
