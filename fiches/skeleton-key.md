---
titre: "Skeleton Key & jailbreaks multi-tours"
theme: securite
niveau: 🔴
provenance: ✅
base: ibm-guide-prompt-engineering
source_url: https://www.ibm.com/fr-fr/think/insights/llm-skeleton-key
source_titre: "Quand les chatbots IA deviennent mauvais"
---

# Skeleton Key & jailbreaks multi-tours

> Fiche du glossaire prompting · Pertinence 🔴 substance · Provenance ✅ présent · Sources corpus : [../md/15-llm-skeleton-key.md](../sources/ibm-guide-prompt-engineering/md/15-llm-skeleton-key.md)

**En une phrase** — technique de débridage Microsoft en plusieurs interactions (faire ajouter un avertissement puis produire le contenu interdit), que les analyses IBM relativisent face à la menace single-shot, plus discrète mais plus urgente.

## Ce que dit le corpus
Skeleton Key est présentée par IBM comme une technique Microsoft, processus à plusieurs étapes conçu pour contourner les garde-fous éthiques. Chenta Lee (architecte en chef renseignement sur les menaces, IBM) la décrit comme unique parce qu'elle nécessite de multiples interactions, là où la plupart des injections de prompt visaient à perturber l'IA en une seule tentative — d'où un taux de réussite potentiellement accru. Le mécanisme typique : convaincre l'IA de fournir un avertissement avant de partager un contenu qu'elle rejetterait normalement. Lee tempère le buzz médiatique : les attaques single-shot restent une préoccupation plus urgente car plus faciles à exécuter, et il cite l'exemple d'une injection de prompt cachée dans un CV traité par un système de recrutement (ATS) alimenté par l'IA — une attaque one-shot, sans possibilité d'interactions multiples. Autres exemples concrets : un agent conversationnel manipulé pour accorder des remises non autorisées, des PoC montrant la génération de code malveillant et l'interception/déformation de conversations audio en quasi temps réel. Défenses évoquées : améliorer l'entraînement pour que le modèle détecte l'attaque, et des pare-feux IA inspectant toutes les requêtes entrantes. Lee compare l'adoption lente à venir au paramétrage anti-injection SQL, qui a mis 5 à 10 ans à devenir réflexe.

## Tradeoff / insight pour un senior
Ne pas se laisser hypnotiser par le multi-tours médiatique : la surface single-shot (CV, document, page web ingérés automatiquement, sans humain dans la boucle) est plus exploitable car elle ne suppose aucun dialogue. L'analogie SQL est l'insight clé — on entre dans la même décennie d'apprentissage collectif : « ne jamais donner d'instructions brutes à un LLM » deviendra l'équivalent de « toujours paramétrer ses requêtes ».

## Source primaire
Page IBM citée (think/insights/llm-skeleton-key). Citations directes de Chenta Lee (IBM), Stephen Kowski (SlashNext) et Narayana Pappu (Zendata). Technique Skeleton Key attribuée à Microsoft ; pas de référence académique formelle.

## Voir aussi
- [jailbreak](jailbreak.md)
- [prompt-injection](prompt-injection.md)
