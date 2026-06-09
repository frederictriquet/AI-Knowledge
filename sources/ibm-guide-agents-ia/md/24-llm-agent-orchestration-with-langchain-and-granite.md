> Source : https://www.ibm.com/fr-fr/think/tutorials/llm-agent-orchestration-with-langchain-and-granite

# Orchestration d’agents LLM : guide étape par étape avec LangChain et Granite

##

L’orchestration d’agents LLM fait référence au processus de gestion et de coordination des interactions entre un grand modèle de langage (LLM) et divers outils, API ou processus, afin d’exécuter des tâches complexes au sein de systèmes d’IA. Elle implique la structuration de workflows dans lesquels un agent d’IA, alimenté par l’intelligence artificielle, agit comme décideur central ou moteur de raisonnement, orchestrant ses actions en fonction des entrées, du contexte et des sorties provenant de systèmes externes. À l’aide d’un cadre d’orchestration, les LLM peuvent s’intégrer de manière fluide à des API, des bases de données et d’autres applications d’IA, permettant ainsi l’activation de fonctionnalités telles que les chatbots et les outils d’automatisation. Les frameworks d’agents open source renforcent encore l’adaptabilité de ces systèmes, rendant les LLM plus efficaces dans des scénarios concrets.

Beaucoup de gens confondent orchestration de LLM et orchestration d’agents LLM. L’illustration suivante met en évidence les différences principales entre ces deux concepts :

  Différence clé entre l’orchestration de LLM et l’orchestration d’agents LLM

Dans ce tutoriel, vous allez apprendre à créer un agent autonome propulsé par des grands modèles de langage (LLM) en utilisant les modèles IBM® Granite et LangChain. Nous allons découvrir comment les agents exploitent des composants clés tels que la mémoire, la planification et l’action pour effectuer des tâches intelligentes. Vous mettrez également en œuvre un système pratique qui traite le texte d’un livre, répond dynamiquement à des questions, et évalue ses performances à l’aide d’indicateurs tels que BLEU, la précision, le rappel et le score F1.

## Cadre pour les agents autonomes basés sur des LLM

Le cadre présenté dans la Figure 1 offre une conception holistique pour des agents autonomes basés sur des grands modèles de langage (LLM), en mettant l’accent sur l’interaction entre des composants clés : le profil, la mémoire, la planification et l’action. Chaque composant représente une étape critique dans la construction d’un agent autonome capable de raisonnement, de prise de décision et d’interaction avec des environnements dynamiques.[1](#f01)

  Cadre pour les agents autonomes basés sur des LLM

**1. Profil : définir l’identité de l’agent**

Le profil donne à l’agent son identité en intégrant des informations telles que les données démographiques, les traits de personnalité et le contexte social. Ce processus permet à l’agent d’interagir de manière personnalisée. Les profils peuvent être conçus manuellement, générés par des modèles d’IA générative tels que les modèles IBM Granite ou GPT (Generative Pretrained Transformer) d’OpenAI, ou alignés sur des jeux de données spécifiques pour répondre aux besoins de la tâche. Grâce au prompt engineering, les profils peuvent être affinés dynamiquement afin d’optimiser les réponses. De plus, dans le cadre d’une orchestration multi-agent, le profil permet de définir les rôles et les comportements, assurant une coordination fluide entre les algorithmes d’IA et les systèmes de prise de décision.

**2. Mémoire : stocker et utiliser le contexte**

La mémoire aide l’agent à conserver et à retrouver les interactions passées, permettant ainsi des réponses contextualisées. Elle peut être unifiée (toutes les données au même endroit) ou hybride (structurée et non structurée). Les opérations telles que la lecture, l’écriture et la réflexion permettent à l’agent d’apprendre par l’expérience et de fournir des réponses cohérentes et informées. Une mémoire bien structurée améliore l’orchestration multi-agent en garantissant que différents agents, y compris ceux spécialisés dans une tâche spécifique, puissent partager et récupérer efficacement les données pertinentes. Dans des frameworks comme AutoGen et Crew AI, la mémoire joue un rôle essentiel dans le maintien de la continuité au sein de l’écosystème des agents collaboratifs, garantissant une coordination fluide et une exécution optimisée des tâches.

**3. Planification : élaborer des stratégies d’action**

La planification permet à l’agent de définir des stratégies pour atteindre des objectifs. Elle peut suivre des étapes prédéfinies ou s’adapter dynamiquement en fonction des retours de l’environnement, des humains ou du LLM lui-même. En intégrant des algorithmes d’IA et en s’appuyant sur une base de connaissances, la planification peut être optimisée pour améliorer l’efficacité du raisonnement et la précision de la résolution de problèmes. Dans les applications LLM, la planification joue un rôle crucial pour garantir que la compréhension du langage naturel et les processus de décision sont alignés avec les objectifs de l’agent. En outre, les techniques d’augmentation par récupération renforcent la capacité de l’agent à accéder dynamiquement à des informations pertinentes, améliorant ainsi la précision des réponses. Cette flexibilité garantit que l’agent reste performant dans des scénarios changeants, notamment dans une orchestration multi-agent où plusieurs agents coordonnent leurs plans pour atteindre des objectifs complexes tout en assurant une évolutivité adaptée à des tâches variées et étendues.

**4. Action : exécuter les décisions**

Les actions représentent la manière dont l’agent interagit avec le monde : accomplir des tâches, collecter des informations ou communiquer. Il utilise la mémoire et la planification pour guider son exécution, emploie des outils si nécessaire et adapte son état interne en fonction des résultats afin de s’améliorer en continu. L’optimisation de l’algorithme d’exécution des actions garantit l’efficacité, en particulier lors de l’intégration de modèles de raisonnement propulsés par GPT et de techniques d’IA générative pour la prise de décision en temps réel.

En combinant ces composants, le cadre transforme les LLM en agents adaptatifs capables de raisonner, d’apprendre et d’exécuter des tâches de manière autonome. Cette conception modulaire est idéale pour des applications telles que le service client, l’assistance à la recherche ou la résolution créative de problèmes.

## Cas d’utilisation : Créer un agent de connaissances interrogeable

Ce tutoriel explique comment créer un agent de connaissances interrogeable conçu pour traiter de longs documents texte (comme des livres) et répondre avec précision aux requêtes des utilisateurs. Sur la base des modèles IBM Granite et LangChain, l’agent est créé en suivant les principes du cadre pour les agents autonomes basés sur des LLM. Les composants du cadre s’alignent parfaitement avec le workflow de l’agent afin de garantir son adaptabilité et des réponses intelligentes.

**Découvrons comment le cadre s’applique à notre cas d’utilisation.**

  Application du cadre

**Profil :** l’agent est conçu avec un profil d’« assistant de connaissances », axé sur les tâches de synthèse, de réponse à des questions et de raisonnement. Son contexte est personnalisé pour traiter un document spécifique (par exemple, The Adventures of Sherlock Holmes).

**Mémoire :** l’agent utilise une mémoire hybride en intégrant des extraits du livre dans une base de données vectorielle FAISS. Cette capacité lui permet de récupérer dynamiquement un contexte pertinent lors des requêtes. Les opérations de mémoire telles que la lecture (récupération) et l’écriture (mise à jour des embeddings) garantissent la capacité de l’agent à s’adapter à de nouvelles requêtes au fil du temps.

**Planification :** Planification : la résolution de requêtes implique un raisonnement linéaire (single-path). L’agent récupère les segments de texte pertinents, génère des réponses à l’aide du modèle LLM Granite d’IBM, puis évalue la précision des résultats. Une planification sans boucles de rétroaction garantit la simplicité, tandis que la modularité du système permet d’intégrer ces boucles lors de futures itérations.

**Action :** l’agent exécute la résolution de requêtes en combinant récupération de mémoire et traitement via LLM. Il accomplit des tâches telles que la génération de réponses, le calcul des indicateurs de précision (BLEU, précision, rappel et score F1) et la visualisation des résultats pour une interprétation par l’utilisateur. Ces sorties reflètent la capacité de l’agent à agir intelligemment en s’appuyant sur le raisonnement et la planification.

## Prérequis

Vous devez disposer d’un compte IBM Cloud pour créer un projet watsonx.ai.  

## Étapes

### Étape 1. Configurer votre environnement

Bien que vous puissiez faire votre choix parmi plusieurs outils, ce tutoriel vous guide pas à pas pour configurer un compte IBM à l’aide d’un Jupyter Notebook.

1.  Connectez-vous à watsonx.ai en utilisant votre compte IBM Cloud.
2.  2\. Créez un projet watsonx.ai. Vous pouvez obtenir l’ID de votre projet à partir de ce dernier. Cliquez sur l’onglet **Manage** (Gérer). Ensuite, copiez l’ID du projet depuis la section **Details** (Détails) de la page **General** (Général). Vous aurez besoin de cet ID pour ce tutoriel.
3.  3\. Créez un Jupyter Notebook.

Cette étape ouvre un environnement de notebook dans lequel vous pouvez copier le code de ce tutoriel. Vous pouvez également télécharger ce notebook sur votre système local et le charger dans votre projet watsonx.ai en tant qu’actif. Pour voir d’autres tutoriels Granite, consultez les pages de la Communauté IBM Granite. Ce tutoriel est également disponible sur GitHub.

### Étape 2. Configurer le service d’exécution watsonx.ai et une clé API

1.  Créez une instance de service Runtime watsonx.ai (choisissez le plan Lite, qui est une instance gratuite).
2.  Générez une clé API (interface de programmation d’applications).
3.  Associez le service Runtime watsonx.ai au projet que vous avez créé dans watsonx.ai.

### Étape 3. Installer les packages

Pour travailler avec le framework LangChain et intégrer IBM WatsonxLLM, nous devons installer plusieurs bibliothèques essentielles. Commençons par installer les paquets requis :

*Remarque : si vous utilisez l’ancienne version de`pip` , vous pouvez utiliser la commande`pip install --upgrade pip` pour vous mettre à niveau et faciliter l’installation des paquets les plus récents, qui pourraient ne pas être compatibles avec les anciennes versions. Mais si vous utilisez déjà la dernière version ou si vous avez récemment mis à jour vos packages, vous pouvez ignorer cette commande.*

```
!pip install --upgrade pip
!pip install langchain faiss-cpu pandas sentence-transformers
%pip install langchain
!pip install langchain-ibm
```

Dans la cellule de code précédente,

- `LangChain`  : cadre principal pour la création d’applications avec des modèles de langage.
- `faiss-cpu`  : outil de recherche de similarité efficace, utilisé pour créer et interroger des index vectoriels..
- `pandas`  : bibliothèque pour la manipulation et l’analyse de données.
- `sentence-transformers`  : génère des embeddings pour la recherche sémantique.
- `langchain-ibm`  : permet d’intégrer IBM WatsonxLLM (dans ce tutoriel, le modèle utilisé est granite-3-8b-instruct) à LangChain.

Cette étape prépare votre environnement pour les tâches à venir.

### Étape 4. Importer les bibliothèques requises

Maintenant que nous avons installé les bibliothèques nécessaires, importons les modules requis pour ce tutoriel :

```python
import os
from langchain_ibm import WatsonxLLM
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pandas as pd
import getpass
```

Dans la cellule de code précédente,

- `os`  : permet d’interagir avec le système d’exploitation (par exemple, accéder aux variables d’environnement).
- `langchain_ibm.WatsonxLLM`  : permet d’utiliser le modèle LLM Granite d’IBM de façon fluide dans le cadre LangChain.
- `langchain.embeddings.HuggingFaceEmbeddings`  : génère des embeddings à partir de modèles HuggingFace, essentiels pour la recherche sémantique.
- `langchain.vectorstores.FAISS`  : bibliothèque pour un stockage des vecteurs et une recherche de similarité efficaces, utilisée pour construire et interroger un index vectoriel.
- `RecursiveCharacterTextSplitter`  : divise de grands blocs de texte en segments plus petits, ce qui est crucial pour traiter efficacement les documents.
- `pandas`  : bibliothèque puissante pour l’analyse et la manipulation de données (tabulaires dans le cas présent).
- `getpass`  : permet de capturer des informations sensibles (comme des clés API) de manière sécurisée, sans les afficher à l’écran.

Cette étape configure tous les outils et modules nécessaires pour traiter le texte, créer des embeddings, les stocker dans une base de données vectorielle et interagir avec WatsonxLLM d’IBM.

### Étape 5. Configurer les identifiants

Ce code configure les identifiants nécessaires pour accéder à l’API IBM Watson Machine Learning (WML) et garantit la configuration correcte de l’ID du projet.

- Un dictionnaire nommé`informations d’identification` est créé avec les entrées`WML service URL` et`Clé api` . La clé API est collectée en toute sécurité à l’aide de 'getpass.getpass' pour éviter d’exposer des informations sensibles.
- Le code essaie de récupérer le `PROJECT_ID`  depuis les variables d’environnement via `os.environ` . Si la variable `PROJECT_ID`  n’est pas trouvée, l’utilisateur est invité à la saisir manuellement via input.

```json
# Set up credentials
credentials = {
"url": "https://us-south.ml.cloud.ibm.com",  # Replace with the correct region if needed
"apikey": getpass.getpass("Please enter your WML API key (hit enter): ")
}
# Set up project_id
try:
project_id = os.environ["PROJECT_ID"]
except KeyError:
project_id = input("Please enter your project_id (hit enter): ")
```

### Étape 6. Initialiser le grand modèle de langage

Ce code initialise IBM WatsonxLLM pour une utilisation dans l’application :

1.  Ce code crée une instance de `WatsonxLLM` en utilisant le modèle`ibm/granite-3-8b-instruct,` conçu pour des tâches génératives basées sur des instructions.
2.  Les`url` ,`clé api` et `project_id` des identifiants précédemment configurés sont utilisées pour l’authentification et la connexion au service IBM WatsonxLLM.
3.  Le paramètre`max_new_tokens` est configuré pour limiter le nombre de tokens générés par le modèle à chaque réponse (ici, 150 tokens).

Cette étape prépare WatsonxLLM à générer des réponses dans le cadre du workflow.

```json
# Initialize the IBM Granite LLM
llm = WatsonxLLM(
model_id="ibm/granite-3-8b-instruct",
url=credentials["url"],
apikey=credentials["apikey"],
project_id=project_id,
params={
"max_new_tokens": 150
}
)
```

### Étape 7. Définir une fonction pour extraire le texte d’un fichier

Pour traiter le texte d’un document, nous avons besoin d’une fonction capable de lire et d’extraire son contenu. La fonction suivante est conçue pour gérer les fichiers en texte brut :

```python
def extract_text_from_txt(file_path):
"""Extracts text from a plain text file."""
with open(file_path, "r", encoding="utf-8") as file:
text = file.read()
return text
```

Cette fonction,`extract_text_from_text` , est conçue pour lire et extraire le contenu d’un fichier en texte brut. Elle prend en argument le chemin du fichier et l’ouvre en mode lecture avec un`encodage UTF-8` , pour garantir la gestion correcte des caractères spéciaux.

L’ensemble du contenu du fichier est lu dans une variable nommée`texte` , puis il est renvoyé. Elle joue un rôle clé dans la préparation des données d’entrée, en extrayant le texte brut du document, le préparant ainsi pour les opérations suivantes : découpage, vectorisation et interrogation. C’est une méthode simple et efficace pour traiter les données textuelles issues de n’importe quel fichier en texte brut.

Dans notre cas, elle permet de traiter le fichier d’entrée *(The Adventures of Sherlock Holmes)* pour en extraire le contenu à plusieurs fins : comme le découpage et la vectorisation du texte. Elle garantit que le texte brut est disponible pour l’analyse.

### Étape 8. Diviser le texte en segments

Pour traiter et indexer efficacement de grands blocs de texte, il faut les diviser en segments plus petits et plus faciles à gérer. La fonction suivante accomplit cette tâche :

```python
def split_text_into_chunks(text, chunk_size=500, chunk_overlap=50):
"""Splits text into smaller chunks for indexing."""
splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
return splitter.split_text(text)
```

Les`split_text_into_chunks` est conçue pour diviser de grands blocs de texte en segments plus petits, afin d’en faciliter le traitement et l’indexation. Elle prend en entrée le texte brut, ainsi que deux paramètres optionnels :`chunk_size` , qui définit la taille maximale de chaque segment *(500 caractères par défaut)*, et`chunk_overlap` , qui spécifie le nombre de caractères en chevauchement entre chaque segment *(50 par défaut)*.

Cette approche garantit une continuité contextuelle entre les segments. La fonction utilise`RecursiveCharacterTextSplitter` de`LangChain` , qui divise intelligemment le texte tout en préservant son contexte. Elle renvoie une liste de segments textuels, préparant ainsi les données pour les prochaines étapes : vectorisation et indexation.

Ce découpage est essentiel lors du traitement de grands documents, car les modèles de langage ont des limitations de tokens et ne peuvent pas analyser de longs textes d’un seul coup.

### Étape 9. Créer un index vectoriel

Pour permettre une recherche sémantique efficace, il faut convertir les segments textuels en embeddings vectoriels et les stocker dans un index interrogeable. Cette étape utilise les embeddings FAISS et HuggingFace pour créer l’index vectoriel, qui servira de base pour récupérer des informations pertinentes lors des requêtes.

```python
def create_vector_index(chunks):
"""Creates a FAISS vector index from text chunks."""
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.from_texts(chunks, embeddings)
return vector_store
```

Les`create_vector_index` crée un`vecteur FAISS` à partir des segments de texte générés à l’étape précédente. Cette fonction est essentielle pour permettre la recherche sémantique, en mappant chaque segment dans un espace vectoriel de haute dimension à l’aide d’embeddings.

Elle commence par initialiser un *modèle HuggingFaceEmbeddings* `sentence-transformers/all-MiniLM-L6-v2` , qui génère des embeddings vectoriels pour les segments de texte. Ces embeddings capturent la signification sémantique de chaque segment.

Ensuite, la fonction utilise`FAISS` pour créer une base de données vectorielle en indexant ces embeddings, ce qui permettra une recherche de similarité efficace par la suite.

La base de données vectorielle résultante est renvoyée et servira à retrouver les segments pertinents à partir des requêtes utilisateurs, formant ainsi l’épine dorsale du processus de recherche et de récupération de l’agent.

### Étape 10. Interroger l’index vectoriel avec Granite

Cette étape implique l’interrogation de l’index vectoriel pour récupérer les informations pertinentes, puis l’utilisation du LLM IBM Granite IBM pour générer une réponse affinée. En intégrant la recherche de similarité et le raisonnement via LLM, cette fonction permet un processus de résolution de requête dynamique et intelligent.

```python
def query_index_with_granite_dynamic(vector_store, query, llm):
"""Searches the vector index, uses Granite to refine the response, and returns all components."""
# Perform similarity search
print("\n> Entering new AgentExecutor chain...")
thought = f"The query '{query}' requires context from the book to provide an accurate response."
print(f" Thought: {thought}")
action = "Search FAISS Vector Store"
print(f" Action: {action}")
action_input = query
print(f" Action Input: \"{action_input}\"")
# Retrieve context
results = vector_store.similarity_search(query, k=3)
observation = "\n".join([result.page_content for result in results])
print(f" Observation:\n{observation}\n")
# Generate response with Granite
prompt = f"Context:\n{observation}\n\nQuestion: {query}\nAnswer:"
print(f" Thought: Combining retrieved context with the query to generate a detailed answer.")
final_answer = llm(prompt)
print(f" Final Answer: {final_answer.strip()}")
print("\n> Finished chain.")
# Return all components as a dictionary
return {
"Thought": thought,
"Action": action,
"Action Input": action_input,
"Observation": observation,
"Final Answer": final_answer.strip()
}
```

Les`query_index_with_granite_dynamic` prend trois arguments en entrée : d’abord, la base de données vectorielle (`vector_store` ), ensuite, la requête de l’utilisateur (`query` ) enfin, l’instance du LLM Granite (`LLM` ).

Elle commence par effectuer une recherche de similarité dans l’index vectoriel afin de récupérer les segments de texte les plus pertinents. Ces segments, appelés`observation` , sont combinés en un bloc de contexte unique.

La fonction construit ensuite un prompt en combinant la requête de l’utilisateur et le contexte extrait. Ce prompt est transmis au`LLM Granite` , qui génère une réponse détaillée et contextuellement précise (`final_answer` ).

Tout au long du processus, des étapes intermédiaires, comme la pensée de l’agent, l’action, et l’entrée de l’action (`thought` ,`action` et `action input` ) sont affichées par souci de transparence.

Enfin, la fonction renvoie un dictionnaire contenant tous les composants : le raisonnement, l’action effectuée, l’observation extraite et la réponse finale.

Cette étape est cruciale pour transformer une simple récupération de données brutes en informations exploitables et pertinentes, grâce aux capacités de raisonnement du LLM.

### Étape 11. Générer un « DataFrame » pour les résultats des requêtes

Cette étape permet de traiter dynamiquement plusieurs requêtes, de récupérer les informations pertinentes et de sauvegarder les résultats dans un format structuré pour analyse. La fonction suivante intègre la requête, la structuration des données et leur exportation.

```python
def dynamic_output_to_dataframe(vector_store, queries, llm, csv_filename="output.csv"):
"""Generates a DataFrame dynamically for multiple queries and saves it as a CSV file."""
# List to store all query outputs
output_data = []
# Process each query
for query in queries:
# Capture the output dynamically
output = query_index_with_granite_dynamic(vector_store, query, llm)
output_data.append(output)
# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(output_data)
# Display the DataFrame
print("\nFinal DataFrame:")
print(df)
# Save the DataFrame as a CSV file
df.to_csv(csv_filename, index=False)
print(f"\nOutput saved to {csv_filename}")
```

Les`dynamic_output_to_dataframe`  accepte quatre entrées : la base de données vectorielle (`vector_store` ), une liste de requêtes (`queries` ), l’instance du LLM Granite (`LLM` ) et un nom de fichier CSV facultatif (`csv_filename` , par défaut`output.csv` ).

Pour chaque requête, elle utilise la fonction`query_index_with_granite_dynamic`  pour récupérer le contexte pertinent et générer une réponse à l’aide du LLM. Les résultats, y compris les composants intermédiaires comme la pensée, l’observation et la réponse finale (`Thought` ,`Observation` et `Final Answer` ) sont stockés dans une liste.

Une fois toutes les requêtes traitées, la liste est convertie en un DataFrame pandas. Ce format tabulaire facilite l’analyse et la visualisation des résultats de la requête. Le DataFrame est affiché pour vérification, puis enregistré en tant que fichier CSV pour une utilisation ultérieure.

Cette étape est essentielle pour organiser les sorties de manière lisible, et permettre des tâches en aval comme l’évaluation de la précision ou la visualisation.

### Étape 12. Exécuter le workflow principal

Cette étape combine toutes les étapes précédentes en un workflow unique : traitement d’un fichier texte, réponse à des requêtes, et enregistrement des résultats dans un format structuré. La fonction`main_workflow function` sert d’orchestrateur central pour l’ensemble du tutoriel.

```python
def main_workflow():
# Replace with your text file
file_path = "aosh.txt"
# Extract text from the text file
text = extract_text_from_txt(file_path)
# Split the text into chunks
chunks = split_text_into_chunks(text)
# Create a vector index
vector_store = create_vector_index(chunks)
# Define queries
queries = [
"What is the plot of 'A Scandal in Bohemia'?",
"Who is Dr. Watson, and what role does he play in the stories?",
"Describe the relationship between Sherlock Holmes and Irene Adler.",
"What methods does Sherlock Holmes use to solve cases?"
]
# Generate and save output dynamically
dynamic_output_to_dataframe(vector_store, queries, llm)
```

Déroulé du workflow :

**Fichier d’entrée :** la variable`file_path` spécifie le fichier texte à traiter. Dans ce tutoriel, le fichier d’entrée est`"aosh.txt"` , qui contient le texte The Adventures of Sherlock Holmes.

**Extraction du texte : la fonction**`extract_text_from_text` est appelée pour lire et extraire le contenu du fichier texte d’entrée.

**Découpage du texte** : le texte extrait est divisé en segments avec la fonction`split_text_into_chunks` pour permettre la vectorisation et l’indexation.

**Création d’un index vectoriel :** les segments sont transformés en embeddings et stockés dans un index`vecteur FAISS` via`create_vector_index` commerciales.

**Définition des requêtes :** une liste de requêtes est fournie, chacune visant à extraire une information spécifique du texte. L’agent répondra à ces requêtes.

**Traitement des requêtes :** la fonction`dynamic_output_to_dataframe`  traite les requêtes via l’index vectoriel et le LLM IBM Granite. Elle récupère le contexte pertinent, génère les réponses et sauvegarde les résultats dans un fichier CSV pour analyse.

Cette étape intègre tous les composants du tutoriel dans un workflow cohérent. Elle automatise le processus, de l’extraction de texte à la résolution des requêtes, vous permettant de tester les capacités de l’agent et d’examiner les résultats dans un format structuré.

Pour exécuter le workflow, il suffit d’appeler la fonction`main_workflow()`  et l’ensemble du pipeline s’exécutera de façon fluide.

```
# Run the workflow
main_workflow()
```

------------------------------------------------------------------------

Sortie

------------------------------------------------------------------------

 

```
> Entering new AgentExecutor chain...
 Thought: The query 'What is the plot of 'A Scandal in Bohemia'?' requires context from the book to provide an accurate response.
 Action: Search FAISS Vector Store
 Action Input: "What is the plot of 'A Scandal in Bohemia'?"
 Observation:
I. A SCANDAL IN BOHEMIA

I.
“I was aware of it,” said Holmes dryly.

“The circumstances are of great delicacy, and every precaution has to
be taken to quench what might grow to be an immense scandal and
seriously compromise one of the reigning families of Europe. To speak
plainly, the matter implicates the great House of Ormstein, hereditary
kings of Bohemia.”

“I was also aware of that,” murmured Holmes, settling himself down in
his armchair and closing his eyes.
Contents

   I.     A Scandal in Bohemia
   II.    The Red-Headed League
   III.   A Case of Identity
   IV.    The Boscombe Valley Mystery
   V.     The Five Orange Pips
   VI.    The Man with the Twisted Lip
   VII.   The Adventure of the Blue Carbuncle
   VIII.  The Adventure of the Speckled Band
   IX.    The Adventure of the Engineer’s Thumb
   X.     The Adventure of the Noble Bachelor
   XI.    The Adventure of the Beryl Coronet
   XII.   The Adventure of the Copper Beeches

 Thought: Combining retrieved context with the query to generate a detailed answer.
/var/folders/4w/smh16qdx6l98q0534hr9v52r0000gn/T/ipykernel_2648/234523588.py:23: LangChainDeprecationWarning: The method `BaseLLM.__call__` was deprecated in langchain-core 0.1.7 and will be removed in 1.0. Use :meth:`~invoke` instead.
  final_answer = llm(prompt)
 Final Answer: Step 1: Identify the main characters and their roles.
- Sherlock Holmes: The detective who is approached by a client with a delicate matter.
- An unnamed client: A representative of the great House of Ormstein, hereditary kings of Bohemia, who seeks Holmes' help to prevent a potential scandal.

Step 2: Understand the main issue or conflict.
- The main issue is a delicate matter that, if exposed, could lead to a massive scandal and compromise one of the reigning families of Europe, specifically the House of Ormstein.

Step 3: Ident

> Finished chain.

> Entering new AgentExecutor chain...
 Thought: The query 'Who is Dr. Watson, and what role does he play in the stories?' requires context from the book to provide an accurate response.
 Action: Search FAISS Vector Store
 Action Input: "Who is Dr. Watson, and what role does he play in the stories?"
 Observation:
“Sarasate plays at the St. James’s Hall this afternoon,” he remarked.
“What do you think, Watson? Could your patients spare you for a few
hours?”

“I have nothing to do to-day. My practice is never very absorbing.”
“Try the settee,” said Holmes, relapsing into his armchair and putting
his fingertips together, as was his custom when in judicial moods. “I
know, my dear Watson, that you share my love of all that is bizarre and
outside the conventions and humdrum routine of everyday life. You have
shown your relish for it by the enthusiasm which has prompted you to
chronicle, and, if you will excuse my saying so, somewhat to embellish
so many of my own little adventures.”
“My God! It’s Watson,” said he. He was in a pitiable state of reaction,
with every nerve in a twitter. “I say, Watson, what o’clock is it?”

“Nearly eleven.”

“Of what day?”

“Of Friday, June 19th.”

“Good heavens! I thought it was Wednesday. It is Wednesday. What d’you
want to frighten a chap for?” He sank his face onto his arms and began
to sob in a high treble key.

“I tell you that it is Friday, man. Your wife has been waiting this two
days for you. You should be ashamed of yourself!”

 Thought: Combining retrieved context with the query to generate a detailed answer.
 Final Answer: Dr. Watson is a character in the Sherlock Holmes stories, written by Sir Arthur Conan Doyle. He is a former military surgeon who becomes the narrator and chronicler of Holmes' adventures. Watson is a close friend and confidant of Holmes, often accompanying him on cases and providing a more human perspective to the stories. He is known for his enthusiasm for the bizarre and unconventional, as well as his skill in recording the details of their investigations. Watson's role is crucial in presenting the narrative and offering insights into Holmes' character and methods.

> Finished chain.

Final DataFrame:
                                             Thought  \
0  The query 'What is the plot of 'A Scandal in B...   
1  The query 'Who is Dr. Watson, and what role do...   
2  The query 'Describe the relationship between S...   
3  The query 'What methods does Sherlock Holmes u...   

                      Action  \
0  Search FAISS Vector Store   
1  Search FAISS Vector Store   
2  Search FAISS Vector Store   
3  Search FAISS Vector Store   

                                        Action Input  \
0        What is the plot of 'A Scandal in Bohemia'?   
1  Who is Dr. Watson, and what role does he play ...   
2  Describe the relationship between Sherlock Hol...   
3  What methods does Sherlock Holmes use to solve...   

                                         Observation  \
0  I. A SCANDAL IN BOHEMIA\n\n\nI.\n“I was aware ...   
1  “Sarasate plays at the St. James’s Hall this a...   
2  “You have really got it!” he cried, grasping S...   
3  to learn of the case was told me by Sherlock H...   

                                        Final Answer  
0  Step 1: Identify the main characters and their...  
1  Dr. Watson is a character in the Sherlock Holm...  
2  Sherlock Holmes and Irene Adler have a profess...  
3  Sherlock Holmes uses a variety of methods to s...  

Output saved to output.csv
```

 

Après avoir exécuté la fonction`main_workflow()` , nous avons traité un fichier texte (aosh.text) et exécuté quatre requêtes définies par l’utilisateur sur The Adventures of Sherlock Holmes. Le résultat fournit une vue détaillée de la manière dont chaque requête a été traitée :

- **Thought** : décrit le raisonnement associé à la requête et le contexte nécessaire pour y répondre avec précision.
- **Action** : indique l’étape exécutée, ici une recherche de similarité dans l’index vectoriel FAISS.
- **Action input** : représente la requête utilisateur traitée à cette itération.
- **Observation** : contient les segments de texte extraits de l’index et jugés pertinents pour la requête.
- **Final answer** : réponse générée par le modèle LLM IBM Granite, à partir du contexte récupéré.

Les résultats ont également été structurés sous forme de DataFrame et enregistrés dans un fichier`output.csv` . Ce fichier contient tous les composants ci-dessus pour une future analyse ou diffusion.

Ici, nous combinons récupération textuelle et raisonnement via LLM pour répondre à des questions complexes sur le contenu du livre. L’agent extrait dynamiquement les passages pertinents, génère des réponses précises en les contextualisant, et structure les résultats dans un format facilitant l’analyse.

## Visualiser les résultats

Maintenant que le fichier output.csv a été généré, nous allons visualiser les résultats des requêtes ainsi que certains indicateurs de précision, afin d’obtenir des informations plus approfondies sur les performances de l’agent.

Dans la cellule de code suivante, nous chargeons les résultats de requêtes enregistrés dans le fichier`output.csv` dans un DataFrame pandas pour les préparer à la visualisation et à l’analyse. Le DataFrame nous permet de manipuler et d’explorer les données dans un format structuré.

```python
# Load the output.csv file into a DataFrame
df = pd.read_csv("output.csv")
print(df.head()) # Display the first few rows
```

------------------------------------------------------------------------

SORTIE

------------------------------------------------------------------------

```
Thought  \
0  The query 'What is the plot of 'A Scandal in B...   
1  The query 'Who is Dr. Watson, and what role do...   
2  The query 'Describe the relationship between S...   
3  The query 'What methods does Sherlock Holmes u...   

                      Action  \
0  Search FAISS Vector Store   
1  Search FAISS Vector Store   
2  Search FAISS Vector Store   
3  Search FAISS Vector Store   

                                        Action Input  \
0        What is the plot of 'A Scandal in Bohemia'?   
1  Who is Dr. Watson, and what role does he play ...   
2  Describe the relationship between Sherlock Hol...   
3  What methods does Sherlock Holmes use to solve...   

                                         Observation  \
0  I. A SCANDAL IN BOHEMIA\n\n\nI.\n“I was aware ...   
1  “Sarasate plays at the St. James’s Hall this a...   
2  “You have really got it!” he cried, grasping S...   
3  to learn of the case was told me by Sherlock H...   

                                        Final Answer  
0  Step 1: Identify the main characters and their...  
1  Dr. Watson is a character in the Sherlock Holm...  
2  Sherlock Holmes and Irene Adler have a profess...  
3  Sherlock Holmes uses a variety of methods to s...
```

Dans ce code, le DataFrame inclut les composants clés`Thought` ,`Action` ,`Observation` et `Final Answer`  pour chaque requête. En affichant les premières lignes via`df.head()` , nous vérifions que les données sont correctement formatées et prêtes pour l’étape suivante : la création de visualisations pertinentes.

### Importer des bibliothèques de visualisation

Pour créer des visualisations des résultats des requêtes, nous importons les bibliothèques nécessaires :

```python
import matplotlib.pyplot as plt
from wordcloud import WordCloud
```

 

`matplotlib.pyplot`  : bibliothèque très utilisée pour créer des visualisations statiques, interactives ou animées (Python). Elle servira ici à générer des diagrammes en barres, des graphiques circulaires et d’autres visualisations.

`wordcloud`  : bibliothèque qui permet de créer des nuages de mots, qui mettent visuellement en avant les mots qui apparaissent le plus fréquemment dans les données. Cette étape permet de résumer et d’explorer le contexte récupéré à partir du texte.

*Remarque importante : si vous rencontrez l’erreur`"WordCloud not found"` , vous pouvez la résoudre en installant la bibliothèque à l’aide de la commande`pip install wordcloud` .*

### Visualiser la longueur des observations et des réponses

Ce code crée un diagramme à barres horizontales qui compare la longueur des **observations (contexte récupéré)** et **des réponses (réponses générées)** pour chaque requête. Cette visualisation fournit des informations sur la quantité de contexte utilisée par l’agent par rapport à la longueur des réponses générées.

```python
def visualize_lengths_with_queries(df):
"""Visualizes the lengths of observations and answers with queries on the y-axis."""
df["Observation Length"] = df["Observation"].apply(len)
df["Answer Length"] = df["Final Answer"].apply(len)
# Extract relevant data
queries = df["Action Input"]
observation_lengths = df["Observation Length"]
answer_lengths = df["Answer Length"]
# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
bar_width = 0.4
y_pos = range(len(queries))
plt.barh(y_pos, observation_lengths, bar_width, label="Observation Length", color="skyblue", edgecolor="black")
plt.barh([y + bar_width for y in y_pos], answer_lengths, bar_width, label="Answer Length", color="lightgreen", edgecolor="black")
plt.yticks([y + bar_width / 2 for y in y_pos], queries, fontsize=10)
plt.xlabel("Length (characters)", fontsize=14)
plt.ylabel("Queries", fontsize=14)
plt.title("Observation and Answer Lengths by Query", fontsize=16)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
```

```
# Call the visualization function
visualize_lengths_with_queries(df)
```

Cette fonction,`visualize_lengths_with_queries` , crée un diagramme à barres horizontales qui compare la longueur des **observations (contexte récupéré)** et **des réponses (réponses générées)** pour chaque requête.

La longueur des observations et des réponses sont mesurées en nombre de caractères, et ajoutées sous forme de nouvelles colonnes (`Observation Length` et `Answer Length` ) dans le DataFrame. Avec`matplotlib` , ces longueurs sont ensuite tracées pour chaque requête, les requêtes étant affichées sur l’axe y pour une meilleure lisibilité.

Le code couleur du diagramme à barres permet de différencier la longueur des observations et celle des réponses, et il est associé à des étiquettes, une légende et un titre pour plus de clarté.

Cette visualisation permet d’analyser l’équilibre entre la taille du contexte récupéré et les détails de la réponse générée, offrant ainsi des informations sur la façon dont l’agent traite les requêtes et y répond.

### Visualiser la proportion de texte utilisée dans les observations

Cette étape permet de visualiser la proportion du texte total traité par l’agent qui est utilisée dans les observations (contexte récupéré) par rapport au texte restant. Un graphique circulaire est créé pour fournir une représentation intuitive de cette proportion.

```python
def visualize_text_proportion(df):
"""Visualizes the proportion of text used in observations."""
total_text_length = sum(df["Observation"].apply(len)) + sum(df["Final Answer"].apply(len))
observation_text_length = sum(df["Observation"].apply(len))
sizes = [observation_text_length, total_text_length - observation_text_length]
labels = ["Observation Text", "Remaining Text"]
colors = ["#66b3ff", "#99ff99"]
plt.figure(figsize=(4, 4))
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
plt.title("Proportion of Text Used in Observations", fontsize=16)
plt.show()
```

```
# Call the visualization function
visualize_text_proportion(df)
```

Les`visualize_text_proportion`  crée un graphique circulaire pour illustrer la proportion du texte total utilisée dans les observations (contexte récupéré) par rapport au texte restant. Elle calcule la longueur totale du texte en additionnant les longueurs de caractère de toutes les observations et réponses, puis détermine la proportion fournie par les observations seules.

Ces données sont visualisées dans un graphique circulaire, avec des étiquettes claires indiquant le texte d’observation et le texte restant (`"Observation Text"` et`"Remaining Text"` et différentes couleurs pour améliorer la lisibilité. Le diagramme affiche des valeurs en pourcentage pour faciliter l’interprétation des proportions.

Cette visualisation fournit une vue d’ensemble de haut niveau de la quantité de texte que l’agent utilise comme contexte pendant le traitement des requêtes, offrant ainsi des informations sur l’efficacité et la pertinence du processus de récupération.

### Générer des nuages de mots pour les observations et les réponses finales

Ce code génère deux nuages de mots pour représenter visuellement les mots les plus fréquents dans le texte des parties `Observation` et`Final Answer` .

```python
def generate_wordclouds_side_by_side(df):
"""Generates and displays word clouds for Observations and Final Answers side by side."""
# Combine text for Observations and Final Answers
observation_text = " ".join(df["Observation"])
final_answer_text = " ".join(df["Final Answer"])
# Create word clouds
observation_wordcloud = WordCloud(width=800, height=400, background_color="white").generate(observation_text)
final_answer_wordcloud = WordCloud(width=800, height=400, background_color="white").generate(final_answer_text)
# Create a side-by-side visualization
plt.figure(figsize=(16, 8))
# Plot the Observation word cloud
plt.subplot(1, 2, 1)
plt.imshow(observation_wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Observations", fontsize=16)
# Plot the Final Answer word cloud
plt.subplot(1, 2, 2)
plt.imshow(final_answer_wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Final Answers", fontsize=16)
plt.tight_layout()
plt.show()
```

```
# Call the function to generate and display the word clouds
generate_wordclouds_side_by_side(df)
```

Ce code génère deux nuages de mots pour représenter visuellement les mots les plus fréquents dans le texte des parties`Observation` et`Final Answer` . Il les affiche côte à côte pour faciliter la comparaison. Le texte des parties`Observation` et `Final Answer`  est d’abord concaténé dans deux chaînes distinctes via`" ".join()`  pour combiner toutes les lignes des colonnes respectives. La bibliothèque`WordCloud` est ensuite utilisée pour générer des nuages de mots pour chaque texte avec des configurations spécifiques.

Pour créer une visualisation côte à côte, on utilise des sous-graphiques : le premier affiche le nuage de mots pour la partie`Observation` , et le second affiche celui pour la partie`Final Answer` . La fonction`tight_layout()`  permet d'assurer un espacement soigné entre les graphiques. Ces nuages de mots nous permettent d’analyser intuitivement les performances de l’agent en mettant en évidence les termes clés extraits du contexte (`Observation` ) et ceux qui sont mis en avant dans les réponses (`Final Answer` ).

## Tester la précision de l’agent

Dans cette section, nous évaluons les performances de l’agent à l’aide de plusieurs indicateurs de précision (correspondance de mots-clés, scores BLEU, précision/rappel et scores F1) :`Keyword Matching` ,`BLEU Scores` ,`Precision/Recall` et `F1 Scores` . Ces indicateurs fournissent une vue d’ensemble complète de la capacité de l’agent à générer des réponses précises et pertinentes à partir des requêtes utilisateur.

### Importer les bibliothèques requises

Avant de lancer les tests, nous devons importer les bibliothèques nécessaires à l’évaluation :

```python
from sklearn.feature_extraction.text import CountVectorizer
from nltk.translate.bleu_score import sentence_bleu
from sklearn.metrics import precision_score, recall_score
```

Ces bibliothèques fournissent des outils pour la correspondance de mots-clés, le calcul des scores BLEU et l’évaluation de la précision et du rappel. Assurez-vous d’avoir installé ces bibliothèques dans votre environnement pour éviter toute erreur d’importation.

### Précision de la correspondance de mots-clés

Ce test évalue dans quelle mesure les réponses générées incluent les mots-clés présents dans les requêtes. Il utilise`CountVectorizer` pour tokeniser et extraire les mots-clés des requêtes et des réponses. La fonction calcule la proportion de mots-clés de la requête présents dans la réponse générée, et marque la réponse comme précise si cette proportion dépasse un seuil (par défaut : 0,5). Les résultats sont ajoutés au DataFrame dans les colonnes`Keyword Match Score` et`Is Accurate` .

```python
def keyword_matching_accuracy(df):
"""Checks if key phrases from the query are present in the final answer."""
vectorizer = CountVectorizer(stop_words='english')
def check_keywords(query, answer):
query_keywords = set(vectorizer.build_tokenizer()(query.lower()))
answer_keywords = set(vectorizer.build_tokenizer()(answer.lower()))
common_keywords = query_keywords & answer_keywords
return len(common_keywords) / len(query_keywords)  # Proportion of matched keywords
df["Keyword Match Score"] = df.apply(lambda row: check_keywords(row["Action Input"], row["Final Answer"]), axis=1)
df["Is Accurate"] = df["Keyword Match Score"] >= 0.5  # Set a threshold for accuracy
return df
```

```
# Apply keyword matching
df = keyword_matching_accuracy(df)
df.to_csv("output_with_accuracy.csv", index=False)
df
```

### Calcul des scores BLEU

Ce test évalue *dans quelle mesure les réponses générées correspondent aux observations extraites.*.`BLEU (Bilingual Evaluation Understudy)` est un indicateur populaire permettant d’évaluer la similarité textuelle sur la base des chevauchements`n-gram` . La fonction calcule les`BLEU Scores`  pour chaque paire requête-réponse et les ajoute au DataFrame sous la colonne BLEU Score.

```python
def calculate_bleu_scores(df):
"""Calculates BLEU scores for answers against observations."""
df["BLEU Score"] = df.apply(
lambda row: sentence_bleu([row["Observation"].split()], row["Final Answer"].split()),
axis=1
)
return df
```

```
# Apply BLEU score calculation
df = calculate_bleu_scores(df)
df.to_csv("output_with_bleu.csv", index=False)
```

### Précision et rappel

La précision et le rappel sont calculés pour évaluer la pertinence et l’exhaustivité des réponses. La précision mesure la proportion de mots pertinents retrouvés dans la réponse, tandis que le rappel mesure la proportion de mots pertinents dans l’observation qui apparaissent dans la réponse.

Ces indicateurs sont ajoutés au DataFrame dans les colonnes `Precision` et `Rappel` .

```python
def calculate_precision_recall(df):
"""Calculates precision and recall for extractive answers."""
def precision_recall(observation, answer):
observation_set = set(observation.lower().split())
answer_set = set(answer.lower().split())
precision = len(observation_set & answer_set) / len(answer_set) if answer_set else 0
recall = len(observation_set & answer_set) / len(observation_set) if observation_set else 0
return precision, recall
df[["Precision", "Recall"]] = df.apply(
lambda row: pd.Series(precision_recall(row["Observation"], row["Final Answer"])),
axis=1
)
return df
```

```
# Apply precision/recall
df = calculate_precision_recall(df)
df.to_csv("output_with_precision_recall.csv", index=False)
df
```

### Calcul du score F1

Le score F1 regroupe la précision et le rappel dans un indicateur unique, fournissant une évaluation équilibrée de la pertinence et de l’exhaustivité de la réponse. La formule du score F1 est la suivante : 

```
F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
```

Les`F1 Scores` calculés sont ajoutés au DataFrame dans la colonne F1 Score.

```python
def calculate_f1(df):
"""Calculates F1 scores based on precision and recall."""
df["F1 Score"] = 2 * (df["Precision"] * df["Recall"]) / (df["Precision"] + df["Recall"])
df["F1 Score"].fillna(0, inplace=True)  # Handle divide by zero
return df
```

```
# Apply F1 calculation
df = calculate_f1(df)
df.to_csv("output_with_f1.csv", index=False)
df
```

### Faire la synthèse des indicateurs de précision

Enfin, une fonction de synthèse consolide tous les indicateurs afin de fournir un aperçu global des performances de l’agent. Elle calcule le nombre total de requêtes, le nombre et le pourcentage de réponses précises et les scores moyens BLEU et F1.

```python
def summarize_accuracy_metrics(df):
"""Summarizes overall accuracy metrics."""
total_entries = len(df)
accurate_entries = df["Is Accurate"].sum()
average_bleu = df["BLEU Score"].mean()
average_f1 = df["F1 Score"].mean()
print(f"Total Entries: {total_entries}")
print(f"Accurate Entries: {accurate_entries} ({accurate_entries / total_entries * 100:.2f}%)")
print(f"Average BLEU Score: {average_bleu:.2f}")
print(f"Average F1 Score: {average_f1:.2f}")
```

```
# Call summary function
summarize_accuracy_metrics(df)
```

------------------------------------------------------------------------

SORTIE

------------------------------------------------------------------------

 

```
Total Entries: 4
Accurate Entries: 4 (100.00%)
Average BLEU Score: 0.04
Average F1 Score: 0.24
```

Ces tests de précision offrent une évaluation détaillée de la capacité de l’agent à générer des réponses pertinentes et précises. Chaque test se concentre sur un aspect spécifique : inclusion des mots-clés, similarité textuelle, exhaustivité des réponses. Le résumé consolide ces indicateurs pour fournir un aperçu global des performances.

## Synthèse

Ce tutoriel vous a guidé à travers la création d’un agent autonome reposant sur le LLM IBM Granite et LangChain. Depuis l’extraction de texte jusqu’à la vectorisation et la résolution des requêtes, nous avons couvert l’ensemble du processus de conception et de mise en œuvre d’un agent fonctionnel basé sur un LLM. Les étapes clés incluent la gestion de la mémoire via des bases de données vectorielles, le traitement des requêtes et la génération de réponses à l’aide de Granite.

Nous avons évalué les performances de l’agent en utilisant des indicateurs de précision telles que la correspondance de mots-clés, les scores BLEU, la précision, le rappel et les scores F1. Des visualisations telles que des diagrammes à barres, des graphiques circulaires et des nuages de mots ont apporté des informations supplémentaires sur le comportement et l’efficacité de l’agent.

En suivant ce tutoriel, vous avez appris à concevoir, tester et visualiser les performances d’un agent LLM. Cette base peut être étendue à des jeux de données plus complexes, à l’amélioration de la précision et à l’exploration de fonctionnalités avancées telles que les systèmes multi-agents.
