---
type: index
titre: "MOC — Raisonnement & planification"
theme: raisonnement-planification
---

# 🧠 Raisonnement & planification

> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.

_Faire raisonner, planifier et s'auto-corriger un modèle._

## Concepts (22)

### 🔴 Substance / cœur
- **[Auto-réflexion des agents (ReAct, Reflexion, CoH, AD)](../fiches/self-reflection-agents.md)** — la famille des mécanismes par lesquels un agent s'améliore en boucle en revenant sur ses décisions et erreurs passées, indispensables dans les tâches réelles où l'essai-erreur est inévitable.
- **[DeepSeek-R1 : le RL fait émerger le raisonnement](../fiches/deepseek-r1-rl-raisonnement.md)** — Appliqué directement à un modèle de base, le renforcement (RL) sans fine-tuning supervisé suffit à faire émerger spontanément de longues chaînes de raisonnement et l'auto-vérification.
- **[Graph of Thoughts (GoT)](../fiches/graph-of-thoughts.md)** — on modélise le raisonnement comme un graphe arbitraire de pensées où l'on peut non seulement ramifier, mais aussi **fusionner** plusieurs pensées, boucler et raffiner, là où Tree-of-Thoughts se limite à un arbre.
- **[LATS (Language Agent Tree Search)](../fiches/lats.md)** — appliquer la recherche arborescente Monte Carlo (MCTS) au raisonnement d'un agent LLM, en mémorisant les autoréflexions pour guider l'exploration.
- **[Modèles de raisonnement & test-time compute](../fiches/inference-time-scaling.md)** — gagner en qualité en laissant le modèle « penser plus longtemps » à l'inférence plutôt qu'en grossissant ses poids.
- **[Process Reward Models (Let's Verify Step by Step)](../fiches/process-reward-models.md)** — Récompenser chaque étape intermédiaire du raisonnement (supervision de processus) entraîne des modèles nettement plus fiables que récompenser seulement la réponse finale (supervision de résultat).
- **[Test-time compute : « penser » comme du calcul à l'inférence](../fiches/test-time-compute-thinking.md)** — « penser » n'est pas une métaphore : c'est allouer davantage de FLOPs à l'inférence, le chain-of-thought permettant d'utiliser une quantité de calcul variable selon la difficulté du problème.
- **[Tree of Thoughts (ToT)](../fiches/tree-of-thoughts.md)** — généraliser la CoT en arbre : générer plusieurs « pensées » par étape, les évaluer, et explorer l'espace de solutions par recherche (BFS/DFS) avec backtracking.
- **[Vérification de source (anti-contamination contexte)](../fiches/verification-de-source.md)** — une étape LLM qui rejette un passage récupéré dès qu'il provient d'une source hors-périmètre, avant qu'il ne pollue le contexte.

### 🟡 Tradeoff / intermédiaire
- **[Autoréflexion / Reflexion](../fiches/reflexion.md)** — après un échec, l'agent rédige une critique de ce qui n'a pas marché et rejoue la tâche avec cette critique gardée en mémoire.
- **[Chain-of-Verification (CoVe)](../fiches/chain-of-verification.md)** — le modèle écrit une réponse, en dérive des questions de vérification factuelle, y répond isolément, puis corrige sa réponse à la lumière de ces vérifications.
- **[Least-to-Most prompting](../fiches/least-to-most.md)** — on décompose explicitement un problème en sous-problèmes ordonnés du plus simple au plus complexe, puis on les résout en séquence, chaque réponse servant de contexte à la suivante.
- **[Planification probabiliste](../fiches/planification-probabiliste.md)** — décider sous incertitude en évaluant plusieurs résultats possibles et en choisissant l'action à l'utilité attendue la plus élevée.
- **[Raisonnement par cas (case-based reasoning)](../fiches/case-based-reasoning.md)** — décider en réutilisant des cas passés similaires plutôt qu'en raisonnant à partir de zéro.
- **[ReWOO](../fiches/rewoo.md)** — « Reasoning Without Observation » : planifier toute la chaîne de raisonnement en interne d'abord, puis exécuter les outils, puis synthétiser, sans réinjecter chaque observation.
- **[Self-Consistency](../fiches/self-consistency.md)** — échantillonner plusieurs chaînes de raisonnement CoT indépendantes puis voter à la majorité pour la réponse finale, plutôt que de se fier à une seule génération.
- **[Self-Refine](../fiches/self-refine.md)** — un même modèle produit une sortie, génère sa propre critique, puis se révise, en boucle, sans aucun signal externe.
- **[Step-Back prompting](../fiches/step-back.md)** — avant de répondre à une question précise, on demande au modèle de « prendre du recul » pour formuler le concept ou le principe général sous-jacent, puis on raisonne à partir de cette abstraction.

### 🟢 Survol / introductif
- **[Architectures réactive / délibérative / cognitive](../fiches/archi-reactif-deliberatif-cognitif.md)** — trois niveaux de sophistication d'un agent : réflexe sans état, planificateur avec modèle du monde, ou système cognitif à mémoire et apprentissage.
- **[Chain-of-Thought (CoT)](../fiches/chain-of-thought.md)** — demander au modèle d'écrire ses étapes de raisonnement intermédiaires avant la réponse finale, au lieu de répondre directement.
- **[Planification : objectif / état / séquençage](../fiches/planification-goal-state-action.md)** — planifier, c'est définir un objectif (état final visé), modéliser l'état courant, puis dériver la séquence d'actions qui mène de l'un à l'autre.
- **[ReAct](../fiches/react.md)** — une boucle pensée → action (appel d'outil) → observation, répétée jusqu'à obtenir une réponse.

## Outils (1)

- **[Task Master (Taskmaster)](../fiches%20outils/task-master.md)** — _CLI + Serveur MCP (gestion de tâches pour agents)_
