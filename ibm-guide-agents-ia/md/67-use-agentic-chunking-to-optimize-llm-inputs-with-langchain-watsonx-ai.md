> Source : https://www.ibm.com/fr-fr/think/tutorials/use-agentic-chunking-to-optimize-llm-inputs-with-langchain-watsonx-ai

# Implémenter le découpage agentique pour optimiser les entrées des LLM avec Langchain et watsonx.ai

## Qu’est-ce que le découpage agentique ?

La façon dont les modèles de langage traitent et segmentent le texte est en train de changer, passant de l’approche statique traditionnelle à un processus plus efficace et plus réactif. Contrairement au découpage traditionnel en blocs de taille fixe, qui découpe les documents volumineux à des points fixes, le découpage agentique utilise des techniques basées sur l’IA pour analyser le contenu dans le cadre d’un processus dynamique afin de déterminer la meilleure façon de segmenter le texte.

Le découpage agentique utilise des méthodes de division de texte basées sur l’IA, le découpage récursif et les méthodes de chevauchement de blocs, qui fonctionnent simultanément pour affiner la capacité de découpage, en préservant les liens entre les idées notables tout en optimisant les fenêtres contextuelles en temps réel. Avec le découpage agentique, chaque bloc est enrichi de métadonnées pour approfondir la précision de la récupération et l’efficacité globale du modèle. Ceci est particulièrement important dans les applications RAG, où la segmentation des données peut avoir un impact direct sur la qualité de récupération et la cohérence de la réponse. Le contexte significatif est préservé dans tous les petits fragments, ce qui rend cette approche extrêmement importante pour les chatbots, les bases de connaissances et les cas d’utilisation de l’IA générative. Des cadres comme Langchain ou LlamaIndex améliorent encore l’efficacité de la récupération et rendent cette méthode très efficace. 

#### **Éléments clés du découpage agentique**

**1. Stratégie de découpage adaptative :** choisissez dynamiquement la meilleure méthode de découpage en fonction du type de contenu, de l’intention derrière la requête et des besoins de récupération pour garantir une segmentation efficace.

**2. Dimensionnement dynamique des blocs :** modification des tailles de blocs en temps réel en tenant compte de la structure sémantique et du contexte, au lieu de s’en tenir à des limites fixes de tokens.

**3. Préservation du contexte :** évaluer intelligemment le chevauchement des blocs pour conserver une cohérence intacte et éviter de perdre des informations essentielles, et ainsi améliorer l’efficacité de la récupération.

 

#### **Avantages du découpage agentique par rapport aux méthodes traditionnelles**

Le découpage agentique offre des avantages par rapport au découpage traditionnel :

**a. Conserve le contexte :** conserve les informations cruciales sans coupure inutile.

**b. Dimensionnement intelligent :** ajuste les limites des blocs en fonction du sens et de la signification.

**c. Optimisé pour les requêtes :** affine en permanence les blocs en fonction des requêtes spécifiques.

**d. Récupération efficace : **améliore la recherche et la production des systèmes RAG en minimisant la fragmentation inutile.

 

Dans ce tutoriel, vous allez découvrir la stratégie de découpage agentique en utilisant le [modèle IBM](https://www.ibm.com/fr-fr/granite) Granite-3.0-8B-Instruct désormais disponible sur [watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai). L’objectif global est d’effectuer un découpage efficace pour implémenter efficacement la RAG.

## Prérequis

Vous devez disposer d’un [compte IBM Cloud](https://cloud.ibm.com/registration?utm_source=ibm_developer&utm_content=in_content_link&utm_id=tutorials_awb-implement-xgboost-in-python&cm_sp=ibmdev-_-developer-_-trial) pour créer un projet [watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai?utm_source=ibm_developer&utm_content=in_content_link&utm_id=tutorials_awb-implement-xgboost-in-python&cm_sp=ibmdev-_-developer-_-product).

## Étapes

### Étape 1. Configurez votre environnement

Bien que vous puissiez choisir parmi plusieurs outils, ce tutoriel vous explique comment configurer un compte IBM pour utiliser un Jupyter Notebook.

1.  Connectez-vous à [watsonx.ai](https://dataplatform.cloud.ibm.com/registration/stepone?context=wx&apps=all) en utilisant votre compte IBM Cloud.

2.  Créez un [projet watsonx.ai](https://www.ibm.com/docs/en/watsonx/saas?topic=projects-creating-project).  Vous pouvez obtenir l’ID de votre projet à partir de celui-ci. Cliquez sur l’onglet Manage (Gérer). Ensuite, copiez l’ID du projet dans la section Details (Détails) de la page General (Général). Vous aurez besoin de cet ID pour ce tutoriel.

3.  Créez un [Jupyter Notebook](https://www.ibm.com/docs/en/watsonx/saas?topic=editor-creating-managing-notebooks).

Cette étape ouvre un environnement Jupyter Notebook dans lequel vous pouvez copier le code de ce tutoriel. Vous pouvez également télécharger ce notebook sur votre système local et le charger dans votre projet watsonx.ai en tant qu’actif. Vous trouverez d’autres tutoriels Granite auprès de la [Communauté IBM Granite](https://github.com/ibm-granite-community). Ce Jupyter Notebook, ainsi que les jeux de données utilisés, se trouvent sur GitHub.

### Étape 2. Configurez une instance d’exécution watsonx.ai et une clé d’API

1.  Créez une instance de service d’exécution [watsonx.ai](https://cloud.ibm.com/catalog/services/watsonxai-runtime) (sélectionnez votre région et choisissez le plan Lite, qui est une instance gratuite).

2.  Générez une [clé d’API](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html).

3.  Associez l’instance de service d’exécution watsonx.ai au projet que vous avez créé dans [watsonx.ai](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/assoc-services.html).

### Étape 3. Installez et importez les bibliothèques pertinentes et configurer vos identifiants

Vous aurez besoin de quelques bibliothèques et modules pour ce tutoriel. Veuillez vous assurer d’importer les éléments suivants. S’ils ne sont pas installés, une rapide commande pip install vous permettra d’y remédier.

*Remarque : ce tutoriel a été créé avec Python 3.12.7*

```
!pip install -q langchain langchain-ibm langchain_experimental langchain-text-splitters langchain_chroma transformers bs4 langchain_huggingface sentence-transformers
```

```python
import getpass
import requests
from bs4 import BeautifulSoup
from langchain_ibm import WatsonxLLM
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.schema import SystemMessage, HumanMessage
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.prompts import ChatPromptTemplate
from langchain.vectorstores import Chroma
from langchain.tools import tool
from langchain.agents import AgentExecutor
from langchain.memory import ConversationBufferMemory
from transformers import AutoTokenizer
from ibm_watsonx_ai.foundation_models.utils.enums import EmbeddingTypes
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain.chains.combine_documents import create_stuff_documents_chain
```

 

Pour définir nos identifiants, nous avons besoin de la clé **"WATSONX_APIKEY"** et du **"WATSONX_PROJECT_ID"**. Nous allons également définir l’URL qui servira de point de terminaison d’API.

```json
load_dotenv(os.getcwd()+"/.env", override=True)
credentials = {
"url": "https://us-south.ml.cloud.ibm.com",
"apikey": os.getenv("WATSONX_APIKEY", ""),
}
project_id = os.getenv("PROJECT_ID", "")
```

### Étape 4. Initialisez votre modèle de langage. 

Pour ce tutoriel, nous vous recommandons d’utiliser le modèle Granite-3.0-8B-Instruct d’IBM comme LLM afin d’obtenir des résultats similaires. Vous pouvez utiliser les modèles IA de votre choix. Vous trouverez les modèles de fondation disponibles avec watsonx [ici](https://www.ibm.com/fr-fr/products/watsonx-ai/foundation-models). 

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

###  Étape 5. Chargez votre document

Cette fonction extrait le contenu textuel de la fiche explicative d’IBM sur le machine learning. Cette fonction supprime les éléments HTML indésirables (scripts, styles) et renvoie un texte propre et lisible.

```python
def get_text_from_url(url):
response = requests.get(url)
if response.status_code != 200:
raise ValueError(f"Failed to fetch the page, status code: {response.status_code}")
soup = BeautifulSoup(response.text, "html.parser")
for script in soup(["script", "style"]):
script.decompose()
return soup.get_text(separator="\n", strip=True)
```

```
url = "https://www.ibm.com/fr-fr/think/topics/machine-learning"
web_text = get_text_from_url(url)
web_text
```

Au lieu d’utiliser une méthode de segmentation de longueur fixe, nous avons utilisé un LLM pour segmenter le texte en fonction de sa signification. Cette fonction tire parti d’un LLM pour diviser intelligemment le texte en blocs sémantiquement significatifs en fonction des sujets.

```python
def agentic_chunking(text):
"""
Dynamically splits text into meaningful chunks using LLM.
"""
system_message = SystemMessage(content="You are an AI assistant helping to split text into meaningful chunks based on topics.")

human_message = HumanMessage(content=f"Please divide the following text into semantically different, separate and meaningful chunks:\n\n{text}")

response = llm.invoke([system_message, human_message]) # LLM returns a string
return response.split("\n\n") # Split based on meaningful sections
```

```
chunks = agentic_chunking(web_text)
chunks
```

Imprimons les blocs pour mieux comprendre leur structure de sortie.

```python
for i, chunk in enumerate(chunks,1):
print(f"Chunk {i}:\n{chunk}\n{'-'*40}")
```

Parfait. Les blocs ont été créés avec succès par les agents dans la production.

### Étape 6. Créez une base de données vectorielle

Maintenant que nous avons découvert le découpage agentique sur le texte, passons à l’implémentation RAG.

Pour ce tutoriel, nous choisissons les blocs produits par les agents et les convertissons en embeddings vectoriels. Pour cela, nous pouvons utiliser la base de données vectorielle open source Chroma DB. Nous pouvons facilement accéder aux fonctionnalités de Chroma via le package langchain_chroma. Initialisons notre base de données vectorielle Chroma, fournissons-lui notre modèle d’embeddings et ajoutons nos documents produits par découpage agentique.

```
embeddings_model = HuggingFaceEmbeddings(model_name="ibm-granite/granite-embedding-30m-english")
```

**Créez une base de données vectorielle Chroma**

```
vector_db = Chroma(
collection_name="example_collection",
embedding_function=embeddings_model
)
```

**Convertissez chaque bloc de texte en objet document**

```
documents = [Document(page_content=chunk) for chunk in chunks]
```

**Ajoutez les documents à la base de données vectorielle**

```
vector_db.add_documents(documents)
```

### Étape 7. Structurez le modèle de prompt

Nous pouvons maintenant créer un modèle de prompt pour notre LLM. Ce modèle permet de poser plusieurs questions tout en conservant une structure de prompt cohérente. De plus, nous pouvons intégrer notre base de données vectorielle en tant que système de récupération, finalisant ainsi le cadre des exigences RAG.

```
prompt_template = """<|start_of_role|>user<|end_of_role|>Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
{context}
Question: {input}<|end_of_text|>
<|start_of_role|>assistant<|end_of_role|>"""
qa_chain_prompt = PromptTemplate.from_template(prompt_template)
combine_docs_chain = create_stuff_documents_chain(llm, qa_chain_prompt)
rag_chain = create_retrieval_chain(vector_db.as_retriever(), combine_docs_chain)
```

### Étape 8. Promptez la chaîne RAG

En utilisant ces blocs agentiques dans le workflow RAG, lançons une requête utilisateur. Tout d’abord, nous pouvons envoyer un prompt stratégique au modèle sans aucun contexte supplémentaire à partir de la base de données vectorielle que nous avons construit pour tester si le modèle utilise ses connaissances intégrées ou véritablement en utilisant le contexte RAG. À l’aide de la fiche explicative de machine learning d’IBM, posons maintenant la question.

```
output = llm.invoke("What is Model optimization process")
output
```

Il est clair que le modèle n’a pas été entraîné sur des informations concernant le processus d’optimisation des modèles et, sans outils ou informations externes, il ne peut pas nous fournir les informations correctes. Le modèle hallucine. Essayons maintenant de fournir la même requête à la chaîne RAG avec les blocs agentiques que nous avons créés.

```json
rag_output = rag_chain.invoke({"input": "What is Model optimization process?"})
rag_output['answer']
```

Parfait. Le modèle Granite a correctement utilisé les blocs RAG en tant que contexte pour nous fournir des informations correctes sur le processus d’optimisation des modèles tout en préservant la cohérence sémantique.

### Récapitulatif

Dans ce tutoriel, nous avons généré des éléments d’information pertinents plus petits à l’aide d’agents IA dans le processus de découpage, et nous avons construit un pipeline de génération augmentée de récupération (RAG).

Cette méthode améliore la recherche d’informations et l’optimisation des fenêtres contextuelles à l’aide de l’intelligence artificielle et du traitement automatique du langage naturel (NLP). Il rationalise les blocs de données pour améliorer l’efficacité de la récupération lors de l’exploitation de grands modèles de langage (LLM), comme les modèles GPT d’OpenAI, pour de meilleurs résultats.
