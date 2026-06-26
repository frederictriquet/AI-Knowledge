---
titre: "Le cadre canonique : Agent = LLM + Planification + Mémoire + Outils"
type: "Concept"
theme: outils-function-calling
niveau: 🔴
source_url: https://lilianweng.github.io/posts/2023-06-23-agent/
source_titre: "LLM Powered Autonomous Agents"
objectifs: [generer-code]
---

# Le cadre canonique : Agent = LLM + Planification + Mémoire + Outils

**En une phrase** — la décomposition de référence d'un agent autonome : un LLM joue le rôle de cerveau (contrôleur), épaulé par trois composants — planification, mémoire et usage d'outils.

## Ce que dit la source
Weng pose qu'un agent autonome piloté par LLM utilise le modèle comme cerveau, complété par trois composants clés. La **planification** couvre la décomposition en sous-objectifs (subgoal decomposition) et l'auto-réflexion sur les actions passées pour apprendre de ses erreurs. La **mémoire** se divise en mémoire court terme (l'apprentissage in-context) et mémoire long terme (rétention et rappel d'informations quasi infinies via un magasin vectoriel externe et une récupération rapide). L'**usage d'outils** permet à l'agent d'appeler des API externes pour combler ce qui manque aux poids du modèle (information courante, exécution de code, sources propriétaires). Weng cite comme démonstrateurs inspirants AutoGPT, GPT-Engineer et BabyAGI, et présente le LLM comme un « résolveur de problèmes généraliste » dépassant la simple génération de texte.

## Exemple
AutoGPT matérialise le schéma : son message système définit le LLM comme cerveau (bloc `thoughts` avec `reasoning`, `plan`, `criticism`) et liste 20 commandes-outils (`google`, `browse_website`, `write_to_file`, `execute_python_file`, `start_agent`…). La planification y est explicite (« Aim to complete tasks in the least number of steps »), la mémoire aussi : « ~4000 word limit for short term memory […] immediately save important information to files » — la mémoire long terme déléguée au système de fichiers faute de contexte. La sortie est imposée en JSON parsable par `json.loads`.

## Pourquoi c'est utile
Weng fournit une carte mentale unifiée et hiérarchisée (cerveau + 3 composants) qui articule explicitement les sous-mécanismes (décomposition, réflexion, CT/LT, API) en un seul schéma de référence.

## Sources primaires (citées par Weng)
- AutoGPT (Significant-Gravitas) — agent autonome avec LLM comme contrôleur principal.
- GPT-Engineer (Anton Osika) — génération d'un dépôt de code complet à partir d'une consigne.
- BabyAGI (Yohei Nakajima) — démonstrateur d'agent à boucle de tâches.

## Voir aussi
- [Mémoire CT/LT](memoire-court-long-terme.md)
- [Planification](planification-goal-state-action.md)
- [Tool calling](tool-calling.md)
- [Types d'agents](taxonomie-5-types-agents.md)
- [post complet](../sources/lilian-weng/md/2023-06-23-agent.md)
