---
titre: "Mixture-of-Agents (MoA)"
theme: multi-agents
niveau: 🔴
source_url: https://arxiv.org/abs/2406.04692
---

# Mixture-of-Agents (MoA)

**En une phrase** — empiler **plusieurs LLM en couches** : chaque couche d'agents reçoit et agrège les réponses de la couche précédente, améliorant la qualité au-delà du meilleur modèle isolé.

## L'idée
MoA organise plusieurs modèles en couches successives. À chaque couche, des agents « proposers » génèrent des réponses ; la couche suivante les reçoit toutes en entrée, les agrège et les raffine, jusqu'à un agent « aggregator » final. La collaboration inter-modèles exploite la complémentarité de LLM hétérogènes : le collectif dépasse le meilleur modèle pris seul, y compris sur des benchmarks comme AlpacaEval. C'est une généralisation en profondeur du débat multi-agents.

## Tradeoff / quand l'utiliser
Pertinent quand la **qualité prime sur le coût** et qu'on dispose de plusieurs modèles complémentaires. Coût : latence et nombre d'appels multipliés par le nombre de couches et d'agents par couche. Inutile pour du débit ou des tâches simples ; on lui préfère alors un appel unique.

## Source primaire
Wang et al., 2024, *Mixture-of-Agents Enhances Large Language Model Capabilities*, arXiv:2406.04692 (Together AI). *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [society-of-mind-debate](society-of-mind-debate.md)
- [strategies-collaboration](strategies-collaboration.md)
