# In-context learning (ICL)

> Fiche du [glossaire prompting](../GLOSSAIRE-PROMPTING.md) · Pertinence 🔴 substance · Provenance ✅ présent · Sources corpus : [../md/23-in-context-learning.md](../md/23-in-context-learning.md)

**En une phrase** — capacité d'un LLM à apprendre une tâche depuis les démonstrations placées dans son prompt, sans aucune mise à jour de ses poids.

## Ce que dit le corpus
L'ICL conditionne un LLM sur un prompt contenant k paires entrée-sortie ; le modèle infère la tâche et applique le même mapping à une nouvelle entrée, en calculant argmax P(yⱼ | x, C) — les paramètres restent inchangés. Le corpus formalise le mécanisme et situe zero/one/few-shot et CoT comme des techniques internes à l'ICL, pas distinctes de lui. Deux cadrages théoriques sont exposés : l'ICL comme inférence bayésienne (le modèle déduit un concept latent et gagne en assurance à mesure que des exemples s'ajoutent) et l'ICL comme descente de gradient implicite (les transformers simulent en interne un apprentissage, démontré sur la régression linéaire). Point fort cité : même des étiquettes aléatoires améliorent la performance — le format et la distribution du prompt comptent autant que les étiquettes. Limites : sensibilité aux prompts, dépendance à l'échelle du modèle et à la qualité du pré-entraînement, biais, confidentialité. Le corpus introduit aussi l'« ingénierie contextuelle » comme extension de l'ICL aux systèmes agentiques.

## Tradeoff / insight pour un senior
Le fait que des étiquettes aléatoires fonctionnent (le modèle apprend surtout le format et l'espace des classes, pas le mapping exact) recadre le débogage few-shot : un échec vient souvent d'un mauvais format ou d'un ordre d'exemples, pas d'étiquettes erronées. L'ICL est une adaptation à l'inférence — puissante, mais instable et non persistante d'une requête à l'autre.

## Source primaire
« Language Models are Few-Shot Learners » (article fondateur de GPT-3), cité par IBM comme introduisant l'ICL.

## Voir aussi
- [few-shot-prompting](few-shot-prompting.md)
- [zero-shot-prompting](zero-shot-prompting.md)
- [prompt-tuning](prompt-tuning.md)
