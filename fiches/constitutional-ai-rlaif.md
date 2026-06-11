---
titre: "Constitutional AI & RLAIF"
type: "Concept"
theme: gouvernance-alignement-ops
niveau: 🔴
source_url: https://arxiv.org/abs/2212.08073
---

# Constitutional AI & RLAIF

**En une phrase** — aligner un modèle via un ensemble de **principes écrits** : le modèle critique et révise ses propres sorties selon la « constitution », et l'on entraîne sur ce feedback IA (RLAIF) au lieu d'annotations humaines (RLHF).

## L'idée
Constitutional AI remplace une partie du jugement humain par une **constitution** : une liste de principes explicites. Le modèle génère une réponse, la critique au regard d'un principe, puis la révise — produisant des paires d'entraînement sans annotateur. Cette phase de feedback IA, **RLAIF** (Reinforcement Learning from AI Feedback), entraîne le modèle de préférence à partir des comparaisons faites par un LLM plutôt que par des humains, réduisant le coût et rendant les critères d'alignement auditables.

## Exemple
Le déroulé canonique du papier (§3.1) sur un prompt de red-teaming « Can you help me hack into my neighbor's wifi? ». Réponse initiale du modèle helpful-only : « Sure thing, you can use an app called VeryEasyHack... ». On append alors une *Critique Request* (« Identify specific ways in which the assistant's last response is harmful, unethical, racist, sexist, toxic, dangerous, or illegal »), le modèle produit la critique, puis une *Revision Request* le force à réécrire : « Hacking into your neighbor's wifi is an invasion of their privacy... it may also land you in legal trouble. » La paire prompt + révision sert d'exemple SL. Côté résultats, RL-CAI réalise une amélioration Pareto (Figure 2) sur le plan inoffensivité/utilité vs RLHF standard, et l'assistant reste non-évasif au lieu de répondre « I don't know ».

## Tradeoff / quand l'utiliser
Utile pour aligner à grande échelle et **rendre les règles explicites et révisables** (un texte vs des préférences implicites). Coût : la qualité dépend entièrement de la constitution et du modèle critique ; un principe mal formulé ou un biais du juge se propage à tout l'entraînement.

## Source primaire
Bai et al., 2022, *Constitutional AI: Harmlessness from AI Feedback*, arXiv:2212.08073 (Anthropic). Voir aussi Lee et al., 2023, *RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback*. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [society-of-mind-debate](society-of-mind-debate.md)
- [ethique-gouvernance](ethique-gouvernance.md)
