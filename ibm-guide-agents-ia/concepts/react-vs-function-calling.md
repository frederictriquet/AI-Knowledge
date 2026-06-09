# ReAct vs function calling

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [28-react-agent](../md/28-react-agent.md)

**En une phrase** — le function calling est plus rapide et économe sur des tâches prévisibles ; ReAct gère mieux l'imprévisible au prix des tokens de boucle de raisonnement.

## Ce que dit le corpus
Le corpus présente deux paradigmes agentiques. ReAct combine le raisonnement par chaîne de pensée (CoT) avec l'usage d'outils, dans une boucle alternant pensées, actions et observations. Le function calling, introduit par OpenAI en juin 2023, ajuste les modèles pour qu'ils reconnaissent quand produire un objet JSON structuré d'arguments d'appel. IBM tranche que le « meilleur » dépend du cas d'usage : pour des tâches relativement simples ou prévisibles, le function calling « peut s'exécuter plus rapidement, économiser des tokens et être plus simple à implémenter qu'un agent ReAct », car les tokens dépensés dans la boucle CoT seraient alors inefficaces. Le compromis : le function calling offre une relative incapacité à personnaliser comment et quand le modèle choisit un outil, et sa rigidité limite l'adaptation aux scénarios dynamiques ou imprévisibles, où la visualisation du raisonnement étape par étape devient utile.

## Tradeoff / insight pour un senior
Ce n'est pas un choix exclusif : un agent ReAct utilise du function calling pour ses actions. L'opposition réelle est « boucle de raisonnement explicite » vs « appel direct ». Paye les tokens de la boucle ReAct quand tu as besoin d'explicabilité, d'auto-correction et d'adaptation ; économise-les quand le chemin est connu d'avance.

## Source primaire
« Dans des scénarios impliquant des tâches relativement simples (ou du moins prévisibles), l'appel de fonction peut s'exécuter plus rapidement, économiser des tokens et être plus simple à implémenter qu'un agent ReAct. » (IBM, [react-agent](../md/28-react-agent.md))

## Voir aussi
- [Tool calling / function calling](tool-calling.md)
