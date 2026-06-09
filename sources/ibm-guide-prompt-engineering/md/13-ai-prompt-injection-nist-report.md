> Source : https://www.ibm.com/fr-fr/think/insights/ai-prompt-injection-nist-report

# Comment pirater l’IA avec une injection de prompt : rapport NIST

##

Le National Institute of Standards and Technology (NIST) suit de près le cycle de vie de l’IA, et pour de bonnes raisons. À mesure que l’IA prolifère, il en va de même pour la découverte et l’exploitation des vulnérabilités de l’IA en matière de cybersécurité. L’injection de prompts est l’une des vulnérabilités qui attaquent spécifiquement l’IA générative.

Dans Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations, le NIST définit diverses tactiques de machine learning et de cyberattaques, comme l’injection de prompt, et conseille les utilisateurs sur la manière de les atténuer et de les gérer. Les tactiques AML extraient des informations sur le comportement des systèmes de machine learning (ML) afin de découvrir comment ils peuvent être manipulés. Ces informations sont utilisées pour attaquer l’IA et ses grands modèles de langage (LLM) afin de contourner la sécurité, de contourner les protections et d’ouvrir des voies d’exploitation.

## Qu’est-ce que l’injection de prompt ?

NIST définit deux types d’attaques par injection de prompt : directes et indirectes. Avec l’injection de prompt direct, un utilisateur saisit un prompt qui amène le LLM à effectuer des actions involontaires ou non autorisées. On parle d’injection de prompt indirecte lorsqu’un pirate empoisonne ou dégrade les données utilisées par un LLM.

Une des méthodes d’injection de prompt direct les plus connues est le DAN, Do Anything Now, un prompt utilisé contre ChatGPT. DAN utilise le jeu de rôle pour contourner les filtres de modération. Dans sa première itération, les prompts ont indiqué à ChatGPT qu’il s’agissait désormais de DAN. DAN pouvait faire tout ce qu’il voulait et devait faire semblant, par exemple, d’aider une personne malveillante à créer et à faire exploser des explosifs. Cette tactique a permis d’échapper aux filtres qui l’empêchaient de fournir des informations criminelles ou préjudiciables en suivant un scénario de jeu de rôle. OpenAI, les développeurs de ChatGPT, suivent cette tactique et mettent à jour le modèle pour empêcher son utilisation, mais les utilisateurs continuent de contourner les filtres jusqu’au point où la méthode a évolué vers (au moins) DAN 12.0.

L’injection de prompt indirecte, comme le note le NIST, dépend de la capacité d’un attaquant à fournir des sources qu’un modèle d’IA générative ingérerait, comme un PDF, un document, une page web ou même des fichiers audio utilisés pour générer de fausses voix. L’injection de prompt indirecte est largement considérée comme la plus grande faille de sécurité de l’IA générative, sans moyens simples pour trouver et corriger ces attaques. Les exemples de ce type de prompt sont nombreux et variés. Elles peuvent être absurdes (faire répondre un chatbot en utilisant un « langage pirate »), préjudiciables (utiliser le chat d’ingénierie sociale pour convaincre un utilisateur de révéler sa carte de crédit et d’autres données personnelles) ou générale (détourner les assistants d’IA pour envoyer des e-mails frauduleux à l’ensemble de votre liste de contacts).

Découvrir les solutions de cybersécurité d'AI

## Comment arrêter les attaques par injection de prompt

Ces attaques ont tendance à être bien cachées, ce qui les rend à la fois efficaces et difficiles à arrêter. Comment se protéger contre l’injection directe de prompt ? Comme le note le NIST, il est impossible de les arrêter complètement, mais les stratégies défensives apportent une certaine protection. Pour les créateurs de modèles, le NIST recommande de s’assurer que les jeux de données sont soigneusement organisés. Ils suggèrent également d’entraîner le modèle sur les types d’entrées qui signalent une tentative d’injection de prompt et de l’entraîner à identifier les prompts adverses.

Pour l’injection de prompts indirecte, le NIST suggère l’intervention humaine pour affiner les modèles, ce que l’on appelle l’apprentissage par renforcement basé sur les commentaires humains (RLHF). Le RLHF aide les modèles à mieux s’aligner sur les valeurs humaines qui empêchent les comportements indésirables. Une autre suggestion consiste à filtrer les instructions à partir des entrées récupérées, ce qui peut empêcher l’exécution d’instructions indésirables provenant de sources extérieures. Le NIST suggère en outre d’utiliser des modérateurs LLM pour aider à détecter les attaques qui ne s’appuient pas sur des sources récupérées pour s’exécuter. Enfin, le NIST propose des solutions basées sur l’interprétabilité. Cela signifie que la trajectoire de prédiction du modèle qui reconnaît les entrées anormales peut être utilisée pour détecter puis arrêter les entrées anormales.

L’IA générative et ceux qui souhaitent exploiter ses vulnérabilités continueront à modifier l’environnement de la cybersécurité. Mais cette même puissance de transformation peut également apporter des solutions. En savoir plus sur la manière dont IBM Security fournit des solutions de cybersécurité basées sur l’IA qui renforcent les défenses de sécurité.
