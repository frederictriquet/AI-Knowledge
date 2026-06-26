---
outil: "Sentry Seer"
titre: "Sentry Seer"
themes: [evaluation, gouvernance-alignement-ops]
type: "Service web (add-on de Sentry)"
url: https://docs.sentry.io/product/ai-in-sentry/seer/
modele_economique: "Propriétaire (SaaS) — add-on Sentry, facturé par contributeur actif"
cout_llm: "Inclus (l'éditeur fournit le LLM dans le prix)"
---

# Sentry Seer

**En une phrase** — Agent IA de debugging de Sentry qui exploite erreurs, traces, logs et profils ; sa fonction *Code Review* analyse les PR pour prédire les défaillances **avant le merge**, avec pour force la sévérité des problèmes de production.

## Type & intégration
Add-on de la plateforme Sentry (donc adossé à ta télémétrie d'erreurs existante). Trois capacités : **Autofix** (analyse de cause racine + génération de PR, déclenchée à l'arrivée d'une issue), **Seer Agent** (debugging conversationnel sur toute la télémétrie), et **Code Review** (analyse de PR, prédiction d'erreurs et suggestions). Peut passer la main à des agents externes (ex. Claude Code). Dans la comparaison citée par Addy Osmani : le meilleur pour juger la **sévérité** d'une défaillance de prod.

## Modèle économique
Propriétaire, add-on à un abonnement Sentry. Facturation **par contributeur actif** : « toute personne créant 2 PR ou plus dans le mois dans un projet Seer-enabled est facturée » (constaté le 2026-06-17). Prix unitaires non détaillés publiquement dans la doc → à confirmer sur la page pricing Sentry.

## Coût LLM
**Inclus (📦)** : le modèle est fourni par Sentry dans le prix de l'add-on (LLM sous-jacent non divulgué) — pas de BYOK.

## À quoi ça sert
Relier **revue de PR** et **observabilité de production** : prioriser ce qui casse vraiment en prod, faire de l'analyse de cause racine et proposer des correctifs, en s'appuyant sur les données d'incidents Sentry. Pertinent si tu utilises déjà Sentry.

## Notes / à creuser
- Plus large qu'un simple reviewer de PR (Autofix + agent de debug) ; la *Code Review* n'est qu'une de ses facettes.
- Valeur conditionnée à l'usage de Sentry comme socle de télémétrie.
- ⚠️ Modèle LLM sous-jacent non divulgué (qualité et coût opaques) et valeur enfermée dans l'écosystème Sentry ; pour de la pure revue de PR, comparer à CodeRabbit / Cursor Bugbot / Greptile.

## Source
https://docs.sentry.io/product/ai-in-sentry/seer/ *(vérifié le 2026-06-17)*
