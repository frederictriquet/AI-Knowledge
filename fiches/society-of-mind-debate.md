---
titre: "Multi-agent debate / Society of Mind"
type: "Concept"
theme: multi-agents
niveau: 🔴
source_url: https://arxiv.org/abs/2305.14325
---

# Multi-agent debate / Society of Mind

**En une phrase** — faire **débattre plusieurs instances de LLM** : chacune propose une réponse, critique celles des autres sur plusieurs tours, jusqu'à converger vers une réponse plus factuelle.

## L'idée
Plutôt qu'un seul modèle (faillible), N agents génèrent des réponses indépendantes puis itèrent en lisant et en critiquant les propositions des pairs. La confrontation fait émerger les erreurs et améliore factualité et raisonnement. Le nom évoque la *Society of Mind* de Minsky (intelligence émergente d'agents simples) ; l'instanciation moderne sur LLM est le « multiagent debate ».

## Exemple
Setup du papier : **3 agents**, **2 tours** de débat (chaque agent relit les réponses des autres et révise). Gains mesurés : arithmétique 67,0 → **81,8 %**, GSM8K 77,0 → **85,0 %**, génération de biographies 66,0 → **73,8 %**, MMLU 63,9 → **71,1 %**, validité des coups d'échecs 29,3 → **45,2 %**. Fait notable : le débat corrige parfois des cas où *tous* les agents partaient sur une réponse fausse — ce n'est pas une simple amplification du consensus initial, la population converge vers une réponse commune plus juste.

## Tradeoff / quand l'utiliser
Améliore factualité et raisonnement sur certaines tâches, mais **coûteux** (N agents × plusieurs tours). C'est l'ancêtre conceptuel des « panels de juges » et de la vérification adversariale. À réserver aux questions à fort enjeu de justesse, pas au débit.

## Source primaire
Du et al., 2023, *Improving Factuality and Reasoning in Language Models through Multiagent Debate*, arXiv:2305.14325. Concept fondateur : Minsky, *The Society of Mind*, 1986. *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [strategies-collaboration](strategies-collaboration.md)
- [llm-as-a-judge](llm-as-a-judge.md)
