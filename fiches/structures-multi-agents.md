---
titre: "Structures multi-agents : hiérarchique / holonique / coalition / équipe"
theme: multi-agents
niveau: 🟡
source_url: https://www.ibm.com/fr-fr/think/topics/multiagent-system
source_titre: "Qu’est-ce qu’un système multi-agent ?"
---

# Structures multi-agents : hiérarchique / holonique / coalition / équipe

**En une phrase** — quatre façons d'organiser les agents : arbre de commandement, tout-et-partie, alliance temporaire, ou équipe interdépendante.

## En détail
Quatre structures d'organisation des agents se distinguent. **Hiérarchique** : structure arborescente avec différents niveaux d'autonomie ; en hiérarchie simple un seul agent décide, en hiérarchie uniforme la responsabilité est répartie. **Holonique** : les agents sont regroupés en holarchies ; un holon est une entité qui ne peut fonctionner sans ses composants (comme le corps humain et ses organes) ; l'agent principal peut avoir plusieurs sous-agents tout en apparaissant comme une entité singulière, et ces sous-agents peuvent jouer des rôles dans d'autres holons — ces structures sont auto-organisées. **Coalition** : utile quand des agents individuels ne sont pas performants seuls ; ils s'unissent temporairement pour améliorer l'utilité, puis la coalition est dissoute une fois la performance atteinte (difficile à maintenir en environnement dynamique). **Équipe** : structure proche de la coalition mais les agents ne travaillent pas indépendamment, dépendent beaucoup plus les uns des autres et la structure est plus hiérarchique.

## Tradeoff / insight pour un senior
Hiérarchique et équipe sont intuitifs. Les deux à connaître sont : **holonique** (un agent est simultanément un tout et une partie, et un sous-agent peut être partagé entre plusieurs holons — utile pour mutualiser des capacités sans dupliquer), et **coalition** (regroupement opportuniste, autonome et éphémère, dissous dès l'objectif atteint — élasticité dynamique au prix d'un coût de (re)formation). L'axe distinctif coalition vs équipe : indépendance et durée de vie de l'alliance.

## Source primaire
La notion de holon vient d'Arthur Koestler (*The Ghost in the Machine*, 1967) et son application multi-agents de la littérature MAS.

## Voir aussi
- [Comportements d'essaim (flocking / swarming)](flocking-swarming.md)
- [Architectures verticale / horizontale / hybride](archi-vertical-horizontal-hybride.md)
