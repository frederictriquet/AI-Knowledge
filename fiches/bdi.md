---
titre: "Architecture BDI (Belief-Desire-Intention)"
type: "Concept"
theme: fondamentaux-agents
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/agentic-architecture
source_titre: "Qu’est-ce qu’une architecture agentique ?"
---

# Architecture BDI (Belief-Desire-Intention)

**En une phrase** — un découpage du raisonnement de l'agent en trois registres (ce qu'il sait, ce qu'il veut, ce qu'il décide de faire), antérieur aux LLM.

## En détail
L'architecture BDI est un modèle (ou framework) conçu pour modéliser la prise de décision rationnelle chez des agents intelligents, basé sur le cadre croyance-désir-intention. Elle modélise le raisonnement humain à partir de trois composants : les **Croyances (B)**, connaissances de l'agent sur le monde et données sensorielles (« La porte est fermée. ») ; les **Désirs (D)**, buts ou objectifs de premier niveau, qui ne sont pas nécessairement des actions (« Je veux entrer dans la pièce. ») ; les **Intentions (I)**, le plan d'action sur lequel l'agent s'engage activement en tenant compte de ses croyances et désirs (« Je vais ouvrir la porte pour entrer. »). Le BDI est rangé dans les architectures cognitives, considérées comme le type d'architecture agentique le plus avancé.

## Exemple
Déroulé du raisonnement humain modélisé par la source, registre par registre. **Croyance (B)** — donnée sensorielle brute : « La porte est fermée. » **Désir (D)** — objectif de premier niveau, qui n'est pas encore une action : « Je veux entrer dans la pièce. » **Intention (I)** — le plan engagé, dérivé en confrontant croyances et désirs : « Je vais ouvrir la porte pour entrer. » Le point clé est cette dérivation D→I : un désir reste un but abstrait tant qu'aucune intention ne s'y attache, et une fois l'intention prise l'agent y persiste plutôt que de la réviser à chaque nouvelle perception — d'où la stabilité des plans qui distingue BDI d'une boucle réactive.

## Tradeoff / insight pour un senior
Le compromis : BDI sépare explicitement les objectifs (désirs) du plan engagé (intentions), ce qui évite qu'un agent change de but à chaque nouvelle perception — il « persiste » dans une intention. C'est une réponse au problème de la stabilité des plans face à un environnement changeant, problème que les boucles ReAct naïves gèrent mal. Modèle pré-LLM (années 1990, Rao & Georgeff) recyclé comme grille de lecture pour les agents modernes.

## Source primaire
Bandura A., « Social cognitive theory: an agentic perspective », *Annual Review of Psychology* 2001;52:1-26, doi:10.1146/annurev.psych.52.1.1 — qui fonde la notion d'agentivité, non le formalisme BDI lui-même (dû à Rao & Georgeff).

## Voir aussi
- [Architectures réactive / délibérative / cognitive](archi-reactif-deliberatif-cognitif.md)
- [Taxonomie des 5 types d'agents](taxonomie-5-types-agents.md)
