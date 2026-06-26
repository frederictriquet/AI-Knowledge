---
titre: "Error analysis : regarde tes données"
type: "Concept"
theme: evaluation
niveau: 🔴
source_url: https://hamel.dev/blog/posts/field-guide/
source_titre: "A Field Guide to Rapidly Improving AI Products"
objectifs: [fiabilite]
---

# Error analysis : regarde tes données

**En une phrase** — Avant toute métrique, lis manuellement les traces de ton produit, annote les comportements indésirables, puis construis une taxonomie des failure modes et compte leur fréquence.

## Ce que dit la source
Hamel présente l'error analysis comme « the single most valuable activity in AI development » et l'activité au plus haut ROI. L'erreur la plus fréquente des équipes est le « tools first » mindset : empiler dashboards et generic metrics au lieu de comprendre ce qui marche. Il oppose deux approches : le « top-down » (partir de métriques comme hallucination ou toxicity, qui rate les problèmes spécifiques au domaine) et le « bottom-up », plus efficace, qui force à regarder les vraies données et laisse les métriques émerger. Le processus concret chez NurtureBoss : un viewer simple, une note ouverte par conversation, puis un LLM pour bâtir une taxonomy des failure modes, enfin un mapping de chaque ligne à un label et un comptage des fréquences. Résultat : trois issues couvraient plus de 60 % des problèmes, et le date handling est passé de 33 % à 95 % de réussite.

## Exemple
Hamel ouvre sur une scène vécue : un client lui présente fièrement son dashboard d'évals à métriques génériques. Le piège : une équipe célèbre un « helpfulness score » gagnant 10 % pendant que ses utilisateurs échouent encore sur des tâches basiques — comme optimiser le temps de chargement du site quand le tunnel de paiement est cassé. À l'inverse, chez NurtureBoss, l'annotation libre fait émerger trois failure modes nommés : flux de conversation (contexte manquant, réponses maladroites), échecs de handoff (ne pas savoir transférer à un humain), et reprogrammation (gestion des dates). Le date handling échouait 66 % du temps sur des tournures comme « planifions une visite dans deux semaines ».

## Pourquoi c'est utile
Hamel fournit le protocole opérationnel concret (annoter, taxonomiser, compter) qui précède toute automatisation — là où la plupart des ressources restent au niveau conceptuel.

## À retenir
- Commencer par lire de vraies traces, pas par choisir un outil ou une métrique.
- Annoter en notes ouvertes (bottom-up), pas avec des catégories imposées d'avance.
- Utiliser un LLM pour synthétiser la taxonomy des failure modes à partir des notes.
- Mapper chaque trace à un failure mode et compter : viser le 20 % de causes qui produit 60-80 % des erreurs.
- En tirer directement des tests ciblés et mesurer l'amélioration sur ces failure modes.

## Voir aussi
- [Évaluation de trajectoire](evaluation-trajectoire.md)
- [Taxonomie d'erreurs d'appel de fonction](taxonomie-erreurs-appel-fonction.md)
- [Le prompt engineering est empirique](prompt-engineering-est-empirique.md)
- [post complet](../sources/hamel-husain/md/field-guide.md)
