---
titre: "Qu'est-ce que le prompt engineering"
theme: prompting
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/prompt-engineering
source_titre: "Qu’est-ce que le prompt engineering ?"---

# Qu'est-ce que le prompt engineering

> Fiche du glossaire prompting · Pertinence 🟢 pur-nom · Provenance ✅ présent · Sources corpus : [../md/01-prompt-engineering.md](../sources/ibm-guide-prompt-engineering/md/01-prompt-engineering.md)

**En une phrase** — la discipline de conception et de raffinement itératif des instructions textuelles fournies à un LLM pour orienter sa sortie.

## Ce que dit le corpus
IBM définit le prompt engineering comme l'élaboration de requêtes qui aident les modèles d'IA générative à comprendre non seulement le langage mais aussi la nuance et l'intention derrière la requête. La règle de base est que « de bons prompts donnent de bons résultats » : un prompt bien conçu réduit le besoin de révision et d'édition post-génération. Le processus repose sur un raffinement itératif : l'ingénieur affine les prompts en fonction des réponses du modèle. Le corpus liste les compétences attendues (connaissance des LLM, communication, vulgarisation technique, maîtrise de Python, structures de données et algorithmes, créativité et évaluation réaliste des risques) et trois techniques avancées : zero-shot, few-shot et chaîne de pensées (CoT). Les cas d'usage cités : chatbots, santé, développement logiciel, ingénierie logicielle, cybersécurité.

## Tradeoff / insight pour un senior
Le corpus présente l'écriture de prompts comme dépendante du modèle cible (l'exemple GPT-3/GPT-4 vs Google Bard est daté). L'insight durable : le prompt engineering est un substitut bon marché à l'entraînement, mais il ne compense pas un modèle de base faible — l'effort doit être calibré sur la criticité de la tâche, pas systématique.

## Source primaire
Non citée par IBM — page conceptuelle sans référence académique (hors-corpus).

## Voir aussi
- [techniques-catalogue](techniques-catalogue.md)
- [rag-vs-fine-tuning-vs-prompt-engineering](rag-vs-fine-tuning-vs-prompt-engineering.md)
