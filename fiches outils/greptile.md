---
outil: "Greptile"
titre: "Greptile"
themes: [evaluation]
type: "Service web (app GitHub)"
url: https://www.greptile.com/
modele_economique: "Propriétaire (SaaS) — Freemium / Abonnement par seat + usage"
cout_llm: "Inclus (l'éditeur fournit le LLM dans le prix)"
---

# Greptile

**En une phrase** — Reviewer de code IA pour PR GitHub qui s'appuie sur une **compréhension de toute la codebase** : fort sur les problèmes d'architecture et de contexte, privilégie le recall.

## Type & intégration
Application connectée à GitHub (GitHub Enterprise en Enterprise) ; revue automatique des PR avec un graphe de la codebase pour repérer les impacts cross-fichiers qu'une revue locale rate. Dans le benchmark cité par Addy Osmani : ~82 % de bugs attrapés, en échangeant de la précision contre du recall.

## Modèle économique
Propriétaire, freemium (constaté le 2026-06-17) :
- **Pro** : 30 $/seat/mois — 50 revues incluses, puis 1 $/revue supplémentaire.
- **Enterprise** : sur devis — support dédié, **self-hosting** (exclusif à ce plan).
- Essai 14 j ; **gratuit** pour les projets open-source qualifiés ; **-50 %** pour les startups pre-Series A (<2 M$ de revenus).

## Coût LLM
**Inclus (📦)** : le LLM est fourni par Greptile dans le prix (par seat + à la revue) — pas de BYOK, pas de tokens facturés séparément.

## À quoi ça sert
Détecter les bugs qui dépendent du **contexte global** du projet (architecture, conventions, effets de bord cross-modules), là où les reviewers « locaux » sont aveugles. Bon complément d'un outil orienté précision.

## Notes / à creuser
- Recall > précision = plus de faux positifs à filtrer ; l'humain garde le merge.
- Self-host réservé à l'Enterprise ; à connaître si la donnée ne peut pas sortir.

## Source
https://www.greptile.com/pricing *(vérifié le 2026-06-17)*
