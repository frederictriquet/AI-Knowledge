# DeepSeek-R1 : le RL fait émerger le raisonnement

> Fiche **source : DeepSeek-AI, « DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning », 2025** · [papier](../md/deepseek-r1.md) · Pertinence 🔴 substance

**En une phrase** — Appliqué directement à un modèle de base, le renforcement (RL) sans fine-tuning supervisé suffit à faire émerger spontanément de longues chaînes de raisonnement et l'auto-vérification.

## Ce que dit la source
Les auteurs introduisent DeepSeek-R1-Zero, entraîné par RL à grande échelle directement sur DeepSeek-V3-Base, sans aucune étape de fine-tuning supervisé (SFT) préalable. À travers le RL, le modèle « émerge » naturellement avec des comportements de raisonnement puissants — auto-vérification, réflexion (revisiter et réévaluer ses propres étapes), génération de longues chaînes de pensée (CoT). C'est la première recherche ouverte à valider que les capacités de raisonnement d'un LLM peuvent être incitées purement par RL. R1-Zero souffre toutefois de lisibilité médiocre et de mélange de langues ; les auteurs introduisent alors DeepSeek-R1, qui ajoute un peu de données de « cold start » et un pipeline multi-étapes pour atteindre des performances comparables à OpenAI-o1-1217. Sur AIME 2024, le pass@1 de R1-Zero passe de 15,6 % à 71,0 % au fil de l'entraînement (86,7 % avec vote majoritaire).

## Ce que ça ajoute vs IBM
Le guide IBM est resté « pré-reasoning-models » : il décrit des agents qui appellent un LLM figé via du prompting et de l'orchestration, sans notion de modèles dont la capacité de raisonnement est elle-même *entraînée* par RL. DeepSeek-R1 montre que le raisonnement n'est pas qu'une affaire de prompt (chain-of-thought sollicitée) mais peut être un comportement appris, mesurable et transférable. Pour une équipe construisant des agents, cela change le socle : on peut désormais s'appuyer sur des modèles de raisonnement (et leurs versions distillées open-source) plutôt que de tout reconstruire au niveau de l'orchestration.

## Points clés
- **Recette R1-Zero** : RL pur appliqué au modèle de base, sans SFT — preuve que le raisonnement s'incite par incitation, pas par imitation.
- **GRPO** (Group Relative Policy Optimization) : algorithme RL qui abandonne le critic (modèle de même taille que la policy) et estime la baseline à partir des scores d'un groupe d'échantillons, ce qui réduit le coût.
- **Récompense à base de règles** : récompense de justesse (vérification déterministe : réponse encadrée pour les maths, compilateur/tests pour le code) + récompense de format (balises `<think>`/`</think>`). Pas de reward model neuronal, pour éviter le reward hacking.
- **Auto-évolution** : le temps de réflexion (longueur des réponses) augmente naturellement pendant l'entraînement ; la réflexion et l'exploration d'approches alternatives émergent sans être programmées.
- **« Aha moment »** : à une version intermédiaire, le modèle apprend à réallouer du temps de réflexion en réévaluant son approche initiale — illustration directe de comportements sophistiqués émergeant du RL.
- **Distillation** : distiller le raisonnement de R1 vers des modèles denses plus petits (1.5B → 70B, Qwen2.5/Llama3) surpasse l'application du RL directement sur ces petits modèles. R1-Distill-Qwen-32B atteint 72,6 % sur AIME 2024.

## Voir aussi
- (Weng) [Test-time compute](../../lilian-weng/concepts/test-time-compute-thinking.md)
- (agents IBM hors-corpus) [Modèles de raisonnement](../../../ibm-guide-agents-ia/concepts/hors-corpus/inference-time-scaling.md)
- [Process Reward Models](process-reward-models.md)
- [papier](../md/deepseek-r1.md)
