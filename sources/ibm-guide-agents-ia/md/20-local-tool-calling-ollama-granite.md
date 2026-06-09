> Source : https://www.ibm.com/fr-fr/think/tutorials/local-tool-calling-ollama-granite

# Appel d’outil avec Ollama

L’[appel d’outil](https://www.ibm.com/fr-fr/think/topics/tool-calling) dans les [grands modèles de langage](https://www.ibm.com/fr-fr/think/topics/large-language-models) (LLM) est la capacité du LLM à interagir avec des outils, services ou API externes pour effectuer des tâches. Cela permet aux LLM d’étendre leurs fonctionnalités et d’améliorer leur capacité à gérer des tâches du monde réel qui peuvent nécessiter l’accès à des données externes, à des informations en temps réel ou à des applications spécifiques. Lorsqu’un LLM utilise un outil de recherche Web, il peut appeler le Web pour récupérer des données en temps réel qui ne sont pas disponibles dans les données d’entraînement du modèle. D’autres types d’outils peuvent inclure Python pour les calculs, l’analyse de données ou la visualisation, ou l’appel d’un point de terminaison pour les données. L’appel d’outil peut rendre un [chatbot](https://www.ibm.com/fr-fr/think/topics/chatbots) plus dynamique et plus adaptable, lui permettant de fournir des réponses plus précises, pertinentes et détaillées sur la base de données en direct ou de tâches spécialisées ne relevant pas de sa base de connaissances immédiate. Parmi les frameworks populaires d’appel d’outil, citons notamment [Langchain](https://www.ibm.com/fr-fr/think/topics/langchain) et maintenant Ollama.

Ollama est une plateforme qui propose des modèles d’IA open source pour une utilisation sur des appareils personnels qui permet aux utilisateurs d’exécuter des LLM directement sur leurs ordinateurs. Contrairement à un service tel que l’API OpenAI, il n’est pas nécessaire de créer un compte, car le modèle se trouve sur votre ordinateur local. Ollama se concentre sur la confidentialité, la performance et la facilité d’utilisation, permettant aux utilisateurs d’accéder et d’interagir avec des modèles IA sans envoyer de données à des serveurs externes. Cette approche peut être particulièrement intéressante pour les personnes soucieuses de la confidentialité des données ou qui souhaitent éviter de dépendre d’API externes. Facile à configurer et à utiliser, la plateforme d’Ollama prend en charge divers modèles, offrant aux utilisateurs une gamme d’outils pour le traitement automatique du langage naturel, la génération de code et d’autres tâches d’IA, directement sur leur propre matériel. Elle convient bien aux architectures d’appel d’outil, car elle permet d’accéder à toutes les capacités d’un environnement local, y compris les données, les programmes et les logiciels personnalisés.

Dans ce tutoriel, vous apprendrez à configurer l’appel d’outil en utilisant Ollama pour examiner un système de fichiers local, une tâche qui serait difficile à effectuer avec un LLM distant. De nombreux modèles Ollama sont disponibles pour l’appel d’outil et la création d’[agents](https://www.ibm.com/fr-fr/think/topics/ai-agents) d’IA comme Mistral et [Llama 3.2](https://www.ibm.com/fr-fr/think/topics/llama-2). Une liste complète est disponible sur le [site Web d’Ollama](https://ollama.com/library). Dans ce cas, nous utiliserons IBM Granite 3.2 Dense qui est [compatible avec les outils](https://www.ibm.com/fr-fr/think/tutorials/granite-function-calling). Les modèles 2B et 8B sont des LLM denses textuels entraînés spécifiquement pour prendre en charge les cas d’utilisation basés sur des outils et pour la [génération augmentée par récupération](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation) (RAG), rationalisant la génération de code, la traduction et la correction des bugs.

Le notebook pour ce tutoriel peut être téléchargé sur Github [ici](https://github.com/IBM/ibmdotcom-tutorials/blob/main/generative-ai/ollama_tools.ipynb).

## Étape 1 : Installer Ollama

D’abord, téléchargez Ollama à partir de https://ollama.com/download et installez-le sur votre système d’exploitation. Sur OSX, cela se fait via un fichier .dmg, sur Linux via une seule commande shell, et sur Windows avec un programme d’installation. Vous aurez peut-être besoin d’un accès administrateur sur votre ordinateur pour exécuter le programme d’installation.

Vous pouvez vérifier qu’Ollama est correctement installé en ouvrant un terminal ou une invite de commandes et en saisissant :

```bash
ollama -v 
```

 

## Étape 2 : Installer les bibliothèques

Ensuite, ajoutez les importations initiales. Cette démo utilise la bibliothèque Ollama Python pour communiquer avec Ollama et la bibliothèque PyMuPDF pour lire des fichiers PDF dans le système de fichiers.

```python
!pip install pymupdf

import ollama
import os
import pymupdf
```

 

Ensuite, extrayez le modèle que vous utiliserez tout au long de ce tutoriel. Cela télécharge les poids de modèle d’Ollama vers votre ordinateur local et les stocke pour les utiliser sans avoir besoin d’effectuer des appels d’API à distance plus tard.

```
!ollama pull granite3.2
!ollama pull granite3.2-vision
```

## Étape 3 : Définir les outils

Définissez maintenant les outils auxquels l’instance d’outils Ollama aura accès. Comme l’objectif des outils est de lire des fichiers et de parcourir des images dans le système local de fichiers, vous allez créer deux fonctions Python pour chacun de ces outils. La première est`research_text_files` et il faut un mot-clé à rechercher dans les fichiers locaux. Pour les besoins de cette démo, le code ne recherche que les fichiers d’un dossier spécifique, mais il pourrait être développé pour inclure un second paramètre, définissant le dossier dans lequel l’outil effectuera la recherche.\
\
Vous pouvez utiliser une simple mise en correspondance des chaînes pour voir si le mot-clé se trouve dans le document, mais comme Ollama facilite l’appel de LLM locaux,`research_text_files` utilisera Granite 3.2 pour déterminer si le mot-clé décrit le texte du document. Pour ce faire, le document est lu dans une chaîne appelée`document_text` . La fonction appelle ensuite ollama.chat et donne le prompt suivant au modèle :

```
"Respond only 'yes' or 'no', do not add any additional information. Is the following text about " + keyword + "? " + document_text 
```

Si le modèle répond « oui », la fonction renvoie le nom du fichier contenant le mot-clé indiqué par l’utilisateur dans le prompt. Si aucun des fichiers ne semble contenir les informations, la fonction renvoie « Aucun » sous forme de chaîne.\
\
Cette fonction peut s’exécuter lentement la première fois car Ollama téléchargera Granite 3.2 Dense. 

```python
def search_text_files(keyword: str) -> str:

directory = os.listdir("./files/")
for fname in directory:

# look through all the files in our directory that aren't hidden files
if os.path.isfile("./files/" + fname) and not fname.startswith('.'):

if(fname.endswith(".pdf")):

document_text = ""
doc = pymupdf.open("./files/" + fname)

for page in doc: # iterate the document pages
document_text += page.get_text() # get plain text (is in UTF-8)

doc.close()

prompt = "Respond only 'yes' or 'no', do not add any additional information. Is the following text about " + keyword + "? " + document_text 

res = ollama.chat(
model="granite3.2:8b",
messages=[{'role': 'user', 'content': prompt}]
)

if 'Yes' in res['message']['content']:
return "./files/" + fname

elif(fname.endswith(".txt")):

f = open("./files/" + fname, 'r')
file_content = f.read()

prompt = "Respond only 'yes' or 'no', do not add any additional information. Is the following text about " + keyword + "? " + file_content 

res = ollama.chat(
model="granite3.2:8b",
messages=[{'role': 'user', 'content': prompt}]
)

if 'Yes' in res['message']['content']:
f.close()
return "./files/" + fname

return "None"
```

Le deuxième outil est `search_image_files`  et il faut un mot-clé à rechercher dans les photos locales. Cette recherche s’effectue en utilisant le modèle de description d’image Granite 3.2 Vision via Ollama. Ce modèle renverra une description textuelle de chaque fichier image du dossier et recherchera le mot-clé dans la description. L’un des points forts de l’utilisation d’Ollama est qu’on peut facilement construire des systèmes multi-agents pour appeler un modèle avec un autre.\
\
La fonction renvoie une chaîne, qui correspond au nom du fichier dont la description contient le mot-clé indiqué par l’utilisateur dans le prompt.

```python
def search_image_files(keyword:str) -> str:

directory = os.listdir("./files/")
image_file_types = ("jpg", "png", "jpeg")

for fname in directory:

if os.path.isfile("./files/" + fname) and not fname.startswith('.') and fname.endswith(image_file_types):
res = ollama.chat(
model="granite3.2-vision",
messages=[
{
'role': 'user',
'content': 'Describe this image in short
sentences. Use simple phrases first and then describe it more fully.',
'images': ["./files/" + fname]
}
]
)

if keyword in res['message']['content']:
return "./files/" + fname

return "None"
```

## Étape 4 : Définir les outils pour Ollama

Maintenant que les fonctions qu’Ollama doit appeler ont été définies, configurez les informations sur l’outil pour Ollama lui-même. La première étape consiste à créer un objet qui associe le nom de l’outil aux fonctions de l’appel de fonction d’Ollama :

```
available_functions = {
'Search inside text files':search_text_files,
'Search inside image files':search_image_files
}
```

Ensuite, configurez un tableau d’outils pour indiquer à Ollama les outils auxquels il aura accès et ce dont ces outils ont besoin. Il s’agit d’un tableau contenant un schéma d’objet par outil, qui indique au cadre d’appel d’outil d’Ollama comment appeler l’outil et ce qu’il renvoie.\
\
Dans le cas des deux outils créés précédemment, il s’agit de fonctions qui nécessitent un paramètre `mot-clé` . Actuellement, seules les fonctions sont prises en charge, bien que cela puisse changer à l’avenir. La description de la fonction et du paramètre permet au modèle d’appeler correctement l’outil. Le champ `Description` relatif à la fonction de chaque outil est transmis au LLM lorsqu’il sélectionne l’outil à utiliser. La `Description` du mot-clé est transmise au modèle lorsqu’il génère les paramètres qui seront transmis à l’outil. Vous pouvez vous tourner vers ces deux options pour affiner les prompts lorsque vous créez vos propres applications d’appel d’outil avec Ollama.

```
# tools don't need to be defined as an object but this helps pass the correct parameters
# to the tool call itself by giving the model a prompt of how the tool is to be used
ollama_tools=[
{
'type': 'function',
'function': {
'name': 'Search inside text files',
'description': 'This tool searches in PDF or plaintext or text files in the local file system for descriptions or mentions of the keyword.',
'parameters': {
'type': 'object',
'properties': {
'keyword': {
'type': 'string',
'description': 'Generate one keyword from the user request to search for in text files',
},
},
'required': ['keyword'],
},
},
},
{
'type': 'function',
'function': {
'name': 'Search inside image files',
'description': 'This tool searches for photos or image files in the local file system for the keyword.',
'parameters': {
'type': 'object',
'properties': {
'keyword': {
'type': 'string',
'description': 'Generate one keyword from the user request to search for in image files',
},
},
'required': ['keyword'],
},
},
},
]
```

\
Vous utiliserez cette définition d’outils pour appeler Ollama avec une entrée utilisateur.

## Étape 5 : Transmettre les entrées utilisateur à Ollama

Il est maintenant temps de transmettre l’entrée utilisateur à Ollama et de lui faire renvoyer les résultats des appels d’outil. Tout d’abord, vérifiez qu’Ollama fonctionne sur votre système :

```python
# if ollama is not currently running, start it
import subprocess
subprocess.Popen(["ollama","serve"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
```

Si Ollama est en cours d’exécution, vous obtiendrez :\

```
<Popen: returncode: None args: ['ollama', 'serve']>
```

Demandez maintenant à l’utilisateur de fournir une entrée. Vous pouvez également coder l’entrée en dur ou la récupérer à partir d’une interface de chat en fonction de la configuration de votre application. La fonction `entrée`  attendra l’entrée de l’utilisateur avant de continuer.

```python
# input
user_input = input("What would you like to search for?")
print(user_input)
```

Par exemple, si l’utilisateur saisit « Informations sur les chiens », cette cellule affichera :\

```
Information about dogs
```

La requête de l’utilisateur est maintenant transmise à Ollama lui-même. Les messages ont besoin du rôle de l’utilisateur et du contenu qu’il a saisi. Cela est transmis à Ollama en utilisant la fonction `chat` . Le premier paramètre est le modèle que vous souhaitez utiliser (dans ce cas, Granite 3.2 Dense), puis le message contenant l’entrée utilisateur, et enfin le tableau d’outils configuré précédemment.\
\
La fonction `chat` générera une production sélectionnant l’outil à utiliser et les paramètres qui doivent lui être transmis dans les appels d’outil suivants.

```
messages = [{'role': 'user', 'content':user_input}]

response: ollama.ChatResponse = ollama.chat(

# set which model we're using
'granite3.2:8b',

# use the message from the user
messages=messages,

tools=ollama_tools
)
```

Maintenant que le modèle a généré des appels d’outil dans la production, exécutez tous les appels d’outil avec les paramètres générés par le modèle et vérifiez la production. Dans cette application, Granite 3.2 Dense est également utilisé pour générer la production finale, de sorte que les résultats des appels d’outil sont ajoutés à l’entrée initiale de l’utilisateur, puis transmis au modèle.\
\
Étant donné que plusieurs appels d’outil peuvent renvoyer des fichiers correspondants, les réponses sont regroupées dans un tableau qui est ensuite transmis à Granite 3.2 pour générer une réponse. Le prompt qui précède les données indique au modèle comment répondre :

```
If the tool output contains one or more file names, then give the user only the filename found. Do not add additional details. 
If the tool output is empty ask the user to try again. Here is the tool output: 
```

La production finale est ensuite générée en utilisant les noms de fichiers renvoyés ou 

```python
# this is a place holder that to use to see whether the tools return anything 
output = []

if response.message.tool_calls:

# There may be multiple tool calls in the response
for tool_call in response.message.tool_calls:

# Ensure the function is available, and then call it
if function_to_call := available_functions.get(tool_call.function.name):
print('Calling tool: ', tool_call.function.name, ' \n with arguments: ', tool_call.function.arguments)
tool_res = function_to_call(**tool_call.function.arguments)

print(" Tool response is " + str(tool_res))

if(str(tool_res) != "None"):
output.append(str(tool_res))
print(tool_call.function.name, ' has output: ', output)
else:
print('Could not find ', tool_call.function.name)

# Now chat with the model using the tool call results
# Add the function response to messages for the model to use
messages.append(response.message)

prompt = '''
If the tool output contains one or more file names, 
then give the user only the filename found. Do not add additional details. 
If the tool output is empty ask the user to try again. Here is the tool output: 
'''

messages.append({'role': 'tool', 'content': prompt + " " + ", ".join(str(x) for x in output)})

# Get a response from model with function outputs
final_response = ollama.chat('granite3.2:8b', messages=messages)
print('Final response:', final_response.message.content)

else:

# the model wasn't able to pick the correct tool from the prompt
print('No tool calls returned from model')
```

À l’aide des fichiers fournis pour ce tutoriel, le prompt « Informations sur les chiens » renverra :

```
    Calling tool:  Search inside text files  
with arguments:  {'keyword': 'dogs'}
Tool response is ./files/File4.pdf
Search inside text files  has output:  ['./files/File4.pdf']
Calling tool:  Search inside image files  
with arguments:  {'keyword': 'dogs'}
Tool response is None
Final response: The keyword "dogs" was found in File4.pdf.
```

Vous pouvez constater que Granite 3.2 a choisi le bon mot-clé dans l’entrée (« chiens »), l’a recherché dans les fichiers du dossier et l’a trouvé dans un fichier PDF. Comme les résultats du LLM ne sont pas purement déterministes, vous pouvez obtenir des résultats légèrement différents avec le même prompt ou des prompts très similaires.
