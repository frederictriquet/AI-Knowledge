---
titre: "Directional Stimulus Prompting (DSP)"
type: "Concept"
theme: prompting
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/directional-stimulus-prompting
source_titre: "Qu’est-ce que le prompting par stimulus directionnel (DSP) ?"
---

# Directional Stimulus Prompting (DSP)

**En une phrase** — entraîner un petit policy model qui génère, par instance, des stimuli (mots-clés, indices) orientant un grand LLM boîte noire gelé — on optimise le policy model, jamais le LLM.

## En détail
Le DSP répond au problème des LLM « boîte noire » (GPT-3/4, PaLM) accessibles seulement par prompt textuel. Plutôt que d'affiner le grand modèle, on entraîne un petit modèle de politique auxiliaire (T5, GPT-2) qui produit des stimuli directionnels adaptés à chaque entrée. L'entraînement se fait en deux temps : affinement supervisé (SFT) sur un petit jeu de données associant chaque entrée à un pseudo-stimulus (mots-clés tirés d'un résumé de référence, actes de dialogue), puis affinement par apprentissage par renforcement (RL) avec une fonction de récompense (ROUGE/BLEU en synthèse). Le LLM cible reste gelé. Chiffres rapportés : +4 % à +13 % sur un sous-ensemble de 4 000 échantillons de CNN/Daily Mail (synthèse), surpassant des modèles entièrement supervisés ; +41,4 % sur MultiWOZ avec seulement 80 dialogues (génération de dialogue, devant ChatGPT, Codex, InstructGPT). Avantages cités : utilisation optimisée des ressources, attention ciblée. Inconvénients : dépendance à des stimuli précis, complexité de configuration, généralisation limitée.

## Tradeoff / insight pour un senior
L'astuce architecturale : déplacer l'optimisation du LLM coûteux (impossible en boîte noire) vers un policy model bon marché. On obtient un contrôle par instance sans gradient sur le gros modèle. Coût : un pipeline SFT+RL à entraîner et maintenir, et une fragilité aux changements de domaine — le policy model ne généralise pas au-delà de sa distribution d'entraînement.

## Source primaire
Voir Li et al. 2023, « Guiding Large Language Models via Directional Stimulus Prompting ». N'invente aucun arXiv.

## Voir aussi
- [Optimisation des prompts](prompt-optimization.md)
- [tool grounding](tool-grounding.md)
