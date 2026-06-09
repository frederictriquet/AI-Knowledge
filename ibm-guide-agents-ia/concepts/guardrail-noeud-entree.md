# Garde-fou en nœud d'entrée (Granite Guardian)

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [54-build-sql-agent-langgraph-mistral-medium-3-watsonx-ai](../md/54-build-sql-agent-langgraph-mistral-medium-3-watsonx-ai.md), [63-human-in-the-loop-ai-agent-langraph-watsonx-ai](../md/63-human-in-the-loop-ai-agent-langraph-watsonx-ai.md)

**En une phrase** — placer un détecteur de modération (HAP/PII via Granite Guardian) comme tout premier nœud du graphe, et router via une arête conditionnelle pour bloquer le contenu indésirable AVANT qu'il n'atteigne le LLM et les outils.

## Ce que dit le corpus
Les deux tutoriels appliquent le même motif LangGraph. Le graphe « commence au nœud `guardian` », qui appelle `guardian_moderation` « pour détecter tout contenu offensant avant qu'il n'atteigne le LLM et la base de données » (fichier 54) / « avant qu'ils n'atteignent le LLM et l'API » (fichier 63). L'arête est posée par `graph.add_edge(START, "guardian")` puis une `add_conditional_edges("guardian", ...)` qui « achemine l'état du graphe soit vers le nœud `llm`/`assistant`, soit vers la fin », selon la sortie de `guardian_moderation`. La fonction définit un dictionnaire `detectors` avec seuils — `"granite_guardian": {"threshold": 0.4}`, `"hap": {"threshold": 0.4}`, `"pii": {}` — instancie `Guardian(...)` (importé de `ibm_watsonx_ai.foundation_models.moderations`) et appelle `guardian.detect(...)`, qui renvoie un `moderation_verdict` (« sûr »/« approprié » ou « inapproprié »). Le fichier 54 démontre qu'« une requête sensible » est bloquée : « le graphe n'a pas atteint le nœud LLM avant de mettre fin à la conversation ».

## Tradeoff / insight pour un senior
Placer le détecteur en amont (fail-closed avant tout appel LLM/outil) économise tokens et latence sur les entrées malveillantes et réduit la surface d'attaque par injection. Limite : un détecteur fixe avec seuil unique (0.4) capture HAP/PII mais pas l'injection sémantique sophistiquée ; à compléter par validation/durcissement des prompts (voir sécurité agentique).

## Source primaire
Non citée académiquement — implémentation IBM watsonx avec le modèle Granite Guardian (`ibm_watsonx_ai.foundation_models.moderations.Guardian`), détecteurs HAP et PII.

## Voir aussi
- [hitl-statique-dynamique](hitl-statique-dynamique.md)
- [securite-agentique](securite-agentique.md)
- [ethique-gouvernance](ethique-gouvernance.md)
