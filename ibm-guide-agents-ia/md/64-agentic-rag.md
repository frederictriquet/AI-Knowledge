> Source : https://www.ibm.com/fr-fr/think/topics/agentic-rag

# Qu’est-ce que la RAG agentique ?

La RAG agentique consiste à utiliser des agents IA pour faciliter la génération augmentée de récupération (RAG). Les systèmes de RAG agentique ajoutent des agents IA au pipeline RAG pour en améliorer l’adaptabilité et la précision. Comparée aux systèmes RAG traditionnels, la RAG agentique permet aux grands modèles de langage (LLM) d’effectuer une recherche d’information à partir de plusieurs sources et de gérer des workflows plus complexes.

### Qu’est-ce que la RAG ?

La génération augmentée de récupération est une application de l’intelligence artificielle (IA) qui connecte un modèle d’IA générative à une base de connaissances externe. Les données de la base de connaissances complètent les requêtes des utilisateurs avec plus de contexte, de sorte que le LLM peut générer des réponses plus précises. La RAG permet aux LLM d’être plus précis dans des contextes propres à un domaine sans avoir besoin d’affinage. 

Plutôt que de s’appuyer uniquement sur les données d’entraînement, les modèles IA optimisés par la RAG peuvent accéder aux données les plus récentes en temps réel via des [API](https://www.ibm.com/fr-fr/think/topics/api) et d’autres connexions aux sources de données. Un pipeline RAG standard comprend deux modèles IA : 

- Le composant de recherche d’information, généralement un modèle de plongement associé à une base de données vectorielle contenant les données à récupérer. 

<!-- -->

- Le composant d’IA générative, généralement un LLM. 

En réponse aux requêtes des utilisateurs en langage naturel, le modèle de plongement convertit la requête en plongement vectoriel, puis récupère les données similaires dans la base de connaissances. Le système d’IA combine les données récupérées avec la requête de l’utilisateur pour générer une réponse contextuelle.

### Qu’est-ce que l’IA agentique ?

L’IA agentique est un type d’IA capable de déterminer et d’effectuer un plan d’action de manière autonome. La plupart des agents disponibles au moment de la publication sont des LLM dotés de capacités d’appel de fonctions, ce qui signifie qu’ils peuvent appeler des outils pour effectuer des tâches. En théorie, les agents d’IA sont des LLM dotés de trois caractéristiques essentielles : 

- Ils disposent d’une **mémoire** à court et à long terme, ce qui leur permet de planifier et d’exécuter des tâches complexes. La mémoire permet également aux agents de se référer aux tâches précédentes et d’utiliser ces données pour éclairer les workflows futurs. Les systèmes de RAG agentique utilisent la mise en cache sémantique pour stocker les ensembles de requêtes, le contexte et les résultats précédents et s’y référer. 

<!-- -->

- Ils sont dotés de capacités de **routage** des requêtes, de **planification** étape par étape et de prise de décision. Les agents utilisent leurs capacités de mémoire pour conserver des informations et préparer un plan d’action approprié en réponse à des requêtes et des prompts complexes. 

<!-- -->

- Ils peuvent **appeler des outils** via des API. Les agents plus compétents peuvent choisir les outils à utiliser pour le workflow généré en réponse aux interactions des utilisateurs. 

Les workflows agentiques peuvent ne faire intervenir qu’un seul agent IA ou des systèmes multi-agents qui en associent plusieurs. 

## RAG agentique et systèmes RAG traditionnels

La RAG agentique apporte plusieurs améliorations significatives par rapport à une mise en œuvre traditionnelle de la RAG :

- **Flexibilité :** les applications de RAG agentique extraient des données de plusieurs bases de connaissances externes, et elles permettent d’utiliser des outils externes. Les pipelines RAG standard connectent un LLM à un seul jeu de données externe. Par exemple, de nombreux systèmes RAG d’entreprise associent un chatbot à une base de connaissances contenant les données propriétaires de l’organisation.

- **Adaptabilité :** les systèmes RAG traditionnels sont des outils de récupération de données réactifs qui trouvent des informations pertinentes en réponse à des requêtes spécifiques. Le système RAG n’est pas capable de s’adapter à des contextes changeants ou d’accéder à d’autres données. La génération de résultats optimaux nécessite souvent un prompt engineering étendu.

  De son côté, la RAG agentique constitue un pont entre l’interrogation statique basée sur des règles et la résolution intelligente et adaptative des problèmes. Les systèmes multi-agents encouragent plusieurs modèles d’IA à collaborer et à vérifier le travail des uns des autres.

- **Exactitude :** les systèmes RAG traditionnels n’effectuent ni la validation ni l’optimisation de leurs propres résultats. Les utilisateurs doivent déterminer eux-mêmes si le système fonctionne à un niveau acceptable. Le système lui-même n’a aucun moyen de savoir s’il trouve les bonnes données ou s’il les intègre correctement pour générer des résultats contextuels. Cependant, les agents IA peuvent itérer sur les processus précédents pour optimiser les résultats au fil du temps.

- **Évolutivité :** grâce à des réseaux d’agents RAG qui collaborent, qui exploitent de multiples sources de données externes et utilisent des capacités d’appel d’outils et de planification, la RAG agentique est plus évolutive. Les développeurs peuvent créer des systèmes RAG flexibles et évolutifs capables de gérer un large éventail de requêtes utilisateur. 

- **Multimodalité :** les systèmes de RAG agentique tirent parti des avancées récentes en matière de LLM multimodaux, ce qui leur permet de fonctionner avec un plus grand éventail de types de données, tels que les images et les fichiers audio. Les modèles multimodaux peuvent traiter divers types de données structurées, semi-structurées et non structurées. Par exemple, plusieurs modèles GPT récents peuvent générer du contenu visuel et audio en plus de la génération de texte standard.

Prenons un exemple. Plusieurs employés travaillent dans un bureau. Un système RAG traditionnel peut être comparé à un employé qui est performant lorsqu’on lui confie des tâches spécifiques et qu’on lui explique comment les accomplir. Cet employé n’aime pas prendre d’initiatives ni aller au-delà des instructions explicites qu’on lui a données. 

Un système de RAG agentique peut quant à lui être comparé à une équipe proactive et créative. Les membres de cette équipe sont tout aussi capables de suivre des instructions, mais ils aiment prendre des initiatives et résoudre les défis par eux-mêmes. Ils n’ont pas peur de proposer leurs propres solutions à des tâches complexes, une démarche qui pourrait perturber ou intimider leurs collègues.

### La RAG agentique est-elle plus efficace que la RAG traditionnelle ? 

Bien que la RAG agentique optimise les résultats grâce à l’appel de fonctions, au raisonnement à plusieurs étapes et aux systèmes multi-agents, il ne s’agit pas toujours de la meilleure option. Mettre un plus grand nombre d’agents au travail entraîne des dépenses plus importantes, et un système de RAG agentique implique généralement l’achat de tokens supplémentaires. Si la RAG agentique peut accélérer les tâches par rapport à la RAG traditionnelle, les LLM introduisent également une latence, car le modèle peut avoir besoin de plus de temps pour générer ses sorties.

Enfin, les agents ne sont pas toujours fiables. Selon la complexité et les agents utilisés, ils peuvent avoir du mal à accomplir certaines tâches. Les agents ne collaborent pas toujours de manière fluide et peuvent se faire concurrence sur les ressources. Plus il y a d’agents dans un système, plus la collaboration devient complexe et les risques de complications élevés. Même le système RAG le plus étanche ne peut pas éliminer entièrement le risque d’hallucination.

## Comment fonctionne la RAG agentique ?

Elle intègre un ou plusieurs types d’agents d’IA dans les systèmes RAG. Un système de RAG agentique peut par exemple combiner plusieurs agents de recherche d’information, chacun étant spécialisé dans un certain domaine ou type de source de données. Un agent consulte des bases de données externes tandis qu’un autre peut parcourir les e-mails et les résultats du Web.

Des cadres d’IA agentique, tels que LangChain et LlamaIndex, ainsi que le cadre d’orchestration LangGraph, sont disponibles sur GitHub. Grâce à eux, il est possible d’expérimenter des architectures agentiques pour la RAG à moindre coût. S’ils utilisent des modèles open source tels que Granite ou Llama-3, les concepteurs de systèmes RAG peuvent également réduire les frais autrement réclamés par d’autres fournisseurs tels qu’OpenAI, tout en bénéficiant d’une meilleure observabilité.

Les systèmes de RAG agentique peuvent contenir un ou plusieurs types d’agents IA :

- Agents de routage

<!-- -->

- Agents de planification de requêtes

<!-- -->

- Agents ReAct

<!-- -->

- Agents de planification et d’exécution

### Agents de routage

Les agents de routage déterminent quelles sources de connaissances et quels outils externes sont utilisés pour gérer une requête utilisateur. Ils traitent les prompts de l’utilisateur et identifient le pipeline RAG le plus susceptible de générer des réponses optimales. Dans un système RAG mono-agent, un agent de routage choisit la source de données à interroger.

### Agents de planification de requêtes

Les agents de planification de requêtes sont les gestionnaires de tâches du pipeline RAG. Ils traitent les requêtes complexes des utilisateurs en les décomposant en processus étape par étape. Ils envoient les sous-requêtes résultantes aux autres agents du système RAG, puis combinent leurs réponses pour former une réponse globale cohérente. L’utilisation d’un agent pour gérer d’autres modèles d’IA est un type de processus d’orchestration de l’IA.

### Agents ReAct

ReAct (raisonnement et action) est un cadre d’agents qui crée des [systèmes multi-agents](https://www.ibm.com/fr-fr/think/topics/multiagent-system) capables de créer des solutions étape par étape et de les mettre en action. Ces systèmes peuvent également identifier les outils qui peuvent les aider. En fonction des résultats de chaque étape, les agents ReAct peuvent ajuster les étapes suivantes du workflow généré de manière dynamique.

### Agents de planification et d’exécution

Les cadres d’agents de planification et d’exécution sont une évolution des agents ReAct. Ils peuvent exécuter des workflows en plusieurs étapes sans rappeler l’agent principal, pour des coûts réduits et une meilleure efficacité. Et comme l’agent de planification doit raisonner sur toutes les étapes nécessaires à une tâche, les taux d’achèvement et la qualité ont tendance à être plus élevés.

## Cas d’utilisation de la RAG agentique

Bien que la RAG agentique puisse convenir à n’importe quelle application RAG traditionnelle, les exigences de calcul plus importantes la rendent plus appropriée aux situations qui nécessitent l’interrogation de plusieurs sources de données. Voici quelques exemples d’applications de RAG agentique :

- **Réponses aux questions en temps réel :** les entreprises peuvent déployer des chatbots et des FAQ alimentés par la RAG pour fournir à leurs employés et à leurs clients des informations à jour et précises.

<!-- -->

- **Support automatisé :** les entreprises qui souhaitent rationaliser les services de support client peuvent utiliser des systèmes RAG automatisés pour traiter les demandes des clients plus simples. Le système de RAG agentique peut transmettre les demandes d’assistance plus exigeantes au personnel humain.

<!-- -->

- **Gestion des données :** les systèmes RAG facilitent la recherche d’informations dans les magasins de données propriétaires. Les employés peuvent obtenir rapidement les données dont ils ont besoin sans avoir à parcourir eux-mêmes les bases de données.
