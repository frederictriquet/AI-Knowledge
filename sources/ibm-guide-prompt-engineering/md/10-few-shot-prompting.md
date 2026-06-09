> Source : https://www.ibm.com/fr-fr/think/topics/few-shot-prompting

# Qu’est-ce que l’apprentissage few-shot ?

L’apprentissage few-shot désigne le processus qui consiste à fournir à un modèle d’IA quelques exemples d’une tâche afin de guider ses performances. Cette méthode est particulièrement utile dans les scénarios où des données d’entraînement exhaustives ne sont pas disponibles.

Contrairement à d’autres techniques telles que l’apprentissage zero-shot, qui ne nécessite aucun exemple, ou l’apprentissage one-shot, qui repose sur un seul exemple, l’apprentissage few-shot utilise plusieurs exemples pour améliorer la précision et l’adaptabilité. En outre, d’autres cadres avancés de prompt engineering, tels que le prompting par [chaîne de pensée](https://www.ibm.com/fr-fr/think/topics/chain-of-thoughts) et le prompting par [arbre de pensée](https://www.ibm.com/fr-fr/think/topics/tree-of-thoughts), utilisent également des exemples pour obtenir le résultat souhaité et optimiser la sortie du modèle.

L’apprentissage few-shot est essentiel dans les situations où l’IA générative doit relever le défi de collecter de vaste volume de données étiquetées. Les méthodes de prompting convertissent les entrées de texte en un format structuré, permettant à des modèles tels que la série IBM Granite, les modèles Llama de Meta et les modèles GPT-3 et GPT-4 d’OpenAI de remplir les blancs avec des réponses appropriées, effectuant ainsi efficacement des tâches sans disposer de vastes jeux de données étiquetées.\[1\] Cette technique permet également d’obtenir le format de sortie prédéfini en guidant le modèle à travers des exemples spécifiques, garantissant ainsi la cohérence et la précision de la structure souhaitée.

Dans le domaine en rapide évolution de l’intelligence artificielle (IA), du machine learning (ML) et du traitement automatique du langage naturel (NLP), l’apprentissage few-shot s’est imposé comme une technique puissante. Cette méthode permet aux modèles d’effectuer des tâches avec un nombre limité d’exemples, ce qui la distingue d’autres méthodes de prompting telles que l’apprentissage zero-shot et one-shot. Il est essentiel de comprendre l’apprentissage few-shot pour exploiter pleinement le potentiel des systèmes d’IA avancés tels que GPT-3/GPT-4 d’OpenAI et d’autres grands modèles de langage (LLM) tels que les modèles Granite d’IBM ou les modèles Llama de Meta.

  Figure 1 – Illustration de l’apprentissage few-shot pour la classification des sentiments à l’aide de méthodes basées sur les prompts

La figure 1 illustre un processus d’apprentissage few-shot pour la classification des sentiments à l’aide d’un grand modèle de langage. Le prompt fournit des exemples de texte étiquetés comme « positifs » ou « négatifs ». Après avoir vu ces exemples étiquetés, le modèle est chargé de classer un nouveau texte (« Ce produit est très rentable ») comme « positif ». Cela démontre comment l’apprentissage few-shot permet au modèle de généraliser à partir d’un petit nombre d’exemples pour effectuer une tâche spécifique.

## Comment fonctionne l’apprentissage few-shot ?

L’apprentissage few-shot présente au modèle plusieurs exemples de la tâche souhaitée dans le prompt. Cette technique exploite les connaissances pré-entraînées des grands modèles de langage (LLM) pour effectuer des tâches spécifiques de manière efficace, même avec des données limitées.

  Figure 2 – Fonctionnement de l’apprentissage few-shot

**Requête utilisateur :** le processus commence par une requête de l’utilisateur, telle que « Ce produit est très rentable ».

**Base de données vectorielle :** tous les exemples sont stockés dans une base de données vectorielle, optimisée pour la recherche sémantique. Lorsqu’une requête utilisateur est reçue, le système effectue une correspondance sémantique pour trouver les exemples les plus pertinents dans la base de données vectorielle.

**Récupération d’exemples pertinents :** seuls les exemples les plus pertinents sont récupérés et utilisés pour créer le prompt. Dans cet exemple, la génération augmentée de récupération (RAG) est employée pour récupérer les exemples d’une base de données vectorielle, ce qui permet d’adapter le prompt à la requête spécifique. Bien que la RAG ne soit pas systématiquement requise pour l’apprentissage few-shot, elle peut considérablement renforcer le processus en garantissant que les exemples les plus pertinents dans le contexte sont utilisés, améliorant ainsi les performances du modèle dans certains scénarios.

**Création du prompt :** le prompt est conçu à partir des exemples récupérés et de la requête de l’utilisateur. Il peut ainsi ressembler à ceci :

  Figure 3 – Création de prompts

**Traitement LLM :** le prompt créé est ensuite intégré au LLM. Le modèle traite le prompt et génère une sortie, dans ce cas, en classant le sentiment de la requête de l’utilisateur.

**Sortie :** Le LLM produit la classification, par exemple « négatif » pour l’exemple donné.

Des études ont mis en évidence l’efficacité d’une approche d’apprentissage few-shot qui réduit la dépendance au prompt engineering intensif. Contrairement au réglage fin traditionnel, qui consiste à affiner les paramètres du modèle à l’aide d’un grand jeu de données avant le prompting, le réglage fin dans le cadre du few-shot fait référence au processus d’adaptation des modèles pré-entraînés à l’aide de quelques exemples fournis directement dans le prompt. Cette approche permet au modèle d’exploiter plus efficacement ses connaissances préexistantes sans avoir besoin d’un entraînement supplémentaire sur de grands jeux de données.\[2\] Cette étude a démontré que même en utilisant des « prompts vides » (qui ne contiennent aucun modèle spécifique à une tâche ni aucun exemple étiqueté), le modèle pouvait toujours atteindre une précision compétitive dans diverses tâches. Ainsi, un prompt vide peut simplement poser une question telle que « Quel est le sentiment du texte suivant ? » sans donner d’exemples spécifiques ni d’instructions sur la manière de classer le sentiment. Malgré ce manque de structure, le modèle peut donner de bons résultats, ce qui démontre la robustesse de l’apprentissage few-shot.

Dans l’ensemble, l’étude suggère que l’apprentissage few-shot est une stratégie très efficace, en particulier lorsque des prompts structurés sont employés. Si les prompts vides peuvent donner de bons résultats, l’ajout de quelques exemples bien choisis peut encore renforcer les performances du modèle, ce qui en fait une approche polyvalente et efficace, en particulier dans les scénarios où les données étiquetées sont limitées. \[1\]

## Avantages et limites de l’apprentissage few-shot

L’apprentissage few-shot est une technique puissante dans le domaine du traitement automatique du langage naturel (NLP) qui permet aux modèles d’effectuer des tâches à partir d’un nombre minimal d’exemples. Cette approche présente plusieurs avantages et limites qui influent sur son efficacité et son applicabilité.

**Avantages**

1.  **Efficacité et flexibilité** : l’apprentissage few-shot réduit considérablement le volume de données étiquetées nécessaires à l’entraînement, ce qui le rend très efficace et adaptable aux nouvelles tâches. En tirant parti de grands modèles de langage pré-entraînés, l’apprentissage few-shot peut atteindre des performances compétitives même avec des données limitées. Par exemple, dans l’étude citée ci-dessous, les auteurs ont montré que le réglage fin des modèles de langage dans un contexte few-shot réduit le besoin d’un prompt engineering approfondi et permet d’atteindre une grande précision dans un large éventail de tâches.\[2\]
2.  **Amélioration des performances dans diverses applications** : l’apprentissage few-shot a démontré des améliorations significatives dans diverses applications, de la classification de texte à la traduction automatique et au-delà. Par exemple, les auteurs de l’étude citée ci-dessous ont proposé TransPrompt, un cadre de prompting transférable qui capture les connaissances inter-tâches, améliorant considérablement les performances sur les tâches de classification de texte en few-shot.\[3\]
3.  **Robustesse face à différents prompts** : la robustesse de l’apprentissage few-shot face à différentes formulations de prompt est un autre avantage clé. L’Unified Prompt Tuning (UPT), tel que décrit par Feihu Jin et al., enrichit les prompts avec des informations spécifiques à la tâche et dépendantes de l’instance, ce qui permet d’obtenir des améliorations significatives des performances dans diverses tâches de NLP.\[4\]
4.  **Réduction de la charge de calcul** : les progrès récents ont rendu l’apprentissage few-shot plus efficace. Ainsi, Lewis Tunstall et al. ont introduit SetFit, un cadre efficace pour le réglage fin few-shot des transformateurs de phrases, qui permet d’obtenir une grande précision avec beaucoup moins de paramètres et un temps d’entraînement réduit par rapport aux méthodes existantes.\[5\]

**Limites**

1.  **Dépendance à l’égard de la qualité des prompts** : la qualité et la conception des prompts ont un impact significatif sur les performances de l’apprentissage few-shot. La création de prompts efficaces nécessite souvent une ingénierie minutieuse et une expertise dans le domaine. Les auteurs Timo Schick et ses collègues chercheurs ont souligné la variabilité des performances due à la qualité des prompts, insistant sur la nécessité d’une gestion intelligente de multiples prompts pour obtenir des résultats fiables.\[6\]
2.  **Complexité de calcul** : les grands modèles de langage employés dans l’apprentissage few-shot nécessitent des ressources de calcul importantes. Cela peut constituer un obstacle pour de nombreuses entreprises et limiter l’accessibilité de ces modèles. Morteza Bahrami et al. ont noté que les modèles comportant un nombre considérable de paramètres nécessitent un matériel puissant, ce qui peut constituer une contrainte pour leur adoption à grande échelle.\[1\]
3.  **Le défi de la généralisation** : la généralisation des prompts à travers diverses tâches et divers jeux de données reste un défi important. Si l’apprentissage few-shot peut donner de bons résultats pour des tâches spécifiques, garantir des performances cohérentes dans diverses applications nécessite des techniques avancées. Par exemple, l’étude menée par Feihu Jin et ses coauteurs a abordé cette question dans le domaine du raisonnement numérique en exploitant de grandes quantités de données d’entraînement afin d’améliorer la généralisation dans l’apprentissage basé sur les prompts.\[4\]
4.  **Capacités zero-shot limitées** : si l’apprentissage few-shot excelle avec un minimum d’exemples, ses performances dans les configurations zero-shot peuvent être moins fiables. L’étude sur les progrès en matière de NER a présenté QaNER, une méthode basée sur les prompts pour la reconnaissance d’entités nommées (NER) qui remédie aux limites des capacités zero-shot en améliorant la robustesse des prompts.\[7\]

Ainsi, l’apprentissage few-shot offre des avantages substantiels en termes d’efficacité, de flexibilité et de performances dans diverses applications. Cependant, sa dépendance à l’égard de la qualité des prompts, sa complexité de calcul, ses défis en matière de généralisation et ses capacités zero-shot limitées mettent en évidence les domaines dans lesquels des progrès supplémentaires sont nécessaires pour maximiser son potentiel.

## Cas d’utilisation

L’apprentissage few-shot s’est révélé être un outil polyvalent et puissant, avec de nombreux exemples dans diverses applications, tirant parti des atouts des grands modèles de langage pour effectuer des tâches complexes avec un nombre limité d’exemples. Il est très apprécié dans les cas d’utilisation créatifs de l’IA générative, tels que la création de contenu ou l’apprentissage contextuel. Voici quelques cas d’utilisation détaillés :

**Analyse des sentiments**\
L’apprentissage few-shot est particulièrement utile dans l’analyse des sentiments, où les modèles classifient le sentiment d’un texte avec des données étiquetées limitées. L’intégration de l’apprentissage few-shot avec la correspondance sémantique, comme le montre la figure 2, en est un exemple. Il permet aux modèles de classer avec précision les sentiments sur la base d’exemples pertinents provenant d’une base de données vectorielle.\[1\]\

**Reconnaissance d’actions dans les vidéos**\
L’apprentissage few-shot a également été appliqué à la reconnaissance d’actions dans les vidéos. Yuheng Shi et al. ont introduit le prompting par connaissances, qui exploite les connaissances de bon sens provenant de ressources externes pour alimenter les modèles de vision-langage. Cette méthode classe efficacement les actions dans les vidéos avec un minimum de supervision, atteignant des performances de pointe tout en réduisant considérablement les coûts d’entraînement.\[8\]

**Génération de dialogues fondés**\
Dans la génération de dialogues fondés ou les chatbots, l’apprentissage few-shot renforce les modèles de dialogue en intégrant des sources d’informations externes. Cette étude a démontré que les méthodes d’apprentissage few-shot pouvaient améliorer considérablement les performances des modèles de dialogue, les rendant plus cohérents et plus pertinents sur le plan contextuel.\[9\]

**Reconnaissance d’entités nommées (NER)**\
L’apprentissage few-shot peut améliorer les tâches de reconnaissance d’entités nommées en fournissant des exemples qui aident le modèle à reconnaître et à classer les entités dans le texte. L’auteur de l’étude citée ci-dessous a développé une méthode d’apprentissage few-shot basée sur des prompts et tenant compte des entités pour les tâches de questions-réponses. Adaptée aux tâches de NER, elle améliore ainsi considérablement les performances du modèle.\[10\]

**Tâches de génération de code**\
L’apprentissage few-shot est également applicable à des tâches liées au code, telles que la génération d’assertions de test et la réparation de programmes. Dans leur étude, Noor Nashid et al. ont développé une technique qui récupère automatiquement des démonstrations de code pour créer des prompts efficaces, montrant des améliorations substantielles dans la précision des tâches.\[11\]

Ces cas d’utilisation démontrent la grande applicabilité et l’efficacité de l’apprentissage few-shot dans différents domaines et tâches, mettant en évidence son potentiel pour stimuler l’innovation et l’efficacité dans les applications d’IA et de NLP.

L’apprentissage few-shot représente une avancée significative dans le domaine de l’IA et du NLP, offrant efficacité, flexibilité et performances améliorées avec un nombre limité d’exemples. À mesure que la technologie évolue, elle jouera un rôle crucial dans diverses applications, stimulant l’innovation et l’efficacité dans de nombreux domaines.
