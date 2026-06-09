---
titre: "Taxonomie des erreurs d'appel de fonction"
theme: fondamentaux-agents
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/ai-agent-evaluation
source_titre: "Qu’est-ce que l’évaluation des agents IA ?"---

# Taxonomie des erreurs d'appel de fonction

> Fiche du glossaire des patterns · Pertinence 🔴 substance · Provenance ✅ présent · Sources corpus : [60-ai-agent-evaluation](../sources/ibm-guide-agents-ia/md/60-ai-agent-evaluation.md)

**En une phrase** — une grille concrète pour évaluer le tool-calling : cinq erreurs détectables par règles déterministes, plus deux contrôles sémantiques délégués à un LLM-juge.

## Ce que dit le corpus
Le fichier 60 distingue deux familles. Les **indicateurs basés sur des règles** (« efficacité opérationnelle des systèmes pilotés par l'IA ») : **Nom de fonction incorrect** (la fonction existe mais le nom/l'orthographe est faux, échec d'exécution) ; **Paramètres requis manquants** (un ou plusieurs paramètres nécessaires omis) ; **Type de valeur de paramètre incorrect** (chaîne/nombre/booléen ne correspondant pas à l'attendu) ; **Valeurs autorisées** (valeur hors de l'ensemble accepté ou prédéfini) ; **Paramètre halluciné** (paramètre non défini ni pris en charge par la spécification de la fonction). Les **indicateurs sémantiques basés sur le LLM en tant que juge** : l'**ancrage des valeurs des paramètres** (« garantir que chaque valeur de paramètre est directement dérivée du texte de l'utilisateur, de l'historique du contexte… ou des valeurs par défaut des spécifications de l'API ») et la **transformation des unités** (« vérifie les conversions d'unités ou de formats, au-delà des types de base, entre les valeurs dans le contexte et les valeurs des paramètres dans l'appel d'outil »).

## Tradeoff / insight pour un senior
La pépite opérationnelle du corpus. La séparation règles/LLM-juge est le bon design : les cinq premières erreurs se valident sans modèle (parsing du schéma de fonction, validation de type, vérification d'enum) — rapide, déterministe, gratuit. On ne mobilise le LLM-juge, coûteux et faillible, que pour ce que les règles ne peuvent pas trancher : la sémantique (la valeur passée provient-elle vraiment du contexte ? l'unité a-t-elle été convertie correctement ?). Réutilisable tel quel comme checklist d'éval de tool-calling.

## Source primaire
Non citée par IBM — la taxonomie est présentée sans référence externe (hors-corpus).

## Voir aussi
- [llm-as-a-judge](llm-as-a-judge.md)
- [evaluation-trajectoire](evaluation-trajectoire.md)
