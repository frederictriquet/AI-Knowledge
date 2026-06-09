# CodeAct (le code comme espace d'action)

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. [Glossaire](../../GLOSSAIRE-PATTERNS.md) · Pertinence 🔴 substance

**En une phrase** — l'agent émet du **code Python exécutable** comme action, au lieu d'appels d'outils en JSON rigide.

## L'idée
Dans le function calling classique, chaque action est un appel structuré (nom + arguments JSON), un par tour. CodeAct unifie l'espace d'action en une seule abstraction : **du code**. L'agent écrit un extrait Python qui peut enchaîner plusieurs outils, utiliser des boucles, des conditions, des variables intermédiaires et composer les résultats, puis l'environnement l'exécute et renvoie la sortie (y compris les erreurs) pour la prochaine itération. Wang et al. montrent que ce format améliore le taux de réussite par rapport au JSON, car il exploite la familiarité massive des LLM avec le code.

## Tradeoff / quand l'utiliser
Idéal pour des tâches multi-outils où la **composition** compte (data, orchestration). Contrepartie : exiger un **interpréteur sandboxé** et gérer le risque d'exécution de code arbitraire ; debug et garde-fous plus lourds que le JSON contraint.

## Source primaire
Wang et al., 2024, *Executable Code Actions Elicit Better LLM Agents*, arXiv:2402.01030 *(arXiv vérifié — HTTP 200 + titre)*.

## Voir aussi
- [computer-use-gui-agents](computer-use-gui-agents.md) (hors-corpus sœur)
- [tool-calling](../tool-calling.md) (corpus)
