> Source : https://www.ibm.com/fr-fr/think/topics/crew-ai

# Qu’est-ce que CrewAI ?

CrewAI est un cadre d’orchestration multi-agent open source créé par João Moura. Ce cadre basé sur Python tire parti de la collaboration entre les outils d’intelligence artificielle (IA) en orchestrant des agents d’IA autonomes ayant chacun un rôle et travaillant ensemble comme un groupe cohérent ou une « équipe » (crew) pour accomplir des tâches. L’objectif de CrewAI est de fournir un cadre solide d’automatisation des workflows multi-agents.1

Le terme « crew » fait référence aux agents IA impliqués dans la collaboration : ils délèguent des tâches de manière autonome et se posent des questions entre eux, comme une véritable équipe de travail. Chaque équipe multi-agent est composée d’agents IA complémentaires qui tirent parti d’outils existants et personnalisés pour accomplir l’ensemble de tâches qui leur est attribué. Les modèles de langage agissent comme un moteur de raisonnement pour les agents en sélectionnant une série d’actions.2 Les agents de CrewAI peuvent être configurés pour utiliser n’importe quel grand modèle de langage (LLM) ou interface de programmation des applications (API) open source.

Les recherches récentes étendent le champ d’application des modèles LLM au-delà de la simple génération de texte, démontrant qu’ils peuvent servir d’agents polyvalents pour les interactions conversationnelles, la prise de décision et l’exécution de tâches.3 Dans le domaine florissant de l’IA et de la recherche sur les agents d’IA et les cadres agentiques, les cadres des exigences multi-agents (dont CrewAI) ont fait leur arrivée sur la scène de l’IA générative.

La prochaine génération d’applications d’IA utilisera l’architecture agentique pour créer des systèmes autonomes basés sur des agents.4 Ces cadres agentiques s’attaquent à des tâches complexes applicables à une multitude de solutions d’IA en améliorant les tâches d’IA générative. Par exemple, les chatbots d’IA peuvent être une modalité de mise en œuvre de cadres d’IA agentique. Les chatbots agentiques, contrairement aux autres chatbots, peuvent utiliser les outils disponibles, planifier des actions avant de les exécuter et les conserver en mémoire. Ces capacités produisent des conversations plus sophistiquées et plus significatives.

## Cadres dédiés aux agents d’IA (agentiques)

Les cadres agentiques sont des architectures destinées aux agents d’IA qui utilisent l’appel d’outils et l’orchestration pour les applications d’IA. Les systèmes agentiques utilisent la planification, l’affinement itératif, la réflexion et d’autres mécanismes de contrôle pour tirer pleinement parti des capacités de raisonnement intégrées au modèle afin d’accomplir des tâches de bout en bout.5 La mise en œuvre d’agents d’IA au sein des systèmes d’IA automatise les processus nécessaires au bon fonctionnement des applications d’IA générative.

Les cadres agentiques offrent également des capacités d’apprentissage et des performances améliorées. Le réglage fin des LLM pour les tâches de prise de décision personnalisées nécessite beaucoup de ressources et peut diminuer les capacités de généralisation des modèles.6 Les agents d’IA peuvent apprendre de leurs actions et expériences antérieures, allégeant ainsi les dépenses de calcul nécessaires au réglage fin des modèles.\

## Architecture des systèmes agentiques

Les cadres agentiques peuvent utiliser des systèmes mono-agents ou multi-agents.

### Mono-agent et multi-agent

Les cadres mono-agents s’appuient sur un modèle de langage pour gérer un large éventail de tâches et de responsabilités. L’agent reçoit un prompt du système et les outils nécessaires à l’accomplissement de ses tâches lui sont fournis (recherche, API et autres agents). Bien que les systèmes mono-agents puissent interagir avec d’autres agents par le biais d’outils, ils ne coopèrent pas de la même manière que les systèmes multi-agents.

Dans les systèmes mono-agents, il n’existe aucun mécanisme de retour d’information provenant d’autres agents d’IA. Par conséquent, il est recommandé d’avoir l’option d’utiliser des commentaires humains pour guider l’agent afin d’améliorer sa précision au fil du temps. Les architectures mono-agents sont adaptées aux problèmes bien définis pour lesquels aucun retour d’information n’est nécessaire de la part d’autres agents ou utilisateurs.7

Plutôt que d’essayer de réunir toutes les capacités dans un seul modèle, les systèmes multi-agents (MAS) répartissent les tâches entre plusieurs agents spécialisés. Les architectures multi-agents impliquent deux agents ou plus, qui peuvent utiliser le même modèle de langage ou des modèles différents. Quelle que soit leur taille, les agents travaillent dans le même environnement pour modéliser les objectifs, la mémoire et le plan d’action de chacun. Ces architectures présentent des avantages notables par rapport à l’incitation à la chaîne de pensée (CoT), où le modèle doit décomposer les tâches en une série d’étapes.8 Les architectures multi-agents ont tendance à être plus efficaces lorsque les tâches impliquent une collaboration et plusieurs chemins d’exécution distincts.

Les meilleures architectures d’agents à utiliser dépendent des spécificités de l’application globale et du cas d’utilisation. Les systèmes mono-agents sont mieux adaptés à la résolution de problèmes restreints. On peut considérer les agents comme des résolveurs de problèmes. Certains problèmes nécessitent les capacités individuelles d’un agent spécialisé, d’autres peuvent nécessiter une équipe de résolveurs de problèmes, ou une équipe de plusieurs agents. Les systèmes multi-agents sont une équipe d’agents qui travaillent ensemble pour résoudre des problèmes qui dépassent les capacités ou les connaissances individuelles de chaque agent. Les systèmes multi-agents peuvent résoudre des problèmes trop vastes pour les systèmes mono-agents. Les recherches suggèrent que les systèmes multi-agents présentent des avantages significatifs, notamment une vitesse et une fiabilité accrues, et qu’ils ont une tolérance pour les données et les connaissances incertaines.9 Les principaux avantages des systèmes multi-agents similaires à CrewAI sont la collaboration entre agents, les workflows autonomes et l’évolutivité.

### Collaboration entre agents

Les agents d’IA peuvent être optimisés grâce à leurs paramètres personnalisables polyvalents. Chaque agent se voit attribuer un profil qui décrit son rôle ainsi que des instructions spécifiques pour son comportement.10 Les cadres multi-agents utilisent les capacités des différents agents pour gérer des tâches au sein d’une équipe : ces agents remplissent leurs rôles spécifiques tout en interagissant les uns avec les autres. La composition de ces équipes peut être adaptée et optimisée en fonction de l’application et des objectifs globaux.

L’une des façons de mettre en œuvre ce système est d’utiliser des agents génératifs collaboratifs. Les cadres multi-agents fournissent les compétences essentielles à une collaboration efficace.11 Certains cadres multi-agents fournissent des modèles de collaboration entre agents basés sur l’objectif global. CrewAI facilite la collaboration entre agents en permettant aux utilisateurs de regrouper les agents en équipes chargées d’effectuer une tâche ou d’atteindre un objectif commun.

### Comportement autonome

Les agents d’IA autonomes peuvent effectuer une tâche ou une série de tâches complexes sans être dirigés. Le potentiel des agents autonomes basés sur des LLM est reconnu comme une approche prometteuse pour l’intelligence artificielle générale (AGI).12 Ces agents basés sur des LLM peuvent exécuter des tâches via une planification et des actions autonomes. S’ils font preuve de capacités impressionnantes, les agents d’IA ont encore du mal à étendre leurs compétences aux tâches qui nécessitent des formes de raisonnement plus complexes.13 Les systèmes agentiques permettent de réduire ces difficultés en fournissant un cadre favorisant des workflows autonomes. Avec CrewAI, l’autonomie est reine grâce à un processus hiérarchique basé sur un agent manager généré de manière autonome qui supervise l’exécution des agents et l’attribution des tâches à ces derniers.

### Évolutivité

Les systèmes multi-agents doivent pouvoir évoluer à plusieurs niveaux. Par exemple : lorsque le nombre total d’agents augmente dans un système ou une application, que la diversité des agents augmente et que la taille des données sur ou avec lesquelles ils opèrent augmente.14 De nombreux cadres multi-agents sont livrés avec des outils de surveillance ou de mesure qui permettent d’évaluer les performances du système. CrewAI permet l’intégration avec des outils de surveillance des ressources et des outils de mesure tiers pour configurer l’observabilité et les évaluations des LLM, des cadres LLM et des bases de données vectorielles.

### Agents d'AI

Les agents d’IA sont des systèmes ou des programmes basés sur des LLM qui peuvent être développés pour effectuer diverses tâches complexes. Les agents possèdent des capacités de mémoire et de planification qui leur permettent de prendre des décisions de manière indépendante et d’agir en fonction de leurs expériences passées.15 Voici comment ces agents améliorent les capacités traditionnelles des LLM : ils utilisent les sorties d’un LLM pour invoquer d’autres outils logiciels (tels que la recherche de données), puis ils renvoient les résultats au LLM jusqu’à ce que l’objectif global soit atteint. Ce qui distingue les agents d’IA des LLM traditionnels, c’est leur capacité à naviguer, interagir et s’adapter à leur environnement grâce à la planification des actions, à l’utilisation de leur mémoire et à l’invocation d’outils. Les systèmes agentiques fournissent des outils et une orchestration permettant aux agents d’exécuter les algorithmes de machine learning associés à leurs tâches.

## Fonctionnement de CrewAI

CrewAI est construit sur la base de LangChain selon un principe de conception modulaire. Ses principaux composants sont les agents, les outils, les tâches, les processus et les équipes.

### Agents

Les agents sont les composants fondamentaux du cadre CrewAI. Chaque agent est une unité autonome chacune dotée d’un rôle différent qui contribue à l’objectif général de l’équipe. Chaque agent est programmé pour effectuer des tâches, prendre les décisions et communiquer avec les autres agents.\

CrewAI encourage les utilisateurs à considérer les agents comme les membres d’une équipe. Les agents peuvent avoir différents rôles tels que « Data scientist », « Chercheur » ou « Chef de produit ». L’équipe multi-agent collabore efficacement pour automatiser les workflows.\
 \
Cette forme de système multi-agent vise à améliorer les capacités de raisonnement des LLM via des discussions inter-agents en utilisant une structure de jeu de rôle pour permettre la résolution de problèmes complexes.16 Les agents interagissent les uns avec les autres via les mécanismes de délégation et de communication inhérents à CrewAI, ce qui leur donne la capacité innée de se connecter les uns aux autres pour déléguer des tâches ou poser des questions.

#### Attributs des agents

Les objectifs et les caractéristiques de l’agent sont définis par des attributs. Les agents de CrewAI ont trois attributs principaux **: un rôle**, **un objectif** et **un profil.**

Par exemple, l’instanciation d’un agent dans CrewAI peut ressembler à ce qui suit :

    agent = Agent(\
         **role=** 'Support client',\
         **goal=** 'Gère les demandes et les problèmes des clients',\
         **backstory=** 'Vous êtes spécialiste du support client pour un restaurant faisant partie d’une chaîne. Vous êtes chargé de gérer les appels des clients, de fournir\
         un support client et d’entrer les données de rétroaction.'\
         )\
 

CrewAI propose plusieurs paramètres facultatifs, notamment des attributs, permettant de choisir les LLM et les dépendances d’outils que l’agent utilisera.17

### Outils

Les outils sont des compétences ou des fonctions que les agents utilisent pour effectuer différentes tâches. Les utilisateurs peuvent tirer parti des outils personnalisés et existants des boîtes à outils CrewAI et LangChain.

Les outils étendent les capacités des agents en leur permettant d’effectuer un large éventail de tâches : gestion des erreurs, mécanismes de mise en cache et personnalisation via des arguments d’outils flexibles.\

#### Outils CrewAI

Tous les outils contiennent des mécanismes de gestion des erreurs et de mise en cache.

La boîte à outils CrewAI contient une suite d’outils de recherche qui utilisent la méthodologie de génération augmentée de récupération (RAG) dans différentes sources. En voici quelques exemples :

- **JSONSearchTool : **effectuez des recherches précises dans des fichiers JSON.
- **GithubSearchTool :** effectuez des recherches dans les référentiels GitHub.
- **YouTubeChannelSearchTool :** effectuez des recherches dans les chaînes YouTube.

Au-delà des outils de génération augmentée de récupération, le kit contient également divers outils de web scraping pour la collecte et l’extraction de données.

#### Outils LangChain

CrewAI permet une intégration simple aux outils LangChain. Voici quelques exemples d’outils intégrés disponibles avec LangChain :

- **Shell (bash) :** donne accès au shell, permettant au LLM d’exécuter des commandes shell.18
- **Document Comparison** : utilisez un agent pour comparer deux documents.19
- **Python :** permettez aux agents d’écrire et d’exécuter du code Python pour répondre aux questions.20

#### Outils personnalisés

Les utilisateurs peuvent créer leurs propres outils pour optimiser les capacités des agents. Avec le package d’outils CrewAI, les utilisateurs peuvent créer un outil en définissant une description claire de son utilisation. L’agent s’appuiera sur la description définie par l’utilisateur pour se servir de l’outil personnalisé. Les outils personnalisés peuvent éventuellement implémenter un mécanisme de mise en cache pouvant être affiné pour un contrôle granulaire.

### Tâches

Les tâches sont des missions spécifiques accomplies par les agents. Les détails relatifs à leur exécution sont définis dans les attributs des tâches. Plusieurs agents peuvent être désignés pour travailler ensemble à la réalisation d’une même tâche.

#### Attributs des tâches

Les attributs de tâche requis incluent **la description, l’agent** et **le résultat attendu**. Ces attributs définissent la portée de la tâche, l’agent qui en est responsable et son objectif. Une tâche peut être soit directement attribuée à un agent, soit gérée via le processus hiérarchique de CrewAI qui prend cette décision en fonction des rôles et de la disponibilité des agents.

Voici un exemple de tâche :

data_collection = Task(\
     **description=** ‘Recueillir des données à partir des interactions avec les clients, de l’historique des transactions et des tickets de support’\
     **expected_output=** ‘Un ensemble organisé de données pouvant être prétraitées’,\
     **agent=**data_science_agent,\
)

Les attributs de tâche facultatifs comprennent l’intégration, l’exécution asynchrone pour les tâches simultanées et les formats de sortie (y compris JSON), les modèles Pydantic et les sorties de fichiers pour les résultats des tâches.

#### Caractéristiques des tâches

Les caractéristiques des tâches comprennent l’intégration d’outils, l’exécution asynchrone, la révision humaine et la personnalisation des sorties.

Les résultats d’une tâche peuvent établir le contexte d’une tâche future. Par exemple, les résultats d’une tâche de « recherche » peuvent être utilisés comme contexte pour exécuter une tâche de « rédaction ». Prenons un exemple simple, une équipe de deux agents, un « agent de recherche » et un agent « rédacteur ». L’agent de recherche est chargé de trouver des exemples de cas d’utilisation d’IA générative de premier plan, et l’agent rédacteur peut utiliser la recherche résultante comme contexte pour effectuer la tâche de rédaction d’un court billet de blog sur le même sujet ou un sujet similaire.

Les tâches peuvent être définies pour s’exécuter de manière asynchrone. Cette approche est utile pour les tâches qui prennent beaucoup de temps ou qui ne sont pas nécessaires à l’exécution des tâches suivantes. L’attribut de contexte peut être utilisé pour indiquer à une tâche future d’attendre la sortie de la tâche asynchrone.21

### Processus

Les processus permettent aux agents d’IA individuels de fonctionner comme une unité cohérente en orchestrant l’exécution des tâches. Dans les cadres agentiques, les processus définissent la manière dont les agents collaboreront et les tâches qui leur seront attribuées. CrewAI assimile les processus à la gestion de projet car ils garantissent que les tâches sont distribuées et exécutées efficacement et qu’elles restent alignées sur une stratégie prédéfinie pour atteindre l’objectif.

CrewAI comprend deux implémentations de processus : séquentielle et hiérarchique, et prévoit une troisième implémentation appelée processus consensuel. Des processus peuvent être attribués à une équipe d’agents pour qu’elle fonctionne comme une unité cohérente. Lorsqu’un processus est attribué à une équipe, son type définit la stratégie d’exécution à appliquer.

- **Séquentiel :** le processus séquentiel est comparable à un workflow d’équipe dynamique. Les tâches sont exécutées selon l’ordre prédéfini dans la liste des tâches, la sortie d’une tâche servant de contexte à la suivante.
- **Hiérarchique :** le processus hiérarchique émule une hiérarchie d’entreprise. CrewAI génère de manière autonome un manager pour les utilisateurs en s’appuyant sur un modèle de langage de gestion adapté à l’agent manager.22 L’agent manager supervise l’exécution des tâches et les attribue aux agents en fonction de leurs capacités, examine les sorties et évalue l’achèvement des tâches. Ce processus est un exemple d’agents d’IA travaillant de manière autonome et collaborative pour accomplir un ensemble de tâches.
- **Consensuel (planifié) :** Au moment de la rédaction de cet article, le processus consensuel n’est actuellement pas mis en œuvre dans la base de code, mais il visera à fournir aux agents un moyen de prendre des décisions de manière collaborative concernant l’exécution des tâches. Ce processus introduit une approche démocratique de la gestion des tâches.

### Équipes

Une équipe est constituée d’un ensemble collectif d’agents qui collaborent pour accomplir un ensemble de tâches prédéfini.23 Chaque équipe définit la stratégie à appliquer à l’exécution des tâches, à l’exécution des agents et au workflow global. Les équipes possèdent plusieurs attributs qui leur permettent de réunir des agents avec des rôles et des outils complémentaires, d’attribuer des tâches et de sélectionner le processus qui dictera leur ordre d’exécution et leurs interactions.24

#### Attributs de l’équipe

Les utilisateurs choisissent et définissent la liste des agents qui travailleront ensemble dans l’équipe. Les équipes se voient attribuer une liste de tâches à accomplir. Les attributs facultatifs définissent la stratégie à appliquer à l’exécution, à la collaboration entre agents et au workflow global.

Voici l’exemple d’une équipe composée de deux agents dont le but est de collaborer pour collecter et organiser les données du support client :

my_crew = Crew(\
    **agents=**\[data_science_agent, customer_support_agent\],\
    **tasks=**\[customer_support_task, data_collection_task\],\
**    process=**Process.sequential,\
    **full_output=**True,\
    **verbose=**True,\
)

Les attributs supplémentaires incluent des fonctions de rappel, des paramètres de langue et de mémoire et des options permettant de définir un agent manager et un LLM à utiliser en fonction du flux de processus (par exemple, séquentiel, hiérarchique). Une fois l’équipe constituée, le workflow est lancé via une méthode de démarrage. CrewAI fournit plusieurs méthodes de démarrage pour contrôler le processus, notamment l’exécution de tâches asynchrones et individuelles.25

## Connexion à tous les LLM

crewAI peut se connecter à n’importe quel LLM via différentes options de connexion. Par défaut, les agents utilisent le modèle GPT-4 d’OpenAI pour le traitement du langage, mais CrewAI permet de se connecter à différents LLM, y compris des modèles tels que ceux de la série IBM Granite. Des modèles locaux peuvent être connectés via ollama ou d’autres API ouvertes. Des exemples de configurations d’API clés et des tutoriels sur la connexion à plusieurs LLM sont fournis dans la documentation de CrewAI. CrewAI est compatible avec tous les composants LLM LangChain, qui fournissent à tous les LLM un support de base pour une interface exécutable.

## Cas d’utilisation de CrewAI

Les cadres dédiés aux agents d’IA tels que CrewAI servent d’outils fondamentaux aux chercheurs et aux développeurs pour créer des systèmes intelligents dans divers domaines, allant des chatbots d’IA agentique aux systèmes multi-agents complexes.

Plusieurs exemples concrets incluent des projets tels que la création de pages de destination interactives et l’utilisation d’une équipe pour automatiser le processus de renforcement de la présence sur les réseaux sociaux. Un référentiel GitHub tenu par Moura intitulé « crewAI-examples » présente plusieurs exemples concrets que les utilisateurs peuvent tester eux-mêmes.26 Ces exemples incluent également des introductions à l’utilisation du framework pour les débutants.

Voici une liste de quelques exemples et d’autres cas d’utilisation émergents provenant de la communauté CrewAI :

- **Planification et création de contenu :** un cas d’utilisation s’appuie sur CrewAI et groq, un modèle de langage naturel, pour créer une équipe d’agents spécialisés dont l’objectif est de créer un contenu attrayant et factuellement précis sur un sujet donné.27
- **Automatisation de la vérification et de la rédaction d’e-mails :** exemple conçu comme une introduction pour les débutants, une équipe d’agents effectue les tâches d’analyse et de filtrage des e-mails, de récupération des fils de discussion, de recherche, et de création de brouillons en utilisant la bibliothèque LangGraph pour automatiser les workflows multi-agents.28
- **Analyse des actions :** les agents se voient attribuer des rôles spécifiques et collaborent pour fournir une analyse complète des actions et des recommandations d’investissement en utilisant GPT 3.5 au lieu du modèle GPT-4 par défaut.29

## Autres cadres multi-agents

CrewAI est comparable à des cadres multi-agents comme AutoGen et ChatDev. Le plus grand avantage de CrewAI, c’est qu’il combine les capacités individuelles de ces deux cadres. CrewAI combine la flexibilité des agents conversationnels d’AutoGen avec l’approche structurée des processus de ChatDev.30

### CrewAI et AutoGen

AutoGen est le cadre agentique open source de Microsoft. Il utilise des algorithmes de traitement automatique du langage naturel (NLP) pour les agents d’IA conversationnelle. Bien que les deux plateformes soient utilisées dans des applications similaires, elles ont chacune leurs avantages et leurs inconvénients. Ces systèmes flexibles sont tous deux dotés d’agents d’IA personnalisables capables de collaborer. CrewAI fournit un moyen plus simple d’orchestrer les interactions des agents en fournissant des attributs personnalisables qui contrôlent les processus de l’application. Autogen nécessite une programmation plus poussée pour y parvenir. AutoGen propose un moyen intégré d’exécuter rapidement le code généré par LLM.31 CrewAI ne propose actuellement pas d’outils en ce sens, mais permet d’y parvenir via une programmation supplémentaire.

### CrewAI et ChatDev

ChatDev est une plateforme open source qui utilise la collaboration multi-agent basée sur des rôles, y compris CrewAI. La structure de processus de ChatDev est rigide, ce qui limite la personnalisation et entrave l’évolutivité et la flexibilité dans les environnements de production. Les cadres comme CrewAI sont conçus pour s’intégrer à des applications tierces et à des workflows personnalisables pour des environnements dynamiques et adaptables. L’une des fonctionnalités uniques de ChatDev, c’est qu’il peut servir d’extension de navigateur pour enchaîner les conversations entre divers agents au sein d’un navigateur web.32

En tant que cadre d’orchestration multi-agent, CrewAI propose une autre innovation dans le domaine de l’intelligence artificielle. Les architectures agentiques vont venir améliorer les performances et les capacités des agents d’IA, permettant aux applications basées sur des LLM d’effectuer des tâches dépassant le simple cadre de la génération de langage.
