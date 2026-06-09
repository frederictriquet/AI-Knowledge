---
titre: CodeAct (le code comme espace d'action)
theme: outils-function-calling
tags: [outils, code, agents]
niveau: 🔴
provenance: ➕
base: ibm-guide-agents-ia/hors-corpus
source_url: https://arxiv.org/abs/2402.01030
source_titre: "Executable Code Actions Elicit Better LLM Agents — Wang et al., 2024"
source_primaire: "PAL: Program-aided Language Models, Gao et al. (arXiv:2211.10435)"
---

# CodeAct (le code comme espace d'action)

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. Glossaire · Pertinence 🔴 substance

**En une phrase** — l'agent émet du **code Python exécutable** comme action, au lieu d'appels d'outils en JSON rigide.

## L'idée
Dans le function calling classique, chaque action est un appel structuré (nom + arguments JSON), un par tour. CodeAct unifie l'espace d'action en une seule abstraction : **du code**. L'agent écrit un extrait Python qui peut enchaîner plusieurs outils, utiliser des boucles, des conditions, des variables intermédiaires et composer les résultats, puis l'environnement l'exécute et renvoie la sortie (y compris les erreurs) pour la prochaine itération. Wang et al. montrent que ce format améliore le taux de réussite par rapport au JSON, car il exploite la familiarité massive des LLM avec le code.

## Tradeoff / quand l'utiliser
Idéal pour des tâches multi-outils où la **composition** compte (data, orchestration). Contrepartie : exiger un **interpréteur sandboxé** et gérer le risque d'exécution de code arbitraire ; debug et garde-fous plus lourds que le JSON contraint.

## Ancêtre — PAL (Program-Aided Language models)
Avant de faire du code l'**espace d'action** complet d'un agent, PAL (Gao et al., 2022) en avait posé le réflexe fondateur sur le seul raisonnement : sur les tâches arithmétiques/logiques, le LLM se trompe à l'**exécution** même quand le raisonnement est correct, donc on lui fait **traduire** le problème en programme (souvent Python) et on délègue le calcul à un **interpréteur** pour une réponse exacte. Variante quasi identique : Program of Thoughts (PoT, Chen et al., 2022). Principe transférable : dès qu'une étape est déterministe (maths, dates, manipulation de données), délègue-la à du code exécuté, pas au modèle. CodeAct généralise ce réflexe d'un sous-calcul ponctuel à l'**ensemble** des actions de l'agent.

## Source primaire
Wang et al., 2024, *Executable Code Actions Elicit Better LLM Agents*, arXiv:2402.01030 *(arXiv vérifié — HTTP 200 + titre)*. Ancêtre : Gao et al., 2022, *PAL: Program-aided Language Models*, arXiv:2211.10435 ; Chen et al., 2022, *Program of Thoughts (PoT)* *(arXiv vérifiés — HTTP 200 + titre)*.

## Voir aussi
- [computer-use-gui-agents](computer-use-gui-agents.md) (hors-corpus sœur)
- [tool-calling](tool-calling.md) (corpus)
- [tool-grounding](tool-grounding.md) (corpus)
- [chain-of-thought](chain-of-thought.md) (corpus)
