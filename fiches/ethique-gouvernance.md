---
titre: "Éthique & gouvernance des agents"
type: "Concept"
theme: gouvernance-alignement-ops
niveau: 🔴
source_url: https://www.ibm.com/fr-fr/think/insights/ai-agent-ethics
source_titre: "De nouveaux risques éthiques liés aux agents d’IA ? Les chercheurs se penchent sur la question"
---

# Éthique & gouvernance des agents

**En une phrase** — aligner les agents sur des documents de politique en langage naturel et organiser une supervision où l'humain décide pendant que l'IA interroge, le tout encadré par des agents de gouvernance, des sandbox éthiques et un kill switch.

## En détail
Via Kush Varshney (IBM Research). **Alignment Studio** : « aligne les grands modèles de langage sur les règles et les valeurs décrites dans les documents de politique en langage naturel, tels que les réglementations gouvernementales ou les propres directives éthiques d'une entreprise », avec un cycle continu pour que les modèles « adoptent réellement les comportements souhaités » et pas seulement le vocabulaire. **Granite Guardian 3.1** « détecte les hallucinations d'appel de fonction par les agents avant que des conséquences imprévues ne se produisent ». **RADAR** (Université chinoise de Hong Kong + IBM Research) : détecteur de texte IA par apprentissage contradictoire entre deux modèles. La **collaboration contradictoire** inverse les rôles habituels : « l'humain prend la décision finale ; l'algorithme n'est pas conçu pour rivaliser dans ce rôle, mais pour interroger et […] affiner les recommandations de l'agent humain » — préservation de la dignité. Référence au scénario de l'optimiseur de trombone (Bostrom). **Gouvernance** : **bac à sable** éthique (environnements simulés, « tests de stress moral »), surveillance d'agent à agent, **agents de gouvernance** « conçus pour surveiller et évaluer d'autres agents » (détection de dérive de modèle), demande d'**approbation humaine** pour certaines actions, et **mécanisme d'arrêt d'urgence** (kill switch) pour désactivation immédiate en environnement à haut risque.

## Tradeoff / insight pour un senior
Le point non trivial est l'**inversion** de la collaboration contradictoire : l'IA n'assiste pas l'humain, elle le challenge — l'humain reste décideur, l'IA joue l'avocat du diable. Et l'idée d'**agents de gouvernance** (un agent qui audite d'autres agents) déplace le contrôle vers le runtime plutôt que le pré-déploiement.

## Source primaire
Alignment Studio, *IEEE Internet Computing*, septembre 2024 ; scénario du trombone, Nick Bostrom ; risque « autonomie », rapport DHS, avril 2024 ; mise en garde désinformation, Google DeepMind, avril 2024 ; collaboration contradictoire, article de recherche août 2024.

## Voir aussi
- [securite-agentique](securite-agentique.md)
- [guardrail-noeud-entree](guardrail-noeud-entree.md)
- [taxonomie-erreurs-appel-fonction](taxonomie-erreurs-appel-fonction.md)
