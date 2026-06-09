> Source : https://www.ibm.com/fr-fr/think/tutorials/agentic-rag

# Créez un système RAG agentique LangChain à l’aide de Granite-3.0-8B-Instruct dans watsonx.ai

## Qu’est-ce que la RAG agentique ?

Dans ce tutoriel, vous allez créer un système RAG agentique LangChain à l’aide du modèle IBM Granite-3.0-8B-Instruct désormais disponible sur watsonx.ai qui peut répondre à des questions complexes concernant l’US Open 2024 en utilisant des informations externes.

## Présentation générale de la RAG agentique

### Qu’est-ce que la RAG ?

La génération augmentée de récupération (RAG) est une technique de  traitement automatique du langage naturel qui tire parti de la récupération d’informations et des modèles génératifs pour produire des réponses plus précises, pertinentes et adaptées au contexte. Dans les tâches traditionnelles de génération de langage, degrands modèles de langage (LLM) tels que les modèles Llama de Meta ou les modèles Granite d’IBM sont utilisés pour élaborer des réponses basées sur un prompt. Les chatbots sont des cas d’utilisation courants de ces grands modèles linguistiques dans le monde réel. Lorsque les modèles ne disposent pas des informations pertinentes et à jour dans leur base de connaissances, la RAG est un outil très efficace.

### Qu’est-ce qu’un agent IA ?

Les agentsIA (intelligence artificielle) sont au cœur des systèmes RAG agentiques. Un agent IA désigne un système ou un programme capable d’exécuter des tâches de manière autonome pour le compte d’un utilisateur ou d’un autre système, en concevant son workflow et en utilisant les outils disponibles. La technologie agentique fait appel à des outils en arrière-plan pour obtenir des informations à jour à partir de diverses sources de données, optimiser le workflow et créer des sous-tâches de manière autonome pour résoudre les tâches complexes. Ces outils externes peuvent être des jeux de données externes, des moteurs de recherche, des API et même d’autres agents. À chaque étape, l’agent réévalue son plan d’action et s’autocorrige.

### RAG agentique vs RAG traditionnelle

Les cadres de RAG agentiques sont puissants, car ils peuvent englober plus d’un seul outil. Dans les applications de RAG traditionnelle, le LLM dispose d’une base de données vectorielle pour s’y référer lors de l’élaboration de ses réponses. En revanche, les applications d’IA agentique ne sont pas limitées aux agents de documentation qui se contentent de récupérer les données. Les agents RAG peuvent également disposer d’outils pour effectuer des tâches telles que résoudre des calculs mathématiques, rédiger des e-mails, analyser des données, etc. Ces outils peuvent venir compléter le processus de prise de décision de l’agent. Les agents IA sont sensibles au contexte dans leur raisonnement en plusieurs étapes et peuvent déterminer quand utiliser les outils appropriés.

Les agents IA, ou agents intelligents, peuvent également travailler en collaboration dans des systèmes multi-agents, qui ont tendance à être plus performants que les agents individuels. Cette évolutivité et cette adaptabilité sont ce qui distingue les agents RAG agentiques des pipelines RAG traditionnels.

## Prérequis

Vous devez disposer d’un compte IBM Cloud pour créer un projet watsonx.ai.

## Étapes

### Étape 1. Configurez votre environnement

Bien que vous puissiez choisir parmi plusieurs outils, ce tutoriel vous explique comment configurer un compte IBM pour utiliser un Jupyter Notebook.

1.  Connectez-vous à watsonx.ai en utilisant votre compte IBM Cloud.

2.  Créez un projet watsonx.ai.

    Vous pouvez obtenir l’ID de votre projet à partir de celui-ci. Cliquez sur l’onglet **Manage (Gérer)**. Ensuite, copiez l’ID du projet dans la section **Details (Détails)** de la page**General (Général)**. Vous aurez besoin de cet ID pour ce tutoriel.

3.  Créez un Jupyter Notebook. 

Cette étape ouvrira un environnement Jupyter Notebook dans lequel vous pouvez copier le code de ce tutoriel. Vous pouvez également télécharger ce notebook sur votre système local et le charger dans votre projet watsonx.ai en tant qu’actif. Vous trouverez d’autres tutoriels Granite auprès de la Communauté IBM Granite. Ce Jupyter Notebook, ainsi que les jeux de données utilisés, se trouvent sur GitHub.

###

## Étape 2. Configurez une instance d’exécution watsonx.ai et une clé d’API

1.  Créez une instance de service d’exécution watsonx.ai (sélectionnez votre région et choisissez le plan Lite, qui est une instance gratuite).

2.  Générer une clé d’API.

3.  Associez l’instance de service d’exécution watsonx.ai au projet que vous avez créé dans watsonx.ai.

### Étape 3. Installez et importez les bibliothèques pertinentes et configurer vos identifiants

Nous avons besoin de quelques dépendances pour ce tutoriel. Veuillez vous assurer d’importer les éléments suivants. S’ils ne sont pas installés, une rapide commande pip install vous permettra d’y remédier.

Les cadres Python couramment utilisés pour la création de systèmes d’IA agentique sont LangChain, LangGraph et LlamaIndex. Dans ce tutoriel, nous utiliserons LangChain.

```
# installations
!pip install langchain | tail -n 1
!pip install langchain-ibm | tail -n 1
!pip install langchain-community | tail -n 1
!pip install ibm-watsonx-ai | tail -n 1
!pip install ibm_watson_machine_learning | tail -n 1
!pip install chromadb | tail -n 1
!pip install tiktoken | tail -n 1
!pip install python-dotenv | tail -n 1
!pip install bs4 | tail -n 1
```

```
# imports
```

```python
import os
from dotenv import load_dotenv
from langchain_ibm import WatsonxEmbeddings, WatsonxLLM
from langchain.vectorstores import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.prompts import PromptTemplate
from langchain.tools import tool
from langchain.tools.render import render_text_description_and_args
from langchain.agents.output_parsers import JSONAgentOutputParser
from langchain.agents.format_scratchpad import format_log_to_str
from langchain.agents import AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables import RunnablePassthrough
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import EmbeddingTypes
```

Configurez vos identifiants. Veuillez enregistrer votre identifiant de projet (PROJECT_ID) et votre clé d’API (APIKEY) dans un fichier .env séparé, au même niveau que ce notebook dans votre répertoire.

```json
load_dotenv(os.getcwd()+"/.env", override=True)
credentials = {
"url": "https://us-south.ml.cloud.ibm.com",
"apikey": os.getenv("WATSONX_APIKEY", ""),
}
project_id = os.getenv("PROJECT_ID", "")
```

### Étape 4. Initialisation d’un agent de base sans outils

Cette étape est importante car elle permettra d’obtenir un exemple clair du comportement d’un agent avec et sans sources de données externes. Commençons par définir nos paramètres.

Vous trouverez les paramètres disponibles pour le modèle  ici. Nous avons testé divers paramètres de modèle, notamment la température, le nombre minimum et maximum de nouveaux tokens et les séquences d’arrêt. Pour en savoir plus sur les paramètres du modèle et leur signification, consultez la documentation de watsonx. Il est important de définir ici nos stop_sequences afin de limiter les hallucinations d’agents. Cela indique à l’agent de cesser toute production lorsqu’il rencontre certaines sous-chaînes. Dans notre cas, nous voulons que l’agent termine sa réponse lorsqu’il atteint une observation et qu’il n’hallucine pas une réponse humaine. Par conséquent, l’une de nos séquences d’arrêt est ’Human:’  et une autre est Observation pour qu’il s’arrête une fois qu’une réponse finale a été produite.

Pour ce tutoriel, nous vous recommandons d’utiliser le modèle Granite-3.0-8B-Instruct d’IBM comme LLM afin d’obtenir des résultats similaires. Vous pouvez utiliser les modèles IA de votre choix. Vous trouverez les modèles de fondation disponibles avec watsonx ici. Dans le cadre d’une application LLM, ces modèles ont pour objectif de servir de moteur de raisonnement afin de déterminer les actions à entreprendre.

```
llm = WatsonxLLM(
model_id="ibm/granite-3-8b-instruct",
url=credentials.get("url"),
apikey=credentials.get("apikey"),
project_id=project_id,
params={
GenParams.DECODING_METHOD: "greedy",
GenParams.TEMPERATURE: 0,
GenParams.MIN_NEW_TOKENS: 5,
GenParams.MAX_NEW_TOKENS: 250,
GenParams.STOP_SEQUENCES: ["Human:", "Observation"],
},
)
```

Nous allons créer un modèle de prompt qui vous permettra de poser plusieurs questions si vous le souhaitez.\

```
template = "Answer the {query} accurately. If you do not know the answer, simply say you do not know."
prompt = PromptTemplate.from_template(template)
```

Nous pouvons maintenant configurer une chaîne avec notre prompt et notre LLM. Cela permet au modèle génératif de produire une réponse.

```
agent = prompt | llm
```

Faisons un test pour voir comment notre agent répond à une question de base.

```json
agent.invoke({"query": 'What sport is played at the US Open?'})
```

**Output**: ' Do not try to make up an answer.\n\nThe sport played at the US Open is tennis.'

L’agent a répondu avec succès à la requête de base en donnant la bonne réponse. À l’étape suivante de ce tutoriel, nous créerons un outil RAG permettant à l’agent d’accéder aux informations pertinentes sur la participation d’IBM à l’US Open 2024. Comme nous l’avons vu, les LLM traditionnels ne peuvent pas obtenir d’informations actuelles par eux-mêmes. Vérifions cela.

```json
agent.invoke({"query": 'Where was the 2024 US Open Tennis Championship?'})
```

**Output**: ' Do not make up an answer.\n\nThe 2024 US Open Tennis Championship has not been officially announced yet, so the location is not confirmed. Therefore, I do not know the answer to this question.'

Évidemment, le LLM n’est pas en mesure de nous fournir les informations pertinentes. Les données d’entraînement utilisées pour ce modèle contenaient des informations antérieures à l’US Open 2024 et, sans les outils appropriés, l’agent n’a pas accès à ces informations.

### Étape 5. Créez la base de connaissances et le système de récupération des informations

La première étape de la création de la base de connaissances consiste à répertorier les URL dont nous allons extraire le contenu. Dans ce cas, notre source de données sera collectée à partir de notre contenu en ligne résumant la participation d’IBM à l’US Open 2024. Les URL pertinentes sont définies dans la liste des URL.

```
urls = ['https://www.ibm.com/fr-fr/case-studies/us-open',
'https://www.ibm.com/fr-fr/sports/usopen',
'https://newsroom.ibm.com/US-Open-AI-Tennis-Fan-Engagement',
'https://newsroom.ibm.com/2024-08-15-ibm-and-the-usta-serve-up-new-and-enhanced-generative-ai-features-for-2024-us-open-digital-platforms']
```

Ensuite, chargez les documents à l’aide de LangChain WebBaseLoader pour les URL que nous avons répertoriées. Nous imprimerons également un exemple de document pour vérifier le chargement.

```
docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]
docs_list[0]
```

**Output: **Document(metadata={'source': 'https://www.ibm.com/fr-fr/case-studies/us-open', 'title': 'U.S. Open \| IBM', 'description': 'To help the US Open stay on the cutting edge of customer experience, IBM Consulting built powerful generative AI models with watsonx.', 'language': 'en'}, page_content='\n\n\n\n\n\n\n\n\n\nU.S. Open \| IBM\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHome\n\n\n\n\nCase Studies\n\n\n\nUS Open \n\n\n\n                    \n\n\n\n  \n    Acing the US Open digital experience\n\n\n\n\n\n\n    \n\n\n                \n\n                        \n\n\n  \n  \n      AI models built with watsonx transform data into insight\n  \n\n\n\n\n    \n\n\n                    \n\n\nGet the latest AI and tech insights\n\n\nLearn More\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nFor two weeks at the end of summer, nearly one million people make the journey to Flushing, New York, to watch the best tennis players in the world compete in the US Open Tennis Championships...')

Afin de diviser les données de ces documents en blocs qui peuvent être traités par le LLM, nous pouvons utiliser un séparateur de texte tel que RecursiveCharacterTextSplitter. Ce séparateur de texte divise le contenu en fonction des caractères suivants : \["\n\n", "\n", " " , "" \]. Cela permet de conserver le texte dans les mêmes blocs, comme les paragraphes, les phrases et les mots ensemble.

Une fois le séparateur de texte activé, nous pouvons l’appliquer à notre liste de documents docs_list.

```
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=250, chunk_overlap=0)
doc_splits = text_splitter.split_documents(docs_list)
```

Le modèle d’embedding que nous utilisons est un modèle IBM Slate via le service d’embedding watsonx.ai. Procédons à son initialisation.

```
embeddings = WatsonxEmbeddings(
model_id=EmbeddingTypes.IBM_SLATE_30M_ENG.value,
url=credentials["url"],
apikey=credentials["apikey"],
project_id=project_id,
)
```

Pour stocker nos documents intégrés, nous utiliserons Chroma DB, une base de données vectorielle open source.

```
vectorstore = Chroma.from_documents(
documents=doc_splits,
collection_name="agentic-rag-chroma",
embedding=embeddings,
)
```

Pour accéder aux informations de la base de données vectorielle, nous devons configurer un système de récupération (« retriever »).

```
retriever = vectorstore.as_retriever()
```

### Étape 6. Définissez l’outil RAG de l’agent

Définissons l’outil get_IBM_US_Open_context() que notre agent utilisera. Le seul paramètre de cet outil est la requête de l’utilisateur. La description de l’outil est également mentionnée afin d’informer l’agent de son utilisation. De cette manière, l’agent sait quand utiliser cet outil. Cet outil peut être utilisé par le système RAG agentique pour acheminer la requête de l’utilisateur vers la base de données vectorielle si elle concerne la participation d’IBM à l’US Open 2024.

```python
@tool
def get_IBM_US_Open_context(question: str):
"""Get context about IBM's involvement in the 2024 US Open Tennis Championship."""
context = retriever.invoke(question)
return context

tools = [get_IBM_US_Open_context]
```

### Étape 7. Créez un modèle de prompt

Nous mettrons ensuite en place un nouveau modèle de prompt pour poser plusieurs questions. Ce modèle est plus complexe. C’est ce que l’on appelle un prompt de chat structuré ; il peut être utilisé pour créer des agents dotés de plusieurs outils. Dans notre cas, l’outil que nous utilisons a été défini à l’étape 6. Le prompt de chat structuré sera composé d’un prompt système, d’un prompt humain et de notre outil RAG.

Tout d’abord, nous allons configurer system_prompt. Ce prompt demande à l’agent d’imprimer son « processus de pensée », qui implique les sous-tâches de l’agent, les outils qui ont été utilisés et le résultat produit. Cela nous donne des informations sur la fonction d’appel de l’agent. Le prompt indique également à l’agent de renvoyer ses réponses au format JSON Blob.

```json
system_prompt = """Respond to the human as helpfully and accurately as possible. You have access to the following tools: {tools}
Use a json blob to specify a tool by providing an action key (tool name) and an action_input key (tool input).
Valid "action" values: "Final Answer" or {tool_names}
Provide only ONE action per $JSON_BLOB, as shown:"
```
{{
"action": $TOOL_NAME,
"action_input": $INPUT
}}
```
Follow this format:
Question: input question to answer
Thought: consider previous and subsequent steps
Action:
```
$JSON_BLOB
```
Observation: action result
... (repeat Thought/Action/Observation N times)
Thought: I know what to respond
Action:
```
{{
"action": "Final Answer",
"action_input": "Final response to human"
}}
Begin! Reminder to ALWAYS respond with a valid json blob of a single action.
Respond directly if appropriate. Format is Action:```$JSON_BLOB```then Observation"""
```

Dans le code suivant, nous définissons le prompt humain, human_prompt. Ce prompt indique à l’agent d’afficher l’entrée utilisateur suivie des étapes intermédiaires prises par l’agent dans le cadre de l’agent_scratchpad.

```
human_prompt = """{input}
{agent_scratchpad}
(reminder to always respond in a JSON blob)"""
```

Ensuite, nous définissons l’ordre de nos prompts nouvellement définis dans le modèle de prompt. Nous créons ce nouveau modèle pour inclure le system_prompt, suivi d’une liste facultative de messages collectés dans la mémoire de l’agent (le cas échéant), et enfin, le human_prompt, qui comprend à la fois l’entrée humaine et l’agent_scratchpad.

```
prompt = ChatPromptTemplate.from_messages(
[
("system", system_prompt),
MessagesPlaceholder("chat_history", optional=True),
("human", human_prompt),
]
)
```

Maintenant, finalisons notre modèle de prompt en ajoutant les noms des outils, leurs descriptions et leurs arguments à l’aide d’un modèle de prompt partiel. Cela permet à l’agent d’accéder aux informations relatives à chaque outil, y compris les cas d’utilisation prévus. Cela signifie également que nous pouvons ajouter et supprimer des outils sans modifier l’ensemble de notre modèle de prompt.

```
prompt = prompt.partial(
tools=render_text_description_and_args(list(tools)),
tool_names=", ".join([t.name for t in tools]),
)
```

### Étape 8. Configurez la mémoire et la chaîne de l’agent

Une fonctionnalité importante des agents IA est leur mémoire. Les agents peuvent enregistrer les conversations passées et les conclusions antérieures dans leur mémoire afin d’améliorer la précision et la pertinence de leurs réponses futures. Dans notre cas, nous utiliserons la fonction ConversationBufferMemory() de LangChain comme moyen de stockage en mémoire.

```
memory = ConversationBufferMemory()
```

Nous pouvons maintenant configurer une chaîne avec le bloc-notes, la mémoire, le prompt et le LLM de notre agent. La classe AgentExecutor est utilisée pour exécuter l’agent. Il faut l’agent, ses outils, son approche de la gestion des erreurs, ses paramètres conversationnels et sa mémoire.

```
chain = ( RunnablePassthrough.assign(
agent_scratchpad=lambda x: format_log_to_str(x["intermediate_steps"]),
chat_history=lambda x: memory.chat_memory.messages,
)
| prompt | llm | JSONAgentOutputParser())

agent_executor = AgentExecutor(agent=chain, tools=tools, handle_parsing_errors=True, verbose=True, memory=memory)
```

### Étape 9. Générez des réponses avec le système RAG agentique

Nous sommes maintenant en mesure de poser des questions à l’agent. Auparavant, l’agent n’était pas en mesure de nous fournir des informations concernant l’US Open 2024. Maintenant que l’agent dispose de son outil RAG, essayons de poser à nouveau les mêmes questions.

```json
agent_executor.invoke({"input": 'Where was the 2024 US Open Tennis Championship?'})
```

**Output**: (some description and page content fields were shortened to succinctly display results)

\> Entering new AgentExecutor chain...\
\
Thought: The human is asking about the location of the 2024 US Open Tennis Championship. I need to find out where it was held.\
Action:\
\`\`\`\
{\
    "action": "get_IBM_US_Open_context",\
    "action_input": "Where was the 2024 US Open Tennis Championship held?"\
}\
\`\`\`\
Observation\[Document(metadata={'description': "IBM and the United States Tennis Association (USTA) announced several watsonx-powered fan features coming to the US Open digital platforms ahead of this year's tournament. These new and enhanced capabilities – a product of collaboration between IBM and the USTA digital team – aim to deliver a more informative and engaging experience for millions of tennis fans around the world.", 'language': 'en-us', 'source': 'https://newsroom.ibm.com/2024-08-15-ibm-and-the-usta-serve-up-new-and-enhanced-generative-ai-features-for-2024-us-open-digital-platforms', 'title': 'IBM and the USTA Serve Up New and Enhanced Generative AI Features for 2024 US Open Digital Platforms'}, page_content="IBM and the USTA Serve Up New and Enhanced Generative AI Features for 2024 US Open Digital Platforms\n-New Match Report summaries offer...")\]

Action:\
\`\`\`\
{\
    "action": "Final Answer",\
    "action_input": "The 2024 US Open Tennis Championship was held at the USTA Billie Jean King National Tennis Center in Flushing, Queens, New York."\
}\
\`\`\`\
Observation\
\
\> Finished chain.

{'input': 'Where was the 2024 US Open Tennis Championship?',\
  'history': '',\
  'output': 'The 2024 US Open Tennis Championship was held at the USTA Billie Jean King National Tennis Center in Flushing, Queens, New York.'}

Parfait. L’agent a utilisé l’outil RAG disponible pour indiquer le lieu où se déroulera l’US Open 2024, conformément à la requête de l’utilisateur. Nous pouvons même voir le document exact à partir duquel l’agent récupère ses informations. Essayons maintenant une question un peu plus complexe. Cette fois, la question se portera sur la participation d’IBM à l’US Open 2024.

```json
agent_executor.invoke({"input": 'How did IBM use watsonx at the 2024 US Open Tennis Championship?'})
```

**Output**: (some description and page content fields were shortened to succinctly display results)

\> Entering new AgentExecutor chain...\
\`\`\`\
{\
    "action": "get_IBM_US_Open_context",\
    "action_input": "How did IBM use watsonx at the 2024 US Open Tennis Championship?"\
}\
\`\`\`\
Observation\[Document(metadata={'description': 'To help the US Open stay on the cutting edge of customer experience, IBM Consulting built powerful generative AI models with watsonx.', 'language': 'en', 'source': 'https://www.ibm.com/fr-fr/case-studies/us-open', 'title': 'U.S. Open \| IBM'}, page_content='The US Open is a sprawling, two-week tournament, with hundreds of matches played on 22 different courts. Keeping up with all the action is a challenge, both for tennis fans and the USTA editorial team covering the event...)\]\
\
Action:\
\`\`\`\
{\
    "action": "Final Answer",\
    "action_input": "IBM used watsonx at the 2024 US Open Tennis Championship to create generative AI-powered features such as Match Reports, AI     Commentary, and SlamTracker. These features enhance the digital experience for fans and scale the productivity of the USTA editorial team."\
}\
\`\`\`\
Observation\
\> Finished chain.

{'input': 'How did IBM use watsonx at the 2024 US Open Tennis Championship?',\
 'history': 'Human: Where was the 2024 US Open Tennis Championship?\nAI: The 2024 US Open Tennis Championship was held at the USTA Billie Jean King National Tennis Center in Flushing, Queens, New York.',\
 'output': 'IBM used watsonx at the 2024 US Open Tennis Championship to create generative AI-powered features such as Match Reports, AI Commentary, and SlamTracker. These features enhance the digital experience for fans and scale the productivity of the USTA editorial team.'}

Une fois encore, l’agent a réussi à récupérer les informations pertinentes relatives à la requête de l’utilisateur. De plus, l’agent met à jour sa base de connaissances au fur et à mesure qu’il apprend de nouvelles informations et acquiert de l’expérience avec de nouvelles interactions, comme le montre la production.

Maintenant, vérifions si l’agent est capable de déterminer quand il n’est pas nécessaire d’utiliser un outil pour répondre à la requête de l’utilisateur. Nous pouvons vérifier cela en posant à l’agent RAG une question qui ne concerne pas l’US Open.

```json
agent_executor.invoke({"input": 'What is the capital of France?'})
```

**Output**: 

\> Entering new AgentExecutor chain...\
\
{\
    "action": "Final Answer",\
    "action_input": "The capital of France is Paris."\
}\
\
Observation\
\> Finished chain.

{'input': 'What is the capital of France?',\
 'history': 'Human: Where was the 2024 US Open Tennis Championship?\nAI: The 2024 US Open Tennis Championship was held at the USTA Billie Jean King National Tennis Center in Flushing, Queens, New York.\nHuman: How did IBM use watsonx at the 2024 US Open Tennis Championship?\nAI: IBM used watsonx at the 2024 US Open Tennis Championship to create generative AI-powered features such as Match Reports, AI Commentary, and SlamTracker. These features enhance the digital experience for fans and scale the productivity of the USTA editorial team.',\
 'output': 'The capital of France is Paris.'}

Comme on le voit dans la chaîne AgentExecutor, l’agent a reconnu qu’il disposait des informations dans sa base de connaissances pour répondre à cette question sans utiliser ses outils.

## Récapitulatif

Dans ce tutoriel, vous avez créé un agent RAG en utilisant LangChain en Python avec Watsonx. Le LLM avec lequel vous avez travaillé était le modèle IBM Granite-3.0-8B-Instruct. L’exemple de production est important car il montre l’importance de cette avancée de l’IA générative. L’agent IA a réussi à récupérer les informations pertinentes à l’aide de l’outil get_IBM_US_Open_context, à mettre à jour sa mémoire à chaque interaction et à produire des réponses appropriées. Il est également important de noter la capacité de l’agent à déterminer si l’appel d’outil est approprié pour chaque tâche. Lorsque l’agent disposait des informations nécessaires pour répondre à la requête initiale, il n’utilisait aucun outil de réponse aux questions.

Pour plus d’informations sur les agents IA, nous vous invitons à consulter notre tutoriel sur les agents IA qui affiche la photo astronomique du jour à l’aide de l’API open source de la NASA et d’un outil de datation.
