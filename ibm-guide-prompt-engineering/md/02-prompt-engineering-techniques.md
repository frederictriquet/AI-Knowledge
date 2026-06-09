> Source : https://www.ibm.com/fr-fr/think/topics/prompt-engineering-techniques

# Techniques de prompt engineering

##

Les techniques de prompt engineering sont des stratégies utilisées pour concevoir et structurer les prompts, les requêtes d’entrée ou les instructions, fournies aux modèles IA, en particulier aux grands modèles de langage (LLM) tels que GPT-4 d’openAI, Google Gemini ou IBM® Granite  . Ces techniques visent à guider les systèmes [d’IA générative](https://www.ibm.com/fr-fr/think/topics/generative-ai) dans la production de réponses précises, pertinentes et contextuellement adaptées, permettant aux utilisateurs d’obtenir efficacement les sorties souhaitées.

Les grands modèles de langage, qui reposent sur des algorithmes de machine learning avancés, sont capables de comprendre et de générer des textes comparables à ceux des humains. Le prompt engineering utilise cette fonctionnalité pour créer des entrées qui aident le modèle à effectuer des tâches complexes, telles que la synthèse, la traduction, l’écriture créative ou la résolution de problèmes, avec une plus grande précision. En expérimentant différentes structures de prompt, les utilisateurs peuvent influencer le comportement des LLM pour optimiser leur performance dans diverses applications.

Alors que l’IA générative continue de jouer un rôle clé dans divers domaines, comprendre les techniques de prompt engineering est devenu essentiel pour libérer tout son potentiel et adapter les modèles IA afin de répondre efficacement à des besoins spécifiques.

## Comprendre les prompts

Un prompt est le texte d’entrée ou la requête qui est fourni à un modèle IA, par exemple un grand modèle de langage, en vue de générer une réponse. Il sert de mécanisme principal pour guider le comportement du modèle, définir la tâche et établir le contexte de l’interaction. La conception d’un prompt a un impact significatif sur la qualité et la pertinence du résultat. Aussi, pour des tâches spécifiques, il est essentiel de choisir le bon type de prompt.

Pour obtenir des résultats optimaux de vos modèles d’IA, il est essentiel de comprendre les différentes façons dont les prompts peuvent être structurés pour s’adapter à différents objectifs et tâches. Il existe trois grandes façons de structurer le prompt : instructions directes, instructions ouvertes et instructions spécifiques à une tâche.

**Les instructions directes** sont des commandes claires et spécifiques qui indiquent précisément à l’IA ce qu’elle doit faire. Ces prompts sont adaptés à des tâches simples pour lesquelles l’utilisateur a une attente très précise du résultat. **Les prompts directs** reposent sur la capacité du modèle à analyser des instructions explicites et à générer des réponses qui s’alignent étroitement sur la commande. Plus l’instruction est détaillée, plus le résultat est susceptible de répondre aux attentes.

Exemple :

```
Write a poem about nature.
```

Pour cet exemple, l’IA connaît le format exact *\[un poème\]* et le sujet *\[la nature\]* et génère le texte en conséquence.

**Les instructions ouvertes** sont moins restrictives et encouragent l’IA à explorer des idées plus larges ou à fournir des réponses créatives et interprétatives. Ces prompts sont utiles pour la réflexion, la narration ou les discussions exploratoires où l’utilisateur apprécie la variété et l’originalité du résultat. Les **prompts ouverts** exploitent les capacités génératives du modèle sans imposer de contraintes. Le modèle s’appuie sur ses données d’entraînement pour déduire la meilleure approche pour le prompt, qui peut produire des résultats divers ou inattendus.

Exemple :

```
Tell me about the universe.
```

Ici, l’IA a la liberté de décider des aspects de l’univers à évoquer, tels que son *origine, sa structure ou des théories scientifiques*.

**Les instructions spécifiques à une tâche** sont conçues pour des tâches précises et orientées vers un objectif, telles que la traduction, la synthèse ou les calculs. Ces prompts sont souvent rédigés avec clarté et peuvent inclure un contexte ou des exemples supplémentaires pour garantir la précision des réponses. Les **prompts spécifiques à une tâche** tirent parti de la compréhension des tâches spécialisées par le modèle. Elles peuvent intégrer des techniques de prompting avancées telles que l’apprentissage few-shot (fournissant des exemples) ou l’apprentissage zero-shot (qui ne fournit pas d’exemples, mais s’appuie sur des connaissances pré-entraînées du modèle).

Exemple : 

```
Translate this text into French: ‘Hello.’
```

Le modèle comprend à la fois la tâche de traduction linguistique et le texte d’entrée spécifique, ce qui lui permet de produire la sortie souhaitée : « Bonjour. »

En comprenant ces types de prompts et les nuances techniques sous-jacentes, les utilisateurs peuvent créer des prompts qui guident efficacement les modèles IA, en optimisant la qualité et la pertinence des réponses. 

## Techniques clés du prompt engineering

Pour optimiser l’efficacité des modèles IA, le prompt engineering utilise une variété de techniques adaptées à des tâches et des objectifs différents. Voici plusieurs techniques clés, chacune expliquée à l’aide d’exemples de prompts conçus pour obtenir des résultats spécifiques. 

Pour démontrer l’efficacité de différentes techniques de prompt engineering, appliquons une seule tâche en tant que cas d’utilisation principal : expliquer le changement climatique. La tâche est définie comme suit : 

```
Explain the concept of climate change, its causes, and its effects in a way that is accessible to a general audience.
```

Chaque technique aborde la tâche différemment, en proposant différents niveaux de conseils, de complexité et de méthodologie. Découvrions ci-dessous comment ces techniques peuvent être appliquées à ce cas d’utilisation, avec des prompts personnalisés pour mettre en valeur leurs capacités uniques.\

#### Apprentissage zero-shot

L’apprentissage zero-shot consiste à demander au modèle d’effectuer une tâche sans fournir d’exemples ou de conseils préalables. Il s’appuie entièrement sur les connaissances pré-entraînées de l’IA pour interpréter le prompt et y répondre\[1\].

Exemple de prompt :

```
Explain the concept of climate change, its causes, and its effects in simple terms.
```

Le modèle ne reçoit aucun exemple antérieur ni contexte supplémentaire et doit s’appuyer uniquement sur ses connaissances pré-entraînées pour générer la sortie.

#### Apprentissage few-shot

L’apprentissage few-shot prévoit d’intégrer un petit nombre d’exemples dans le prompt pour expliquer la tâche au modèle. Cette approche permet au modèle de mieux comprendre le contexte et la sortie attendue.[\[2\]](#f02)

Exemple de prompt :

```
Here are some examples of how to explain complex topics:

- Topic: Photosynthesis
- Explanation: Photosynthesis is the process by which plants convert sunlight, water, and carbon dioxide into energy and oxygen.
- Topic: Gravity
- Explanation: Gravity is the force that pulls objects toward each other, like how the Earth pulls us to its surface.

Now explain: Climate Change.
```

En fournissant quelques exemples sur la façon d’expliquer d’autres thèmes, le modèle reçoit des instructions à propos du ton et du niveau de simplicité attendus pour expliquer le changement climatique.

#### Prompting par chaîne de pensées (CoT)

Le prompting CoT encourage le modèle à raisonner étape par étape, en décomposant le problème en éléments plus petits afin d’aboutir à une conclusion logique.[\[3\]](#f03)

Exemple de prompt :

```
Step 1: Define what climate change is.
Step 2: Explain the causes of climate change.
Step 3: Describe its effects on the planet.

Now, follow these steps to explain climate change.
```

Le modèle est encouragé à penser par étapes, en décomposant l’explication en éléments plus petits et logiques pour gagner en clarté.

#### Meta-prompting

Le meta-prompting consiste à demander au modèle de générer ou d’affiner ses propres prompts pour mieux exécuter la tâche. Cette technique peut améliorer la qualité de la sortie en tirant parti de la capacité d’auto-gestion du modèle.[\[4\]](#f04)

Exemple de prompt :

```
Create a prompt that will help you explain climate change, its causes, and its effects in simple terms
```

Le modèle génère son propre prompt avant d’essayer d’expliquer le sujet, ce qui améliore potentiellement la pertinence et la qualité de la sortie.

#### Cohérence propre

Le principe de cohérence propre utilise le modèle pour générer plusieurs propositions indépendantes et identifier la réponse la plus cohérente et la plus précise. Ceci est particulièrement utile pour les tâches nécessitant un raisonnement ou une interprétation.[\[5\]](#f05)

Exemple de prompt :

```
Provide three different explanations of climate change, its causes, and its effects. Then identify the most coherent and clear explanation
```

Le modèle génère plusieurs réponses distinctes et sélectionne la plus cohérente ou la plus logique.

#### Générer des prompts de connaissances

Cette technique consiste à demander au modèle de générer des connaissances de base avant de traiter la tâche principale, améliorant ainsi sa capacité à produire des réponses éclairées et précises.[\[6\]](#f06)

Exemple de prompt :

```
Before explaining climate change, first list the key scientific principles related to it. Once done, use these principles to explain the concept, its causes, and its effects.
```

Le modèle génère d’abord les connaissances de base (par exemple, les gaz à effet de serre, le réchauffement climatique) avant de fournir une explication plus éclairée.

#### Prompt chaining

Le prompt chaining consiste à relier plusieurs prompts entre eux, la production d’un prompt servant d’entrée au suivant. Cette technique est idéale pour les processus à plusieurs étapes.

Exemple de prompt :

```
What is climate change? Provide a brief definition.
```

Prompt suivant basé sur la réponse précédente :

```
What are the primary causes of climate change?
```

Prompt suivant basé sur la réponse précédente : 

```
What are the effects of climate change on the environment and human life?
```

La tâche est divisée en une série de prompts plus petits, le résultat de chaque étape alimentant la suivante pour structurer l’explication.

#### Arbre des pensées

La méthode de prompting appelée arbre des pensées encourage le modèle à explorer plusieurs branches de raisonnement ou d’idées avant d’arriver à un résultat final.[\[7\]](#f07)[\[8\]](#f08)

Exemple de prompt :

```
List three possible ways to explain climate change to a general audience. For each method, describe its advantages and disadvantages. Then choose the best explanation and elaborate on it
```

Le modèle produit une explication en explorant plusieurs approches et sélectionne la plus efficace afin de générer un résultat complet.

#### La génération augmentée de récupération (RAG)

La génération augmentée de récupération (RAG) associe la récupération d’informations externes à l’IA générative pour produire des réponses basées sur des connaissances à jour ou spécifiques à un domaine.[\[9\]](#f09)

Exemple de prompt :

```
Using the global temperature datasets from NASA GISS (GISTEMP) dataset on climate science, explain climate change, its causes, and its effects in simple terms.
```

Le modèle combine ses capacités génératives avec des connaissances externes pour produire une explication éclairée.

#### Raisonnement et utilisation automatiques des outils

Cette technique intègre des capacités de raisonnement à des outils externes ou à des interfaces de programmation d’applications (API), ce qui permet au modèle d’utiliser des ressources telles que des calculateurs ou des moteurs de recherche.[\[10\]](#f10)

Exemple de prompt :

```
Use the provided climate data to calculate the global temperature rise over the last century, and then explain how this relates to climate change, its causes, and its effects.
```

Le modèle intègre le raisonnement à des outils externes (par exemple, des calculateurs ou des API) pour analyser les données et fournir une explication basée sur les données.

#### Prompt engineering automatique

Cette méthode consiste à utiliser l’IA elle-même pour générer et optimiser des prompts pour des tâches spécifiques, en automatisant ainsi le processus de création d’instructions efficaces.

Exemple de prompt :

```
Generate a prompt that will help explain climate change, its causes, and effects. Then use the generated prompt to provide the explanation.
```

Le modèle automatise la création d’un prompt optimisé pour améliorer la qualité de sa réponse.

#### Prompting actif

Le prompting actif ajuste dynamiquement le prompt en fonction des sorties intermédiaires du modèle, affinant l’entrée pour améliorer les résultats.[\[11\]](#f11)

Prompt initial

```
Explain climate change, its causes, and its effects in simple terms.
```

Prompt de suivi

```
Add more detail about the causes of climate change, focusing on human activities.
```

Le prompt évolue dynamiquement en fonction de la sortie intermédiaire, affinant la réponse au fil des itérations.

#### Prompt de stimulation directionnelle

Le prompt de stimulation directionnelle (DSP) utilise des indices directionnels pour orienter le modèle vers un type de sortie ou une perspective spécifique.[\[12\]](#f12)

Exemple de prompt :

```
Explain the concept of climate change from an environmentalist’s perspective, focusing on the need for immediate action.
```

Le modèle est orienté vers une perspective ou un ton spécifique, ce qui influence le contexte de l’explication.

#### Modèles de langage assistés par programmation (PALM)

Les PALM intègrent des capacités de programmation pour améliorer les compétences de raisonnement et de calcul du modèle.[\[13\]](#f13)

Exemple de prompt :

```
Write Python code to visualize the increase in global temperatures over time. Then explain how this data relates to climate change, its causes, and its effects.
```

Le modèle associe programmation et génération de langage pour fournir à la fois une visualisation et une explication.

#### ReAct

Re Act combine le raisonnement et les prompts d’action, encourageant le modèle à penser de manière critique et à agir en fonction de son raisonnement.[\[14\]](#f14)

Exemple de prompt :

```
Analyze the following climate data and identify key trends. Based on your analysis, explain the concept of climate change, its causes, and its effects.
```

Cet exemple illustre comment le modèle peut combiner le raisonnement analytique et les informations exploitables.

#### Reflexion

Reflexion permet au modèle d’évaluer ses sorties précédentes et de les affiner pour améliorer leur précision et leur cohérence.[\[15\]](#f15)

Exemple de prompt :

```
Here is my first attempt at explaining climate change: [Insert initial output]. Review this explanation and improve it for clarity and accuracy.
```

Le modèle réfléchit sur ses résultats précédents et les améliore de manière itérative.

#### Chaîne de pensée multimodale (CoT multimodale)

Cette technique intègre la chaîne de raisonnement de la pensée à plusieurs modalités, telles que le texte, les images ou l’audio.[\[16\]](#f16)

Exemple de prompt :

```
Analyze this infographic on global warming trends, then explain climate change, its causes, and its effects step by step
```

Le modèle intègre le raisonnement à travers plusieurs modalités (texte et images) afin de fournir une explication complète.

#### Graph prompting

Le graph prompting tire parti de structures basées sur des graphiques pour organiser et raisonner sur des relations complexes entre des concepts ou des points de données.

Exemple de prompt :

```
Using the provided graph of CO₂ emissions over time, explain how it relates to climate change, its causes, and its effects.
```

Le modèle utilise le raisonnement basé sur un graphique pour connecter les points de données et générer une explication éclairée.

Nous pouvons ainsi voir comment différentes techniques de prompt engineering peuvent être appliquées à une seule tâche. En utilisant la même tâche pour plusieurs méthodes telles que le zero-shot, le few-shot, la chaîne de pensées et l’arbre des pensées, nous pouvons voir comment chaque technique structure la tâche différemment et guide l’IA pour produire des réponses uniques. Ces exemples illustrent la flexibilité et la créativité du prompt engineering pour résoudre divers problèmes. Nous encourageons les lecteurs à tester ces exemples de prompts avec différents modèles d’IA ou applications, tels que les modèles IBM Granite, ChatGPT d’OpenAI, Bard de Google, Claude d’Anthropic, Cohere ou Jurassic d’AI21 Labs. Cela permet aux utilisateurs de voir comment les résultats varient et de trouver ce qui fonctionne le mieux en fonction de leurs besoins.

## Défis liés aux techniques de prompt engineering

Bien que les techniques de prompt engineering soient puissantes, elles s’accompagnent de plusieurs défis. Il peut être difficile de créer des prompts efficaces qui produisent systématiquement des productions précises, en particulier pour les tâches nécessitant un raisonnement complexe, une compréhension fondée sur le bon sens ou des réponses nuancées. L’hallucination est un autre problème courant, où les modèles IA génèrent des informations inexactes ou entièrement fabriquées. Le fait de s’appuyer sur des modèles structurés ou de régler le modèle peut contribuer à atténuer certains de ces problèmes, mais la conception de prompts qui fonctionnent dans divers scénarios reste un processus d’essai et d’erreur. En outre, il peut être délicat d’équilibrer les capacités générales de l’intelligence artificielle et les objectifs spécifiques à une tâche, en particulier pour les tâches spécialisées ou spécifiques à un domaine.

## Applications des techniques de prompt engineering

Les techniques de prompt engineering ont un large éventail d’applications dans divers domaines. Dans les chatbots, ils permettent d’affiner les réponses générées pour améliorer les interactions des utilisateurs en temps réel. Pour les développeurs, les prompts peuvent aider à générer des extraits de code ou à créer des tutoriels étape par étape pour les concepts de programmation. Dans le cadre de la formation, ils peuvent simplifier les explications ou résoudre un problème mathématique avec un raisonnement détaillé. Les entreprises utilisent le prompt engineering pour la prise de décision en générant des résultats d’IA perspicaces et adaptés à des scénarios spécifiques. À grande échelle, ces techniques sont utilisées dans la création de contenu, le support client et les workflows, rendant les systèmes d’IA plus efficaces et adaptables à diverses tâches.

## L’avenir des techniques de prompt engineering

L’avenir des techniques de prompt engineering réside dans les progrès du traitement automatique du langage naturel, qui permet de garantir des réponses plus précises et plus pertinentes dans diverses applications. Au fur et à mesure que les modèles IA évoluent, leur capacité de raisonnement s’améliorera, leur permettant de gérer des tâches plus complexes avec un minimum de prompting. On peut également s’attendre au développement d’outils et de cadres de frameworks plus intelligents pour automatiser et optimiser la création de prompts, afin de rendre les interactions avec l’IA plus intuitives, efficaces et personnalisées pour les utilisateurs dans divers domaines.

## Synthèse

Les techniques de prompt engineering sont essentielles pour optimiser les interactions de l’IA et déverrouiller tout le potentiel des grands modèles de langage. En utilisant des approches structurées telles que le zero-shot, le few-shot, la chaîne de pensées et l’arbre des pensées, ces techniques permettent à l’IA de s’attaquer à un large éventail de tâches, des chatbots à la prise de décision et à la formation. Malgré des défis tels que les hallucinations et la conception de prompts efficaces, les applications de prompt engineering continuent à se développer dans tous les domaines, et les résultats de l’IA n’en seront que plus intelligents et plus personnalisés. À mesure que les progrès dans le traitement automatique du langage naturel et les capacités de raisonnement progressent, l’avenir du prompt engineering est la promesse d’une efficacité et d’une adaptabilité accrues. Nous vous encourageons à expérimenter ces techniques sur différents modèles IA afin de découvrir leurs capacités et d’affiner vos résultats.
