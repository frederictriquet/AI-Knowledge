> Source : https://www.ibm.com/fr-fr/think/tutorials/build-agentic-workflows-langgraph-granite

# Créer des workflows agentiques avec LangGraph et Granite

Les systèmes d’IA modernes évoluent au-delà des simples interactions prompt-réponse. Les [agents d’IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) d’aujourd’hui peuvent effectuer un raisonnement structuré à plusieurs étapes, prendre des décisions et coordonner des tâches complexes de manière autonome. Cette fonctionnalité émergente est appelée [workflow agentique](https://www.ibm.com/fr-fr/think/topics/agentic-workflows), un bouleversement dans le domaine du [machine learning,](https://www.ibm.com/fr-fr/think/topics/machine-learning) où les agents passent par une série d’étapes logiques pour résoudre les problèmes plus efficacement.

Dans ce tutoriel, nous allons découvrir comment de tels workflows agentiques d’IA en utilisant deux outils clés : LangGraph un framework pour construire des chemins de raisonnement basés sur des graphes, et IBM Granite[](https://www.ibm.com/fr-fr/products/watsonx-ai/foundation-models), un modèle robuste qui complète cette structure. Chaque étape du workflow, appelée « nœud », est gérée par un agent, généralement alimenté par de grands modèles de langage. Ces agents passent d’un état à l’autre en fonction des sorties du modèle ou de la logique conditionnelle, formant ainsi un graphe dynamique axé sur les décisions.

Pour donner vie à ces workflows, intéressons-nous à deux composants essentiels : LangGraph et Granite.

## Comprendre LangGraph

#### Un framework pour des workflows évolutifs pilotés par l’IA

LangGraph est un framework conçu pour rationaliser le développement des workflows pilotés par l’IA en représentant les modèles d’IA sous forme d’agents à état dans un graphe de calcul. Il permet aux développeurs de créer des systèmes modulaires et évolutifs où chaque comportement ou point de décision est défini comme un nœud dans le graphe.

Avec LangGraph, vous pouvez :

- Définir chaque comportement d’agent comme un nœud distinct
- Utilisez des algorithmes ou des sorties de modèles pour déterminer l’étape suivante
- Transmettez l’état entre les nœuds pour préserver la mémoire et le contexte
- Visualisez, déboguez et contrôlez facilement le flux de raisonnement

Les systèmes multiagents et les frameworks comme LangGraph, lorsqu’ils sont appliqués à des tâches d’IA générative, structurent généralement l’exécution des tâches sous forme de workflows séquentiels ou conditionnels. Que vous travailliez avec LangChain, les modèles IBM Granite, les modèles GPT d’OpenAI ou d’autres outils d’intelligence artificielle, LangGraph vous aide à optimiser votre workflow pour plus d’évolutivité et de meilleures performances.

## Composants clés de LangGraph pour l’automatisation de workflows complexes

LangGraph introduit une approche moderne de l’orchestration des technologies d’IA en décomposant des workflows complexes en composants modulaires et intelligents. Contrairement à l’automatisation traditionnelle ou à l’automatisation robotisée des processus (RPA), LangGraph permet une exécution dynamique et contextuelle des tâches en s’appuyant sur la logique et la mémoire en temps réel. Voici les quatre composants clés qui alimentent ce framework :

- Nœuds : les nœuds représentent des unités individuelles de logique ou d’action, telles que l’appel d’un outil d’IA, l’interrogation de sources de données ou l’exécution d’une tâche spécifique. Ils sont parfaits pour automatiser les tâches répétitives dans le cadre de processus métier plus vastes.
- Arcs : les arcs définissent le flux entre les nœuds, guidant la façon dont les tâches sont reliées et exécutées. Cette structure favorise une prise de décision flexible et permet aux workflows de s’adapter en fonction des résultats.
- Arcs conditionnels (graphes cycliques) : les graphes cycliques activent les boucles et les embranchements conditionnels, ce qui permet au système de revoir les nœuds en fonction de la logique ou des productions du modèle. Cette capacité est essentielle pour gérer les tâches itératives et prendre des décisions éclairées dans des environnements dynamiques.
- État (graphes avec état) : l’état agit comme une mémoire partagée, préservant le contexte et permettant l’utilisation de données en temps réel entre les nœuds. Cette capacité permet à LangGraph d’aller au-delà des flux statiques et de prendre en charge des améliorations adaptatives et intelligentes dans l’automatisation des workflows.

Ensemble, ces composants permettent à LangGraph de transformer la façon dont les entreprises conçoivent et exécutent des workflows pilotés par l’IA, en rapprochant les outils d’IA des processus métier réels.

  Figure 1 : Composants clés de LangGraph pour l’automatisation de workflows complexes

## Modèle Granite : un LLM léger pour la résolution de problèmes concrets

Granite-4.0-Tiny-Preview, développé par IBM Research, est un modèle de langage open source léger et performant, conçu pour résoudre des problèmes complexes et des tâches pratiques de traitement automatique du langage naturel (NLP). Bien qu’il soit plus petit que les modèles commerciaux tels que GPT-4, Granite est rapide, efficace et entièrement compatible avec Hugging Face, ce qui en fait un excellent choix pour les développeurs qui recherchent l’efficacité opérationnelle sans sacrifier les performances.

Granite excelle dans :

- Classification d’intentions – identifier les objectifs des utilisateurs dans les chatbots ou les systèmes basés sur les tâches
- La génération créative : production de synthèses, de dialogues ou de contenus courts
- Raisonnement et synthèse – idéal pour les workflows impliquant la RAG ou l’analyse de données

Dans ce tutoriel, le modèle Granite joue un rôle clé dans différentes étapes du workflow agentique, assurant à la fois la résolution de problèmes et la génération de contenu. Sa conception légère le rend adapté aux applications du monde réel où l’intervention humaine peut être limitée et où les modèles de conception évolutifs sont essentiels pour créer des solutions d’IA robustes à travers divers ensembles de données et fournisseurs.

## Cas d’utilisation

Dans ce tutoriel, nous allons créer un workflow agentique qui agit comme un assistant créatif pour l’écriture de courts scénarios animés.

### Objectif

Lorsque l’utilisateur fournit une idée d’histoire, l’agent peut :

- Identifier le genre et le ton appropriés
- Élaborer un bref résumé de l’intrigue
- Le développer en une scène clé (par exemple, un rebondissement ou un tournant)
- Écrire le dialogue pour cette scène au format capture d’écran

Ce cas d’utilisation est conçu pour illustrer à la fois les capacités de raisonnement et de génération d’un modèle de langage, structurées par le workflow compositionnel de LangGraph.

### Fonctionnement du workflow

Chacune des étapes suivantes est mise en œuvre en tant que nœud LangGraph :

- **Entrée utilisateur** : l’utilisateur propose une première idée d’histoire pour initier le workflow.
- **Détection du genre *(node_name - select_genre)*** : un LLM analyse l’entrée pour en déduire le genre et le ton appropriés à l’histoire.
- **Génération du résumé *(node_name - generate_outline)*** : le LLM génère un court résumé de l’intrigue en fonction du genre sélectionné.
- **Écriture de scènes *(node_name - generate_select)*** : le LLM écrit une scène charnière en prose, donnant vie à l’histoire.
- **Écriture de dialogue *(node_name - write_dialogue)*** : le LLM réécrit la scène sous forme de boîte de dialogue de capture d’écran formatée, adaptée à la production ou à l’édition ultérieure.

Ces nœuds sont connectés séquentiellement à un LangGraph, et le modèle se déplace à travers eux tout en transportant un dictionnaire d’état modifiable.

Ce workflow établit un équilibre entre la génération créative et la planification structurelle. Il démontre :

- La coordination du LLM avec LangGraph
- La narration en plusieurs étapes avec une intervention manuelle minimale
- L’automatisation créative dans un domaine où l’imagination humaine est essentielle

Il est également facile à adapter ; vous pouvez l’étendre aisément en ajoutant des étapes de révision, plusieurs générateurs de scènes ou même une logique de branchement basée sur les personnages.

## Prérequis

Vous devez disposer d’un [compte IBM Cloud](https://cloud.ibm.com/registration?utm_source=ibm_developer&utm_content=in_content_link&utm_id=tutorials_awb-implement-xgboost-in-python&cm_sp=ibmdev-_-developer-_-trial) pour créer un projet [watsonx.ai](https://www.ibm.com/fr-fr/products/watsonx-ai?utm_source=ibm_developer&utm_content=in_content_link&utm_id=tutorials_awb-implement-xgboost-in-python&cm_sp=ibmdev-_-developer-_-product) .

## Étapes

### Étape 1. Configurer votre environnement

Bien que vous puissiez faire votre choix parmi plusieurs outils, ce tutoriel vous guide pas à pas pour configurer un compte IBM à l’aide d’un Jupyter Notebook.

1.  Connectez-vous à [watsonx.ai](https://dataplatform.cloud.ibm.com/registration/stepone?context=wx&apps=all) en utilisant votre compte IBM Cloud.
2.  Créez un [projet watsonx.ai](https://www.ibm.com/docs/en/watsonx/saas?topic=projects-creating-project). Vous pouvez obtenir l’ID de votre projet à partir de ce dernier. Cliquez sur l’onglet **Manage** (Gérer). Ensuite, copiez l’ID du projet depuis la section **Details** (Détails) de la page **General** (Général). Vous aurez besoin de cet ID pour ce tutoriel.
3.  Créez un [Jupyter Notebook](https://www.ibm.com/docs/en/watsonx/saas?topic=editor-creating-managing-notebooks).

Cette étape ouvre un environnement de notebook dans lequel vous pouvez copier le code de ce tutoriel. Vous pouvez également télécharger ce notebook sur votre système local et le charger dans votre projet watsonx.ai en tant qu’actif. Pour consulter d’autres tutoriels Granite, accédez à la page [Communauté IBM Granite](https://github.com/ibm-granite-community). Ce tutoriel est également disponible sur [GitHub](https://github.com/IBM/ibmdotcom-tutorials)

### Étape 2. Configurer le service d’exécution watsonx.ai et une clé API

1.  Créez une instance de service [Runtime watsonx.ai](https://cloud.ibm.com/catalog/services/watsonxai-runtime) (choisissez le plan Lite, qui est une instance gratuite).
2.  Générez une clé d’interface de programmation d’application [(clé API)](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html).
3.  Associez le service d’exécution watsonx.ai au projet que vous avez créé dans [watsonx.ai](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/assoc-services.html?context=cpdaas).

### Étape 3. Installer les bibliothèques requises

Cette cellule installe les bibliothèques principales requises pour utiliser le modèle IBM Granite hébergé sur Hugging Face :

- `transformers:` Il s’agit de la bibliothèque principale pour charger et interagir avec des modèles de langage pré-entraînés, notamment`granite-4.0-tiny-preview` .
- `accelerate:`  Facilite le chargement efficace des modèles et le placement des appareils, particulièrement utile pour une utilisation transparente des GPU.

Les`-q` indicateur exécute l’installation silencieusement, supprimant ainsi la sortie verbeuse pour une interface plus propre. Ces bibliothèques sont essentielles pour télécharger le modèle et gérer efficacement l’inférence dans ce tutoriel.

Remarque : si vous exécutez ce tutoriel dans un environnement virtuel et que Langgraph n’est pas préinstallé, utilisez la commande pip ’install langgraph’ pour l’installer dans votre environnement local.

```
!pip install -q transformers accelerate
```

  Extrait de sortie : Créer un workflow agentique – installation des bibliothèques

### Étape 4. Importer les bibliothèques requises

Cette cellule importe toutes les bibliothèques principales nécessaires à la création et à l’exécution du workflow agentique :

`AutoTokenizer` et`AutoModelForCausalLM` de`transformers` : permet de charger le modèle Granite et de tokeniser les prompts d’entrée pour la génération.

`torch` : fournit l’accélération GPU et les opérations tensorielles requises pour l’inférence des modèles.

`time:` Permet le suivi du temps et la surveillance des performances (optionnels).

`StateGraph` et`END` de`langgraph.graph` : ces éléments sont utilisés pour définir et compiler le graphe du workflow agentique.

`IPython.display` ,`base64:` Permet d’afficher le résultat de manière soignée et d’activer les fonctionnalités de téléchargement optionnelles du contenu généré dans les Jupyter Notebooks.

Ensemble, ces importations préparent l’environnement pour l’interaction avec les modèles, la structuration du workflow et la présentation de la production.

```python
# Import libraries
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time
from langgraph.graph import StateGraph, END
from IPython.display import display, HTML
import base64
```

### Étape 5. Charger le modèle Granite et le tokenizer

Cette cellule charge le modèle d’IBM`granite-4.0-tiny-preview` et son tokeniseur correspondant de Hugging Face :

`model_id:` Spécifie l’identifiant du modèle pré-entraîné hébergé sur Hugging Face.

`AutoTokenizer.from_pretrained(model_id):` Charge le tokeniseur associé au modèle Granite. Le tokeniseur est chargé de convertir le texte lisible par l’homme en tokens d’entrée pour le modèle.

`AutoModelForCausalLM.from_pretrained(...):` Charge le modèle de langage proprement dit pour la modélisation du langage causal (c’est-à-dire génératif). Ce modèle peut prédire et générer des sorties textuelles sur la base de l’entrée.

Les`torch_dtype=torch.float32` argument définit explicitement le type de données sur float32, ce qui est plus efficace en termes de mémoire et plus largement compatible, particulièrement utile dans les environnements où les GPU sont limités.

Cette étape initialise efficacement le modèle Granite comme « **moteur de raisonnement** » derrière notre workflow agentique.

```
#Load Granite-4.0-Tiny-Preview model and tokenizer from Hugging Face
model_id = "ibm-granite/granite-4.0-tiny-preview"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32)
```

  Extrait de sortie : Créer un workflow agentique – charger le modèle Granite

### Étape 6. Fonction utilitaire pour générer du texte avec Granite

Cette fonction,`generate_with_granite` , encapsule le processus de génération de texte à l’aide du modèle Granite. Accepte le prompt qui correspond à l’entrée pour guider la réponse du modèle.

`max_tokens` : nombre maximal de tokens à générer dans la sortie (par défaut : 200).

`use_gpu` : un indicateur précisant s’il faut exécuter l’inférence sur le GPU (si disponible).

**Informations principales :**

`device = torch.device(...):` Sélectionne dynamiquement le GPU (cuda) si demandé et disponible ; sinon, il utilise le CPU par défaut.

`model.to(device):` Charge le modèle sur l’appareil approprié juste à temps, contribuant ainsi à économiser de la mémoire.

`tokenizer(prompt, return_tensors="pt"):` Convertit la chaîne d’entrée en tenseurs de token pour le traitement des modèles.

`model.generate(...):` Démarre la génération de texte avec les stratégies d’échantillonnage suivantes :

- `do_sample=True:` Permet d’obtenir des résultats aléatoires plus créatifs.

- `temperature=0.7` et`top_p=0.9:` Contrôle la diversité du texte généré.

`tokenizer.decode(...):` Convertit les tokens générés en texte lisible, en supprimant tous les tokens spéciaux.

Cette fonction sera réutilisée tout au long du workflow agentique pour invoquer le modèle Granite sur différents nœuds de décision ou de génération.

```python
def generate_with_granite(prompt: str, max_tokens: int = 200, use_gpu: bool = False) -> str:
    device = torch.device("cuda" if use_gpu and torch.cuda.is_available() else "cpu")

    # Move model to device only at generation time
    model.to(device)
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
```

 

### Étape 7. Créer un nœud pour sélectionner le genre et le ton *(node-1)*

Cette fonction,`select_genre_node` , définit le premier nœud de notre workflow de génération de scripts agentiques. Elle utilise le modèle Granite pour déterminer le genre et le ton de l’histoire en fonction de l’entrée de l’utilisateur.

Entrée :`state` , un dictionnaire qui inclut`"user_input"` (par exemple, « Je veux écrire une histoire fantastique pour les enfants »).

Construction du prompt : le prompt demande au modèle de :

- Agir en tant qu’assistant créatif.
- Analyser l’entrée fournie par l’utilisateur.
- Recommander un genre et un ton en utilisant un format de sortie spécifique :`Genre: ` et`Tone: `

Génération de texte : le prompt est transmis à la`generate_with_granite()` fonction utilitaire pour générer une réponse créative.

Analyse de la sortie : une simple boucle extrait le genre et le ton de la réponse du modèle sur la base des préfixes de ligne (`"Genre:"` et`"Tone:"` ).

Mise à jour de l’état : les valeurs extraites`genre` et`tone` sont insérées à nouveau dans le dictionnaire d’état qui sera transmis au nœud suivant.

Ce nœud agit comme un classificateur créatif, permettant aux nœuds suivants de générer des résumés, des structures et des scènes alignés sur le contexte en utilisant le genre et le ton comme paramètres fondamentaux.

```python
def select_genre_node(state: dict) -> dict:
prompt = f"""
You are a creative assistant. The user wants to write a short animated story.
Based on the following input, suggest a suitable genre and tone for the story.
User Input: {state['user_input']}

Respond in this format:
Genre: <genre>
Tone: <tone>
""".strip()

response = generate_with_granite(prompt)

# Basic parsing of output
genre, tone = None, None
for line in response.splitlines():
if "Genre:" in line:
genre = line.split("Genre:")[1].strip()
elif "Tone:" in line:
tone = line.split("Tone:")[1].strip()

# Update state
state["genre"] = genre
state["tone"] = tone
return state
```

### Étape 8. Créer un nœud pour générer le résumé de l’intrigue *(node-2)*

Les`generate_outline_node` définit le deuxième nœud dans le workflow de génération de scénario. Elle s’appuie sur le genre et le ton sélectionnés pour générer un résumé concis de l’article.

Entrée : la fonction reçoit le dictionnaire d’états contenant :

- user_input : l’idée originale de l’histoire.
- genre : sélectionné dans le nœud précédent.
- ton : sélectionné dans le nœud précédent.

Construction de prompt : il est indiqué au modèle de :

- Agir comme un assistant d’écriture créative.
- Tenir compte de l’idée, du genre et du ton de l’utilisateur.
- Générer un bref résumé de l’intrigue (3 à 5 phrases) adapté à un court scénario animé.

Génération de texte : le prompt est envoyé à`generate_with_granite()` avec un taux`token limit (max_tokens=250)` pour laisser de la place à un résumé de plusieurs phrases.

Mise à jour de l’état : le résumé de l’intrigue généré est ajouté à l’état sous la clé`"outline"` , prêt à l’utilisation dans la prochaine étape d’extension de la structure.

Ce nœud traduit l’intention créative abstraite en **trame narrative** et fournit un cadre pour la structure détaillée en trois actes qui suit. Il s’assure que les nœuds en aval fonctionnent à partir d’une base de référence cohérente et imaginative.

```python
def generate_outline_node(state: dict) -> dict:
prompt = f"""
You are a creative writing assistant helping to write a short animated screenplay.
The user wants to write a story with the following details:
Genre: {state.get('genre')}
Tone: {state.get('tone')}
Idea: {state.get('user_input')}

Write a brief plot outline (3–5 sentences) for the story.
""".strip()

response = generate_with_granite(prompt, max_tokens=250)
state["outline"] = response
return state
```

### Étape 9. Créer un nœud pour générer une scène clé à partir du résumé *(node-3)*

Les`generate_scene_node` fonction définit la troisième étape du workflow où le résumé de l’intrigue est transformé en une scène narrative riche. Cette scène sert à dramatiser de façon saisissante un tournant dans l’histoire, faisant passer l’idée du résumé à la narration.

Entrée : le nœud prend le dictionnaire d’état, qui inclut désormais :

- `genre` et`tone`
- Les`plot outline` du nœud précédent

Construction de prompt : il est indiqué au modèle de :

- Agir en tant que scénariste
- Générer un tournant ou un rebondissement en utilisant le`genre` ,`tone` et`outline`
- Écrire en prose pour préserver la **lisibilité** et l’**adaptation à l’animation** de la description

Exigences pour la scène :

- Dynamique et descriptive (adaptée à l’animation)
- Au cœur de l’arc émotionnel ou narratif (par exemple, découverte, conflit ou résolution)

Génération de texte :`generate_with_granite` est appelée avec`max_tokens=300` , laissant suffisamment d’espace pour créer des scènes immersives.

Mise à jour de l’état : la scène générée est ajoutée au dictionnaire d’état sous la`"scene"` clé.

Il introduit une immersion conversationnelle et un storytelling visuel dans le workflow. Au lieu de simplement résumer l’histoire, ce nœud **lui donne vie** grâce à des détails sensoriels et émotionnels, essentiels pour la scénarisation de courts métrages d’animation.

```python
def generate_scene_node(state: dict) -> dict:
prompt = f"""
You are a screenwriter.
Based on the following plot outline, write a key scene from the story.
Focus on a turning point or climax moment. Make the scene vivid, descriptive, and suitable for an animated short film.

Genre: {state.get('genre')}
Tone: {state.get('tone')}
Outline: {state.get('outline')}

Write the scene in prose format (not screenplay format).
""".strip()

response = generate_with_granite(prompt, max_tokens=300)
state["scene"] = response
return state
```

### Étape 10. Créer un nœud pour l’écriture d’un dialogue entre personnages au format scénario *(node-4)*

Les`write_dialogue_node` fonction définit la quatrième étape créative du workflow de storytelling : convertir une scène narrative en **dialogue formaté entre personnages**. Cette étape permet de combler le fossé entre la prose et l’**écriture de scénarios prêts à être filmés**, en donnant une voix aux personnages.

Entrée : le nœud attend l’état`scene` pour contenir un moment fort (généralement un tournant ou un rebondissement).

Construction de prompt : le modèle est guidé pour :

- Agir en tant qu’auteur de dialogues
- Extraire et adapter le dialogue de la scène
- Formater la sortie dans un style d’écran en utilisant :`CHARACTER: Dialogue line`

Consignes pour le dialogue :

- Rester concis et expressif
- S’assurer que le texte est adapté à l’animation (visuel, émotionnel, concis)
- Inventer des noms si nécessaire pour plus de clarté

Génération : l’appel`generate_with_granite()` utilise`max_tokens=300` , qui concilie expressivité et brièveté, est idéal pour les petits scripts animés.

Mise à jour de l’état : le dialogue est enregistré dans l’état sous`dialogue` la clé pour les étapes suivantes (par exemple, afficher ou modifier).

```python
def write_dialogue_node(state: dict) -> dict:
prompt = f"""
You are a dialogue writer for an animated screenplay.

Below is a scene from the story:
{state.get('scene')}

Write the dialogue between the characters in screenplay format.
Keep it short, expressive, and suitable for a short animated film.

Use character names (you may invent them if needed), and format as:

CHARACTER:
Dialogue line

CHARACTER:
Dialogue line
""".strip()

response = generate_with_granite(prompt, max_tokens=300)
state["dialogue"] = response
return state
```

### Étape 11. Ajouter des rapports de progression à chaque nœud

Cette fonction d’assistance`with_progress` est conçu pour encapsuler chaque nœud de workflow avec des indicateurs de progression en temps réel. Il ne modifie pas la logique de la fonction originale ; il suit et imprime simplement l’état et le calendrier d’exécution pour rendre les workflows plus transparents.

Objectif de la fonction : encadrer un nœud (par exemple, generate_scene_node) avec un décorateur qui consigne :

- Quelle étape est en cours
- Index d’étape et nombre total
- Durée de l’étape

Paramètres :

- `fn` : la fonction de nœud réelle (par exemple, write_dialogue_node)
- `label` : une étiquette lisible par l’humain pour cette fonction
- `index` : numéro de l’étape dans la séquence (par exemple, 2)
- `total` : nombre total d’étapes dans le workflow

Commutateur interne :

- Imprime un message de départ
- Enregistre l’heure de début
- Appelle la fonction initiale
- Imprime un message de fin avec la durée écoulée

Retours : version modifiée de la fonction qui ajoute des **messages de progression**, mais qui se comporte de manière identique.

À mesure que les workflows se développent, il devient important de **savoir quelle étape est exécutée**, en particulier si certaines étapes (comme la génération ou l’édition) prennent plus de temps ou peuvent entraîner des problèmes tels qu’une surcharge de la mémoire. Cet encapsuleur de progression garantit la **transparence** ; il est utile pour le **débogage** et les **diagnostics d’exécution**.

```python
# Wrap with progress reporting

def with_progress(fn, label, index, total):
def wrapper(state):
print(f"\n[{index}/{total}] Starting: {label}")
start = time.time()
result = fn(state)
duration = time.time() - start
print(f"[{index}/{total}] Completed: {label} in {duration:.2f} seconds")
return result
return wrapper
```

### Étape 12. Définir le workflow LangGraph

Cette cellule définit la logique de workflow permettant de générer une courte histoire animée en utilisant LangGraph, un framework basé sur des graphes compositionnels et conçu pour les workflows de LLM. Chaque étape du graphe représente une tâche créative et est exécutée dans un ordre spécifique pour produire le scénario final.

**Composants du workflow :**`StateGraph(dict)`  - Initialise le workflow avec un état basé sur un dictionnaire (la mémoire de travail est un dict transmis de nœud à nœud).

Enregistrement d’un nœud avec suivi de la progression : chaque étape (sélection de genre, génération de résumé, écriture de scène, écriture de dialogue) est ajoutée en tant que nœud avec l’encapsuleur with_progress() - 

```
graph.add_node("select_genre", with_progress(select_genre_node, "Select Genre", 1, 4)) 
```

Cette approche garantit que chaque nœud enregistre son exécution et sa progression lorsqu’il est exécuté.

Arcs de workflow (séquencement de nœuds) : la séquence du pipeline créatif est clairement définie :

```
select_genre → generate_outline → generate_scene → write_dialogue
```

 

`set_entry_point()` et`set_finish_point():` Ces éléments définissent les nœuds de début et de fin du workflow.

`graph.compile():` Compile le workflow dans un format exécutable (workflow) qui peut désormais être invoqué avec un état initial.

Cette structure permet un workflow de LLM **modulaire**, **lisible** et **débogable**. Chaque étape de votre processus créatif est isolée, peut être profilée séparément et être ensuite permutée ou étendue (par exemple, en ajoutant une étape « Réviser la scène » ou un nœud « Résumer la sortie »). Le`workflow` est maintenant prêt à être exécuté avec un prompt et exécutera votre pipeline créatif étape par étape, en montrant la progression en direct.

```
# Define LangGraph

graph = StateGraph(dict)
graph.add_node("select_genre", with_progress(select_genre_node, "Select Genre", 1, 4))
graph.add_node("generate_outline", with_progress(generate_outline_node, "Generate Outline", 2, 4))
graph.add_node("generate_scene", with_progress(generate_scene_node, "Generate Scene", 3, 4))
graph.add_node("write_dialogue", with_progress(write_dialogue_node, "Write Dialogue", 4, 4))

graph.set_entry_point("select_genre")
graph.add_edge("select_genre", "generate_outline")
graph.add_edge("generate_outline", "generate_scene")
graph.add_edge("generate_scene", "write_dialogue")
graph.set_finish_point("write_dialogue")

workflow = graph.compile()
```

 

### Étape 13. Exécuter le workflow LangGraph et afficher la sortie

C’est dans cette dernière cellule de code que vous exécutez le **workflow** et que vous affichez les résultats de chaque étape de la génération de l’histoire.

`initial_state:` Cette commande constitue le point de départ du workflow, où l’utilisateur fournit une idée créative ou un thème. L’entrée utilisateur sert de départ au pipeline de l’histoire.

`final_state:` Cette commande déclenche le pipeline LangGraph complet. L’entrée passe par chaque nœud enregistré (select_genre, generate_outline, generate_rational, et write_dialogue) en séquence.

Affichage des résultats : le dictionnaire d’état final contient désormais des clés alimentées par différents nœuds :

- `"genre":` Le genre identifié en fonction de l’entrée de l’utilisateur.
- `"tone":` La qualité tonale de l’histoire.
- `"outline":` un résumé de l’intrigue de 3 à 5 phrases.
- `"scene":` Une scène marquant un tournant écrite en prose.
- `"dialogue":` Dialogue entre les personnages présenté comme un scénario.

Cette section montre comment l’intention de l’utilisateur est transformée en un mini-script complet grâce à un workflow de LLM modulaire par étapes. Il s’agit d’un pipeline créatif de bout en bout, interactif, interprétable et personnalisable.

***Remarque : l’exécution prend environ 15 à 17 minutes si vous utilisez un GPU ou un GPU. Comptez 65 à 70 minutes dans un environnement virtuel local pour l’exécution et la génération de la sortie en fonction de l’infrastructure utilisée.***

```python
# Run workflow
initial_state = {
"user_input": "I want to write a whimsical fantasy story for children about a lost dragon finding its home."
}
final_state = workflow.invoke(initial_state)

# Display Results
print("\n=== Final Output ===")
print("Genre:", final_state.get("genre"))
print("Tone:", final_state.get("tone"))
print("\nPlot Outline:\n", final_state.get("outline"))
print("\nKey Scene:\n", final_state.get("scene"))
print("\nDialogue:\n", final_state.get("dialogue"))
```

Essayons de comprendre comment le système transforme le prompt de l’utilisateur (« Je veux écrire une histoire captivante pour les enfants sur un dragon perdu qui retrouve sa maison ») en une histoire animée complète. Chaque étape s’appuie sur la précédente, guidée par les nœuds créatifs du workflow et optimisée par le modèle Granite.

**1. Genre et ton**. Le workflow commence par interpréter le prompt original de l’utilisateur : *Je veux écrire une histoire captivante pour les enfants sur un dragon perdu qui retrouve sa maison.* Sur la base de cette entrée, le nœud select_genre_node classe correctement le récit en tant que **conte fantastique** et identifie le ton enchanteur et réconfortant approprié. Ce résultat est précis et contextuellement cohérent, car l’utilisation d’expressions comme **« fantastique »**, **« pour enfants »** et **« dragon perdu retrouvant sa maison »** signale clairement un style narratif magique mais gentil. Le genre et le ton agissent comme des paramètres fondamentaux qui façonnent chaque étape de génération suivante dans le workflow.

**2. Résumé de l’intrigue et description des personnages.** Lors de l’étape suivante, il est demandé au modèle de créer un résumé de l’intrigue en fonction du genre identifié, du ton et de l’idée originale de l’utilisateur. *Le résultat comprend non seulement un résumé de l’histoire de 3 à 5 phrases, mais aussi des descriptions de personnages bonus*, probablement en raison d’une fuite de prompt ou d’une mise en forme d’instructions conservée des itérations précédentes.

L’intrigue est centrée sur une jeune fille nommée Lily qui découvre un dragon blessé et l’aide à retourner dans la forêt enchantée grâce aux conseils d’un vieux herboriste. Ce scénario reflète exactement l’intention de l’utilisateur, en se concentrant sur un parcours magique adapté aux enfants avec des nuances émotionnelles sur la guérison, l’appartenance et l’amitié. Les portraits des personnages que sont le dragon, Lily et l’herboriste ajoutent de la profondeur, transformant une idée vague en un concept structuré avec des rôles, des personnalités et des responsabilités narratives définis. Cette étape permet de passer d’une intention abstraite à une structure tangible adaptée à l’écran.

**3. Scène clé.** Compte tenu de la description complète de l’intrigue, le`generate_scene_node` écrit une scène saisissante en prose qui capture un tournant dans l’histoire, un autre élément explicitement demandé dans l’intention initiale de l’utilisateur de développer un court script d’animation.

Le moment choisi est celui où Lily soigne le dragon blessé dans la forêt enchantée, établissant ainsi un lien émotionnel et une compréhension mutuelle entre les personnages. Ce moment est crucial car il oriente l’histoire vers le retour du dragon chez lui. La scène, riche en images et en émotions, respecte les contraintes « fantastiques » et « réconfortantes » tout en étant visuellement expressive, parfaitement adaptée à un court métrage d’animation.

La capacité du modèle à maintenir le ton et la cohérence de genre à travers les étapes démontre la valeur du workflow de passage d’état de LangGraph et les capacités de raisonnement du modèle Granite.

**4. Dialogue au format scénario.** Enfin, le`write_dialogue_node` convertit la scène en prose en un dialogue structuré au format écran. Le prompt utilisateur, axé sur la **création d’une histoire pour l’animation**, exige implicitement que le récit soit présenté dans un format prêt pour la production ou la visualisation. Ce nœud remplit cet objectif en fournissant un dialogue correctement mis en forme entre Lily, Drago (le dragon) et le vieux herboriste sur deux scènes distinctes : le cottage et la forêt enchantée. Le dialogue préserve les nuances émotionnelles et les intentions des personnages, et sa mise en forme respecte les conventions d’écriture des scénarios d’animation (par exemple, les noms des personnages en majuscules, les en-têtes de scène comme`[INT. LILY’S COTTAGE - DAY])` . La sortie reste courte, expressive et émotionnelle, ce qui est essentiel pour capter l’attention du jeune public dans un décor animé.

À chaque étape du workflow, le prompt, *« une histoire fantastique pour enfants sur un dragon perdu retrouvant sa maison »*, est converti en sortie structurée, créative et expressive. De la sélection du genre à la mise en forme des dialogues, le système crée progressivement un arc de storytelling cohérent. Le framework LangGraph garantit que les transitions entre les tâches sont logiquement reliées, et le modèle IBM Granite permet de générer des textes sensibles au contexte avec un ton cohérent. Le résultat est une histoire d’animation courte et dense, prête à être diffusée à l’écran, qui émerge entièrement d’une simple ligne de saisie utilisateur, démontrant ainsi la puissance pratique des workflows automatisés dans les applications d’IA créatives.

Pour rendre l’expérience de storytelling encore plus attrayante, voici une simple visualisation en HTML qui agence magnifiquement les éléments de l’histoire générés : genre, ton, intrigue, scène et dialogue. De plus, **en un seul clic, vous pouvez télécharger l’intégralité du script** sous forme de fichier texte pour une utilisation ou un partage ultérieur. Donnons vie à cette histoire à l’écran !

```python
# Beautification and Downloadable option creation for user

def display_output_with_download(final_state):
genre = final_state.get("genre", "")
tone = final_state.get("tone", "")
outline = final_state.get("outline", "")
scene = final_state.get("scene", "")
dialogue = final_state.get("dialogue", "")

# Combine scene and dialogue into a full script
script = f"""Genre: {genre}
Tone: {tone}
Outline:
{outline}
Scene:
{scene}
Dialogue:
{dialogue}
"""

# Encode to base64
b64_script = base64.b64encode(script.encode()).decode()

# Create downloadable HTML content
html = f"""
<h2>Genre & Tone</h2>
<p><strong>Genre:</strong> {genre}</p>
<p><strong>Tone:</strong> {tone}</p>

<h2>Outline</h2>
<pre>{outline}</pre>

<h2>Scene</h2>
<pre>{scene}</pre>

<h2>Dialogue</h2>
<pre>{dialogue}</pre>

<a download="screenplay_script.txt" href="data:text/plain;base64,{b64_script}">
<button style="margin-top: 20px; padding: 10px 20px; font-size: 16px;">Download Script as .txt</button>
</a>
"""
display(HTML(html))

# Run this after workflow.invoke()
display_output_with_download(final_state)
```

## Remarques sur l’infrastructure et l’utilisation du GPU

Ce tutoriel utilise la solution Granite-4.0-Tiny-Preview pour la génération de texte. Bien qu’il s’agisse d’un modèle plus petit de la famille Granite, il nécessite tout de même un environnement compatible GPU pour fonctionner efficacement, en particulier lors de l’exécution de plusieurs nœuds dans un workflow LangGraph.

Configuration recommandée :

- Au moins un GPU NVIDIA V100 ou A100
- 16 Go de mémoire GPU ou plus pour des performances stables
- Python 3.8+ avec Torch, transformers et Langgraph installés

Remarques sur les performance :

- Vous pouvez rencontrer des erreurs de mémoire CUDA si vous exécutez tous les nœuds de manière séquentielle sans effacer la mémoire du GPU.
- Pour minimiser les problèmes de mémoire :
  - Déplacez le modèle vers le GPU uniquement pendant la génération et revenez ensuite au CPU.
  - Limitez la génération des tokens (max_tokens=200–300).
  - Vous pouvez également supprimer ou simplifier des nœuds tels que la révision ou l’extension détaillée de la scène.

Si vous exécutez ce tutoriel dans un environnement de notebook hébergé (par exemple, IBM watsonx.ai ou Google Colab Pro), assurez-vous que le GPU est activé dans les paramètres d’exécution.

Pour les environnements aux ressources limitez, envisagez ce qui suit :

- Déchargement de l’inférence du modèle vers l’API Hugging Face Inference.
- Réduire la complexité du workflow.
- En utilisant le CPU (avec des temps de génération plus longs).

## Récapitulatif

Dans ce tutoriel, nous avons créé un workflow de storytelling modulaire et agentique à l’aide de LangGraph et du modèle de langage Granite-4.0-Tiny-Preview d’IBM. À partir d’un simple prompt créatif, nous avons construit un pipeline étape par étape qui classe les genres et les tons, génère un résumé de l’intrigue, écrit une scène clé et se termine par des dialogues de type scénario. En cours de route, nous avons démontré comment :

- Structurez vos workflows dynamiques à l’aide de LangGraph
- Intégrez des LLM légers comme Granite pour le raisonnement créatif
- Gérer les contraintes de mémoire GPU avec un chargement de modèles ad hoc
- Affichez et exportez la sortie de l’histoire dans un format facile à utiliser

Ce framework agentique est non seulement puissant pour l’écriture de scénarios, mais peut également être étendu à un large éventail de cas d’utilisation créatifs ou de routage de tâches. En quelques nœuds seulement, vous avez créé un assistant d’écriture miniature capable de transformer une idée singulière en une histoire prête à être scénarisée.

Que vous soyez développeur, conteur ou chercheur, ce tutoriel vous fournit une base pratique pour explorer l’ingénierie des workflows basée sur les LLM dans les domaines créatifs.

Prêt à créer vos propres agents ? Laissez libre cours à votre créativité avec les modèles IBM Granite et IBM watsonx Orchestrate.
