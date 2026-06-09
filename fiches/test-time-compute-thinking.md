---
titre: "Test-time compute : « penser » comme du calcul à l'inférence"
theme: raisonnement-planification
niveau: 🔴
provenance: 🔗
base: sources/lilian-weng
source_url: https://lilianweng.github.io/posts/2025-05-01-thinking/
source_titre: "Why We Think"
---

# Test-time compute : « penser » comme du calcul à l'inférence

> Fiche **source : Lilian Weng** · [post complet](../sources/lilian-weng/md/2025-05-01-thinking.md) · Pertinence 🔴 substance

**En une phrase** — « penser » n'est pas une métaphore : c'est allouer davantage de FLOPs à l'inférence, le chain-of-thought permettant d'utiliser une quantité de calcul variable selon la difficulté du problème.

## Ce que dit la source
Weng cadre le raisonnement par trois motivations : l'analogie psychologique (Système 1 / Système 2 de Kahneman), le **calcul comme ressource** (en Transformer, ~2× le nombre de paramètres par token ; le CoT démultiplie ce calcul par token de réponse) et la modélisation à variable latente (la trace de pensée z comme variable cachée). Elle distingue au décodage le **parallel sampling** (best-of-N, beam search, self-consistency, guidés par un Process Reward Model) et la **sequential revision** (auto-correction itérative, qui ne marche pas nativement sans feedback externe — Huang et al. 2024). Côté entraînement, le **RL pour le raisonnement** culmine avec o1/o3 et le rapport DeepSeek-R1 (2025), où un simple policy gradient à récompenses règles (format + exactitude) fait émerger réflexion et backtracking (« aha moment ») même en RL pur sans SFT ; l'équipe DeepSeek rapporte aussi l'échec des PRM et du MCTS. Weng couvre enfin le **raisonnement latent** (architectures récurrentes type Geiping et al. 2025, thinking/pause tokens, Quiet-STaR) et les lois d'échelle (Snell et al. 2024 : le test-time compute ne remplace pas un bon modèle de base sur les problèmes difficiles).

## Ce que ça ajoute vs IBM
Comble l'angle mort « pré-reasoning-models » d'IBM : pose le test-time compute comme nouvelle dimension de scaling et explicite la recette o1/R1 et ses échecs.

## Sources primaires (citées par Weng)
- DeepSeek-AI, *DeepSeek-R1* (2025)
- Wei et al., *Chain-of-thought prompting* (2022)
- Snell et al., *Scaling LLM Test-Time Compute Optimally* (2024)
- Lightman et al., *Let's Verify Step by Step* (PRM, 2023)
- Zelikman et al., *STaR: Bootstrapping Reasoning With Reasoning* (2022)

## Voir aussi
- (base agents) [Modèles de raisonnement & test-time compute (hors-corpus)](inference-time-scaling.md) · [Process Reward Models (hors-corpus)](process-reward-models.md)
- (base prompting) [Chain-of-Thought](chain-of-thought.md)
- [post complet](../sources/lilian-weng/md/2025-05-01-thinking.md)
