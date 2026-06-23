---
titre: "Toolformer"
type: "Concept"
theme: outils-function-calling
niveau: 🔴
source_url: https://arxiv.org/abs/2302.04761
---

# Toolformer

**En une phrase** — un LLM *fine-tuné* pour décider seul quand et comment appeler un outil, sans exemples few-shot ni prompt d'orchestration.

## L'idée
Au lieu d'apprendre l'usage d'outils par prompting (ReAct, function calling), Toolformer l'apprend par **auto-supervision** : on laisse le modèle insérer des appels d'API candidats dans un grand corpus, on exécute ces appels, et on **ne garde dans les données d'entraînement que les appels qui réduisent la perplexité** de la suite. Le modèle internalise ainsi quand un outil (calculatrice, recherche, traduction, calendrier) aide réellement.

## Tradeoff / quand l'utiliser
Approche par **entraînement**, pas par prompting — pertinente si tu *construis/affines* un modèle, pas si tu consommes une API. Avantage : décision d'outil native, sans prompt d'orchestration. Inconvénient : coûteux (génération de données + fine-tuning), figé au jeu d'outils vu à l'entraînement. En pratique, le function calling natif des API récentes a rendu cette voie moins nécessaire pour la plupart des usages applicatifs.

## Source primaire
Schick et al., 2023, *Toolformer: Language Models Can Teach Themselves to Use Tools*, arXiv:2302.04761 (Meta AI). *(arXiv vérifié — HTTP 200 + titre)*

## Voir aussi
- [tool-calling](tool-calling.md)
- [react](react.md)
