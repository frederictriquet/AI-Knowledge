# Architecture blackboard

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. [Glossaire](../../GLOSSAIRE-PATTERNS.md) · Pertinence 🟡 tradeoff

**En une phrase** — des agents spécialisés collaborent via un **tableau noir partagé** (état commun) au lieu de s'envoyer des messages directs.

## L'idée
Le « blackboard » est une structure de données partagée où plusieurs sources de connaissances (agents experts) lisent l'état courant et y écrivent leurs contributions quand elles ont quelque chose à apporter. Aucun agent ne s'adresse directement à un autre : la coordination passe entièrement par l'état partagé, qu'un contrôleur supervise pour décider qui agit. Classique de l'IA distribuée, le modèle est réactualisé pour orchestrer des agents LLM autour d'un scratchpad commun.

## Tradeoff / quand l'utiliser
Utile pour des problèmes **incrémentaux et opportunistes** où l'ordre des contributions n'est pas connu à l'avance (diagnostic, fusion de données). Coût : le tableau partagé devient un point de contention et exige un contrôle d'accès et un arbitrage soignés. Pour des pipelines linéaires, l'orchestration séquentielle est plus simple.

## Source primaire
Hayes-Roth, 1985, *A Blackboard Architecture for Control* (Artificial Intelligence). Système fondateur : HEARSAY-II (reconnaissance de la parole, années 1970).

## Voir aussi
- [structures-multi-agents](../structures-multi-agents.md) (corpus)
- [strategies-collaboration](../strategies-collaboration.md) (corpus)
