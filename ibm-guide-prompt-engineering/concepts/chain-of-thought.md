# Chain-of-Thought (CoT)

> Fiche du [glossaire prompting](../GLOSSAIRE-PROMPTING.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [../md/20-chain-of-thoughts.md](../md/20-chain-of-thoughts.md)

**En une phrase** — demander au modèle d'écrire ses étapes de raisonnement intermédiaires avant la réponse finale, au lieu de répondre directement.

## Ce que dit le corpus
IBM présente la CoT comme une technique de prompt engineering qui décompose un problème complexe en étapes logiques séquentielles, améliorant le raisonnement arithmétique, symbolique et de bon sens. L'utilisateur ajoute typiquement une instruction en fin de prompt (« décrivez vos étapes de raisonnement »). IBM la qualifie de capacité émergente, qui apparaît avec la taille du modèle, mais note que l'instruction tuning permet à des modèles plus petits (Granite Instruct) de pratiquer la CoT. Le corpus détaille plusieurs variantes : CoT zero-shot (sans exemples), auto-CoT (génération automatique des étapes), CoT multimodale (texte + image) et la « cohérence propre ». Limites citées : coût de calcul accru, prompts de haute qualité requis, risque de chemins plausibles mais incorrects, difficulté d'évaluation.

## Tradeoff / insight pour un senior
La CoT échange du coût de calcul (tokens générés) contre de la fiabilité et de l'observabilité sur les tâches multi-étapes. Le piège : un raisonnement verbeux et plausible n'est pas un raisonnement correct — la trace n'est pas une preuve. Sur les modèles récents déjà entraînés au raisonnement, l'instruction explicite apporte moins, voire dégrade les tâches simples.

## Source primaire
Non citée par IBM (notes de bas de page [1]–[15] non résolues dans le fichier) — voir Wei et al. 2022, « Chain-of-Thought Prompting Elicits Reasoning in Large Language Models » (hors-corpus).

## Voir aussi
- [Tree of Thoughts (ToT)](tree-of-thoughts.md)
- [Self-Consistency](self-consistency.md)
- (base agents) [Chain-of-Thought](../../ibm-guide-agents-ia/concepts/chain-of-thought.md)
