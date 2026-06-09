> Source : https://www.ibm.com/fr-fr/think/topics/rewoo

# Qu’est-ce que ReWOO ?

ReWOO (abréviation de « reasoning without observation », « raisonnement sans observation » en français) est un cadre qui rend les [grands modèles de langage](https://www.ibm.com/fr-fr/think/topics/large-language-models) (LLM) plus rentables et plus précis dans certaines applications de raisonnement complexes. Les modèles avec ReWOO s’engagent dans un processus de [raisonnement](https://www.ibm.com/fr-fr/think/topics/ai-reasoning) autour d’un problème avant d’essayer de le résoudre, ce qui permet d’améliorer l’efficacité, la précision et la robustesse en cas de défaillance de l’outil.

Les premiers LLM (comme les [modèles GPT-1 et GPT-2](https://www.ibm.com/fr-fr/think/topics/gpt) d’OpenAI) fournissaient des réponses directes ; la vague suivante de modèles de [chaîne de pensée](https://www.ibm.com/fr-fr/think/topics/chain-of-thoughts), qui a débuté en 2022, ajoutait un élément de raisonnement externalisé. En effet, les modèles « pensaient à haute voix » lorsqu’ils parvenaient à une réponse, améliorant ainsi la précision et l’explicabilité. 

Vint ensuite une génération de modèles de langage augmentés (« systèmes ALM ») et d’agents IA, qui ajoutaient des capacités d’appel d’outils à ce raisonnement. Les premiers cadres ALM, comme [ReAct](https://www.ibm.com/fr-fr/think/topics/react-agent), suivent un schéma de pensée-action-observation : le système observe ce qu’il génère avant de recommencer à y réfléchir. Bien qu’ils soient généralement efficaces, les cadres comme ReAct peuvent enregistrer une forte consommation de tokens, car chaque [appel d’outil](https://www.ibm.com/fr-fr/think/topics/tool-calling) ultérieur doit inclure tout l’historique de conversation qui le précède, un coût qui s’alourdit à chaque étape. 

ReWOO s’affranchit du schéma penser-agir-observer en dissociant le raisonnement des observations externes, ce qui permet au modèle de planifier sa chaîne de raisonnement en interne avant d’invoquer de manière sélective les outils ou de récupérer des informations. Cette séparation évite les allers-retours inutiles et permet au modèle de conserver son plan tout au long de la tâche.

## Comment fonctionne ReWOO ?

ReWOO utilise trois modules distincts, qui divisent et maîtrisent les tâches complexes. Tout d’abord, le module Planner établit un schéma directeur indiquant la manière dont le modèle se comportera en fonction du prompt de l’utilisateur. Deuxièmement, le module Worker exécute le plan, en appelant des outils externes (sans répéter les appels d’API LLM coûteux pour « réfléchir », comme dans ReAct). Enfin, le module Solver récupère les plans et les preuves, synthétisant la réponse finale. 

Si la différence d’approche semble mineure, les résultats sont spectaculaires : ReWOO est tout aussi performant (voire légèrement plus) que ReAct selon certains [benchmarks](https://www.ibm.com/fr-fr/think/topics/llm-benchmarks), tout en utilisant environ 80 % de tokens en moins. (Un [token](https://www.ibm.com/docs/en/watsonx/saas?topic=solutions-tokens) est une unité sémantique pour les modèles d’IA ; plus il y en a, plus le coût d’exploitation est élevé.) Par exemple, sur le jeu de données HotpotQA (une batterie de questions utilisée pour évaluer les systèmes d’IA), ReWOO atteint une précision de 42,4 % en utilisant 2 000 tokens, tandis que ReAct atteint une précision de 40,8 % avec 10 000 tokens.  

Surtout, ce [gain d’efficacité des tokens](https://developer.ibm.com/articles/awb-token-optimization-backbone-of-effective-prompt-engineering/) rend [les modèles de raisonnement](https://www.ibm.com/fr-fr/think/topics/reasoning-model) économiquement viables à l’échelle.

## ReAct et ReWoo : un exemple concret

Pour illustrer la différence entre ces deux cadres courants d’[IA générative](https://www.ibm.com/fr-fr/think/topics/generative-ai), examinons un cas d’utilisation spécifique. Considérons les différentes façons dont les systèmes ReAct et ReWOO aborderaient la question d’un utilisateur qui demande de l’aide pour préparer ses bagages en vue d’un voyage impliquant un vol entre New York et Chicago demain, et un trajet en voiture jusqu’à Milwaukee le lendemain.

Le système ReAct décomposerait le problème en trois cycles de pensée-action-observation avant de donner sa réponse finale. Lors du premier cycle, il penserait : « Je dois vérifier la météo pour demain à New York », en utilisant la [génération augmentée par récupération](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation) (RAG) pour rechercher ces informations (une action), et enfin observer le résultat. Ces résultats servent ensuite de point de départ d’un autre cycle réfléchir-agir-observer en trois étapes pour la météo à Chicago. Troisièmement, il ferait la même chose pour la météo à Milwaukee. Enfin, il rassemblerait ses conclusions dans une sortie (par exemple, « Prévoir plusieurs couches, car il fait plus froid à chaque endroit »). 

Le système de type ReWOO, quant à lui, gagnerait en efficacité en effectuant toute la planification à l’avance. Tout d’abord, il planifierait comme suit : « J’ai besoin de savoir la météo de demain à New York, la météo de demain à Chicago, et la météo à Milwaukee le lendemain. » Ensuite, il appellerait les API météorologiques dans une séquence serrée (ou potentiellement en parallèle), sans « réfléchir » à cette étape fastidieuse. Enfin, il résoudrait le problème en rassemblant les preuves et en produisant une réponse finale.  

## Avantages et inconvénients de ReWOO

Outre l’économie de tokens, ReWOO démontre un avantage supplémentaire : la robustesse en cas de défaillance d’un outil. Si un outil ne fonctionne pas sous ReAct, par exemple, le système peut se retrouver dans une boucle infinie (car le LLM interrogerait de manière répétée une base de données défaillante pour obtenir la météo à Chicago, par exemple).

ReWOO est plus agile. Même si un outil ne renvoie pas l’élément de preuve demandé, le plan général est toujours en place : le module Worker peut progresser, et le module Solver sera en mesure de fournir au moins une réponse partielle. Dans l’exemple de la météo, au lieu de s’enfermer dans une boucle infinie ou excessive en interrogeant une base de données sur la météo à Chicago, le module Solver renverrait au moins une réponse informant l’utilisateur de la météo à New York et à Milwaukee (en supposant que le module Worker soit en mesure de récupérer ces éléments), ce qui pourrait en fin de compte suffire pour répondre aux besoins de l’utilisateur. 

Malgré ses avantages, ReWOO n’est pas un cadre absolument supérieur ; il est tout simplement meilleur pour certains types de tâches, en particulier lorsque les types et les quantités de preuves nécessaires sont régulières et prévisibles. Là où ReWOO échoue, c’est face aux problèmes moins prévisibles ou moins structurés qui demandent de la créativité, de l’exploration ou de l’improvisation. S’il excelle en présence d’inconnues connues, ReWOO échoue face aux inconnues inconnues.

Par exemple, ReWOO ne serait pas une solution optimale pour déboguer le code Python, un processus exploratoire et itératif où chaque correctif peut générer de nouvelles erreurs et de nouveaux indices, devenant rapidement caducs. Un cadre plus adaptable comme ReAct, bien que moins économique en tokens dans l’abstrait, serait finalement mieux adapté à un tel problème. 

## Comment mettre en œuvre ReWOO ?

Comme pour la plupart des systèmes et cadres d’IA, différentes approches sont disponibles pour la mise en œuvre des workflows ReWOO. Une mise en œuvre « officielle » du cadre, qui a été décrite pour la première fois par le chercheur Binfeng Xu (et ses collègues, en 2023\[1\]), est disponible sur Github. Les cadres d’IA générative comme [LangGraph](https://www.ibm.com/fr-fr/think/topics/langgraph) (qui appelle ses modules « nœuds ») et [LangChain](https://www.ibm.com/fr-fr/think/topics/langchain), sont également très utilisés. Une méthode de raisonnement à plusieurs étapes de type ReWOO est également disponible avec [IBM Granite](https://www.ibm.com/fr-fr/think/tutorials/build-rewoo-reasoning-agent-granite#1793360183).

À un niveau conceptuel, on peut se lancer avec ReWOO dans tout environnement LLM à l’aide d’un prompt bien conçu, qui encourage simplement l’IA à élaborer un plan étape par étape pour répondre aux questions suivantes avant de passer à une entrée d’outil. 

L’article décrivant pour la première fois ReWOO comprend des exemples de prompt, dont un qui commence ainsi : « Pour la tâche suivante, élaborer des plans qui peuvent résoudre le problème étape par étape. Pour chaque plan, indiquer l’outil externe avec l’entrée d’outil pour récupérer les preuves. » Les auteurs de l’étude ajoutent toutefois : « ReWOO est un paradigme général, et les prompts ne sont pas nécessairement fixes. Nous encourageons les lecteurs et les utilisateurs à adapter les prompts à leurs propres besoins. »1
