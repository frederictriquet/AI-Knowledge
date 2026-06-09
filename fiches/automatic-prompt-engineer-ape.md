---
titre: "Automatic Prompt Engineer (APE) & design automatique de prompts"
theme: prompting
niveau: 🟡
source_url: https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/
source_titre: "Prompt Engineering"---

# Automatic Prompt Engineer (APE) & design automatique de prompts

> Fiche **source : Lilian Weng** · [post complet](../sources/lilian-weng/md/2023-03-15-prompt-engineering.md) · Pertinence 🟡 tradeoff

**En une phrase** — le prompt n'est pas un texte à rédiger à la main mais un objet à optimiser : on fait générer des candidats d'instruction par le LLM puis on garde le meilleur selon une fonction de score mesurable.

## Ce que dit la source
Weng pose le cadre : un prompt est une séquence de tokens-préfixes qui augmente la probabilité de la sortie voulue, donc traitable comme des paramètres optimisables. Côté espace d'embeddings, elle cite AutoPrompt (Shin et al. 2020), Prefix-Tuning (Li & Liang 2021), P-tuning et Prompt-Tuning, en notant une tendance à la simplification progressive du dispositif. **APE** (Automatic Prompt Engineer ; Zhou et al. 2022) opère en langage naturel : (1) faire générer au LLM des instructions candidates à partir de quelques paires entrée-sortie ; (2) chercher l'instruction ρ qui maximise une fonction de score f par échantillon, comme l'exactitude d'exécution ou la log-probabilité ; (3) raffiner par une recherche Monte-Carlo itérative qui propose des variantes sémantiquement proches. Weng cite aussi Shum et al. (2023) — augment-prune-select — et Zhang et al. (2023) — clustering de questions par k-means — pour construire automatiquement des prompts chain-of-thought.

## Ce que ça ajoute vs IBM
Le guide IBM traite l'optimisation de prompts comme une pratique outillée (DSPy, etc.) ; Weng en donne la formulation fondatrice : le prompt comme variable d'une recherche pilotée par un score d'exécution.

## Sources primaires (citées par Weng)
- Zhou et al., *Large Language Models Are Human-Level Prompt Engineers* (APE, ICLR 2023)
- Shin et al., *AutoPrompt* (2020)
- Shum et al., *Automatic Prompt Augmentation and Selection with CoT from Labeled Data* (2023)
- Zhang et al., *Automatic chain of thought prompting* (2022)

## Voir aussi
- (base prompting) [Optimisation des prompts](prompt-optimization.md) · [DSPy](dspy.md)
- [post complet](../sources/lilian-weng/md/2023-03-15-prompt-engineering.md)
