> Source : https://www.ibm.com/fr-fr/think/topics/langchain

# Qu’est-ce que LangChain ?

LangChain est un cadre d’orchestration open source qui permet de développer des applications à l’aide de grands modèles de langage (LLM). Disponibles dans les bibliothèques basées sur Python et Javascript, les outils et API de LangChain simplifient le processus de création d’applications pilotées par LLM telles que chatbots et agents IA. 

Interface générique pour la quasi-totalité des LLM, LangChain propose un environnement de développement centralisé qui permet de créer des applications LLM et de les intégrer à des sources de données externes, ainsi qu’à des workflows logiciels.

Grâce à l’approche modulaire de LangChain, les développeurs et les data scientists peuvent comparer dynamiquement différents prompts, et même différents modèles de fondation avec une réécriture de code minimale.

Cet environnement modulaire accepte également les programmes qui s’appuient sur plusieurs LLM (par exemple, une application qui s’appuie sur un LLM pour interpréter les requêtes utilisateur, et sur un autre LLM pour créer une réponse).

Lancé par Harrison Chase en octobre 2022, LangChain a connu une montée en puissance considérable : en juin 2023, il s’agissait du projet open source qui avait connu la plus forte croissance sur Github.1

À l’occasion du lancement massif de ChatGPT d’OpenAI le mois suivant, LangChain a joué un rôle important dans l’accès à l’IA générative aux passionnés et aux startups, ceci dans le cadre de sa popularité généralisée. Les progrès réalisés en matière d’accessibilité pour l’IA agentique entraînent actuellement une révolution dans l’automatisation.

LangChain facilite la plupart des cas d’utilisation des LLM et du traitement automatique du langage naturel (TAL): chatbots, recherche intelligente, réponse aux questions,  services de synthèse et agents IA permettant l’ automatisation robotisée des processus.

### Intégration avec les LLM

Les LLM ne sont pas des applications autonomes. Pour remplir leur vocation, ces modèles statistiques pré-entraînés doivent être associés à une application (et, dans certains cas, à certaines sources de données). 

Par exemple, Chat-GPT n’est pas un LLM, mais une application chatbot qui, selon la version choisie, s’appuie sur les modèles de langage GPT-3.5 ou GPT-4.

Alors que le modèle GPT interprète l’entrée de l’utilisateur et compose une réponse en langage naturel, c’est l’application qui (entre autres) fournit une interface permettant à l’utilisateur de saisir et de lire, ainsi qu’un design UX qui régit l’expérience chatbot. Même en entreprise, Chat-GPT n’est pas la seule application qui s’appuie sur le modèle GPT. En effet, Microsoft exploite GPT-4 pour alimenter Bing Chat.

En outre, bien que les modèles de fondation (comme ceux qui alimentent les LLM) soient pré-entraînés sur d’immenses jeux de données datasets, ils ne sont pas omniscients. Si une tâche donnée nécessite l’accès à des informations contextuelles bien spécifiques, comme une documentation interne ou des compétences sectorielles, les LLM doivent être connectés à ces sources de données externes.

Même si vous souhaitez tout simplement qu’il reflète en temps réel les événements actuels, votre modèle nécessitera des informations externes car ses données internes sont à jour uniquement pendant la période de pré-entraînement.

De la même manière, si une tâche d’IA générative donnée requiert l’accès à des workflows logiciels externes (par exemple, si vous souhaitez que votre agent conversationnel s’intègre à Slack), le LLM devra être intégré à l’API pour ce logiciel. 

Si ces intégrations peuvent généralement être réalisées manuellement à l’aide d’un code, les cadres d’orchestration tels que LangChain et le portefeuille de produits d’intelligence artificielle IBM watsonx simplifient fortement le processus. Essayer différents LLM pour comparer les résultats devient plus facile également, puisque les différents modèles peuvent être interchangés avec une modification minimale du code.

## Comment fonctionne LangChain ?

Au cœur de LangChain se trouve un environnement de développement pensé pour rationaliser la programmation d’applications LLM grâce à l’*abstraction*. Cette dernière consiste à simplifier le code en représentant un ou plusieurs processus complexes en tant que composant nommé qui englobe toutes ses étapes.

Intrinsèquement liée au langage, l’abstraction fait partie de notre quotidien. Par exemple, « *π* » nous permet de représenter le rapport de la circonférence d’un cercle à son diamètre sans avoir à écrire son nombre infini de décimales.

De même, un thermostat nous permet de contrôler la température dans notre logement sans avoir à comprendre les circuits complexes associés. Il suffit de savoir à quelles températures correspondent ses différents réglages.

LangChain est essentiellement une bibliothèque d’abstractions pour Python et Javascript, représentant les étapes et les notions courantes nécessaires à l’exploitation des modèles de langage.

Ces composants modulaires, comme les fonctions et les classes d’objets, constituent les éléments de base des programmes d’IA générative. Ils peuvent être « *enchaînés* » pour créer des applications, et permettent donc de réduire la quantité de code et les compétences requises pour réaliser des tâches TAL complexes.

Si l’approche abstraite de LangChain limite le degré de personnalisation des applications, elle permet tant aux experts qu’aux novices d’expérimenter et d’accélérer le prototypage.

### Importation des modèles de langage

Tout LLM, ou presque, peut être utilisé dans LangChain. Les modèles de langage sont faciles à importer dans LangChain, à condition de disposer d’une clé API. La classe *LLM* fournit une interface standard pour tous les modèles.

La plupart des fournisseurs LLM vous demanderont de créer un compte pour recevoir une clé API. Certaines de ces API, notamment les API destinées aux modèles propriétaires à source fermée, comme celles proposées par OpenAI ou Anthropic, peuvent impliquer des frais.

Bon nombre de modèles open source, comme LLaMa de Meta AI, Deepseek-LLM de Deepseek,Granite d'IBM et Flan-T5 de Google, sont accessibles par le biais de Hugging Face. Grâce à son partenariat avec Hugging Face,IBM watsonx propose également une suite de modèles open source rigoureusement sélectionnés. En créant votre compte auprès de l’un de ces deux services, vous pourrez générer une clé API pour le modèle de votre choix.

LangChain ne se limite pas aux modèles de fondation prêts à l’emploi : la classeCustomLLM  permet de créer des wrappers LLM personnalisés. Vous pouvez également utiliser les API d’IBM watsonx et le SDK Python, qui comprend une intégration LangChain, pour créer des applications dans LangChain à l’aide de modèles que vous avez déjà entraînés ou finement réglés selon vos besoins, grâce à la classe *WatsonxLLM* (et l’ ID associé au projet).

### Modèles de prompts

Les prompts sont les instructions données à un LLM. L’« art » de rédiger des prompts efficaces, qui fournissent au LLM le contexte nécessaire pour interpréter les entrées et structurer les sorties selon vos besoins, est généralement appelé prompt engineering.

La classe *PromptTemplate* de LangChain formalise la rédaction de prompts sans qu’il soit nécessaire de manuellement coder en dur le contexte et les requêtes. Les éléments importants du prompt sont également saisis comme des classes formelles telles que *input_variables*.

Un modèle de prompt peut donc contenir et reproduire un contexte, des instructions (comme « ne pas utiliser de termes techniques »), un ensemble d’exemples pour guider ses réponses (dans le cadre de ce que l’on appelle « apprentissage few-shot »), un format de sortie spécifié ou une question standardisée à laquelle il faut répondre. Ces modèles de prompt efficacement structurés peuvent être enregistrés, nommés et réutilisés selon vos besoins.

Bien que ces éléments puissent tous être codés manuellement, les modules *PromptTemplate* permettent une intégration fluide avec d’autres fonctionnalités LangChain, comme les *chaînes éponymes.*

### Chaînes

Comme leur nom l’indique, les *chaînes* sont au cœur des workflows LangChain. Elles relient les LLM aux autres composants pour créer des applications en exécutant une séquence de fonctions. 

La chaîne la plus basique est *LLMChain*. Elle appelle simplement un modèle et un prompt pour ce modèle. Par exemple, imaginez que vous ayez enregistré un prompt sous le nom « ExamplePrompt » et que vous souhaitiez l’exécuter sur Flan-T5.

Vous pouvez importer LLMChain depuis langchain.chains, puis définir *chain_example = LLMChain(llm = flan-t5, prompt = ExamplePrompt)*. Pour exécuter la chaîne pour une entrée donnée, appelez simplement *chain_example.run(“entrée”).*

Pour utiliser la sortie d’une fonction comme entrée pour la fonction suivante, vous pouvez utiliser *SimpleSequentialChain*. Pour chaque fonction, vous pouvez utiliser différents prompts, outils, paramètres ou même modèles selon vos besoins. 

### Index

Pour accomplir certaines tâches, les LLM doivent pouvoir accéder à des sources de données externes non incluses dans son jeu de données d’entraînement (documents internes, e-mails ou jeux de données). LangChain désigne collectivement ces documents externes par le terme « index ».

#### Chargeurs de documents

LangChain propose un large éventail de chargeurs de documents pour applications tierces (lien externe à ibm.com). Cela permet d’importer facilement des données à partir de sources telles que les services de stockage de fichiers (Dropbox, Google Drive ou Microsoft OneDrive), le contenu Web (YouTube, PubMed ou URL spécifiées), les outils de collaboration (Airtable, Trello, Figma ou Notion), ou encore les bases de données (Pandas, MongoDB ou Microsoft).

#### Bases de données vectorielles

Contrairement aux bases de données structurées « traditionnelles », les bases de données vectorielles convertissent les points de données en *représentations vectorielles*. Ces représentations numériques, ou vecteurs, comportent un nombre fixe de dimensions et regroupent généralement les points de données apparentés grâce aux méthodes d’apprentissage non supervisé.

Cela permet d’exécuter des requêtes à faible latence, même sur les jeux de données volumineux, ce qui représente un gain d’efficacité considérable. Représentations vectorielles stockent également les métadonnées de chaque vecteur, optimisant ainsi les recherches.

LangChain propose des intégrations pour plus de 25 méthodes de représentation vectorielle différentes, et pour plus de 50 magasins de vecteurs (hébergés dans le cloud, mais aussi locaux).

#### Séparateurs de texte 

Pour augmenter la vitesse et réduire les demandes de calcul, il est souvent préférable de diviser les documents texte volumineux en petits morceaux. Les séparateurs *TextSplitters* de LangChain découpent le texte en blocs sémantiques, que vous pouvez ensuite combiner à l’aide des méthodes et des paramètres de votre choix.

#### Récupération

Une fois les sources externes de connaissances connectées, le modèle doit être capable de récupérer et d’intégrer rapidement les informations pertinentes pour vos besoins. Tout comme watsonx, LangChain propose des fonctionnalités de génération augmentée par récupération (RAG) : ses modules de *récupération* acceptent une requête sous forme de chaîne en entrée et renvoient une liste de *documents* comme sortie.

Avec LangChain, nous pouvons également créer des systèmes RAG agentiques. Dans les applications RAG traditionnelles, le LLM dispose d’une base de données vectorielle pour s’y référer lors de la formation de ses réponses. En revanche, les applications d’IA agentique ne sont pas limitées à la seule récupération de données. RAG agentique peut également englober des outils pour des tâches telles que la résolution de calculs mathématiques, la rédaction d’e-mails, l’analyse de données et plus encore.

### Mémoire

Par défaut, les LLM ne conservent pas de mémoire à long terme des interactions précédentes (sauf si l’historique de chat concerné est utilisé comme entrée pour une requête). LangChain résout ce problème grâce à des fonctionnalités simples qui permettent d’ajouter de la capacité de mémoire à un système. Il dispose de différentes options : conserver les conversations dans leur intégralité, conserver un résumé de la conversation à ce jour, ou encore conserver les *n* échanges les plus récents.

### Outils

Malgré leur puissance et leur polyvalence reconnues, les LLM ont leurs limites non négligeables, à savoir un manque d’informations actualisées et de compétences sectorielles, ainsi que des difficultés en mathématiques.

Les outilsLangChain constituent un ensemble de fonctions conçues pour permettre aux agents LangChain d’interagir avec les informations du monde réel, afin d’étendre ou d’améliorer les services proposés.

### Exemples d’outils LangChain prédéfinis \

- **Wolfram Alpha :** associant fonctions de calcul et de visualisation des données puissantes, cet outil propose des capacités mathématiques avancées.

- **Google Search :** accès à la recherche Google pour fournir aux applications et aux agents des informations en temps réel.

- **OpenWeatherMap :** récupération de données météorologiques.

- **Wikipedia :** accès facilité aux informations contenues dans les articles Wikipedia.

## Agents LangChain

Nous pouvons créer un agent avec le cadre des exigences LangChain pour donner à un LLM la possibilité de prendre des décisions, d’utiliser des outils et d’effectuer des tâches complexes étape par étape, plutôt que de simplement générer une seule réponse textuelle. Contrairement à une simple interaction prompt-réponse avec un simple LLM, un agent optimisé par LangChain peut penser , planifier, exécuter une séquence d’actions, apprendre et adapter.

LangChain offre une expérience utilisateur rationalisée avec un cadre des exigences extensible et prêt à l’emploi pour créer des agents IA, il n’est donc pas nécessaire de créer une nouvelle logique de sélection d’outils, des boucles de raisonnement (comme pour les agents ReAct), un suivi des observations/actions ou une orchestration et formatage des prompts.

Les packages, les classes et les méthodes LangChain varient en fonction de la plateforme d’IA que vous souhaitez utiliser.

Voici quelques-unes des composantes clés de la classe *WatsonxLLM qui permettent de communiquer avec les modèles watsonx.ai grâce à LangChain :*

### *langchain_ibm*

Le package responsable de l’intégration de LangChain IBM. Il est nécessaire d’installer ce package pour utiliser l’une des classes et méthodes suivantes.

### *ibm_watsonx_ai *

La bibliothèque qui permet de se connecter aux services watsonx.ai comme IBM Cloud®  et IBM®  Cloud Pak for Data.

### *APIClient*

La classe principale de la  bibliothèque ibm_watsonx_ai qui gère les ressources du service API. Les paramètres incluent les identifiants de l’API et le point de terminaison.

### *WatsonxLLM*

L’enveloppe pour les modèles de fondation IBM watsonx®. Cet encapsuleur permet l’intégration de la chaîne et est nécessaire à l’importation. Les paramètres comprennent l’ID du modèle, la clé API watsonx.ai, le point de terminaison de l’URL, l’ID du projet, ainsi que tous les paramètres LLM.

### *ModelInferenc*e* *

Classe qui instancie l’interface du modèle. Les paramètres comprennent l’ID du modèle, les identifiants watsonx.ai, l’ID du projet, les paramètres du modèle et plus encore. Une fois instancié, le modèle peut être passé dans la classe.

### Appeler 

La méthode qui appelle le modèle directement à l’aide d’un prompt de type chaîne. 

### Générer

La méthode qui appelle le modèle avec plusieurs invites de type chaîne dans une liste.

Une autre classe LangChain pour la création d’agents IA avec l’intégration de l’appel et du chaînage d’outils avec les modèles watsonx.ai est *ChatWatsonx*.

### ChatWatsonx

La classe LangChain ChatWatsonx, qui est exploitée dans bon nombre de nos tutoriels, utilise la méthode *binlink_tools* pour transmettre une liste d’outils au LLM à chaque itération. Il peut s’agir d’outils personnalisés ou d’outils pré-créés.

Pour récupérer la réponse de l’agent IA, la méthode *invoke* peut être utilisée. Une fois l’agent invoqué, l’attribut *tool_calls* de la réponse affiche le nom, les arguments, l’identifiant et le type de chaque appel d’outil effectué, le cas échéant.

### LangGraph

LangGraph, créé par LangChain, est un cadre des exigences d’agent IA open source qui prend en charge l’orchestration multi-agent et permet aux développeurs de créer des workflows dans lesquels différents agents interagissent, se spécialisent et collaborent. 

À la base, LangGraph exploite la puissance des architectures basées sur des graphes pour modéliser et gérer les relations complexes entre les différents composants d’un workflow d’agent IA. Associé au mécanisme de surveillance « human-in-the-loop » et à un ensemble d’intégrations d’API et d’outils, LangGraph offre aux utilisateurs une plateforme polyvalente pour développer des solutions et des workflows d’IA, notamment des chatbots, des graphiques d’état et d’autres systèmes basés sur des agents. 

Avec la bibliothèque *langchain-mcp-adapters,*les agents LangGraph peuvent également utiliser des outils définis sur des serveurs MCP (model context Protocol).

La bibliothèque *mcp* permet également aux utilisateurs de créer des serveurs MCP personnalisés. Fondamentalement, le MCP permet une connexion sécurisée entre un système d’IA, comme un agent IA, et des outils externes.

Ainsi, différents LLM peuvent se connecter aux mêmes outils et sources de données compte tenu du MCP standard. 

## LangSmith

LangSmith, qui sortira à l’automne 2023, vise à combler l’écart entre les fonctionnalités de prototypage accessibles qui ont fait connaître LangChain et la création d’applications LLM de qualité professionnelle. 

LangSmith propose des outils pour surveiller, évaluer et déboguer les applications, notamment le suivi automatique des appels de modèles pour détecter les erreurs et tester la performance dans différentes configurations.

L’utilisation de LangSmith n’est pas limitée aux applications développées à l’aide de l’écosystème LangChain. L’évaluation des performances des agents est effectuée à l’aide d’évaluateurs LLM en tant que juge. Cette observabilité et ces indicateurs clés visent à optimiser des applications plus robustes et plus rentables. \

## Premiers pas avec LangChain

LangChain est open source et libre d’accès : le code source est disponible en téléchargement sur Github.

LangChain peut également être installé sur Python à l’aide d’une simple commande pip : *pip install langchain*. Pour installer toutes les dépendances de LangChain (et non seulement celles que vous jugez nécessaires), il suffit d’exécuter la commande *pip install langchain\[all\]*.

De nombreux tutoriels détaillés sont fournis par IBM, notamment l’appel d’outil LangChain, la RAG agentique, l’orchestration d’agent LLM, le découpage agentique et bien plus encore.

## Cas d’utilisation de LangChain

Les applications d’IA conçues avec LangChain offrent une grande utilité pour une variété d’utilisations, des tâches simples de réponse à des questions et de génération de texte aux solutions plus complexes qui utilisent un LLM comme « moteur de raisonnement ».

### Chatbots

Les chatbots font partie des utilisations les plus intuitives des LLM. LangChain peut être utilisé pour fournir un contexte pertinent selon la vocation des chatbots, mais aussi pour intégrer les chatbots dans les workflows et les canaux de communication existants, et ce avec leur propre API.

### Synthèse

Les modèles de langage peuvent être chargés de résumer différents types de textes, allant de la synthèse d'articles académiques complexes et de transcriptions à la fourniture d'un résumé des e-mails entrants.

### Réponse aux questions

En utilisant des documents spécifiques ou des bases de connaissances spécialisées (comme Wolfram, arXiv ou PubMed), les LLM peuvent récupérer des informations pertinentes et formuler des réponses utiles. S’ils sont finement réglés ou guidés par les prompts appropriés, certains LLM peuvent même répondre à bon nombre de questions sans informations externes.

### Augmentation des données

Les LLM permettent de générer des données synthétiques utilisables à des fins de machine learning. Par exemple, on peut entraîner un LLM pour générer des échantillons supplémentaires qui imitent les points de données contenus dans un jeu de données d’entraînement.

### Agents conversationnels

Intégrés aux bons workflows, les modules Agent de LangChain peuvent utiliser un LLM pour déterminer de manière autonome les prochaines étapes et agir en utilisant l'automatisation robotisée des processus (RPA).
