---
titre: "Automatic Prompt Engineer (APE) & design automatique de prompts"
type: "Concept"
theme: prompting
niveau: 🟡
source_url: https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/
source_titre: "Prompt Engineering"
---

# Automatic Prompt Engineer (APE) & design automatique de prompts

**En une phrase** — le prompt n'est pas un texte à rédiger à la main mais un objet à optimiser : on fait générer des candidats d'instruction par le LLM puis on garde le meilleur selon une fonction de score mesurable.

## Ce que dit la source
Weng pose le cadre : un prompt est une séquence de tokens-préfixes qui augmente la probabilité de la sortie voulue, donc traitable comme des paramètres optimisables. Côté espace d'embeddings, elle cite AutoPrompt (Shin et al. 2020), Prefix-Tuning (Li & Liang 2021), P-tuning et Prompt-Tuning, en notant une tendance à la simplification progressive du dispositif. **APE** (Automatic Prompt Engineer ; Zhou et al. 2022) opère en langage naturel : (1) faire générer au LLM des instructions candidates à partir de quelques paires entrée-sortie ; (2) chercher l'instruction ρ qui maximise une fonction de score f par échantillon, comme l'exactitude d'exécution ou la log-probabilité ; (3) raffiner par une recherche Monte-Carlo itérative qui propose des variantes sémantiquement proches. Weng cite aussi Shum et al. (2023) — augment-prune-select — et Zhang et al. (2023) — clustering de questions par k-means — pour construire automatiquement des prompts chain-of-thought.

## Exemple
Les prompts d'amorçage d'APE sont littéraux. Pour générer les candidats, on conditionne sur des paires entrée-sortie puis on termine par `{{Given desired input-output pairs}}\n\nThe instruction is` : le LLM complète l'instruction qui aurait produit ces exemples. Pour la phase Monte-Carlo, le prompt de mutation est `Generate a variation of the following instruction while keeping the semantic meaning.\n\nInput: ...\n\nOutput: ...`. Le score f est typiquement l'exactitude d'exécution `1[LM(·|ρ,x)=y]`, mesurable sans humain.

## Pourquoi c'est utile
Weng fournit la formulation fondatrice : le prompt comme variable d'une recherche pilotée par un score d'exécution — base théorique des approches outillées comme DSPy.

## Sources primaires (citées par Weng)
- Zhou et al., *Large Language Models Are Human-Level Prompt Engineers* (APE, ICLR 2023)
- Shin et al., *AutoPrompt* (2020)
- Shum et al., *Automatic Prompt Augmentation and Selection with CoT from Labeled Data* (2023)
- Zhang et al., *Automatic chain of thought prompting* (2022)

## Voir aussi
- [Optimisation des prompts](prompt-optimization.md) · [DSPy](dspy.md)
- [post complet](../sources/lilian-weng/md/2023-03-15-prompt-engineering.md)
