---
titre: ReAct
type: "Concept"
theme: raisonnement-planification
tags: [agents, outils, raisonnement]
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/react-agent
source_titre: "Qu'est-ce qu'un agent ReAct ? — IBM Think"
source_primaire: "Yao et al., ReAct: Synergizing Reasoning and Acting in Language Models (arXiv:2210.03629)"
---

# ReAct

**En une phrase** — une boucle pensée → action (appel d'outil) → observation, répétée jusqu'à obtenir une réponse.

## En détail
ReAct (« Reasoning and acting ») combine le raisonnement par chaîne de pensée (CoT) avec l'utilisation d'outils externes via une boucle entrelacée pensée/action/observation. L'agent génère une pensée, exécute une action (outil, API, recherche), observe le résultat, puis réinjecte cette observation dans la pensée suivante. La boucle se termine après un nombre max d'itérations ou lorsqu'une condition est remplie ; à noter que ReAct peut régénérer les mêmes raisonnements et actions, ce qui peut entraîner des boucles infinies. Le prompt système `ZERO_SHOT_REACT-DESCRIPTION` de LangGraph suit le format Question/Thought/Action/Observation/Final Answer. ReAct dépend fortement d'un LLM central performant en raisonnement et suivi d'instructions.

## Tradeoff / insight pour un senior
Face à des tâches simples/prévisibles, l'appel de fonction est plus rapide, économe en tokens et plus simple ; ReAct ne se justifie que pour le raisonnement complexe ou imprévisible, où la traçabilité étape par étape et l'adaptabilité dynamique valent le surcoût de tokens et le risque de boucle.

## Source primaire
Yao et al., « ReAct: Synergizing Reasoning and Acting in Language Models », arXiv:2210.03629 (10 mars 2023).

## Voir aussi
- [ReWOO](rewoo.md)
- [Autoréflexion / Reflexion](reflexion.md)
- [Chain-of-Thought (CoT)](chain-of-thought.md)
