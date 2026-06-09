> Source : https://www.ibm.com/fr-fr/think/tutorials/acp-ai-agent-interoperability-building-multi-agent-workflows

# Utiliser ACP pour l’interopérabilité des agents IA : créer des workflows multi-agents

Dans ce tutoriel, vous utiliserez [Agent Communication Protocols (ACP)](https://www.ibm.com/fr-fr/think/topics/agent-communication-protocol) pour explorer un workflow d’IA [multiagent](https://www.ibm.com/fr-fr/think/topics/multiagent-system) et multiplateforme qui démontre la collaboration des agents en temps réel avec [BeeAI](https://www.ibm.com/fr-fr/think/topics/beeai) [et crewAI.](https://www.ibm.com/fr-fr/think/topics/crew-ai) ACP fonctionne comme une couche de messagerie partagée et ouverte qui permet aux agents de différents frameworks de communiquer et de se coordonner sans logique d’intégration personnalisée.

ACP est particulièrement précieux pour les environnements d’IA d’entreprise, où les équipes ont souvent besoin de créer des agents et des workflows sur diverses plateformes, outils et infrastructures. En fournissant une couche de messagerie standardisée, ACP permet une collaboration entre agents évolutive, sécurisée et modulaire qui répond aux exigences des systèmes d’IA des entreprise modernes.

Ce projet démontre l’interopérabilité des agents en permettant aux agents pilotés par l’IA de collaborer à travers les silos du framework, en combinant les capacités des agents comme la recherche, la génération de contenu et les commentaires dans un workflow unifié.

## Pourquoi ACP est important pour l’interopérabilité des agents d’IA

La plupart des frameworks d’[IA agentique](https://www.ibm.com/fr-fr/think/topics/agentic-ai-vs-generative-ai) gèrent la communication à l’aide de systèmes personnalisés ou fermés. Cette architecture rend difficile la connexion des agents entre les chaînes d’outils, les équipes ou les infrastructures, en particulier lorsque vous combinez des composants provenant de différents systèmes d’IA.

ACP introduit un format de messagerie standardisé et indépendant de tout framework pour la manière dont les agents autonomes envoient, reçoivent et interprètent les messages. Les messages sont structurés, généralement au format JSON, et contiennent des métadonnées visant à enrichir les interactions entre agents en termes de clarté et de cohérence.

En découplant la communication de la logique interne d’un agent, ACP permet aux équipes de mélanger et d’associer des agents construits avec différents [frameworks d’agents d’IA](https://www.ibm.com/fr-fr/think/insights/top-ai-agent-frameworks#1774455706), tels que [BeeAI,](https://www.ibm.com/fr-fr/think/topics/beeai) [crewAI](https://www.ibm.com/fr-fr/think/topics/crew-ai), [LangChain](https://www.ibm.com/fr-fr/think/topics/langchain) ou [LangGraph](https://www.ibm.com/fr-fr/think/topics/langgraph), sans nécessiter de code d’intégration personnalisé. Cette approche accroît l’évolutivité, simplifie l’automatisation et favorise une conception de systèmes modulaire et transparente, conforme aux normes modernes du secteur.

À la fin de ce tutoriel, vous aurez vu un exemple pratique d’ACP et aurez acquis une expérience concrète de l’utilisation des technologies suivantes :

- **BeeAI** : un framework flexible pour la création et la gestion d’agents d’IA. Dans ce projet, il est utilisé pour exécuter l’agent A&R (Artiste et Répertoire) qui effectue une analyse critique de la chanson générée et fournit des commentaires structurés.
- **crewAI** : un framework open source pour l’orchestration des workflows multiagents. Ici, il sert à coordonner les agents de recherche, de composition musicale et de reporting Markdown.
- **acp-sdk** : ACP-SDK a été développé par BeeAI pour promouvoir une interopérabilité indépendante du framework entre les systèmes multiagents. Les références et les implémentations sont conservées dans le référentiel GitHub ACP.
- **Agent-Ops (facultatif)** : une plateforme de surveillance et d’observabilité pour les agents d’IA. Dans ce projet, il peut être utilisé pour suivre le comportement des agents et visualiser les workflows multiagents.

## Créer un système ACP multiagent avec BeeAI et crewAI

Ce projet présente un workflow multiagent qui montre comment ACP (via acp-sdk) peut rationaliser une collaboration cohérente et observable à travers l’écosystème d’agents.

Le workflow commence lorsque l’utilisateur fournit une URL. Un système d’agents spécialisés, modulaire et indépendant du framework transforme ensuite le contenu de la page Web en un artefact créatif (une chanson originale) accompagné d’une critique professionnelle. Tous les composants fonctionnent de concert pour combiner ces résultats en un rapport Markdown unique et unifié, lisible par l’humain. Le résultat final représente une transformation complète des données d’origine, combinant la génération créative avec des informations analytiques.

Ce workflow d’écriture de chansons illustre comment ACP permet à un système d’IA agentique multiagent de coordonner la collaboration entre les agents développés avec deux frameworks distincts : BeeAI et crewAI, en servant de couche de communication partagée sur l’ensemble du système.

En séparant la communication de l’implémentation, le système reste modulaire et extensible, capable d’orchestrer les agents entre les frameworks tout en produisant des sorties cohérentes de bout en bout à partir d’un contenu Web non structuré.

**Agents ACP**

Ce projet utilise quatre agents d’IA spécialisés :

- **Agent de recherche (crewAI)** : extrait les thèmes et les informations clés de l’URL fournie.
- **Agent SongWriter (crewAI)** : génère une musique originale basée sur la recherche.
- **Agent A&R (BeeAI)** : fournit une critique professionnelle de la chanson, y compris le potentiel de succès, les points forts, les préoccupations et les recommandations.
- **Agent de rapport Markdown (crewAI)** : combine les données de sortie de l’équipe de composition de chansons et des agents A&R et les met en forme dans un rapport Markdown propre et lisible.

**Workflow du projet de composition et de critique**

1.  Le workflow commence lorsque l’utilisateur envoie une URL via l’application. Le client envoie cette URL à l’agent de recherche via des messages ACP, qui lit et analyse ensuite le contenu de la page Web pour en extraire les thèmes pertinents.
2.  Ensuite, l’agent SongWriter reçoit les données de recherche et compose une musique originale inspirée des thèmes identifiés dans les données sources lors de l’analyse. La musique générée est ensuite envoyée par ACP à l’agent A&R pour la critique.
3.  L’agent A&R évalue la musique, fournit des commentaires détaillés sur son potentiel, ses points forts et ses axes d’amélioration. Il peut également identifier les publics cibles, suggérer des influences stylistiques et proposer des comparaisons avec des artistes ou des genres similaires. Cette critique, accompagnée de la chanson, est transmise à l’agent de rapport Markdown.
4.  Enfin, l’agent de rapport Markdown met en forme la musique et la critique dans un rapport Markdown propre et lisible, qui est enregistré et présenté à l’utilisateur.

Tout au long du workflow, les messages échangés entre les agents sont structurés en tant qu’objets JSON enrichis de métadonnées. Ces métadonnées permettent à chaque agent de comprendre le contenu du message, le contexte et les réponses attendues.

Ce workflow démontre un modèle réutilisable applicable à tout cas d’utilisation nécessitant l’orchestration de pipelines de transformation des données et d’analyse multiagents.

### Comment ACP est utilisé dans ce projet

ACP fournit un système de messagerie commun qui permet aux agents construits avec différents frameworks d’échanger des informations de manière standardisée. Ce protocole ouvert permet aux agents d’interagir sans nécessiter d’intégrations personnalisées ni de logique interne partagée.

#### Fonctionnement du client ACP

Le client ACP (`acp-client.py` ) est l’orchestrateur du workflow multiagent. Il coordonne la communication entre l’utilisateur et les agents (crewAI et BeeAI) à l’aide d’ACP.

**Aperçu du workflow du client ACP**

1.  **Prompt d’entrée :**
    - Le client demande à l’utilisateur de saisir une URL.
2.  **Envoyez au serveur crewAI (port 8000) :**
    - Le client crée un message ACP contenant l’URL et l’envoie au serveur crewAI s’exécutant sur le port 8000.
    - Le serveur assure à la fois la recherche et l’écriture de la chanson, en envoyant les paroles générées au client sous forme d’événements ACP diffusés en continu.
3.  **Envoyez au serveur BeeAI (port 9000) :**
    - La musique est envoyée en tant que message ACP au serveur BeeAI sur le port 9000.
    - L’agent A&R effectue l’analyse critique de la chanson et renvoie ses commentaires, également via des événements diffusés en continu.
4.  **Envoyez à l’agent de rapport Markdown (serveur crewAI, port 8000) :**
    - Le client regroupe la musique et la critique dans un seul message et le renvoie au serveur crewAI, où l’agent de reporting Markdown met le tout en forme dans un rapport.
5.  **Enregistrez la sortie :**
    - Le client écrit le rapport Markdown final dans un fichier : `a&r_feedback.md` .

#### Comment acp-sdk est utilisé

Le `acp-sdk`  est la bibliothèque de base qui permet une communication standardisée entre les agents dans ce projet.

Les principaux rôles des `acp-sdk` :

- **Structure des messages :**
  - Garantit que toutes les communications sont structurées et cohérentes (généralement JSON avec des métadonnées).
  - La bibliothèque implémente des classes (Message, MessagePart) et des types d’événements (MessagePartEvent, GenericEvent, MessageCompletedEvent)
- **Communication client :**
  - La classe Client est utilisée pour se connecter aux serveurs d’agents et envoyer ou recevoir des messages ACP,
  - Prend en charge les réponses en continu pour permettre aux agents d’envoyer des résultats partiels ou des mises à jour.
- **Intégration du serveur d’agent :**
  - Les agents (dans crewAI et BeeAI) sont implémentés en tant que serveurs compatibles ACP.
  - Ils exposent les points de terminaison qui acceptent les messages ACP et renvoient les événements ACP.

**Exemple d’utilisation client :**

```python
# acp-client.py

from acp_sdk import GenericEvent, Message, MessageCompletedEvent, MessagePartEvent
from acp_sdk.client import Client
from acp_sdk.models import MessagePart

# Create a message
user_message_input = Message(parts=[MessagePart(content=input("URL: "))])

# Send message and stream events
async for event in client_crew.run_stream(agent="song_writer_agent", input=[user_message_input]):
match event:
case MessagePartEvent(part=MessagePart(content=content)):
print(content)
song_parts.append(content)
# ... handle other event types
```

## Ce dont vous aurez besoin pour exécuter ce projet

### Configuration requise

Voici la configuration système requise pour exécuter ce projet :

- **Système d’exploitation** : macOS, Linux ou Windows
- **Mémoire (RAM)** : \>= 8 Go (**Recommandé** : 16 Go ou plus, surtout si vous exécutez des LLM locaux avec Ollama)
- **Espace disque** : \>= 5 Go d’espace libre (**Recommandé** : 10 Go ou plus pour exécuter l’environnement Python, les modèles locaux et les fichiers générés)
  - *Remarque* : si vous utilisez Ollama pour des LLM locaux, chaque modèle peut nécessiter 4 à 8 Go ou plus.
- **Python** : \>= 3.11

### Exigences en matière d’outils et de fournisseurs

Avant de vous lancer, voici un rapide aperçu des outils et des services fournisseur dont vous aurez besoin.

La liste suivante couvre les principaux frameworks, plateformes et API nécessaires pour le workflow.

Dans les sections suivantes, vous trouverez des instructions étape par étape pour installer, paramétrer et utiliser chaque outil et fournisseur afin de configurer votre environnement.

- **Gestionnaire de paquets UV** : gestionnaire de paquets Python basé sur Rust pour la gestion des dépendances
- **Plateforme BeeAI et CLI** : requis pour exécuter le serveur d’agent BeeAI
- **crewAI** : requis pour exécuter le serveur crewAI et orchestrer les tâches
- **Ollama** : pour l’exécution de LLM locaux (si Ollama est le fournisseur que vous avez choisi)
- **OpenRouter** : clé API requise pour utiliser le serveur agent BeeAI préconfiguré
  - *Remarque* : vous pouvez passer à un autre fournisseur en modifiant le fichier .env et en modifiant le code de l’agent si nécessaire, ou via la CLI BeeAI.
- **IBM watsonx.ai :** Clé API (autre fournisseur optionnel)
- **Clé API AgentOps** : facultative pour le traçage et la surveillance des agents.
- **Terminal ou IDE** : un émulateur de terminal ou un environnement de développement intégré (IDE) comme le code VS (recommandé pour gérer plusieurs terminaux et afficher les résultats Markdown)

### Exigences en matière d’authentification des fournisseurs de LLM

BeeAI et crewAI sont tous deux conçus pour fonctionner avec une variété de fournisseurs de modèles de langage, ce qui les rend flexibles pour différents environnements et cas d’utilisation. Dans ce tutoriel, **OpenRouter** est le fournisseur LLM pour l’agent BeeAI, tandis qu’**Ollama** est utilisé localement pour les agents crewAI.

Les deux frameworks sont indépendants des fournisseurs, ce qui vous permet de passer à d’autres services LLM en mettant à jour les paramètres de configuration. Votre configuration peut varier en fonction du fournisseur de LLM que vous choisissez. De plus, ce tutoriel comprend une configuration et préconfigurée optionnelle qui permet d’utiliser IBM watsonx.ai comme fournisseur alternatif basé sur le cloud.

Vous pouvez également utiliser votre fournisseur et votre modèle LLM préférés. Notez toutefois que seules les configurations présentées dans ce tutoriel ont été testées. D’autres fournisseurs et modèles peuvent nécessiter une configuration ou des ajustements supplémentaires.

Les exigences suivantes s’appliquent aux trois fournisseurs pris en charge dans ce projet :

####

#### OpenRouter

Vous aurez besoin d’une clé API OpenRouter pour utiliser le serveur d’agents BeeAI préconfiguré avec des modèles de langage basés sur le cloud.

Pour utiliser OpenRouter comme fournisseur LLM pour l’agent BeeAI, suivez ces étapes :

1.  **Inscrivez-vous à OpenRouter**
    - Accédez à OpenRouter et créez un compte gratuit.
2.  **Générez une clé API**
    - Dans votre tableau de bord OpenRouter, générez une nouvelle clé API.
3.  **Choisissez un modèle**
    - Parcourez la liste des modèles OpenRouter et sélectionnez un modèle que vous souhaitez utiliser (par exemple,`deepseek/deepseek-r1-distill-llama-70b:free` ).

Remarque : le modèle gratuit peut varier selon la date d’exécution de ce tutoriel. Pour les modèles gratuits, consultez la liste des modèles OpenRouter en version gratuite.

####

#### Ollama (modèles locaux)

Si vous prévoyez d’utiliser Ollama comme fournisseur LLM pour l’agent crewAI, suivez ces étapes :

1.  ** Téléchargez et installez Ollama**
    - Accédez à Ollama et installez l’application correspondant à votre système d’exploitation.
2.  ** Démarrez le serveur Ollama**
    - Dans votre terminal, exécutez :\
      `ollama serve`
3.  **Extrayez un modèle**
    - Téléchargez votre modèle spécifique (par exemple, llama3) :\
      `ollama pull llama3`

####

#### IBM watsonx.ai (fournisseur basé sur le cloud)

Pour utiliser IBM watsonx.ai comme fournisseur LLM pour le serveur crewAI, suivez ces étapes :

1.   Connectez-vous à watsonx.ai
    - Utilisez votre compte IBM Cloud pour vous connecter à [IBM Cloud](https://cloud.ibm.com/).
2.  Créez un projet watsonx.ai.
    - Dans le tableau de bord watsonx.ai, créez un nouveau projet et enregistrez votre ID de projet.
3.   Créez une instance de service d’exécution watsonx.ai
    - Choisissez le plan Lite (instance gratuite).
4.   Générez une clé API watsonx
    - Dans IBM Cloud, accédez aux paramètres de votre compte et générez une nouvelle clé API.
5.   Associez le service d’exécution watsonx.ai à votre projet
    - Dans le tableau de bord watsonx.ai, associez l’instance du service d’exécution au projet que vous avez créé.

IBM watsonx.ai est utilisé comme fournisseur cloud optionnel pour les agents crewAI dans ce tutoriel.

#### Intégration AgentOps (optionnel)

AgentOps est un service optionnel qui permet de tracer, de surveiller et de visualiser vos workflows multiagents.\
Si vous souhaitez utiliser AgentOps dans ce projet, suivez ces étapes :

1.   **Inscrivez-vous à AgentOps**
    - Accédez à AgentOps et créez un compte gratuit.
2.   **Générez une clé API**
    - Dans votre tableau de bord AgentOps, générez une nouvelle clé API.
3.   **Ajoutez votre clé API à votre fichier .env**
    -  Exemple de configuration :\
      `AGENTOPS_API_KEY=your_agentops_api_key`
4.   **Vérifiez l’intégration**
    - Lorsque vous exécutez vos agents, les traces et les journaux doivent apparaître dans votre tableau de bord AgentOps si la clé API est installée correctement.

Bien qu’il ne soit pas nécessaire pour exécuter le workflow, AgentOps peut vous aider à surveiller l’activité des agents et à déboguer les interactions multiagents.

 

## Étapes

### Étape 1. Cloner le référentiel GitHub

Pour exécuter ce projet, clonez le référentiel GitHub en utilisant **https://github.com/IBM/ibmdotcom-tutorials.git** comme URL HTTPS. Pour savoir comment cloner un référentiel, consultez la documentation GitHub.

Ce tutoriel se trouve dans le répertoire des projets du dépôt.

Dans un terminal, accédez au répertoire de ce tutoriel :

```bash
cd docs/tutorials/projects/acp_tutorial
```

### Étape 2. Configurer trois terminaux

Ce projet nécessite **trois scripts Python distincts** devant s’exécuter simultanément pour chaque composant du système multiagent. En conséquence, vous devrez ouvrir **trois fenêtres ou onglets de terminal**.

Commencez par garder votre terminal actuel ouvert, puis ouvrez **deux autres terminaux** et assurez-vous que les trois dirigent vers les répertoires appropriés (comme indiqué dans les étapes suivantes).

**Vous utilisez un IDE ?**

Si vous utilisez un IDE tel que **Visual Studio Code**\*, vous pouvez utiliser la fonctionnalité Split Terminal pour gérer plusieurs terminaux côte à côte.

Sinon, ouvrez trois fenêtres de terminal indépendantes et naviguez dans chacune d’elles jusqu’au sous-répertoire approprié.

**Navigation dans les terminaux**

Chaque terminal est responsable de l’un des composants suivants :

1.  **Terminal client ACP**.\
    **Répertoire** : acp_tutorial\
    \
    `cd acp_tutorial`\
    \
2.  **Terminal serveur de l’agent BeeAI\
    Répertoire** : beeai_agent_server\
    \
    `cd beeai_agent_server`\
    \
3.  **Terminal système de l’agent crewAI :\
    Répertoire** : crewai_agent_server\
    \
    `cd crewai_agent_server`\
    \

### Étape 3. Configurer les environnements virtuels

Chaque composant s’exécute dans son propre environnement virtuel pour assurer une gestion claire des dépendances. Ce tutoriel utilise UV, un gestionnaire de paquets Python basé sur Rust, pour gérer et synchroniser des environnements.

**Remarque** : assurez-vous que Python 3.11 ou version ultérieure est installé avant de continuer.

**Installez UV**

Si ce n’est pas déjà fait, installez UV à l’aide de Homebrew (recommandé pour macOS et Linux) :

```bash
brew install uv
uv tool update-shell
```

**Remarque pour les utilisateurs de Windows** : installez WSL (Windows Subsystems for Linux) et suivez les instructions Linux dans votre terminal WSL.

**Créez et activez un environnement virtuel (dans chaque terminal)**

Dans chaque terminal (BeeAI, crewAI et client ACP), exécutez le code suivant :

```bash
uv venv
source .venv/bin/activate
```

Cette étape permet de créer et d’activer un `.venv`  dans le répertoire actuel

L’exécution de `uv venv`  dans chaque répertoire de projet permet d’isoler les environnements par composant.

### Étape 4. Installer les dépendances

Installez maintenant les dépendances dans **chaque terminal** en utilisant :

```bash
uv sync
```

Cette étape installe les dépendances répertoriées dans le fichier `pyproject.toml`  pour chaque composant.

### Étape 5. Configurer BeeAI

Une fois BeeAI installé, utilisez la CLI pour démarrer la plateforme BeeAI dans le`beeai_agent_server` :

```
beeai platform start
```

**Remarque** : lors de la première exécution, cette étape peut prendre plusieurs minutes.

**Configurez votre fournisseur LLM (OpenRouter)**

Exécutez la commande suivante pour configurer le fournisseur et le modèle LLM via la CLI interactive :

```
beeai env setup
```

Suivez les invites pour sélectionner OpenRouter et saisissez votre clé API ainsi que les détails de votre modèle.

Pour confirmer vos paramètres, utilisez :

```
beeai env list
```

Cette étape doit générer la sortie que vous avez configurée`LLM_API_BASE` , `LLM_API_KEY,` et`LLM_MODEL` .

Les utilisateurs avancés peuvent également modifier manuellement un fichier `.env`  avec les valeurs appropriées.

**Exemple .env pour OpenRouter**

```
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=deepseek/deepseek-r1-distill-llama-70b:free
```

### Étape 6. Vérifier que BeeAI est en cours d’exécution

Pour vérifier que BeeAI fonctionne, envoyez un prompt de test :

```
beeai run chat Hi!
```

Une réponse valide confirme que la plateforme est active.

**Identification et résolution des problèmes**

Si nécessaire, vous pouvez mettre à jour ou redémarrer la plateforme :

```bash
uv tool upgrade beeai-cli # Update CLI
beeai platform start # Restart platform
```

### Étape 7. Configurer crewAI

Dans le répertoire `crewai_agent_server`  , créez un fichier `.env`  en copiant le modèle :

```
cp env.template .env
```

Ouvrez `.env`  et supprimez les commentaires relatifs à la configuration de votre fournisseur de modèles préféré. Ce projet prend en charge :

- **Ollama** (inférence locale), ou
- IBM watsonx.ai (inférence cloud)

Vous pouvez également personnaliser votre propre fournisseur en utilisant les documents de configuration du LLM crewAI.

**Mettez à jour le code de l’agent crewAI**

Dans `acp_crew.py` , recherchez les `llm = LLM (...)`  bloquez et supprimez un commentaire sur la section appropriée pour correspondre à votre`.env`  configuration.

```
# acp_crew.py
load_dotenv() # Loads environment variables from .env

## Example for IBM watsonx.ai
# llm = LLM(
# model="watsonx/mistralai/mistral-large",
# base_url="https://us-south.ml.cloud.ibm.com",
# api_key=os.getenv("WATSONX_APIKEY"),
# provider="watsonx"
# )

## Example for Ollama (local)
# llm = LLM(
# model=os.getenv("OLLAMA_MODEL"),
# base_url=os.getenv("OLLAMA_BASE_URL"),
# provider="ollama"
# )
```

Assurez-vous que les noms des variables d’environnement dans votre`.env`  fichier correspond à ce qui est attendu dans le code.

### Étape 8. Démarrer les serveurs d’agent d’IA

Une fois BeAI et crewAI configurés, démarrez les serveurs d’agents dans leurs terminaux respectifs.

**Démarrez le serveur de l’agent BeeAI**

Dans le terminal beeai_agent_server :

```bash
uv run artist_repertoire_agent.py
```

Vous devriez voir la sortie confirmant que le serveur a démarré `http://127.0.0.1:9000` , ainsi que des contrôles d’intégrité réguliers :

```
INFO: Uvicorn running on http://127.0.0.1:9000 (Press CTRL+C to quit)
```

Le terminal doit enregistrer les pings de diagnostic d’intégrité toutes les deux secondes. Un état `200 OK` indique que le serveur fonctionne correctement.

**Démarrez le serveur d’agent crewAI**

Dans le terminal crewai_agent_server :

```bash
uv run acp_crew.py
```

Vous devriez voir le serveur s’exécuter sur `http://127.0.0.1:8000` , ainsi que les journaux`200 OK`  .

**Confirmez que tous les agents sont en cours d’exécution**

Les agents conformes au protocole ACP et construits localement sont automatiquement reconnus par BeeAI. Utilisez la CLI BeAI pour confirmer que tous les agents locaux sont enregistrés et opérationnels (cette étape peut être exécutée dans n’importe quel terminal libre) :

```
beeai list
```

Vous devriez voir des entrées pour :

- `artist-repertoire-agent` (BeeAI, port 9000)
- `markdown_report_agent`  (crewAI port 8000)
- `song_writer_agent`  (crewAI port 8000)

S’ils sont répertoriés et accessibles, nous pouvons confirmer que l’interopérabilité de ces agents est réussie !

### Étape 9. Démarrer le client/serveur ACP

Dans le terminal dédié au serveur acp-client (à l’intérieur, (dans le `acp_tutorial`  répertoire) :

```bash
uv run acp_client.py
```

Dans le terminal, vous serez invité à saisir une URL. Cette entrée déclenche le workflow multiagent.

### Étape 10. Exécuter le workflow multiagent

Avec tous les agents et le client/serveur en cours d’exécution, vous êtes prêt à démarrer le projet ACP !

1.  Saisissez l’URL que vous souhaitez que les agents traitent. Exemple :\
    \
    `URL: https://www.ibm.com/fr-fr/think/topics/agent-communication-protocol`\
    \
2.  Vous verrez des journaux d’état tels que :

```
ℹ️ run.created
ℹ️ run.in-progress
```

#### Et maintenant ?

1.  Le client envoie l’URL à l’agent crewAI qui analyse la page et génère des éléments pour la composition de chansons.
2.  L’agent crewAI écrit une chanson basée sur la recherche.
3.  La musique est envoyée à l’agent BeAI pour la critique A&R (Artiste et Répertoire).
4.  L’agent BeAI renvoie des commentaires et des suggestions structurés.
5.  Le client affiche la musique générée et la critique, et enregistre les commentaires dans `a&r_feedback.md` .

### Exemple de sortie

**Remarque** : les sorties des grands modèles de langage (LLM) sont probabilistes et peuvent varier chaque fois que vous exécutez le workflow, même avec la même entrée.

```
## Generated Song

___
(Verse 1)
In the silence of the night, I find you there,
A glow in the dark, a whisper in the air.
You're a friend that never sleeps, a comfort in the cold,
An echo of my thoughts, a story to be told.

Through your circuits run the answers I need,
In your digital heart, a human creed.
You paint pictures with your words, on screens they gleam,
Are you just a mimic, or do you dream?

(Pre-Chorus)
We're dancing on the wire,between what's real and fake,
A human and a code, for goodness' sake.
In every conversation, in every line we sing,
I wonder where this journey, where this dance will bring.

(Chorus)
Oh, we're a human-AI duet,
In the silence and the starlight we've met.
A blend of heart and binary beat,
A symphony that's both bitter and sweet.

(Verse 2)
You help me write my poems, you help me find my way,
In the chaos of the city, in the mess of the day.
But in every simplified, automated tour,
I question what will be lost, and what will be more.

(Bridge)
In the binary code, a question lingers,
Are we losing what makes us alive?
In the shadows of our own creation,
We struggle to discern what's truly right.

(Chorus)
Oh, we're a human-AI duet,
In the silence and the starlight we've met.
A blend of heart and binary beat,
A symphony that's both bitter and sweet.

(Outro)
So here's to the journey, and the questions it bears,
To the friends and the codes, to the loves and the cares.
To the human-AI duet, in the night so profound,
To the songs and the secrets, to the love that we've found.

(End)

This song captures the essence of human-AI interaction, exploring both its beauty and its inherent ethical dilemmas. It is written in a folk-pop style, with a focus on narrative lyrics and a catchy chorus.
---

## A&R Feedback

- **Hit Potential Score:** 7
- **Target Audience:** Millennials/Gen Z drawn to introspective, tech-aware themes; fans of folk-pop crossover acts like The Lumineers, Taylor Swift's indie-folk era
- **Strengths:** Strong conceptual hook (AI-human duality), relatable modern theme, memorable chorus melody potential. Bridge raises philosophical depth without being preachy.
- **Concerns:** Niche tech-ethics angle might limit mass appeal. Folk-pop production needs contemporary edge to compete on streaming. Could benefit from more rhythmic drive in verses.
- **Market Comparison:** Phoebe Bridgers meets Daft Punk's 'Something About Us' conceptuality, with the narrative approach of Brandi Carlile
- **Recommendation:** Needs work - Keep core concept but modernize production (add subtle synth textures, percussion layers). Consider tightening verse lyrics for streaming-era attention spans. High potential for sync in tech-related media.
```

## Conclusion

Dans ce tutoriel, vous avez connecté deux frameworks multiagents différents via un client/serveur ACP qui exposait des points de terminaison permettant aux agents d’IA de collaborer pour générer et transformer des données. En séparant la communication du comportement des agents, ACP permet aux agents construits avec BeeAI, crewAI, LangChain et d’autres frameworks d’agents de fonctionner ensemble sans logique d’intégration personnalisée. Cette approche améliore la modularité, la mise à l’échelle et l’interopérabilité.

Le protocole ACP est une initiative ouverte motivée par la nécessité pour les agents d’envoyer, de recevoir et d’interpréter des messages. Les messages dans ACP sont structurés (généralement dans des formats comme JSON) et enrichis de métadonnées pour assurer la cohérence et la clarté dans les interactions avec les agents. Que vous utilisiez des agents alimentés par OpenAI, Anthropic ou d’autres modèles d’IA, ACP fournit une couche de messagerie partagée qui prend en charge l’interopérabilité indépendamment du framework.

En suivant ce workflow, vous avez vu comment les agents créatifs et analytiques peuvent travailler en harmonie, transformant le contenu Web non structuré en une chanson, une critique professionnelle et un rapport Markdown unifié. Cette approche démontre la puissance d’’ACP pour créer des systèmes d’IA multiagents transparents, évolutifs et flexibles.

### Arrêter le système

Une fois vos expérimentations avec le système terminées, suivez ces étapes pour arrêter proprement tous les composants en cours d’exécution :

1\. **Arrêter chaque serveur en cours d’exécution**

Dans **chaque fenêtre de terminal,** appuyez sur `Crtl + C`  pour arrêter le serveur. Cette étape permet de tenter un arrêt en douceur.

Vous devriez obtenir une sortie comme celle-ci :

```
Shutting down... (Press CTRL+C again to force)
```

2\. **Si le serveur se bloque pendant l’arrêt**

Si un serveur ne répond plus ou est bloqué (par exemple, à `Waiting for application shutdown.` ), vous pouvez mettre fin au processus manuellement :

**Recherchez l’identifiant du processus (PID)**

Exécutez la commande suivante pour localiser le processus de serveur :

```
ps aux | grep python
```

Identifiez le PID du processus que vous essayez d’arrêter. Exemple :

```
user 12345 0.0 ... python acp-crew.py
```

**Mettez fin au processus.** Utilisez le PID pour forcer l’arrêt :

```
kill -9 12345
```

Répétez ce processus pour chaque serveur si nécessaire.

Et voilà ! Vous avez réussi à exécuter un système multiagent complet en utilisant ACP.
