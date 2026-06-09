---
titre: "Constitutional AI & RLAIF"
theme: gouvernance-alignement-ops
niveau: 🔴
source_url: https://arxiv.org/abs/2212.08073
---

# Constitutional AI & RLAIF

**En une phrase** — aligner un modèle via un ensemble de **principes écrits** : le modèle critique et révise ses propres sorties selon la « constitution », et l'on entraîne sur ce feedback IA (RLAIF) au lieu d'annotations humaines (RLHF).

## L'idée
Constitutional AI remplace une partie du jugement humain par une **constitution** : une liste de principes explicites. Le modèle génère une réponse, la critique au regard d'un principe, puis la révise — produisant des paires d'entraînement sans annotateur. Cette phase de feedback IA, **RLAIF** (Reinforcement Learning from AI Feedback), entraîne le modèle de préférence à partir des comparaisons faites par un LLM plutôt que par des humains, réduisant le coût et rendant les critères d'alignement auditables.

## Tradeoff / quand l'utiliser
Utile pour aligner à grande échelle et **rendre les règles explicites et révisables** (un texte vs des préférences implicites). Coût : la qualité dépend entièrement de la constitution et du modèle critique ; un principe mal formulé ou un biais du juge se propage à tout l'entraînement.

## Source primaire
Bai et al., 2022, *Constitutional AI: Harmlessness from AI Feedback*, arXiv:2212.08073 (Anthropic). Voir aussi Lee et al., 2023, *RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback*. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [society-of-mind-debate](society-of-mind-debate.md)
- [ethique-gouvernance](ethique-gouvernance.md)
