---
titre: "Step-Back prompting"
type: "Concept"
theme: raisonnement-planification
niveau: 🟡
source_url: https://arxiv.org/abs/2310.06117
---

# Step-Back prompting

**En une phrase** — avant de répondre à une question précise, on demande au modèle de « prendre du recul » pour formuler le concept ou le principe général sous-jacent, puis on raisonne à partir de cette abstraction.

## L'idée
Plutôt que d'attaquer directement le détail, Step-Back fait dériver une **question d'abstraction** : quel principe physique, quelle règle, quel concept de plus haut niveau gouverne ce cas ? Le modèle répond d'abord à cette question générale, puis utilise ce principe comme guide pour résoudre la question concrète. Cette abstraction réduit les erreurs de raisonnement causées par une focalisation prématurée sur des détails non pertinents.

## Tradeoff / quand l'utiliser
Gains sur le raisonnement scientifique, multi-étapes et les questions factuelles nécessitant un principe intermédiaire. Coût modeste : un appel supplémentaire pour l'abstraction. Efficace quand il existe un principe généralisable derrière le cas particulier ; inutile, voire contre-productif, sur des questions purement factuelles ou de lookup où aucune abstraction n'aide. Complémentaire de Least-to-Most : l'un abstrait vers le haut, l'autre décompose vers le bas.

## Source primaire
Zheng et al., 2023, *Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models*, arXiv:2310.06117. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [least-to-most](least-to-most.md)
- [chain-of-thought](chain-of-thought.md)
