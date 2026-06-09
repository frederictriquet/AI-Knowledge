# ReAct

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [../md/18-agentic-reasoning.md](../md/18-agentic-reasoning.md), [../md/28-react-agent.md](../md/28-react-agent.md), [../md/17-ai-agent-planning.md](../md/17-ai-agent-planning.md)

**En une phrase** — une boucle pensée → action (appel d'outil) → observation, répétée jusqu'à obtenir une réponse.

## Ce que dit le corpus
ReAct (« Reasoning and acting ») combine le raisonnement par chaîne de pensée (CoT) avec l'utilisation d'outils externes via une boucle entrelacée pensée/action/observation (18, 28). L'agent génère une pensée, exécute une action (outil, API, recherche), observe le résultat, puis réinjecte cette observation dans la pensée suivante (28). La boucle se termine après un nombre max d'itérations ou lorsqu'une condition est remplie ; le corpus avertit que ReAct peut régénérer les mêmes raisonnements et actions, ce qui peut entraîner des boucles infinies (18). Le fichier 28 fournit le prompt système `ZERO_SHOT_REACT-DESCRIPTION` de LangGraph (format Question/Thought/Action/Observation/Final Answer). ReAct dépend fortement d'un LLM central performant en raisonnement et suivi d'instructions (28).

## Tradeoff / insight pour un senior
Le compromis explicité par le corpus (28) : face à des tâches simples/prévisibles, l'appel de fonction est plus rapide, économe en tokens et plus simple ; ReAct ne se justifie que pour le raisonnement complexe ou imprévisible, où la traçabilité étape par étape et l'adaptabilité dynamique valent le surcoût de tokens et le risque de boucle.

## Source primaire
Citée par IBM : Yao et al., « ReAct: Synergizing Reasoning and Acting in Language Models », arXiv:2210.03629 (référencée par le corpus comme arXiv, 10 mars 2023).

## Voir aussi
- [ReWOO](rewoo.md)
- [Autoréflexion / Reflexion](reflexion.md)
- [Chain-of-Thought (CoT)](chain-of-thought.md)
