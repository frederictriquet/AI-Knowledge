> Source : https://www.ibm.com/fr-fr/think/topics/directional-stimulus-prompting

# Qu’est-ce que le prompting par stimulus directionnel (DSP) ?

## Qu’est-ce que l’apprentissage directionnel de stimulus (DSP) ?

Le prompting par stimulus directionnel (DSP) est une nouvelle méthodologie de prompting dans le traitement automatique du langage naturel (NLP) dans laquelle un modèle est présenté avec un stimulus directif ou structuré afin de générer les résultats souhaités.

Contrairement aux méthodes standard telles que l’apprentissage one-shot, zero-shot ou few-shot, cette approche se distingue en permettant un contrôle direct sur les résultats du modèle en établissant des critères ou en fournissant des instructions. Dans ce cadre, un stimulus directeur agit comme un mécanisme de contrôle du processus génératif du modèle selon des lignes définies par un certain critère.

Le prompting par stimulus directionnel (DSP) est utile lorsqu’une tâche nécessite un ensemble spécifique de réponses, très sensibles au contexte, mais sans données étiquetées.

Ainsi, lors de tâches de synthèse, où il est essentiel de conserver les informations critiques, le DSP fournit un stimulus directeur qui incite le modèle à produire d’une manière spécifique. Cela permet de générer des résumés plus précis et mieux adaptés au contexte.[1](#f01)

Besoin d’un prompt de stimulus directionnel\
--------------------------------------------

Les grands modèles de langage (LLM) tels que GPT-3, 4 et PaLM sont communément appelés modèles « boîte noire » car les utilisateurs n’ont pas accès à leurs composants internes, tels que les paramètres, les méthodes de réglage ou les processus de prise de décision.

Cette interaction se fait essentiellement par le biais de prompts textuels qui utilisent des appels d’interface de programmation d’application (API) comme principaux mécanismes d’entrée et de sortie. Bien que ces modèles soient excellents, leur capacité à produire des résultats précis et spécifiques à une tâche dépend souvent fortement de la qualité des prompts.[2](#f02)[, 3](#f03)

Dans ce contexte, le prompt engineering visant à concevoir des prompts ciblées pour orienter le comportement du modèle est pertinent. Les approches manuelles et automatisées ont donné des résultats remarquables. Cependant, elles ne sont pas sans inconvénients, en particulier pour les tâches qui exigent un contrôle strict ou des résultats très spécifiques à chaque résultat.

Par exemple, des tâches telles que la synthèse ou la génération de dialogues demandent que le modèle suive systématiquement des comportements cibles, tels que l’inclusion de détails clés ou le respect d’un modèle de raisonnement strict ou de directives stylistiques prescrites. Les techniques conventionnelles ne suffisent souvent pas à garantir le respect continu de ces exigences nuancées.

Le prompting par stimulus directionnel (DSP) vient combler cette lacune. Le DSP est un petit modèle de politique auxiliaire qui génère des prompts directionnels adaptés aux instances pour guider le LLM dans ses décisions.

Chaque prompt établit un contexte spécifique à l’instance et a pour fonction d’inciter le LLM à générer des réponses plus cohérentes et plus adaptées. En intégrant le DSP dans le processus, les utilisateurs disposent d’un outil puissant pour corriger le comportement des LLM « boîte noire » afin d’obtenir une plus grande cohérence, pertinence et précision dans les travaux qui nécessitent de la précision.[1](#f01)

## Comment fonctionne le DSP

Entraînement du modèle de politique avec affinement supervisé (SFT)

Le processus d’entraînement du modèle de politique commence par un affinement supervisé (SFT) sur un modèle pré-entraîné tel que T5, GPT-2 ou tout autre LLM adapté. L’idée principale est d’affiner un modèle de politique plus petit sur des données d’entraînement qui génèrent des stimuli directionnels plutôt que de modifier directement le LLM.

Ce processus est efficace car l’affinement d’un modèle de politique plus petit et spécifique à une tâche évite les défis et les coûts de calcul associés à l’entraînement direct de modèles complexes et de grande taille.

Pour former ce modèle, un petit jeu de données étiquetées est créé, dans lequel chaque entrée est associée à un pseudo-stimulus. Ces pseudo-stimuli sont conçus pour guider les réponses du LLM dans la direction souhaitée en fonction de la tâche à accomplir.

Ainsi, dans une tâche de synthèse, le pseudo-stimulus peut être constitué de mots-clés ou de phrases tirés d’un résumé de référence. Pour les tâches de génération de dialogue, des actes de dialogue tels que des demandes, des questions ou des déclarations peuvent être employés comme pseudo-stimuli.

Ces stimuli servent de signaux que le modèle de politique exploite pour générer des entrées spécifiques à la tâche qui orientent efficacement la sortie du LLM vers le comportement cible.

Le jeu de données étiquetées utilisé pour le SFT peut être relativement petit, car l’objectif est de fournir au modèle de langage de politique les connaissances nécessaires pour générer des stimuli, et non d’entraîner un LLM massif à partir de zéro. Le SFT est donc un moyen économe en ressources d’amorcer le modèle de politique avec des connaissances fondamentales sur les exigences spécifiques à la tâche.[4](#f04)

Affinement par apprentissage par renforcement (RL)

Après l’affinement initial avec le SFT, le modèle de politique est optimisé grâce à l’apprentissage par renforcement (RL). Le RL permet au modèle de politique d’explorer et d’affiner sa capacité à générer des stimuli qui conduisent à des sorties LLM de meilleure qualité. L’idée centrale de cette phase est de s’appuyer sur une fonction de récompense pour évaluer l’efficacité des stimuli générés.

Dans les tâches de synthèse, par exemple, la fonction de récompense peut être basée sur des indicateurs telles que les scores ROUGE ou BLEU, qui mesurent la qualité du résumé généré par rapport à celui de référence. 

En se concentrant sur l’entraînement du modèle de politique plutôt que directement sur le LLM, le DSP surmonte les défis associés à l’affinement des modèles boîte noire, ce qui conduit à une méthode plus efficace et plus évolutive. 

**** Figure 1 : Architecture du cadre de DSP 

 

## Avantages et inconvénients du DAST

Le prompting par stimulus directionnel présente des avantages notables et certains défis, ce qui en fait une technique aussi intrigante que complexe. Voici un aperçu plus détaillé de ses avantages et de ses inconvénients.[5](#f05)

Avantages :

Mécanisme d’attention ciblée : le mécanisme d’attention ciblée du DSP met l’accent sur les tokens ou les informations pertinents, améliorant ainsi la précision et l’efficacité en concentrant le traitement sur les composants essentiels.

Utilisation optimisée des ressources : en se focalisant sur les stimuli pertinents, le stimulus directionnel réduit les besoins en matière de jeux de données. Cela se traduit par des temps de traitement plus courts et des coûts de calcul moins élevés.

Précision améliorée : en isolant et en mettant l’accent sur les tokens d’entrée les plus pertinents, le stimulus directionnel améliore la précision des réponses et des interprétations du modèle de langage.

Adaptabilité : cette approche peut être personnalisée pour diverses tâches linguistiques, allant de la génération de texte à l’analyse des sentiments, et offre ainsi une grande polyvalence dans différentes applications de traitement automatique du langage naturel.

Inconvénients :

Dépendance à l’égard de signaux précis : le succès du prompting par stimulus directionnel dépend fortement de la précision des stimuli, qui peut être difficile à obtenir dans des environnements complexes ou bruyants. Si le contexte ou les stimuli subissent des changements importants, l’efficacité de la méthode peut diminuer et réduire ainsi sa fiabilité.

Complexité de la configuration : la mise en place de stimuli directionnels exige une conception et un calibrage minutieux, ce qui peut compliquer le processus de configuration initial.

Généralisation limitée : sa capacité à généraliser différents types de signaux ou des variations d’entrée inattendues est limitée, ce qui restreint son applicabilité dans des contextes plus larges.

##

## Cas d’utilisation

Le prompting par stimulus directionnel (DSP) présente un grand potentiel pour diverses tâches de NLP, guidant efficacement les modèles afin d’améliorer leurs performances.

Synthèse : le DSP est utilisé pour créer des résumés souhaités qui correspondent davantage aux résumés de référence. Dans une expérience menée sur un sous-ensemble réduit de seulement 4 000 échantillons issus du jeu de données CNN/Daily Mail, le DSP a permis d’améliorer les performances de référence (mesurées notamment par ROUGE, BLEU et d’autres indicateurs, y compris les scores de préférences humaines) de 4 % à 13 %, surpassant ainsi certains modèles entièrement supervisés.[6](#f05)

Génération de réponses au dialogue : dans le cadre de la génération de dialogues axés sur des tâches, le DSP a aidé ChatGPT à produire des réponses plus précises et plus pertinentes. Par exemple, avec seulement 80 dialogues provenant du jeu de données MultiWOZ, le DSP a permis d’améliorer les performances de 41,4 %, surpassant plusieurs modèles de pointe (tels que ChatGPT, Codex et InstructGPT) entraînés sur des ensembles de données plus importants.[7](#f07)

Raisonnement en chaîne : le DSP améliore également le raisonnement en chaîne en générant des prompts spécifiques à chaque instance qui surpassent les prompts spécifiques à une tâche conçues par l’humain et générées automatiquement. La précision du raisonnement en est ainsi renforcée. Ces exemples illustrent comment le DSP peut offrir des conseils ciblés, améliorant ainsi les performances des modèles dans toute une série d’applications du NLP.[8](#f08)
