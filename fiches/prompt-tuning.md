---
titre: "Prompt tuning (soft prompts)"
theme: prompting
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/prompt-tuning
source_titre: "Qu’est-ce que l’optimisation des prompts ?"
---

# Prompt tuning (soft prompts)

**En une phrase** — méthode PEFT qui entraîne par descente de gradient un petit jeu de vecteurs continus (« soft prompts » / tokens virtuels) injectés en entrée, le backbone restant gelé — à ne pas confondre avec le prompt engineering textuel.

## En détail
Le prompt tuning adapte un modèle pré-entraîné gelé en apprenant quelques vecteurs entraînables (soft prompts), non interprétables, qui guident le comportement sans toucher aux poids. Seuls ces paramètres (souvent < 1 % du modèle) sont mis à jour par rétropropagation, d'où des coûts de calcul et de stockage drastiquement réduits et une modularité « plug-and-play » (un fichier de prompts par tâche). Le comparatif PEFT classe le P-tuning v2 (~0,1-3 % des paramètres) comme moins expressif que LoRA (~0,1-1 %) ou les adaptateurs (~1-4 %). Limite expressive centrale : une analyse formelle montre que prompt/prefix-tuning n'ajoute qu'un biais à la sortie des blocs d'attention et ne modifie pas les patterns d'attention appris — il combine des compétences existantes mais n'apprend pas de tâches véritablement nouvelles. L'efficacité dépend de l'échelle : compétitif avec le réglage fin intégral au-delà de 10 milliards de paramètres. Sur Granite 3-8B en classification d'avis, le prompt tuning obtient ~98 % de précision contre ~93 % pour le modèle de base, soit ~+5 %.

## Tradeoff / insight pour un senior
Le piège est de croire que « tuner le prompt » apprend de nouvelles capacités : non, le soft prompt ne fait que ré-éliciter et combiner ce que le backbone sait déjà. Pour des patterns de raisonnement réellement inédits, il faut LoRA ou un fine-tuning intégral. Côté ops, le soft prompt pèse quelques Ko contre 350 Go pour une copie complète d'un modèle de 175 Md — la modularité est l'argument décisif, pas la performance brute.

## Réserves
L'analyse formelle de la limite expressive et les chiffres PEFT (P-tuning v2, LoRA, adaptateurs) ne disposent pas de référence arXiv reproductible.

## Voir aussi
- [in-context-learning](in-context-learning.md)
- [rag-vs-fine-tuning-vs-prompt-engineering](rag-vs-fine-tuning-vs-prompt-engineering.md)
