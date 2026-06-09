---
titre: La « lethal trifecta »
theme: securite
tags: [securite, injection-prompt, agents, exfiltration]
niveau: 🔴
provenance: ➕
base: ibm-guide-agents-ia/hors-corpus
source_url: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
source_titre: "The lethal trifecta for AI agents — Simon Willison, 2025"
---

# La « lethal trifecta »

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. Glossaire · Pertinence 🔴 substance

**En une phrase** — l'injection de prompt devient une fuite de données réelle uniquement quand un agent réunit trois capacités simultanées ; en supprimer une seule neutralise toute la classe d'attaque.

## L'idée
Simon Willison formalise pourquoi certains assemblages d'agents sont catastrophiques. Le danger n'est pas l'injection de prompt seule, mais la conjonction de **trois ingrédients** : (1) accès à des données privées, (2) exposition à du contenu non fiable (mails, pages web, documents tiers), (3) capacité de communication sortante permettant l'exfiltration. Réunis, ils laissent un attaquant injecter une instruction via le contenu non fiable, lire les données privées, puis les renvoyer. Le cadre est diagnostique : on inspecte un agent et on coche les trois cases.

## Tradeoff / quand l'utiliser
Outil de revue d'architecture : casser la trifecta en retirant un sommet (couper l'exfiltration, isoler les données privées, ou ne traiter que du contenu fiable) est plus robuste que tenter de « filtrer » l'injection, qui reste non résolue à ce jour. Coût : on ampute des fonctionnalités utiles (un agent qui ne peut rien envoyer perd de sa valeur).

Deux mises en garde de Willison : (1) les **guardrails ne sauvent pas** — un produit qui bloque « 95 % des attaques » est un échec en sécurité applicative, car l'attaquant cible justement les 5 % restants ; (2) **MCP aggrave** le risque en encourageant à mélanger des outils de sources différentes, ce qui réunit les trois pattes sans qu'on s'en rende compte. Côté utilisateur, la seule parade sûre est d'éviter entièrement la combinaison : les fournisseurs ne vous sauveront pas.

## Source primaire
Simon Willison, 2025, *The lethal trifecta for AI agents* (billet de blog, simonwillison.net ; pas d'arXiv). Willison est la source primaire de référence sur la **prompt injection** : il a forgé le terme et la notion de lethal trifecta ; la fiche IBM correspondante en est une version dérivée et vulgarisée.

## Voir aussi
- [dual-llm-camel](dual-llm-camel.md) (hors-corpus sœur)
- [securite-agentique](securite-agentique.md) (corpus)
