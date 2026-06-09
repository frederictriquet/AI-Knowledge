---
titre: "Chain-of-Thought (CoT)"
theme: raisonnement-planification
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/chain-of-thoughts
source_titre: "Qu’est-ce que le prompting par chaîne de pensée (CoT) ?"
---

# Chain-of-Thought (CoT)

**En une phrase** — demander au modèle d'écrire ses étapes de raisonnement intermédiaires avant la réponse finale, au lieu de répondre directement.

## En détail
La CoT est une technique de prompt engineering qui décompose un problème complexe en étapes logiques séquentielles, améliorant le raisonnement arithmétique, symbolique et de bon sens. L'utilisateur ajoute typiquement une instruction en fin de prompt (« décrivez vos étapes de raisonnement »). La CoT est une capacité émergente qui apparaît avec la taille du modèle ; l'instruction tuning permet toutefois à des modèles plus petits (Granite Instruct) de la pratiquer. Plusieurs variantes existent : CoT zero-shot (sans exemples), auto-CoT (génération automatique des étapes), CoT multimodale (texte + image) et la « cohérence propre ». Limites : coût de calcul accru, prompts de haute qualité requis, risque de chemins plausibles mais incorrects, difficulté d'évaluation.

## Dans les agents
Côté agents, le CoT n'est pas une technique autonome mais la **brique de raisonnement de ReAct** : la boucle pensée→action→observation s'appuie sur une chaîne de pensée. À noter : le CoT seul augmente le risque d'**hallucination**, atténué par l'ancrage externe (les observations d'outils) ; ReAct « tire grandement parti de modèles hautement performants ».

## Tradeoff / insight pour un senior
La CoT échange du coût de calcul (tokens générés) contre de la fiabilité et de l'observabilité sur les tâches multi-étapes. Le piège : un raisonnement verbeux et plausible n'est pas un raisonnement correct — la trace n'est pas une preuve. Sur les modèles récents déjà entraînés au raisonnement, l'instruction explicite apporte moins, voire dégrade les tâches simples. L'insight de l'état de l'art : le CoT n'émerge réellement que sur les gros modèles ; sur petits modèles il dégrade souvent la réponse (sauf instruction tuning, cf. Granite Instruct).

## Source primaire
Wei et al. 2022, « Chain-of-Thought Prompting Elicits Reasoning in Large Language Models ».

## Voir aussi
- [Tree of Thoughts (ToT)](tree-of-thoughts.md)
- [Self-Consistency](self-consistency.md)
- [ReAct](react.md)
