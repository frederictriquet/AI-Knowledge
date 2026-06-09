# Tree of Thoughts (ToT)

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🔴 substance · Provenance ✅ présent · Sources corpus : [../md/18-agentic-reasoning.md](../md/18-agentic-reasoning.md), [../md/10-components-of-ai-agents.md](../md/10-components-of-ai-agents.md)

**En une phrase** — généraliser le Chain-of-Thought en arbre : explorer plusieurs branches de raisonnement, évaluer, élaguer et backtracker plutôt que suivre une seule chaîne linéaire.

## Ce que dit le corpus
Le corpus ne traite pas ToT comme un concept à part entière : il l'évoque uniquement par analogie. Le fichier 18 indique que LATS « partage des similitudes avec le raisonnement par arbre de pensées dans les LLM », sans définir ce raisonnement par arbre. Le fichier 10 décrit plus largement le module de raisonnement comme cherchant à « évaluer différents chemins de solution » et à associer raisonnement en chaîne de pensée et techniques de résolution multi-étapes, ce qui constitue le terrain conceptuel du ToT sans le nommer. Aucun chiffre, benchmark ni détail d'algorithme (exploration, élagage, backtracking) n'est fourni dans le corpus pour ToT.

## Tradeoff / insight pour un senior
ToT remplace la chaîne unique du CoT par une recherche arborescente avec évaluation des nœuds : meilleure couverture des problèmes à forte combinatoire (puzzles, planification) mais coût en appels LLM qui croît avec la largeur et la profondeur de l'arbre. Dans ce corpus, ToT n'est qu'une référence d'arrière-plan derrière LATS ; l'essentiel de la substance vient de l'état de l'art, pas d'IBM.

## Source primaire
Non citée par IBM (nommée sans référence) — voir Yao et al. 2023, « Tree of Thoughts: Deliberate Problem Solving with Large Language Models » (hors-corpus).

## Voir aussi
- [Chain-of-Thought (CoT)](chain-of-thought.md)
- [LATS (Language Agent Tree Search)](lats.md)
- (base prompt engineering) [Tree of Thoughts](../../ibm-guide-prompt-engineering/concepts/tree-of-thoughts.md)
