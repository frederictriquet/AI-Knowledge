> Source : https://www.ibm.com/fr-fr/think/topics/langgraph

# Qu’est-ce que LangGraph ?

LangGraph, créé par LangChain, est un cadre d’exigences d’agent IA open source conçu pour construire, déployer et gérer des workflows d’agents d’IA générative complexes. Elle fournit un ensemble d’outils et de bibliothèques qui permettent aux utilisateurs de créer, d’exécuter et d’optimiser de grands modèles de langage (LLM) de manière évolutive et efficace. 

À la base, LangGraph exploite la puissance des architectures basées sur des graphes pour modéliser et gérer les relations complexes entre les différents composants d’un [workflow de l’agent](https://www.ibm.com/fr-fr/think/topics/ai-agents) IA.

Que signifient toutes ces informations ? L’exemple suivant permet de mieux comprendre LangGraph : pensez à ces architectures basées sur des graphes comme une carte configurable puissante, une « super-carte ». Les utilisateurs peuvent considérer le workflow d’IA comme le « Navigator » de cette « Super-map ».

Enfin, dans cet exemple, l’utilisateur est « Le cartographe ». Dans ce sens, le navigateur trace les itinéraires optimaux entre les points de la « Super-Map », qui sont tous créés par « The Cartographer ».

Pour résumer, les itinéraires optimaux au sein des architectures basées sur les graphiques (« Super-Map ») sont tracés et découverts en utilisant le workflow d’IA (« Navigator »).

Cette analogie est un excellent point de départ pour comprendre LangGraph, et si vous aimez les cartes, vous pouvez profiter en prime de l’opportunité de voir quelqu’un utiliser le mot cartographe.

 Workflow LangGraph

LangGraph éclaire les processus au sein d’un workflow d’IA, offrant une transparence totale sur l’état de l’agent. Dans LangGraph, la fonctionnalité « état » sert de banque de mémoire qui enregistre et suit toutes les informations précieuses traitées par le système d’IA.

À l’instar d’un bloc-notes numérique, le système capture et met à jour les données au fur et à mesure qu’elles déplacent par différentes étapes d’un workflow ou d’une analyse graphique.

Par exemple, si vous utilisez des agents pour surveiller la météo, cette fonctionnalité peut suivre le nombre d’enneigement et faire des suggestions en fonction de l’évolution des tendances des chutes de neige.

Cette observabilité de la façon dont le système fonctionne pour accomplir des tâches complexes est utile aux débutants pour mieux comprendre la gestion des états. La gestion des états est utile lors du débogage, car elle permet de centraliser l’état de l’application, raccourcissant ainsi souvent le processus global.

Cette approche permet une prise de décision plus efficace, une meilleure évolutivité et une performance globale améliorée. Cela permet également de renforcer l’engagement des personnes qui découvrent ces processus ou qui préfèrent une vision plus claire de ce qui se passe en coulisses.

LangGraph s’appuie également sur plusieurs technologies clés, dont LangChain, un cadre Python dédié à la création d’applications d’IA. LangChain propose une bibliothèque dédiée à la création et à la gestion des LLM. LangGraph utilise également l’approche « human-in-the-loop ».

En combinant ces technologies avec un ensemble d’API et d’outils, LangGraph offre aux utilisateurs une plateforme polyvalente pour développer des solutions et des workflows d’IA, y compris des chatbots, des graphiques d’état et d’autres systèmes basés sur des agents.

Approfondissez vos connaissances sur LangGraph en découvrant ses principales fonctionnalités, ses avantages et ses cas d’utilisation. À la fin de cet article, vous posséderez les connaissances et les ressources nécessaires pour passer à l’étape suivante avec LangGraph.\

## Principaux composants de LangGraph

Commençons par comprendre les composants clés de LangGraph. Le cadre des exigences est construit autour de plusieurs composants qui fonctionnent ensemble pour permettre aux utilisateurs de créer et de gérer des workflows complexes d’IA. Ces composants comprennent :

1.  Mécanisme de surveillance
2.  Architecture de graphe
3.  Outils

### Mécanisme de surveillance

**Human-in-the-loop**: Human-in-the-loop (HITL) fait référence à l’exigence d’interaction humaine à un moment donné au cours du processus. Dans le domaine du machine learning (ML), l’HITL fait référence à un processus collaboratif dans lequel les humains améliorent les capacités de calcul des machines pour prendre des décisions éclairées tout en construisant un modèle.

En utilisant les points de données les plus critiques, HITL améliore la précision des algorithmes de machine learning, surpassant ainsi les méthodes d’échantillonnage aléatoires.

### Architecture de graphe

#### Graphes avec état

Un concept où chaque nœud du graphe représente une étape dans le calcul, créant essentiellement un graphe d’état. Cette approche avec état permet au graphique de conserver les informations sur les étapes précédentes, ce qui permet un traitement continu et contextuel des informations au fur et à mesure du calcul. Les utilisateurs peuvent gérer tous les graphiques avec état de LangGraph via ses API.

#### Graphique cyclique

Un graphique cyclique est un graphique qui contient au moins un cycle et qui est essentiel pour les exécutions d’agents. Cela signifie qu’il existe un chemin qui commence et se termine au même nœud, formant une boucle dans le graphique. Les workflows complexes impliquent souvent des dépendances cycliques, où le résultat d’une étape dépend des étapes précédentes dans la boucle.

#### Nœuds

Dans LangGraph, les nœuds représentent des composants ou des agents individuels au sein d’un workflow d’IA. Les nœuds peuvent être considérés comme des « acteurs » qui interagissent les uns avec les autres d’une manière spécifique. Par exemple, pour ajouter des nœuds pour l’appel d’outils, on peut utiliser le ToolNode. Un autre exemple, le nœud suivant, fait référence au nœud qui sera exécuté après le nœud actuel.

#### Edges

Les edges sont une fonction de Python qui détermine le nœud à exécuter en fonction de l’état actuel. Les edges peuvent être des branches conditionnelles ou des transitions fixes.

### Outils

1.  RAG 
2.  Workflows 
3.  API 
4.  LangSmith 

### RAG 

La génération augmentée de récupération (RAG) combine la puissance des LLM avec des informations contextuelles provenant de sources externes en récupérant les documents pertinents, qui sont ensuite utilisés comme entrée pour générer des réponses.

### Workflows 

les workflows sont les séquences d’interactions de nœuds qui définissent un workflow d’IA. En organisant des nœuds dans un workflow, les utilisateurs peuvent créer des workflows plus complexes et plus dynamiques qui utilisent les forces des composants individuels.

### API 

LangGraph fournit un ensemble d’API qui permettent aux utilisateurs d’interagir avec ses composants de manière programmatique. Les utilisateurs peuvent utiliser une clé API, ajouter de nouveaux nœuds, modifier les workflows existants et récupérer des données à partir d’un workflow d’IA.

### LangSmith 

LangSmith est une API spécialisée pour la création et la gestion de LLM dans LangGraph. Il fournit des outils pour initialiser les LLM, ajouter des edges conditionnels et optimiser la performance. En combinant ces composants de manière innovante, les utilisateurs peuvent créer des workflows d’IA plus sophistiqués qui utilisent les forces des composants individuels.

## Évolutivité LangGraph

En utilisant une architecture basée sur des graphes, LangGraph permet aux utilisateurs de dimensionner les workflows sans ralentir ni sacrifier l’efficacité.

LangGraph utilise une prise de décision améliorée en modélisant des relations complexes entre les nœuds, ce qui signifie qu’il utilise des agents IA pour analyser leurs actions passées et leurs commentaires. Dans le monde des LLM, ce processus est appelé réflexion.

**Prise de décision renforcée** : en modélisant des relations complexes entre les nœuds, LangGraph fournit un cadre des exigences pour créer des systèmes de prise de décision plus efficaces.

**Flexibilité accrue** : une nature open source et une conception modulaire permettant aux développeurs d’intégrer de nouveaux composants et d’adapter les workflows existants.

**Workflows multiagents :** les tâches complexes peuvent être traitées par des workflows multi-agents. Cette approche consiste à créer des agents LangChain dédiés pour des tâches ou des domaines spécifiques.

L’acheminement des tâches vers les agents LangChain appropriés permet une exécution parallèle et une gestion efficace des Workloads divers. Une telle architecture de réseau multi-agent illustre la coordination décentralisée de l’automatisation des agents.

Un excellent exemple, créé par Joao Moura, est celui de l’utilisation de CrewAI avec LangChain et LangGraph. La vérification des e-mails et la création de brouillons sont automatisées avec CrewAI orchestrant des agents IA, ce qui leur permet de collaborer et d’exécuter efficacement des tâches complexes.

## Cas d’utilisation de LangGraph

1.  Chatbots 
2.  Systèmes d’agents
3.  Applications LLM

### Chatbots 

Les utilisateurs peuvent créer une application pour planifier leurs vacances, avec des workflows basés sur des nœuds et des graphiques acycliques orientés (DAG). Le chatbot apprend à répondre à l’entrée minimale de l’utilisateur et à personnaliser les recommandations. Actuellement, des services tels que duplex de Google utilisent LangGraph de la même manière pour imiter les conversations humaines.

### Systèmes d’agents

LangGraph fournit un cadre des exigences pour la création de systèmes basés sur des agents, qui peuvent être utilisés dans des applications telles que la robotique, les véhicules autonomes ou les jeux vidéo.

### Applications LLM

En utilisant les capacités de LangGraph, les développeurs peuvent créer des modèles d’IA plus sophistiqués qui apprennent et s’améliorent au fil du temps. Norwegian Cruise Line utilise LangGraph pour compiler, créer et affiner des solutions d’IA destinées aux hôtes. Cette capacité permet d’améliorer et de personnaliser l’expérience des invités.

## Intégration des LLM dans LangGraph

Les agents de LangGraph sont basés sur la série de modèles GPT (generative pretrained transformer) d’OpenAI, GPT-3.5 et GPT-4. Cependant, LangGraph et sa communauté open source ont contribué à ajouter plusieurs autres modèles qui s’initialisent via la configuration d’API LLM, notamment les modèles Anthropic et AzureChatOpenAI.

La boucle relativement petite est similaire à des projets tels qu’Auto-GPT.

LangGraph propose un tutoriel YouTube qui facilite l’exploration de la façon d’intégrer les LLM open source sur son site de documentation GitHub. La première étape de l’intégration d’un LLM consiste à configurer un référentiel d’inférence (repo) tel que LLaMA-Factory, FastChat et Ollama.

Ce référentiel permet le déploiement du modèle LLM correspondant, qui est configuré via ses identifiants d’API.

## Autres cadres des exigences d'agent IA

CrewAI, MetaGPT et AutoGen ne sont que quelques cadres des exigences multi-agents capables de gérer des workflows complexes. Cette opérations permet une approche plus flexible et nuancée pour relever divers défis de calcul.

En fournissant des capacités de débogage complètes, ces cadres des exigences permettent aux développeurs d’identifier et de résoudre rapidement les problèmes, ce qui se traduit par des processus de développement et d’optimisation plus efficaces.

## LangGraph Studio : une interface visuelle pour le développement de workflows

LangGraph a également introduit LangGraph Studio, une interface visuelle pour le développement de workflows. Avec LangGraph Studio, les utilisateurs peuvent concevoir et créer des workflows à l’aide d’une interface graphique, sans avoir à écrire de code.

L’application de bureau téléchargeable rend LangGraph Studio plus utilisable pour les débutants. LangGraph Studio propose également ces fonctionnalités supplémentaires :

**Courbe d’apprentissage peu profonde** : LangGraph Studio n’est pas nécessaire pour accéder à LangGraph. Toutefois, grâce à l’interface visuelle de LangGraph Studio, les utilisateurs peuvent se concentrer sur la conception de leurs workflows sans s’enliser dans le code.

Collaboration améliorée : LangGraph Studio permet le partage de workflows avec d’autres personnes, qu’il s’agisse d’une équipe de développeurs ou d’un client.

**Débogage** : les capacités ne se limitent pas à la création d’un graphique, des fonctionnalités de débogage sont incluses pour garantir la précision et la fiabilité du graphique. Grâce à son environnement de développement intégré (IDE) edge, LangGraph Studio permet de visualiser et de déboguer des applications LangGraph.

## Développements futurs

**Traitement automatique du langage naturel (NLP) amélioré** : LangGraph aura des capacités NLP plus avancées, qui lui permettront de mieux comprendre le langage naturel et de fournir des réponses plus précises.

**Machine learning amélioré** : LangGraph disposera de capacités de machine learning améliorées, qui lui permettront d’apprendre et de s’améliorer au fil du temps.

**Prise en charge de nouvelles plateformes** : LangGraph prendra en charge de nouvelles plateformes, telles que les appareils mobiles et l’edge computing pour rendre sa technologie plus accessible.
