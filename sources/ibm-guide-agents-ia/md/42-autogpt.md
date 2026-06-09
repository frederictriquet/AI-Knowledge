> Source : https://www.ibm.com/fr-fr/think/topics/autogpt

# Qu’est-ce qu’AutoGPT ?

AutoGPT est une plateforme d’intelligence artificielle (IA) open source qui permet aux utilisateurs d’automatiser des projets multi-étapes et des workflows complexes à l’aide d’agents d’IA basés sur le grand modèle de langage (LLM) GPT-4 d’OpenAI. AutoGPT applique le traitement automatique du langage naturel (NLP) pour comprendre les objectifs de haut niveau de l’utilisateur, décomposer la tâche globale en sous-tâches, puis automatiser ces sous-tâches dans un workflow à l’aide de GPT-4o mini, GPT-4 et GPT-3.5.

AutoGPT a été lancé le 30 mars 2023 par son créateur Toran Bruce Richards, fondateur de la société de jeux vidéo et de développement logiciel Significant Gravitas. Il se connecte au modèle GPT (Generative Pretrained Transformer) d’OpenAI et permet d’automatiser des projets qui nécessiteraient autrement de nombreux prompts humains à donner à un chatbot comme ChatGPT.

## Qu’est-ce qu’un agent IA ?

Les agents d’IA sont un type de technologie d’IA autonome capable d’exécuter des tâches auto-déterminées sans intervention humaine afin d’atteindre un objectif prédéfini. Une fois le prompt défini par l’utilisateur, l’agent d’IA détermine la séquence optimale d’étapes à suivre pour accomplir la tâche assignée. Les agents utilisent les résultats de chaque étape pour informer la suivante et structurer l’ensemble du workflow.

AutoGPT est un exemple de cadre multi-agent : une plateforme d’IA qui crée et coordonne une équipe d’agents d’IA autonomes collaborant pour atteindre un objectif donné. Parmi les autres plateformes multi-agents de premier plan, citons crewAI, LangGraph et AutoGen.

Les agents conversationnels sont des agents d’IA qui interagissent avec les utilisateurs humains via une interface conversationnelle. Certains cadres multi-agents offrent des fonctions d’agent conversationnel, mais ce n’est pas systématique.

## Comment fonctionne AutoGPT ?

AutoGPT traite le prompt utilisateur global et crée des agents d’IA pour l’exécuter. Ces agents décomposent les tâches complexes en une séquence de sous-tâches, génèrent eux-mêmes les prompts nécessaires pour les accomplir, et appliquent des données en temps réel pour s’améliorer de manière itérative.

En plus de GPT-4o mini, GPT-4 et GPT-3.5, AutoGPT peut également utiliser des plug-ins pour accéder à Internet et à d’autres applications afin d’intégrer des actualités en temps réel et d’autres données dans son workflow. AutoGPT peut stocker les données utilisateur sous forme de fichiers et dispose d’une mémoire à court et long terme (grâce à l’utilisation de bases de données vectorielles), ce qui lui permet de revenir sur des projets antérieurs.

Voici à quoi ressemble un workflow AutoGPT type :

1.  Entrée utilisateur

2.  Création de tâches

3.  Hiérarchisation des tâches

4.  Exécution des tâches

5.  Évaluation de l’avancement et amélioration du workflow

6.  Finalisation du projet

### Étape 1 : Entrée utilisateur

Les utilisateurs fournissent à AutoGPT des objectifs explicites, accompagnés de tout contexte nécessaire ou de toute contrainte. Par exemple, lorsqu’AutoGPT est utilisé comme outil IA de développement commercial, il peut identifier de nouveaux prospects, créer un plan pour les réseaux sociaux, esquisser une saison d’épisodes de podcast, ou encore déboguer le code d’un site web.

### Étape 2 : Création de tâches

AutoGPT crée un agent de création de tâches qui utilise le traitement automatique du langage naturel pour comprendre l’objectif de haut niveau de l’utilisateur. Ensuite, cet agent d’IA décompose l’objectif en une séquence de tâches.

### Étape 3 : Hiérarchisation des tâches

Un agent de hiérarchisation des tâches évalue la liste générée par l’agent de création pour déterminer si les tâches peuvent raisonnablement être réalisées dans l’ordre prévu. Cela évite qu’AutoGPT ne crée des tâches dépendantes de résultats situés plus loin dans le workflow.

### Étape 4 : Exécution des tâches

Les agents d’exécution des tâches utilisent GPT-4o mini, GPT-4, GPT-3.5, Internet et d’autres applications pour atteindre leurs objectifs. AutoGPT génère automatiquement les prompts nécessaires pour ses agents d’exécution dans le cadre du processus de création du workflow. Ces prompts sont transmis au GPT et combinés à des données en temps réel pour produire les résultats attendus.

### Étape 5 : Évaluation de l’avancement et amélioration du workflow

Les agents impliqués dans le projet communiquent en temps réel, transmettant leurs données à l’agent de création de tâches afin que ce dernier puisse ajuster les tâches suivantes ou générer une nouvelle liste. C’est ainsi qu’AutoGPT itère chaque étape pour améliorer son workflow tout en poursuivant l’objectif initial de l’utilisateur.

### Étape 6 : Finalisation du projet

Si AutoGPT parvient à accomplir la tâche assignée, il présente les résultats à l’utilisateur. AutoGPT reste un outil expérimental et sa fiabilité n’est pas garantie. Il peut se laisser distraire par des tâches non essentielles, halluciner puis se baser sur ces hallucinations dans les tâches suivantes, mal interpréter des données, mal comprendre l’utilisateur, et finir par échouer ou s’arrêter.

## Cas d’utilisation d’AutoGPT

AutoGPT peut accomplir toutes les tâches dont ChatGPT est capable, mais avec l’objectif de renvoyer des résultats plus rapidement en automatisant le processus de génération des prompts. En théorie, c’est un outil puissant, capable de résoudre des tâches complexes et des défis de haut niveau. Ses capacités en matière d’automatisation intelligente, d’analyse de données, de résumé de documents, d’exécution automatisée de tâches et de génération de texte ouvrent la voie à un large éventail de cas d’utilisation potentiels :

- Études et analyses de marché
- Développement de produits
- Analyse financière
- Optimisation du marketing
- Assistance virtuelle
- Optimisation de la chaîne d’approvisionnement
- Optimisation des ventes

### Études et analyses de marché

AutoGPT peut naviguer sur Internet pour analyser des articles d’actualité ou des contenus issus des réseaux sociaux afin d’identifier les tendances ou les perturbations du marché. Il peut ensuite résumer ses découvertes et présenter un rapport aux dirigeants et aux parties prenantes. Les fondateurs de start-ups peuvent évaluer le paysage de leur secteur et élaborer des plans d'affaires concrets.

### Développement de produits

Grâce à l’analyse des sentiments dans les avis clients et le contenu des réseaux sociaux, AutoGPT peut offrir aux équipes produit une vue en temps réel de ce que ressentent leurs clients. Les chefs de projet peuvent prioriser les mises à jour pour résoudre les problématiques les plus urgentes des utilisateurs, tandis que les développeurs peuvent tirer parti de la capacité d’AutoGPT à déboguer du code et créer des tutoriels pour leurs produits.

### Analyse financière

AutoGPT peut analyser les tendances du marché et générer des rapports d’investissement, permettant aux dirigeants de prendre des décisions plus rapidement en réponse aux événements réels du marché. Les analystes peuvent également exploiter les capacités de traitement des données et d’accès à Internet d’AutoGPT pour créer des évaluations des risques basées à la fois sur des données historiques et les comportements actuels du marché.

### Optimisation du marketing

Les équipes de marketing numérique peuvent utiliser AutoGPT pour analyser les campagnes concurrentes et générer des informations afin d’éclairer leur propre travail. En parallèle, les capacités de génération de texte d’AutoGPT lui permettent d’effectuer des tâches de création de contenu. Il est recommandé de relire et d’éditer tout contenu généré par l’IA avant publication, afin de garantir son exactitude, de maintenir les standards de qualité et d’éviter toute violation de propriété intellectuelle.

### Assistance virtuelle

AutoGPT peut agir comme un assistant virtuel, offrant une aide supérieure à celle des chatbots de support classiques. Il peut également aider les utilisateurs individuels à gérer leur temps, programmer des rendez-vous ou planifier des voyages.

### Optimisation de la chaîne d’approvisionnement

AutoGPT peut analyser les tendances du marché pour prévoir la demande et aider les entreprises à allouer leurs ressources efficacement. Les entreprises peuvent également intégrer des données de chaîne d’approvisionnement dans AutoGPT, comme les quantités en stock, les délais de traitement ou de livraison, afin d’identifier les goulets d’étranglement et découvrir des opportunités d’amélioration.

### Optimisation des ventes

Les entreprises disposent de quantités quasi illimitées de données sur leurs clients. Les équipes commerciales peuvent utiliser AutoGPT pour analyser les profils clients, créer des stratégies de fidélisation efficaces et identifier les prospects les plus susceptibles de se convertir.

## AutoGPT est-il meilleur que ChatGPT ?

L’avantage principal d’AutoGPT par rapport au chatbot d’IA ChatGPT est qu’il peut générer ses propres prompts et les exécuter automatiquement sans intervention humaine. À l’inverse, ChatGPT est un exemple d’IA conversationnelle conçue pour entretenir un dialogue continu avec son utilisateur, mais qui ne peut pas générer seule ses propres prompts en réponse à ses propres sorties.

AutoGPT offre plusieurs avantages par rapport à ChatGPT :

- Automatisation des prompts

- Accès aux données en temps réel

- Gestion de la mémoire

### Automatisation des prompts

Chaque fois qu’un utilisateur interagit avec ChatGPT, le service répond à l’invite, puis attend que l’utilisateur fournisse la suivante pour poursuivre l’échange. AutoGPT automatise cet échange, en générant lui-même les prompts suivants dans le but d’atteindre l’objectif général initial défini par l’utilisateur.

### Accès aux données en temps réel

AutoGPT a accès à des informations en temps réel, tandis que les connaissances de ChatGPT sont limitées à la date d’arrêt des connaissances du modèle GPT utilisé. AutoGPT peut se connecter à Internet via des plug-ins, rechercher des données réelles et intégrer ces informations dans ses réponses et les prompts qui en découlent.

### Gestion de la mémoire

La mémoire de ChatGPT est limitée à la fenêtre de contexte du modèle GPT : c’est-à-dire le nombre de tokens que le modèle peut traiter avant de perdre le fil du contexte. Ces fenêtres imposent une limite stricte quant à la taille et à la complexité des prompts. Les utilisateurs peuvent connecter AutoGPT à des bases de données vectorielles pour lui permettre une gestion de la mémoire à long terme, lui donnant la capacité d’apprendre dans le temps, de se souvenir des préférences de l’utilisateur, de rappeler des processus antérieurs et de faire référence à du contenu pertinent.

## AutoGPT est-il gratuit ?

AutoGPT n’est pas gratuit. Bien qu’AutoGPT soit librement accessible sur GitHub, son utilisation nécessite une clé API OpenAI, disponible via un compte OpenAI payant. Au moment de la publication, la tarification d’OpenAI dépend du modèle utilisé ainsi que de la taille de la fenêtre de contexte sélectionnée.

Les prompts envoyés à GPT via AutoGPT comptent dans le total de tokens utilisés par l’utilisateur, à la fois pour les entrées et les sorties. L’usage continu d’AutoGPT pour des projets à grande échelle ou en production peut rapidement entraîner des coûts substantiels.

L’installation et la configuration d’AutoGPT sont également complexes : les utilisateurs doivent télécharger Git et Python avant d’installer et d’auto-héberger AutoGPT dans un environnement de développement tel que Docker. D’autres créateurs ont développé des solutions pour simplifier l’utilisation d’AutoGPT. Des applications récentes comme AgentGPT et GodMode permettent d’accéder à AutoGPT via des interfaces navigateur simplifiées.

## AutoGPT est-il un exemple d’intelligence artificielle générale (IAG) ?

AutoGPT n’est pas une intelligence artificielle générale (IAG). C’est un agent d’IA qui utilise l’IA générative pour résoudre des problèmes et accomplir des tâches complexes. Comme d’autres outils d’IA générative et modèles de machine learning, AutoGPT utilise des algorithmes statistiques pour prédire les résultats les plus probables à partir de données en entrée : il ne pense ni ne raisonne pas de la même manière qu’un humain. L’IAG reste un concept théorique selon lequel une IA serait pleinement capable de raisonnement de type humain.

Même si la capacité d’AutoGPT à concevoir automatiquement des plans d’action et à les exécuter est impressionnante, la plateforme est encore loin d’égaler une intelligence humaine. Et bien que les réseaux neuronaux s’inspirent de la structure du cerveau humain, nous sommes encore très loin de comprendre, et encore plus de reproduire, son fonctionnement.
