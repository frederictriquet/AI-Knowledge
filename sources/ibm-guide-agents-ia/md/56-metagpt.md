> Source : https://www.ibm.com/fr-fr/think/topics/metagpt

# Qu'est-ce que MetaGPT ?

## Qu’est-ce que MetaGPT ?

MetaGPT est un cadre des exigences multi-agents open source qui orchestre l'utilisation des connaissances procédurales humaines et d'agents IA alimentés par de grands modèles linguistiques (LLM) pour développer une gamme variée de solutions logicielles. En tant que société de logiciels d'IA, MetaGPT propose des agents IA spécialisés qui jouent des rôles similaires à ceux des éditeurs de logiciels traditionnels.

MetaGPT est la technologie propriétaire de DeepWisdom fondée par Chenglin Watson. Ce cadre des exigences a rapidement gagné en popularité sur GitHub, suscitant un vif intérêt pour l'objectif sous-jacent de MetaGPT, qui est de faire progresser la programmation en langage naturel à l'aide de systèmes multi-agents (MAS).\
\
L'article de recherche très apprécié « MetaGPT : Metaprogramming for A Multi-Agent Collaborative cadre des exigences » explique l'orchestration de la collaboration entre agents dans le cadre des exigences. Alors que les recherches sur l'orchestration des LLM et les agents IA continuent, MetaGPT est l'un des premiers contributeurs à proposer une approche simple de la collaboration multi-agent en utilisant des workflows familiers.

## Qu’est-ce que la collaboration multi-agent ?

Les agents opérant au sein d'un système multi-agent (MAS) restent autonomes, mais coopèrent et se coordonnent dans des structures agentiques ou des cadres des exigences tels que MetaGPT.[1](#f1) Un MAS coordonne les agents individuels pour opérer et interagir au sein de leur environnement afin d’accomplir des tâches complexes et d’atteindre un objectif commun. Cette idée fait partie de l’intelligence collective, un concept populaire parfois lié à l’ AGI.\
\
Un système multi-agent est constitué d’un réseau d’agents capables de résoudre les problèmes, qui collaborent pour relever les défis qui dépassent les capacités d’un seul agent.[2](#f2) L’un des principaux défis de la conception d’un système MAS efficace est de coordonner les agents pour s’assurer de leur collaboration autour d’un objectif partagé. Une collaboration réussie repose sur la capacité de chaque agent à résoudre des tâches individuelles, ainsi que sur sa capacité à interagir efficacement les uns avec les autres.[3](#f3)

Voici quelques éléments à prendre en compte pour planifier un environnement MAS :

- Les limites que les activités des autres agents créent pour la prise de décision d'un agent,
- Les contraintes qui découlent des engagements d'un agent envers d'autres en ce qui concerne ses actions disponibles,
- Et l’évolution imprévisible du monde causée par des agents externes et non modélisés.[4](#f4)

L’une des approches permettant de relever ce défi de conception consiste à orchestrer la collaboration des agents en modélisant explicitement le teamworks . Ce modèle de conception multicollaborative décompose un prompt complexe et délègue les tâches abstraites aux agents qui les exécutent en fonction de leurs rôles spécialisés.[5](#f5)

Dans le cadre des exigences de MetaGPT, une équipe d'agents IA opère selon un workflow guidé par des procédures opérationnelles standard (SOP) qui définissent des rôles et des instructions distincts. En intégrant des protocoles de communication et des workflows rationalisés dans des systèmes multi-agents basés sur des LLM, les utilisateurs peuvent créer des applications avec une seule ligne d'entrée.

## Comment fonctionne MetaGPT ?

MetaGPT agit comme un cadre des exigences collaboratif multi-agent capable de résoudre des tâches complexes. Le cadre des exigences de collaboration multi-agent fonctionne en simulant l’ensemble d’une société de logiciels à l’aide d’agents spécialisés qui interagissent en fonction des procédures d’exploitation standard et d’un paradigme de chaîne de montage pour fractionner les tâches. Chaque agent joue un rôle spécialisé en fonction des fonctions qui lui sont propres au sein de l’éditeur de logiciels. Par exemple, le cadre des exigences inclut des agents qui agissent comme chefs de produit, architectes, chefs de projet et ingénieurs qui fournissent l’ensemble du processus d’une entreprise de logiciels.

Ces agents, dans leurs différents rôles, agissent au sein d’un espace de travail virtuel pour répondre aux exigences d’une seule ligne en entrée et en sortie à partir de diverses solutions logicielles. Ces entrées comprennent les structures de données, les interfaces de programmation des applications (API), l’analyse concurrentielle et les documents. Les agents communiquent via des sorties structurées basées sur les exigences définies par un paradigme de chaîne d’assemblage. Chaque agent génère les informations nécessaires pour inciter l'agent suivant à atteindre l'objectif collectif : produire une application basée sur le prompt de l'utilisateur. Ce processus de développement incrémentiel est dû à la manière dont MetaGPT intègre les workflows pour rationaliser la coordination sur une tâche complexe.

### Connaissance des procédures humaines pour la collaboration multi-agent

Les procédures opérationnelles standard ont été adoptées dans divers domaines, car elles jouent un rôle critique dans la décomposition des tâches et la coordination efficace.[6](#f6) Dans le développement de logiciels, les SOP encouragent la collaboration entre les équipes en décomposant les tâches du projet en procédures exploitables plus petites qui sont ensuite affectées à des rôles spécifiques et spécialisés. MetaGPT encode les SOP dans des séquences de prompts pour organiser et promouvoir des workflows multiagents. Les workflows SOP présentent une structure et des possibilités d'amélioration. 

Par exemple, l’agent responsable de projet est invité à créer un document d’exigences produit (PRD). L'agent chef de produit est prompt une fois puis invité à affiner certains éléments du PRD en raison du développement incrémentiel du projet. Par exemple, l’agent est invité à créer une section dans le PRD pour les « objectifs du produit ». Il est ensuite nécessaire d'affiner ces objectifs en mettant à jour les objectifs initiaux du produit afin de s'assurer qu'ils correspondent à l'orientation actuelle du projet[.](#f7) Cette méthode de raffinement est utilisée pour garantir que la tâche globale est reconnue et cohérente pour tous les agents.\
\
Dans l’exemple ci-dessous, l’agent du chef de produit est invité à générer une analyse des exigences. Après ce prompt initial, l'agent est invité à générer une analyse affinée qui prend en compte toute nouvelle fonctionnalité et amélioration issue de la collaboration continue.\
\
**prompt Instruction relative à l'analyse des besoins : ***« Fournissez une analyse détaillée des besoins. »*[8](#f8)

**Instruction pour une analyse de prompt affinée :*** « Examinez et affinez l’analyse des exigences existantes en une liste de chaînes pour l’aligner sur l’évolution des besoins du projet en raison du développement incrémentiel. Assurez-vous que l’analyse couvre de manière exhaustive les nouvelles fonctionnalités et les améliorations requises pour la portée affinée du projet.*[9](#f9)\
\
Cet exemple montre un PRD généré en tant que sortie standardisée qui est transmis de l’agent du gestionnaire de produit à l’agent de l’architecte. Le prompt basé sur le SOP pour chaque production générée est répertoriée à côté. Vous remarquez que le prompt est également basée sur le flux de travail SOP, y compris les définitions des exigences, les méthodes d'exécution des tâches et l'ordre d'exécution\
\
 :**Prompt utilisateur*** : « Créez-moi une application Web basée sur React que les gestionnaires de patrimoine peuvent utiliser pour examiner leurs clients les portefeuilles et leur recommander des fonds appropriés à utiliser. Cette application doit fonctionner en Amérique, au Royaume-Uni et en Espagne. »*\
\
**Exigences initiales**\
Instructions prompt : *« Placez les exigences de l'utilisateur d'origine ici. »*[10](#f10)\
\
*« Créez-moi une application basée sur React pour les gestionnaires de patrimoine pour examiner les portefeuilles de leurs clients et leur faire des recommandations sur les fonds appropriés à utiliser. Cette application doit fonctionner en Amérique, au Royaume-Uni et en Espagne. »*

**Objectifs du produit** \
Instruction du prompt : *« Fournir jusqu'à trois objectifs de produit clairs et orthogonaux. »*[11](#f11)

1.  Développez une application Web sécurisée et fiable pour les gestionnaires de patrimoine.
2.  Assurez la prise en charge multilingue pour les variantes anglaises, espagnoles et régionales.
3.  Créez une interface intuitive et conviviale pour la gestion des portefeuilles et la recommandation.

**Scénarios d'utilisateur** \
Instruction *de prompt : « Fournir jusqu'à 3 à 5 scénarios d'utilisateur basés sur des scénarios. »*[12](#f12)

1.  En tant que gestionnaire de patrimoine, je souhaite passer en revue les portefeuilles de mes clients et leur fournir des conseils personnalisés.
2.  En tant que gestionnaire de patrimoine, je souhaite recommander des fonds à mes clients en fonction de leurs objectifs d'investissement et de leur tolérance au risque.
3.  En tant que gestionnaire de patrimoine, je souhaite accéder à l'application en anglais ou en espagnol selon mon emplacement.

**Analyse concurrentielle\**
Instruction de prompt : *« Fournir 5 à 7 produits compétitifs. »*[13](#f13)

1.  « Wealthfront : service d’investissement automatisé avec une interface propre, mais sans recommandations personnalisées en matière de fonds. »
2.  « Personal Capital : offre des outils complets de gestion de patrimoine, mais peut être difficile pour les nouveaux utilisateurs. »
3.  « Amélioration : se concentre sur les investissements automatisés avec une personnalisation limitée pour les gestionnaires de patrimoine. »

**Analyse des exigences\**
Instruction de prompt : *« Fournir une analyse détaillée des exigences. »*[14](#f14)

L’application doit être conçue à l’aide de React, garantissant ainsi qu’elle est évolutive et maintenable. Il doit disposer d’une interface multilingue pour s’adapter aux utilisateurs en Amérique, au Royaume-Uni et en Espagne. L’application doit être sécurisée pour protéger les données financières sensibles et se conformer aux réglementations régionales. Il doit également s’intégrer à diverses sources de données financières pour fournir une analyse des portefeuilles en temps réel et des recommandations de fonds.

**Pool d’exigences\**
Instruction de prompt : *« Énumérez les 5 à 7 principales exigences avec leur priorité (P0, P1, P2) », « Couvrir à la fois le contenu d'héritage et le contenu incrémental. Conservez le contenu sans rapport avec le développement incrémental. »*[15](#f15)

-  (« Authentification sécurisée des utilisateurs et chiffrement des données pour protéger les informations client », « P0 »),
- (« Prise en charge multilingue pour l’anglais et l’espagnol, avec des variations régionales ,» « P0 »),
-  (« Intégration en temps réel avec les sources de données financières pour la gestion des portefeuilles », « P0 »),
-  (« Tableau de bord convivial pour l'examen et la gestion des portefeuilles clients »), « P1 »),
- (« Moteur de recommandation pour suggérer des fonds appropriés en fonction des profils des clients », « P2 »)

**Projet de design d'interface utilisateur\**
Instruction de prompt : *« Fournissez une description simple des éléments, des fonctions, du style et de la mise en page de l'interface*[utilisateur. » 16](#f16)

L'interface utilisateur présentera une conception épurée et moderne avec un tableau de bord qui offre une vue d'ensemble des portefeuilles. Elle comprendra des graphiques interactifs pour l’analyse des portefeuilles, une section de recommandation pour la sélection des fonds et un basculement facile entre les langues anglaises et espagnoles.\
\
**Tout ce qui n’est pas clair\**
Instruction de prompt : *« Mentionnez les aspects du projet qui ne sont pas clairs et essayez de les clarifier. »*[17](#f17)\

*Il n'y a aucun point obscur.*

L’exemple précédent est un transfert de relais à l’agent architecte pour la conception, voici le prompt basé sur le SOP donné avec le PRD :

« Voici le document d’exigences du produit (PRD)  sur la base de ce PRD, examinez si la conception de cette API répond aux exigences du PRD et si elle est conforme aux bonnes pratiques de conception. » [18](#f18)

L’architecte suit son propre workflow SOP pour concevoir le système pour l’application.

Un SOP décrit les responsabilités du rôle de chaque agent et établit des normes pour les sorties intermédiaires. Ces SOP sont ensuite codés pour influencer le comportement de l'agent. Cette pratique permet aux agents de générer des sorties structurées, telles que des documents d’exigences de haute qualité, des artefacts de conception, des organigrammes et des spécifications d’interface. Tous les transferts entre agents doivent respecter certaines normes établies qui réduisent le risque d’hallucination causée par des discussions à vide entre différents LLM. L’utilisation de sorties structurées améliore considérablement le taux de réussite de la génération de code cible.[19](#f19)

## Comment MetaGPT utilise les SOP pour réaliser les prompts des agents

Tous les agents de MetaGPT agissent comme des employés qui doivent suivre un workflow strict et rationalisé. Deux parties principales du SOP définissent le comportement des agents : la spécialisation des rôles et le workflow entre agents.

**Spécialisation des rôles d'agent :** MetaGPT définit cinq rôles au sein de l'éditeur de logiciels : chef de produit, architecte, chef de projet, ingénieur et ingénieur QA. Le profil de chaque agent est initialisé avec des informations spécifiques telles que le nom de l’agent, le profil, l’objectif et les contraintes pour chaque rôle, ainsi que le contexte et les compétences spécifiques pour chaque rôle.[20](#f20) Chaque agent est comme un organisme numérique qui agit au sein d’un environnement.[21 ](#f21)Le concept de rôles prédéfinis est différent des cadres multiagents comme CrewAI qui permettent aux utilisateurs de définir la fonction de l'agent au sein d'une équipe pour des cas d’utilisation plus généraux.

Worklow entre les agents : la définition des rôles et des compétences opérationnelles des agents établit un workflow de base que les agents peuvent suivre dans le cadre du processus de développement logiciel. Les agents travaillent dans le cadre d’un ordre séquentiel ou d’un paradigme de chaîne de montage pour décomposer les tâches complexes afin d’accroître l’efficacité de l’équipe.

## Comment les agents interagissent-ils dans MetaGPT ?

MetaGPT affirme qu’une collaboration significative nécessite des processus de résolution des problèmes efficaces, cohérents et précis. Les agents IA sont des systèmes complexes ; cependant, leurs processus n'ont pas à l'être, du moins pas selon MetaGPT et son héritage de workflows humains simples.

**Protocole de communication**

Les agents interagissent au sein d’une interface de communication structurée appelée protocole de communication. MetaGPT se distingue de la plupart des cadres des exigences multi-agents basés sur des LLM, car il n’utilise pas de langage naturel non contraint comme interface de communication, mais propose une communication structurée pour formuler l’interaction entre les agents. Par exemple, dans ChatDev, un autre cadre de collaboration multi-agent, les agents communiquent par dialogue tandis que les agents de MetaGPT communiquent via des résultats structurés tels que des documents et des diagrammes.

Pour faciliter ce protocole de communication, MetaGPT établit un schéma et un format pour chaque agent et demande à chaque rôle de fournir les sorties nécessaires en fonction de son objectif et de son contexte spécifiques.[22](#f22) Dans un exemple, l’agent architecte génère deux sorties : la conception d’interface système et un organigramme de séquence. Les deux sorties contiennent des séquences de conception de modules système et d’interaction qui servent de livrables primordiales pour les agents d’ingénierie.[23](#f23)

**Mécanisme de publication et s'abonner**

Pour améliorer l’efficacité de la communication, MetaGPT utilise un pool de messages global pour magasin des informations qui permettent aux agents d’échanger des messages directement. Les agents publient leurs messages structurés dans le pool et peuvent accéder aux messages d’autres agents de manière transparente. Cette approche permet aux agents d’accéder directement aux informations nécessaires à partir du pool partagé, évitant ainsi de devoir interroger d’autres agents et attendre leurs réponses.[24](#f24)

## Processus de développement MetaGPT

Le processus de développement commence par la commande d’entrée d’un utilisateur et se termine par un logiciel conçu selon les spécifications de l’utilisateur. Par exemple, l’entrée utilisateur peut être « Écrire une application graphique Python permettant de dessiner une image avec elle. » Le prompt utilisateur est transmis à l'éditeur du logiciel, une équipe d'agents jouant le rôle : chef de produit, architecte, chef de projet, ingénieur, ingénieur en assurance qualité

Après avoir reçu le prompt de l'utilisateur pour créer une application spécifique, le chef de produit génère un PRD qui comprend des objectifs, des histoires d'utilisateurs, une analyse de la concurrence, une analyse des exigences et un pool d'exigences. En outre, l'agent gestionnaire de produit génère également un graphique en quadrant concurrentiel basé sur les spécifications de l'application. Ces documents et graphiques sont remis à l'agent architecte pour la conception du système.

L’agent architecte gère les spécifications techniques en fonction des exigences du PRD. Les spécifications comprennent des schémas d’architecture du système et des définitions d’interface pour la trajectoire technique globale du projet. L’architecture du projet, notamment les fichiers, les classes et l’organigramme de séquence, est conçue sur la base des définitions techniques de l’agent d’architecte. La documentation générée par l’architecte est ensuite remise au chef de projet pour l’allocation et l’exécution des tâches.

Le responsable de projet décompose le projet en une liste de tâches. Chaque fichier de code est analysé en fonction de la fonctionnalité prévue, puis traité comme une tâche distincte confiée aux ingénieurs.

L’agent ingénieur génère le code nécessaire avec les compétences de développement fondamentales pour mener à bien les tâches de développement. Dès qu'il reçoit la production du code de l'agent d'ingénierie, l'agent d'ingénierie d'assurance qualité génère un code de test unitaire et le donne son avis pour identifier et apporter des correctifs.

## Intégration de LLM dans MetaGPT

Les agents MetaGPT sont basés sur la série de modèles GPT (generative pre-trained transformer) d’OpenAI, GPT-3.5 et GPT-4. Cependant, MetaGPT et sa communauté open source ont contribué à l'ajout de plusieurs autres modèles qui peuvent être initialisés via la configuration d'API LLM. MetaGPT propose un tutoriel qui facilite l'exploration de la façon d'intégrer les LLM open source sur son site de documentation GitHub. La première étape de l’intégration d’un LLM consiste à configurer un référentiel d’inférence (repo) tel que LLaMA-Factory, FastChat, Ollama, etc. Ce référentiel permet le déploiement du modèle LLM correspondant, qui est configuré via ses identifiants d’API. Tous les dépôts d’inférence pris en charge, à l’exception d’Ollama, prennent en charge la publication d’interfaces compatibles avec OpenAI. MetaGPT cherche à prendre en charge l'interface Ollama à l'avenir.

## Les agents IA peuvent-ils exceller dans la métaprogrammation ?

Les cadres des exigences de métaprogrammation permettent de créer des programmes qui peuvent écrire, manipuler et analyser d’autres programmes ainsi que le programme lui-même. MetaGPT modélise cet objectif en incorporant des workflows humains pour alimenter l'IA générative en utilisant des techniques basées sur des agents pour améliorer la métaprogrammation.

Les agents basés sur les LLM disposent de plusieurs fonctionnalités de base qui disposent de tâches de programmation automatiques avancées.[25](#f25) Parmi ces avancées figurent ReAct et Reflexion, des paradigmes de raisonnement utilisés par des agents qui utilisent une chaîne de pensées pour générer des trajectoires de raisonnement et des plans d’action avec des LLM.[26](#f26)

La boucle de conception de l’agent ReAct démontre un processus efficace pour la programmation automatique en raison de sa boucle de conception itérative qui permet aux agents de raisonner, d’agir et d’observer.[27](#f27) Reflexion renforce les agents linguistiques grâce à des commentaires linguistiques, en suivant une boucle de conception itérative similaire pour améliorer la prise de décision.[28](#f28) Les deux conceptions de paradigme permettent aux agents d'apprendre et d'améliorer en permanence leur workflow.

Les LLM traditionnels, tels que le modèle GPT-3 d’OpenAI, les modèles Llama de Meta et les modèles Granite d’IBM, sont limités dans leurs connaissances et leur raisonnement. Ils génèrent des réponses basées sur les données d'apprentissage, qui peuvent souvent inclure des informations obsolètes. En revanche, la technologie agentique tire parti de l'appel d'outils de back-end pour accéder aux informations actuelles, tirer parti de workflow et créer de manière autonome des tâches spécifiques pour accomplir des objectifs complexes. Au cours de ce processus, l’agent autonome apprend à s’adapter aux attentes des utilisateurs au fil du temps, en offrant une expérience sur mesure et des réponses plus complètes. Cet outil d'appel peut se produire sans intervention humaine, élargissant ainsi le potentiel des applications réelles pour ces systèmes d'IA.

## Comment MetaGPT utilise des agents de métaprogrammation

Les agents d'ingénierie de MetaGPT participent à la programmation itérative avec des commentaires exécutable. Les processus de débogage et d'optimisation sont importants dans les tâches de programmation quotidiennes. D’autres implémentations manquent de mécanismes d’auto-correction des agents qui conduisent à des résultats indésirables tels que des hallucinations de code ou du code qui ne fonctionne pas. Pour atténuer ces risques, MetaGPT introduit un mécanisme de commentaires exécutable pour améliorer le code à chaque itération.\

L’agent ingénieur écrit du code en fonction des exigences et de la conception du produit d’origine. Cela permet à l’agent d’améliorer continuellement le code en utilisant sa propre mémoire historique d’exécution et de débogage. L’ingénieur obtient plus d’informations pour améliorer le code en écrivant et en exécutant les cas de test unitaires correspondants. Après avoir reçu les résultats, l’ingénieur procède à des tâches de développement supplémentaires ou débogue le code avant de reprendre la programmation. Ce processus itératif se poursuit jusqu’à ce que le test soit réussi ou qu’un maximum de 3 tentatives soit atteint.[29](#f29)

## Autres cadres multi-agents

crewAI – CrewAI est un cadre multi-agents open source, basé sur python, qui s’appuie sur des agents autonomes de jeu de rôle qui travaillent ensemble en équipe pour accomplir des tâches. Les utilisateurs peuvent créer et personnaliser des agents en fonction des besoins ou de l’utilisation de leur application. Les cas d’utilisation incluent des objectifs généraux tels que la planification et la création de contenu, l’analyse de données et les tâches d’automatisation. CrewAI propose une Intégration avec l’IBM’s watsonx.ai et offre plusieurs Intégrations LLM et une compatibilité avec Ollama.[30](#f30)

ChatDev – ChatDev est un cadre des exigences multiagent open source qui simule une société de logiciels virtuelle fonctionnant par l'intermédiaire de divers agents intelligents tenant différents rôles organisationnels. Les agents coopèrent par dialogue pour créer un produit logiciel comprenant du code exécutable et de la documentation. ChatDev prend en charge les modèles GPT-3.5-turbo et GPT-4 d’OpenAI pour alimenter ses agents intelligents.[31](#f31)

AutoGPT – AutoGPT est un cadre multi-agent open source qui applique le traitement automatique du langage naturel (NLP) pour comprendre les objectifs des utilisateurs et la décomposition de tâches complexes. Les agents coopèrent dans un workflow pour traiter un prompt utilisateur de haut niveau en décomposant chaque tâche en une séquence de sous-tâches plus petites. Les cas d’utilisation comprennent des solutions générales telles que les études et les analyses de marché, le développement de produits, l’assistance virtuelle, etc. Ce framework est construit avec des agents d'IA basés sur le GPT-4 d'OpenAI.[32](#f32)
