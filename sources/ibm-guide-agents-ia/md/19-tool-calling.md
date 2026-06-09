> Source : https://www.ibm.com/fr-fr/think/topics/tool-calling

# Qu’est-ce qu’un appel de fonction ?

L’appel d’outil désigne la capacité des modèles d’intelligence artificielle (IA) à interagir avec les outils, interfaces de programmation d’application ou systèmes externes pour en améliorer les fonctions.

Au lieu de s’appuyer uniquement sur les connaissances pré-acquises, un système d’IA doté de capacités d’appel d’outil peut interroger des bases de données, récupérer des informations en temps réel, exécuter des fonctions ou réaliser des opérations complexes au-delà de ses capacités natives.

L’appel d’outil, parfois appelé appel de fonction, est un catalyseur clé de l’IA agentique. Il permet aux systèmes autonomes d’effectuer des tâches complexes en accédant et en agissant dynamiquement sur des ressources externes.\
\
En plus de répondre à des questions, les grands modèles de langage (LLM) avec appel d’outil peuvent automatiser les workflows, interagir avec les bases de données, résoudre des problèmes en plusieurs étapes, prendre des décisions en temps réel et bien plus encore.\
\
Avec ce changement, les LLM quittent leur statut d’assistants passifs pour devenir des agents numériques proactifs, capables de réaliser des tâches complexes.

## Pourquoi l’appel d’outil est-il important ?

Les grands modèles de langage (LLM) sont traditionnellement limités par les données sur lesquelles ils ont été entraînés, un processus qui peut s’avérer long et gourmand en ressources de calcul.\
\
Même si les principaux LLM sont entraînés sur d’immenses ensembles de données, le besoin de données en temps réel, de calculs externes et d’une meilleure interactivité a conduit à l’intégration de capacités d’appel d’outil.

Les premiers LLM, y compris GPT-2 d’OpenAI, étaient statiques. Ils généraient des réponses basées sur leurs données d’entraînement, sans avoir la possibilité d’extraire de nouvelles informations.\
\
Bien qu’impressionnants, ils manquaient de connaissances du monde réel et avaient du mal à répondre à des requêtes dynamiques nécessitant des données en direct, telles que des événements actuels, des cours de bourse ou des actions spécifiques à l’utilisateur.

Pour y remédier, les développeurs ont commencé à intégrer des plug-in, des API et des bases de données externes permettant aux modèles de demander et de traiter les informations en temps réel, au lieu de s’appuyer uniquement sur leurs données d’entraînement statiques.\
\
Les développeurs ont entraîné les LLM à reconnaître quand une requête nécessite une assistance externe. De plus, les systèmes externes ont souvent un schéma d’entrée particulier. L’outil appelle les réponses du modèle qui correspondent au schéma particulier employé par les systèmes externes.

## Comment fonctionne l’appel d’outil ?

L’appel d’outil implique plusieurs composants clés qui fonctionnent ensemble pour faciliter l’interaction de l’IA avec des outils externes. Les LLM modernes, dont Claude d’Anthropic, Llama 3 de Meta, Mistral et IBM Granite, possèdent tous des capacités d’appel d’outil, mais les gèrent chacun quelque peu différemment.

Le premier composant est le modèle d’IA lui-même, qui se rend compte s'il manque de connaissances ou s’il a besoin d’une fonction externe pour traiter une requête.\
\
Ensuite, le mécanisme de sélection des outils identifie les dépendances appropriées pour traiter la tâche donnée, qu’il s’agisse d’un moteur de recherche, d’une base de données ou d’une ressource informatique.\
\
Lorsqu’un outil est sélectionné, l’interface API entre en jeu pour permettre à l’IA d’envoyer des requêtes structurées et de recevoir des réponses dans un format lisible par une machine.\
\
Enfin, le système de traitement des réponses permet de s’assurer que les données récupérées sont formatées correctement et présentées à l’utilisateur de manière pertinente.

### Étape 1. Reconnaître la nécessité d’un outil

Supposons qu’un utilisateur demande à un LLM : « Quel temps fait-il à San Francisco en ce moment ? » L’IA s’appuie sur la compréhension du langage naturel pour établir qu’il a besoin de données météorologiques en temps réel, qui ne peuvent pas être puisées dans sa base de connaissances statique.

Un identifiant d’appel d’outil unique est attribué automatiquement à la requête faite par un modèle pour utiliser un outil, qui sert de numéro de suivi pour relier la requête au résultat correspondant.

### Étape 2. Sélectionner l’outil

L’IA identifie l’outil le mieux adapté à la tâche (en l’occurrence, la vérification d’une base de données météorologique actuelle). Cette étape permet de s’assurer que les informations extraites sont exactes et pertinentes.

Chaque outil contient des métadonnées et des informations structurées telles qu’un nom d’outil unique (ou un nom de fonction), ce qui permet au modèle et au système de l’identifier correctement. Parmi les autres métadonnées, citons la description, les paramètres de l’outil et les types d’entrée et de sortie requis.

Le modèle choisit un outil après avoir déterminé que les données doivent être obtenues à partir d’une sélection d’outils disponibles.

Les templates sont des formats de prompt structurés qui indiquent au modèle l’outil à utiliser, ainsi que les arguments à fournir, afin de mieux contrôler et structurer les interactions avec les API.\
\
Dans le contexte de l’appel d’outil, les arguments désignent les entrées structurées transmises à un outil ou à une fonction lancés par le modèle génératif. Ces arguments définissent les paramètres dont l’outil a besoin pour s’exécuter correctement.

Associer appel d’outil et la  génération augmentée par récupération (RAG) permet d’améliorer les capacités de l’IA. En effet, cela permet aux systèmes de récupérer des données tant structurées que non structurées afin de générer des sorties structurées.

Cette approche améliore la pertinence du contexte en récupérant les données les plus adaptées avant de générer une réponse, ce qui favorise des sorties plus informées et plus précises.\
\
Elle optimise également l’utilisation des API en regroupant plusieurs extractions au sein d’une seule et même étape, afin de réduire les coûts et la latence. Plus flexible qu’un appel d’outil traditionnel, la RAG permet aux modèles de puiser dans diverses sources et de s’adapter parfaitement à différents domaines.\
\
Contrairement à la structure rigide des outils traditionnels, la RAG permet une intégration plus fluide des connaissances récupérées aux fonctions de raisonnement et de génération, ce qui se traduit par des réponses plus dynamiques et plus pertinentes.

### Étape 3. Construire et envoyer une requête

L’IA formule ensuite une requête structurée que l’outil ou l’API peuvent comprendre.

Chaque outil est associé à des fonctions bien spécifiques, qui définissent son rôle. Ces fonctions s’appuient sur une référence d’API, qui fournit la documentation nécessaire pour bien interagir avec l’API de l’outil, notamment les URL des points de terminaison, les méthodes de requête et les formats de réponse.

Pour accéder à une API externe, bon nombre de services requièrent une clé API, c’est-à-dire un identifiant unique qui les autorise à faire des requêtes. Lorsque l’outil est sélectionné et que les paramètres sont définis, un appel d’API est effectué pour récupérer les données demandées. Cette requête est généralement envoyée via HTTP à un serveur externe.

### Étape 4. Recevoir et traiter la réponse

L’outil externe renvoie des données. L’IA doit ensuite analyser les résultats de l’outil. Pour une requête météorologique, l’API peut répondre avec un objet de schéma JSON contenant la température, l’humidité et la vitesse du vent. L’IA filtre et structure ces données pour fournir une réponse pertinente à l’utilisateur.

### Étape 5. Présenter les informations ou prendre des mesures

L’IA fournit les informations traitées de manière intuitive. Si la requête implique une automatisation, telle que la configuration d’un rappel, l’IA confirmera qu’une action a été planifiée.

### Étape 6. Affiner la recherche

Si l’utilisateur demande plus de détails ou des modifications, l’IA peut répéter le processus avec une requête ajustée, afin de continuer à affiner sa réponse en fonction des besoins de l’utilisateur.

LangChain est couramment utilisé dans l’appel d’outil en fournissant un cadre open source pour l’intégration d’outils externes, d’API et de fonctions avec des LLM. Il facilite la gestion de l’exécution des outils, le traitement des entrées et des sorties, ainsi que la prise de décision en fonction du contexte.\
\
Par exemple, LangChain traite les arguments des fonctions avec un analyseur syntaxique pour les requêtes utilisateur, en extrayant les paramètres pertinents et en les formatant pour s’adapter à l’outil. Contrairement à un simple appel d’outil, LangChain peut stocker et rappeler les sorties d’outil précédentes, afin d’améliorer les interactions multitours.\

LangChain permet de combiner plusieurs outils en séquence pour des workflows plus complexes. Par exemple, il peut tout d’abord récupérer les données auprès de l’API météo, puis utiliser un autre outil pour recommander des vêtements en fonction des prévisions météorologiques.

## Types d’appels d’outil

L’appel d’outil permet aux LLM de réaliser toutes sortes de tâches. Si les cas d’utilisation sont infinis, voici 5 catégories courantes d’applications d’IA qui utilisent l’appel d’outil, accompagnées d’exemples concrets.

### Extraction et recherche d’informations

L’IA récupère les données en temps réel à partir du Web, de sources d’actualité, de bases de données universitaires ou de marchés financiers. Par exemple, un modèle de chat alimenté par l’IA peut appeler une API de recherche pour obtenir les cours des actions en temps réel ou les derniers articles de recherche sur l’IA et fournir ces informations par le biais d’un chatbot.

### Exécution du code

Cela permet à l’IA de réaliser des calculs complexes ou d’exécuter des scripts à l’aide de moteurs mathématiques tels que Wolfram Alpha ou les environnements d’exécution Python. Cela est utile pour résoudre des équations, effectuer des simulations ou exécuter de petits extraits de code.

### Automatisation des processus

L’IA automatise des workflows tels que la planification de réunions, l’envoi d’e-mails ou encore la gestion des listes de tâches grâce à l’intégration de plateformes comme Google Agenda et Zapier. Les agents d’IA peuvent interagir avec des outils CRM, financiers et analytiques comme Salesforce et QuickBooks, pour permettre aux entreprises d’automatiser leurs processus, notamment la récupération des données client ou le reporting financier.

### Appareils intelligents et surveillance de l’IdO

Les systèmes d’IA agentique permettent de surveiller et de contrôler les systèmes d’automatisation, les objets connectés à usage professionnel et la robotique. On peut facilement imaginer qu’un jour, les workflows soient gérés de bout en bout par des agents autonomes.
