> Source : https://www.ibm.com/fr-fr/think/tutorials/multi-agent-autogen-rag-granite

# RAG multi-agents avec AutoGen : créer localement avec Granite

Peut-on créer des \[workflows agentiques\] hhttps://www.ibm.com/fr-fr/think/topics/agentic-workflows) sans avoir besoin de \[grands modèles de langage (LLM)\] extrêmement volumineux et coûteux (https://www.ibm.com/fr-fr/think/topics/large-language-models) ? La réponse est oui. Dans ce tutoriel, nous allons vous montrer comment construire un système RAG multi-agents local avec AutoGen IBM® \[Granite\].(https://www.ibm.com/fr-fr/granite).

## Présentation de la RAG agentique

[La génération augmentée par récupération (RAG)](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation) est un moyen efficace de fournir à un LLM des jeux de données supplémentaires provenant de différentes sources de données, sans avoir à effectuer des ajustements onéreux. De même, la [RAG agentique](https://www.ibm.com/fr-fr/think/topics/agentic-rag) fait appel à la capacité des [agents IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) à planifier et à exécuter des sous-tâches, ainsi qu’à la récupération d’informations pertinentes pour compléter la base de connaissances d’un LLM. Cette capacité permet l’optimisation et des applications RAG plus évolutives que les [chatbots](https://www.ibm.com/fr-fr/think/topics/chatbots) traditionnels. Nul besoin d’écrire des requêtes SQL complexes pour extraire les données pertinentes d’une base de connaissances.

L’avenir de la RAG agentique ? La RAG multi-agents, où plusieurs agents spécialisés [collaborent](https://www.ibm.com/fr-fr/think/topics/multi-agent-collaboration) pour atteindre une latence et une efficacité optimales. Nous démontrerons cette collaboration en utilisant un modèle efficace tel que Granite 3.2 et en l’associant à une architecture modulaire d’agents. Nous utiliserons plusieurs « mini-agents » spécialisés qui collaboreront pour accomplir des tâches grâce à une planification adaptative et à des appels d’outils ou de fonctions. Tout comme les humains, une équipe d’agents, ou un [système multi-agents](https://www.ibm.com/fr-fr/think/topics/multiagent-system), surpasse souvent les efforts héroïques d’un individu, surtout lorsque les rôles sont clairement définis et que la [communication](https://www.ibm.com/fr-fr/think/topics/ai-agent-communication) est efficace.

Afin d’[orchestrer](https://www.ibm.com/fr-fr/think/topics/ai-agent-orchestration) cette collaboration, nous pouvons utiliser AutoGen (AG2) comme [cadre](https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks) central pour gérer les workflows et la prise de décision, parallèlement à d’autres outils comme Ollama pour la mise à disposition locale des LLM, et Open WebUI pour l’interaction. AutoGen est un cadre conçu pour créer des applications d’IA multi-agents développées par Microsoft.1 Notamment, tous les composants utilisés dans ce tutoriel sont open source. Ensemble, ces outils vous permettent de créer un système d’IA puissant et respectueux de la vie privée, et ce sans quitter votre ordinateur portable.

## Architecture multi-agents : quand la collaboration l’emporte sur la concurrence

Notre agent de récupération Granite s’appuie sur une architecture modulaire au sein de laquelle chaque agent a un rôle spécialisé. Comme les humains, les agents sont plus performants lorsqu’ils disposent d’instructions ciblées et de suffisamment de contexte pour prendre une décision éclairée. Trop d’informations superflues, telles qu’un historique de discussion non filtré, peut créer un effet de type « aiguille dans la botte de foin », où il devient de plus en plus difficile de déchiffrer le signal du bruit.

  Architecture agentique

Dans cette [architecture d’IA agentique](https://www.ibm.com/fr-fr/think/topics/agentic-architecture), les agents travaillent ensemble de manière séquentielle pour atteindre un objectif donné. Voici comment le système d’IA générative est organisé :

**Agent planificateur** : il crée le plan de haut niveau au début du workflow. Par exemple, si l’utilisateur demande : « Quels sont les projets open source comparables à ceux que mon équipe utilise ? », l’agent élabore un plan étape par étape qui pourrait ressembler à ceci : « 1. Rechercher les technologies open source dans les documents de l’équipe. 2. Rechercher sur le Web les projets open source similaires à ceux trouvés à l’étape 1. » Si l’une de ces étapes échoue ou fournit des résultats insuffisants, elle peut être adaptée ultérieurement par l’agent de réflexion.

**Assistant de recherche** : l’assistant de recherche est le cheval de bataille du système. Il reçoit et exécute des instructions telles que « Rechercher les technologies open source dans les documents de l’équipe ». Pour l’étape 1 du plan, il utilise l’instruction initiale de l’agent planificateur. Pour les étapes suivantes, il reçoit également un contexte organisé, issu des résultats des étapes précédentes.

Par exemple, si on lui demande de « Rechercher sur le Web des projets open source similaires », il recevra également la sortie de l’étape de recherche de documents précédente. En fonction des instructions, l’assistant de recherche peut utiliser des outils tels que la recherche Web et la recherche de documents, ou les deux, pour accomplir sa tâche.

**Critique de l’étape :** la critique de l’étape permet de décider si le résultat de l’étape précédente a répondu de manière satisfaisante aux instructions qui lui ont été données. L’outil reçoit deux informations : l’instruction à une seule étape qui vient d’être exécutée et la sortie de cette instruction. Le fait d’avoir un avis critique d’étape permet de clarifier si l’objectif a été atteint, ce qui est nécessaire pour planifier les étapes suivantes.

**Juge de l’objectif :** le juge de l’objectif détermine si l’objectif final a été atteint, en se basant sur toutes les exigences de l’objectif fourni, les plans élaborés pour l’atteindre et les informations recueillies jusqu’à présent. La sortie du juge est « OUI » ou « PAS ENCORE », suivie d’une brève explication qui ne dépasse pas une ou deux phrases.

**Agent de réflexion** : l’agent de réflexion est notre décideur exécutif. Il décide de l’étape à suivre, qu’il s’agisse d’empiéter sur l’étape suivante planifiée, de modifier sa trajectoire pour rattraper les erreurs ou de confirmer que l’objectif a été atteint. Comme un vrai PDG, il prend ses meilleures décisions lorsqu’il a un objectif clair en tête et qu’on lui présente des conclusions concises sur les progrès réalisés ou non pour atteindre cet objectif. La sortie de l’agent de réflexion est soit la prochaine étape à franchir, soit les instructions pour terminer si l’objectif a été atteint. Nous présentons à l’agent de réflexion les éléments suivants :

- L’objectif
- Le plan initial
- La dernière étape exécutée
- Le résultat de la dernière étape indiquant la réussite ou l’échec
- Une séquence concise d’instructions précédemment exécutées (seules les instructions, sans leur sortie)

En présentant ces éléments dans un format structuré, notre décideur comprend clairement ce qui a été fait et peut décider de ce qui doit suivre.

**Générateur de rapports** : une fois l’objectif atteint, le générateur de rapports synthétise tous les résultats dans une sortie cohérente, qui répond directement à la requête d’origine. Alors que chaque étape du processus génère des sorties ciblées, le générateur de rapports rassemble le tout dans un rapport final.

## Tirer parti des outils open source

Pour les débutants, il peut être difficile de créer une application d’IA agentique à partir de zéro. Nous allons donc utiliser un ensemble d’outils open source. Granite Retrieval Agent intègre plusieurs outils pour la RAG agentique.

**Open WebUI** : l’utilisateur interagit avec le système via une interface de chat intuitive, hébergée dans Open WebUI. Cette interface sert de point principal pour l’envoi de requêtes (telles que « Cherche-moi les derniers articles d’actualité relatifs à mes notes de projet ») et l’affichage des sorties.

**Agent basé sur Python (cadre AG2)** : au cœur du système se trouve un agent basé sur Python et construit à l’aide d’AutoGen (AG2). Cet agent coordonne le workflow en décomposant les tâches et en appelant dynamiquement les outils pour exécuter les étapes.

L’agent a accès à deux outils principaux :

- Outil de recherche de documents : récupère les informations pertinentes auprès d’une base de données vectorielle contenant des notes de projet téléchargées ou des documents stockés sous forme d’embeddings. Cette recherche vectorielle tire parti des API de récupération documentaire intégrées à Open WebUI, au lieu de mettre en place un magasin de données distinct.

- Outil de recherche Web : effectue des recherches sur le Web pour recueillir des connaissances externes et des informations en temps réel. Dans le cas présent, nous utilisons SearXNG comme moteur de métarecherche.

**Ollama** : le LLM IBM® Granite 3.2 sert de modèle de langage pour alimenter le système. Il est hébergé localement à l’aide d’Ollama, ce qui garantit inférence rapide, rentabilité et protection des données. Si vous souhaitez exécuter ce projet avec des modèles plus grands, un accès API via IBM® [watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai) ou OpenAI, par exemple, est préférable. Cette approche requiert toutefois une clé d’API watsonx.ai ou OpenAI. Dans ce tutoriel, nous utilisons Ollama (hébergé localement).

Parmi les autres cadres d’agents open source courants, qui ne sont pas abordés dans ce tutoriel, citons [LangChain,](https://www.ibm.com/fr-fr/think/topics/langchain) [LangGraph](https://www.ibm.com/fr-fr/think/topics/langgraph) et [crewAI.](https://www.ibm.com/fr-fr/think/topics/crew-ai)

## Étapes

Les instructions de configuration détaillées et l’ensemble du projet sont disponibles sur  [IBM Granite Community GitHub.](https://github.com/ibm-granite-community/granite-retrieval-agent "Success - 200") La version Jupyter Notebook de ce tutoriel est également disponible sur [GitHub](https://github.com/IBM/ibmdotcom-tutorials).

Les étapes suivantes permettent de configurer rapidement l’agent de récupération Granite.

### Étape 1 : installer Ollama

Pour installer Ollama, il suffit de télécharger le client à partir du [site officiel d’Ollama](https://ollama.com/). Après avoir installé Ollama, exécutez la commande suivante pour extraire le LLM Granite 3.2.

```bash
ollama pull granite3.2:8b
```

Vous pouvez maintenant utiliser Ollama et Granite.

### Étape 2. Créer un agent simple (facultatif)

AutoGen Studio est une solution low code pour la création de workflows. Cependant, créer nous-mêmes un agent simple nous aidera à mieux comprendre la configuration de ce projet RAG multi-agents complet. Pour continuer, configurez un Jupyter Notebook dans l’environnement de développement intégré (IDE) de votre choix, et activez un environnement virtuel en exécutant les commandes suivantes dans votre terminal.

```bash
python3.11 -m venv venv
source venv/bin/activate
```

Nous aurons besoin de quelques bibliothèques et modules pour cet agent simple. Assurez-vous d’installer et d’importer les éléments suivants.

```
!pip install -qU langchain chromadb tf-keras pyautogen "ag2[ollama]" sentence_transformers
```

```python
import getpass
from autogen.agentchat.contrib.retrieve_assistant_agent import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
```

Il existe plusieurs paramètres de configuration à définir localement pour appeler le LLM approprié, que nous avons extrait en utilisant Ollama.

```json
ollama_llm_config = {
    "config_list": [
        {
            "model": "granite3.2:8b",
            "api_type": "ollama",
        }
    ],
}
```

Nous pouvons transmettre ces paramètres de configuration dans le paramètre « llm_config » de la classe « AssistantAgent » pour instancier notre premier agent IA.

```
assistant = AssistantAgent(
    name="assistant",
    system_message="You are a helpful assistant.",
    llm_config=ollama_llm_config,
)
```

Cet agent utilise Granite 3.2 pour synthétiser les informations renvoyées par l’agent « ragproxyagent ». Le document que nous fournissons à l’agent RAG comme contexte supplémentaire est le fichier brut README Markdown, qui se trouve dans le dépôt AutoGen sur GitHub. En outre, nous pouvons transmettre un nouveau dictionnaire de configurations spécifique à l’agent de récupération. Parmi les clés supplémentaires qui pourraient vous être utiles, citons « vector_db », « chunk_token_size » et « embedding_model ».

Pour obtenir la liste complète des clés de configuration, reportez-vous à la [documentation officielle](https://microsoft.github.io/autogen/0.2/docs/reference/agentchat/contrib/retrieve_user_proxy_agent/).

```json
ragproxyagent = RetrieveUserProxyAgent(
    name="ragproxyagent",
    max_consecutive_auto_reply=3,
    is_termination_msg=lambda msg: msg.get("content") is not None or "TERMINATE" in msg["content"],
    system_message = "Context retrieval assistant.",
    retrieve_config={
        "task": "qa",
        "docs_path": "https://raw.githubusercontent.com/microsoft/autogen/main/README.md",
        "get_or_create": True,
        "collection_name": "autogen_docs",
        "overwrite": True
    },
    code_execution_config=False,
    human_input_mode="NEVER",
)
```

Nous pouvons maintenant initier un chat avec notre agent RAG pour poser une question concernant le document fourni comme contexte.

```python
qs = "What languages does AutoGen support?"
result = ragproxyagent.initiate_chat(
    assistant, message=ragproxyagent.message_generator, problem=qs
)

print(result)
```

Veuillez noter que le contenu Markdown du fichier ReadME a été supprimé de la sortie pour plus de concision.

\*\* Sortie\*\* :

*Création d’une collection.*

*2025-07-21 12:20:36,125 - autogen.agentchat.contrib.retrieve_user_proxy_agent - INFO - 1 chunk trouvé.\
2025-07-21 12:20:36,129 - autogen.agentchat.contrib.vectordb.chromadb - INFO - Aucun embedding de contenu n’est fourni. La fonction embedding de VectorDB sera utilisée pour générer l’embedding de contenu.*

*VectorDB renvoie doc_ids : \[\['8e9131c7'\]\]\
Ajout du contenu du doc 8e9131c7 au contexte.*

***ragproxyagent** (à l’assistant) :\
\
Tu es un chatbot augmenté par récupération. Tu réponds aux questions de l’utilisateur en fonction de tes propres connaissances et du contexte fourni par l’utilisateur.\
Si tu ne peux pas répondre à la question, que ce soit avec ou sans le contexte actuel, tu dois répondre « METTRE À JOUR LE CONTEXTE ».\
Tu dois donner une réponse aussi courte que possible.\
\
La question de l’utilisateur est la suivante : Quelles sont les langues prises en charge par AutoGen ?\
\
Le contexte est le suivant : *

\[SUPPRIMÉ\]

------------------------------------------------------------------------

**assistant** (à ragproxyagent) :

Le texte fourni semble être un fichier README pour le projet AutoGen, une initiative open source de Microsoft. Voici un résumé de son contenu : 1. Présentation du projet : AutoGen est un système de création et de gestion d’applications complexes et distribuées. Il prend en charge plusieurs langages (C#, Python) et fournit un environnement d'exécution pour déployer et mettre à l'échelle ces applications. 2. Composants clés : - AutoGen Core : la bibliothèque de base contenant les classes et interfaces fondamentales pour la création d’applications AutoGen. - AutoGen Agent : un composant d’exécution chargé de gérer le cycle de vie des applications AutoGen. - AutoGen Runtime Gateway : un service qui facilite la communication entre les agents et permet l’équilibrage de charge, la mise à l’échelle et la tolérance aux pannes. 3. Langages pris en charge : C# et Python sont actuellement pris en charge. 4. Premier pas : le fichier README fournit des instructions pour installer les paquets nécessaires, créer un nouveau projet et construire/exécuter une application AutoGen. 5. Documentation : liens vers une documentation détaillée à des fins de référence, y compris des références d’API, des guides et des tutoriels. 6. Communauté et contribution : directives pour contribuer au projet, y compris des informations sur le suivi des problèmes, les demandes d’extraction et les normes de codage. 7. Mentions légales : informations sur les licences et les marques déposées. 8. Support et FAQ : informations sur la façon de poser des questions, de signaler les problèmes et de trouver des réponses aux requêtes courantes.

Le fichier README comprend également un tableau résumant les paquets disponibles pour chaque langage pris en charge (C# et Python) et leurs gestionnaires de paquets respectifs (NuGet et PyPI). Cela permet aux développeurs d’identifier rapidement les composants nécessaires pour démarrer avec AutoGen dans leur langage préféré.

------------------------------------------------------------------------

\>\>\>\>\>\>\>\> TERMINATING RUN (601a53dc-8a5d-4e19-8503-1517fe3c7634): Termination message condition on agent 'ragproxyagent' met

Super ! Notre agent assistant et notre agent RAG ont réussi à synthétiser le contexte supplémentaire permettant de répondre correctement à la requête de l’utilisateur avec les langages de programmation actuellement pris en charge par AutoGen. Vous pouvez considérer cela comme un chat de groupe entre des agents échangeant des informations. Cet exemple est une démonstration simple de la mise en œuvre locale d’une RAG agentique avec AutoGen.

### Étape 3. Installer Open WebUI

Nous allons maintenant créer un système RAG agentique plus avancé. Sur votre terminal, installez et exécutez Open WebUI.

```bash
pip install open-webui
open-webui serve
```

### Étape 4. Configurer la recherche Web

Pour la recherche Web, nous tirerons parti des fonctionnalités de recherche Web intégrées dans Open WebUI.

Open WebUI prend en charge un certain nombre de fournisseurs de recherche. D’une manière générale, vous pouvez soit utiliser un service d’interface de programmation d’application (API) tiers, pour lequel vous devrez obtenir une clé d’API, soit configurer localement un conteneur [Docker](https://www.ibm.com/fr-fr/think/topics/docker) SearXNG. Dans les deux cas, vous devrez configurer votre fournisseur de recherche dans la console Open WebUI.

Cette configuration, soit un pointeur vers SearXNG, soit l'entrée de votre clé d’API, se trouve sous **Panneau d’administration \> Paramètres \> Recherche Web** dans la console Open WebUI.

Reportez-vous à la [documentation d’Open WebUI](https://docs.openwebui.com/category/-web-search) pour plus d’instructions.

### Étape 5. Importer l’agent dans Open WebUI

1\. Dans votre navigateur, allez sur http://localhost:8080/ pour accéder à l’interface utilisateur Open Web. Si vous ouvrez l’interface Open WebUI pour la première fois, enregistrez votre nom d’utilisateur et votre mot de passe. Ces informations sont conservées localement (sur votre machine).

2\. Après vous être connecté(e), cliquez sur l’icône en bas à gauche de votre nom d’utilisateur. Dans le menu, cliquez sur Panneau d’administration.

3\. Dans l’onglet **Fonctions**, cliquez sur **+** pour ajouter une nouvelle fonction.

4\. Nommez la fonction (par exemple « Agent Granite RAG »), saisissez une description, les deux de `str` type.

5\. Collez le script Python [granite_autogen_rag.py](https://github.com/ibm-granite-community/granite-retrieval-agent/blob/main/granite_autogen_rag.py) dans la zone de texte prévue à cet effet, en remplaçant tout contenu existant. 

6\. Cliquez sur **Enregistrer** en bas de l’écran.

7\. De retour sur la page **Fonctions**, assurez-vous que l’agent est **activé**.

8\. Cliquez sur l’icône d’engrenage à côté du bouton d’activation pour personnaliser des paramètres tels que le point de terminaison d’inférence, le point de terminaison SearXNG ou l’ID du modèle.

Maintenant, votre tout nouvel agent AutoGen apparaît comme modèle dans l’interface Open WebUI. Vous pouvez le sélectionner et lui fournir des requêtes utilisateur.

### Étape 6. Charger les documents dans Open WebUI

1.  Dans Open WebUI, accédez à **Workspace (Espace de travail) \> Knowledge (Connaissances).**
2.  Cliquez sur \*\*\*\*\* pour créer une nouvelle collection.
3.  Téléchargez les documents que l’agent de récupération Granite devra interroger.

### Étape 7. Configurer la recherche Web dans Open WebUI

Pour configurer un fournisseur de recherche (par exemple, SearXNG), suivez ce [guide](https://docs.openwebui.com/tutorials/web-search/searxng/#4-gui-configuration).

Les paramètres de configuration sont les suivants :

|  |  |  |
|----|----|----|
| Paramètre | Description | Valeur par défaut |
| task_model_id | Modèle principal pour l’exécution des tâches | granite3.2:8b |
| vision_model_id | Modèle de vision pour l’analyse d’images | granite-vision3.2:2b |
| openai_api_url | Point de terminaison d’API pour les appels de modèles de type OpenAI | http://localhost:11434 |
| openai_api_key | Clé d’API pour l’authentification | Ollama |
| vision_api_url | Point de terminaison pour les tâches de vision | http://localhost:11434 |
| model_temperature | Contrôle le caractère aléatoire des réponses | 0 |
| max_plan_steps | Nombre maximal d’étapes dans la planification des agents | 6 |

***Remarque*** : ces paramètres peuvent être configurés via l’icône en forme d’engrenage dans la section « Functions » (Fonction) du panneau d’administration (Admin Panel) Open WebUI après l’ajout de la fonction.

### Étape 8. Interroger le système agentique

L’agent de récupération Granite exécute une RAG basée sur AG2 en interrogeant les documents locaux et les sources Web, en effectuant une planification de tâches multi-agents et en appliquant une exécution adaptative. Démarrez un chat et envoyez à votre système agentique une requête concernant les documents fournis pour voir la chaîne RAG en action.

## Récapitulatif

Une configuration multi-agents permet de créer des outils pratiques et utilisables en tirant le meilleur parti des modèles open source de taille moyenne comme Granite 3.2. Cette architecture RAG agentique, construite avec des outils entièrement open source, peut servir de point de départ pour concevoir et personnaliser vos agents de type questions-réponses et vos algorithmes d’IA. Elle peut également être utilisée librement pour un large éventail de cas d'utilisation. Dans ce tutoriel, vous avez pu découvrir des systèmes agentiques simples et complexes en exploitant les capacités d’AutoGen. Le LLM Granite a été invoqué à l’aide d’Ollama, ce qui permet une exploration entièrement locale de ces systèmes. Par la suite, pensez à intégrer des outils plus personnalisés dans votre système agentique.
