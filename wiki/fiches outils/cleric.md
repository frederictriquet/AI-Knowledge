---
outil: "Cleric"
titre: "Cleric"
themes: [gouvernance-alignement-ops]
type: "Plateforme SaaS — AI SRE (investigation d'incidents)"
url: https://cleric.ai/
modele_economique: "Propriétaire SaaS — pas de prix public (démo/enterprise) ; pas de tier gratuit affiché"
cout_llm: "Inclus (📦) — l'éditeur exécute le LLM dans son service ; pas de clé à fournir"
---

# Cleric

**En une phrase** — agent **AI SRE** qui enquête en continu sur les incidents de prod, produit la *root cause analysis* et recommande des correctifs, en se branchant sur ta stack d'observabilité.

## Type & intégration
**Plateforme SaaS propriétaire**. Se connecte à la stack (AWS, Azure, Datadog, Grafana, PagerDuty…) « en un après-midi ». **Read access par défaut, write quand tu es prêt** ; chaque action est loguée et auditable. Sert de « mémoire opérationnelle » de l'équipe. Gartner *Cool Vendor 2025* (AI for SRE & Observability).

## Modèle économique
**Propriétaire, SaaS.** Pas de prix public ni de tier gratuit affiché → **démo / enterprise** (sur devis). *(constaté 2026-06-18)*

## Coût LLM
**Inclus (📦)** — Cleric **exécute le LLM dans son service** ; tu n'apportes pas de clé. Le coût LLM est intégré au contrat (pas de facturation token visible côté client). Posture **read-only par défaut** = pas d'action destructrice sans ton accord.

## À quoi ça sert
Réduire le MTTR : corréler logs/métriques/traces pour diagnostiquer en minutes, garder une RCA auditable. Annoncé : ~5 min jusqu'à la cause racine, 92 % de findings « actionnables », 200 000+ investigations.

## Notes / à creuser
- **Famille [CI/CD, livraison & ops](../produire-du-code.md#fam-9)**, sous-espace **AI SRE / incident** avec [Resolve.ai](resolve-ai.md) et [Traversal](traversal.md). Cleric se positionne **prudent** (observation/recommandation par défaut), là où [Resolve.ai](resolve-ai.md) pousse l'auto-résolution.
- ⚠️ Outil d'**exploitation de prod** → déborde vers « exploiter un produit » (frontière entre *produire du code* et *embarquer l'IA dans un produit*).
- Prix réels et limites d'autonomie (write) à vérifier en démo.
- ⚠️ « 5 min jusqu'à la cause racine / 92 % de findings actionnables / 200 000+ investigations » et le label Gartner sont des chiffres **éditeur non vérifiés** ; pas de prix public ni de tier gratuit → évaluation possible seulement en démo enterprise.

## Source
- Site : https://cleric.ai/

*(vérifié le 2026-06-18 — site officiel + recherche web)*
