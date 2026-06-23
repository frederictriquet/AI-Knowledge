---
titre: "Tool calling / function calling"
type: "Concept"
theme: outils-function-calling
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/tool-calling
source_titre: "Qu’est-ce qu’un appel de fonction ?"
---

# Tool calling / function calling

**En une phrase** — le modèle émet un appel structuré (JSON + tool_call_id) que ton code exécute, puis dont il réinjecte le résultat.

## En détail
L'appel d'outil (aussi nommé appel de fonction) désigne la capacité d'un LLM à interagir avec des outils, API ou systèmes externes pour dépasser ses connaissances pré-acquises : interroger une base, récupérer des données temps réel, exécuter du code. Le cycle se décompose en étapes : reconnaître la nécessité d'un outil, sélectionner l'outil (chaque outil porte des métadonnées — nom, description, paramètres, types), construire une requête structurée, recevoir et traiter la réponse. Un identifiant unique relie chaque requête à son résultat. Les exemples LangChain montrent que le LLM renvoie seulement le `name` de l'outil et ses `arguments` dans `tool_calls` ; l'exécution réelle reste à la charge du code, et chaque `ToolMessage` porte un `tool_call_id`. IBM Granite, Llama 3, Mistral et Claude exposent tous cette capacité, gérée différemment.

## Tradeoff / insight pour un senior
Distinction clé : émettre l'appel et l'exécuter sont deux étapes séparables. `bind_tools` produit le JSON sans rien exécuter ; il faut un agent (ou ta boucle) pour fermer le cycle. La fiabilité dépend entièrement de la qualité des `description` d'outils et de paramètres, transmises au modèle pour la sélection et le remplissage des arguments.

## Source primaire
« L'appel d'outil, parfois appelé appel de fonction, est un catalyseur clé de l'IA agentique. » ([source](../sources/ibm-guide-agents-ia/md/19-tool-calling.md))

## Voir aussi
- [ReAct vs function calling](react-vs-function-calling.md)
- [Tool grounding](tool-grounding.md)
- [LLM imbriqué dans un outil](llm-dans-un-outil.md)
