---
titre: "Architectures réactive / délibérative / cognitive"
type: "Concept"
theme: raisonnement-planification
niveau: 🟢
source_url: https://www.ibm.com/fr-fr/think/topics/agentic-architecture
source_titre: "Qu’est-ce qu’une architecture agentique ?"
source_primaire: "arXiv:2404.11584"
---

# Architectures réactive / délibérative / cognitive

**En une phrase** — trois niveaux de sophistication d'un agent : réflexe sans état, planificateur avec modèle du monde, ou système cognitif à mémoire et apprentissage.

## En détail
On distingue trois familles de frameworks agentiques. Les **architectures réactives** associent directement situations et actions ; elles sont réflexives, les décisions reposant sur les stimuli immédiats plutôt que sur la mémoire ou la prédiction — ces agents ne peuvent ni apprendre du passé ni planifier l'avenir. Les **architectures délibératives** prennent des décisions basées sur le raisonnement, la planification et des modèles internes du monde : contrairement aux agents réactifs, les agents délibératifs analysent leur environnement, prédisent les résultats futurs et font des choix éclairés avant d'agir. Les **architectures cognitives** sont des systèmes avancés qui imitent la pensée, le raisonnement, l'apprentissage et la prise de décision humains ; elles intègrent perception, mémoire, raisonnement et adaptation, chacun représenté par des modules individuels, et constituent le type le plus avancé. Le modèle BDI est rangé dans cette dernière catégorie.

## Exemple
Même mission « atteindre une cible dans un labyrinthe », trois agents. Le **réactif** applique un réflexe pur — *mur à droite → tourner à gauche* — sur le seul stimulus immédiat : ni mémoire des couloirs déjà visités, ni anticipation, il peut boucler indéfiniment. Le **délibératif** maintient un modèle interne du labyrinthe, simule plusieurs chemins, prédit lequel mène à la sortie et n'agit qu'après ce choix éclairé. Le **cognitif** ajoute des modules séparés de perception, mémoire, raisonnement et adaptation : il retient ses échecs passés et améliore sa stratégie d'un parcours à l'autre — le plus avancé, mais le plus coûteux.

## Tradeoff / insight pour un senior
Pur vocabulaire, qui recoupe la taxonomie AIMA : réactif = réflexe simple, délibératif = basé objectif/utilité, cognitif = apprenant + mémoire. L'axe est l'état conservé : sans état (rapide, prévisible) → modèle du monde (planifie) → mémoire + apprentissage (s'adapte, mais coûteux). Le choix dépend de l'observabilité et du dynamisme de l'environnement.

## Source primaire
Cette tripartition relève du vocabulaire classique de l'IA des agents (Wooldridge, Brooks pour le réactif). Bandura (doi:10.1146/annurev.psych.52.1.1) et Masterman et al. (arXiv:2404.11584) interviennent par ailleurs sur d'autres points.

## Voir aussi
- [Taxonomie des 5 types d'agents](taxonomie-5-types-agents.md)
- [Architecture BDI (Belief-Desire-Intention)](bdi.md)
