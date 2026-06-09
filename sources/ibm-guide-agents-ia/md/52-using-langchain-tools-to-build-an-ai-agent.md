> Source : https://www.ibm.com/fr-fr/think/tutorials/using-langchain-tools-to-build-an-ai-agent

# Appel d’outil LangChain utilisant Granite-3.0-8B-Instruct en Python avec watsonx.ai

Dans ce tutoriel, nous utiliserons les outils LangChain préconfigurés pour un agent ReAct agentic afin de showcase sa capacité à différencier les cas d’utilisation appropriés pour chaque outil. Nous utiliserons principalement le package open source LangChain Python.

## Qu’est-ce qu’un appel de fonction ?

L'appel d'outils, également appelé appel de fonction, est l'interface qui permet aux agents d'intelligence artificielle (IA) d'effectuer des tâches spécifiques nécessitant des informations actualisées, qui ne sont pas disponibles pour les grands modèles linguistiques (LLM) entraînés. Les modèles de LLM tels que les modèles IBM Granite ou les modèles GPT (generative pre-trained transformer) d'OpenAI n'ont accès qu'aux informations utilisées lors de leur formation. Il existe de nombreux outils par défaut accessibles via LangChain, notamment un outil pour travailler avec des requêtes de SQL database, accéder aux informations sur Wikipédia et bien plus encore. Nous vous encourageons à lire la documentation de LangChain pour une liste complète des outils prédéfinis.

Les outils personnalisés peuvent être définis à l’aide de diverses méthodes, notamment à l’aide de @tool Decorator ou des LangChain Runsibles que nous aborderons dans ce tutoriel. Les outils asynchrones peuvent être créés à l’aide des classes StructuredTool ou BaseTool. Pour distinguer chaque approche, nous vous invitons à consulter la documentation officielle de LangChain. Reportez-vous au tutoriel d’appel des fonctions IBM pour obtenir des exemples d’outils personnalisés.

Nous vous encourageons à consulter notre fiche explicative sur les agents IA pour obtenir une présentation approfondie des différents types d'agents IA et de la manière dont ils diffèrent des chatbots LLM traditionnels.

## Prérequis

Vous avez besoin d’un compte IBM Cloud.

## Étapes

### Étape 1. Configurer votre environnement

Bien que vous puissiez choisir parmi plusieurs outils, ce tutoriel vous explique comment configurer un compte IBM pour utiliser un Jupyter Notebook.

1.  Se connecter à watsonx.ai en utilisant votre compte IBM Cloud.

2.  Créer un projet watsonx.ai.

    Vous pouvez obtenir votre identifiant de projet à partir de votre projet. Cliquez sur **l’onglet** Gérer. Ensuite, copiez l’identifiant du projet depuis la section **Détails de** **la page** Général. Vous avez besoin de cet identifiant pour ce tutoriel.

3.  Créer un Carnet Jupyter.

    Cette étape ouvrira un environnement Jupyter Notebook dans lequel vous pourrez copier le code de ce tutoriel. Vous pouvez également télécharger ce notebook sur votre système local et le charger dans votre projet watsonx.ai en tant qu’actif. Pour voir d'autres tutoriels Granite, consultez la Communauté IBM®  Granite. Ce tutoriel est également disponible sur Github.

###

## Étape 2. Configurer une instance d’exécution watsonx.ai et une clé d’API

1.  Créez une instance de service d’exécution watsonx.ai (sélectionnez votre région et choisissez le plan Lite, qui est une instance gratuite).

2.  Générer une clé API.

3.  Associez l’instance de service d’exécution watsonx.ai au projet que vous avez créé dans watsonx.ai.

### Étape 3. Installer et importer les bibliothèques pertinentes et configurer vos identifiants

Nous avons besoin de quelques bibliothèques et modules pour ce tutoriel. Assurez-vous d’importer les suivants et s’ils ne sont pas installés, vous pouvez résoudre ce problème avec une installation rapide de pip. LangChain et LangGraph seront les cadres des exigences et les outils utilisés.

**Remarque** : ce tutoriel a été créé à l'aide de Python 3.11.9 et est également compatible avec Google Colab, qui utilise Python 3.10.12. Pour vérifier votre version de Python, vous pouvez exécuter !python --version  commande dans une cellule de code.

```
#installations
!pip install -q langchain \
"langchain_community<0.3.0" \
langgraph \
youtube_search \
pyowm \
ionic-langchain \
python-dotenv

!pip install -qU langchain-ibm
```

```python
#imports
import os

from langchain_ibm import ChatWatsonx
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import Tool
from langchain_core.messages import HumanMessage
from langchain_community.tools import YouTubeSearchTool
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from ionic_langchain.tool import IonicTool
from dotenv import load_dotenv

load_dotenv(os.getcwd()+"/.env", override=True)
```

Pour définir nos identifiants, nous avons besoin des identifiants WATSONX_APIKEY et WATSONX_PROJECT_ID que vous avez générés à l’étape 1. Vous pouvez soit les stocker dans un fichier .env dans votre répertoire, soit remplacer le texte de l'espace réservé. Nous définirons également l’URL servant de point de terminaison de l’API.

```
WATSONX_APIKEY = os.getenv('WATSONX_APIKEY', "<WATSONX_APIKEY_HERE>")
WATSONX_PROJECT_ID = os.getenv('WATSONX_PROJECT_ID', "<WATSONX_PROJECT_ID_HERE>")
URL = "https://us-south.ml.cloud.ibm.com"
```

L'outil météorologique utilisé dans ce tutoriel nécessite une clé API OpenWeather. Pour en générer un, créez un compte OpenWeather. Lors de la création d’un compte, sélectionnez l’onglet « Clés API » pour afficher votre clé gratuite.

```
OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY', "<OPEN_WEATHERMAP_API_KEY_HERE>")
```

### Étape 4. Initialiser le LLM

Pour ce tutoriel, nous utiliserons l’encapsuleur ChatWatsonx pour définir notre modèle de chat. Cet encapsuleur simplifie l’intégration de l’appel et du chaînage des outils. Nous utiliserons le modèle granite-3-8b-instruct. Nous vous encourageons à utiliser les références API dans la documentation ChatWatsonx pour plus d'informations.

Pour initialiser le LLM, nous devons définir les paramètres du modèle. Il est important de configurer la température du modèle ici afin de limiter les hallucinations de l’agent.

```json
llm = ChatWatsonx(
model_id="ibm/granite-3-8b-instruct",
url = URL,
apikey = WATSONX_APIKEY,
project_id = WATSONX_PROJECT_ID,
params = {
"decoding_method": "greedy",
"temperature": 0,
"min_new_tokens": 5,
"max_new_tokens": 2000
}
)
```

### Étape 5. Mettre en place les outils intégrés

Nous pouvons utiliser la classe Tool pour rendre nos outils appelables. Une description claire et simple de l’outil est également importante. De plus, l'attribut booléen return_direct détermine si la réponse de l'outil doit être renvoyée directement à l'utilisateur. Enfin, l'attribut facultatif args_schema du type pydantic.BaseModel est utilisé pour fournir des informations ou une validation supplémentaires au modèle.

Imaginons que vous planifiez vos prochaines vacances en Grèce et que vous souhaitiez en savoir plus et vous préparer pour votre voyage. Commençons par configurer l'outil météorologique intégré LangChain. Cet outil utilise OpenWeatherMapAPIWrapper, qui utilise la clé OPENWEATHERMAP_API_KEY que nous avons générée précédemment.

```
weather = OpenWeatherMapAPIWrapper(openweathermap_api_key=OPENWEATHERMAP_API_KEY)

weather_search = Tool(
name="weather_search",
description="Get weather for a city and country code, e.g. Athens, GR",
func=weather.run,
)
```

Il suffit maintenant de configurer l’outil YouTube prédéfini à l’aide du package YouTube Search disponible via LangChain. Cette étape vous sera utile pour trouver des vidéos sur votre destination de voyage.

```
youtube = YouTubeSearchTool()

youtube_search = Tool(
name="youtube_search",
description="Search YouTube for video links.",
func=youtube.run,
)
```

Pour finir, créons un [outil d’achat en ligne](https://python.langchain.com/docs/integrations/tools/ionic_shopping/) à l’aide d’Ionic. Cet outil renvoie les articles pertinents pour la requête de l’utilisateur qui sont en vente sur le marketplace.

```
ionic_search = IonicTool().tool()
```

Définissez notre liste des différents outils que nous fournissons au LLM. Nous pouvons également imprimer la liste pour voir comment elle s’est chargée. Pour obtenir une liste complète des outils LangChain disponibles, reportez-vous à la documentation LangChain.

```
tools = [weather_search, youtube_search, ionic_search]
tools
```

**Output:**

\[**Tool**(name='weather_search', description='Get weather for a city and country code, e.g. Athens, GR', func=\, openweathermap_api_key='\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*')\>),

**Tool**(name='youtube_search', description='Search YouTube for video links.', func=\),

**Tool**(name='ionic_commerce_shopping_tool', description='\nIonic is an e-commerce shopping tool...\[abbreviated\]', verbose=True, func=\\>)\] 

### Étape 6. Appel d’outil

L’appel d’un outil fait généralement référence à un LLM qui renvoie le nom de l’outil à appeler et ses arguments. Nous pouvons soit utiliser les informations extraites à d’autres fins, soit appeler l’outil en utilisant ces arguments. Pour d'autres exemples, consultez notre tutoriel sur les appels de fonctions.

En fait, l'exécution de l'outil et la récupération de sa sortie ne sont pas toujours impliquées. Dans ce tutoriel, nous allons découvrir les deux approches.

### Fournir l'outil et les arguments pertinents

Pour effectuer un appel d’outil traditionnel, il nous suffit de fournir une requête utilisateur et d’utiliser la méthode Bind_Tools prédéfinie pour transmettre la liste d’outils au LLM à chaque itération.

```
llm_with_tools = llm.bind_tools(tools)
response = llm_with_tools.invoke([("human", "What are some youtube videos about greece")])
response
```

**Output:**

***AIMessage**(content='', additional_kwargs={'tool_calls': \[{'id': 'chatcmpl-tool-7a15abba7d3c4419970d807ac0c8d353', 'type': 'function', 'function': {'name': 'youtube_search', 'arguments': '{"query": "greece"}'}}\]}, response_metadata={'token_usage': {'completion_tokens': 21, 'prompt_tokens': 578, 'total_tokens': 599}, 'model_name': 'ibm/granite-3-8b-instruct', 'system_fingerprint': '', 'finish_reason': 'tool_calls'}, id='chat-5fe7a26b8f954c179c4995e873bff91e', tool_calls=\[{'name': 'youtube_search', 'args': {'query': 'greece'}, 'id': 'chatcmpl-tool-7a15abba7d3c4419970d807ac0c8d353', 'type': 'tool_call'}\], usage_metadata={'input_tokens': 578, 'output_tokens': 21, 'total_tokens': 599})*

```
response.additional_kwargs
```

**Output:**

*{'tool_calls': \[{'id': 'chatcmpl-tool-7a15abba7d3c4419970d807ac0c8d353',\
'type': 'function',\
'function': {'name': 'youtube_search',\
'arguments': '{"query": "greece"}'}}\]}*

Comme le montre la sortie de tool_calls, le LLM identifie correctement l’appel d’outil et les arguments appropriés. Le LLM n’exécute pas l’outil lui-même. Nous le ferons à l’étape suivante.

### Exécuter l’appel de l’outil et récupérer sa sortie

Pour exécuter les appels d’outil, nous devons d’abord créer un agent ReAct en utilisant la méthode d’assistance prédéfinie LangGraph. Cette fonction crée un graphique qui sert de pont entre le modèle de chat et les outils disponibles, permettant ainsi un appel d'outils agentique. Ce graphique est représenté dans le diagramme suivant.

```
agent_executor = create_react_agent(llm, tools)
```

Nous sommes maintenant en mesure de poser à l'agent les questions qui nécessitent un appel outil. Tout d’abord, nous pouvons demander au modèle de renvoyer des URL aux vidéos YouTube sur la Grèce. Nous pouvons utiliser la classe HumanMessage pour transmettre la requête utilisateur au LLM.

```json
user_query = "What are some YouTube videos about Greece"
response = agent_executor.invoke({"messages": user_query})
response["messages"]
```

**Output:**

*\[HumanMessage(content='What are some YouTube videos about Greece', additional_kwargs={}, response_metadata={}, id='1adba6c0-32e6-4bbd-92a6-7d21b0177439'),\
AIMessage(content='', additional_kwargs={'tool_calls': \[{'id': 'chatcmpl-tool-b4b5bf452404424ba4d6d9c26e53c6ce', 'type': 'function', 'function': {'name': 'youtube_search', 'arguments': '{"query": "Greece"}'}}\]}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 578, 'total_tokens': 600}, 'model_name': 'ibm/granite-3-8b-instruct', 'system_fingerprint': '', 'finish_reason': 'tool_calls'}, id='chat-5f41aee6736842749285aa7fbff50f65', tool_calls=\[{'name': 'youtube_search', 'args': {'query': 'Greece'}, 'id': 'chatcmpl-tool-b4b5bf452404424ba4d6d9c26e53c6ce', 'type': 'tool_call'}\], usage_metadata={'input_tokens': 578, 'output_tokens': 22, 'total_tokens': 600}),\
ToolMessage(content="\['https://www.youtube.com/watch?v=waQY2Ucpbd0&pp=ygUGR3JlZWNl', 'https://www.youtube.com/watch?v=NMlBB2pK5qo&pp=ygUGR3JlZWNl'\]", name='youtube_search', id='1ccf3137-2c10-495e-86ad-a548a3434243', tool_call_id='chatcmpl-tool-b4b5bf452404424ba4d6d9c26e53c6ce'),\
AIMessage(content='Here are some YouTube videos about Greece:\n\n1. \[Greece Travel Guide \| Top 10 Tourist Attractions\](https://www.youtube.com/watch?v=waQY2Ucpbd0&pp=ygUGR3JlZWNl)\n2. \[Greece Travel Guide \| Top 10 Tourist Attractions\](https://www.youtube.com/watch?v=NMlBB2pK5qo&pp=ygUGR3JlZWNl)', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 117, 'prompt_tokens': 677, 'total_tokens': 794}, 'model_name': 'ibm/granite-3-8b-instruct', 'system_fingerprint': '', 'finish_reason': 'stop'}, id='chat-801e3b596a174ac88246b507c93e5869', usage_metadata={'input_tokens': 677, 'output_tokens': 117, 'total_tokens': 794})\]*

Super ! Comme on le voit dans l’ AIMessage , le modèle a correctement identifié l’appel d’outil approprié. Dans le ToolMessage, nous constatons que le modèle a renvoyé avec succès la sortie attendue en utilisant l’outil LangChain YouTube intégré. Enfin, l'AIMessage indique que le LLM a synthétisé la réponse de l'outil.\

Ensuite, interrogeons le modèle sur la météo en Grèce pour déterminer s'il appelle l'outil weather_search comme prévu.

```json
user_query = "What is the weather in Athens, GR"
response = agent_executor.invoke({"messages": user_query})
response["messages"]
```

**Output:**

*\[**HumanMessage**(content='What is the weather in Athens, GR', additional_kwargs={}, response_metadata={}, id='a0c4b69c-988a-4f7d-9b8a-4780305f8e2a'),\
**AIMessage**(content='', additional_kwargs={'tool_calls': \[{'id': 'chatcmpl-tool-9a0c07a3b35f4c69a351c5540ab663f8', 'type': 'function', 'function': {'name': 'weather_search', 'arguments': '{"\_\_arg1": "Athens, GR"}'}}\]}, response_metadata={'token_usage': {'completion_tokens': 26, 'prompt_tokens': 579, 'total_tokens': 605}, 'model_name': 'ibm/granite-3-8b-instruct', 'system_fingerprint': '', 'finish_reason': 'tool_calls'}, id='chat-eeed087050e049f0ad715f3615c7fdda', tool_calls=\[{'name': 'weather_search', 'args': {'\_\_arg1': 'Athens, GR'}, 'id': 'chatcmpl-tool-9a0c07a3b35f4c69a351c5540ab663f8', 'type': 'tool_call'}\], usage_metadata={'input_tokens': 579, 'output_tokens': 26, 'total_tokens': 605}),\
**ToolMessage**(content='In Athens, GR, the current weather is as follows:\nDetailed status: few clouds\nWind speed: 4.47 m/s, direction: 23°\nHumidity: 58%\nTemperature: \n - Current: 15.15°C\n - High: 15.74°C\n - Low: 14.1°C\n - Feels like: 14.24°C\nRain: {}\nHeat index: None\nCloud cover: 20%', name='weather_search', id='587b0230-b667-41de-97b9-3779554d2559', tool_call_id='chatcmpl-tool-9a0c07a3b35f4c69a351c5540ab663f8'),\
**AIMessage**(content='The current weather in Athens, GR is:\n- Detailed status: few clouds\n- Wind speed: 4.47 m/s, direction: 23°\n- Humidity: 58%\n- Temperature:\n - Current: 15.15°C\n - High: 15.74°C\n - Low: 14.1°C\n - Feels like: 14.24°C\n- Rain: None\n- Heat index: None\n- Cloud cover: 20%', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 125, 'prompt_tokens': 733, 'total_tokens': 858}, 'model_name': 'ibm/granite-3-8b-instruct', 'system_fingerprint': '', 'finish_reason': 'stop'}, id='chat-6719a5ca266a439bb10ed410db25c5ef', usage_metadata={'input_tokens': 733, 'output_tokens': 125, 'total_tokens': 858})\]*

Le modèle a pu identifier l’outil approprié à appeler, l’exécuter avec les arguments extraits et synthétiser la sortie de l’outil. Maintenant, demandons au LLM de vous fournir des valises à moins de 100 USD pour votre prochain voyage. Notez que l’outil est conçu pour rechercher les prix en centimes. Par conséquent, nous demandons des valises de moins de 10 000 cents, soit l’équivalent de 100 USD.

```json
user_query = "Find some suitcases for less than 10000"
response = agent_executor.invoke({"messages": user_query})
response["messages"]
```

**Output:**

*\[HumanMessage(content='Find some suitcases for less than 10000', additional_kwargs={}, response_metadata={}, id='8b207035-150a-4390-aff3-8b09ef85a592'),\
AIMessage(content='', additional_kwargs={'tool_calls': \[{'id': 'chatcmpl-tool-b011e718b18e41dcbcae2f7786af263d', 'type': 'function', 'function': {'name': 'ionic_commerce_shopping_tool', 'arguments': '{"\_\_arg1": "suitcases, 10, 0, 10000"}'}}\]}, response_metadata={'token_usage': {'completion_tokens': 41, 'prompt_tokens': 582, 'total_tokens': 623}, 'model_name': 'ibm/granite-3-8b-instruct', 'system_fingerprint': '', 'finish_reason': 'tool_calls'}, id='chat-e38c8568d1754636a6a92082561180bd', tool_calls=\[{'name': 'ionic_commerce_shopping_tool', 'args': {'\_\_arg1': 'suitcases, 10, 0, 10000'}, 'id': 'chatcmpl-tool-b011e718b18e41dcbcae2f7786af263d', 'type': 'tool_call'}\], usage_metadata={'input_tokens': 582, 'output_tokens': 41, 'total_tokens': 623}),\
ToolMessage(content='\[{"products": \[{"links": \[{"text": "Details", "type": "pdp", "url": "https://go.ionic.click/Ch4CKd"}\], "merchant_name": "Walmart", "merchant_product_id": "811277349", "name": "Zimtown Hardside Lightweight Spinner Orange 3 Piece Luggage Set with TSA Lock", "price": "\$69.99", "status": "available", "thumbnail": "https://i5.walmartimages.com/asr/b809a274-ccc7-4ca4-b4f1-e848b4412fe6.314144bcd13e5467a33cb99e8dd5237c.jpeg?odnHeight=100&odnWidth=100&odnBg=ffffff", "brand_name": "Zimtown", "upc": "273109526768"}, {"links": \[{"text": "Details", "type": "pdp", "url": "https://www.amazon.com/dp/B071HHX6VF?tag=ioniccommer00-20&linkCode=osi&th=1&psc=1"}\], "merchant_name": "Amazon", "merchant_product_id": "B071HHX6VF", "name": "Amazon Basics Expandable Hardside Luggage, Suitcase with Wheels, 30-Inch Spinner with Four Spinner Wheels and Scratch-Resistant Surface, Black", "price": "\$74.49", "status": "available", "thumbnail": "https://m.media-amazon.com/images/I/41jJcuMYSdL.\_SL160\_.jpg", "brand_name": "Amazon Basics", "upc": "841710177190"}, .....\[abbreviated\],\
AIMessage(content='Here are some suitcases that are less than 10000:\n\n1. \[Zimtown Hardside Lightweight Spinner Orange 3 Piece Luggage Set with TSA Lock\](https://go.ionic.click/Ch4CKd) - \$69.99\n2. \[Amazon Basics Expandable Hardside Luggage, Suitcase with Wheels, 30-Inch Spinner\](https://www.amazon.com/dp/B071HHX6VF) - \$74.49\n3. \[SwissGear Sion Softside Expandable Luggage, Blue, Carry-On 21-Inch\](https://www.amazon.com/dp/B01MFBVKDF) - \$80.73\n4. \[Travelers Club Midtown Hardside Luggage Travel, Rose Gold, 4-Piece Set\](https://www.amazon.com/dp/B07RS4PK3J) - \$95.19\n5. \[American Tourister Stratum 2.0 Expandable Hardside Luggage with Spinner Wheels, 28" SPINNER, Slate Blue\](https://www.amazon.com/dp/B0B2X1BDFH) - \$89.97\n6. \[Wrangler Smart Luggage Set with Cup Holder and USB Port, Navy Blue, 20-Inch Carry-On\](https://www.amazon.com/dp/B07SLG6WZ2) - \$39.99\n7. \[Wrangler Hardside Carry-On Spinner Luggage, Lilac, 20-Inch\](https://www.amazon.com/dp/B0C7YWMBGP) - \$40.00\n8. \[Protege 20 inch Hard Side Carry-On Spinner Luggage, Black Matte Finish (Walmart.com Exclusive)\](https://go.ionic.click/qJqBRA) - \$29.87\n9. \[Wrangler Wesley Rolling Duffel Bag, Tannin, Large 30-Inch\](https://www.amazon.com/dp/B07XKWMLJ5) - \$44.00\n10. \[U.S. Traveler Boren Polycarbonate Hardside Rugged Travel Suitcase Luggage with 8 Spinner Wheels, Aluminum Handle, Lavender, Checked-Large 30-Inch\](https://www.amazon.com/dp/B085B4D852) - \$79.99', additional_kwargs={}, response_metadata={'token_usage': {'completion_tokens': 612, 'prompt_tokens': 2794, 'total_tokens': 3406}, 'model_name': 'ibm/granite-3-8b-instruct', 'system_fingerprint': '', 'finish_reason': 'stop'}, id='chat-d08201ff6ef84c428e7ae44372396926', usage_metadata={'input_tokens': 2794, 'output_tokens': 612, 'total_tokens': 3406})\]*

Comme l'a vu la réponse du LLM, le modèle a correctement utilisé l'outil d'achat pour retourner plusieurs valises pour un achat en ligne de moins de 100 USD.

## Récapitulatif

Dans ce tutoriel, vous avez utilisé des outils LangChain préconfigurés pour créer un agent ReAct en Python avec watsonx à l’aide des granite-3-8b-instruct  model. Vous avez utilisé la youtube_search , weather_search  et ionic_search  outils. Le tutoriel a montré comment implémenter l’appel d’outils traditionnel ainsi qu’une approche qui exécute les outils. L'exemple de sortie est important, car il montre les étapes suivies par l'agent pour créer son propre workflow d'agent en utilisant les fonctions disponibles. Les outils mis à la disposition de l’agent étaient essentiels pour répondre aux questions des utilisateurs.
