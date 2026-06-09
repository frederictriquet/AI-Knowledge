> Source : https://www.ibm.com/fr-fr/think/topics/dspy

# Qu’est-ce que DSPy ?

Les [grands modèles de langage](https://www.ibm.com/fr-fr/think/topics/large-language-models) (LLM), les [workflows agentiques](https://www.ibm.com/fr-fr/think/topics/agentic-workflows) et les [bases de données vectorielles](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation) sont devenus de plus en plus puissants, tandis que les cadres permettant de rationaliser le développement d’applications d’IA ont gagné en popularité. DSPy est une boîte à outils qui fournit des modules polyvalents qui remplacent le [prompt engineering](https://www.ibm.com/fr-fr/think/topics/prompt-engineering) et la saisie directe de langage naturel par une configuration à l’aide de code Python. 

En général, l’utilisation de LLM ou de [modèles de fondation](https://www.ibm.com/fr-fr/think/topics/foundation-models) nécessite un [prompt engineering](https://www.ibm.com/fr-fr/think/topics/prompt-engineering) minutieux, où l’utilisateur modifie les prompts textuels pour obtenir le résultat souhaité. Bien que cette approche puisse être efficace, elle est chronophage et source d’erreurs, et crée des chaînes d’outils fragiles qui doivent être mises à jour lorsque de nouvelles versions d’un modèle sont publiées. Les cadres populaires tels que [LangChain](https://www.ibm.com/fr-fr/think/topics/langchain), qui enchaînent les modèles de langage pour la création d’applications, et [LlamaIndex](https://www.ibm.com/fr-fr/think/topics/llamaindex), qui se consacre à l’amélioration des capacités de recherche dans les textes, nécessitent toujours que les développeurs aient une expertise dans le [réglage fin](https://www.ibm.com/fr-fr/think/topics/fine-tuning) et du temps pour tester chaque prompt afin d’obtenir le résultat souhaité. DSPy simplifie ce processus d’affinement grâce à une approche programmatique qui guide et limite le comportement du modèle de langage.

DSPy se dédie à l’automatisation de l’optimisation de la conception des prompts. Pour remplacer le piratage des prompts et les générateurs de données synthétiques ponctuels, DSPy fournit des **optimiseurs** généraux, des algorithmes qui mettent à jour les paramètres de votre programme. Chaque fois que vous modifiez votre code, vos données, vos assertions ou vos indicateurs, vous pouvez recompiler votre programme et DSPy effectuera une optimisation afin de créer de nouveaux prompts efficaces qui correspondent à vos modifications.

On imagine parfois que l’optimisation automatique des prompts consiste à créer un système dans lequel les LLM analysent et améliorent les prompts générées par les utilisateurs. Ce n’est pas la manière la plus efficace d’exploiter les LLM. DSPy exploite la puissance de génération d’idées des LLM pour générer ses propres prompts. Il teste ensuite ces variations à l’aide d’un ensemble d’indicateurs d’évaluation afin de déterminer si elles permettent de mieux résoudre le problème. S’ils n’obtiennent pas de meilleurs résultats sur un indicateur attribué par l’utilisateur, les nouveaux prompts sont rejetés. Ce processus s’apparente à un algorithme évolutif dans lequel les prompts sont évalués en fonction de leur adéquation et améliorés de manière itérative.

### Cas d’utilisation de DSPy

DSPy peut être utile dans plusieurs types de workflows et de scénarios différents. Les plus couramment utilisés incluent la génération augmentée de récupération, la réponse aux questions à sauts multiples et la [synthèse de documents](https://www.ibm.com/fr-fr/think/topics/text-summarization).

- [Chaîne de pensée](#cot1)
- [Génération augmentée par la récupération](#rag1)
- [Réponse aux questions à sauts multiples](#mqa1)
- [Synthèse](#sum1)

**Chaîne de pensée**

Le prompting par [chaîne de pensée](https://www.ibm.com/fr-fr/think/topics/chain-of-thoughts) (CoT) simule des processus de raisonnement humains en demandant au modèle de décomposer des tâches complexes en une séquence d’étapes logiques menant à une résolution finale. Ces étapes de raisonnement sont intégrées dans la fenêtre contextuelle du modèle, ce qui lui permet de mieux s’ancrer dans la tâche à accomplir et conduit souvent à de meilleures réponses, même dans des scénarios complexes. DSPy aide en demandant au modèle de langage de générer des prompts et des stratégies de chaîne de pensée et en les testant avec le modèle de langage afin de générer les prompts CoT les plus efficaces pour le modèle donné.

**Génération augmentée de récupération**

La [génération augmentée de récupération](https://www.ibm.com/fr-fr/architectures/hybrid/genai-rag) (RAG) est une approche qui permet aux LLM d’exploiter un vaste corpus de connaissances provenant de différentes sources et d’interroger leur base de connaissances afin de trouver des passages ou des contenus pertinents et de produire une réponse bien affinée. Le RAG garantit que les LLM peuvent exploiter de manière dynamique des connaissances en temps réel, même s’ils n’ont pas été initialement entraînés sur le sujet, et donner des réponses correctes. Cette puissance supplémentaire entraîne une plus grande complexité lors de la mise en place des pipelines RAG. DSPy offre une approche transparente pour mettre en place des pipelines de prompting et soit générer des prompts efficaces (via l’optimisation), soit, dans le cas de modèles plus petits, affiner les pondérations du modèle lui-même.

Les pipelines RAG peuvent être optimisés avec DSPy de deux manières : à l’aide d’exemples étiquetés ou d’exemples d’amorçage. Les exemples étiquetés sont simplement des exemples préexistants, étiquetés manuellement et employés pour entraîner directement le modèle élève. Dans le contexte de DSPy, les amorçages consistent à utiliser un mode de langage dans un paradigme enseignant-élève. L’enseignant génère de nouveaux exemples d’entraînement à partir de quelques prompts fournies par l’utilisateur. Ces exemples amorcés sont ensuite employés en complément ou à la place des exemples étiquetés manuellement pour entraîner le module élève jusqu’à ce qu’il fournisse les bonnes réponses. Les prompts qui génèrent les bonnes réponses sont ensuite mis à jour de manière itérative tout au long du pipeline DSPy.

**Réponse aux questions à sauts multiples**

Une seule requête de recherche ne suffit souvent pas pour une tâche complexe de [réponse aux questions](https://www.ibm.com/fr-fr/think/topics/question-answering). Le célèbre jeu de données [HotPot Question Answering](https://hotpotqa.github.io/) comprend des questions qui nécessitent plusieurs analyses et récupérations avant de pouvoir y répondre. Par exemple : « En quelle année Bill Nelson a-t-il volé pour la première fois en tant que spécialiste de charge utile à bord d’une navette spatiale ? » Pour répondre à cette question, il faut savoir que Bill Nelson a volé à bord de la navette spatiale Columbia, puis déterminer que celle-ci a volé pour la première fois en 1981.

L’approche standard pour relever ce défi dans la littérature augmentée par récupération consiste à créer un système de recherche à sauts multiples. Ces systèmes lisent les résultats récupérés, puis génèrent des requêtes supplémentaires pour recueillir des informations complémentaires si nécessaire avant de parvenir à une réponse finale. Grâce à DSPy, vous pouvez créer le même système en quelques lignes de code de manière robuste, ce qui vous permet de mettre à jour les modèles et d’exécuter à nouveau votre pipeline.

**Synthèse**

La synthèse condense un texte long en une version plus courte tout en conservant les informations clés et les idées principales. C’est une compétence puissante pour un LLM, avec des applications allant de la création de résumés d’articles à la génération de rapports concis à partir de documents longs.

L’évaluation de la qualité des résumés produits par les modèles de langage présente des défis importants. Contrairement aux tâches pour lesquelles les réponses sont clairement bonnes ou mauvaises, la qualité de la synthèse est souvent subjective et dépend du contexte. Le modèle doit trouver un équilibre entre la conservation des informations et la concision, tout en préservant le ton et l’intention du texte original et en garantissant l’exactitude des faits sans introduire d’erreurs. L’adaptation à différents types de sources et à différents objectifs de résumé représente un défi supplémentaire. DSPy vous permet d’exploiter des données étiquetées pour affiner vos prompts de résumé afin d’obtenir les meilleures réponses possibles.

### Les concepts de DSPy

DSPy possède son propre vocabulaire et sa propre terminologie. L’apprentissage de certains de ces termes clés vous aidera à mieux comprendre son architecture générale.

- [Compilation](#comp1)
- [Signature](#sign1)
- [Optimiseur](#opt1)
- [Pipeline](#pipe1)
- [Indicateurs](#metr1)

**Compilation** : ce processus correspond à la manière dont DSPy traduit un programme basé sur Python en instructions qu’un modèle de langage peut comprendre et exécuter efficacement. 

**Signature** : il s’agit d’une classe qui définit les types d’entrée et de sortie d’un module, garantissant la compatibilité entre les différents modules d’un programme DSPy. Parmi les exemples de signatures, citons des tâches telles que la saisie d’une question et la production du raisonnement et de la réponse, ou la saisie d’un document et la production d’un résumé.

**Optimiseur** : ce composant de DSPy affine le programme compilé en fonction du modèle de langage spécifique que vous employez (par exemple : GPT3.5-Turbo, GPT-4.0 ou Llama 3.1). Les optimiseurs vous permettent de maximiser les performances et la précision de votre programme. Dans les anciennes versions de DSPy, ils étaient appelés « téléprompteurs ». Les programmes DSPy consistent en plusieurs appels à des modèles de langage qui sont empilés ensemble sous forme de modules DSPy. Chaque module DSPy possède trois types de paramètres internes : les pondérations LM, les instructions qu’il est censé suivre et les démonstrations stockées du comportement d’entrée/sortie.

Lorsqu’on lui fournit un indicateur, DSPy crée des prompts optimisés en utilisant toutes les pondérations, les instructions et le comportement du modèle avec des algorithmes d’optimisation à plusieurs étapes. Ceux-ci peuvent allier la descente de gradient (pour les pondérations du modèle de langage) et l’optimisation discrète basée sur le modèle langage, c’est-à-dire pour élaborer ou mettre à jour des instructions et pour créer ou valider des démonstrations. Les démonstrations DSPy sont similaires aux exemples few-shot, mais elles sont beaucoup plus puissantes. Ils peuvent être conçus de toutes pièces à partir de votre programme, et leur élaboration comme leur sélection peuvent être optimisées de nombreuses manières efficaces.

Dans de nombreux cas, la compilation conduit à de meilleurs prompts que l’écriture humaine, car les optimiseurs peuvent essayer plus de choses, de manière beaucoup plus systématique, et ajuster les indicateurs directement, ce que l’humain ne peut pas faire.

**Pipeline** : un « pipeline » est le terme employé par DSPy pour désigner une séquence de modules connectés qui opèrent ensemble pour accomplir une tâche complexe. Ainsi, un pipeline peut résumer un article, le traduire d’une langue source vers une langue cible, puis générer des questions à son sujet dans la langue cible.

**Indicateurs** : DSPy définit plusieurs indicateurs différents pour évaluer les performances de la sortie. Vous pouvez par exemple exiger que la sortie corresponde exactement à votre étiquette. Dans d’autres cas, une correspondance partielle peut vous convenir. Le F1 sémantique est un indicateur couramment utilisé fourni par DSPy. Il mesure la quantité d’informations contenues dans l’étiquette qui se trouve dans la réponse et la quantité de données superflues qui ne se trouvent pas dans la réponse cible étiquetée et qui sont présentes dans la réponse. Vous pouvez également fournir vos propres indicateurs personnalisés si vous souhaitez mesures les performances d’un autre façon.

### Utilisation de DSPy

Pour commencer à utiliser DSPy, il suffit d’appeler pip install dspy-ai. Aucun matériel particulier n’est nécessaire, car la plupart des modèles peuvent être utilisés dans le cloud via une API ou localement. DSPy peut être exécuté localement ou sur des environnements de notebook hébergés tels que Google Colab ou Watson Studio.

- [Création de signatures](#buil1)
- [Compilation](#comp2)
- [Évaluation et itération](#eval1)

Un pipeline DSPy typique pour la génération augmentée de récupération se compose d’un modèle de langage et d’un modèle de récupération. Par exemple, pour travailler avec GPT-3.5 Turbo d’OpenAI comme modèle de langage et ColBERTV2 comme modèle de récupération, DSPy serait configuré comme suit :

```python
import dspy
turbo = dspy.OpenAI(model=’gpt-3.5-turbo’)
colbertv2_wiki17_abstracts = dspy.ColBERTv2(url=’http://20.102.90.50:2017/wiki17_abstracts’)
# set the language model and the retrieval model
dspy.settings.configure(lm=turbo, rm=colbertv2_wiki17_abstracts)
```

 

**Création de signatures**

Les signatures sont des modèles qui vous permettent de configurer la manière dont les champs d’entrée et de sortie du modèle de langage et du modèle de recherche peuvent être structurés. Par exemple, cet extrait de code montre la syntaxe permettant de fournir au modèle de langage un contexte et au modèle de recherche une structure :

```python
class GenerateAnswer(dspy.Signature):
“””Answer questions with short factoid answers.”””
context = dspy.InputField(desc=”may contain relevant facts”)
question = dspy.InputField()
answer = dspy.OutputField(desc=”often between 1 and 5 words”)
```

Nous incluons de brèves descriptions pour les champs de contexte et de réponse afin de définir des directives plus précises sur ce que le modèle recevra et devra générer.

**Compilation**

Une fois vos signatures définies, vous pouvez exécuter votre programme et créer des prompts optimaux pour votre tâche en utilisant un optimiseur adapté à celle-ci. Dans DSPy, ce processus est appelé compilation. La compilation d’un programme met à jour les paramètres stockés dans chaque module. Dans la plupart des scénarios, cela consiste principalement à collecter et à sélectionner de bonnes démonstrations à inclure dans le prompt.

La compilation nécessite :

• un jeu d’entraînement ou des exemples amorcés ;

• Un indicateur pour la validation. Dans un scénario RAG, il s’agirait d’un moyen de mesurer la précision de la réponse prédite et de vérifier que le contexte récupéré contient la réponse ;

• Un optimiseur spécifique pour générer des prompts à tester. Par exemple, l’optimiseur BootstrapFewShot peut être employé pour générer des prompts, puis les tester.

Pour compiler un programme DSPy, vous configurez les modèles que vous souhaitez utiliser et les transmettez à la méthode de compilation de l’optimiseur de votre choix. Par exemple, un programme pour une application RAG contiendrait un modèle de langage et un modèle de récupération. Ceux-ci seraient ensuite transmis à la méthode de compilation et l’optimiseur s’appuierait sur les données récupérées pour définir le contexte de la génération du langage.

Vous définissez ensuite un indicateurs pour évaluer à la fois le modèle de récupération et le modèle de langage. Cette définition des indicateurs serait ensuite transmise à un optimiseur tel que BootstrapFewShot ou LabeledFewShot afin qu’il s’en serve pour évaluer les prompts générés par le modèle de langage. Enfin, l’optimiseur compile un module personnalisé contenant la méthode forward que vous avez définie ainsi qu’un [jeu de données](https://www.ibm.com/fr-fr/think/topics/dataset) d’entraînement.

Le choix de l’optimiseur à utiliser nécessite généralement des essais, mais voici quelques lignes directrices :

• Si vous disposez de très peu d’exemples (environ 10), vous pouvez commencer par BootstrapFewShot pour générer de nouvelles données d’entraînement.

• Si vous disposez de plus de données (50 exemples ou plus), essayez BootstrapFewShotWithRandomSearch pour générer de nouvelles données d’entraînement sur des parties aléatoires de vos données d’entraînement.

• Si vous avez besoin d’un programme très efficace, vous pouvez affiner un petit LLM pour votre tâche avec BootstrapFinetune.

**Évaluation et itération**

Après avoir compilé votre programme et comparé vos indicateurs, vous serez peut-être satisfait des résultats. Vous pouvez également trouver que vous n’aimez pas certains aspects du programme final ou des résultats selon le(s) indicateur(s) choisi(s). Le développement itératif est essentiel. DSPy fournit des outils pour le faire de manière incrémentielle en itérant sur vos données, en mettant à jour la structure de votre programme, le(s) indicateur(s) sélectionné(s) et l’optimiseur choisi.

### En savoir plus

DSPy est open source ; vous pouvez donc inspecter le code et voir l’avancement du développement. La documentation disponible sur le site StanfordNLP de [Github](https://github.com/stanfordnlp/dspy) contient des documents et de nombreux tutoriels et démonstrations par étapes pour vous aider à vous lancer avec DSPy.
