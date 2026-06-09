> Source : https://www.ibm.com/fr-fr/think/topics/react-agent

# Qu’est-ce qu’un agent ReAct ?

Un agent ReAct est un agent d’IA qui s’appuie sur le cadre « raisonnement et action » (« Reasoning and acting », ReAct) pour combiner le raisonnement par chaîne de pensée (CoT) avec l’utilisation d’outils externes. Le cadre ReAct améliore la capacité d’un grand modèle de langage (LLM) à gérer des tâches complexes et la prise de décision dans des workflows agentiques.

Présenté pour la première fois par Yao et d’autres chercheurs dans l’article « ReACT: Synergizing Reasoning and Acting in Language Models » publié en 2023, ReAct peut être défini de manière générale comme un paradigme de machine learning (ML) visant à intégrer les capacités de raisonnement et d’action des LLM.\
\
Plus précisément, ReAct est un cadre conceptuel permettant de créer des agents d’IA capables d’interagir avec leur environnement de manière structurée mais adaptable, grâce à un LLM qui sert de « cerveau » à l’agent pour coordonner toutes sortes d’actions,de la simple génération augmentée par récupération (RAG) à des workflows multi-agents complexes.

Contrairement aux systèmes d’intelligence artificielle (IA) traditionnels, les agents ReAct ne séparent pas la prise de décision de l’exécution des tâches. Par conséquent, le développement du paradigme ReAct a constitué une étape importante dans l’évolution de l’IA générative au-delà des simples chatbots conversationnels et vers la résolution de problèmes complexes.\
\
Les agents ReAct et les approches dérivées continuent d’alimenter des applications d’IA capables de planifier, d’exécuter et de s’adapter de manière autonome à des circonstances imprévues.

## Comment fonctionnent les agents ReAct ?

Le cadre ReAct s’inspire de la manière dont les humains peuvent intuitivement employer le langage naturel, souvent à travers leur monologue intérieur, pour planifier et exécuter étape par étape des tâches complexes.\
\
Plutôt que de mettre en œuvre des workflows basés sur des règles ou prédéfinis, les agents ReAct s’appuient sur les capacités de raisonnement de leur LLM pour s’adapter dynamiquement à de nouvelles informations ou aux résultats des étapes précédentes.

Imaginez que vous fassiez vos valises pour un court voyage. Vous pouvez commencer par identifier les éléments clés («*Quel temps fera-t-il pendant mon séjour ?* »), puis consulter activement des sources externes («*Je vais vérifier les prévisions météo locales* »).\
\
À partir de ces nouvelles informations (« *Il va faire froid* »), vous déterminez l’étape suivante (« *Quels vêtements chauds ai-je ?* ») et l’action à entreprendre (« *Je vais regarder dans mon placard* »). Lorsque vous effectuez cette action, un obstacle inattendu peut se présenter («*Tous mes vêtements chauds sont au grenier* ») et vous devez ajuster l’étape suivante en conséquence («*Quels vêtements puis-je superposer ?* »).

De manière similaire, le cadre ReAct utilise le prompt engineering pour structurer l’activité d’un agent d’IA selon un modèle formel alternant pensées, actions et observations :

- Les étapes de raisonnement verbalisées de la CoT (*pensées*) aident le modèle à décomposer la tâche globale en sous-tâches plus faciles à gérer.

<!-- -->

- Les *actions* prédéfinies permettent au modèle d’utiliser des outils, d’effectuer des appels d’interface de programmation des applications (API) et de recueillir davantage d’informations auprès de sources externes (telles que des moteurs de recherche) ou de bases de connaissances (telles qu’un magasin de documents interne).

<!-- -->

- Après avoir exécuté une action, le modèle réévalue sa progression et s’appuie sur cette *observation* pour fournir une réponse finale ou alimenter la *pensée* suivante. Idéalement, l’observation devrait également tenir compte des informations antérieures, qu’elles proviennent de la fenêtre contextuelle standard du modèle ou d’un composant de mémoire externe.

Étant donné que les performances d’un agent ReAct dépendent fortement de la capacité de son LLM central à penser « verbalement » pour accomplir des tâches complexes, les agents ReAct tirent grandement parti de modèles hautement performants dotés de capacités avancées de raisonnement et de suivi des instructions.

Afin de minimiser les coûts et la latence, un cadre ReAct multi-agents peut s’appuyer principalement sur un modèle plus vaste et plus performant qui sert d’agent central dont le processus de raisonnement ou les actions peuvent impliquer la délégation de sous-tâches à d’autres agents conçus à partir de modèles plus petits et plus efficaces.

### Boucles d’agent ReAct

Ce cadre crée intrinsèquement une boucle de rétroaction dans laquelle le modèle résout les problèmes en répétant de manière itérative ce processus entrelacé de *réflexion, d’action et d’observation*.

Chaque fois que cette boucle est effectuée, c’est-à-dire chaque fois que l’agent agit et fait une observation basée sur les résultats de cette action, il doit alors décider s’il faut répéter ou terminer la boucle.

Quand et comment mettre fin à la boucle de raisonnement est un élément important à prendre en compte dans la conception d’un agent ReAct. Fixer un nombre maximal d’itérations de boucle est un moyen simple de limiter la latence, les coûts et l’utilisation de tokens, et d’éviter la possibilité d’une boucle sans fin.\
\
À l’inverse, la boucle peut être configurée pour se terminer lorsqu’une condition spécifique est remplie, par exemple lorsque le modèle a identifié une réponse finale potentielle qui dépasse un certain seuil de confiance.

Pour mettre en œuvre ce type de boucle de raisonnement et d’action, les agents ReAct emploient généralement une variante du *prompting ReAct*, que ce soit dans le prompt système fourni au LLM ou dans le contexte de la requête de l’utilisateur elle-même.

## Prompting ReAct

Le prompting ReAct est une technique de prompting spécifique conçue pour guider un LLM afin qu’il suive le paradigme ReAct des boucles *pensée*, *action* et *observation*. Bien que l’usage explicite des méthodes de prompting ReAct conventionnelles ne soit pas strictement nécessaire pour développer un agent ReAct, la plupart des agents basés sur ReAct les implémentent ou s’en inspirent directement.

Décrite pour la première fois dans l’article original sur ReAct, la fonction principale du prompting ReAct est d’indiquer à un LLM de suivre la boucle ReAct et de déterminer les outils qui peuvent être employés (ou les actions qui peuvent être entreprises) lors du traitement des requêtes des utilisateurs.

Que ce soit par le biais d’instructions explicites ou de l’inclusion d’exemples few-shot, le prompting ReAct doit :

- **Guider le modèle pour qu’il utilise un raisonnement en chaîne** : invitez le modèle à raisonner pour accomplir des tâches en réfléchissant étape par étape, en enchaînant les pensées et les actions.

<!-- -->

- **Définir les actions** : définissez les actions spécifiques disponibles pour le modèle. Une action peut impliquer la génération d’un type spécifique de pensée suivante ou de sous-prompt, mais elle nécessite généralement des outils externes ou la création d’API.

<!-- -->

- **Demander au modèle de faire des observations** : invitez le modèle à réévaluer son contexte après chaque étape d’action et à se baser sur ce contexte actualisé pour alimenter l’étape de raisonnement suivante.

<!-- -->

- **Boucle** : demandez au modèle de répéter les étapes précédentes si nécessaire. Vous pouvez fournir des conditions spécifiques pour mettre fin à cette boucle, telles qu’un nombre maximal de boucles, ou demander à l’agent de mettre fin à son processus de raisonnement lorsqu’il estime être parvenu au résultat final correct.

<!-- -->

- **Fournir la réponse finale** : lorsque ces conditions de fin sont remplies, fournissez à l’utilisateur le résultat final en réponse à sa requête initiale. Comme pour de nombreuses utilisations des LLM, en tant que modèles de raisonnement utilisant un raisonnement en chaîne avant de déterminer un résultat final, les agents ReAct sont souvent invités à mener leur processus de raisonnement dans un « bloc-notes ». 

Une démonstration classique du prompting ReAct est le prompt système pour le préconstruit`ZERO_SHOT_REACT-DESCRIPTION` Module d’agents ReAct dans Langchain de LangGraph. Il est appelé « zero-shot » car, avec ce prompt système prédéfini, le LLM utilisé avec le module n’a besoin d’aucun autre exemple pour se comporter comme un agent ReAct.

```
Answer the following questions as best you can. You have access to the following tools: 

Wikipedia: A wrapper around Wikipedia. Useful for when you need to answer general questions about people, places, companies, facts, historical events, or other subjects. Input should be a search query.
duckduckgo_search: A wrapper around DuckDuckGo Search. Useful for when you need to answer questions about current events. Input should be a search query.
Calculator: Useful for when you need to answer questions about math.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [Wikipedia, duckduckgo_search, Calculator]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
```

## Avantages des agents ReAct

L’introduction du cadre ReAct constitué une étape importante dans l’avancement des workflows agentiques basés sur les LLM. De l’ancrage des LLM en temps réel dans des informations externes du monde réel grâce au RAG (Real-World Grounding) à la contribution à des avancées ultérieures, telles que Reflexion, qui a conduit aux modèles de raisonnement modernes, ReAct a contribué à catalyser l’utilisation des LLM pour des tâches qui vont bien au-delà de la génération de texte.

L’utilité des agents ReAct découle en grande partie de certaines qualités inhérentes au cadre ReAct :

- **Polyvalence** : les agents React peuvent être configurés pour fonctionner avec un large éventail d’outils externes et d’API. Bien que le réglage fin des prompts ReAct pertinents (à l’aide d’outils adaptés) puisse améliorer les performances, aucune configuration préalable du modèle n’est nécessaire pour exécuter les appels d’outil.

<!-- -->

- **Adaptabilité** : cette polyvalence, associée à la nature dynamique et situationnelle de la manière dont ils déterminent l’outil ou l’API approprié à appeler, signifie que les agents ReAct peuvent utiliser leur processus de raisonnement pour s’adapter à de nouveaux défis. En particulier lorsqu’ils opèrent dans un contexte étendu ou lorsqu’ils sont augmentés par une mémoire externe, ils peuvent tirer des leçons de leurs erreurs et de leurs réussites passées pour faire face à des obstacles et à des situations imprévus. Cela rend les agents ReAct flexibles et résilients.

<!-- -->

- **Explicabilité** : le processus de raisonnement verbalisé d’un agent ReAct est simple à suivre, ce qui facilite le débogage et contribue à rendre leur création et leur optimisation relativement conviviales.

<!-- -->

- **Précision** : comme l’affirme l’article original sur ReAct, le raisonnement par chaîne de pensée (CoT) présente à lui seul de nombreux avantages pour les LLM, mais il comporte également un risque accru d’hallucination. La combinaison du CoT et d’une connexion externe aux sources d’information de ReAct réduit considérablement les hallucinations, rendant les agents ReAct plus précis et plus fiables.

## Agents ReAct et appels de fonction

Introduit initialement par OpenAI en juin 2023 pour renforcer les capacités agentiques de ses modèles GPT, l’appel de fonction constitue un autre paradigme important de l’IA agentique.

Le paradigme de l’appel de fonction implique d’ajuster les modèles afin qu’ils reconnaissent quand une situation particulière doit donner lieu à un appel d’outil et produire un objet JSON structuré contenant les arguments nécessaires pour appeler ces fonctions.\
\
De nombreuses familles de LLM propriétaires et open source, notamment IBM Granite, la série Llama de Meta, Claude d’Anthropic et Google Gemini, prennent désormais en charge les appels de fonction.

Que ReAct ou l’appel de fonction soit « meilleur » dépend généralement de la nature de votre cas d’utilisation. Dans des scénarios impliquant des tâches relativement simples (ou du moins prévisibles), l’appel de fonction peut s’exécuter plus rapidement, économiser des tokens et être plus simple à implémenter qu’un agent ReAct.Dans de telles circonstances, le nombre de tokens qui seraient dépensés pour la boucle itérative de raisonnement CoT d’un agent ReAct pourrait être considéré comme inefficace.

Le compromis inhérent à cette approche réside dans une relative incapacité à personnaliser la manière dont le modèle choisit l’outil à utiliser et à quel moment. De même, lorsqu’un agent traite des tâches qui exigent un raisonnement complexe ou des scénarios dynamiques ou imprévisibles, la rigidité de l’appel de fonction peut limiter sa capacité d’adaptation. Dans de telles situations, la visualisation du raisonnement étape par étape qui a conduit à l’appel d’un outil spécifique est souvent utile.

## Premiers pas avec les agents ReAct

Les agents React peuvent être conçus et implémentés de plusieurs manières, qu’ils soient codés à partir de zéro en Python ou développés à l’aide de frameworks open source tels que BeAI. La popularité et la longévité du paradigme ReAct ont donné lieu à une vaste littérature et à des tutoriels pour les agents ReAct sur GitHub et d’autres communautés de développeurs.

Comme alternative au développement d’agents ReAct personnalisés, de nombreux cadres d’IA agentique, notamment BeeAI, LlamaIndex et LangGraph de LangChain, proposent des modules d’agents ReAct préconfigurés pour des cas d’utilisation spécifiques.
