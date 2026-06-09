# LangChain

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [51-langchain](../md/51-langchain.md)

**En une phrase** — un cadre d'orchestration open source qui fournit des abstractions modulaires (chaînes, index, mémoire, outils, agents) pour bâtir des applications pilotées par LLM, branchables sur quasi n'importe quel modèle.

## Ce que dit le corpus
LangChain est un cadre d'orchestration open source (bibliothèques Python et JavaScript) qui simplifie la création d'applications pilotées par LLM. Son cœur est l'**abstraction** : représenter des processus complexes comme des composants nommés, « enchaînables » pour réduire le code nécessaire. Le corpus détaille les briques : **chaînes** (LLMChain, SimpleSequentialChain) qui relient modèle et prompt ; **index** (chargeurs de documents, bases vectorielles, séparateurs de texte, récupération/RAG) ; **mémoire** (conversation complète, résumé, n derniers échanges) ; **outils** (Wolfram Alpha, Google Search, Wikipedia…) ; et **agents** qui donnent au LLM la capacité de décider, planifier et agir étape par étape. Lancé par **Harrison Chase en octobre 2022**, LangChain était en juin 2023 le projet open source à plus forte croissance sur GitHub. Le corpus insiste sur l'intégration **watsonx** (package langchain_ibm, classes WatsonxLLM, ChatWatsonx) et mentionne LangGraph et LangSmith comme prolongements.

## Tradeoff / insight pour un senior
Pur vocabulaire pour qui code déjà des pipelines LLM. À retenir : l'abstraction accélère le prototypage mais « limite le degré de personnalisation » — le compromis classique framework vs contrôle bas niveau.

## Source primaire
Non citée académiquement par IBM — voir la documentation LangChain et le dépôt GitHub (hors-corpus).

## Voir aussi
- [langgraph](langgraph.md)
- [crewai](crewai.md)
