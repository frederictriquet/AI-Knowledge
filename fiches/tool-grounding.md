---
titre: "Tool grounding"
theme: outils-function-calling
niveau: 🟡
provenance: ✅
base: ibm-guide-agents-ia
source_url: https://www.ibm.com/fr-fr/think/tutorials/use-lm-studio-to-build-automatic-tool-calling-granite
source_titre: "Utiliser LM Studio pour automatiser l’appel d’outils avec Granite"
---

# Tool grounding

> Fiche du glossaire des patterns · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [21-use-lm-studio-to-build-automatic-tool-calling-granite](../sources/ibm-guide-agents-ia/md/21-use-lm-studio-to-build-automatic-tool-calling-granite.md)

**En une phrase** — donner à l'agent des outils qui exposent l'état légal vérifiable (ex. coups d'échecs légaux) pour l'empêcher d'halluciner ses décisions.

## Ce que dit le corpus
Le tutoriel LM Studio illustre l'idée sur deux cas. D'abord le calcul : un LLM seul ne renvoie pas le quotient exact de `26.97 / 6.28` car « il ne peut pas calculer le quotient seul » ; on lui fournit des fonctions `add`, `subtract`, `divide`… qu'il choisit via `model.act()`. Ensuite les échecs : un chatbot « déraille souvent après plusieurs tours, effectuant des déplacements illégitimes ou irrationnels ». On l'équipe alors d'outils — `legal_moves()`, `possible_captures()`, `possible_checks()`, `get_move_history()`, `get_book_moves()`, `make_ai_move()` — qui exposent l'état réel et légal de l'échiquier. Le corpus conclut : « Ce n'est pas beaucoup, mais c'est suffisant pour que le modèle puisse jouer une partie d'échecs complète sans halluciner et utiliser un raisonnement intelligent pour fonder ses décisions. » L'idée à retenir : l'outil permet au LLM de fonder ses réponses sur des données factuelles ou des opérations précises.

## Tradeoff / insight pour un senior
Le grounding ne supprime pas le raisonnement du LLM, il le contraint à un espace de décisions valides. Plutôt que de demander « quel est ton coup ? » (réponse libre, hallucinable), on demande « parmi ces coups légaux, lequel ? ». Le prompt système indique d'ailleurs au modèle d'utiliser sa connaissance des échecs comme méthode primaire et les outils comme assistants — le grounding cadre, il ne remplace pas.

## Source primaire
« Ce n'est pas beaucoup, mais c'est suffisant pour que le modèle puisse jouer une partie d'échecs complète sans halluciner et utiliser un raisonnement intelligent pour fonder ses décisions. » (IBM, [use-lm-studio…](../sources/ibm-guide-agents-ia/md/21-use-lm-studio-to-build-automatic-tool-calling-granite.md))

## Voir aussi
- [Tool calling / function calling](tool-calling.md)
- [Vérification de source](verification-de-source.md)
