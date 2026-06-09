> Source : https://www.ibm.com/fr-fr/think/tutorials/build-corrective-rag-agent-granite-tavily

# Créer un agent RAG correctif avec IBM Granite et Tavily

[Les grands modèles de langage](https://www.ibm.com/fr-fr/think/topics/large-language-models) (LLM) sont incroyablement puissants, mais leurs connaissances se limitent à leurs [jeux de données](https://www.ibm.com/fr-fr/think/topics/dataset) d’entraînement. Lorsqu’ils répondent à des questions, surtout celles portant sur des informations spécifiques, évolutives ou propriétaires, les LLM sont sujets aux hallucinations ou peuvent fournir des réponses générales, non pertinentes. [La génération augmentée par récupération](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation) (RAG) fournit aux LLM des informations pertinentes, récupérées à partir de sources de données externes.

Cependant, tous les outils RAG ne se valent pas. La génération augmentée par récupération corrective (cRAG) ne se contente pas de s’appuyer sur la RAG traditionnelle, mais l’améliore de manière significative. Elle évalue la qualité et la pertinence des résultats récupérés pour renforcer la fiabilité. Si le contexte est faible, non pertinent ou provenant d’une source non fiable, la cRAG tente de trouver de meilleures informations grâce à des actions correctives, ou refuse explicitement de répondre au lieu de fabriquer une réponse. Cette technique rend les systèmes cRAG plus fiables dans des applications critiques telles que les questions-réponses liées aux politiques.

Dans ce tutoriel, vous apprendrez à créer un système RAG correctif (cRAG) robuste en utilisant les modèles IBM® Granite sur Watsonx et LangChain. Des cadres similaires tels que [LlamaIndex](https://www.ibm.com/fr-fr/think/topics/llamaindex) et [LangGraph](https://www.ibm.com/fr-fr/think/topics/langgraph) peuvent également être utilisés pour créer des flux RAG complexes, avec des nœuds distincts. Des techniques comme [le réglage fin](https://www.ibm.com/fr-fr/think/topics/fine-tuning) peuvent améliorer davantage la performance des LLM avec RAG spécialisée. Si les LLM comme ceux d’OpenAI (par exemple, les modèles [GPT](https://www.ibm.com/fr-fr/think/topics/gpt) [comme ChatGPT](https://www.ibm.com/fr-fr/think/topics/chatgpt)), sont également très utilisés pour ces agents, ce tutoriel porte sur IBM Granite.

Ici, nous nous concentrerons sur le cas d’utilisation suivant : répondre à des questions sur une police d’assurance (document PDF). Ce tutoriel vous guidera pour mettre en œuvre un algorithme RAG avancé qui :

- [Récupère les informations](https://www.ibm.com/fr-fr/think/topics/information-retrieval) de votre document PDF.

- Si les documents internes ne suffisent pas pour générer la réponse, l’agent peut avoir recours à une solution de recherche Web externe (Tavily).

- L’agent filtre intelligemment les résultats externes non pertinents, afin que les réponses soient adaptées aux politiques privées.

- L’agent donnera des réponses claires et limitées avec des informations partielles lorsqu’elles sont disponibles, ou refusera de répondre si le contexte est manquant.

## Cas d’utilisation : créer un agent fiable de demande de polices d’assurance

Ce tutoriel explique comment créer un agent de requête sur les polices d’assurance, conçu pour analyser les documents correspondants (une brochure PDF) et répondre avec précision aux questions de l’utilisateur. Nous utilisons les modèles IBM Granite et LangChain pour créer l’agent avec des étapes de récupération et de vérification robustes, qui garantissent des réponses de qualité, limitées à la source.

Découvrons comment les principes clés de la RAG s’appliquent à notre cas d’utilisation.

## Application des principes clés

**Base de connaissances interne (PDF) :** la principale source d’information de l’agent est la police d’assurance que vous avez fournie en PDF. Il convertit ce document en base de données vectorielle interrogeable.

**Recherche externe de secours (Tavily) :** si la base de connaissances interne ne dispose pas de suffisamment d’informations, l’agent peut consulter des sources Web externes via Tavily. Tavily est un moteur de recherche spécialement conçu pour les agents IA et les LLM. Il permet des résultats plus rapides, en temps réel, grâce à son interface de programmation d'application (API) pour les applications avec RAG.

**Notation du contexte :** l’évaluateur de récupération basé sur LLM fournira un score de pertinence aux éléments récupérés de votre PDF interne, tout en s’assurant que seuls les éléments de qualité sont inclus.

**Réécriture de la requête :** pour les recherches Web, l’agent peut reformuler la requête de l’utilisateur afin d’améliorer les chances de trouver des informations externes pertinentes.

**Vérification des sources :** une vérification basée sur LLM permet d’évaluer si les résultats de la recherche Web externe sont pertinents pour une police d’assurance privée, en filtrant les informations générales ou les détails sur les programmes de santé publique (comme Medi-Cal). Cette fonction empêche la génération de réponses trompeuses et permet l’autocorrection, ce qui contribue à l’affinement des connaissances.

**Génération sous contrainte :** le prompt final adressé au LLM lui demande strictement d’utiliser uniquement le contexte fourni, d’offrir des réponses exactes, d’indiquer si les informations ne sont pas disponibles, ou de fournir des réponses partielles avec des limitations explicites. Cette fonction améliore l’adaptabilité et la fiabilité des réponses générées.

## Prérequis

Vous devez disposer d’un [compte IBM® Cloud](https://cloud.ibm.com/registration?utm_source=ibm_developer&utm_content=in_content_link&utm_id=tutorials_awb-implement-xgboost-in-python&cm_sp=ibmdev-_-developer-_-trial) pour créer votre projet [watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai?utm_source=ibm_developer&utm_content=in_content_link&utm_id=tutorials_awb-implement-xgboost-in-python&cm_sp=ibmdev-_-developer-_-product).   Assurez-vous d’avoir accès à votre clé d’API watsonx et à votre ID de projet. Vous aurez également besoin d’une clé d’[API](https://www.ibm.com/fr-fr/think/topics/api) pour utiliser les capacités de recherche Web de Tavily AI.

## Étapes

### Étape 1. Configurer votre environnement

Bien que vous puissiez choisir parmi plusieurs outils, ce tutoriel vous explique comment configurer un compte IBM à l’aide d’un Jupyter Notebook.

1.  Connectez-vous à [watsonx.ai](https://dataplatform.cloud.ibm.com/registration/stepone?context=wx&apps=all) à l’aide de votre compte IBM Cloud.
2.  Créez un [projet watsonx.ai](https://www.ibm.com/docs/en/watsonx/saas?topic=projects-creating-project). Vous pouvez obtenir l’ID de votre projet à partir de ce dernier. Cliquez sur l’onglet Gérer. Ensuite, copiez l’ID du projet depuis la section Détails de la page Général. Vous aurez besoin de cet ID pour ce tutoriel.
3.  Créez un [Jupyter Notebook](https://www.ibm.com/docs/en/watsonx/saas?topic=editor-creating-managing-notebooks).

Cette étape ouvre un environnement de notebook dans lequel vous pourrez copier le code de ce tutoriel. Vous pouvez également télécharger ce notebook localement sur votre système, et le charger dans votre projet watsonx.ai en tant qu’actif. Pour voir d’autres tutoriels Granite, consultez les pages de la Communauté IBM Granite. Ce tutoriel est également disponible sur Github.

### Étape 2. Configurer le service d’exécution watsonx.ai et une clé API

1.  Créez une instance de service d’[exécution watsonx.ai](https://cloud.ibm.com/catalog/services/watsonxai-runtime) (choisissez le forfait Lite, qui est une instance gratuite).
2.  Générez une [clé d’interface de programmation d’applications (API)](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html).
3.  Associez le service d’exécution watsonx.ai au projet que vous avez créé dans [watsonx.ai](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/assoc-services.html?context=cpdaas).

### Étape 3. Installer les packages

Pour travailler avec le cadre LangChain et intégrer IBM WatsonxLLM, nous devons installer plusieurs bibliothèques essentielles. Commençons par installer les paquets requis. Cet ensemble comprend **langchain** pour le cadre RAG, **langchain-ibm** pour l’intégration de watsonx, **faiss-cpu** pour un stockage vectoriel efficace, **PyPDF2** pour le traitement des PDF, **sentence-transformers** pour obtenir un [embedding](https://www.ibm.com/fr-fr/think/topics/embedding) et  **requests** pour les appels d’API Web. Ces bibliothèques sont critiques pour appliquer les solutions de [machine learning](https://www.ibm.com/fr-fr/think/topics/machine-learning) et TAL.

```
# Install Libraries
!pip install langchain langchain-ibm faiss-cpu PyPDF2 sentence-transformers requests
```

**Remarque** : aucun GPU n’est nécessaire, mais l’exécution peut être plus lente sur les systèmes avec CPU. Cette étape ouvre un environnement de notebook dans lequel vous pourrez copier le code de ce tutoriel. Ce tutoriel est également disponible sur GitHub.

### Étape 4. Importer les bibliothèques requises

Ensuite, importez tous les modules requis et fournissez de manière sécurisée vos clés d’API pour watsonx et Tavily, ainsi que votre ID de projet watsonx.

```python
# Import required libraries

import os
import io
import getpass
from PyPDF2 import PdfReader
from langchain_ibm import WatsonxLLM
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import requests
from botocore.client import Config
import ibm_boto3
from langchain.prompts import PromptTemplate
from langchain.tools import BaseTool

# Watsonx
WML_URL = "https://us-south.ml.cloud.ibm.com"
WML_API_KEY = getpass.getpass(" Enter Watsonx API Key: ")
PROJECT_ID = input(" Enter Watsonx Project ID: ")

# Tavily
TAVILY_API_KEY = getpass.getpass(" Enter Tavily API Key: ")

print(" Credentials loaded.")
```

**os** permet de travailler avec le système d’exploitation.

**io** permet de travailler avec les flux de données.

**getpass** utilise un moyen sûr de capter des informations sensibles telles que les clés d’API et n’affiche pas les entrées à l’écran.

**PyPDF2.PdfReader** permet l’extraction de contenu à partir des PDF.

**langchain_ibm.WatsonxLLM** facilite l’utilisation du LLM IBM watsonx Granite dans le cadre LangChain.

**langchain.embeddings.HuggingFaceEmbeddings** utilise un modèle HuggingFace et génère les embeddings textuels importants pour la recherche sémantique.

**langchain.vectorstores.FAISS** est une bibliothèque conçue pour favoriser un stockage vectoriel et une recherche de similarités efficaces, qui nous permet de créer un index de vecteurs et de l’interroger.

**langchain.text_splitter.RecursiveCharacterTextSplitter** permet de découper de grandes parties de texte en petits morceaux pour traiter les documents qui ne tiendraient autrement pas en mémoire.

**langchain.schema.Document** représente une unité de texte arbitraire, avec les métadonnées associées, ce qui en fait un élément constitutif de Langchain.

**requests** permet d’effectuer des requêtes HTTP en externe aux API.

**botocore.client.Config** est une classe de configuration utilisée pour définir les paramètres de configuration pour les clients AWS/IBM Cloud Object Storage.

**ibm_boto3** est le SDK d’IBM Cloud Object Storage pour Python ; il permet d’interagir avec le stockage d’objets cloud.

**langchain.prompts.PromptTemplate** permet de créer des prompts structurés et réutilisables pour les modèles de langage.

**langchain.tools.BaseTool** est la classe de base à partir de laquelle vous créez des outils personnalisés, qui peuvent être fournis aux agents LangChain.

Cette étape met en place tous les outils et modules nécessaires pour traiter le texte, créer des embeddings, les stocker dans une base de données vectorielle et interagir avec le LLM IBM watsonx. Elle établit tous les éléments nécessaires à la création d’un système RAG capable d’obtenir, d’interroger et de rechercher différents types de données.

### Étape 5. Charger et traiter un PDF à partir d’IBM Cloud Object Storage

Lors de cette étape, nous chargerons le PDF de la police d’assurance à partir d’IBM Cloud Object Storage. Le code lit le PDF, ainsi que le contenu du texte, et divise le texte en blocs plus faciles à gérer. Ces morceaux sont convertis en embeddings numériques et stockés dans une base de données vectorielle FAISS qui préparera la recherche de similarités sémantiques ultérieurement, dans le contexte local, afin d’optimiser les résultats de la recherche.

```python
import os, types
import pandas as pd
from botocore.client import Config
import ibm_boto3

def __iter__(self): return 0

cos_client = ibm_boto3.client(service_name='s3',
ibm_api_key_id='YOUR_IBM_API_KEY',
ibm_auth_endpoint="https://iam.cloud.ibm.com/identity/token",
config=Config(signature_version='oauth'),
endpoint_url='https://s3.direct.us-south.cloud-object-storage.appdomain.cloud')

bucket = 'YOUR_BUCKET_NAME'
object_key = 'YOUR_OBJECT_KEY'

streaming_body_2 = cos_client.get_object(Bucket=bucket, Key=object_key)['Body']
```

```python
pdf_bytes = io.BytesIO(streaming_body_2.read())

reader = PdfReader(pdf_bytes)
text = ""
for page in reader.pages:
extracted = page.extract_text()
if extracted:
text += extracted

print(f" Extracted {len(text)} characters from PDF.")
```

```python
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(text)
print(f" Split into {len(chunks)} chunks.")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_texts(chunks, embeddings)

print(f" Created FAISS index.")
```

**ibm_boto3.client** permet au client d’interagir avec IBM Cloud Object Storage.

**Bucket** est le nom du compartiment de stockage d’objets cloud qui contient le PDF.

**object_key** est le nom du PDF dans le compartiment de stockage d’objets cloud.

**cos_client.get_object(...).read()** récupère le contenu du fichier PDF sous forme d’octets dans le stockage d’objets cloud.

**io. BytesIO** convertit les octets bruts du PDF en flux binaire en mémoire, dans un format utilisable par PdfReader.

**PdfReader** crée un objet capable d’analyser et d’extraire le texte du PDF.

**page.extract_text()** extrait le texte d’une seule page du PDF.

**RecursiveCharacterTextSplitter** est configuré pour diviser le texte extrait en morceaux de 500 caractères, avec un chevauchement de 50 caractères, afin de préserver le contexte.

**splitter.split_text(text)** divise toutes les pages du texte PDF en petits morceaux.

**HuggingFaceEmbeddings** charge un modèle transformateur de phrases qui a été pré-entraîné pour convertir les morceaux de texte en représentations vectorielles denses.

**FAISS.from_texts(chunks, embeddings)** construit un index FAISS en mémoire qui permet de rechercher les morceaux de texte en fonction de leur similarité sémantique.

Cette étape assure l’ingestion complète d’un document PDF, du cloud au texte prêt pour LLM, ainsi qu’une indexation confortable pour une récupération en temps réel.

### Étape 6. Initialiser le LLM et les outils

Lors de cette étape, vous allez configurer le LLM IBM Granite pour piloter le raisonnement de votre agent et l’intégrer à la fonction de recherche Web Tavily. Les paramètres du LLM sont configurés pour garantir des réponses factuelles et stables.

```python
llm = WatsonxLLM(
model_id="ibm/granite-3-2b-instruct",
url=WML_URL,
apikey=WML_API_KEY,
project_id=PROJECT_ID,
params={
"max_new_tokens": 300, # ~2-3 paragraphs, good for corrective RAG
"temperature": 0.2, # low temperature = more factual, stable answers
}
)

print(" Watsonx Granite LLM ready.")
```

```python
class TavilySearch(BaseTool):
name: str = "tavily_search"
description: str = "Search the web using Tavily for extra info."

def _run(self, query: str):
response = requests.post(
"https://api.tavily.com/search",
json={"api_key": TAVILY_API_KEY, "query": query}
)
response.raise_for_status()
return response.json()['results'][0]['content']

tavily_tool = TavilySearch()
```

**WatsonxLLM** instancie le wrapper LLM pour IBM watsonx, permettant l'interaction avec les modèles Granite.

**model_id="ibm/granite-3-2b-instruct"** est le modèle IBM Granite (un modèle d’instructions avec 2,7 milliards de paramètres) conçu pour les tâches d’IA générative basées sur les instructions.

**class TavilySearch(BaseTool)** définit un outil LangChain personnalisé pour effectuer des recherches Web à l’aide de l’API Tavily.

**tavily_tool = TavilySearch()** crée une instance exécutable de l’outil de recherche personnalisé Tavily.

Lors de l’initialisation de watsonxLLM, les valeurs **url**, **apikey** et **projet_id** de nos identifiants précédemment configurés sont transmises pour l’authentification et la connexion au service. Ses paramètres, comme **"max_new_tokens": 300**, limitent la longueur de la réponse, tandis que **"température": 0,2** contrôle la créativité de la sortie, favorisant des résultats plus déterministes.

La définition de la classe **TavilySearch** comprend une description de sa fonction. Sa logique est contenue dans la méthode **def \_run(self, query: str)**. Dans cette méthode, nous envoyons une requête HTTP POST au point de terminaison de l’API Tavily, y compris **TAVILY_API_KEY** et la requête de recherche dans la charge utile JSON. Nous vérifions ensuite s’il y a des erreurs HTTP avec **response.raise_for_status()** et analysons la réponse JSON pour accéder à l’extrait de contenu à partir du premier résultat de recherche.

Cette étape consiste à configurer le modèle de langage pour la génération de texte et inclut un outil de recherche Web externe permettant d’enrichir les connaissances du modèle.

### Étape 7. Définir des modèles de prompt et des fonctions d’assistance

Cette étape définit les différents templates de prompt qui guideront le comportement du LLM à différentes étapes du processus RAG. Cette approche inclut des prompts permettant d’évaluer la pertinence des morceaux de documents internes, de réécrire les requêtes des utilisateurs pour une meilleure recherche Web, ainsi qu’un nouveau prompt, essentiel pour vérifier la source des résultats de recherche Web. Des fonctions d’assistance permettant de noter les morceaux et de les récupérer dans la base de données vectorielle sont également définies.

```python
# Define Prompt Templates and Helper Functions

# Prompt for scoring the relevance of retrieved chunks
scoring_prompt_template = PromptTemplate.from_template(
"""
You are an evaluator. Score the relevance of the context chunk to the given insurance question.

Question: "{query}"

Context:
\"\"\"
{chunk}
\"\"\"

Respond only in this format:
Score: <0-5>
Reason: <one line reason>
"""
)

# Prompt for rewriting the user's query for better web search results
rewrite_prompt_template = PromptTemplate.from_template(
"""
You are a helpful assistant. Improve the following question to be clearer for an insurance information search.
Focus on making the query more specific if possible.

Original Question: "{query}"

Rewrite it to be clearer:
"""
)

# NEW: Prompt for verifying if Tavily context is from a relevant source (private policy vs. public program)
CONTEXT_SOURCE_VERIFICATION_PROMPT = PromptTemplate.from_template(
"""
You are an expert at identifying if a piece of text is from a general, public, or unrelated source
versus a specific, private, or relevant policy document.

Read the following context and determine if it appears to discuss general information,
public health programs (like Medi-Cal, Medicaid, Medicare, NHS, government-funded programs, state-funded),
or information that is clearly *not* specific to a private insurance policy like the one
the user might be asking about (assuming the user is asking about their own private policy).

If the context explicitly mentions or heavily implies public health programs, or is too general
to be useful for a specific private policy question, respond with "NO".
Otherwise (if it seems like it *could* be from a private policy context, a general insurance guide,
or does not explicitly mention public programs), respond with "YES".

Context:
\"\"\"
Response:
"""
)

# Function to score chunks using the LLM
def score_chunks(chunks, query):
scored = []
for chunk in chunks:
prompt = scoring_prompt_template.format(query=query, chunk=chunk)
response = llm(prompt).strip()

try:
# Extract score using more robust parsing
score_line = [line for line in response.splitlines() if "Score:" in line]
if score_line:
score = int(score_line[0].replace("Score:", "").strip())
else:
score = 0 # Default to 0 if score line not found
except Exception as e:
print(f" Could not parse score for chunk: {e}. Response: {response[:50]}...")
score = 0 # Default to 0 on error

scored.append((chunk, score))
return scored

# Function to retrieve documents from FAISS vector store
def retrieve_from_vectorstore(query):
# Retrieve top 8 similar documents from your PDF content
docs = vectorstore.similarity_search(query, k=8)
return [doc.page_content for doc in docs]

print(" Prompt templates and helper functions defined.")
```

Cette étape définit les différents templates de prompt qui guideront le comportement du LLM aux différentes étapes du processus RAG. Sont inclus les prompts permettant d’évaluer la pertinence des morceaux de documents internes, de réécrire les requêtes des utilisateurs pour une meilleure recherche Web, ainsi qu’un nouveau prompt, essentiel pour vérifier la source des résultats de recherche Web. Des fonctions d’assistance permettant de noter les morceaux et de les récupérer dans la base de données vectorielle sont également définies.

**PromptTemplate.from_template** est une fonctionnalité LangChain permettant de créer un template réutilisable pour la création de prompts.

**scoring_prompt_template** définit un prompt qui demande au LLM d’agir en tant qu’évaluateur et d’attribuer un score de pertinence (0-5) à un morceau de contexte donné en fonction d’une question.

**rewrite_prompt_template** définit un prompt qui guide le LLM pour améliorer ou clarifier la question de l’utilisateur à des fins de recherche.

**CONTEXT_SOURCE_VERIFICATION_PROMPT** définit un prompt qui demande au LLM de vérifier si un texte (par exemple, provenant d’une recherche Web) est issu d’un contexte de politique privée, ou d’une source générale ou publique.

**def score_chunks(chunks, requête)** définit une fonction qui prend une liste de morceaux de texte et une requête, et utilise ensuite le LLM pour évaluer la pertinence de chaque morceau.

**def retrieve_from_vectorstore(query)** définit une fonction pour récupérer les documents avec le plus haut degré de similarité auprès de la base de données vectorielle FAISS.

Dans la fonction **score_chunks**, une liste de notation vierge est initialisée. Pour chaque morceau, le **scoring_prompt_template** est formaté avec la requête et le morceau correspondants. Ce prompt formaté est ensuite envoyé au LLM, et la réponse est dépouillée. La fonction tente d’extraire le score entier (un score binaire s’il est simplifié en pertinent ou non pertinent) en identifiant la ligne « Score: » dans la réponse du modèle. Le morceau et son score analysé ou attribué par défaut sont ensuite ajoutés à la liste des scores. Cette partie du système sert d’évaluateur de récupération.

La fonction **react_from_vectorstore** met en œuvre une **vectorstore.similarity_search** pour trouver les 8 morceaux de documents les plus pertinents en fonction de la requête, et récupérer le **page_content** à partir des objets LangChain Document récupérés.

Cette étape permet de construire l’échafaudage conceptuel du système RAG correctif, afin que le LLM évalue le contexte et détermine comment récupérer les connaissances à partir des sources internes et externes.

### Étape 8. Implémenter la logique corrective RAG

La **récupération initiale** est la fonction qui analyse la base de données vectorielle du PDF.

**La notation du contexte** consiste à évaluer les morceaux de PDF récupérés en fonction de leur pertinence.

**Recours à Tavily** : si le contexte pertinent du PDF n’est pas suffisant, il interroge Tavily (recherche Web).

La **vérification des sources** est une étape alimentée par LLM qui consiste à vérifier si les résultats de Tavily sont pertinents pour une politique privée avant de les utiliser. Cette fonction permet d’éviter les réponses trompeuses relatives aux programmes de santé publique.

**Réécriture de la requête et deuxième recherche Tavily** : s’il n’y a toujours pas de contexte adéquat, il réécrit la requête et retente une recherche Tavily.

**Décision finale** : lorsqu’il y a un contexte pertinent, il est envoyé au LLM avec un prompt (strict) pour créer la réponse. S’il n’y a pas de contexte pertinent après toutes les tentatives viables, il envoie un refus poli.

```python
# Implement the Corrective RAG Logic

MIN_CONTEXT_LENGTH = 100 # Adjust this based on how much minimal context you expect for a partial answer
SIMILARITY_THRESHOLD = 3 # Only scores >= 3 used for vector store chunks

def corrective_rag(query: str, policy_context_keywords: list = None):
"""
Executes the Corrective RAG process to answer insurance queries.

Args:
query (str): The user's question.
policy_context_keywords (list, optional): Keywords related to the specific policy
(e.g., ["Super Star Health", "Care Health Insurance"]).
Used to make external searches more specific. Defaults to None.
Returns:
str: The final answer generated by the LLM or a predefined refusal.
"""
retrieved_context_pieces = [] # To store all relevant pieces found throughout the process

# Initial vector search & Scoring (from your PDF)
chunks_from_vectorstore = retrieve_from_vectorstore(query)
scored_chunks_vector = score_chunks(chunks_from_vectorstore, query)
good_chunks_vector = [chunk for chunk, score in scored_chunks_vector if score >= SIMILARITY_THRESHOLD]
retrieved_context_pieces.extend(good_chunks_vector)

current_context = "\n\n".join(retrieved_context_pieces)
print(f" Context length after initial vector scoring: {len(current_context)}")

# Prepare specific query for Tavily by optionally adding policy keywords
tavily_search_query = query
if policy_context_keywords:
tavily_search_query = f"{query} {' '.join(policy_context_keywords)}"

# Fallback: Tavily direct search (only if current context is too short from vector store)
if len(current_context) < MIN_CONTEXT_LENGTH:
print(f" Context too short from internal docs, trying Tavily direct with query: '{tavily_search_query}'...")
tavily_context_direct = tavily_tool._run(tavily_search_query)

if tavily_context_direct:
# --- NEW STEP: Verify Tavily Context Source ---
# Ask the LLM if the Tavily result seems to be from a private policy context or a public program
verification_prompt = CONTEXT_SOURCE_VERIFICATION_PROMPT.format(context=tavily_context_direct)
is_relevant_source = llm(verification_prompt).strip().upper()

if is_relevant_source == "YES":
retrieved_context_pieces.append(tavily_context_direct)
current_context = "\n\n".join(retrieved_context_pieces) # Re-combine all good context
print(f" Context length after Tavily direct (verified and added): {len(current_context)}")
else:
print(f" Tavily direct context source rejected (e.g., public program): {tavily_context_direct[:100]}...")
# Context is NOT added, so it remains short and triggers the next fallback or final refusal

# Fallback: Rewrite query + Tavily (only if context is still too short after direct Tavily)
if len(current_context) < MIN_CONTEXT_LENGTH:
print(" Context still too short, rewriting query and trying Tavily...")
rewrite_prompt = rewrite_prompt_template.format(query=query)
improved_query = llm(rewrite_prompt).strip()

# Add policy keywords to the rewritten query too
if policy_context_keywords:
improved_query = f"{improved_query} {' '.join(policy_context_keywords)}"

print(f" Rewritten query: '{improved_query}'")
tavily_context_rewritten = tavily_tool._run(improved_query)

if tavily_context_rewritten:
# --- NEW STEP: Verify Rewritten Tavily Context Source ---
verification_prompt = CONTEXT_SOURCE_VERIFICATION_PROMPT.format(context=tavily_context_rewritten)
is_relevant_source = llm(verification_prompt).strip().upper()

if is_relevant_source == "YES":
retrieved_context_pieces.append(tavily_context_rewritten)
current_context = "\n\n".join(retrieved_context_pieces) # Re-combine all good context
print(f" Context length after rewritten Tavily (verified and added): {len(current_context)}")
else:
print(f" Tavily rewritten context source rejected (e.g., public program): {tavily_context_rewritten[:100]}...")

# --- Final Decision Point ---
# Now, `current_context` holds ALL the "good" and "verified" context we managed to gather.
# The decision to call the LLM for an answer or give a hard refusal is based on `current_context`'s length.

# Final check for absolutely no good context
# This triggers only if *no* relevant internal or external context was found or verified.
if len(current_context.strip()) == 0:
print(" No good context found after all attempts. Returning absolute fallback.")
return (
"Based on the information provided, there is no clear mention of this specific detail "
"in the policy documents available."
)

# If we have *any* context (even if short), pass it to the LLM to process
# The LLM will then decide how to phrase the answer based on its prompt instructions
# (exact, partial, or full refusal if context is irrelevant or insufficient based on its own reasoning).
final_prompt = (
f"You are a careful insurance expert.\n"
f"Use ONLY the following context to answer the user's question. If the context is too short "
f"or does not contain the answer, you must indicate that.\n"
f"Context:\n```\n{current_context}\n```\n\n" # Pass the gathered context
f"User's Question: {query}\n\n" # Pass the original query for the LLM's reference
f"NEVER add new details that are not in the context word-for-word.\n"
f"If the context clearly says the answer, give it exactly as written in the context, but in prose.\n"
f"If the context does not mention the topic at all, or the answer is not in the context, say:\n"
f"\"I'm sorry, but this information is not available in the provided policy details.\"\n"
f"If the context partially mentions the topic but does not directly answer the specific question (e.g., mentions 'dental' but not 'wisdom tooth removal'), reply like this:\n"
f"\"Based on the information provided, here’s what is known: [quote relevant details from the context related to the broad topic.] "
f"There is no clear mention of the specific detail asked about.\"\n"
f"Do NOT assume. Do NOT make up extra information.\n"
f"Do NOT generate extra questions or conversational filler.\n"
f"Final Answer:"
)

return llm(final_prompt)

print(" Corrective RAG logic implemented.")
```

Le premier passage du paramètre **policy_context_keywords** vous permet d’ajouter des termes de votre police (par exemple, son nom, l’assureur) afin d’affiner la recherche sur Tavily.

**MIN_CONTEXT_LENGTH** définit la longueur minimale acceptable du contexte récupéré.

**SIMILARITY_THRESHOLD **définit le score minimum de pertinence qu’un morceau doit avoir pour être considéré comme « bon ».

**def corrective_rag(...)** définit la fonction principale qui orchestre l’ensemble du [workflow](https://www.ibm.com/fr-fr/think/topics/workflow) de RAG corrective.

La fonction **corrective_rag** crée **retrieved_context_pieces** pour recueillir le contexte pertinent. Elle récupère et note d’abord les **chunks_from_vectorstore à partir de la base de données vectorielle** PDF en fonction de la requête, puis **scored_chunks_vector** évalue leur pertinence en utilisant le modèle de langage. Seuls les **good_chunks_vector** qui respectent **SIMILARITY_THRESHOLD** sont retenus. **current_context** est ensuite compilé à partir de ces éléments.

Si la valeur **current_context** est inférieure à **MIN_CONTEXT_LENGTH**, le système tente d’effectuer une recherche Web. Il construit **tavily_search_query**, intégrant potentiellement **policy_context_keywords**. Une recherche directe (**tavily_context_direct**) est effectuée. Un prompt de vérification est obligatoirement créé et envoyé au LLM pour déterminer si le résultat de la recherche Web**(is_relevant_source)** provient d’une politique privée, ou d’un programme public. Si la réponse est OUI, le contexte est ajouté.

Si le contexte reste insuffisant, le système se prépare à réécrire la requête. Il utilise **rewrite_prompt** pour obtenir une **improved_query** du LLM, puis effectue une deuxième recherche Web (**tavily_context_rewritten**). Ce nouveau contexte fait également l’objet d’une vérification des sources.

Enfin, **si** **len(current_context.strip()) == 0** est la dernière vérification. Si aucun contexte pertinent n’est trouvé après toutes ces tentatives, un message de refus prédéfini est renvoyé. Sinon, un **final_prompt** est créé avec tout le contexte vérifié et envoyé au modèle de langage pour générer sa réponse finale.

La fonction **corrective_rag** gère en détail les fonctions de récupération, de notation et de vérification du système de RAG corrective. Elle permet une mise à jour constante de la base de connaissances et du flux de connaissances, et favorise des réponses efficaces et contextuelles.

### Étape 9. Tester le système

Pour finir, exécutez la fonction **corrective_rag** avec un exemple de requête. Il est essentiel de fournir des **policy_context_keywords** spécifiques à votre document PDF. Ces mots-clés rendront la recherche Web Tavily plus pertinente par rapport à votre politique réelle, empêchant les informations générales ou publiques relatives aux programmes de santé de polluer votre contexte.

Observez les instructions d’impression pour connaître le contexte, la longueur et les résultats de vérification afin de comprendre le flux d’informations.

```python
query = "How does the policy cover for In-Patient Hospitalisation?"
result = corrective_rag(query)

print("\n FINAL ANSWER:\n")
print(result)
```

**policy_specific_keywords = \["Super Star Health", "Care Health Insurance"\]** définit une liste de mots-clés pertinents pour la police d’assurance téléchargée, ce qui permet d’affiner les résultats de la recherche Web.

**query = "..."** définit la question que l’utilisateur est susceptible de poser.

**result = corrective_rag(query, policy_context_keywords=policy_specific_keywords)** appelle la fonction **corrective_rag** principale et transmet la requête de l’utilisateur et les mots-clés associées à la police pour lancer le processus RAG.

**print("\n FINAL ANSWER (...)")**  affiche un en-tête clair avant l’impression de la réponse générée.

**print(result)** produit la réponse finale renvoyée par le système **corrective_rag**.

Cette étape montre comment invoquer le système de RAG corrective complet à l’aide d’un exemple de requête et de mots-clés, afin de démontrer ses fonctionnalités de bout en bout dans un scénario réel.

## Points essentiels à retenir

Le système de RAG corrective a mis en place une base de connaissances PDF interne entièrement coordonnée avec un service externe (Tavily), afin de récupérer des informations complètes pour les requêtes complexes.

Il a évalué et filtré avec précision le contexte récupéré à l’aide d’une notation basée sur LLM et d’une vérification des sources indispensable pour garantir l’utilisation d’informations valides et fiables.

Le système a démontré sa capacité à améliorer la recherche externe en réécrivant intelligemment les requêtes des utilisateurs pour demander des informations plus ciblées et de meilleure qualité.

Grâce à la génération sous contrainte, une réponse fiable et contextualisée a été générée ; le système a poliment refusé de répondre lorsqu’il n’y avait pas suffisamment d’informations vérifiées connues.

Cet exemple nous a montré comment utiliser LangChain et les LLM IBM Granite sur watsonx pour développer des applications d’IA puissantes et dignes de confiance dans un domaine aussi sensible que les questions-réponses relatives aux polices d’assurance.
