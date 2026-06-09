> Source : https://www.ibm.com/fr-fr/think/tutorials/how-to-build-an-mcp-server

# Comment créer un serveur MCP

Dans ce tutoriel, vous allez créer un serveur [Model Context Protocol](https://www.ibm.com/fr-fr/think/topics/model-context-protocol) (MCP) qui expose un outil unique de recherche de tutoriels IBM. En utilisant le cadre « fastmcp » et la bibliothèque de requêtes, le script télécharge un index JSON de tutoriels à partir d'une URL distante. Il recherche ensuite les correspondances avec la requête d’un utilisateur et renvoie une liste de résultats soigneusement formatée. Vous ajouterez également un traitement des erreurs pour les problèmes de réseau, les mauvais JSON et les problèmes inattendus, ce qui rendra l’outil robuste et adapté aux débutants. Enfin, vous allez exécuter le serveur MCP afin qu’il puisse être connecté et testé avec un client comme Cursor.

## Qu’est-ce que MCP ?

Les grandes entreprises et les start-ups développent toujours plus de solutions alimentées par l’\[intelligence artificielle\] générative (https://www.ibm.com/fr-fr/think/topics/artificial-intelligence) (IA). Pour rendre leurs solutions plus utiles, leurs développeurs ont besoin d’informations et d’un contexte à jour. Les \[modèles\] de machine learning (https://www.ibm.com/fr-fr/think/topics/ai-model) doivent interagir avec des outils, des [interfaces de programmation d’application](https://www.ibm.com/fr-fr/think/topics/api)(API), des [kits de développement logiciel](https://www.ibm.com/fr-fr/think/topics/api-vs-sdk) (SDK) et des systèmes front-end pour y parvenir.

MCP standardise la manière dont le contexte est transmis entre les modèles d’IA et les systèmes. Il simplifie la coordination entre un [grand modèle de langage](https://www.ibm.com/fr-fr/think/topics/large-language-models) (LLM) et les sources de données et outils externes. Une analogie courante consiste à considérer MCP comme un port USB-C pour un LLM. Il rend le LLM beaucoup plus utile, car le modèle a accès à des capacités et à des données qui ne faisaient pas partie de son entraînement. Cette fonctionnalité est particulièrement utile lors de la création d’[agents IA](https://www.ibm.com/fr-fr/think/topics/ai-agents).

MCP a été développé par Anthropic et adopté par les principaux fournisseurs d’IA, notamment OpenAI, Google DeepMind et autres acteurs du secteur. Il offre aux modèles d’IA un moyen sécurisé et normalisé d’accéder aux données, aux ressources externes (telles que les templates de prompts) et aux outils, et de les utiliser.

En outre, les [environnements de développement intégrés](https://www.ibm.com/fr-fr/think/topics/integrated-development-environment) (IDE) tels que Cursor et Visual Studio Code ont également adopté MCP, permettant à leurs assistants IA d’accéder aux serveurs MCP afin de les rendre plus contextuels et plus conviviaux pour les développeurs. Conçu comme un standard ouvert, le MCP est un pont entre le monde stochastique de l’IA générative et le monde déterministe de la plupart des systèmes d’entreprise qui existent aujourd’hui. MCP fournit un LLM avec des informations contextuelles, à l’instar d’autres schémas de conception qui ont commencé à émerger, tels que la [génération augmentée par récupération](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation) (RAG), [l’appel d’outils](https://www.ibm.com/fr-fr/think/topics/tool-calling) et les agents IA.

Voici quelques-uns des atouts qui distinguent MCP des autres solutions :

\- Échelle : les serveurs MCP peuvent être définis et hébergés une seule fois et utilisés par de nombreux systèmes d’IA. Cette capacité limite la nécessité de définir l’accès aux mêmes données sources, ressources et outils d’IA pour plusieurs systèmes d’IA générative.

\- Récupération des données : contrairement à la RAG, où la récupération des données nécessite un prétraitement et une vectorisation avant la requête, MCP est dynamique et permet des fluctuations et des mises à jour à partir de sources d’informations en temps réel.

\- Complexité : MCP est assez simple à configurer et à intégrer dans les applications d’IA, comme nous le montrons ici. Vous pouvez facilement utiliser des fichiers de configuration pour rendre un serveur MCP portable dans tous les environnements.

\- Indépendant des plateformes : outre le fait que vous pouvez créer des serveurs MCP avec Python, TypeScript ou d’autres langages, ils ne sont pas non plus associés à une solution LLM particulière.

\- Débogage via un modèle client/serveur : le client MCP envoie des requêtes au serveur MCP, qui récupère ensuite les données nécessaires à partir de divers systèmes et sources externes, qu’il s’agisse d’API, de bases de données ou de fichiers locaux. Cette approche structurée garantit que le modèle d’IA bénéficie d’un contexte cohérent et pertinent, ce qui permet d’obtenir des sorties plus précises et plus fiables. MCP utilise JSON-RPC pour encoder les messages et prend en charge 2 mécanismes de transport, stdio et HTTP en flux. Dans les itérations précédentes du protocole, il prenait également en charge le protocole HTTP avec des événements envoyés par le serveur (SSE).

Il peut être décourageant de devoir se tenir constamment au courant des dernières informations dont votre entreprise a besoin. Le MCP peut aider à créer du contexte et à incorporer de nouvelles informations pour les contrats au fur et à mesure de leur exécution, d’héritage qui est numérisé, mais pas nécessairement digéré, etc. Ces informations peuvent être à la fois internes et externes, mais l’ajout de contexte permet de contourner le besoin fastidieux de réentraîner un LLM pour être utile.

Il existe de nombreux serveurs MCP distants, ainsi que de nombreuses implémentations de référence sur github.com

## Étapes

Ce guide détaillé est disponible sur notre dépôt GitHub,, avec le script server.py auquel vous ferez référence lors de la création de votre serveur MCP. Dans ce tutoriel, nous allons construire un serveur MCP personnalisé de base, qui peut :

- Se connecter à notre dépôt de tutoriels GitHub
- Effectuer une recherche sur des sujets susceptibles d’intéresser l’utilisateur
- Renvoyer les résultats avec des liens vers le tutoriel

Afin de faciliter la réalisation de ce tutoriel, nous avons créé un mécanisme qui permet au serveur que vous allez créer d’utiliser facilement le contenu de notre tutoriel, sans authentification requise.

### Étape 1. Configurer votre environnement

\- Python 3.11 (ou une version ultérieure) installé sur votre ordinateur (vérifiez en exécutant python3 --version dans votre terminal).

\- Le module venv intégré est disponible (il est fourni avec Python sur la plupart des systèmes ; sur certaines distributions Linux®, vous devrez peut-être l’installer séparément, avec sudo apt install python3-venv).

\- Un terminal de ligne de commande (CLI) :

\- macOS ou Linux : utilisez votre application Terminal (ces environnements sont de type Unix).

\- Windows : utilisez PowerShell ou Command Prompt, dont les légères différences de syntaxe sont expliquées à l’étape suivante.

\- Le logiciel de traitement de texte ou l’IDE de votre choix 

Créer un nouveau répertoire et utiliser la commande cd pour y accéder

  `mkdir ibmtutorialmcpserver`  et `cd ibmtutorialmcpserver`

S'assurer que vous êtes dans le répertoire`ibmtutorialmcpserver` vous pouvez exécuter la commande suivante pour créer un environnement virtuel 

`python3 -m venv venv`\

Remarque : sous Windows, vous pourrez peut-être remplacer`python3`  avec`python`\

Une fois que vous avez créé l’environnement virtuel, vous devez l’activer en utilisant la commande suivante

`source venv/bin/activate`

Une fois activé, votre shell vous indiquera probablement`(venv)` dans l’invite 

Vous devez maintenant installer le paquet Python pour`fastMCP` . Ce cadre open source fournit toutes les fonctionnalités nécessaires pour exécuter un serveur MCP et fait l’objet d’une maintenance active. Nous allons également installer`requests package`  pour effectuer des requêtes HTTP simples \

Installez le`fastMCP` et`requests` paquet avec`pip` en utilisant la commande suivante

`pip install fastmcp requests`\

Une fois cette étape terminée, vous pouvez vérifier si fastMCP est correctement installé en exécutant la commande suivante \

`fastmcp version`\

Si vous obtenez une sortie similaire à celle ci-dessous, vous avez installé fastMCP dans votre environnement virtuel.

```
FastMCP version:                                       2.10.1
MCP version:                                           1.10.1
Python version:                                       3.11.13
Platform:                          macOS-15.5-arm64-arm-64bit
FastMCP root path: /opt/homebrew/lib/python3.11/site-packages
```

Maintenant que vous avez installé fastMCP, créons notre serveur MCP.

### Étape 2. Créer un serveur MCP

Créez un nouveau fichier dans le répertoire et donnez-lui le nom`server.py` .

Une fois que vous avez ce fichier, ouvrez-le et copiez-y l’extrait de code suivant \

```python
# Simple MCP server that exposes a single tool to search IBM tutorials.
# How to run:
# 1) Install dependencies: pip install fastmcp requests
# 2) Start the server using an MCP client with the command: fastmcp run <YOUR PATH>/server.py

from fastmcp import FastMCPimport requests

# Source of the tutorials index 
DOCS_INDEX_URL = "https://raw.githubusercontent.com/IBM/ibmdotcom-tutorials/refs/heads/main/docs_index.json"

mcp = FastMCP("IBM Tutorials")

@mcp.tool
def search_ibmtutorials(query: str) -> str:
"""
Search for tutorials on GitHub by downloading a JSON file from a GitHub repo and searching the payload for any relevant results and the respective details

Args:
query: The search term to look for in tutorial titles and URLs

Returns:
A formatted list of relevant tutorial results
"""
try:
# Download the JSON file from the GitHub repo
response = requests.get(DOCS_INDEX_URL, timeout=10)
response.raise_for_status() # Raise an exception for bad status codes

# Parse the JSON data
tutorials = response.json()

# Search for relevant tutorials (case-insensitive)
query_lower = query.lower()
relevant_tutorials = []

for tutorial in tutorials:
# Search in title and URL
title = tutorial.get('title', '').lower()
url_path = tutorial.get('url', '').lower()

if query_lower in title or query_lower in url_path:
relevant_tutorials.append(tutorial)

# Format and return results
if not relevant_tutorials:
return f"No IBM tutorials found matching '{query}'"

# Format the results
result_lines = [f"Found {len(relevant_tutorials)} tutorial(s) matching '{query}':\n"]

for i, tutorial in enumerate(relevant_tutorials, 1):
title = tutorial.get('title', 'No title')
tutorial_url = tutorial.get('url', 'No URL')
date = tutorial.get('date', 'No date')
author = tutorial.get('author', '')

result_lines.append(f"{i}. **{title}**")
result_lines.append(f" URL: {tutorial_url}")
result_lines.append(f" Date: {date}")
if author:
result_lines.append(f" Author: {author}")
result_lines.append("") # Empty line for spacing

return "\n".join(result_lines)

except requests.exceptions.RequestException as e:
return f"Error fetching tutorials from GitHub: {str(e)}"
except ValueError as e:
return f"Error parsing JSON data: {str(e)}"
except Exception as e:
return f"Error searching IBM tutorials: {str(e)}"

if __name__ == "__main__":
mcp.run()
```

Passons en revue le code précédent et expliquons ce que font les éléments clés. 

### Importations et configuration\

Le script commence par l’importation de FastMCP, qui fournit le cadre pour la création du serveur MCP, ainsi que des requêtes, qui sont utilisées pour télécharger les données via HTTP. Nous avons ajouté une constante`DOCS_INDEX_URL` pour contenir l’URL JSON distante pour l’index des tutoriels. Cette approche permet de modifier plus facilement l’emplacement de la source si vous disposez d’une autre source de données JSON pour laquelle vous souhaitez réutiliser ce tutoriel ultérieurement.

### Configurer le serveur MCP\

Nous créons ensuite une instance de serveur MCP avec`FastMCP(“IBM Tutorials”)` . Cette étape sert de contrôleur central pour tous les outils que le serveur exposera aux clients MCP, tels que`search_ibmtutorials`  , l’outil que nous définissons.

### Définir l’outil MCP \

Les`@mcp.tool`  décorateur marque`search_ibmtutorials`  en tant qu’outil MCP. Cette fonction prend un terme de recherche, télécharge l’index du tutoriel à partir de`DOCS_INDEX_URL`  en utilisant`requests.get()` (avec un délai d’attente de 10 secondes pour la sécurité du réseau) et déclenche une exception si l’état de la réponse HTTP indique une erreur. Une fois les données récupérées, elles sont analysées à partir de JSON vers des objets Python.

La recherche n’est pas sensible à la casse : la requête est convertie en minuscules, et le titre et l’URL de chaque tutoriel sont également réduits pour la mise en correspondance. Si un tutoriel contient le terme de recherche dans le titre ou dans l’URL, il est ajouté à une liste de résultats pertinents.

### Formatage et envoi des résultats

Si aucun tutoriel ne correspond à la recherche, la fonction renvoie un message convivial indiquant que rien n’a été trouvé. S’il y a des correspondances, la fonction crée une liste formatée et numérotée montrant le titre, l’URL, la date, la date et (le cas échéant) l’auteur de chaque tutoriel. Le formatage utilise des caractères gras de type Markdown pour les titres, afin qu’ils se démarquent dans les clients qui le prennent en charge. Le texte formaté final est renvoyé sous la forme d’une chaîne unique.

### Gestion des erreurs\

La fonction comprend une gestion ciblée des exceptions :

`requests.exceptions.RequestException` détecte les problèmes de réseau tels que les délais d’attente et les mauvaises connexions.\

`ValueError`  (qui peuvent être soulevés par .json()) détecte les cas où la réponse n’est pas un JSON valide.

Un`Exception`  gestionnaire général détecte tout autre élément inattendu.

Chaque erreur renvoie un message descriptif à l’appelant au lieu d’arrêter le programme.

### Démarrer le serveur\

En bas,`if name == “main”` : bloc garantissant que`mcp.run()` ne s’exécute que lorsque le script est exécuté directement. Cette étape permet de démarrer le serveur MCP, de façon à rendre`search_ibmtutorials`  l’outil disponible à tout client MCP, tel que MCP Inspector. Cet outil est utile pour résoudre les problèmes et déboguer votre serveur MCP. L’outil fournit une interface utilisateur que vous pouvez utiliser pour déboguer le serveur MCP et la validation du comportement attendu. \

### Étape 3. Ajouter le serveur MCP à votre IDE

Maintenant que vous avez créé votre serveur, vous devez l’activer dans votre IDE afin de pouvoir l’utiliser. Il existe de nombreux clients qui prennent en charge MCP, avec différents niveaux d’intégration au protocole. Le site officiel de MCP fournit une liste exhaustive d’exemples de clients.\
Si Cursor est installé, vous pouvez ajouter le serveur MCP dans Cursor en suivant ces instructions.

Ouvrez les paramètres Cursor et allez dans Outils et intégrations. Sélectionnez Nouveau serveur MCP et collez-le dans le fichier mcp.json. que Cursor ouvre dans un nouvel onglet. Veillez à remplacer \ par le répertoire dans lequel vous vous trouvez. Vous pouvez exécuter pwd dans votre terminal pour obtenir le chemin complet. Pour plus d’informations sur Cursor et MCP, consultez la documentation Cursor.

```json
{
  "mcpServers": {
    "tutorials": {
      "command": "fastmcp",
      "args": ["run <YOUR PATH>/ibmtutorialmcpserver/server.py"],
      "env": {
      }
    }
  }
}
```

Si vous utilisez Microsoft VS Code, vous pouvez ajouter le serveur MCP en suivant les instructions liées ici. Assurez-vous que Copilot est configuré dans VS Code avant de poursuivre.\
Si vous souhaitez activer le serveur MCP à l’aide d’un fichier, créez un fichier .vscode/mcp.json dans le répertoire de ce projet, puis copiez-collez ce code dans le fichier. Veillez à remplacer \ par le répertoire dans lequel vous vous trouvez. Vous pouvez exécuter pwd dans votre terminal pour obtenir le chemin complet.

```json
"servers": {
		"IBM Tutorials": {
			"type": "stdio",
			"command": "fastmcp",
			"args": [
				"run",
				"<YOUR PATH>/ibmtutorialmcpserver/server.py"
			]
		},
	},
```

### Étape 4. Utiliser le serveur MCP

Maintenant que vous avez activé votre serveur MCP, faisons-le fonctionner pour que vous puissiez utiliser l’outil créé dans server.py. Si vous utilisez VS Code, consultez ces documents.

Dans le chat IDE, je vais demander : « Quels sont les tutoriels que propose IBM sur les séries chronologiques ? » Ce qui suit montre que la sortie a été reçue, mais votre réponse peut varier en fonction du modèle utilisé et de votre IDE.

\*\* Sortie :\*\*

```
Here are some IBM time series tutorials:

Time series forecasting with Lag-Llama (zero-shot learning)
Tutorial link
Predict overnight low temperatures using the Lag-Llama model in a zero-shot learning scenario.

Using the watsonx.ai Time Series Forecasting API to predict energy demand
Tutorial link
Predict energy demand with the watsonx.ai Time Series Forecasting API.
Authors: Aleksandra Kłeczek and Meredith Syed

Let me know if you want details or help with a specific tutorial.
```

Parfait ! L'agent a pu utiliser l’outil `search_ibmtutorials`  que nous avons créé pour rechercher des tutoriels relatifs aux séries chronologiques.

## Récapitulatif

Dans ce tutoriel, vous avez appris à créer un serveur MCP pour rechercher tous nos tutoriels à l’aide du client MCP de votre choix. Vous avez créé un serveur MCP avec un outil de recherche unique qui récupère un index JSON à distance de tutoriels, filtré les résultats en fonction d’un terme de recherche pour les renvoyer dans un format lisible. Il utilise fastmcp pour enregistrer et exécuter l’outil, les requêtes pour récupérer les données, et inclut la gestion des erreurs pour le réseau, l’analyse et les problèmes inattendus. Lorsqu’il est exécuté, le serveur peut être connecté aux clients MCP pour une interrogation en direct de tous nos tutoriels.
