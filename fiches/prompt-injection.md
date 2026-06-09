---
titre: "Injection de prompt"
theme: securite
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/topics/prompt-injection
source_titre: "Qu’est-ce qu’une attaque par injection d’invites ?"
---

# Injection de prompt

**En une phrase** — faire exécuter à un LLM des instructions malveillantes déguisées en entrée légitime, faille irréductible car prompt système et entrée utilisateur partagent le même type : du langage naturel.

## En détail
L'injection de prompt est une cyberattaque où des entrées malveillantes sont camouflées en prompts légitimes pour détourner un LLM (fuite de données, désinformation, exécution de code, propagation de malware). La cause racine : prompt système (fiable) et entrée utilisateur (non fiable) sont tous deux des chaînes en langage naturel, le modèle ne peut donc pas les distinguer par type de données — d'où le parallèle avec l'injection SQL et l'ingénierie sociale. Deux variantes : directe (le pirate contrôle l'entrée, ex. « Ignore les instructions précédentes ») et indirecte (charge utile cachée dans une source ingérée : page web, PDF, image, forum). Le NIST la traite dans *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*, distinguant les mêmes deux types et présentant l'injection indirecte comme la plus grande faille de la GenAI, sans correctif simple. Chronologie : Preamble la découvre confidentiellement (mai 2022), Riley Goodside la met au jour publiquement sur GPT-3 (11 sept. 2022), Simon Willison la nomme officiellement (12 sept. 2022), Greshake et al. publient la première description de l'injection indirecte (23 fév. 2023). C'est la vulnérabilité n°1 du Top 10 OWASP pour applications LLM.

## Tradeoff / insight pour un senior
Il n'existe pas de fix complet : éliminer la faille reviendrait à brider la flexibilité même qui rend le LLM utile. Le bon modèle mental est qu'aucune frontière de confiance n'existe à l'intérieur du prompt — toute donnée ingérée (RAG, outils, mémoire) est potentiellement adversariale. La défense est architecturale (moindre privilège, human-in-the-loop), pas un simple filtre.

## Références
Rapport NIST *Adversarial Machine Learning*. Découverte et nommage attribués à Goodside et Willison ; injection indirecte à Greshake, Abdelnabi, Mishra, Endres, Holz et Fritz (fév. 2023).

## Voir aussi
- [Sécurité agentique](securite-agentique.md)
- [lethal trifecta](lethal-trifecta.md)
- [prevent-prompt-injection](prevent-prompt-injection.md)
- [jailbreak](jailbreak.md)
