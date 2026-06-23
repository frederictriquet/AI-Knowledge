---
outil: "Braintrust"
titre: "Braintrust"
type: "Service web (SaaS) + SDK"
url: https://www.braintrust.dev/
modele_economique: "Propriétaire — Freemium / Abonnement + usage"
cout_llm: "Intégré (logs) + BYOK / Revendu à l'usage (éval & playground)"
---

# Braintrust

**En une phrase** — Plateforme LLMOps propriétaire **centrée sur l'évaluation et l'expérimentation** (datasets, scoring, playground, comparaison de versions de prompts/modèles), avec logs et observabilité en complément.

## Type & intégration
SaaS + SDK (Python, TS). Cœur du produit : créer des **datasets** d'éval, lancer des **expériences** scorées (y compris **LLM-as-judge** via la lib `autoevals`), comparer les résultats dans un playground, puis brancher logs et observabilité de prod. On-prem / hybride disponibles en Enterprise pour données sensibles.

## Modèle économique
Propriétaire, freemium (constaté le 2026-06-15) :
- **Starter** : gratuit — 10 $ de crédits, 1 Go de données traitées (+4 $/Go), 10k scores (+2,50 $/1k), rétention 14 j, utilisateurs/projets/datasets illimités.
- **Pro** : 249 $/mois.
- **Enterprise** : sur devis, déploiement on-prem ou hébergé.
- Facturation à trois dimensions : **données traitées** (Go), **scores**, et **tokens/crédits**.

## Coût LLM
- **Logs / observabilité** : enregistre tes appels → pas de coût LLM propre (🟢).
- **Évaluation & playground** : Braintrust peut **exécuter des appels LLM** (proxy) pour scorer/comparer → consomme des tokens. Soit via **tes clés** (BYOK 🔑), soit via leurs crédits facturés à l'usage (💸) : tarifs proxy constatés ~0,06 $/Mtok en entrée, ~0,40 $/Mtok en sortie.

## À quoi ça sert
Quand le besoin n°1 est **l'évaluation rigoureuse** : mesurer si un changement de prompt/modèle améliore ou dégrade la qualité, industrialiser les évals en CI, comparer des approches côte à côte.

## Notes / à creuser
- Positionnement « éval-first » vs LangSmith/Langfuse plus « tracing-first » (tous se recouvrent).
- Le SDK `autoevals` (évaluateurs prêts à l'emploi) est publié sur GitHub — vérifier sa licence si réutilisé hors plateforme.

## Source
https://www.braintrust.dev/pricing · https://www.braintrust.dev/docs *(vérifié le 2026-06-15)*
