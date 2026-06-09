# Stratégies de collaboration : règles / rôles / modèles

> Fiche du [glossaire des patterns](../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff · Provenance ✅ présent · Sources corpus : [27-multi-agent-collaboration](../md/27-multi-agent-collaboration.md)

**En une phrase** — trois manières de faire coopérer des agents : scripté, par répartition de rôles, ou par raisonnement probabiliste sous incertitude.

## Ce que dit le corpus
IBM décrit trois stratégies de collaboration entre agents. **Basée sur des règles** : les interactions sont strictement régies par un ensemble de règles précises (instructions conditionnelles, automates d'état, cadres logiques) ; capacité d'apprentissage limitée, politique fixe ; efficace et équitable pour les tâches très structurées, mais peu adaptable ni évolutive. **Basée sur les rôles** : chaque agent se voit attribuer un rôle, des permissions et des objectifs liés à une partie de l'objectif global ; les agents travaillent de façon semi-indépendante tout en partageant l'information (inspiré des dynamiques humaines : chef, observateur, exécuteur) ; permet une collaboration modulaire et experte, mais dépend de l'intégration fluide des agents. **Basée sur des modèles** : les agents construisent des modèles internes (souvent probabilistes ou appris) de leur état, de l'environnement et des autres agents ; ils planifient sous incertitude via mise à jour de croyances et inférence. Méthodes citées : raisonnement bayésien, processus de décision markoviens (MDP), modèles de machine learning. Grande flexibilité, mais complexité et coût computationnel élevés.

## Tradeoff / insight pour un senior
Gradient coût/adaptabilité : règles (déterministe, débogable, rigide) → rôles (modulaire, dépend du découpage) → modèles (gère l'incertitude via bayésien/MDP, mais cher). Choisir « modèles » seulement si l'environnement est réellement partiellement observable ou incertain ; sinon le scripté ou les rôles suffisent et restent prévisibles.

## Source primaire
Citée par IBM via la note 4 du fichier 27 (renvoi de la section). Méthodes nommées sans référence : raisonnement bayésien, MDP.

## Voir aussi
- [Réseaux centralisés vs décentralisés](reseaux-centralises-decentralises.md)
- [Structures multi-agents : hiérarchique / holonique / coalition / équipe](structures-multi-agents.md)
