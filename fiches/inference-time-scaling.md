---
titre: "Modèles de raisonnement & test-time compute"
type: "Concept"
theme: raisonnement-planification
niveau: 🔴
source_url: https://arxiv.org/abs/2501.12948
---

# Modèles de raisonnement & test-time compute

**En une phrase** — gagner en qualité en laissant le modèle « penser plus longtemps » à l'inférence plutôt qu'en grossissant ses poids.

## L'idée
L'axe d'échelle classique était la taille du modèle et des données d'entraînement. L'*inference-time scaling* déplace le budget de calcul vers l'**inférence** : le modèle produit de longues chaînes de raisonnement internes, explore plusieurs pistes, se corrige, avant de répondre. Les modèles de raisonnement (o1/o3 chez OpenAI, DeepSeek-R1) sont entraînés par renforcement à exploiter ce budget. Snell et al. montrent qu'à budget donné, dépenser au test-time peut surpasser un modèle bien plus gros.

## Exemple
DeepSeek-R1-Zero, entraîné par pur RL sans SFT, voit son pass@1 sur AIME 2024 grimper de 15,6 % à 71,0 % au fil de l'entraînement (86,7 % en vote majoritaire sur 64 échantillons, au niveau d'o1-0912). La longueur des chaînes de raisonnement croît spontanément de quelques centaines à plusieurs milliers de tokens, et un « aha moment » émerge : à mi-résolution le modèle s'interrompt par « Wait, wait. Wait. That's an aha moment » avant de réévaluer son approche. DeepSeek-R1 final atteint 97,3 % sur MATH-500 et un rating Codeforces de 2 029 (top 3,7 % humains).

## Tradeoff / quand l'utiliser
Précieux sur les tâches à raisonnement profond (maths, code, planification) où une réponse juste vaut le surcoût. Inconvénient : **latence et coût par requête** bien plus élevés, sortie verbeuse, gains faibles sur les tâches simples. Les modèles de raisonnement représentent une évolution postérieure aux approches classiques de prompting.

## Source primaire
OpenAI, 2024, *o1* (annonce produit) ; DeepSeek-AI, 2025, *DeepSeek-R1*, arXiv:2501.12948 *(arXiv vérifié — HTTP 200 + titre)* ; Snell et al., 2024, *Scaling LLM Test-Time Compute Optimally*, arXiv:2408.03314 *(arXiv vérifié — HTTP 200 + titre)*.

## Voir aussi
- [process-reward-models](process-reward-models.md)
- [react](react.md)
