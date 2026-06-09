# Chain-of-Thought (CoT)

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [../md/18-agentic-reasoning.md](../md/18-agentic-reasoning.md), [../md/10-components-of-ai-agents.md](../md/10-components-of-ai-agents.md), [../md/28-react-agent.md](../md/28-react-agent.md)

**En une phrase** — on demande au modèle d'écrire son raisonnement intermédiaire avant de produire la réponse finale.

## Ce que dit le corpus
Le corpus décrit le « raisonnement en chaîne de pensées » comme le fait, pour un modèle d'IA générative ou un LLM, de générer des traces verbalisées de son processus de raisonnement (18). Le module de raisonnement d'un agent peut associer raisonnement en chaîne de pensée et techniques de résolution de problèmes multi-étapes, jugées indispensables pour des applications comme l'analyse financière automatisée ou l'examen de contrats (10). ReAct combine explicitement le raisonnement par chaîne de pensée (CoT) avec l'utilisation d'outils externes (28). Le corpus note aussi, citant l'article original sur ReAct, que le CoT seul apporte de nombreux avantages mais comporte un risque accru d'hallucination, atténué par l'ancrage externe (28).

## Tradeoff / insight pour un senior
Pur vocabulaire au niveau du corpus IBM : le CoT n'y est qu'une brique sous-jacente à ReAct, jamais traité comme technique autonome. L'insight non explicité par IBM mais connu de l'état de l'art : le CoT n'émerge réellement que sur les gros modèles ; sur petits modèles il dégrade souvent la réponse. Le corpus rappelle implicitement ce point en soulignant que ReAct « tire grandement parti de modèles hautement performants » (28).

## Source primaire
Non citée directement comme source CoT par IBM — voir Wei et al. 2022, « Chain-of-Thought Prompting Elicits Reasoning in Large Language Models » (hors-corpus). Le corpus cite l'article ReAct (arXiv, 10 mars 2023) qui s'appuie sur le CoT.

## Voir aussi
- [ReAct](react.md)
- [Tree of Thoughts (ToT)](tree-of-thoughts.md)
- (base prompt engineering) [Chain-of-Thought](../../ibm-guide-prompt-engineering/concepts/chain-of-thought.md)
