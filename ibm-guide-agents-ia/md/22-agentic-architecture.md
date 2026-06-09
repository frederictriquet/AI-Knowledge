> Source : https://www.ibm.com/fr-fr/think/topics/agentic-architecture

# Qu’est-ce qu’une architecture agentique ?

L’architecture agentique fait référence à la structure et à la conception des frameworks d’intelligence artificielle (IA) agentique. Une architecture agentique est celle qui façonne l’espace virtuel et la structure du workflow pour automatiser les modèles d’IA au sein d’un système d’IA agentique.

L’IA agentique est un système ou un programme qui utilise des agents d’IA pour exécuter des tâches de manière autonome au nom d’un utilisateur ou d’un autre système. L’architecture agentique fonctionne de manière à prendre en charge et réguler le comportement des agents alimentés par l’IA travaillant dans un système d’IA générative. Les systèmes d’IA agentique exigent que leurs agents soient adaptables et capables de naviguer dans des environnements dynamiques afin d’atteindre les résultats escomptés.\
\
Ce modèle n’est pas si différent de la psychologie humaine : la fonction d’agent fait référence à la capacité de faire intentionnellement en sorte que quelque chose se produise en fonction de ses actions.[1](https://www.ibm.com/fr-fr/think/topics/agentic-architecture#f1) Pour obtenir les résultats souhaités, il faut faire appel à la planification, à l’action, à la mémoire et à la réflexion. Ces caractéristiques correspondent à celles des agents d’IA modernes, utilisés dans des frameworks mono-agents et multi-agents.\
 \
Les progrès des algorithmes de machine learning (ML) et des grands modèles de langage (LLM) tels que GPT d’OpenAI ont favorisé le développement des agents d’IA. L’objectif de l’architecture agentique est de fournir une structure permettant à un LLM d’automatiser les tâches complexes.

Le comportement autonome ou de prise de décision d’un agent d’IA dépend de l’infrastructure qui le soutient. L’architecture agentique est conçue pour s’adapter aux environnements dynamiques, améliorant ainsi l’interopérabilité.\
\
Par exemple, les agents peuvent interagir avec divers formats et sources de données, interfaces de programmation des applications (API) ou systèmes. Ce comportement adaptable permet aux agents de prendre des décisions éclairées.

## Fonctionnement de l’architecture agentique

L’architecture d’IA agentique doit être structurée en composants qui répondent aux caractéristiques essentielles de la fonction d’agent : intentionnalité (planification), prévoyance, auto-réactivité et auto-réflectivité.[2](https://www.ibm.com/fr-fr/think/topics/agentic-architecture#f2) Ces caractéristiques confèrent aux agents d’IA une autonomie qui leur permet de fixer des objectifs, de planifier, de surveiller leurs performances et de réfléchir pour atteindre leur objectif spécifique.\
 \
La technologie agentique utilise un outil de backend pour recueillir des informations à jour, optimise les workflows complexes et génère automatiquement des tâches pour atteindre des objectifs complexes.\
\
Au fur et à mesure de son fonctionnement, l’agent autonome s’adapte aux préférences de l’utilisateur au fil du temps, offrant une expérience plus personnalisée et fournissant des réponses plus détaillées. Ce processus d’appel d’outil peut s’exécuter sans entrée humaine, déverrouillant ainsi des possibilités plus larges pour les applications d’IA réelles.

## Agentique vs non agentique

Les architectures agentiques prennent en charge le comportement agentique au sein des agents d’IA. Les agents d’IA sont des systèmes adaptables pilotés par des modèles de machine learning qui peuvent interagir avec des environnements externes et utiliser des outils pour atteindre des objectifs spécifiques. Tous les agents d’IA ne sont pas agentiques. Cela dépend de la complexité et des capacités du framework ou du système.\
\
L’architecture agentique permet aux agents d’IA d’agir avec un certain degré d’autonomie et de prendre des décisions basées sur des objectifs sans avoir besoin constamment d’entrée humaine.[3](https://www.ibm.com/fr-fr/think/topics/agentic-architecture#f3) Les agents d’IA autonomes n’ont besoin que de peu ou pas d’intervention humaine pour mener à bien leurs tâches spécifiques.

Dans les architectures non agentiques, les LLM sont capables d’effectuer des tâches singulières ou linéaires.[4](https://www.ibm.com/fr-fr/think/topics/agentic-architecture#f4) La fonction du modèle d’IA dans une architecture non agentique est de fournir des sorties basées sur les entrées et le contexte.\
\
En l’absence d’une orchestration explicite, les LLM ne peuvent pas conserver les nouvelles informations en temps réel et rencontrent souvent des difficultés avec des problèmes complexes en raison de leur contexte limité. Par exemple, l’analyse sémantique, les chatbots et la génération de texte sont des applications d’IA courantes qui ne nécessitent pas de workflows agentiques complexes.

L’architecture d’agent idéale dépend des exigences de l’application et du cas d’utilisation. Les systèmes mono-agents excellent dans la résolution de problèmes ciblés et spécifiques, en agissant essentiellement comme des résolveurs de problèmes individuels.\
\
Cependant, certains défis peuvent nécessiter l’expertise unique d’un agent spécialisé, tandis que d’autres pourraient tirer profit d’une approche impliquant plusieurs agents travaillant ensemble en équipe.

## Types d’architectures agentiques

Le tableau fournit une comparaison claire des différents types de systèmes d’architecture d’agent d’IA : vertical, horizontal et hybride. Il met en évidence leurs structures, leurs fonctionnalités principales, leurs forces, leurs faiblesses et leurs cas d’utilisation afin de déterminer l’approche la plus appropriée pour des tâches variées. 

### **Architectures mono-agents**

Une architecture à mono-agent présente une seule entité autonome prenant des décisions centralisées au sein d'un environnement.

- **Structure\
  \**
  - Une architecture mono-agent est un système dans lequel un agent d’IA unique fonctionne de manière indépendante pour percevoir son environnement, prendre des décisions et prendre des mesures pour atteindre un objectif.\
    \
- **Fonctionnalités principales\
  \**
  - **Autonomie** : l’agent fonctionne de manière indépendante, sans nécessiter d’interaction avec d’autres agents.\
     
- **Points forts\
  \**
  - **Simplicité** : plus facile à concevoir, à développer et à déployer que les systèmes multi-agents. Nécessite moins de ressources puisqu’il n’est pas nécessaire de gérer plusieurs agents ou protocoles de communication.
  - **Prévisibilité** : plus facile à déboguer et à surveiller, car l’agent fonctionne indépendamment.
  - **Rapidité** : aucune négociation ni recherche de consensus nécessaire entre plusieurs agents.
  - **Coût** : moins coûteux à gérer et à mettre à jour par rapport aux architectures multi-agents complexes. Réduction des problèmes d’intégration lors du déploiement dans les applications d’entreprise.\
     
- **Points faibles\
  \**
  - **Évolutivité limitée** : un agent unique peut devenir un goulot d’étranglement lorsqu’il gère des tâches complexes ou à volume élevé.
  - **Rigidité** : difficulté avec les tâches qui nécessitent des workflows en plusieurs étapes ou une coordination entre différents domaines.
  - **Étroit** : généralement conçu pour une fonction ou un domaine spécifique.\
     
- **Meilleurs cas d’utilisation\
  \**
  - **Chatbots simples** : les chatbots peuvent fonctionner de manière indépendante, ne nécessitent pas de coordination avec d’autres agents et fonctionnent bien dans les interactions utilisateur structurées et autonomes.
  - **Systèmes de recommandation** : les recommandations de contenu personnalisées, telles que celles proposées par les services de streaming, sont assez simples pour une architecture mono-agent.

### Architectures multi-agents

Les architectures multi-agents vont au-delà des capacités d’IA des configurations mono-agents traditionnelles, et offrent plusieurs avantages uniques. Chaque agent est spécialisé dans un domaine spécifique, tel que l'analyse des performances, la prévention des blessures ou les études de marché, tout en collaborant de manière fluide pour résoudre des problèmes complexes.\
\
Les agents adaptent leurs rôles en fonction de l’évolution des tâches, ce qui permet de garantir flexibilité et réactivité dans des scénarios dynamiques.

Les systèmes multi-agents sont plus flexibles. Un agent peut utiliser le traitement automatique du langage naturel (NLP), un autre peut se spécialiser dans la vision par ordinateur. Un agent peut utiliser la génération augmentée par récupération (RAG) pour extraire des données à partir d’ensembles de données externes.

Il existe de nombreux fournisseurs de frameworks multi-agents tels que crewAI, basé sur Python, qui fonctionne en plus de LangChain. Parmi les autres solutions d’IA, DeepWisdom propose MetaGPT, un workflow utilisant un framework guidé par des procédures opérationnelles standard.

**Architectures d’IA verticales**

- **Structure\
  \**
  - Dans une architecture verticale, un agent leader supervise les sous‑tâches et les décisions, les agents rendant compte pour un contrôle centralisé.[5](https://www.ibm.com/fr-fr/think/topics/agentic-architecture#f5) Les agents IA hiérarchique connaissent leur rôle et rendent compte à d’autres agents ou les supervisent en conséquence.\
     
- **Fonctionnalités principales\
  \**
  - **Hiérarchie** : les rôles sont clairement définis.
  - **Communication centralisée** : les agents rendent compte au leader.\
     
- **Points forts\
  \**
  - **Efficacité des tâches** : idéal pour les workflows séquentiels.
  - **Responsabilité claire** : le leader aligne les objectifs.

<!-- -->

- **Points faibles**

  - **Goulets d’étranglement** : la dépendance à l’égard du leader peut ralentir les progrès.

  - **Point de défaillance unique** : vulnérable face aux problèmes liés au leader.

<!-- -->

- **Meilleurs cas d’utilisation**

  - **Automatisation du workflow** : approbations à plusieurs étapes.

  - **Génération de document** : sections supervisées par un leader.

**Architectures d’IA horizontales**

- **Structure**

  - **Modèle de collaboration entre pairs** : les agents travaillent sur un pied d’égalité dans un système décentralisé, collaborant librement pour résoudre des tâches.[6](#f6)

<!-- -->

- **Fonctions principales**

  - **Collaboration distribuée** : tous les agents partagent des ressources et des idées.

  - **Décisions décentralisées** : prise de décision pilotée par le groupe pour une autonomie collaborative.

<!-- -->

- **Points forts**

  - **Résolution dynamique des problèmes** : favorise l’innovation.

  - **Traitement parallèle** : les agents travaillent simultanément sur des tâches.

<!-- -->

- **Points faibles**

  - **Problèmes de coordination** : une mauvaise gestion peut engendrer des inefficacités.

  - **Décisions plus lentes** : trop de délibérations.

<!-- -->

- **Meilleurs cas d’utilisation**

  - **Brainstorming** : générer des idées diverses.

  - **Résolution de problèmes complexes** : relever les défis interdisciplinaires.

**Architectures d’IA hybrides**

- **Structure**

  - Combine un leadership structuré avec une flexibilité collaborative ; changements de direction en fonction des exigences de la tâche.

<!-- -->

- **Fonctions principales**

  - **Leadership dynamique** : le leadership s’adapte à la phase de la tâche.

  - **Leadership collaboratif** : les leaders impliquent ouvertement leurs pairs.

<!-- -->

- **Points forts**

  - **Polyvalence** : combine les forces des deux modèles.

  - **Adaptabilité** : gère les tâches nécessitant à la fois structure et créativité.

<!-- -->

- **Points faibles**

  - **Complexité** : équilibrer les rôles de direction et la collaboration nécessite des mécanismes robustes.

  - **Gestion des ressources** : plus exigeante.

<!-- -->

- **Meilleurs cas d’utilisation**

  - **Tâches polyvalentes** : planification stratégique ou projets d’équipe.

  - **Processus dynamiques** : équilibre entre les demandes structurées et créatives.

## Frameworks agentiques

Les frameworks agentiques font référence aux architectures de conception ou aux modèles qui définissent comment les agents (artificiels ou naturels) peuvent effectuer des tâches, prendre des décisions et interagir avec leur environnement de manière autonome et intelligente. Ces cadres fournissent la structure et les directives sur la manière dont les agents opèrent, raisonnent et s’adaptent à divers contextes.

### Architectures réactives\

Les architectures réactives associent directement les situations aux actions. Elles sont de nature réflexive et les décisions sont prises en fonction des stimuli immédiats de l’environnement plutôt que de faire appel à la mémoire ou aux capacités prédictives. Ces agents ne peuvent pas apprendre du passé ni planifier l’avenir. 

### Architectures délibératives

Une architecture délibérative est un système d’IA qui prend des décisions basées sur le raisonnement, la planification et des modèles internes du monde. Contrairement aux agents réactifs, les agents délibératifs analysent leur environnement, prédisent les résultats futurs et font des choix éclairés avant d’agir.

### Architectures cognitives

Une architecture agentique cognitive est un système d’IA avancé qui imite la pensée, le raisonnement, l’apprentissage et la prise de décision humains.\
\
Ces agents intègrent des éléments de perception, de mémoire, de raisonnement et d’adaptation, chacun représenté par des modules individuels, ce qui leur permet d’opérer dans des environnements complexes et incertains tout en s’améliorant au fil du temps. Il s’agit du type d'architecture agentique le plus avancé.

Une **architecture BDI** (plus communément appelée modèle ou framework) est conçue pour modéliser la prise de décision rationnelle chez des agents intelligents. Elle est basée sur le cadre croyance-désir-intention (BDI).\

Cette architecture modélise le raisonnement humain dans un agent BDI à partir des :

- **Croyances (B)** : les connaissances de l’agent sur le monde, pouvant inclure sa compréhension de l’environnement, de la situation actuelle et des données sensorielles.

Exemple : « La porte est fermée. »

- **Désirs (D)** : les buts ou objectifs de l’agent, représentant ce qu’il souhaite accomplir. Les désirs ne sont pas nécessairement des actions, mais des objectifs de premier niveau.

Exemple : « Je veux entrer dans la pièce ».

- **Intentions (I)** : le plan d’action sur lequel l’agent s’engage pour réaliser ses désirs. Les intentions représentent des actions planifiées que l’agent poursuit activement, en tenant compte de ses croyances et de ses désirs.

Exemple : « Je vais ouvrir la porte pour entrer dans la pièce. »

##### Notes de bas de page

1 Bandura A. « Social cognitive theory: an agentic perspective ». Annual Review of Psychology 2001;52:1-26. doi: 10.1146/annurev.psych.52.1.1. https://pubmed.ncbi.nlm.nih.gov/11148297/.

2 Bandura A. « Social cognitive theory: an agentic perspective. »\
\
3 T. Masterman, S. Besen, M. Sawtell, et A. Chao, « The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey », arXiv preprint arXiv:2404.11584, avril 2024. \[En ligne\]. Disponible : https://arxiv.org/abs/2404.11584.

4 E. H. Durfee and V. Lesser, « Negotiating Task Decomposition and Allocation Using Partial Global Planning, », *Distributed Artificial Intelligence Volume II*, ed. L. Gasser et M. Huhns (London: Pitman Publishing; San Mateo, CA: Morgan Kaufmann, 1989), 229–244.\
\
5 Masterman, et al., « The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey. »

6 Masterman, et al, « The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey. »
