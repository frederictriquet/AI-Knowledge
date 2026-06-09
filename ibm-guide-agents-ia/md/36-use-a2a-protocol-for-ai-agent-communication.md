> Source : https://www.ibm.com/fr-fr/think/tutorials/use-a2a-protocol-for-ai-agent-communication

# Utiliser le protocole A2A pour la communication avec l’agent d’IA

Le protocole A2A, ou [Agent2Agent](https://www.ibm.com/fr-fr/think/topics/agent2agent-protocol), est un standard ouvert qui permet une communication structurée entre les agents d’IA, les clients et les outils. Dans ce tutoriel, vous pouvez créer un système d’agent où un client de chat traite les requêtes utilisateur et les envoie à un agent d’IA sur un serveur conforme à la norme A2A.

La plupart des applications d’IA agentique mettent en œuvre une communication personnalisée entre les composants (par exemple, [ChatChain de ChatDev](https://www.ibm.com/fr-fr/think/tutorials/chatdev-chatchain-agent-communication-watsonx-ai)), ce qui rend difficile la réutilisation du même agent dans différentes applications ou l’intégration d’outils externes. Ce manque de standardisation empêche l’interopérabilité et limite le développement d’un écosystème d’agents plus large.

A2A résout cette limitation en séparant la couche de communication de la logique d’agent grâce à un protocole standardisé basé sur HTTP, JSON-RPC 2.0 et Server-Sent Events (SSE). Ce découplage permet aux agents de collaborer entre eux, de répondre aux requêtes client et d’accéder à des outils externes sans code d’intégration personnalisé.

A2A prend en charge les architectures décentralisées qui permettent aux équipes de faire évoluer leurs systèmes d’IA de manière progressive sans casser le code client. Les équipes peuvent mettre à jour les outils, échanger des modèles ou modifier le comportement des agents tout en conservant une interface cohérente dans des workflows complexes.

Les agents échangent des informations dans des messages structurés au format JSON-RPC qui incluent des métadonnées qui enrichissent les interactions des agents de manière claire et cohérente. Chaque serveur A2A expose une fiche AgentCard à un point de terminaison bien connu (.well-known/agent-card.json) qui décrit les capacités de l’agent sous forme de données JSON structurées. Cela permet aux clients de découvrir dynamiquement ce qu’un agent peut faire, de la même manière que la documentation de l’API décrit les points de terminaison disponibles.

Suivez ce guide pour créer et gérer un système d’agents A2A, et acquérez une expérience pratique avec :

- **BeeAI** : un framework open source pour la construction d’agents d’IA.
- **Protocole A2A** : un protocole de communication standardisé pour l’interopérabilité des agents.
- **Ollama** : un outil pour exécuter localement de grands modèles de langage (LLM).
- **Outils d’agents** : fonctionnalités spécialisées, notamment la recherche sur le Web (DuckDuckGo), les données météorologiques (OpenMeteo), l’accès à Wikipédia (WikipediaTool) et le raisonnement (ThinkTool)

**Remarque** : si vous avez travaillé avec ACP ([Agent Communication Protocol](https://www.ibm.com/fr-fr/think/topics/agent-communication-protocol)), vous constaterez quelques similitudes. ACP, initialement développé par BeeAI d’IBM, s’est associé à Google A2A sous l’égide de la Linux Foundation. BeeAI utilise désormais des adaptateurs A2A ([A2AServer](https://framework.beeai.dev/integrations/a2a#a2a-server) et [A2AAgent](https://framework.beeai.dev/integrations/a2a#a2a-agent-client)) pour fournir une communication conforme au protocole A2A. A2A fonctionne également avec MCP ([Model Context Protocol](https://www.ibm.com/fr-fr/think/topics/model-context-protocol)) pour permettre aux agents d’interagir avec les sources de données et les outils, créant ainsi des écosystèmes d’agents interopérables.

## Fonctionnement du système de chat A2A

Ce projet montre comment A2A permet une séparation claire entre l’interface client et la logique d’agent.

Le workflow suit cette séquence :

1.  **Entrée utilisateur** : le client capture l’entrée utilisateur via l’interface du terminal.
2.  **Requête A2A** : le client met en forme l’entrée en tant que contenu de message JSON-RPC et l’envoie au serveur d’agent.
3.  **Traitement de l’agent** : le serveur transmet la demande au`RequirementAgent` , qui analyse la tâche et exécute les outils appropriés selon les besoins.
4.  **Réponse A2A** : le serveur renvoie la réponse de l’agent sous forme de données structurées au format JSON-RPC, diffusant les résultats en temps réel au fur et à mesure de leur génération.
5.  **Affichage** : le client extrait et affiche le texte de la réponse dans le terminal.

Ce workflow démontre un modèle réutilisable applicable aux cas d’utilisation nécessitant une communication structurée entre clients et agents, tels que les chatbots, les systèmes d’automatisation des tâches, les agents de support client et les assistants de recherche avec orchestration des outils.

### Agent A2A

Ce projet utilise un seul agent d’IA avec plusieurs capacités d’outil. Dans les systèmes plus complexes, vous pouvez déployer plusieurs agents spécialisés, chacun se concentrant sur des domaines ou des tâches spécifiques.

**RequirementAgent** (BeeAI) : un agent déclaratif qui sélectionne et coordonne dynamiquement plusieurs outils en fonction de la requête utilisateur. Il utilise :

- `ThinkTool` pour le raisonnement et les opérations logiques
- `DuckDuckGoSearchTool` pour les recherches Web
- `OpenMeteoTool`  pour les données météorologiques
- `WikipediaTool` pour la récupération d’informations

### Le serveur A2A

Le serveur A2A (`beeai-a2a-server/beeai_chat_server.py` ) expose les fonctionnalités de l’agent via une API HTTP. Il gère trois responsabilités clés :

1.  **Initialisation du LLM** : charge un modèle de langage local via Ollama

```
llm = ChatModel.from_name(os.environ.get(“BEEAI_MODEL”, “ollama:granite3.3:8b”))
```

 

2. **Configuration de l’agent** : crée un RequirementAgent avec des outils et de la mémoire pour gérer le cycle de vie de l’agent

```
    agent = RequirementAgent(
llm=llm,
tools=[ThinkTool(), DuckDuckGoSearchTool(), OpenMeteoTool(), WikipediaTool()],
memory=UnconstrainedMemory(),
description=”An agent that can search the web, check the weather, and think through problems step-by-step.”,
```

 

3. **Configuration du serveur** : expose l’agent via des points de terminaison HTTP conformes à A2A.

```
A2AServer(
config=A2AServerConfig(port=int(os.environ.get(“A2A_PORT”, 9999))),
memory_manager=LRUMemoryManager(maxsize=100)
).register(agent).serve()
```

 

Le serveur expose automatiquement une fiche AgentCard à l’adresse /.well-known/agent-card.json qui décrit les capacités de l’agent et permet de valider les configurations d’agent.

### Le client A2A

Le client A2A (`beeai-a2a-client/beeai_chat_client.py` ) fournit l’interface utilisateur et gère la communication avec le serveur en utilisant le SDK A2A et la bibliothèque asyncio de Python pour un traitement asynchrone des messages.

**Configuration de la connexion** : crée un adaptateur client A2A

```
agent = A2AAgent(
url=os.environ.get(“BEEAI_AGENT_URL”, “http://127.0.0.1:9999”),
memory=UnconstrainedMemory()
)
```

Les`url` paramètre spécifie le point de terminaison du serveur conforme à A2A (par défaut :`http://127.0.0.1:9999` ). Les`memory` paramètre stocke l’historique des conversations localement, ce qui permet au client de conserver le contexte pendant les interactions et de prendre en charge les tâches de longue durée.

**Échange de messages** : envoie des prompts asynchrones et traite les réponses :

```
for prompt in reader:
response = await agent.run(prompt)
# Extract and display response text
```

Les`A2AAgent` est un adaptateur côté client qui abstrait les détails de communication JSON-RPC. Il ne s’agit pas d’un agent autonome ; il convertit simplement les entrées utilisateur en messages conformes à A2A et gère les réponses du serveur, ce qui permet un échange de données et une observabilité transparents.

## Prérequis pour exécuter ce projet

### Configuration requise

Voici la configuration système requise pour exécuter ce projet :

- **Système d’exploitation** : macOS, Linux ou Windows
- **Mémoire (RAM)** : \>= 8 Go (**Recommandé** : 16 Go ou plus pour l’exécution des LLM locaux)
- **Espace disque** : \>= 5 Go d’espace libre (**Recommandé** : 10 Go ou plus pour prendre en charge l’environnement Python et les modèles locaux)
- **Version Python** : \>= 3.11

### Exigences en matière d’outils et de fournisseurs

Avant de vous lancer, voici un aperçu des outils nécessaires pour ce projet :

- **BeeAI** : un kit de développement d’agents open source pour créer des agents d’IA. BeeAI prend en charge plusieurs fournisseurs de LLM, notamment Ollama (utilisé dans ce tutoriel), OpenAI et Anthropic.
- **Ollama** : pour exécuter des LLM locaux afin d’alimenter l’agent d’IA.
- **Protocole A2A** : intégré au framework BeeAI pour permettre une communication structurée entre le client et le serveur.\
- **Terminal ou IDE** : un terminal ou un IDE comme Visual Studio Code (recommandé pour gérer plusieurs terminaux et afficher des journaux).\
- **Environnement virtuel Python** : pour isoler les dépendances pour le client et le serveur.

### Exigences relatives aux fournisseurs de LLM

Ce projet utilise **Ollama** comme fournisseur de modèle pour l’agent d’IA. Suivez ces étapes pour configurer Ollama :

1.  Télécharger et installer Ollama :\
    - Accédez à [Ollama](https://ollama.com/download) et installez l’application correspondant à votre système d’exploitation
2.  Démarrer le serveur Ollama \
    - Ouvrez un terminal et exécutez :\
    `ollama serve`
3.  Extrayez le modèle par défaut (nécessite environ 5 Go d’espace disque) :\
    \
    `ollama pull granite3.3:8b`

**Remarque** : vous pouvez utiliser n’importe quel modèle compatible avec Ollama en paramétrant la`BEEAI_MODEL` variable d’environnement. Consultez la [bibliothèque de modèles Ollama](https://ollama.com/search) pour connaître les modèles disponibles et leurs tailles.

## Étapes

### Étape 1. Cloner le référentiel GitHub

Pour exécuter ce projet, clonez le référentiel GitHub en utilisant https://github.com/IBM/ibmdotcom-tutorials.git comme URL HTTPS. Pour obtenir des étapes détaillées sur le clonage d’un dépôt, consultez la [documentation GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

Ce tutoriel se trouve dans le [répertoire des projets du dépôt](https://github.com/IBM/ibmdotcom-tutorials/tree/main/docs/tutorials/projects).

Dans un terminal, accédez au répertoire de ce tutoriel :

```bash
cd docs/tutorials/projects/a2a_tutorial
```

### Étape 2. Configurer l’environnement de développement

Ce projet nécessite l’exécution simultanée de deux scripts Python distincts, l’un pour le serveur et l’autre pour le client. Vous devez ouvrir deux fenêtres ou onglets de terminal.

Maintenez le terminal actuel ouvert, puis ouvrez un deuxième terminal et assurez-vous que les deux redirigent vers le répertoire de projet approprié (le`a2a_tutorial` répertoire racine).

**Vous utilisez un IDE ?**

Si vous utilisez un IDE tel que Visual Studio Code, vous pouvez utiliser la fonctionnalité Split Terminal pour gérer plusieurs terminaux côte à côte.

Sinon, ouvrez deux fenêtres de terminal indépendantes et accédez dans chacune d’elles au répertoire du projet.

### Étape 3. Créer et activer les environnements virtuels

Les environnements virtuels permettent de séparer et de maintenir les dépendances. Pour séparer les dépendances serveur et client, créez un environnement virtuel pour chaque composant.

**Pour le serveur :**

Accédez au`beeai-a2a-server` répertoire :

```bash
cd beeai-a2a-server
```

Créer un environnement virtuel avec Python 3.11 :

```bash
python3.11 -m venv venv
```

Activez l’environnement virtuel :

```bash
source venv/bin/activate
```

**Remarque pour les utilisateurs de Windows** : utilisez venv\Scripts\Activate pour activer l’environnement virtuel.

**Pour le client :**

Accédez au`beeai-a2a-client` répertoire :

```bash
cd beeai-a2a-client
```

Créer et activer un environnement virtuel :

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### Étape 4. Installer les dépendances

Installez les dépendances requises pour chaque composant en exécutant ce code dans chaque terminal :

```bash
pip install -r requirements.txt
```

Vous pouvez exécuter`pip freeze` dans le terminal pour vérifier que l’environnement est à jour avec les dépendances.

### Étape 5. Démarrer le serveur d’agent A2A

Dans le premier terminal, démarrez le serveur d’agent A2A :

```bash
python beeai_chat_server.py
```

Vous devriez voir :

```
INFO:     Started server process [88159]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9999 (Press CTRL+C to quit)
```

Le serveur écoute désormais les requêtes entrantes de l’application client, prêt à prendre en charge la communication d’agent à agent.

### Étape 6. Démarrer le client A2A

Dans l’autre terminal, démarrez le client A2A :  

```bash
python beeai_chat_client.py
```

Vous êtes invité à saisir vos instructions :

```
Type your message (Ctrl+C to exit):
You:
```

### Étape 7. Interagir avec l’agent

Saisissez un message dans le terminal client et appuyez sur`Enter` . L’agent traite votre requête et vous répond :

```
You: What is the capital of France?
Agent 🤖 : The capital of France is Paris.
```

Dans le terminal du serveur, vous pouvez voir les journaux de protocole A2A montrant la communication avec les notifications push :

```
INFO:     127.0.0.1:49292 - “GET /.well-known/agent-card.json HTTP/1.1” 200 OK
INFO:     127.0.0.1:49294 - “POST / HTTP/1.1” 200 OK
```

La première requête récupère la fiche AgentCard qui décrit les capacités de l’agent. La deuxième requête envoie votre message sous la forme d’un`TextPart` (une unité de contenu textuel dans le message A2A) et reçoit la réponse.

**Remarque** : les sorties des LLM sont probabilistes et peuvent varier chaque fois que vous exécutez le workflow, même avec la même entrée.

### Essayez différentes requêtes

Expérimentez différents types de requêtes pour tester les différents outils de l’agent :

- **Recherche Web** : « Rechercher les dernières actualités sur l’intelligence artificielle »
- **Données météorologiques** : « Quel temps fait-il à Tokyo ? »
- **Wikipédia** : « Parlez-moi de l’informatique quantique »
- **Raisonnement** : « Quelles sont les trois raisons pour lesquelles le ciel est bleu ? »

### Voir la fiche AgentCard

Accédez à  dans votre navigateur pour afficher la fiche`RequirementAgent` AgentCard.

```
{
“capabilities”: {
“streaming”: true
},
“defaultInputModes”: [
“text”
],
“defaultOutputModes”: [
“text”
],
“description”: “An agent that can search the web, check the weather, and think through problems step-by-step.”,
“name”: “RequirementAgent”,
“preferredTransport”: “JSONRPC”,
“protocolVersion”: “0.3.0”,
“skills”: [
{
“description”: “An agent that can search the web, check the weather, and think through problems step-by-step.”,
“id”: “RequirementAgent”,
“name”: “RequirementAgent”,
“tags”: []
}
],
“url”: “http://localhost:9999”,
“version”: “1.0.0”
}
```

Ce document JSON décrit :

- Le nom de l’agent (RequirementAgent) et une brève description de ses capacités.
- Les protocoles de communication et formats de message pris en charge
- Toutes les exigences ou contraintes

Cette fiche AgentCard permet aux clients conformes au protocole A2A de découvrir l’agent et d’interagir avec lui sans connaître les détails de son implémentation au préalable.

## Conclusion

Dans ce tutoriel, vous avez créé un système de chat en utilisant un serveur conforme au protocole A2A qui a présenté une interface structurée pour la communication client-agent. En séparant la couche de messagerie de la logique interne, le protocole Agent2Agent permet aux équipes de mettre à jour les capacités des agents, d’échanger des modèles ou de modifier les configurations des outils sans modifier le code client. Cette flexibilité est particulièrement précieuse lorsque vous coordonnez les tâches requises en entrée, pour suivre l’état des tâches ou pour traiter chaque opération comme une unité de travail distincte.

A2A fonctionne en définissant un format de message commun que tout composant conforme peut comprendre, ce qui permet aux agents autonomes de collaborer avec d’autres agents. La spécification du protocole définit comment les messages sont structurés au format JSON-RPC et enrichis de métadonnées pour assurer la cohérence et la clarté entre les interactions.

Ce tutoriel s’appuie sur les exemples de base fournis par le [référentiel d’exemples A2A](https://github.com/a2aproject/a2a-samples). Pour plus d’informations sur l’implémentation initiale, reportez-vous au fichier readme du référentiel, qui fournit plus de contexte et d’exemples pour la création de systèmes conformes à A2A.

Pour les déploiements réels, les serveurs A2A peuvent mettre en œuvre des mécanismes d’authentification pour sécuriser les points de terminaison des agents, utiliser les événements envoyés par le serveur pour les réponses en streaming et évoluer pour gérer les workflows de production. En suivant ce workflow, vous avez vu comment un client de ligne de commande peut interagir avec un agent d’IA via un protocole standardisé, permettant à l’agent d’IA de coordonner plusieurs outils et de fournir des réponses contextuelles. Cette approche démontre la puissance de l’A2A pour permettre la mise en place de systèmes d’IA maintenables, évolutifs et flexibles.

## Arrêter le système

Une fois vos expérimentations avec le système terminées, suivez ces étapes pour arrêter proprement tous les composants en cours d’exécution :

### Arrêtez chaque serveur en cours d’exécution

Dans chaque fenêtre de terminal, appuyez sur Ctrl+C pour mettre fin au processus en cours.

Vous devriez obtenir une sortie comme celle-ci :

```
INFO:     Shutting down
INFO:     Finished server process
```

### Si le serveur est bloqué pendant un arrêt

Si le serveur ne répond plus ou est bloqué à l’arrêt, vous pouvez forcer l’arrêt :

**Recherchez l’identifiant du processus (PID) :**

```
ps aux | grep python
```

Identifiez le PID du processus que vous essayez d’arrêter.

**Mettez fin au processus :**

```
kill -9 <PID>
```

Répétez ce processus pour chaque serveur si nécessaire.

Et voilà. Vous avez réussi à exécuter un système de chat complet conforme au protocole A2A.
