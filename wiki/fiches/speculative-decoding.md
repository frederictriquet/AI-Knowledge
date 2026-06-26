---
titre: "Speculative decoding"
type: "Concept"
theme: efficacite-cout
niveau: 🟡
source_url: https://arxiv.org/abs/2211.17192
objectifs: [couts]
---

# Speculative decoding

**En une phrase** — un petit modèle « brouillon » propose plusieurs tokens, le gros modèle les VÉRIFIE en un pass ; accélère l'inférence sans changer la distribution de sortie.

## L'idée
La génération autoregressive est séquentielle : un token par pass du gros modèle, donc lente. Le *speculative decoding* fait proposer par un petit modèle **draft** une rafale de k tokens candidats, que le gros modèle **cible** valide en un seul pass parallèle. Un test d'acceptation probabiliste accepte le plus long préfixe cohérent et rejette le reste. Garantie clé : la distribution de sortie reste **exactement** celle du gros modèle seul — c'est de l'accélération, pas une approximation.

## Exemple
Mesures du papier (Table 2) avec **T5-small (77M)** comme draft et **T5-XXL (11B)** comme cible. Traduction WMT EnDe en argmax (T=0) : **3,4×** d'accélération, γ=7 tokens proposés par pass, taux d'acceptation α=0,75 ; en sampling (T=1) le gain retombe à 2,6× car α=0,62. Résumé CNN/DM : 3,1× (γ=5, α=0,65) en argmax, 2,3× en sampling. Le speedup suit directement α : un draft mal aligné fait chuter le gain malgré le parallélisme.

## Tradeoff / quand l'utiliser
Accélère la latence (souvent 2-3×) sans toucher à la qualité. Le gain dépend du **taux d'acceptation** : il faut un draft suffisamment aligné sur la cible, sinon les rejets annulent le bénéfice. Coûte de la mémoire (deux modèles) et de la complexité d'implémentation ; transparent côté utilisateur, c'est un levier d'infrastructure d'inférence.

## Source primaire
Leviathan et al., 2023, *Fast Inference from Transformers via Speculative Decoding*, arXiv:2211.17192 *(arXiv vérifié — HTTP 200 + titre)* ; Chen et al., 2023, *Accelerating Large Language Model Decoding with Speculative Sampling* (DeepMind).

## Voir aussi
- [model-routing-cascades](model-routing-cascades.md)
- [inference-time-scaling](inference-time-scaling.md)
