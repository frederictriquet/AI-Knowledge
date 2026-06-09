> Source : https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks

# Cadres d’agents d’IA : choisir de bonnes bases pour votre entreprise

D’un simple agent d’intelligence artificielle (IA) qui surveille et signale les transactions frauduleuses aux institutions financières à un système multi-agents de gestion de la chaîne d’approvisionnement qui suit les niveaux de stocks et prévoit la demande, l’IA agentique peut être salutaire pour les entreprises. Comment les entreprises peuvent-elles commencer à faire appel aux agents d’IA ? C’est là qu’interviennent les cadres d’agents d’IA.

## Cadres d’agent d’IA : une structure fondamentale pour l’IA agentique

Les agents d’IA sont des programmes qui peuvent effectuer de manière autonome une tâche pour le compte d’un utilisateur. Ces systèmes d’IA élaborent d’abord un plan comportant une série d’étapes pour accomplir une tâche complexe.

Ils utilisent ensuite l’appel de fonction pour se connecter à des outils externes (tels que les interfaces de programmation des applications (API), les sources de données, les recherches sur le Web et même d’autres agents d’IA) qui peuvent les aider à combler leurs lacunes.

Après avoir exécuté leur plan d’action, les agents autonomes apprennent du feedback reçu et stockent les informations apprises en mémoire pour améliorer leur performance.

Les entreprises peuvent créer des agents d’IA de A à Z en s’appuyant sur des langages de programmation comme Python ou JavaScript. Cependant, une approche plus rapide et plus évolutive consiste à utiliser les frameworks d’agents IA.

Les cadres d’IA agentique sont essentiels au développement, au déploiement et à la gestion de vos agents IA. Ces plateformes logicielles intègrent des caractéristiques et des fonctions qui permettent de rationaliser et d’accélérer le processus, notamment :

- une architecture prédéfinie qui décrit la structure, les caractéristiques et les capacités de l’IA agentique ;
- des protocoles de communication qui facilitent l’interaction entre les agents d’IA et les utilisateurs humains ou d’autres agents ;
- Systèmes de gestion pour coordonner les tâches.
- des outils d’intégration pour l’appel de fonction ;
- Outils de surveillance pour suivre la performance de l’IA agentique.

## Facteurs d’évaluation des cadres pour les agents d’IA

Avant de vous plonger dans l’univers des agents d’IA, définissez les objectifs et les cas d’utilisation de votre organisation. Le cadre idéal doit concilier vos capacités techniques, vos besoins à court terme et vos objectifs à long terme.

Voici quelques aspects à prendre en compte lors du choix d’un cadre d’agents d’IA :

- Complexité
- Confidentialité et sécurité des données
- Facilité d'utilisation
- Intégration transparente
- Performance et évolutivité

### Complexité

Identifiez les tâches que vous souhaitez confier à votre agent IA, ainsi que leur niveau de complexité. Déterminez s’il s’agira d’une mise en œuvre simple, avec un seul agent, ou d’un écosystème multi-agent.

Pour les environnements multi-agents, mappez les interactions requises entre les agents et les aspects qui nécessitent toujours une intervention humaine.

Dans le domaine du support client, par exemple, un seul agent d’IA peut aider à hiérarchiser les problèmes qui se présentent. Cependant, si vous souhaitez un workflow plus robuste, envisagez de créer un système multi-agents avec différents agents pour résoudre les problèmes, suggérer des solutions et attribuer les cas complexes à d’autres agents d’IA ou humains.

### Confidentialité et sécurité des données

La confidentialité et la sécurité des données doivent être une priorité lors du choix d’un cadre agentique. Vérifiez les politiques et mesures de sécurité de l’infrastructure que vous avez choisie, notamment le chiffrement des données au repos et en transit, les contrôles d’accès et la suppression de toute information sensible.

### Facilité d’utilisation

Prenez en compte le niveau de compétences de votre équipe de développement. Un cadre d’IA adapté aux débutants comme CrewAI, par exemple, associe interface no-code pour accélérer le prototypage et modèles d’agents IA prêts à l’emploi pour un déploiement rapide.

Les développeurs d’IA plus expérimentés peuvent opter pour des frameworks d’agents avancés tels que LangGraph, qui offrent un contrôle de bas niveau et des options de code personnalisables.

### Intégration transparente

Évaluez la compatibilité des cadres d’IA agentique avec votre pile existante. Assurez-vous que le cadre choisi s’intègre à vos sources de données, à votre infrastructure et à vos outils actuels.

Décidez comment l’IA agentique sera déployée dans votre environnement, que ce soit sur site ou dans le cloud, et si un déploiement à petite ou grande échelle est nécessaire.

### Performance et évolutivité

Évaluez la performance du cadre d’agents IA choisi. Prenez en compte le temps de réponse ou la latence pour les applications en temps réel, et déterminez si la performance se dégrade lorsque vous traitez d’immenses volumes de données ou des requêtes simultanées. En outre, même si l’accent est mis sur le court terme, réfléchissez à l’évolution du cadre au fur et à mesure que votre entreprise se développera.

## Cadres courants pour les agents d’IA

L’IA agentique n’en est qu’à ses débuts. Au fur et à mesure que la technologie derrière les agents IA évolue, les cadres sous-jacents évoluent également. Voici quelques exemples de cadres d’agents IA très utilisés actuellement :

### AutoGen

AutoGen est un cadre open source de Microsoft permettant de créer des applications d’IA multi-agents pour effectuer des tâches complexes. Son architecture se compose de trois couches :

- Core est un cadre de programmation qui permet de développer un réseau d’agents évolutif et distribué, avec des outils de traçage et de débogage des workflows d’agents. S’appuyant sur une messagerie asynchrone, il prend en charge les interactions requête-réponse et celles basées sur les événements.
- Construit sur Core, AgentChat permet de créer des assistants d’IA conversationnelle. Les débutants se voient proposer comme point de départ des agents uniques par défaut et des équipes multi-agents dont les comportements et les schémas d’interaction sont prédéfinis.
- Extensions est un package contenant des implémentations des composants Core et AgentChat pour étendre leurs capacités et interagir avec des bibliothèques externes et d’autres services. Vous pouvez exploiter les extensions intégrées et celles développées par la communauté AutoGen, ou même créer les vôtres.

AutoGen fournit également 2 outils de développement pratiques : AutoGen Bench pour évaluer et comparer la performance de l’IA agentique, et AutoGen Studio, une interface no-code pour développer des agents. AutoGen est disponible sur GitHub.

### CrewAI

CrewAI est un cadre d’orchestration pour les solutions d’IA multi-agents. Comme AutoGen, CrewAI est open source.

L’architecture basée sur les rôles de CrewAI traite l’IA agentique comme une « équipe » de « travailleurs ». Voici les principaux composants d’une telle équipe :

- Les agents se voient attribuer des rôles spécialisés tout en continuant à collaborer sur des workflows complexes. Les développeurs peuvent décrire le rôle, l’objectif et le contexte d’un agent en langage naturel.
- Les tâches définissent les responsabilités spécifiques de chaque agent. Les développeurs peuvent également employer le langage naturel pour définir la tâche et le résultat attendu de chaque agent.
- Un processus identifie la manière dont les agents travaillent ensemble et dont les tâches sont exécutées. Il peut être séquentiel, les tâches étant accomplies selon un ordre prédéfini, ou hiérarchique, un agent gestionnaire personnalisé supervisant la délégation, l’exécution et l’achèvement des tâches.

L’un des exemples de l’ensemble de CrewAI comprend une équipe d’analyse boursière. Cette équipe collabore de manière séquentielle, avec un agent analyste de marché chargé d’analyser les données d’une action particulière, un agent chercheur chargé de recueillir des informations complémentaires qui valident l’analyse des données, et un agent stratégique chargé de créer un plan d’action par étapes basé sur l’analyse et les données complémentaires.

CrewAI permet la connexion à divers grands modèles de langage (LLM) comme Claude d’Anthropic, Gemini de Google, les modèles d’IA de Mistral , les modèles GPT d’OpenAI et les modèles de fondation proposés par IBM watsonx.ai.

Le framework dispose également d’une suite d’outils de génération augmentée par récupération (RAG) pour faire des recherches dans différentes sources de données.

CrewAI est accessible sur GitHub.

### LangChain

LangChain est un autre cadre open source permettant de créer des applications basées sur les LLM, notamment des [chatbots](https://www.ibm.com/fr-fr/think/topics/chatbots) tels que ChatGPT et des agents d’IA.

Il repose sur une architecture modulaire, chaque module représentant des abstractions qui encapsulent les concepts complexes et les étapes nécessaires pour travailler avec les LLM.

Ces composants modulaires peuvent ensuite être reliés entre eux pour créer des applications d’IA.

LangChain est utile pour développer des agents d’IA simples avec des workflows élémentaires. Il prend en charge les bases de données vectorielles et les utilitaires permettant d’intégrer de la mémoire dans les applications, ce qui permet de conserver l’historique et le contexte.

Sa plateforme LangSmith permet le débogage, les tests et la surveillance des performances.

LangChain est accessible sur GitHub.

### LangChain4j

LangChain4j est une bibliothèque Java open-source qui simplifie et facilite l’intégration de grands modèles de langage dans les applications Java. Une API unifiée permet d’accéder aux [LLM](https://www.ibm.com/fr-fr/think/topics/large-language-models-list) et aux bases de données vectorielles courantes.

Il présente des fonctionnalités allant du modèle de prompt de bas niveau, de la gestion de la mémoire de chat et de l’appel de fonctions aux modèles de haut niveau tels que les[agents, la génération augmentée de récupération (RAG)](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation) et les outils (y compris la prise en charge du [Model Context Protocol](https://www.ibm.com/fr-fr/think/topics/model-context-protocol)). Il facilite également les Intégrations avec divers cadres des exigences Java d’entreprise.

LangChain4j suit une conception modulaire :

- Les`langchain4j` Le module contient des fonctionnalités de haut niveau telles que l’API unifiée, les implémentations de mémoire de chat et des outils tels que les chargeurs de documents.
- Les `langchain4j-core` décrit les abstractions de base et leurs API correspondantes.
- Une gamme de`langchain4j-{integration}` les modules offrent une intégration avec différents LLM et bases de données vectorielles.

Pendant ce temps, le`langchain4j-agentic` permet de construire des applications d'IA agentique et d'[orchestrer des](https://www.ibm.com/fr-fr/think/topics/ai-agent-orchestration) [flux de travail](https://www.ibm.com/fr-fr/think/topics/agentic-workflows) multi-agents. Il permet l'ingénierie du contexte et de la mémoire et la gestion des [appels d'outils](https://www.ibm.com/fr-fr/think/topics/tool-calling). En outre, le`langchain4j-agentic-a2a` prend en charge l’utilisation du [protocole Agent2Agent](https://www.ibm.com/fr-fr/think/topics/agent2agent-protocol) pour connecter plusieurs agents dans un système agentique distribué.

LangChain est accessible sur [GitHub.](https://github.com/langchain4j/langchain4j)

### LangGraph

LangGraph fait partie de l’écosystème LangChain. Le cadre est extrêmement efficace pour orchestrer les workflows complexes des systèmes multi-agents.

Il applique une architecture graphique, au sein de laquelle les différentes tâches ou actions des agents IA sont représentées par des nœuds, tandis que les transitions entre ces actions sont représentées sous forme de contours.

Un composant d’état gère la liste des tâches tout au long des interactions. Ce type d’architecture convient aux workflows cycliques, conditionnels ou non linéaires.

Ainsi, une compagnie aérienne peut créer un agent d’IA assistant de voyage qui aide les utilisateurs à trouver et à réserver des vols. Avec LangGraph, chacune de ces actions est représentée par des nœuds, et ces nœuds peuvent avoir plusieurs agents effectuant des tâches particulières.

On peut intégrer l’humain dans la boucle, afin que les utilisateurs puissent choisir un vol dans la liste de recherche, et si rien ne correspond à leurs préférences, l’agent de voyage IA peut facilement revenir au nœud « Rechercher un vol » et recommencer la recherche.

LangGraph est accessible sur GitHub.

### LlamaIndex

LlamaIndex est un cadre d’harmonisation des données open source pour la création de solutions d’IA générative et d’IA agentique. Il propose des agents et des outils préconfigurés ainsi que des workflows récemment introduits, un mécanisme de développement de systèmes multi-agents.

Voici les principaux éléments qui composent un workflow dans LlamaIndex :

- Les étapes sont les actions spécifiques à chaque agent. Il s’agit des composantes de base d’un workflow.
- Les événements déclenchent les étapes et constituent le moyen de communication entre ces dernières.
- Le contexte est partagé tout au long du workflow afin que les étapes puissent stocker, récupérer et transmettre des données et maintenir l’état tout au long de leur exécution.

Cette architecture événementielle permet d’accomplir les étapes du workflow de manière asynchrone. Cela signifie que, contrairement à une architecture graphique, les parcours entre étapes n’ont pas besoin d’être définis, ce qui permet des transitions plus souples entre les actions des agents.

Ainsi, les workflows LlamaIndex sont bien adaptés aux applications d’agents d’IA plus dynamiques qui doivent souvent retourner aux étapes précédentes ou se ramifier vers plusieurs étapes.

LlamaIndex est disponible sur GitHub.

### Semantic Kernel

Semantic Kernel est un kit de développement open source Microsoft qui permet de créer des applications d’IA générative pour les entreprises. Son cadre d’agents, actuellement annoncé comme expérimental, fournit des abstractions de base pour la création d’agents.

Il dispose de deux implémentations d’agents intégrées : un agent de complétion de chat et un agent assistant plus avancé.

Plusieurs agents peuvent être orchestrés par le biais de discussions de groupe ou en utilisant le Process Framework de Semantic Kernel (également marqué comme expérimental) pour des workflows plus complexes.

Un processus se compose d’étapes, qui représentent les tâches assignées aux agents d’IA, et décrivent comment les données circulent entre les étapes.

Semantic Kernel est accessible sur GitHub.

Pour informer davantage la prise de décision, n’hésitez pas à tester les cadres de votre choix. Commencez petit, avec une mise en œuvre simple et un seul agent, pour explorer le fonctionnement de chaque cadre et le comparer aux autres.

Un cadre d’agent efficace s’adapte aux besoins de votre entreprise et permet de créer des agents IA qui automatisent les workflows, afin d’améliorer l’efficacité de vos processus métier.
