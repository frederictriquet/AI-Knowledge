> Source : https://www.ibm.com/fr-fr/think/topics/ai-agent-memory

# Qu’est-ce que la mémoire des agents IA ?

La mémoire des agents IA désigne la capacité d’un système d’intelligence artificielle (IA) à stocker et à retrouver des expériences passées afin d’améliorer la prise de décision, la perception et les performances globales.\
\
Contrairement aux modèles IA traditionnels qui traitent chaque tâche indépendamment, les agents IA dotés de mémoire peuvent conserver le contexte, reconnaître des modèles au fil du temps et s’adapter en fonction des interactions passées.Cette capacité est essentielle pour les applications d’IA orientées vers des objectifs, qui exigent des boucles de rétroaction, des bases de connaissances et un apprentissage adaptatif.

La mémoire est un système qui se souvient de quelque chose concernant des interactions précédentes. Les agents IA n’ont pas nécessairement besoin de tels systèmes. Les agents réflexes simples, par exemple, perçoivent des informations en temps réel sur leur environnement et agissent en conséquence ou transmettent ces informations.

Un thermostat basique n’a pas besoin de se souvenir de la température d’hier. Mais un thermostat « intelligent » plus avancé, doté d’une mémoire, peut aller au-delà de la simple régulation de la température en identifiant des tendances, en s’adaptant au comportement de l’utilisateur et en optimisant l’efficacité énergétique. Plutôt que de réagir uniquement à la température actuelle, il peut stocker et analyser les données passées afin de prendre des décisions plus intelligentes.

Les grands modèles de langage (LLM) ne peuvent pas, à eux seuls, mémoriser des informations. Il est nécessaire d’y ajouter un composant mémoire. Cependant, l’un des plus grands défis de la conception de la mémoire de l’IA est l’optimisation de l’efficacité de la récupération, car le stockage excessif de données peut entraîner des temps de réponse plus lents.\
\
Une gestion optimisée de la mémoire permet de garantir que les systèmes d’IA ne stockent que les informations les plus pertinentes tout en conservant un traitement à faible latence pour les applications en temps réel.

## Types de mémoire agentique

Les chercheurs classent la mémoire agentique de la même manière que les psychologues classent la mémoire humaine. Rédigé par une équipe de l’université de Princeton, l’article phare Cognitive Architectures for Language Agents (CoALA)1 décrit différents types de mémoire :

### Mémoire à court terme

La mémoire à court terme (STM) permet à un agent IA de se souvenir des entrées récentes pour prendre des décisions immédiates. Ce type de mémoire est utile dans l’IA conversationnelle, où il est nécessaire de préserver le contexte au cours de multiples échanges.\
\
Ainsi, un chatbot qui se souvient des messages précédents au cours d’une session peut fournir des réponses cohérentes au lieu de traiter chaque entrée utilisateur de manière isolée, ce qui améliore l’expérience utilisateur. Par exemple, ChatGPT d’OpenAI conserve l’historique des conversations au sein d’une même session, ce qui contribue à rendre les conversations plus fluides et plus contextuelles.

La mémoire à court terme est généralement mise en œuvre à l’aide d’une mémoire tampon circulaire ou d’une fenêtre contextuelle, qui contient une quantité limitée de données récentes avant d’être écrasée. Si cette approche améliore la continuité dans les interactions courtes, elle ne conserve toutefois pas les informations au-delà de la session, ce qui la rend inadaptée à la personnalisation ou à l’apprentissage à long terme.

### Mémoire à long terme

La mémoire à long terme (LTM) permet aux agents IA de stocker et de récupérer des informations entre différentes sessions, les rendant ainsi plus personnalisés et plus intelligents au fil du temps.\
\
Contrairement à la mémoire à court terme, la mémoire à long terme est conçue pour le stockage permanent. Elle est souvent mise en œuvre à l’aide de bases de données, de graphes de connaissances ou d’embeddings vectoriels. Ce type de mémoire est essentiel pour les applications d’IA qui nécessitent des connaissances historiques, telles que les assistants personnalisés et les systèmes de recommandation.\
\
Par exemple, un agent de support client alimenté par l’IA peut se souvenir des interactions précédentes avec un utilisateur et adapter ses réponses en conséquence, améliorant ainsi l’expérience client globale.

La génération augmentée de récupération (RAG) est l’une des techniques les plus efficaces pour mettre en œuvre la mémoire à long terme. Elle consiste pour l’agent à extraire des informations pertinentes d’une base de connaissances stockée afin d’améliorer ses réponses.

#### Mémoire épisodique

La mémoire épisodique permet aux agents IA de se souvenir d’expériences passées spécifiques, de la même manière que les humains se souviennent d’événements individuels. Ce type de mémoire est utile pour le raisonnement basé sur des cas, où une IA apprend des événements passés afin de prendre de meilleures décisions à l’avenir.\
\
La mémoire épisodique est souvent mise en œuvre en enregistrant les événements clés, les actions et leurs résultats dans un format structuré auquel l’agent peut accéder lorsqu’il prend des décisions.\
\
Ainsi, un conseiller financier alimenté par l’IA peut se souvenir des choix d’investissement passés d’un utilisateur et s’appuyer sur cet historique pour lui fournir de meilleures recommandations. Ce type de mémoire est également essentiel dans la robotique et les systèmes autonomes, où un agent doit se souvenir d’actions passées pour naviguer efficacement.

#### Mémoire sémantique

La mémoire sémantique est chargée de stocker des connaissances factuelles structurées qu’un agent IA peut récupérer et exploiter dans son raisonnement. Contrairement à la mémoire épisodique, qui traite des événements spécifiques, la mémoire sémantique contient des informations généralisées telles que des faits, des définitions et des règles.\
\
Les agents IA implémentent généralement la mémoire sémantique à l’aide de bases de connaissances, d’IA symbolique ou d’embeddings vectoriels, leur permettant de traiter et de récupérer efficacement les informations pertinentes. Ce type de mémoire est utilisé dans des applications concrètes qui nécessitent une expertise dans un domaine particulier, telles que les assistants juridiques basés sur l’IA, les outils de diagnostic médical et les systèmes de gestion des connaissances d’entreprise.\
\
Par exemple, un assistant juridique alimenté par l’IA peut se servir de sa base de connaissances pour retrouver des précédents et fournir des conseils juridiques précis.

#### Mémoire procédurale

La mémoire procédurale des agents IA désigne la capacité à stocker et à se souvenir des compétences, des règles et des comportements appris qui permettent à un agent d’effectuer des tâches automatiquement sans avoir à raisonner explicitement à chaque fois.\
\
Elle s’inspire de la mémoire procédurale humaine, qui permet aux individus d’effectuer des actions telles que faire du vélo ou écrire à l’ordinateur sans réfléchir consciemment à chaque étape. Dans le domaine de l’IA, la mémoire procédurale aide les agents à améliorer leur efficacité en automatisant des séquences d’actions complexes sur la base d’expériences antérieures.

Les agents IA apprennent des séquences d’actions grâce à l’entraînement, souvent à l’aide de l’apprentissage par renforcement afin d’optimiser leurs performances au fil du temps. En stockant les procédures liées aux tâches, les agents IA peuvent réduire le temps de calcul et répondre plus rapidement à des tâches spécifiques sans avoir à traiter à nouveau les données depuis le début.

## Cadres pour la mémoire d’IA agentique

Les développeurs mettent en œuvre la mémoire à l’aide d’un stockage externe, d’architectures spécialisées et de mécanismes de rétroaction. Étant donné que les agents IA varient en complexité, allant des agents réflexifs simples aux agents d’apprentissage avancés, la mise en œuvre de la mémoire dépend de l’architecture de l’agent, du cas d’utilisation et de l’adaptabilité requise.

### LangChain

LangChain est un cadre clé pour la création d’agents IA dotés de mémoire, qui facilite l’intégration de la mémoire, des API et des workflows de raisonnement. En alliant LangChain à des bases de données vectorielles, les agents IA peuvent stocker et récupérer efficacement de grands volumes d’interactions passées, ce qui leur permet de fournir des réponses plus cohérentes au fil du temps.

### LangGraph

LangGraph permet aux développeurs de concevoir des graphiques de mémoire hiérarchiques pour les agents IA, améliorant ainsi leur capacité à suivre les dépendances et à apprendre au fil du temps.\
\
Grâce à l’intégration de bases de données vectorielles, les systèmes agentiques peuvent stocker efficacement les embeddings des interactions précédentes, ce qui permet un rappel contextuel. Cela est utile pour la génération de documents pilotée par l’IA, où un agent doit se souvenir des préférences des utilisateurs et des modifications passées.

### Autres solutions open source

L’essor des cadres open source a accéléré le développement d’agents IA à mémoire améliorée. Des plateformes telles que GitHub hébergent de nombreux référentiels qui fournissent des outils et des modèles pour intégrer de la mémoire dans les workflows d’IA.\
\
Hugging Face propose également des modèles pré-entraînés qui peuvent être affinés avec des composants de mémoire afin d’améliorer les capacités de rappel de l’IA. Python, langage dominant dans le développement de l’IA, fournit des bibliothèques pour gérer l’orchestration, le stockage et la récupération de la mémoire, ce qui en fait un choix incontournable pour la mise en œuvre de systèmes de mémoire d’IA.

##### Notes de bas de page

1 « Cognitive Architectures for Language Agents », Université de Princeton, février 2024.
