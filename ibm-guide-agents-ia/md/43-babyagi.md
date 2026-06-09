> Source : https://www.ibm.com/fr-fr/think/topics/babyagi

# Qu’est-ce que BabyAGI ?

BabyAGI est un cadre d’[agent autonome](https://www.ibm.com/fr-fr/think/topics/agentic-automation) conçu pour générer et exécuter une séquence de tâches selon un objectif fourni par l’utilisateur. Partagé publiquement par Yohei Nakajima en 2023, BabyAGI orchestre une boucle de création, d’exécution et de priorisation des tâches à l’aide d’un [grand modèle de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models) et d’un magasin de mémoire vectorielle. 

L’implémentation standard est un script [Python](https://developer.ibm.com/languages/python/) qui utilise les modèles GPT d’OpenAI via une [API](https://www.ibm.com/fr-fr/think/topics/api), une [base de données vectorielle](https://www.ibm.com/fr-fr/think/topics/vector-database) (généralement Pinecone) pour la mémoire, et le cadre d’agent [LangChain pour structurer les rôles des agents IA.](https://www.ibm.com/fr-fr/think/topics/langchain) La base de données vectorielle enregistre les résultats des tâches sous forme d’embeddings utilisés pour la recherche contextuelle, tandis que le LLM alimente le raisonnement de l’agent et la logique des tâches.1

En tant qu’[agent IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) autonome, BabyAGI procède à une itération continue en utilisant les résultats des tâches accomplies pour informer les nouvelles tâches, redéfinir les priorités de la liste des tâches et exécuter des sous-tâches. Le processus se poursuit jusqu’à ce que la file d’attente des tâches soit épuisée ou qu’une condition d’arrêt soit atteinte.

## Comment fonctionne BabyAGI ?

BabyAGI utilise un [workflow d’IA](https://www.ibm.com/fr-fr/think/topics/ai-workflow) répétitif en trois étapes : 

1.  **Exécution des tâches** : l’agent d’exécution exécute une tâche en utilisant le contexte de la base de données vectorielle et l’objectif de haut niveau comme guide.\
     

2.  **Création de tâches** : en fonction du résultat de la tâche exécutée, l’agent de création de tâches génère des tâches de suivi qui correspondent à l’objectif initial. \
     

3.  **Priorisation des tâches** : un agent de priorisation réorganise toutes les tâches en attente, y compris les nouvelles, en fonction des dépendances et de la pertinence par rapport à l’objectif. 

La boucle se répète jusqu’à ce qu’il ne reste plus aucune tâche ou qu’une autre condition de fin soit remplie.

## Fonctionnalités principales de BabyAGI

BabyAGI se compose de plusieurs modules architecturaux de base, qui fonctionnent ensemble pour faciliter la génération, la priorisation et l’exécution automatisées des tâches. Ces composants comprennent :

- LLM\
   

- Base de données vectorielle\
   

- Liste des tâches\
   

- Agent d’exécution des tâches\
   

- Agent de création de tâches\
   

- Agent de priorisation des tâches

### LLM

Le composant LLM de BabyAGI est l’orchestrateur central du système agentique. Ce modèle d’[intelligence artificielle (IA)](https://www.ibm.com/fr-fr/think/topics/artificial-intelligence) agit comme un directeur de haut niveau. Il reçoit le prompt de l’utilisateur et l’évalue grâce au [traitement automatique du langage naturel (TAL)](https://www.ibm.com/fr-fr/think/topics/natural-language-processing) pour en identifier l’objectif. Il alimente également les agents qui créent, exécutent et priorisent les tâches.

BabyAGI s’appuie généralement sur GPT-4 d’OpenAI. Les trois agents du système BabyAGI réalisent un prompt engineering précis pour guider le comportement de GPT-4 dans ses rôles agentiques.

### Base de données vectorielle

Le composant de base de données vectorielle de BabyAGI stocke les enregistrements et les résultats des tâches terminées et constitue la mémoire de l’agent. BabyAGI peut utiliser les résultats de la première tâche pour informer la deuxième tâche et itérer ce processus au fur et à mesure qu’il progresse dans la liste des tâches.

Les bases de données vectorielles stockent les données sous forme de représentations mathématiques appelées embeddings. Les points de données plus proches les uns des autres dans l’espace vectoriel à haute dimension sont considérés comme plus proches sur le plan sémantique. BabyAGI utilise la recherche sémantique pour trouver les informations pertinentes dans la base de données.

L'implémentation canonique utilise Pinecone, mais des magasins de vecteurs alternatifs tels que Facebook AI Similarity Search (FAISS) de Meta et Chroma sont parfois utilisés dans des variantes ou des forks. FAISS et Chroma sont [open source](https://www.ibm.com/fr-fr/think/topics/open-source), tandis que Pinecone, comme de nombreux produits OpenAI, ne l’est pas.

### Liste des tâches

La liste ou file d’attente des tâches est une liste hiérarchisée de sous-tâches découlant de l’objectif de haut niveau et de la tâche initiale. Au fur et à mesure que l’agent d’exécution accomplit les tâches, ces résultats sont téléchargés dans la base de données vectorielle. En fonction des résultats de ces tâches, la liste des tâches peut changer à mesure que les priorités sont ajustées et que de nouvelles tâches sont ajoutées.

### Agent d’exécution des tâches

L’agent d’exécution des tâches utilise le LLM et les données de la base de données vectorielle pour exécuter les tâches de la liste. Diverses techniques de recherche sémantique sont utilisées pour trouver les informations pertinentes dans la base de données. Une fois la tâche terminée, le système crée un nouvel embedding et stocke l’enregistrement dans la base de données.

### Agent de création de tâches

L’agent de création utilise l’objectif général et les résultats des tâches précédentes pour générer les tâches suivantes du [workflow](https://www.ibm.com/fr-fr/think/topics/workflow). Au lieu de suivre un workflow prédéterminé, le processus continu de génération de tâches permet au système d’itérer sur les résultats antérieurs et d’apprendre de manière dynamique.

### Agent de priorisation des tâches

L’agent de priorisation des tâches gère les tâches en réordonnant et en organisant régulièrement leur liste. Son travail consiste à hiérarchiser les sous-tâches en fonction des résultats des tâches précédentes et des relations entre les nouvelles tâches et l’objectif de haut niveau. L’agent de priorisation prend également en compte les dépendances entre les tâches : si une tâche doit être achevée afin qu’une autre devienne possible.

## Comment utiliser BabyAGI

BabyAGI est une bibliothèque Python dont l’utilisation requiert quelques connaissances en matière de codage Python. Cependant, le processus de configuration est relativement simple :

1.  Installez Python et Git. Téléchargez le référentiel GitHub BabyAGI à partir de *github.com.\
     *

2.  Ouvrez le répertoire avec BabyAGI et installez toutes les dépendances en utilisant la commande *pip install.*\
     

3.  Créez un *fichier .env* et copiez-y l’exemple de fichier *.env*.\
     

4.  Ajoutez une clé d’API OpenAI et une clé d’API Pinecone au *fichier.env* que vous avez créé. Si nécessaire, créez d’abord un compte OpenAI et obtenez votre clé d’API.\
     

5.  Définissez l’objectif en modifiant la valeur OBJECTIVE. Ensuite, proposez une tâche initiale.\
     

6.  Enregistrez et fermez le fichier .env.\
     

7.  Entrez la commande *python babyagi.py* pour exécuter l’agent.

## Cas d’utilisation de BabyAGI

BabyAGI est plus un bac à sable éducatif qu’une application de production prête pour une utilisation standard de l’[IA agentique](https://www.ibm.com/fr-fr/think/topics/ai-agent-use-cases). Les passionnés du machine learning (ML) et de l’IA agentique ont utilisé BabyAGI pour découvrir les agents de tâches autonomes et le raisonnement en chaîne de pensée avec des LLM.

### BabyAGI et AutoGPT

BabyAGI est souvent comparé à [AutoGPT](https://www.ibm.com/fr-fr/think/topics/autogpt), un autre cadre open source pour les agents autonomes construits sur des LLM. Les deux sont des outils d’IA conçus pour automatiser les objectifs multi-étapes en combinant un LLM avec l’utilisation de mémoire et d’outils.

BabyAGI exécute une boucle compacte qui crée, exécute et priorise les tâches à l’aide d’une base de données vectorielle pour la mémoire à court et à long terme. AutoGPT fournit un cadre riche en fonctionnalités pour la décomposition des objectifs, l’intégration des outils et l’utilisation d’API externes.

Alors que BabyAGI est utilisé surtout comme outil de recherche et bac à sable, AutoGPT peut automatiser les tâches à plus grande échelle.

## BabyAGI est-il une intelligence artificielle générale (AGI) ?

Malgré son nom, BabyAGI n’est pas un exemple [d’intelligence artificielle générale (AGI).](https://www.ibm.com/fr-fr/think/topics/artificial-general-intelligence) L’AGI est une IA hypothétique dotée de capacités de réflexion et de raisonnement comparables à celles de l’humain. A ce jour, l’AGI est encore une notion théorique. Aucune application d’IA, ni même BabyAGI, n’a atteint un tel niveau de complexité.

Comme beaucoup d’autres applications d’IA générative, BabyAGI utilise une modélisation statistique avancée pour prédire le résultat le plus probable pour toute entrée donnée. Il ne comprend pas, n’apprend pas et ne réfléchit pas non plus comme un humain.

## Qu’est-ce que BabyAGI 2 ?

En 2024, Nakajima a lancé BabyAGI 2, une variante expérimentale qui utilise un cadre *functionz* pour stocker les fonctions et les métadonnées associées dans une base de données. L’agent peut charger, exécuter et mettre à jour les fonctions à l’aide de métadonnées au fur et à mesure de sa création.
