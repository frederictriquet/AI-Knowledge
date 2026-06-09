---
titre: "Auto-réflexion des agents (ReAct, Reflexion, CoH, AD)"
theme: raisonnement-planification
niveau: 🔴
source_url: https://lilianweng.github.io/posts/2023-06-23-agent/
source_titre: "LLM Powered Autonomous Agents"
---

# Auto-réflexion des agents (ReAct, Reflexion, CoH, AD)

**En une phrase** — la famille des mécanismes par lesquels un agent s'améliore en boucle en revenant sur ses décisions et erreurs passées, indispensables dans les tâches réelles où l'essai-erreur est inévitable.

## Ce que dit la source
L'auto-réflexion est essentielle pour que l'agent s'améliore itérativement. **ReAct** (Yao et al. 2023) entrelace raisonnement et action en étendant l'espace d'action à des actions discrètes plus l'espace langagier, selon le gabarit `Thought / Action / Observation` répété ; il bat la baseline `Act`-seule. **Reflexion** (Shinn & Labash 2023) ajoute mémoire dynamique et auto-réflexion sur un cadre RL à récompense binaire : une fonction heuristique détecte les trajectoires inefficaces ou les hallucinations (actions identiques répétées) et peut réinitialiser l'environnement ; les réflexions (jusqu'à trois) sont injectées dans la mémoire de travail. **Chain of Hindsight** (CoH ; Liu et al. 2023) présente au modèle une séquence de ses sorties passées annotées de feedback humain, par fine-tuning supervisé, pour qu'il apprenne à produire mieux. **Algorithm Distillation** (AD ; Laskin et al. 2023) applique la même idée à des trajectoires multi-épisodes de RL, distillant le processus d'apprentissage lui-même.

## Pourquoi c'est utile
Ces quatre techniques (ReAct, Reflexion, CoH, AD) relèvent d'une même lignée « apprendre de ses erreurs », dont les mécanismes internes diffèrent (heuristique, récompense binaire, fine-tuning sur historique).

## Sources primaires
- Yao et al. 2023 — « ReAct: Synergizing Reasoning and Acting in Language Models » (ICLR 2023).
- Shinn & Labash 2023 — « Reflexion: an autonomous agent with dynamic memory and self-reflection ».
- Liu et al. 2023 — « Chain of Hindsight Aligns Language Models with Feedback ».
- Laskin et al. 2023 — « In-context Reinforcement Learning with Algorithm Distillation » (ICLR 2023).

## Voir aussi
- [Reflexion](reflexion.md)
- [ReAct](react.md)
- [post complet](../sources/lilian-weng/md/2023-06-23-agent.md)
