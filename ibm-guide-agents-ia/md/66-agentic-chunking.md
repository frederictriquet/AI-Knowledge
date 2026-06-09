> Source : https://www.ibm.com/fr-fr/think/topics/agentic-chunking

# Qu’est-ce que le découpage agentique ?

Le chunking agentique consiste à utiliser l’[intelligence artificielle](https://www.ibm.com/fr-fr/think/topics/artificial-intelligence) (IA) pour segmenter de longues entrées de texte en blocs plus petits et sémantiquement cohérents, appelés « chunks » (morceaux). Alors que de nombreuses stratégies de [segmentation](https://www.ibm.com/fr-fr/architectures/papers/rag-cookbook/chunking) traditionnelles utilisent des morceaux de taille fixe pour fractionner le texte, le chunking agentique segmente dynamiquement le texte en fonction du contexte.

[Les grands modèles de langage (LLM)](https://www.ibm.com/fr-fr/think/topics/large-language-models) ne peuvent pas traiter les grandes séquences d’entrées textuelles dans leur intégralité. La [fenêtre contextuelle](https://www.ibm.com/fr-fr/think/topics/natural-language-processing) du modèle de [traitement automatique du langage naturel (TAL)](https://www.ibm.com/fr-fr/think/topics/context-window) détermine la quantité maximale de contenu que le modèle peut ingérer tout en assurant la compréhension du contexte. Les systèmes de [machine learning](https://www.ibm.com/fr-fr/think/topics/machine-learning) (ML) utilisent des techniques de chunking pour diviser les documents en plusieurs parties qui correspondent à la fenêtre contextuelle du LLM.

## Découpage et RAG

Face au développement de la [génération augmentée par récupération (RAG)](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation), c’est-à-dire la connexion des LLM aux sources de données externes, la création de systèmes de chunking est devenue une nécessité. Les systèmes RAG ont été créés pour lutter contre le problème des [hallucinations](https://www.ibm.com/fr-fr/think/topics/ai-hallucinations), lorsque les LLM fournissent des réponses qui ne reflètent pas les résultats ou informations du monde réel.

Les systèmes RAG aident les LLM à générer des réponses plus précises et plus utiles, en les reliant à des bases de connaissances supplémentaires. Dans de nombreux cas, les bases de connaissances RAG sont des [bases de données vectorielles](https://www.ibm.com/fr-fr/think/topics/vector-database) contenant des documents qui permettent aux LLM reliés d’accéder à des connaissances spécialisées. Les modèles d’[embedding](https://www.ibm.com/fr-fr/think/topics/embedding) convertissent les documents en vecteurs mathématiques, puis font de même pour les requêtes des utilisateurs.

Le système RAG trouve dans sa [base de données vectorielle](https://www.ibm.com/fr-fr/think/topics/vector-database) les embeddings qui représentent des informations pertinentes et qui correspondent à la requête de l’utilisateur. Ensuite, le LLM utilise les données récupérées pour fournir aux utilisateurs des réponses plus pertinentes et plus précises.

Mais en raison des limites de la fenêtre contextuelle, le LLM n’est pas en mesure de traiter un document tout entier à la fois. Le chunking s’est imposé comme solution. En décomposant un document en plusieurs parties, le LLM peut trouver efficacement les morceaux pertinents en temps réel, tout en assurant la compréhension du contexte.

## Autres méthodes de découpage

Le chunking agentique permet aux LLM de créer des morceaux significatifs qui les aident à fournir de meilleures réponses, comme dans le cas d’utilisation de la RAG. Certaines méthodes de chunking prennent également en compte la sémantique, tandis que d’autres divisent les documents en petits morceaux de longueur fixe.

Les autres méthodes de chunking sont les suivantes :

### Découpage à taille fixe

La stratégie de segmentation la plus simple, le chunking à taille fixe, consiste à diviser le texte en morceaux de taille égale, selon un nombre prédéfini de caractères ou de tokens. Un token est la quantité minimale de texte que le LLM peut traiter, souvent un mot ou une partie de mot.

Pour éviter de fragmenter les phrases, de nombreuses implémentations de chunking à taille fixe incluent une fonctionnalité de chevauchement qui répète la fin d’un chunk au début du suivant. Le chunking à taille fixe est simple et léger en termes de calcul, mais il est rigide. Il ne tient compte ni de la densité du contenu, ni de la structure du document, pouvant créer des segments sémantiquement incohérents.

### Découpage récursif

Le chunking récursif utilise une liste hiérarchique de séparateurs de texte prédéfinis pour décomposer le texte de manière plus cohérente. Les séparateurs incluent des structures naturelles telles que les paragraphes, les phrases ou les mots. Dans un document de codage Python, les séparateurs peuvent inclure des définitions de classes et de fonctions.

Comparé au chunking en taille fixe, le chunking récursif crée des morceaux plus cohérents en suivant les séparations naturelles dans le texte. L’utilisation de Markdown aide également l’algorithme de chunking, ou « chunker », à déterminer où faire les divisions. *RecursiveCharacterTextSplitter* est un outil de chunking très utilisé, disponible dans [LangChain.](https://www.ibm.com/fr-fr/think/topics/langchain)

Mais si le texte ne comporte pas de séparateurs clairs, les algorithmes de chunking récursif ne sauront pas où créer de nouveaux morceaux. Le chunking récursif nécessite également plus de ressources de calcul que celui à taille fixe.

### Découpage sémantique

Le chunking sémantique utilise des modèles d’embedding pour créer des représentations mathématiques de chaque phrase. Ensuite, l’algorithme de chunking crée des morceaux de phrases sémantiquement similaires, créant un nouveau segment s’il détecte un changement dans la sémantique. Le chunking sémantique est attribué à Greg Kamradt, qui a abordé cette technique sur Github.1

Le chunking sémantique tient compte du contexte et construit les morceaux autour du flux naturel et de la sémantique du document. Lorsque le sujet change, un nouveau morceau est créé. Cependant, des problèmes peuvent survenir lorsque les paragraphes traitent de plusieurs sujets ou que le seuil de segmentation n’est pas correctement défini pour le type et la structure du document.

Le chunking sémantique est plus intensif en termes de calcul que le chunking récursif et celui à taille fixe, et a besoin de modèles avancés pour identifier le contenu sémantique dans le texte.

## Comment fonctionne le découpage agentique ?

Le chunking agentique est un exemple d’[automatisation agentique](https://www.ibm.com/fr-fr/think/topics/agentic-automation) : utiliser des [agents IA](https://www.ibm.com/fr-fr/think/topics/ai-agents) pour [automatiser un workflow](https://www.ibm.com/fr-fr/think/topics/workflow-automation). Dans ce cas, l’[automatisation intelligente](https://www.ibm.com/fr-fr/think/topics/workflow) du [workflow](https://www.ibm.com/fr-fr/think/topics/intelligent-automation) consiste à déterminer comment diviser un document en morceaux adaptés à la fenêtre contextuelle du LLM.

[L’IA agentique](https://www.ibm.com/fr-fr/think/topics/agentic-ai) désigne l’utilisation de systèmes d’IA qui prennent des décisions autonomes et agissent sans intervention humaine. Avec le chunking agentique, l’agent agit seul pour déterminer comment diviser le texte et étiqueter les morceaux.

Le chunking (ou segmentation) agentique s’inspire d’autres méthodes pour créer des sections superposées et un découpage récursif, appliquer [l’IA générative](https://www.ibm.com/fr-fr/think/topics/generative-ai) pour étiqueter chaque segment avec des [métadonnées](https://www.ibm.com/fr-fr/think/topics/metadata) et faciliter la récupération RAG.

Le chunking agentique en est encore aux stades exploratoires. Les créateurs partagent et discutent de leurs approches sur GitHub. Ces dernières sont souvent créées à l'aide du langage de codage Python et de cadres LLM tels que Llamaindex et Langchain, ainsi que de LLM [open source](https://www.ibm.com/fr-fr/think/topics/open-source-llms) disponibles sur Huggingface. 

Un [workflow d’IA type](https://www.ibm.com/fr-fr/think/topics/ai-workflow) pour le chunking agentique peut comporter les étapes suivantes :

### 1. Préparation du texte

Grâce à des outils d’automatisation intelligente, le texte est extrait du document source, par exemple un PDF, et nettoyé. Le nettoyage du texte implique la suppression des éléments superflus tels que les numéros de page et les pieds de page, afin que le LLM ne reçoive que du texte brut.

### 2. Fractionnement du texte

Les algorithmes de chunking récursif découpent le texte en petits morceaux pour éviter de hacher les phrases. À l’instar du chunking sémantique, le chunking agentique divise dynamiquement le texte en fonction de la signification, de la structure et du contexte à l’aide de la technique de chevauchement des morceaux.

### 3. Découpage des morceaux

Les LLM, tels que le [GPT](https://www.ibm.com/fr-fr/think/topics/gpt) d’OpenAI, traitent, combinent et enrichissent les morceaux. Les petits morceaux sont combinés pour former des morceaux plus grands et préserver la cohérence sémantique. Le LLM enrichit chaque morceau de métadonnées qui incluent un titre et un résumé de son contenu. Les métadonnées générées facilitent l’utilisation en aval, comme avec les [systèmes de RAG agentique](https://www.ibm.com/fr-fr/think/topics/agentic-rag).

### 4. Embedding

Chaque morceau est converti en embedding et stocké dans une base de données vectorielle. Les modèles de récupération interrogent la base de données, utilisent la recherche sémantique pour trouver les morceaux avec des métadonnées pertinentes et les incluent dans les prompts du LLM dans le système RAG.

Le paramètre prompt_template de LangChain détermine le prompt d’entrée passé au LLM. En savoir plus sur l’[optimisation du chunking RAG avec LangChain et watsonx.ai.](https://www.ibm.com/fr-fr/think/tutorials/use-agentic-chunking-to-optimize-llm-inputs-with-langchain-watsonx-ai)

## Avantages du découpage agentique

Le dynamisme et l’étiquetage de métadonnées que propose le chunking agentique en font une solution idéale pour la mise en œuvre de la RAG. Voici ses avantages :

- **Récupération efficace :** les titres et résumés générés par l’IA pour chaque morceau aident les systèmes RAG à trouver les informations pertinentes plus rapidement dans les [jeux de données](https://www.ibm.com/fr-fr/think/topics/dataset) connectés.

- **Réponses exactes :** le chunking sémantiquement cohérent avec les métadonnées générées par l’IA aide les systèmes RAG à enrichir les réponses générées avec des données pertinentes pour améliorer les réponses.

- **Flexibilité :** le chunking piloté par l’IA peut gérer divers types de documents. Les systèmes de chunking agentique peuvent s’intégrer à diverses chaînes LLM et RAG pour s’adapter à l’évolution et à l’expansion du projet.

- **Préservation du contenu :** les systèmes de chunking agentique s’appuient sur les méthodes antérieures pour créer des morceaux qui préservent le sens et la cohérence.
