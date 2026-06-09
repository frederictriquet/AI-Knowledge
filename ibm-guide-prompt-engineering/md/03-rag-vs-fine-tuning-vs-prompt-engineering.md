> Source : https://www.ibm.com/fr-fr/think/topics/rag-vs-fine-tuning-vs-prompt-engineering

# RAG, réglage fin et prompt engineering

Le [prompt engineering](https://www.ibm.com/fr-fr/think/topics/prompt-engineering), le [réglage fin](https://www.ibm.com/fr-fr/think/topics/fine-tuning) et la [génération augmentée de récupération (RAG)](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation) sont trois méthodes d’optimisation que les entreprises peuvent employer pour tirer davantage de valeur des [grands modèles de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models). Ces trois méthodes optimisent le comportement des modèles, mais le choix de l’une d’entre elles dépend du cas d’utilisation visé et des ressources disponibles.

Les modèles d’[IA générative](https://www.ibm.com/fr-fr/think/topics/generative-ai) sont entraînés à partir de vastes ensembles de données, dont la plupart sont recueillies sur Internet. Les développeurs d’[intelligence artificielle](https://www.ibm.com/fr-fr/think/topics/artificial-intelligence) n’ont généralement pas accès aux données de niche, telles que les données internes et propriétaires d’une entreprise. Lorsque les organisations souhaitent appliquer de [grands modèles de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models) à des besoins spécifiques, elles doivent modifier la façon dont le [modèle d’IA](https://www.ibm.com/fr-fr/think/topics/ai-model) générative fonctionne pour produire les résultats et le comportement escomptés.

Le prompt engineering, la RAG et le réglage fin permettent d’optimiser les résultats d’un LLM pour des cas d’utilisation ciblés. Grâce à eux, les data scientists peuvent obtenir de meilleures performances en aval, une plus grande précision spécifique au domaine et des résultats qui répondent aux exigences de formatage, de langue ou de réglementation.

## Quelle est la différence entre la RAG, le réglage fin et le prompt engineering ?

Quatre domaines principaux se distinguent :

- Approche

<!-- -->

- Objectifs

<!-- -->

- Besoins en ressources 

<!-- -->

- Applications

### Approche

Le prompt engineering optimise les prompts d’entrée afin d’orienter un modèle vers de meilleurs résultats. Le réglage fin des LLM permet de les entraîner à l’aide de jeux de données spécifiques à un domaine afin d’augmenter les performances dans les tâches en aval. La RAG connecte un LLM à une base de données et automatise la recherche d’informations afin d’enrichir les prompts avec des données pertinentes pour une plus grande précision.

### Objectifs

La RAG, le prompt engineering et le réglage fin ont le même résultat général : améliorer la performance d’un modèle pour maximiser la valeur pour l’entreprise qui l’exploite. Plus précisément, le prompt engineering doit permettre à un modèle de fournir les résultats souhaités par l’utilisateur. La RAG vise à guider un modèle pour qu’il produise des résultats plus pertinents et plus précis. 

Un modèle affiné est entraîné à nouveau sur un ensemble ciblé de données externes afin d’améliorer les performances dans des cas d’utilisation spécifiques. Les trois méthodes sont complémentaires et sont souvent associées pour obtenir des résultats optimaux. 

### Besoins en ressources

Parmi les trois techniques d’optimisation, le prompt engineering est celle qui prend le moins de temps et qui mobilise le moins de ressources. Le prompt engineering de base peut être réalisé manuellement sans aucun investissement dans des capacités de calcul supplémentaires.

La RAG nécessite une expertise en science des données pour organiser les jeux de données de l’entreprise et créer les pipelines de données qui connectent les LLM à ces sources de données. Le réglage fin est sans doute le plus exigeant, car les processus de préparation et d’entraînement des données sont très gourmands en temps et en ressources informatiques.

### Applications

Le prompt engineering est le plus flexible et se distingue dans les situations ouvertes avec un éventail potentiellement diversifié de résultats, comme lorsqu’on demande à un LLM de générer du contenu à partir de zéro. La réussite de la génération d’images, de vidéos et de textes repose sur des prompts de qualité.

Le réglage fin affine un modèle pour un travail très ciblé, lorsque les data scientists ont besoin d’un modèle très performant dans un domaine précis. La RAG est une solution idéale lorsque des informations précises, pertinentes et actuelles sont primordiales, comme dans le cas des [chatbots](https://www.ibm.com/fr-fr/think/topics/chatbots) de service client.

## Pourquoi le prompt engineering, la RAG et le réglage fin sont-ils importants ?

Le prompt engineering propose toute une gamme de méthodes permettant de donner aux modèles des instructions explicites sur leur comportement. Avec des directives claires, le comportement du modèle peut être sculpté plus précisément sans avoir à investir dans des systèmes de récupération ou d’entraînement gourmands en ressources.

La RAG permet à un LLM d’accéder à des données propriétaires en temps réel qui lui seraient autrement inaccessibles. Les modèles RAG peuvent fournir des réponses plus précises grâce au contexte supplémentaire fourni par ces données internes.

Un modèle affiné surpasse généralement son modèle de base correspondant, tel que ceux de la famille [GPT](https://www.ibm.com/fr-fr/think/topics/gpt), lorsqu’il applique son entraînement à des données spécifiques à un domaine. Grâce à un meilleur accès aux connaissances externes, un LLM affiné a une meilleure compréhension du domaine spécifique et de sa terminologie.

## Qu’est-ce que le prompt engineering ?

Le prompt engineering est le processus de création de prompts efficaces qui guident un modèle vers les résultats souhaités sans élargir sa base de connaissances. Ce processus ne modifie pas de manière significative les paramètres d’un modèle pré-entraîné.

L’objectif du prompt engineering est de créer des prompts qui amènent les sorties d’un modèle à répondre aux exigences spécifiques du cas d’utilisation envisagé. Un entraînement plus poussé et un accès plus large aux données ne peuvent pas compenser des prompts de mauvaise qualité.

### Comment fonctionne le prompt engineering ?

Le prompt engineering consiste à ajuster la structure et le contenu des prompts d’entrée en se basant sur les sorties précédentes du modèle. À chaque itération, le prompt engineering apprend comment le modèle répond aux entrées précédentes, puis se sert de ces résultats pour informer le prompt suivant. L’objectif est de modifier le comportement du modèle par le biais d’instructions claires.

Un prompt engineering efficace repose sur des prompts qui indiquent à un modèle de [traitement automatique du langage naturel (NLP)](https://www.ibm.com/fr-fr/think/topics/natural-language-processing) exactement ce qu’il doit faire. Le processus de prompt engineering suppose d’expérimenter le contenu, la structure et le langage du prompt afin de découvrir le format optimal qui permet au modèle d’obtenir les résultats souhaités.

Comparons un modèle de machine learning à un cuisinier en herbe qui souhaite préparer un bon dîner. Le prompt engineering correspondrait à un proche mieux informé qui l’aiderait à planifier son approche du repas. Avec des conseils avisés sur ce qu’il faut faire et sur la manière de le faire, le cuisinier en herbe a plus de chances de préparer un repas délicieux.

## Qu’est-ce que la génération augmentée par récupération (RAG) ?

La RAG est un cadre d’architecture de données qui relie un LLM à d’autres données, telles que les données propriétaires d’une organisation, souvent stockées dans des [data lakehouses](https://www.ibm.com/fr-fr/think/topics/data-lakehouse). Les systèmes RAG ajoutent des données pertinentes aux prompts LLM afin que le LLM puisse générer des réponses plus précises.

### RAG : comment ça marche ?

La génération augmentée de récupération consiste à localiser les données pertinentes par rapport à la requête de l’utilisateur, puis à utiliser ces données pour créer des prompts plus informatifs. Un mécanisme de récupération d’informations est ajouté pour compléter les prompts du LLM et l’aider à générer des réponses plus pertinentes.

Les modèles RAG génèrent des réponses par le biais d’un processus en quatre étapes :

1.  Requête : un utilisateur soumet une requête qui lance le système RAG.

2.  Récupération d’informations : des algorithmes complexes ou des API passent au peigne fin les bases de connaissances internes et externes à la recherche d’informations pertinentes. 

3.  Intégration : les données récupérées sont combinées à la requête de l’utilisateur et transmises au modèle RAG pour qu’il y réponde. À ce stade, le LLM n’a pas encore traité la requête.

4.  Réponse : en combinant les données récupérées à ses données d’entraînement et aux connaissances stockées, le LLM génère une réponse adaptée au contexte.

Lorsqu’ils recherchent des documents, les systèmes RAG utilisent la recherche sémantique. Les bases de données vectorielles organisent les données par similarité, permettant ainsi des recherches par signification plutôt que par mot-clé. Les techniques de recherche sémantique permettent aux algorithmes RAG d’aller au-delà des mots-clés pour atteindre l’intention d’une requête et renvoyer les données les plus pertinentes.

Les systèmes RAG nécessitent une construction et une maintenance élaborées de l’architecture de données. Les [ingénieurs de données](https://www.ibm.com/fr-fr/think/topics/data-engineering) doivent créer les pipelines de données nécessaires pour connecter les data lakehouses de leur organisation au LLM et exploiter la RAG. Les systèmes RAG ont également besoin du prompt engineering pour localiser les bonnes données et s’assurer que le LLM sait comment s’en servir.

Encore une fois, imaginez un modèle d’IA générative comme un cuisinier en herbe à la maison. Il connaît les bases de la cuisine, mais n’a pas les informations et les connaissances spécialisées d’un chef formé à une cuisine plus sophistiquée. La RAG est comme donner un livre de recettes à un cuisinier. En combinant ses connaissances culinaires générales avec les recettes du livre de cuisine, il peut facilement confectionner ses plats préférés.

## Qu’est-ce que le réglage fin ?

Le réglage fin consiste à réentraîner un modèle pré-entraîné sur un ensemble de données d’apprentissage plus petit et plus ciblé pour lui apporter des connaissances spécifiques au domaine. Le modèle ajuste ensuite ses paramètres (les directives régissant son comportement) et ses plongements lexicaux (embeddings) pour mieux s’adapter à l’ensemble de données spécifique.

### Comment fonctionne le réglage fin ?

Le réglage fin consiste à exposer un modèle à un jeu de données d’exemples étiquetés. Le modèle améliore son entraînement initial, car il met à jour ses poids de modèle en fonction des nouvelles données. Le réglage fin est une méthode d’apprentissage supervisé, c’est-à-dire que les données utilisées pour l’entraînement sont organisées et étiquetées. En revanche, la plupart des modèles de base sont soumis à un apprentissage non supervisé pour lequel les données ne sont pas triées ; le modèle doit donc les classer tout seul.

Pour revenir à notre exemple de cuisinier amateur, le réglage fin d’un modèle d’IA générative est comme un cours de cuisine plus élaborée. Avant de suivre le cours, le cuisinier doit connaître les bases de la cuisine. Après avoir suivi une formation culinaire et acquis des connaissances spécifiques à un domaine, il sera bien plus compétents dans la préparation de plats plus sophistiqués.

### Réglage fin intégral et réglage fin efficace des paramètres

Les modèles peuvent être soit entièrement affinés, ce qui met à jour tous leurs paramètres, soit affinés de manière à ne mettre à jour que les paramètres les plus pertinents. Appelé [réglage fin efficace des paramètres](https://www.ibm.com/fr-fr/think/topics/parameter-efficient-fine-tuning) (PEFT, « parameter-efficient fine-tuning »), ce dernier processus est un moyen rentable de rendre les modèles plus efficaces dans un certain domaine.

Le réglage fin d’un modèle est gourmand en ressources informatiques et nécessite l’exécution en parallèle de plusieurs GPU puissants, sans parler de la mémoire pour stocker le LLM lui-même. Le PEFT permet aux utilisateurs de LLM de réentraîner leurs modèles sur des configurations matérielles plus simples tout en obtenant des améliorations de performances comparables dans le cas d’utilisation prévu du modèle, comme le support client ou l’analyse des sentiments. Le réglage fin est particulièrement efficace pour aider les modèles à surmonter les biais, qui sont un écart entre les prédictions du modèle et les résultats effectifs du monde réel. 

### Réglage fin et pré-entraînement continu

Le pré-entraînement intervient au tout début du processus d’entraînement. Les poids ou les paramètres du modèle sont initialisés de manière aléatoire et le modèle commence à s’entraîner sur son jeu de données initial. Le pré-entraînement continu introduit un modèle entraîné sur un nouvel ensemble de données non étiquetées selon une pratique dénommée apprentissage par transfert. Le modèle pré-entraîné « transfère » ce qu’il a appris jusqu’à présent vers de nouvelles informations externes.

En revanche, le réglage fin utilise des données étiquetées pour affiner les performances d’un modèle dans un cas d’utilisation donné. Le réglage fin permet d’affiner l’expertise d’un modèle sur des tâches spécifiques, tandis que le pré-entraînement continu permet d’approfondir l’expertise du modèle.
