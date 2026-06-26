---
titre: "Qu'est-ce que le prompt engineering"
type: "Concept"
theme: prompting
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/prompt-engineering
source_titre: "Qu’est-ce que le prompt engineering ?"
---

# Qu'est-ce que le prompt engineering

**En une phrase** — la discipline de conception et de raffinement itératif des instructions textuelles fournies à un LLM pour orienter sa sortie.

## En détail
Le prompt engineering désigne l'élaboration de requêtes qui aident les modèles d'IA générative à comprendre non seulement le langage mais aussi la nuance et l'intention derrière la requête. La règle de base est que « de bons prompts donnent de bons résultats » : un prompt bien conçu réduit le besoin de révision et d'édition post-génération. Le processus repose sur un raffinement itératif : l'ingénieur affine les prompts en fonction des réponses du modèle. Les compétences attendues sont : connaissance des LLM, communication, vulgarisation technique, maîtrise de Python, structures de données et algorithmes, créativité et évaluation réaliste des risques. Trois techniques avancées sont distinguées : zero-shot, few-shot et chaîne de pensées (CoT). Les cas d'usage cités : chatbots, santé, développement logiciel, ingénierie logicielle, cybersécurité.

## Exemple
La source illustre les usages « limites » par des cas réels : des chercheurs ont conçu, par prompt engineering, un système traduisant une langue sans entraînement sur texte parallèle ; d'autres ont intégré l'IA générative dans des jeux pour un storytelling réactif aux joueurs ; d'autres encore ont obtenu des informations inédites sur les phénomènes astronomiques des trous noirs. En cybersécurité, des prompts simulent des cyberattaques pour concevoir de meilleures défenses et déceler des vulnérabilités logicielles. Tous dépassent la « portée originelle » des modèles, sans réentraînement.

## Tradeoff / insight pour un senior
L'écriture de prompts est dépendante du modèle cible (l'exemple GPT-3/GPT-4 vs Google Bard est daté). L'insight durable : le prompt engineering est un substitut bon marché à l'entraînement, mais il ne compense pas un modèle de base faible — l'effort doit être calibré sur la criticité de la tâche, pas systématique.

## Source primaire
Page conceptuelle sans référence académique.

## Voir aussi
- [techniques-catalogue](techniques-catalogue.md)
- [rag-vs-fine-tuning-vs-prompt-engineering](rag-vs-fine-tuning-vs-prompt-engineering.md)
