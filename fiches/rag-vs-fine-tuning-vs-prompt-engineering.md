---
titre: "RAG vs fine-tuning vs prompt engineering"
theme: rag-contexte
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/rag-vs-fine-tuning-vs-prompt-engineering
source_titre: "RAG, réglage fin et prompt engineering"---

# RAG vs fine-tuning vs prompt engineering

> Fiche du glossaire prompting · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [../md/03-rag-vs-fine-tuning-vs-prompt-engineering.md](../sources/ibm-guide-prompt-engineering/md/03-rag-vs-fine-tuning-vs-prompt-engineering.md)

**En une phrase** — comparatif des trois leviers d'optimisation d'un LLM sur quatre axes (approche, objectifs, ressources, applications), présentés comme complémentaires et souvent combinés.

## Ce que dit le corpus
IBM compare trois méthodes. Le prompt engineering optimise les prompts d'entrée sans modifier significativement les paramètres ; c'est le moins coûteux, réalisable manuellement sans calcul supplémentaire, idéal pour les situations ouvertes (génération de contenu). La RAG connecte le LLM à une base de données et enrichit les prompts via recherche sémantique sur bases vectorielles ; elle exige une expertise data pour bâtir les pipelines, et brille quand des informations précises et actuelles priment (chatbots de service client). Le réglage fin réentraîne le modèle sur un jeu de données étiqueté spécifique au domaine, mettant à jour ses poids ; c'est le plus gourmand en temps et en calcul (GPU). Le corpus distingue réglage fin intégral et PEFT (parameter-efficient fine-tuning), ainsi que réglage fin (données étiquetées, expertise ciblée) vs pré-entraînement continu (apprentissage par transfert sur données non étiquetées).

## Tradeoff / insight pour un senior
L'arbitrage réel n'est pas « lequel choisir » mais « dans quel ordre les empiler » : commencer par le prompt engineering (coût nul), passer à la RAG quand le problème est un déficit de connaissances fraîches, réserver le fine-tuning aux déficits de comportement ou de format que le contexte ne corrige pas. La métaphore du cuisinier d'IBM (conseiller / livre de recettes / cours de cuisine) résume bien : connaissance vs accès vs compétence.

## Source primaire
Non citée par IBM — page conceptuelle sans référence académique (hors-corpus).

## Voir aussi
- [RAG agentique](rag-agentique.md)
- [prompt-tuning](prompt-tuning.md)
- [prompt-engineering](prompt-engineering.md)
