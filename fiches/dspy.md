---
titre: "DSPy"
theme: gouvernance-alignement-ops
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/dspy
source_titre: "Qu’est-ce que DSPy ?"
---

# DSPy

**En une phrase** — « programmer, pas prompter » : on déclare des signatures et des modules en Python, et des optimiseurs compilent automatiquement les prompts contre un metric, au lieu de les rédiger et bricoler à la main.

## En détail
DSPy (boîte à outils Python open source, StanfordNLP) remplace le prompt hacking par une approche programmatique. Vocabulaire clé exposé : **Signature** (classe définissant types d'entrée/sortie d'un module, ex. question → reasoning + answer), **Module**, **Compilation** (traduction du programme Python en prompts exécutables, qui met à jour les paramètres internes : pondérations LM, instructions, démonstrations), **Optimiseur** (anciennement « téléprompteur », ex. BootstrapFewShot, BootstrapFewShotWithRandomSearch, BootstrapFinetune, LabeledFewShot), **Pipeline** et **Indicateurs** (correspondance exacte, F1 sémantique, métriques personnalisées). Le processus s'apparente à un algorithme évolutif : DSPy fait générer des prompts au LLM, les teste contre un metric, rejette ceux qui ne s'améliorent pas. Un tutoriel construit un RAG sur watsonx (Llama 3 + ColBERTv2, jeu de données HotPotQA, dspy.ChainOfThought, BootstrapFewShot) : la version compilée corrige une réponse fausse (« France » → « Turquie, Orhan Pamuk »). Lignes directrices : BootstrapFewShot pour ~10 exemples, RandomSearch au-delà de 50, Finetune pour la performance.

## Tradeoff / insight pour un senior
DSPy traite le prompt comme un artefact compilé, découplé du modèle sous-jacent : changer de LLM ou de données → recompiler, au lieu de réécrire des chaînes de prompts fragiles. Coût : courbe d'apprentissage du framework, besoin d'un jeu d'entraînement et d'un metric fiables, et opacité des prompts générés (à inspecter via inspect_history). L'optimisation auto-générée peut sur-ajuster au trainset.

## Source primaire
Dépôt [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) (open source, documentation et tutoriels) ; jeu de données HotPotQA ([hotpotqa.github.io](https://hotpotqa.github.io/)).

## Voir aussi
- [Optimisation des prompts](prompt-optimization.md)
- [In-context learning](in-context-learning.md)
