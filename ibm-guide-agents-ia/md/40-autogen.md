> Source : https://www.ibm.com/fr-fr/think/topics/autogen

# Qu’est-ce qu’AutoGen ?

## Qu’est-ce qu’AutoGen ? 

Microsoft AutoGen est un framework [open source](https://www.ibm.com/fr-fr/think/topics/open-source) qui permet de créer des [agents d’IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) et d’autres applications d’intelligence artificielle. Il est le résultat de l’incursion de Microsoft Research dans l’[IA agentique](https://www.ibm.com/fr-fr/think/topics/agentic-ai "IA Agentique"), qui simplifie la création de [systèmes multiagents](https://www.ibm.com/fr-fr/think/topics/multiagent-system) à l’aide de [grands modèles de langage](https://www.ibm.com/fr-fr/think/topics/large-language-models) (LLM). 

Un article primé publié en 2024 par Chi Wang de Microsoft et d’autres chercheurs a démontré l’applicabilité d’AutoGen à plusieurs problèmes du monde réel, notamment l’optimisation de la chaîne d’approvisionnement et la prise de décisions en ligne.1 Le SDK Python d’AutoGen permet de démarrer aussi simplement qu’avec une `pip install` .

Bien qu’AutoGen soit un framework multiagent de premier plan, il existe tout un écosystème de [frameworks d’agent d’IA](https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks#1774455706) parmi lesquels choisir. Citons notamment [crewAI](https://www.ibm.com/fr-fr/think/topics/crew-ai#1091481868), [LangChain](https://www.ibm.com/fr-fr/think/topics/langchain#80364618) et [LangGraph](https://www.ibm.com/fr-fr/think/topics/langgraph#585923243), sans oublier [BeeAI d’IBM](https://www.ibm.com/fr-fr/think/news/beeai-open-source-multiagent).

## Architecture d’AutoGen

AutoGen est composé de trois couches principales:

1.  La couche principale
2.  La couche AgentChat
3.  La couche d’extensions

### La couche principale

Core est la couche fondamentale du framework AutoGen, en quelque sorte la plomberie et le câblage de base qui lui permet de fonctionner. Dans le langage de Microsoft, « l’[API](https://www.ibm.com/fr-fr/think/topics/api) Core implémente le transfert de messages, les agents pilotés par les événements et un environnement d’exécution local et distribué ».

En d’autres termes, il permet aux agents de [parler entre eux](https://www.ibm.com/fr-fr/think/topics/conversational-ai), de réagir à certains déclencheurs d’événements et de fonctionner localement sur votre ordinateur ou sur différents serveurs.

### La couche AgentChat

Si Core représente la plomberie et le câblage électrique, AgentChat est comme une maison préfabriquée avec des équipements intégrés. AgentChat part du principe (sur la base des cas d’utilisation courants) que la plupart des gens souhaitent que les agents d’IA puissent discuter avec des humains et d’autres bots (en termes techniques, qu’ils soient des « agents conversationnels »).

Et plutôt que de forcer les développeurs à coder une logique d’[orchestration](https://www.ibm.com/fr-fr/think/topics/workflow-orchestration) à partir de zéro, AgentChat suppose également que, dans la [collaboration multiagents](https://www.ibm.com/fr-fr/think/topics/ai-agent-orchestration), il y aura une division du travail, les équipes d’agents incluant souvent un « AssistantAgent » (qui utilise des LLM pour « penser » pour l’utilisateur) ainsi qu’un « UserProxyAgent » (pour l’exécution du code et l’utilisation de l’outil).

Cette capacité à tirer parti des équipes d’agents « modèles » facilite le prototypage rapide des applications d’IA.

### La couche d’extensions

AutoGen est « extensible », ce qui signifie que les utilisateurs peuvent ajouter de nouvelles capacités. Les extensions par défaut d’AutoGen comprennent des composants tels que LocalSearchTool, qui permet de rechercher dans votre propre ensemble de fichiers, ainsi que MultimodalWebSurfer, capable de surfer sur Internet.

Microsoft encourage également les développeurs à créer leurs propres extensions.

Parmi les autres outils intéressants, citons AutoGenBench, qui évalue les performances de l’IA agentique et aide à orienter le [débogage](https://www.ibm.com/fr-fr/think/topics/debugging), ainsi qu’AutoGen Studio, une interface no-code pour les débutants (pour laquelle un tutoriel vidéo est disponible sur YouTube). 

## Cas d’utilisation concrets d’AutoGen

Microsoft affirme avoir constaté des centaines d’applications d’AutoGen dans des secteurs allant de la biotechnologie aux biens de consommation conditionnés en passant par les télécommunications.2

### Formation

Benjamin Stern, professeur de thérapie physique à l’université de Tufts, a utilisé AutoGen pour des tâches complexes, notamment la création d’évaluations sur mesure, de guides d’étude individualisés et de services de tutorat pour les étudiants en transition vers des cours de niveau supérieur.

En outre, il a utilisé les interactions avec les agents pour simuler les entretiens avec les patients et a exploité les capacités de type « chat de groupe » d’AutoGen pour favoriser les débats participatifs de type round robin. Il déclare également utiliser des agents [OpenAI](https://www.ibm.com/fr-fr/think/topics/gpt) Assistant via AutoGen.

### Découverte de médicaments

La société pharmaceutique Novo Nordisk a décrit les différentes manières dont elle utilise la pile d’IA de Microsoft pour mener à bien la découverte de médicaments et partager son raisonnement.3 Sam Khalil, le vice-président des données de l’entreprise, déclare qu’AutoGen « nous aide à développer un cadre multiagents prêt pour la production ».

### Science des données

Les ingénieurs d’IBM Kelly Abuelsaad et Anna Gutowska ont créé une [application RAG multiagent avec AutoGen](https://www.ibm.com/fr-fr/think/tutorials/multi-agent-autogen-rag-granite#1181250928) qui fonctionne à partir d’entrées humaines pour collecter des informations à partir d’un corpus local de documents.

Elles décrivent un système dans lequel six agents hautement spécialisés (dont un agent de planification, un assistant de recherche et un générateur de rapports, entre autres) se divisent pour mieux régner. « Nous n’avons plus besoin d’écrire des requêtes SQL complexes pour extraire les données pertinentes d’une base de connaissances », écrivent-elles.

Cette solution est plus évolutive que de travailler avec un seul grand modèle, car les développeurs peuvent augmenter de manière sélective n’importe quel agent qui devient un goulot d’étranglement.

### Sécurité au travail

Sur Github, un utilisateur a démontré comment AutoGen pouvait être utilisé pour examiner des images prises par une caméra dans un environnement potentiellement dangereux comme une usine, déterminant en temps réel si des humains présents ne portent pas de casque. Grâce à une automatisation, le système ajoute un cadre de délimitation rouge au-dessus de l’image pour alerter le personnel de sécurité.

## AutoGen vs AG2

Ce qui précède concerne AutoGen, l’offre de Microsoft. Cependant, comme c’est souvent le cas avec les projets logiciels, il a fallu faire un choix. Un framework concurrent, AG2, est présenté comme un « AgentOS open source pour les agents d’IA » par ses créateurs, y compris Chi Wang.

Anciennement chez Microsoft, Chi Wang a rejoint Google DeepMind ; il semble avoir décidé de développer une version indépendante d’AutoGen depuis qu’il a quitté Microsoft.

« Ce n’est pas un nouveau framework, mais essentiellement la version 0.2.34 d’AutoGen qui continue sous un autre nom », explique un utilisateur de Reddit qui souhaitait dissiper toute confusion.4

L’une des principales différences entre AutoGen et AG2 de Microsoft est que celle-ci est pilotée par la communauté et non soutenue par une seule grande entreprise. Parmi les responsables d’AG2, citons Chi Wang, ainsi que des chercheurs de Meta, d’IBM et de diverses universités.5
