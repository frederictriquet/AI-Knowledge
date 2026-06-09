> Source : https://www.ibm.com/fr-fr/think/topics/agentic-workflows

# Qu’est-ce qu’un workflow agentique ?

Les workflows sont des processus pilotés par l’IA lors desquels les agents d’IA autonomes prennent des décisions, exécutent des actions et coordonnent les tâches avec une intervention humaine minimale. Ces workflows s’appuient sur des éléments essentiels des agents intelligents tels que le raisonnement, la planification et l’utilisation d’outils pour réaliser efficacement des tâches complexes. L’automatisation traditionnelle, telle que l’automatisation robotisée des processus (RPA), suit des règles et des modèles de conception prédéfinis. Cette approche peut suffire pour les tâches répétitives, qui suivent une structure standard. Dynamiques, les workflows agentiques offrent plus de flexibilité en s’adaptant aux données en temps réel et aux conditions inattendues. Les workflows d’IA agentique abordent les problèmes complexes en plusieurs étapes, de manière itérative, pour permettre aux agents d’IA de décomposer les processus métier, de s’adapter de façon dynamique et d’affiner leurs actions au fil du temps.

En laissant l’IA générative gérer des workflows complexes, les entreprises améliorent l’efficacité opérationnelle, l’évolutivité et la prise de décisions. Alors que les techniques de machine learning et de traitement automatique du langage naturel (NLP) continuent de progresser, la technologie de l’IA est de plus en plus présente dans les secteurs qui cherchent à automatiser et à optimiser les processus tout en réduisant la dépendance à la supervision humaine. Les impacts de l’évolution des modèles d’IA affectent non seulement le développement de logiciels, mais aussi des secteurs comme la santé, la finance, les ressources humaines et bien d’autres.

## Comment fonctionnent les workflows agentiques ?

Prenons l’exemple d’une entreprise dotée d’un chatbot de support informatique qui suit un système d’automatisation basé sur les règles. Lorsqu’un employé signale un problème (par exemple, « Mon wifi ne fonctionne pas »), le chatbot parcourt divers arbres de décision pour fournir des réponses prédéfinies. Si le problème n’est pas résolu, le chatbot passe simplement à l’équipe d’assistance. Si cette approche s’avère efficace pour résoudre les problèmes simples et bien définis, elle peine face aux tâches de dépannage complexes, qui comportent plusieurs étapes et demandent une certaine adaptabilité.

Avec un workflow agentique, l’assistant informatique aborde la résolution des problèmes comme un processus itératif en plusieurs étapes. Si un employé signale un problème de Wi-Fi, l’agent suit un processus dynamique, étape par étape, pour décomposer le workflow :

1.  **Comprendre le problème** : l’agent d’IA recueille des informations détaillées auprès de l’employé en lui posant des questions, par exemple, « Y a-t-il d’autres appareils connectés au réseau ?» ou « Le problème a-t-il commencé après une mise à jour réalisée récemment ? »

2.  **Exécuter les étapes de diagnostic** : en fonction des réponses de l’utilisateur, l’IA sélectionne et exécute différentes étapes de résolution des problèmes. Il peut s’agir d’envoyer une requête ping au routeur, de vérifier les journaux réseau ou de suggérer des modifications des paramètres, tout en récupérant et en synthétisant ces informations pour l’utilisateur.

3.  **Utilisation adaptative des outils** : si l’IA détecte un problème lié au serveur, elle peut appeler une API d’outil de surveillance interne pour vérifier les pannes. Si le problème est lié à un appareil, l’IA peut récupérer des suggestions de mise à jour des pilotes ou exécuter un script pour réinitialiser les paramètres réseau.

4.  **Itération basée sur les résultats** : si une action ne résout pas le problème, l’IA ajuste son approche de manière dynamique. Elle peut recouper les problèmes connexes, tenter un nouveau diagnostic ou suggérer une solution différente au lieu de faire remonter immédiatement.

5.  **Finalisation et apprentissage** : si le problème est résolu, l’IA enregistre la solution pour une utilisation ultérieure et améliore ainsi ses capacités de dépannage au fil du temps. Si le problème n’est pas résolu, il est transmis aux équipes informatiques, accompagné d’un rapport détaillé des correctifs tentés, afin de leur faire gagner du temps.

## Composants des workflows agentiques

Voici les principaux composants d’un workflow agentique :

- **Agents d’IA** : en intelligence artificielle (IA), un workflow n’est pas agentique s’il ne comporte aucun agent d’IA. Un agent d’IA est un système ou à un programme capable de réaliser de manière autonome des tâches pour le compte d’un utilisateur ou d’un autre système. Pour ce faire, il conçoit son workflow et utilise les outils disponibles.

- **Grands modèles de langage (LLM)** : les grands modèles de langage sont au cœur des agents d’IA. Les LLM sont essentiels pour le traitement et la génération de texte en langage naturel. L’ajustement des paramètres LLM tels que la température entraînera également une qualité de sortie variable.

<!-- -->

- **Outils** : pour qu’un LLM puisse récupérer des informations autres que les données utilisées lors de son entraînement, nous devons lui fournir des outils. Parmi les outils couramment utilisés, citons les ensembles de données externes, les recherches sur le Web et les interfaces de programmation des applications (API). Nous pouvons utiliser des outils pour adapter un agent d’IA à des cas d’utilisation bien précis, et non seulement aux tâches de routine.

<!-- -->

- **Mécanismes de rétroaction** : les mécanismes de rétroaction, comme l’humain dans la boucle (HITL), voire d’autres agents, facilitent la prise de décision de l’agent d’IA et pilotent ses sorties.

<!-- -->

- **Prompt engineering** : les performances des workflows agentiques dépendent fortement de la qualité des prompts fournis. Le prompt engineering aide les modèles d’IA générative à mieux comprendre et traiter un large éventail de requêtes, des plus simples aux plus techniques. Les techniques courantes de prompt engineering comprennent la chaîne de pensée (CoT), le one-shot, le zero-shot et l’auto-réflexion.

<!-- -->

- **Collaboration multi-agent** : la communication et la résolution distribuée des problèmes au sein des systèmes multi-agents (MAS) sont essentielles aux cas d’utilisation complexes. Chaque agent d’un SMA se voit attribuer un ensemble d’outils, d’algorithmes, ainsi qu’un domaine de « compétences », pour que les agents ne réapprennent pas tous les mêmes informations et qu’ils partagent les informations qu’ils ont apprises avec les autres agents du MAS.

<!-- -->

- **Intégrations** : pour rationaliser les processus existants, les workflows agentiques doivent être intégrés à l'infrastructure existante. Cette synergie dépend des exigences et des objectifs du workflow agentique. L’intégration des données, le processus consistant à consolider les données dans une base de données centrale accessible aux agents, est souvent la première étape. Parmi les autres formes d’intégration, citons les frameworks d’agents tels que LangChain, LangGraph, crewAI et BeAI d’IBM. Ces frameworks d’orchestration d’agents peuvent servir de fournisseurs pour atteindre une échelle et des performances supérieures. L’intégration d’outils spécifiques au contexte est également essentielle pour obtenir des résultats pertinents.\

## L’impact des workflows agentiques

Une anecdote personnelle racontée par Andrew Ng, spécialiste de l’IA, met en évidence l’adaptabilité des workflows agentiques. Andrew se souvient de sa démonstration portant sur la création d’un agent IA, au cours de laquelle l’un des nombreux outils d’IA, une API de recherche Web, a échoué. Le système d’IA a pu rapidement gérer l’échec de la dépendance en utilisant un outil de recherche Wikipédia disponible. Le système a accompli la tâche et est resté adaptable à l’environnement changeant. La réduction du besoin de supervision humaine nous permettrait de nous consacrer moins aux tâches banales et répétitives, afin de nous concentrer sur les missions complexes, nécessitant une intelligence humaine.

Andrew Ng explique également que les workflows permettent non seulement d’exécuter des tâches, mais aussi d’entraîner la prochaine génération de LLM. Dans les workflows traditionnels sans agent, l’utilisation des sorties d’un LLM pour en entraîner un autre ne permet pas d’obtenir des résultats satisfaisants. En revanche, les workflows agentiques qui produisent des données de qualité favorisent un entraînement efficace.
