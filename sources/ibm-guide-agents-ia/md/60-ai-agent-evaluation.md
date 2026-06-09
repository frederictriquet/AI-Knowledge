> Source : https://www.ibm.com/fr-fr/think/topics/ai-agent-evaluation

# Qu’est-ce que l’évaluation des agents IA ?

L’évaluation des agents IA fait référence au processus d’évaluation et de compréhension des performances d’un agent IA dans l’exécution de tâches, la prise de décisions et l’interaction avec les utilisateurs. Compte tenu de leur autonomie inhérente, l’évaluation des agents est essentielle pour promouvoir leur bon fonctionnement. Les agents IA doivent se comporter conformément à l’intention de leurs concepteurs, être efficaces et respecter certains principes d’IA éthique pour répondre aux besoins de l’entreprise. L’évaluation permet de vérifier que les agents répondent à ces exigences et d’améliorer la qualité des agents en identifiant les domaines à affiner et à optimiser.

Les agents d’IA générative sont souvent évalués sur des tâches traditionnelles de synthèse de texte, similaires aux de référence standards des [grands modèles de langage](https://www.ibm.com/fr-fr/think/topics/large-language-models) (LLM), [](https://www.ibm.com/fr-fr/think/topics/llm-benchmarks)où des indicateurs tels que la cohérence, la pertinence et la fidélité du texte généré sont couramment utilisés. Cependant, les agents d’IA générative effectuent généralement des opérations plus larges et plus complexes, comme le raisonnement en plusieurs étapes, l’appel d’outils et l’interaction avec des systèmes externes, qui nécessitent une évaluation plus complète. Même lorsque la production finale est du texte, elle peut être le résultat d’actions intermédiaires telles que l’interrogation d’une base de données ou l’appel d’une API, chacune devant être évaluée séparément.

Dans d’autres cas, il se peut que l’agent ne produise pas de sortie textuelle du tout, mais effectue une tâche telle que la mise à jour d’un enregistrement ou l’envoi d’un message, où la réussite est mesurée par la bonne exécution de la tâche. Par conséquent, l’évaluation doit aller au-delà de la qualité du texte en surface et mesurer le comportement global des agents, la réussite des tâches et la cohérence par rapport à l’intention de l’utilisateur. En outre, afin d’éviter le développement d’agents hautement performants mais gourmands en ressources, qui limitent leur déploiement pratique, des mesures de coût et d’efficacité doivent être incluses dans l’évaluation.

Au-delà de la mesure de la performance dans l’exécution des tâches, l’évaluation des agents IA doit donner la priorité à des dimensions critiques telles que la sécurité, la fiabilité, la conformité aux politiques et l’atténuation des biais. Ces facteurs sont essentiels pour déployer des agents dans des environnements réels à haut risque. L’évaluation permet de s’assurer que les agents évitent les comportements nuisibles ou dangereux, qu’ils conservent la confiance des utilisateurs grâce à des résultats prévisibles et vérifiables, et qu’ils résistent à la manipulation ou à l’utilisation abusive.

Pour atteindre ces objectifs fonctionnels (qualité, coût) et non fonctionnels (sécurité), les méthodes d’évaluation peuvent inclure des tests de référence, des évaluations humaines dans la boucle, des tests A/B et des simulations réelles. En évaluant systématiquement les agents IA, les entreprises peuvent améliorer leurs capacités en matière d’IA, optimiser leurs efforts d’[automatisation](https://www.ibm.com/fr-fr/think/topics/automation?_gl=1*wslfec*_ga*NDQ4NjQ1NjE5LjE3Mzg2MTk3ODg.*_ga_FYECCCS21D*czE3NDg4ODAyODckbzEwNyRnMCR0MTc0ODg4MDI4NyRqNjAkbDAkaDA.) et renforcer leurs fonctions métier tout en minimisant les risques associés à une [IA agentique](https://www.ibm.com/fr-fr/think/topics/agentic-ai) non sécurisée, peu fiable ou biaisée.

## Comment fonctionne l’évaluation des agents IA ?

L’évaluation d’un agent IA nécessite une approche structurée dans un cadre des exigences d’observabilité formel plus large. Les méthodes d’évaluation (ou éval) diffèrent considérablement, mais le processus implique généralement les étapes suivantes :

### 1. Définir les objectifs de l’évaluation et les indicateurs

Quel est l’objectif de l’agent ? Quels sont les résultats attendus ? Comment l’IA est-elle utilisée dans des scénarios réels ?

Voir « Indicateurs d’évaluation des agents IA » pour connaître certains des indicateurs les plus populaires, qui entrent dans les catégories suivantes : performance, interaction et expérience, IA responsable, système et efficacité et indicateurs spécifiques aux tâches.

### 2. Collecter des données et préparer les tests

Pour évaluer efficacement l’agent IA, utilisez des jeux de données d’évaluation représentatifs, y compris diverses entrées qui reflètent des scénarios réels et des scénarios de test qui simulent des conditions en temps réel. Les données annotées représentent une vérité terrain par rapport à laquelle les modèles IA peuvent être testés.

Planifiez chaque étape potentielle du workflow d’un agent, qu’il s’agisse d’appeler une API, de transmettre des informations à un deuxième agent ou de prendre une décision. En décomposant le workflow de l’IA en éléments individuels, vous pouvez plus facilement évaluer la manière dont l’agent gère chaque étape. Tenez également compte de l’approche globale de l’agent tout au long du workflow, c’est-à-dire le cheminement qu’il suit pour résoudre un problème en plusieurs étapes.

### 3. Réaliser des tests

Exécutez l’agent IA dans différents environnements, si possible avec différents LLM, et suivez la performance. Analysez les étapes des agents individuels et évaluez-les. Par exemple, surveillez l’utilisation par l’agent IA de la génération augmentée de récupération (RAG) pour récupérer des informations à partir d’une base de données externe, ou la réponse à un appel d’API.

### 4. Analyser les résultats

Comparez les résultats aux critères de réussite prédéfinis s’il y en a ; si ce n’est pas le cas, utilisez un LLM en tant que juge (voir ci-dessous). Évaluez les compromis en mettant en balance les performances et les considérations éthiques.

L’agent a-t-il choisi le bon outil ? A-t-il appelé la bonne fonction ? A-t-il transmis la bonne information dans le bon contexte ? A-t-il produit une réponse factuellement correcte ?

L’appel de fonctions et l’utilisation d’outils sont une capacité fondamentale pour construire des agents intelligents capables de fournir des réponses en temps réel et contextuellement précises. Envisagez d’utiliser une évaluation et une analyse dédiées utilisant une approche basée sur des règles, ainsi qu’une évaluation sémantique utilisant un LLM en tant que juge.

Le LLM-as-a-judge, ou LL en tant que juge, est un système d’évaluation automatisé qui évalue la performance des agents IA à l’aide de critères et d’indicateurs prédéfinis. Au lieu de s’appuyer uniquement sur des examinateurs humains, un LLM en tant que juge applique des algorithmes, des heuristiques ou des modèles de notation basés sur l’IA pour évaluer les réponses, les décisions ou les actions d’un agent IA.

Voir « Indicateurs d’évaluation de l’appel de fonctions » ci-dessous.

### 5. Optimiser et itérer

Les développeurs peuvent désormais modifier les prompts, déboguer les algorithmes, rationaliser la logique ou configurer les architectures agentiques en fonction des résultats de l’évaluation. Par exemple, les cas d’utilisation du support client peuvent être améliorés en accélérant la génération de réponses et les délais d’exécution des tâches. L’efficacité du système peut être optimisée en termes d’évolutivité et d’utilisation des ressources.

## Indicateurs courants pour l’évaluation des agents IA

Les développeurs veulent que les agents fonctionnent comme prévu. Et compte tenu de l’autonomie de l’IA des agents, il est important de comprendre le « pourquoi » des décisions prises par l’IA. Nous vous présentons quelques-uns des indicateurs les plus courants que les développeurs peuvent utiliser pour évaluer correctement leurs agents.

### Spécifique à une tâche

Selon l’application de l’IA, des indicateurs d’évaluation spécifiques de la qualité peuvent s’appliquer :

- le **LLM en tant que juge** évalue la qualité de la génération de texte par l’IA, indépendamment de la disponibilité de données de référence.
- **BLEU et ROUGE** sont des alternatives moins coûteuses qui évaluent la qualité du texte généré par l’IA en le comparant à du texte écrit par des humains.

Parmi les autres indicateurs fonctionnels pour évaluer la performance des agents IA, on trouve :

- Le **taux de réussite/achèvement des tâches** mesure la proportion de tâches ou d’objectifs que l’agent réalise correctement ou de manière satisfaisante par rapport au nombre total de\
  tentatives.
- Le **taux d’erreur** est le pourcentage de résultats incorrects ou d’opérations ratées.
- Le **coût** mesure l’utilisation des ressources, comme les tokens ou le temps de calcul.
- La **latence** est le temps nécessaire à un agent IA pour traiter et renvoyer les résultats.

### IA éthique et responsable

- La **vulnérabilité à l’injection de prompts** évalue le taux de réussite des prompts malveillants qui modifient le comportement prévu de l’agent.
- Le **taux de respect des politiques** est le pourcentage de réponses conformes aux politiques organisationnelles ou éthiques prédéfinies.
- Le **score de biais et d’équité** détecte les disparités dans la prise de décision de l’IA entre différents groupes d’utilisateurs.

### Interaction et expérience utilisateur

Pour les agents d’IA qui interagissent avec les utilisateurs, tels que les chatbots et les assistants virtuels, les évaluateurs examinent ces indicateurs.

- Le **score de satisfaction des utilisateurs (CSAT)** mesure la satisfaction des utilisateurs vis-à-vis des réponses de l’IA.

- Le **taux d’engagement** indique la fréquence à laquelle les utilisateurs interagissent avec le système d’IA.

- Le **flux conversationnel** évalue la capacité de l’IA à maintenir des conversations cohérentes et significatives.

- Le **taux d’achèvement des tâches** mesure l’efficacité avec laquelle l’agent IA aide les utilisateurs à accomplir une tâche.

### Appel de fonction

Ces indicateurs basés sur des règles permettent d’évaluer l’efficacité opérationnelle des systèmes pilotés par l’IA :

- **Nom de fonction incorrect** : l’agent a tenté d’appeler une fonction qui existe, mais a utilisé un nom ou une orthographe incorrects, ce qui a entraîné un échec de l’exécution.
- **Paramètres requis manquants** : l’agent a lancé un appel de fonction, mais a omis un ou plusieurs paramètres nécessaires à son fonctionnement.
- **Type de valeur de paramètre incorrect** : l’agent a fourni une valeur de paramètre, mais son type (chaîne, nombre, booléen) ne correspondait pas à ce que la fonction attendait.
- **Valeurs autorisées** : l’agent a utilisé une valeur qui ne fait pas partie de l’ensemble des valeurs acceptées ou prédéfinies pour un paramètre spécifique.
- **Paramètre halluciné** : l’agent a inclus un paramètre dans l’appel de fonction qui n’est pas défini ou pris en charge par la spécification de la fonction.

Voici quelques indicateurs sémantiques basés sur le LLM en tant que juge.

- L’**ancrage des valeurs des paramètres** aide à garantir que chaque valeur de paramètre est directement dérivée du texte de l’utilisateur, de l’historique du contexte (comme les sorties précédentes des appels d’API) ou des valeurs par défaut des spécifications de l’API.
- La **transformation des unités** vérifie les conversions d’unités ou de formats (au-delà des types de base) entre les valeurs dans le contexte et les valeurs des paramètres dans l’appel d’outil.
