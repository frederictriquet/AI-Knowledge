---
titre: "ReAct vs function calling"
type: "Concept"
theme: outils-function-calling
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/react-agent
source_titre: "Qu’est-ce qu’un agent ReAct ?"
---

# ReAct vs function calling

**En une phrase** — le function calling est plus rapide et économe sur des tâches prévisibles ; ReAct gère mieux l'imprévisible au prix des tokens de boucle de raisonnement.

## En détail
Deux paradigmes agentiques coexistent. ReAct combine le raisonnement par chaîne de pensée (CoT) avec l'usage d'outils, dans une boucle alternant pensées, actions et observations. Le function calling, introduit par OpenAI en juin 2023, ajuste les modèles pour qu'ils reconnaissent quand produire un objet JSON structuré d'arguments d'appel. Le « meilleur » dépend du cas d'usage : pour des tâches relativement simples ou prévisibles, le function calling « peut s'exécuter plus rapidement, économiser des tokens et être plus simple à implémenter qu'un agent ReAct », car les tokens dépensés dans la boucle CoT seraient alors inefficaces. Le compromis : le function calling offre une relative incapacité à personnaliser comment et quand le modèle choisit un outil, et sa rigidité limite l'adaptation aux scénarios dynamiques ou imprévisibles, où la visualisation du raisonnement étape par étape devient utile.

## Exemple
Le prompt système de l'agent préconstruit `ZERO_SHOT_REACT-DESCRIPTION` de LangChain matérialise la boucle ReAct sans aucun few-shot : il liste les outils (`Wikipedia`, `duckduckgo_search`, `Calculator`) puis impose le gabarit textuel `Question → Thought → Action → Action Input → Observation` avec la mention « … (this Thought/Action/Action Input/Observation can repeat N times) », clos par `Thought: I now know the final answer` / `Final Answer:`. Le raisonnement transite par le `{agent_scratchpad}` — là où le function calling pur émettrait directement le JSON d'arguments sans cette verbalisation intermédiaire.

## Tradeoff / insight pour un senior
Ce n'est pas un choix exclusif : un agent ReAct utilise du function calling pour ses actions. L'opposition réelle est « boucle de raisonnement explicite » vs « appel direct ». Paye les tokens de la boucle ReAct quand tu as besoin d'explicabilité, d'auto-correction et d'adaptation ; économise-les quand le chemin est connu d'avance.

## Source primaire
« Dans des scénarios impliquant des tâches relativement simples (ou du moins prévisibles), l'appel de fonction peut s'exécuter plus rapidement, économiser des tokens et être plus simple à implémenter qu'un agent ReAct. » ([source](../sources/ibm-guide-agents-ia/md/28-react-agent.md))

## Voir aussi
- [Tool calling / function calling](tool-calling.md)
