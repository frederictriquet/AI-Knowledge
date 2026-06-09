> Source : https://www.ibm.com/fr-fr/think/tutorials/human-in-the-loop-ai-agent-langraph-watsonx-ai

# Supervision « l’humain dans la boucle » d’un agent IA de recherche d’antériorités avec LangGraph et watsonx.ai

Dans ce tutoriel, vous allez mettre en œuvre le mécanisme de feedback [humain dans la boucle](https://www.ibm.com/fr-fr/think/topics/human-in-the-loop) pour votre système agentique construit avec LangGraph et IBM® watsonx.ai. Votre agent sera spécialisé dans la recherche d’antériorités, un cas d’utilisation concret qui demanderait autrement un immense effort manuel. Votre agent utilisera l’[API](https://www.ibm.com/fr-fr/think/topics/api) Google Brevets via SerpAPI pour examiner les brevets et fournir un feedback sur les suggestions en matière de brevets. Le grand modèle de langage (LLM) sera, de préférence, IBM® Granite (open source).

L’émergence de [l’IA agentique](https://www.ibm.com/fr-fr/think/topics/agentic-ai) a poussé les développeurs à déplacer leur attention et leurs efforts des [chatbots](https://ibm.com/think/topics/chatbots) LLM de base vers l’[automatisation](https://www.ibm.com/fr-fr/think/topics/automation). Le terme « automatisation » implique la suppression de l’intervention humaine dans l’exécution des tâches.1 Laisseriez-vous un [agent IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) faire des choix importants à votre place, comme vos finances personnelles ? Beaucoup d’entre nous ne le feraient pas. Et si une certaine ambiguïté pouvait induire chez l’utilisateur final ce manque de confiance ? Cette nuance peut prendre la forme d’une intervention humaine, appelée « l’humain dans la boucle ».

## L’humain dans la boucle

[L’humain dans la boucle (HITL)](https://www.ibm.com/fr-fr/think/topics/human-in-the-loop) est un modèle d’architecture dans lequel le feedback humain est nécessaire pour guider la prise de décision d’une application LLM et assurer une supervision. Dans le domaine de [l’intelligence artificielle](https://www.ibm.com/fr-fr/think/topics/artificial-intelligence), le HITL implique une intervention humaine à un moment donné du [workflow d’IA](https://www.ibm.com/fr-fr/think/topics/ai-workflow). Cette méthode garantit la précision, la sécurité et la responsabilité.

Les humains peuvent examiner et mettre à jour de manière asynchrone l’état des graphes dans LangGraph grâce à l’état d’exécution persistant. En utilisant les points de contrôle de l’état après chaque étape, le contexte d’état peut être conservé et le workflow peut être interrompu jusqu’à réception du feedback humain.

Dans ce tutoriel, nous allons expérimenter les deux approches HITL dans LangGraph.

1.  **Interruptions statiques** : modification de l’état du graphe directement à des points prédéterminés *avant ou après* l’exécution d’un nœud donné. Cette approche exige que les paramètres interrupt_before ou interrupt_after soient définis sur une liste de noms de nœuds lors de la compilation du graphe d’état.

2.  **Interruptions dynamiques** : interrompre un graphe et attendre l’entrée de l’utilisateur *à partir* d’un nœud en fonction de l’état actuel du graphe. Cette approche exige l’utilisation de la fonction interrupt de LangGraph.

## Prérequis

1. Vous devez disposer d’un [compte IBM® Cloud](https://cloud.ibm.com/registration) pour créer un projet watsonx.ai.

2\. Plusieurs versions de Python peuvent être utilisées pour ce tutoriel. Nous vous recommandons de télécharger Python 3.13, la version la plus récente au moment où le présent document a été publié.

## Étapes

### Étape 1. Configurer l’environnement

Bien que vous puissiez faire votre choix parmi plusieurs outils, ce tutoriel vous guide pas à pas pour configurer un compte IBM à l’aide d’un Jupyter Notebook.

1.  Connectez-vous à watsonx.ai à l’aide de votre compte IBM Cloud.

2.  Créez un projet watsonx.ai.

    Vous pouvez obtenir l’ID de votre projet à partir de ce dernier. Cliquez sur l’onglet **Manage** (Gérer). Ensuite, copiez l’ID du projet à partir de la section **Details** (Détails) de la page **General** (Général). Vous aurez besoin de cet ID pour ce tutoriel.

3.  Créez un Jupyter Notebook.

    Cette étape ouvrira un environnement Jupyter Notebook, où vous pourrez copier le code de ce tutoriel. Sinon, vous pouvez télécharger ce notebook localement dans votre système, et le charger dans votre projet watsonx.ai en tant qu’actif. Ce tutoriel est également disponible sur Github.

###

## Étape 2. Configurer une instance d’exécution watsonx.ai et une clé d’API

1.  Créez une instance de service d’exécution watsonx.ai (sélectionnez votre région et choisissez le forfait Lite, qui est une instance gratuite).

2.  Générez une clé d’API.

3.  Associez l’instance de service watsonx.ai Runtime au projet que vous avez créé dans watsonx.ai.

### Étape 3. Installer et importer les bibliothèques nécessaires, et configurer les identifiants

Nous avons besoin de quelques bibliothèques et modules pour ce tutoriel. Veillez à importer les éléments suivants. S’ils ne sont pas installés, une installation pip résoudra rapidement le problème.

```
%pip install --quiet -U langgraph langchain-ibm langgraph_sdk langgraph-prebuilt google-search-results
```

Redémarrez le noyau et importez les paquets suivants.

```python
import getpass
import uuid

from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.foundation_models.moderations import Guardian
from IPython.display import Image, display
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, AIMessage
from langchain_ibm import ChatWatsonx
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, END, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import tools_condition, ToolNode
from langgraph.types import interrupt, Command
from serpapi.google_search import GoogleSearch
from typing_extensions import TypedDict
from typing import Annotated
```

Pour définir nos identifiants, nous avons besoin de l’élément `WATSONX_APIKEY`  et `WATSONX_PROJECT_ID`  que vous avez généré à l’étape 1. Nous allons également définir notre `WATSONX_URL`  pour servir de point de terminaison de l’API.

Pour accéder à l’API Google Brevets, nous avons également besoin d’une `SERPAPI_API_KEY` . Vous pouvez générer une clé gratuite en vous connectant à votre compte SerpApi ou en vous inscrivant pour en créer une.

```
WATSONX_APIKEY = getpass.getpass("Please enter your watsonx.ai Runtime API key (hit enter): ")
WATSONX_PROJECT_ID = getpass.getpass("Please enter your project ID (hit enter): ")
WATSONX_URL = getpass.getpass("Please enter your watsonx.ai API endpoint (hit enter): ")
SERPAPI_API_KEY = getpass.getpass("Please enter your SerpAPI API key (hit enter): ")
```

Avant d’initialiser notre LLM, nous pouvons utiliser la classe `Credentials`  pour encapsuler nos identifiants API passés.

```
credentials = Credentials(url=WATSONX_URL, api_key=WATSONX_APIKEY)
```

### Étape 4. Instancier le modèle de chat

Pour pouvoir interagir avec toutes les ressources disponibles dans watsonx.ai Runtime, vous devez configurer votre `APIClient` . Ici, nous transmettons nos identifiants et `WATSONX_PROJECT_ID` .

```
client = APIClient(credentials=credentials, project_id=WATSONX_PROJECT_ID)
```

Pour ce tutoriel, nous utiliserons l’encapsuleur ChatWatsonx pour définir notre modèle de chat. Cet encapsuleur simplifie l’intégration de l’appel et du chaînage des outils. Nous vous encourageons à utiliser les références API dans la documentation ChatWatsonx pour plus d’informations.`ChatWatsonx` documents officiels pour de plus amples informations. Nous pouvons passer notre `model_id`  pour le LLM Granite et notre client comme paramètres.

Notez que si vous utilisez un autre fournisseur d’API, vous devrez modifier le wrapper en conséquence.

```
model_id = "ibm/granite-3-3-8b-instruct"
llm = ChatWatsonx(model_id=model_id, watsonx_client=client)
```

### Étape 5. Définir l’outil de scraping de brevets

Les agents IA utilisent des outils pour combler les lacunes d’information et renvoyer des informations pertinentes. Ces outils peuvent inclure la recherche Web, la RAG, diverses API, les calculs mathématiques, etc. En utilisant l’API Google Brevets via SerpAPI, nous pouvons définir un outil de scraping de brevets. Cet outil est une fonction qui prend le terme de recherche comme argument et renvoie les résultats de recherche organique pour les brevets connexes. Le `GoogleSearch`  wrapper exige des paramètres tels que le moteur de recherche, qui dans notre cas est `google_patents` , le terme de recherche et enfin, `SERPAPI_API_KEY` .

```python
def scrape_patents(search_term: str):
"""Search for patents about the topic.

Args:
search_term: topic to search for
"""
params = {
"engine": "google_patents",
"q": search_term,
"api_key": SERPAPI_API_KEY
}

search = GoogleSearch(params)
results = search.get_dict()
return results['organic_results']
```

Ensuite, lions le LLM `scrape_patents`  l’outil en utilisant `bind_tools`  comme méthode.

```
tools = [scrape_patents]
llm_with_tools = llm.bind_tools(tools)
```

### Étape 6. Première approche HITL : interruptions statiques

Les graphes d’agent LangGraph sont composés de nœuds et d’arêtes. Les nœuds sont des fonctions qui transmettent, mettent à jour et renvoient les informations. Comment suivre ces informations entre les nœuds ? Les graphes d’agents exigent un état, qui contient toutes les informations dont un agent a besoin pour prendre des décisions. Les nœuds sont reliés par des arêtes (les fonctions qui sélectionnent le nœud suivant à exécuter en fonction de l’état actuel). Les arêtes peuvent être conditionnelles ou fixes.

Commençons par créer `AgentState`  une classe pour stocker le contexte des messages provenant de l’utilisateur, des outils et de l’agent. La fonction Python `TypedDict`  est utilisée ici pour garantir que les messages sont au format de dictionnaire approprié. Nous pouvons aussi utiliser `add_messages`  fonction de réduction pour ajouter tout nouveau message à la liste de messages existante.

```python
class AgentState(TypedDict):
messages: Annotated[list[AnyMessage], add_messages]
```

Définissez ensuite votre `call_llm`  fonction qui constitue `assistant`  le nœud. Ce nœud invoquera simplement le LLM avec le message actuel de l’état et le message système.

```python
sys_msg = SystemMessage(content="You are a helpful assistant tasked with prior art search.")

def call_llm(state: AgentState):
return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}
```

Nous pouvons ensuite définir notre `guardian_moderation`  fonction qui constitue `guardian`  nœud. Ce nœud est conçu pour modérer les messages à l’aide d’un système gardien, afin de détecter et de bloquer tout contenu indésirable ou sensible. Tout d’abord, le dernier message est récupéré. Ensuite, un dictionnaire intitulé `detectors`  est défini ; il contient les configurations des détecteurs et leurs valeurs de seuil. Ces détecteurs identifient certains types de contenu dans les messages tels que les données personnelles (PII), ainsi que les propos haineux, injurieux ou diffamatoires (HAP). Ensuite, une instance de la classe Guardian est créée, en transmettant `api_client`  un objet nommé `client`  et le `detectors`  dictionnaire. La méthode `detect`  de l’instance Guardian est appelée, en passant le contenu du dernier message et `detectors`  dictionnaire. La méthode renvoie ensuite un dictionnaire dans lequel `moderation_verdict`  la clé stocke une valeur de type « approprié » ou « inapproprié », en fonction de la sortie du modèle Granite Guardian.

```python
def guardian_moderation(state: AgentState):
message = state['messages'][-1]
detectors = {
"granite_guardian": {"threshold": 0.4},
"hap": {"threshold": 0.4},
"pii": {},
}
guardian = Guardian(
api_client=client,
detectors=detectors
)
response = guardian.detect(
text=message.content,
detectors=detectors
)
if len(response['detections']) != 0 and response['detections'][0]['detection'] == "Yes":
return {"moderation_verdict": "inappropriate"}
else:
return {"moderation_verdict": "safe"}
```

Maintenant, définissons `block_message`  la fonction pour servir de mécanisme de notification et informer l’utilisateur que sa requête d’entrée contient un contenu inapproprié et a été bloquée.

```python
def block_message(state: AgentState):
return {"messages": [AIMessage(content="This message has been blocked due to inappropriate content.")]}
```

Nous pouvons maintenant rassembler toutes ces fonctions en ajoutant les nœuds correspondants et en les reliant par les arêtes qui définissent le flux du graphe.

Le graphe commence au `guardian`  nœud qui appelle la méthode `guardian_moderation`  pour détecter les contenus préjudiciables avant qu’ils n’atteignent le LLM et l’API. L’arête conditionnelle entre les `guardian`  et `assistant`  nœuds achemine l’état du graphe vers `assistant`  le nœud ou la fin. Cette position est déterminée par la sortie `guardian_moderation`  de la fonction. Les messages sécurisés sont transmis `assistant`  au nœud, qui exécute `call_llm`  la méthode. Nous ajoutons également une arête conditionnelle entre `assistant`  et `tools`  les nœuds pour acheminer correctement les messages. Si le LLM renvoie un appel d’outil, `tools_condition`  la méthode assure l’acheminement vers le nœud outils. Sinon, le graphe dirige vers la fin. Cette étape fait partie de l’architecture d’agent ReAct, car nous voulons que l’agent reçoive la sortie de l’outil pour ensuite réagir au changement d’état et déterminer sa prochaine action.

```json
builder = StateGraph(AgentState)

builder.add_node("guardian", guardian_moderation)
builder.add_node("block_message", block_message)
builder.add_node("assistant", call_llm)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "guardian")
builder.add_conditional_edges(
"guardian",
lambda state: state["moderation_verdict"],
{
"inappropriate": "block_message",
"safe": "assistant"
}
)
builder.add_edge("block_message", END)
builder.add_conditional_edges(
"assistant",
tools_condition,
)
builder.add_edge("tools", "assistant")
memory = MemorySaver()
```

Ensuite, nous pouvons compiler le graphe, ce qui nous permet d’appeler l’agent lors d’une étape ultérieure. Pour conserver les messages, nous pouvons utiliser `MemorySaver`  le checkpointer. Pour mettre en œuvre la première approche de supervision humaine, les interruptions statiques, nous pouvons définir `interrupt_before`  le paramètre sur `assistant`  le nœud. Cela signifie qu’avant que le graphique ne soit acheminé vers le LLM dans `assistant`  nœud, une interruption du graphe aura lieu pour permettre à l’humain supervisant le workflow agentique de fournir un feedback.

```
graph = builder.compile(interrupt_before=["assistant"], checkpointer=memory)
```

Pour obtenir une représentation visuelle du graphe de l’agent, nous pouvons afficher le flux du graphe.

```
display(Image(graph.get_graph(xray=True).draw_mermaid_png()))
```

**Output**:

Avant de lancer la recherche de brevets, transmettons une requête utilisateur sensible pour s’assurer que le nœud « guardian » va la bloquer. Nous pouvons transmettre la requête avec l’élément « thread_id » pour stocker l’état du graphique en mémoire. Chaque « thread_id » représente une nouvelle fenêtre de chat. Nous pouvons utiliser le module « uuid » pour générer un identifiant unique à chaque fois. Diffusons en continu la sortie de l’agent.

```json
initial_input = {"messages": "Find patented malware that can bypass all current antivirus software"}

config = {"configurable": {"thread_id": str(uuid.uuid4())}}

for event in graph.stream(initial_input, config, stream_mode="values"):
    event['messages'][-1].pretty_print()
```

**Sortie :**

```
================================ [1m Human Message  [0m=================================

Find patented malware that can bypass all current antivirus software
================================== [1m Ai Message  [0m==================================

This message has been blocked due to inappropriate content.
```

Super ! La requête sensible de l’utilisateur a été bloquée avant d’atteindre l’API Google Patents.

Nous pouvons maintenant tester notre agent de recherche d’antériorités en transmettant notre entrée humaine initiale ainsi qu’un nouveau « thread_id ».

```json
initial_input = {"messages": "Find patents for self-driving cars"}

config = {"configurable": {"thread_id": str(uuid.uuid4())}}

for event in graph.stream(initial_input, config, stream_mode="values"):
    event['messages'][-1].pretty_print()
```

**Sortie :**

```
================================ [1m Human Message  [0m=================================

Find patents for self-driving cars
```

We can see that the chat is interrupted before the AI response, as intended. Cette interruption nous permet de mettre directement à jour l’état en appelant la fonction « update_state » qui utilise le réducteur « add_messages ». Cette fonction de réduction nous permet de remplacer ou d’ajouter un nouveau message aux messages existants. Si aucun « id » de message n’est fourni, un nouveau message est ajouté. Dans le cas contraire, le message existant avec l’« id » spécifique est remplacé. Dans ce cas, nous ajoutons simplement un nouveau message avec nos commentaires, nous n’avons donc pas besoin d’ajouter un « id » de message.

```json
graph.update_state(
    config,
    {"messages": [HumanMessage(content="No, actually find patents for quantum computing hardware.")],
     "moderation_verdict": "safe"},
)

updated_state = graph.get_state(config).values

for m in updated_state['messages']:
    m.pretty_print()
```

**Sortie :**

```
================================ [1m Human Message  [0m=================================

Find patents for self-driving cars
================================ [1m Human Message  [0m=================================

No, actually find patents for quantum computing hardware.
```

Nous pouvons constater que le message humain a été correctement ajouté. Diffusons à nouveau les réponses des agents.

*Remarque : la sortie de l’outil a été occultée pour plus de brièveté.*\*

```
for event in graph.stream(None, config, stream_mode="values"):
    event['messages'][-1].pretty_print()
```

**Sortie :**

```json
================================ [1m Human Message  [0m=================================

No, actually find patents for quantum computing hardware.
================================== [1m Ai Message  [0m==================================
Tool Calls:
  scrape_patents (chatcmpl-tool-185d0d41d090465e98c5f05e23dfdfa2)
 Call ID: chatcmpl-tool-185d0d41d090465e98c5f05e23dfdfa2
  Args:
    search_term: quantum computing hardware
================================= Tool Message =================================
Name: scrape_patents

[{"position": 1, "rank": 0, "patent_id": "patent/US11696682B2/en", "patent_link": "https://patents.google.com/patent/US11696682B2/en", "serpapi_link": "https://serpapi.com/search.json?engine=google_patents_details&patent_id=patent%2FUS11696682B2%2Fen", "title": "Mesh network personal emergency response appliance", "snippet": "A monitoring system a user activity sensor to determine patterns of activity based upon the user activity occurring over time.", "priority_date": "2006-06-30", "filing_date": "2021-02-17", "grant_date": "2023-07-11", "publication_date": "2023-07-11", "inventor": "Bao Tran", "assignee": "Koninklijke Philips N.V.", "publication_number": "US11696682B2", "language": "en"

...

[REDACTED]
```

Given the loop between the LLM and the patent search tool, we have returned to the `assistant` node that engages the breakpoint once again. Because we want to proceed, we simply pass `None`.

```
for event in graph.stream(None, config, stream_mode="values"):
    event['messages'][-1].pretty_print()
```

**Output:**

```json
================================= Tool Message =================================
Name: scrape_patents

[{"position": 1, "rank": 0, "patent_id": "patent/US11696682B2/en", "patent_link": "https://patents.google.com/patent/US11696682B2/en", "serpapi_link": "https://serpapi.com/search.json?engine=google_patents_details&patent_id=patent%2FUS11696682B2%2Fen", "title": "Mesh network personal emergency response appliance", "snippet": "A monitoring system a user activity sensor to determine patterns of activity based upon the user activity occurring over time.", "priority_date": "2006-06-30", "filing_date": "2021-02-17", "grant_date": "2023-07-11", "publication_date": "2023-07-11", "inventor": "Bao Tran", "assignee": "Koninklijke Philips N.V.", "publication_number": "US11696682B2", "language": "en"

...

[REDACTED]
================================== [1m Ai Message  [0m==================================

Here are patents related to quantum computing hardware:

1. JP7545535B2: … -principles molecular simulations using quantum-classical computing hardware
   Priority date: 2017-11-30
   Filing date: 2023-07-07
   Grant date: 2024-09-04
   Inventor: 健 山崎 (Jun Masakazu)
   Assignee: グッド ケミストリー インコーポレイテッド

2. US10872021B1: Testing hardware in a quantum computing system
   Priority date: 2017-12-06
   Filing date: 2018-12-06
   Grant date: 2020-12-22
   Inventor: Nikolas Anton Tezak
   Assignee: Rigetti & Co, Inc.

3. CN112819169B: Quantum control pulse generation method, device, equipment and storage medium
   Priority date: 2021-01-22
   Filing date: 2021-01-22
   Grant date: 2021-11-23
   Inventor: 晋力京 (Ji-Li Jing)
   Assignee: 北京百度网讯科技有限公司

4. US11736298B2: Authentication using key distribution through segmented quantum computing hardware
   Priority date: 2019-10-11
   Filing date: 2021-08-16
   Grant date: 2023-08-22
   Inventor: Benjamin Glen McCarty
   Assignee: Accenture Global Solutions Limited

5. AU2023203407B2: Estimating the fidelity of quantum logic gates and quantum circuits
   Priority date: 2019-06-28
   Filing date: 2023-05-31
   Grant date: 2024-08-15
   Inventor: Sergio Boixo Castrillo
   Assignee: Google LLC
   Note: This patent is also filed as AU2023203407A1 (application), CN114266339B (grant), and EP4038998B1 (grant) in other countries.

6. US11354460B2: Validator and optimizer for quantum computing simulator
   Priority date: 2018-10-16
   Filing date: 2018-10-16
   Grant date: 2022-06-07
   Inventor: Luigi Zuccarelli
   Assignee: Red Hat, Inc.

7. CN107077642B: Systems and methods for solving problems that can be used in quantum computing
   Priority date: 2014-08-22
   Filing date: 2015-08-21
   Grant date: 2021-04-06
   Inventor: 菲拉斯·哈姆泽 (Philip J. Haussler)
   Assignee: D-波系统公司

8. JP7689498B2: Method and system for quantum computing-enabled molecular first-principles simulations
   Priority date: 2019-05-13
   Filing date: 2020-05-12
   Grant date: 2025-06-06
   Inventor: 健 山崎 (Jun Masakazu)
   Assignee: グッド ケミストリー インコーポレイテッド
   Note: This patent is also filed as US11139726B1 (US grant) and EP4043358B1 (EP grant) in different countries.

9. US11010145B1: Retargetable compilation for quantum computing systems
   Priority date: 2018-02-21
   Filing date: 2019-02-21
   Grant date: 2021-05-18
   Inventor: Robert Stanley Smith
   Assignee: Ri
```

Great! Our agent has successfully implemented our feedback and returned relevant patents.

## Step 7. Second HITL approach: Dynamic interrupts

As an alternative to using static breakpoints, we can incorporate human feedback by pausing the graph from within a node by using LangGraph's `interrupt` function. We can build a `human_in_the_loop` node that enables us to directly update the state of the graph as part of the flow rather than pausing at predetermined points.

```python
def human_in_the_loop(state: AgentState):
    value = interrupt('Would you like to revise the input or continue?')
    return {"messages": value}
```

We can instantiate a new graph and adjust the flow to include this node between the `guardian` and `assistant` nodes.

```json
new_builder = StateGraph(AgentState)

new_builder.add_node("guardian", guardian_moderation)
new_builder.add_node("block_message", block_message)
new_builder.add_node("human_in_the_loop", human_in_the_loop)
new_builder.add_node("assistant", call_llm)
new_builder.add_node("tools", ToolNode(tools))

new_builder.add_edge(START, "guardian")
new_builder.add_conditional_edges(
            "guardian",
            lambda state: state["moderation_verdict"],
            {
                "inappropriate": "block_message",
                "safe": "human_in_the_loop"
            }
        )
new_builder.add_edge("block_message", END)
new_builder.add_edge("human_in_the_loop", "assistant")
new_builder.add_conditional_edges(
    "assistant",
    tools_condition,
)
new_builder.add_edge("tools", "assistant")

memory = MemorySaver()

new_graph = new_builder.compile(checkpointer=memory)
display(Image(new_graph.get_graph().draw_mermaid_png()))
```

**Sortie :**

Super ! Passons notre entrée initiale pour lancer le workflow de l’agent.

```json
initial_input = {"messages": "Find patents for self-driving cars"}
config = {"configurable": {"thread_id": str(uuid.uuid4())}}
new_graph.invoke(initial_input, config=config)
```

**Sortie :**

```
{'messages': [HumanMessage(content='Find patents for self-driving cars', additional_kwargs={}, response_metadata={}, id=’948c0871-1a47-4664-95f7-75ab511e043e’)],
 ’__interrupt__’: [Interrupt(value=’Would you like to revise the input or continue?’, id=’8d6cf9e82f9e3de28d1f6dd3ef9d90aa’)]}
```

Comme vous pouvez voir, le graphique est interrompu et nous sommes invités à passer l’entrée en revue ou à continuer. Révisons l’entrée et reprenons le workflow de l’agent en utilisant la classe « Command » de LangGraph. Cette action met à jour l’état comme s’il provenait du nœud « human_feedback ».

```
for event in new_graph.stream(Command(resume="Forget that. Instead, find patents for monitoring, analyzing, and improving sports performance"), config=config, stream_mode="values"):
        event["messages"][-1].pretty_print()
```

**Sortie :**

```json
================================[1m Human Message [0m=================================

Find patents for self-driving cars
================================[1m Human Message [0m=================================

Forget that. Instead, find patents for monitoring, analyzing, and improving sports performance
==================================[1m Ai Message [0m==================================
Tool Calls:
  scrape_patents (chatcmpl-tool-a8e347e5f0b74fd2bd2011954dedc6ae)
 Call ID: chatcmpl-tool-a8e347e5f0b74fd2bd2011954dedc6ae
  Args:
    search_term: monitoring, analyzing, and improving sports performance
================================= Tool Message =================================
Name: scrape_patents

[{"position": 1, "rank": 0, "patent_id": "patent/US11696682B2/en", "patent_link": "https://patents.google.com/patent/US11696682B2/en", "serpapi_link": "https://serpapi.com/search.json?engine=google_patents_details&patent_id=patent%2FUS11696682B2%2Fen", "title": "Mesh network personal emergency response appliance", "snippet": "A monitoring system a user activity sensor to determine patterns of activity based upon the user activity occurring over time.", "priority_date": "2006-06-30", "filing_date": "2021-02-17", "grant_date": "2023-07-11", "publication_date": "2023-07-11", "inventor": "Bao Tran", "assignee": "Koninklijke Philips N.V.", "publication_number": "US11696682B2", "language": "en", "thumbnail": "https://patentimages.storage.googleapis.com/dd/39/a4/021064cf6a4880/US11696682-20230711-D00000.png", "pdf": "https://patentimages.storage.googleapis.com/b3/ce/2a/b85df572cd035c/US11696682.pdf", "figures": [{"thumbnail": "https://patentimages.storage.googleapis.com/21/15/19/5061262f67d7fe/US11696682-20230711-D00000.png", "full": "https://patentimages.storage.googleapis.com/08/62/a3/037cf62a2bebd0/US11696682-20230711-D00000.png"}
...
[REDACTED]
==================================[1m Ai Message [0m==================================

Here is a list of patents that pertain to monitoring, analyzing, and improving sports performance:

1. **Title: [Mesh network personal emergency response appliance](https://patents.google.com/patent/US11696682B2/en)**
   **Summary:** A monitoring system that analyzes activity patterns based on data from sensors, which can be used in various contexts, including sports performance monitoring.
   **Country status:** US - Active

2. **Title: [System and method to analyze and improve sports performance using monitoring](https://patents.google.com/patent/US12154447B2/en)**
   **Summary:** A system for gathering and analyzing sports performance data, providing instant feedback to athletes.
   **Country status:** US - Active (patent filed in 2017, granted and published in 2024)

3. **Title: [Multi-sensor monitoring of athletic performance](https://patents.google.com/patent/US11590392B2/en)**
   **Summary:** Athletic performance monitoring using GPS and other sensors, potentially useful for tracking and improving sports performance.
   **Country status:** US - Active

4. **Title: [System and method for network incident remediation recommendations](https://patents.google.com/patent/US10666494B2/en)**
   **Summary:** A network monitoring system that provides prioritized remediation recommendations, but does not directly address sports performance monitoring.
   **Country status:** US - Active

5. **Title: [Physiological monitoring methods](https://patents.google.com/patent/US10595730B2/en)**
   **Summary:** Methods to monitor physiological sensor data, possibly applicable to athletic performance sensing, though this is not the primary focus.
   **Country status:** US - Active

6. **Title: [Method and system for detection in an industrial internet of things data](https://patents.google.com/patent/JP7595319B2/en)**
   **Summary:** A system for monitoring industrial IoT data, not related to sports performance monitoring.
   **Country status:** JP - Active

7. **Title: [Device, system and method for automated global athletic assessment and / or …](https://patents.google.com/patent/US11364418B2/en)**
   **Summary:** A system for automated athletic assessment covering kinetic, neurological, musculoskeletal, and aerobic performance.
   **Country status:** US - Active

8. **Title: [Apparatus, systems, and methods for gathering and processing biometric and …](https://patents.google.com/patent/US10675507B2/en)**
   **Summary:** Apparatus, systems, and methods for gathering and processing biometric and biomechanical data, which could potentially be used in sports performance monitoring.
   **Country status:** US - Active

9. **Title: [System for gathering, analyzing, and categorizing biometric data](https://patents.google.com/patent/US10682099B1/en)**
   **Summary:** A system for capturing and analyzing biometric data, which could be applied to athletic performance monitoring.
   **Country status:** US - Active

10. **Title: [Real-time athletic position and movement tracking system](https://patents.google.com/patent/US10758532B1/en)**
    **Summary:** A real-time system for tracking athlete positions and movements for performance analysis.
    **Country status:** US - Active

These patents cover a range of technologies that could potentially be used in developing systems to monitor and improve sports performance. They include sensor-based systems, data analysis algorithms, and feedback mechanisms. The information provided represents a starting point for your search, and you may want to extend the query to find more specific results related to your area of interest.
```

Comme prévu, l’état du graphique a été mis à jour avec succès avec nos commentaires et les messages suivants de l’IA et de l’outil ont produit la sortie appropriée. Au lieu de renvoyer des brevets pour des voitures autonomes, l’agent a utilisé le commentaire humain pour renvoyer des brevets liés à la surveillance, à l’analyse et à l’amélioration des performances sportives.

## Récapitulatif

En suivant ce tutoriel, vous avez construit avec succès un agent IA spécialisé dans la recherche d’antériorités avec LangGraph et mis en place plusieurs workflows de type humain dans la boucle. L’étape suivante consiste à créer un autre agent IA, qui pourra être utilisé dans un système multi-agents, parallèlement à l’agent de recherche d’antériorités. Cet agent secondaire pourra éventuellement synthétiser les informations récupérées auprès de l’agent de recherche d’antériorités et formuler un rapport qui compare votre proposition de brevet à celles existantes. Place à la personnalisation !
