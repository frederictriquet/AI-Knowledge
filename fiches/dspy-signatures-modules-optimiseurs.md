---
titre: "DSPy : signatures, modules, optimiseurs"
type: "Concept"
theme: gouvernance-alignement-ops
niveau: 🔴
source_url: https://arxiv.org/abs/2310.03714
source_titre: "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines"
---

# DSPy : signatures, modules, optimiseurs

**En une phrase** — DSPy remplace les « prompt templates » codés en dur par trois abstractions composables — *signatures* déclaratives, *modules* paramétrés (Predict, ChainOfThought, ReAct…) et *teleprompters* (optimiseurs) — pour qu'on programme un pipeline LM au lieu de rédiger des prompts.

## Ce que dit la source
Le papier pose DSPy comme un *programming model* qui traite les LM comme des « abstract devices for text generation » et abstrait les pipelines en *text transformation graphs* (graphes de calcul impératifs où les LM sont invoqués via des modules déclaratifs). Il contribue trois abstractions vers l'optimisation automatique :

- **Signatures** — déclaration typée en langage naturel d'une fonction : un tuple de champs d'entrée et de sortie (plus une instruction optionnelle), spécifiant *quoi* faire (« consume questions and return answers ») plutôt que *comment* prompter un LM précis. Notation abrégée `question -> answer` ; les noms de champs portent le rôle sémantique et sont étendus en instructions par le compilateur (`english_document -> french_translation` prompte une traduction EN→FR). Avantage vs prompt : compilables en prompts/finetunes auto-améliorants et adaptés au pipeline, et gestion du formatage/parsing structuré pour réduire la manipulation de chaînes fragile.
- **Modules** — composants adaptatifs analogues à des couches de réseau de neurones, qui remplacent les techniques de prompting manuelles et se composent dans des pipelines arbitraires. Le module cœur est **Predict** (stocke la signature, un LM optionnel, une liste de démonstrations ; se comporte comme une fonction callable type couche PyTorch). Modules plus sophistiqués cités : **ChainOfThought**, **ProgramOfThought**, **MultiChainComparison**, **ReAct** — chacun généralisant une technique de la littérature (respectivement Wei et al. 2022, Chen et al. 2022, Yoran et al. 2023, Yao et al. 2022) et implémenté en quelques lignes en étendant la signature et en appelant Predict. Exemple : passer de `Predict` à `ChainOfThought` ajoute un champ `rationale` (« Reasoning: Let's think step by step. ») avant la sortie. Les **outils** sont des modules exécutant du calcul : `dspy.Retrieve` (support intégré ColBERTv2, Pyserini, Pinecone), `dspy.SQL`, `dspy.PythonInterpreter` (expérimentaux).
- **Paramétrisation** — tout appel LM implémentant une signature spécifie : (1) le LM à appeler, (2) les instructions de prompt et le préfixe de chaque champ, (3) — le plus important — les *démonstrations* utilisées comme exemples few-shot (LM gelés) ou comme données d'entraînement (finetuning). DSPy se concentre sur la génération et la sélection automatiques de démonstrations.
- **Programmes** — interface *define-by-run* inspirée de PyTorch et Chainer : on déclare les modules à l'init, puis on les compose dans une méthode `forward` avec du contrôle de flux arbitraire (if, for, exceptions). Exemple complet d'un RAG en ~10 lignes (`Retrieve` + `ChainOfThought("context, question -> answer")`).
- **Teleprompters** — optimiseurs qui prennent un programme, un trainset et un metric, et renvoient un nouveau programme optimisé. Les trainsets peuvent être petits (une poignée d'exemples), incomplets (entrées seules) et sans labels pour les étapes intermédiaires — on suppose typiquement des labels seulement pour la sortie finale. Cette efficacité en labels est critique pour la modularité : construire un nouveau pipeline = recompiler son code, pas réannoter. Les metrics vont de l'exact match (EM) ou F1 jusqu'à des programmes DSPy entiers.

Le papier s'inspire explicitement du consensus autour des abstractions de réseaux de neurones (couches composables ; poids entraînés par optimiseurs plutôt qu'ajustés à la main) et emprunte sa syntaxe à PyTorch. DSPy est la seconde itération du framework Demonstrate–Search–Predict (DSP, Khattab et al. 2022).

## Pourquoi c'est utile
Le papier fondateur apporte le *pourquoi* conceptuel : l'analogie « hand-tuning the weights of a classifier » qui rend le prompt manuel fragile et non scalable, et le cadre théorique du *text transformation graph* avec interface define-by-run type PyTorch. Il montre aussi que chaque module générique (CoT, ReAct…) est une généralisation paramétrée d'une technique de la littérature, encodée en quelques lignes de code plutôt qu'en prompts rédigés à la main.

## Points clés
- Trois abstractions : *signatures* (interface typée déclarative), *modules* (techniques de prompting paramétrées et composables), *teleprompters* (optimiseurs pilotés par un metric).
- Notation abrégée `question -> answer` ; les noms de champs encodent le rôle sémantique.
- Un module = quelques lignes ; changer `Predict` → `ChainOfThought` est un drop-in.
- Define-by-run inspiré de PyTorch/Chainer : déclarer les modules, puis les composer dans `forward`.
- Label-efficient : labels requis seulement pour la sortie finale ; nouveau pipeline = recompiler, pas réannoter.
- « Teleprompter » = abstraire et automatiser le prompting « à distance », sans intervention manuelle.

## Voir aussi
- [DSPy](dspy.md) · [Optimisation des prompts](prompt-optimization.md)
- [DSPy : compilation & bootstrapping](dspy-compilation-bootstrap.md)
- [papier complet](../sources/dspy/md/dspy-paper.md)
