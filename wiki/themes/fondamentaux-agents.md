---
type: index
titre: "Thème — Fondamentaux des agents"
theme: fondamentaux-agents
---

# 🧱 Fondamentaux des agents

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Ce qu'est un agent, ses composants et ses limites structurelles._

## Concepts (14)

### 🔴 Substance / cœur
- **[ACI : concevoir l'interface agent-ordinateur](../fiches/aci-agent-computer-interface.md)** — soigner la définition des outils (noms, descriptions, formats) avec autant d'attention que les prompts : l'interface agent-ordinateur (ACI) est, pour un agent, l'équivalent de l'IHM pour un humain.
- **[Les 5 patterns de workflow composables (Anthropic)](../fiches/patterns-de-workflow.md)** — un catalogue de patterns composables, du plus simple au plus complexe, à assembler soi-même plutôt qu'à déléguer à un framework.
- **[Modèles de langage augmentés (taxonomie de Weng)](../fiches/augmented-language-models.md)** — la généalogie sourcée des agents tool-using : avant le « function calling » packagé, trois familles de techniques (récupération, exécution de code, appels d'API) augmentaient déjà un LLM gelé via le seul prompt.
- **[Taxonomie des erreurs d'appel de fonction](../fiches/taxonomie-erreurs-appel-fonction.md)** — une grille concrète pour évaluer le tool-calling : cinq erreurs détectables par règles déterministes, plus deux contrôles sémantiques délégués à un LLM-juge.
- **[Workflows vs agents : la distinction architecturale d'Anthropic](../fiches/workflows-vs-agents.md)** — distinguer **workflows** (LLM et outils orchestrés par des chemins de code prédéfinis) et **agents** (le LLM dirige dynamiquement son propre processus), au lieu de tout appeler « agentique ».

### 🟡 Tradeoff / intermédiaire
- **[Architecture BDI (Belief-Desire-Intention)](../fiches/bdi.md)** — un découpage du raisonnement de l'agent en trois registres (ce qu'il sait, ce qu'il veut, ce qu'il décide de faire), antérieur aux LLM.
- **[Architectures verticale / horizontale / hybride](../fiches/archi-vertical-horizontal-hybride.md)** — les trois topologies d'un système multi-agents : chef centralisé, pairs égaux, ou mélange des deux selon la phase.
- **[Deep Agents (pattern)](../fiches/deep-agents.md)** — patron d'architecture d'agent pour les tâches **long-horizon** : au lieu d'une simple boucle « réfléchir → appeler un outil → observer », on combine **planification explicite + sous-agents à contexte isolé + système de fichiers comme mémoire externe + prompt système détaillé** pour tenir la distance sans saturer le contexte.
- **[Limites structurelles des agents LLM (selon Weng)](../fiches/agent-limites-weng.md)** — les trois limites communes que Weng identifie après avoir parcouru les démonstrateurs d'agents : contexte fini, planification long-horizon fragile, et interface en langage naturel peu fiable.

### 🟢 Survol / introductif
- **[Agent apprenant (modèle AIMA)](../fiches/agent-apprenant.md)** — un agent qui se décompose en quatre rôles internes pour boucler sur ses propres erreurs et s'améliorer dans le temps.
- **[AutoGPT](../fiches/autogpt.md)** — le démonstrateur de 2023 qui décompose un objectif de haut niveau en sous-tâches et tourne en boucle création/priorisation/exécution avec mémoire vectorielle ; surtout une valeur historique.
- **[BabyAGI](../fiches/babyagi.md)** — la boucle minimale de 2023 (Yohei Nakajima) à trois agents — exécution, création, priorisation — adossée à une mémoire vectorielle ; un « bac à sable éducatif » plus qu'un outil de production.
- **[Logique conditionnelle & heuristique](../fiches/logique-conditionnelle-heuristique.md)** — du raisonnement câblé : des règles si-alors et des scores/fonctions d'utilité codés en dur dans la boucle de décision, sans apprentissage.
- **[Taxonomie des 5 types d'agents](../fiches/taxonomie-5-types-agents.md)** — l'échelle de sophistication classique des agents, du `if/then` câblé jusqu'à l'agent qui s'améliore par feedback.

## Outils (1)

- **[deepagents (Deep Agents)](../fiches%20outils/deepagents.md)** — _Bibliothèque Python (+ JS/TS) — harness d'agents_
