---
titre: "Modèles de raisonnement & test-time compute"
theme: raisonnement-planification
niveau: 🔴
provenance: ➕
base: ibm-guide-agents-ia/hors-corpus
source_url: https://arxiv.org/abs/2501.12948
---

# Modèles de raisonnement & test-time compute

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. Glossaire · Pertinence 🔴 substance

**En une phrase** — gagner en qualité en laissant le modèle « penser plus longtemps » à l'inférence plutôt qu'en grossissant ses poids.

## L'idée
L'axe d'échelle classique était la taille du modèle et des données d'entraînement. L'*inference-time scaling* déplace le budget de calcul vers l'**inférence** : le modèle produit de longues chaînes de raisonnement internes, explore plusieurs pistes, se corrige, avant de répondre. Les modèles de raisonnement (o1/o3 chez OpenAI, DeepSeek-R1) sont entraînés par renforcement à exploiter ce budget. Snell et al. montrent qu'à budget donné, dépenser au test-time peut surpasser un modèle bien plus gros.

## Tradeoff / quand l'utiliser
Précieux sur les tâches à raisonnement profond (maths, code, planification) où une réponse juste vaut le surcoût. Inconvénient : **latence et coût par requête** bien plus élevés, sortie verbeuse, gains faibles sur les tâches simples. C'est un angle mort du corpus, resté pré-reasoning-models.

## Source primaire
OpenAI, 2024, *o1* (annonce produit) ; DeepSeek-AI, 2025, *DeepSeek-R1*, arXiv:2501.12948 *(arXiv vérifié — HTTP 200 + titre)* ; Snell et al., 2024, *Scaling LLM Test-Time Compute Optimally*, arXiv:2408.03314 *(arXiv vérifié — HTTP 200 + titre)*.

## Voir aussi
- [process-reward-models](process-reward-models.md) (hors-corpus sœur)
- [react](react.md) (corpus)
