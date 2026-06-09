> Source : https://www.ibm.com/fr-fr/think/topics/model-context-protocol

# Qu’est-ce que le MCP ?

## Qu’est-ce que le MCP ?

Le Model Context Protocol (MCP) agit comme une couche de standardisation pour permettre aux applications d’[IA](https://www.ibm.com/fr-fr/think/topics/artificial-intelligence) de communiquer efficacement avec des services externes tels que des [outils](https://www.ibm.com/fr-fr/think/topics/tool-calling), des [bases de données](https://www.ibm.com/fr-fr/think/topics/database) et des modèles prédéfinis.

Avez-vous déjà tenté de construire un [système multi-agent](https://www.ibm.com/fr-fr/think/topics/multiagent-system), mais rencontré des difficultés à diffuser efficacement les informations entre chaque agent spécialisé ? La variété d’outils préconfigurés ou personnalisés fournis à votre [agent d’IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) provoque-t-elle des erreurs d’exécution ou d’analyse de la sortie ? Ces complications vous ont-elles dissuadé de développer vos propres agents ?

Ces obstacles peuvent être surmontés grâce au Model Context Protocol (MCP). Le MCP permet aux agents d’IA d’être conscients du contexte, tout en respectant un protocole standardisé pour l’intégration d’outils.

Un [agent d’IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) est un système ou programme capable d’exécuter des tâches de manière autonome pour le compte d’un utilisateur ou d’un autre système. Il exécute ces tâches en concevant son propre workflow et en utilisant les outils disponibles. Les [systèmes multi-agents](https://www.ibm.com/fr-fr/think/topics/multiagent-system) sont composés de plusieurs agents d’IA travaillant collectivement pour exécuter des tâches au nom d’un utilisateur ou d’un autre système.

On peut comparer le rôle que joue le MCP pour les applications d’IA à celui d’un port USB-C pour le matériel informatique.1 Cette analogie met en parallèle l’adaptabilité des ports USB-C pour connecter le matériel à l’interface standardisée et universelle facilitant la connexion à différents outils et sources de données, fournissant ainsi le contexte aux [modèles d’IA](https://www.ibm.com/fr-fr/think/topics/ai-model) via le MCP.

## Les outils donnent du sens

[Les grands modèles de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models) comme [Granite](https://www.ibm.com/fr-fr/granite), Gemini et Llama sont limités dans leurs capacités lorsqu’ils sont déployés seuls. Sans outils d’IA externes, les LLM ont plusieurs compétences de base :

- Prédiction textuelle : demander à un LLM de compléter une phrase comme « Jack et Jill ont gravi la... » aboutira à « Jack et Jill ont gravi la colline ». Ce prompt et les réponses associées sont un exemple de prédiction textuelle, qui fonctionne mieux avec du texte sur lequel le modèle a été entraîné.

<!-- -->

- Questions-réponses basiques : un LLM seul n’a pas accès à des bases de données externes ou à la recherche Internet. Il peut donc uniquement répondre à des questions en langage naturel si la réponse figure dans ses données d’entraînement. Vous pouvez par exemple demander au LLM de vous « parler du traité de Versailles », car ces informations sur un conflit mondial majeur sont très probablement incluses dans les données d’entraînement des modèles à usage général. Les LLM génèrent souvent ce type de texte dans un [chatbot](https://www.ibm.com/fr-fr/think/topics/chatbots).

<!-- -->

- [Analyse des sentiments](https://www.ibm.com/fr-fr/think/topics/sentiment-analysis) : les LLM peuvent déterminer si un texte exprime un sentiment positif, négatif ou neutre.

<!-- -->

- Traduction linguistique : les LLM peuvent traduire des textes dans plusieurs langues et pour plusieurs zones géographiques. Cependant, tous les LLM ne sont pas entraînés sur des données multilingues.

En dehors de ces fonctions de base, un LLM sans accès à des outils externes ne peut pas traiter des requêtes nécessitant des informations en temps réel.

Afin de permettre aux LLM de produire des résultats plus pertinents, il est possible d’y intégrer des outils. En leur donnant accès à des outils [externes](https://www.ibm.com/fr-fr/think/topics/api) tels que la recherche Internet, des jeux de données et des API , l’utilisateur peut étendre leurs capacités au-delà de leurs données d’entraînement.

Pour aller encore plus loin, on peut construire des agents d’IA en combinant un LLM et ses outils disponibles.

Parce qu’ils leur donnent accès à tout un ensemble d’outils, ces systèmes agentiques permettent aux LLM de choisir l’outil approprié, de s’adapter aux changements dans l’environnement et de formuler des conclusions synthétisées à partir des résultats. Mais à grande échelle, ces systèmes d’IA échouent souvent.

C’est pourquoi le MCP, introduit par Anthropic en 2024, propose un standard ouvert pour les interactions IA-outils.2

## Le MCP établit une norme

Connecter des services externes à un LLM peut s’avérer laborieux. Imaginez un circuit électrique reliant un moteur à différentes sources d’énergie. Le MCP joue le rôle du câblage et du tableau de commande : il décide quel courant électrique (informations) alimente le moteur (modèle d’IA).

On peut comparer la sortie de l’outil ou le contexte du modèle au courant en entrée : il s’agit du courant provenant de la source d’alimentation, pouvant inclure la mémoire, les outils et les résultats précédents.

Dans son rôle de tableau de commande, le MCP décide quelles sources d’alimentation (sortie de l’outil ou contexte) connecter et à quel moment, régule le courant (flux d’informations), filtre et hiérarchise les entrées. Il veille à ce que seuls les câbles pertinents soient alimentés (le contexte pertinent est chargé) et gère le timing et le routage du circuit pour ne pas surcharger le système.

Tout comme un bon circuit évite les surtensions et optimise la consommation, le MCP joue le rôle de connecteur et assure une utilisation efficace, pertinente et structurée du contexte pour améliorer les performances des modèles d’IA.

Le MCP établit une nouvelle norme [open source](https://www.ibm.com/fr-fr/think/topics/open-source) sur laquelle les ingénieurs en IA peuvent s’accorder. Ce concept n’est pas nouveau dans l’industrie logicielle. Les [API REST](https://www.ibm.com/fr-fr/think/topics/rest-apis) en sont un exemple : elles permettent un échange de données cohérent entre applications grâce à des requêtes HTTP alignées sur les principes de conception REST.

De même, le MCP vise à unifier la communication entre les LLM et les services externes à travers une interface standardisée. Cette norme permet d’utiliser des outils « plug-and-play » plutôt que d’avoir à écrire du code pour créer une intégration personnalisée pour chaque outil.

Le MCP n’est pas un framework pour les agents, mais une couche d’intégration standardisée pour les agents qui accèdent à des outils. Il complète les cadres d’orchestration d’agents. Le MCP peut compléter les cadres d’orchestration d’agents comme [LangChain](https://www.ibm.com/fr-fr/think/topics/langchain), [LangGraph](https://www.ibm.com/fr-fr/think/topics/langgraph), [BeeAI](https://beeai.dev/), LlamaIndex et [crewAI](https://www.ibm.com/fr-fr/topics/crew-ai), mais il ne les remplace pas : le MCP ne décide pas quand un outil est appelé ni pour quel usage.

Le MCP se contente d’établir une connexion standardisée pour simplifier l’intégration des outils.3 C’est le LLM, au final, qui décide quels outils appeler selon le contexte de la requête utilisateur.

## Architecture MCP

Le modèle client/serveur MCP comporte trois principaux composants d’architecture :

- Hôte MCP
- Client MCP
- Serveur MCP

### Hôte MCP

Une application d’IA reçoit les requêtes des utilisateurs et cherche à accéder au contexte via le MCP. Cette couche d’intégration peut inclure des IDE tels que Cursor ou Claude Desktop. Elle contient la logique d’orchestration et peut connecter chaque client à un serveur. Elle contient la logique d’orchestration et peut connecter chaque client à un serveur.4

### Client MCP

Dans l’écosystème MCP, la communication entre l’hôte et le serveur doit obligatoirement passer par un client. Ce client existe au sein de l’hôte et convertit les requêtes des utilisateurs en un format structuré que le protocole ouvert peut traiter. Plusieurs clients peuvent coexister avec un seul hôte MCP, mais chaque client entretient une relation 1:1 avec un serveur MCP.

Parmi les exemples de clients MCP, on trouve IBM® BeeAI, Microsoft Copilot Studio, Claude.ai, Windsurf Editor et Postman.

Les clients jouent le rôle de gestionnaire de session en gérant les interruptions, les délais d’expiration, les reconnexions et les fermetures de session. Ils analysent également les réponses, gèrent les erreurs et vérifient que les réponses sont appropriées et pertinentes par rapport au contexte.4

### Serveur MCP

Le service externe fournit le contexte au LLM en convertissant les requêtes utilisateur en actions côté serveur. Parmi les intégrations possibles côté serveur MCP, on retrouve Slack, GitHub, Git, Docker ou la recherche Internet.

Ces serveurs sont en général des dépôts GitHub disponibles dans divers langages de programmation (C#, Java, TypeScript, Python, etc.) et donnent accès aux outils MCP.

Des tutoriels sont généralement inclus dans ces dépôts GitHub pour faciliter la mise en œuvre technique. Les serveurs MCP peuvent aussi servir à connecter les capacités d’[inférence des LLM](https://www.ibm.com/fr-fr/think/topics/ai-inference) au SDK MCP, via des fournisseurs de plateformes d’IA comme IBM ou OpenAI. Ce faisant, on crée un service MCP réutilisable auquel les clients peuvent accéder sous forme d’outil de discussion « standardisé ».

Les serveurs MCP sont polyvalents, car ils permettent des connexions aussi bien avec des ressources et outils internes qu’externes. Selon la documentation fournie par Anthropic, les serveurs Model Context Protocol exposent les données via :

- **Des ressources** : recherche d’informations à partir de bases de données internes ou externes. Les ressources renvoient des données, mais n’exécutent pas de calculs exploitables.5
- **Des outils** : échange d’informations avec des outils capables de provoquer un effet secondaire tel qu’un calcul ou une récupération de données via une requête API.6
- **Des prompts** : modèles et workflows réutilisables pour la communication LLM-serveur.7

La couche de transport entre les clients et les serveurs est responsable de la conversion bidirectionnelle des messages. Dans le flux client-serveur, les messages du protocole MCP sont convertis au format JSON-RPC, permettant le transport de différentes structures de données et de leurs règles de traitement.8

Dans le flux serveur-client, les messages reçus au format JSON-RPC sont reconvertis en messages de protocole MCP.9 es trois types de messages JSON-RPC sont les suivants : requêtes, réponses et notifications. Les requêtes nécessitent une réponse du serveur, contrairement aux notifications.

  Architecture du Model Context Protocol (MCP)

Dans la couche de transport entre les clients et les serveurs, deux méthodes principales sont utilisées pour transmettre les messages MCP au format JSON-RPC 2.0. Entrée/Sortie standard (stdio) : idéale pour intégrer des ressources locales en raison de la simplicité de transmission des informations d’entrée/sortie. Ce format est utilisé pour une communication synchrone et légère.4 Ces ressources comprennent les systèmes de fichiers locaux, les bases de données et les API locales.

Événements envoyés par le serveur (SSE) : méthode mieux adaptée à l’intégration de ressources distantes. Les requêtes HTTP POST servent à transmettre les messages du client au serveur, tandis que les réponses sont envoyées via SSE. Ce format permet de gérer en parallèle plusieurs appels asynchrones et pilotés par événements.4

## Avantages du MCP

Imaginez une IA capable de scanner votre boîte mail pour planifier des rendez-vous clients, envoyer des mises à jour boursières, et vous résumer la dernière heure d’activité sur Slack par SMS.

Chaque fournisseur de services construit ses API différemment, exigeant des informations spécifiques en entrée et produisant des formats de sortie variés. Ainsi, la moindre modification dans ces outils peut faire s’effondrer toute l’infrastructure du workflow d’IA.

Les ingénieurs doivent souvent consacrer beaucoup de temps à construire manuellement ces connexions entre outils, à les [déboguer](https://www.ibm.com/fr-fr/think/topics/debugging), et à gérer les systèmes d’authentification comme les clés API et les autorisations. Les outils dépendent souvent de la sortie d’autres outils, et de nombreux cas limites peuvent provoquer des échecs de connexion.

Il est donc crucial de fournir une couche d’intégration MCP entre les LLM et les outils de développement. À ce niveau, le MCP peut convertir les sorties des outils de façon compréhensible pour le modèle, sans avoir à jongler entre plusieurs interfaces en ligne de commande (CLI). L’intégration se fait à un seul et même endroit.

Il existe de nombreux cas d’utilisation concrets du MCP. Par exemple, le MCP améliore [l’orchestration](https://www.ibm.com/fr-fr/think/topics/ai-agent-orchestration) et la communication multi-agents grâce à un espace de travail partagé avec des outils communs, éliminant ainsi le besoin d’intégrations directes.3

Le MCP peut également être utilisé en complément de la [génération augmentée de récupération (RAG)](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation). Au lieu de faire appel à un agent de récupération pour faire des recherches dans une base de données vectorielle ou un base de connaissances, le MCP permet de se connecter à une [base de données vectorielle](https://www.ibm.com/fr-fr/think/topics/vector-database) via une action côté serveur.

Utiliser la recherche dans la base de données comme un outil plutôt que de faire intervenir l’agent de récupération à chaque appel de LLM permet une utilisation plus stratégique de l’outil. Cette approche permet également [d’appeler d’autres outils](https://www.ibm.com/fr-fr/think/topics/tool-calling) après récupération des données.3

## L’avenir du MCP

Le MCP représente une approche évolutive de l’intégration des outils aux LLM, qui continue de mûrir et de transformer le paysage au fil du temps. Alors que de nouveaux défis techniques apparaissent et que les serveurs MCP évoluent, la norme s’adapte et les capacités du protocole s’améliorent.

Dans tous les cas, une intégration normalisée des outils est essentielle pour permettre aux agents d’IA de fonctionner de manière autonome et de s’adapter dynamiquement aux environnements réels.10 

Grâce à MCP, il est possible de rationaliser des [workflows agentiques](https://www.ibm.com/fr-fr/think/topics/agentic-workflows) complexes avec moins de supervision humaine. Ce changement permet de consacrer plus de temps à des tâches plus nuancées exigeant intelligence et intuition humaines.
