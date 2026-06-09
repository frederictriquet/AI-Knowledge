> Source : https://www.ibm.com/fr-fr/think/topics/ai-agent-communication

# Qu’est-ce que la communication des agents d’IA ?

 La communication des agents d’IA fait référence à la manière dont les agents d’IA interagissent entre eux, avec les humains ou avec des systèmes externes, pour échanger des informations, prendre des décisions et accomplir des tâches. Cette communication est particulièrement importante dans les systèmes multi-agents, où plusieurs agents d’IA collaborent, et dans les interactions humain-IA.

Grands modèles de langage ([LLM](https://www.ibm.com/fr-fr/think/topics/large-language-models-list)) : les algorithmes de machine learning entraînés sur de grandes quantités de données permettent aux agents de raisonner. Grâce aux capacités d’IA générative, les agents peuvent partager les informations qu’ils connaissent avec d’autres entités. Lorsque les agents ont la capacité de communiquer entre eux, un système agentique devient plus que la somme de ses parties.

Un système multi-agent peut être considéré comme une équipe d’humains, chacun possédant une expertise dans son domaine respectif. Les agents autonomes partagent des informations qu’ils sont les seuls à pouvoir percevoir sur leur environnement, ce qui avantage la compréhension de l’ensemble du groupe. À mesure que de plus en plus d’agents deviennent capables de « se parler » dans le cadre de workflows agentiques complexes, nous pouvons nous attendre à des écosystèmes entiers d’agents en ligne travaillant ensemble dans une harmonie autonome.

## Avantages de la communication des agents d’IA

Les agents d’IA en réseau peuvent travailler ensemble à la réalisation d’un objectif commun de manière plus efficace qu’un seul agent d’IA. Mais pour coordonner leurs actions, ils doivent être capables de communiquer efficacement.

Une communication efficace entre les agents d’IA conduit à une meilleure connaissance de la situation et à des processus de prise de décision plus éclairés. Lorsque les agents partagent des données, ils peuvent affiner leurs stratégies et leurs réponses en fonction des informations en temps réel.

Dans les systèmes complexes, l’IA distribuée peut répartir les tâches entre plusieurs agents pour accélérer la résolution des problèmes. Au lieu d’une seule IA essayant de tout traiter, plusieurs agents peuvent se spécialiser dans différents aspects d’un problème et communiquer leurs conclusions.

Les agents d’IA qui communiquent peuvent apprendre les uns des autres, améliorant ainsi l’adaptabilité au fil du temps. En échangeant des informations, ils affinent leurs comportements sur la base d’expériences partagées. Les systèmes d’IA multi-agent peuvent également évoluer efficacement, en gérant de plus grandes quantités de données et des tâches plus complexes.

## Types de communication des agents d’IA

Les agents d’IA communiquent de différentes manières en fonction de leur rôle, de leur environnement et de leurs objectifs. La communication peut être explicite ou implicite, impliquant des échanges de messages directs ou une observation indirecte des actions.

Certains systèmes s’appuient sur un contrôle centralisé, où une seule IA traite et distribue les données à d’autres agents. D’autres encore utilisent une communication décentralisée, où les agents d’IA interagissent entre pairs.

### Communication d’agent à agent

La plupart des agents sont alimentés par des LLM, ce qui leur permet souvent de communiquer entre eux dans un langage humain naturel. Les agents doivent être en mesure non seulement de partager des informations, mais aussi d’exprimer une intention, de se coordonner au sein d’une hiérarchie et de négocier l’allocation des ressources.\
\
Les chercheurs travaillent sur des modes de communication d’agent à agent plus efficaces, tels que la solution « DroidSpeak » de Microsoft, qui vise à permettre aux agents de communiquer plus rapidement avec une perte de précision minimale.1 Les deux protocoles privilégiés pour la communication avec les agents sont KQML (Knowledge Query and Manipulation Language) et FIPA-ACL (Foundation for Intelligent Physical Agents – Agent Communication Language).2

La DARPA, Defense Advanced Research Projects Agency (Agence américaine pour les projets de recherche avancée en matière de défense), a développé le KQML dans les années 1990, posant les bases d’une communication entre agents bien avant que des agents d’IA intelligents ne soient mis au point. Les développeurs de la FIPA ont poursuivi ce travail peu de temps après, apportant des améliorations en matière de standardisation et de clarté sémantique.

De nombreux agents d’IA s’appuient sur des appareils de cloud computing et d’Internet des objets (IdO) pour échanger des données en temps réel. Les systèmes d’IA cloud stockent, récupèrent et analysent des ensembles de données à grande échelle, tandis que les appareils connectés à l’IdO partagent les informations des capteurs sur les réseaux.

### Communication humain-IA

Les agents d’IA communiquent également avec les humains à l'aide du traitement automatique du langage naturel (NLP), de la reconnaissance vocale et d'interfaces visuelles. Les assistants virtuels tels que ChatGPT d’OpenAI, Siri d’Apple et Alexa d’Amazon utilisent le NLP pour interpréter les requêtes humaines et générer des réponses pertinentes.

Dans le domaine du support client, les chatbots d’IA fournissent une assistance automatisée en comprenant et en répondant aux demandes des utilisateurs. Certains modèles d’IA intègrent également la communication multimodale, qui combine texte, parole et images pour améliorer l’interaction.

## Les défis de la communication des agents d’IA

Les agents d’IA sont confrontés à plusieurs défis qui peuvent affecter la précision, l’efficacité, la sécurité et l’évolutivité.

### Manque de protocoles standardisés\
 

Les agents d’IA opèrent souvent sur différentes plateformes, chacune utilisant des protocoles, des formats de données et des langages de communication uniques. Les protocoles incluent des informations sur la syntaxe et la sémantique des messages. Les protocoles peuvent être prédéfinis par des programmeurs humains, ou émergents, découlant de manière organique de la communication d’agent à agent.\

Sans un cadre des exigences normalisé, les agents pourraient avoir du mal à interpréter les messages des autres et à y répondre, ce qui affecterait l’efficacité. Par exemple, dans les villes intelligentes, les systèmes de gestion du trafic et les véhicules autonomes peuvent utiliser différents protocoles de communication, ce qui empêche la coordination et le partage transparents des données.

### Ambiguïté et erreur d’interprétation

Les agents d’IA doivent traiter les informations avec précision, mais l'ambiguïté dans l’interprétation des messages reste un défi. Les agents peuvent mal interpréter les messages, ce qui entraîne des actions incorrectes. Dans les chatbots de service client, les requêtes utilisateur vagues telles que « Je veux modifier ma commande » pourraient être mal comprises, entraînant des modifications ou des annulations incorrectes.

### Latence

De nombreux cas d’utilisation de l’IA nécessitent une communication en temps réel, mais la latence du réseau et les contraintes de calcul peuvent ralentir les temps de réponse. C’est particulièrement problématique dans les systèmes autonomes qui nécessitent une prise de décision en une fraction de seconde. Dans les voitures autonomes, les agents d’IA doivent traiter instantanément les données des caméras, des capteurs et du GPS. Tout retard dans l’échange de données pourrait causer de mauvaises décisions de navigation.

### Sécurité et confidentialité

Les agents d’IA qui communiquent sur les réseaux sont vulnérables aux cyberattaques, aux violations de données et aux manipulations adverses. Les acteurs malveillants peuvent intercepter ou altérer les communications de l’IA, entraînant des prises de décision erronées et des pannes de système.\
\
L'authentification, la sécurisation des points de terminaison et le traitement approprié des données sensibles sont primordiaux. Dans les systèmes d’IA pour les soins de santé, par exemple, si un pirate modifie les données de diagnostic échangées entre les agents d’IA, cela pourrait conduire à des recommandations de traitement incorrectes.

### Évolutivité

À mesure que le nombre d’agents d’IA dans un système de communication augmente, les frais de communication augmentent, ce qui pose des problèmes d’évolutivité. Les agents doivent gérer efficacement les interactions à grande échelle sans surcharger les ressources de calcul.\

Sur les marchés financiers, des milliers de bots de trading IA communiquent et réagissent aux évolutions du marché. Si trop de bots échangent des données en même temps, cela peut entraîner une congestion du réseau.

### Adaptabilité

Les agents d’IA doivent communiquer efficacement dans des environnements dynamiques, où des mises à jour d’informations en temps réel sont nécessaires. Si les agents d’IA ne parviennent pas à s’adapter aux nouvelles conditions, les changements inattendus peuvent perturber leurs processus de prise de décision.\
\
En cas de catastrophe, l’IA, les drones autonomes et les robots doivent continuellement ajuster leurs stratégies de communication en fonction d’obstacles imprévisibles, tels que des bâtiments effondrés ou des signaux réseau perdus.

### Compréhension du langage humain

Lorsque les agents d’IA interagissent avec des humains, des problèmes de communication surviennent en raison de différences dans la compréhension du langage, le contexte émotionnel et les styles de raisonnement. L’IA doit interpréter correctement l’intention humaine tout en fournissant des réponses claires.\

Pour les assistants virtuels, la compréhension du sarcasme, des dialectes régionaux ou des requêtes implicites reste un défi. Par exemple, si un utilisateur dit « Il fait froid ici », un assistant d’IA pourrait ne pas comprendre qu’il souhaite que le thermostat soit augmenté.

##### Notes de bas de page

1 Droidspeak: KV Cache Sharing for Cross-LLM Communication and Multi-LLM Serving, Liu *et al*, Université de Chicago, Microsoft, 19 décembre 2024.

2 The Current context of Agent Communication Languages, Labrou *et al*, Université du Maryland, mars 1999.
