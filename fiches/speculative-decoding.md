---
titre: "Speculative decoding"
type: "Concept"
theme: efficacite-cout
niveau: 🟡
source_url: https://arxiv.org/abs/2211.17192
---

# Speculative decoding

**En une phrase** — un petit modèle « brouillon » propose plusieurs tokens, le gros modèle les VÉRIFIE en un pass ; accélère l'inférence sans changer la distribution de sortie.

## L'idée
La génération autoregressive est séquentielle : un token par pass du gros modèle, donc lente. Le *speculative decoding* fait proposer par un petit modèle **draft** une rafale de k tokens candidats, que le gros modèle **cible** valide en un seul pass parallèle. Un test d'acceptation probabiliste accepte le plus long préfixe cohérent et rejette le reste. Garantie clé : la distribution de sortie reste **exactement** celle du gros modèle seul — c'est de l'accélération, pas une approximation.

## Tradeoff / quand l'utiliser
Accélère la latence (souvent 2-3×) sans toucher à la qualité. Le gain dépend du **taux d'acceptation** : il faut un draft suffisamment aligné sur la cible, sinon les rejets annulent le bénéfice. Coûte de la mémoire (deux modèles) et de la complexité d'implémentation ; transparent côté utilisateur, c'est un levier d'infrastructure d'inférence.

## Source primaire
Leviathan et al., 2023, *Fast Inference from Transformers via Speculative Decoding*, arXiv:2211.17192 *(arXiv vérifié — HTTP 200 + titre)* ; Chen et al., 2023, *Accelerating Large Language Model Decoding with Speculative Sampling* (DeepMind).

## Voir aussi
- [model-routing-cascades](model-routing-cascades.md)
- [inference-time-scaling](inference-time-scaling.md)
