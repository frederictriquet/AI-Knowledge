---
titre: "Le cadre canonique : Agent = LLM + Planification + Mémoire + Outils"
theme: outils-function-calling
niveau: 🔴
provenance: 🔗
base: sources/lilian-weng
source_url: https://lilianweng.github.io/posts/2023-06-23-agent/
source_titre: "LLM Powered Autonomous Agents"
---

# Le cadre canonique : Agent = LLM + Planification + Mémoire + Outils

> Fiche **source : Lilian Weng** · [post complet](../sources/lilian-weng/md/2023-06-23-agent.md) · Pertinence 🔴 substance

**En une phrase** — la décomposition de référence d'un agent autonome : un LLM joue le rôle de cerveau (contrôleur), épaulé par trois composants — planification, mémoire et usage d'outils.

## Ce que dit la source
Weng pose qu'un agent autonome piloté par LLM utilise le modèle comme cerveau, complété par trois composants clés. La **planification** couvre la décomposition en sous-objectifs (subgoal decomposition) et l'auto-réflexion sur les actions passées pour apprendre de ses erreurs. La **mémoire** se divise en mémoire court terme (l'apprentissage in-context) et mémoire long terme (rétention et rappel d'informations quasi infinies via un magasin vectoriel externe et une récupération rapide). L'**usage d'outils** permet à l'agent d'appeler des API externes pour combler ce qui manque aux poids du modèle (information courante, exécution de code, sources propriétaires). Weng cite comme démonstrateurs inspirants AutoGPT, GPT-Engineer et BabyAGI, et présente le LLM comme un « résolveur de problèmes généraliste » dépassant la simple génération de texte.

## Ce que ça ajoute vs IBM
Weng fournit une carte mentale unifiée et hiérarchisée (cerveau + 3 composants) qui articule explicitement les sous-mécanismes (décomposition, réflexion, CT/LT, API) en un seul schéma de référence, plus condensé que le découpage IBM.

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
