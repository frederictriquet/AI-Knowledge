---
outil: "LiteLLM"
titre: "LiteLLM"
themes: [efficacite-cout, gouvernance-alignement-ops]
type: "Bibliothèque Python (SDK) + Proxy/Gateway self-host (open-source) + Enterprise"
url: https://www.litellm.ai/
modele_economique: "Open-source (MIT) + Enterprise payant (self-managed)"
cout_llm: "BYOK — pass-through, ne facture pas les tokens"
objectifs: [couts, mise-en-prod]
famille: "Passerelles / routeurs LLM"
eco_icones: "🔓🎁"
cout_icones: "🔑"
resume: "Cœur **open-source MIT** (BerriAI) : SDK (dans le code) **ou** proxy/gateway self-host (clés virtuelles, budgets, multi-tenant). API unifiée vers 100+ LLM, routing/fallback. **Pass-through pur** : ne facture pas les tokens (BYOK). Enterprise payant (SSO/RBAC/audit, self-managed, prix non publiés)"
---

# LiteLLM

**En une phrase** — Appeler 100+ fournisseurs de LLM via une **API unifiée au format OpenAI**, en SDK Python (intégré au code) ou en proxy self-host (gateway centralisé), avec routing, fallbacks et suivi des dépenses. Éditeur : BerriAI.

## Type & intégration
Deux objets distincts, utilisables séparément :
- **SDK Python (bibliothèque)** : à importer dans une appli — retry/fallback, load-balancing applicatif, callbacks d'observabilité.
- **Proxy Server / « AI Gateway » (self-host)** : gateway centralisé partagé entre équipes (auth, **clés virtuelles**, budgets, rate limits RPM/TPM, dashboard, suivi multi-tenant), déployable en Docker.

Pas d'offre cloud hébergée grand public : on l'héberge soi-même.

## Modèle économique
- **Cœur open-source — licence MIT** (SDK *et* proxy de base) : gratuit, modifiable, usage commercial libre.
- **LiteLLM Enterprise** (payant, **self-managed**) : SSO/SAML/SCIM, RBAC granulaire, guardrails, secret-manager, key rotation, métriques Prometheus, audit logs, support SLA 24/7. Essai via clé 30 jours.
- **Prix Enterprise non publiés** à la source (« contact sales »). Des estimations tierces circulent (~250 $/mois à ~2 500 $/mois) mais proviennent d'un blog concurrent — **non vérifiées**, à ne pas citer comme officielles.

## Coût LLM
**🔑 BYOK pur** : tu branches tes propres clés fournisseur ; LiteLLM **ne facture pas les tokens** — il proxifie tes appels et la consommation est facturée directement par chaque fournisseur sur tes clés. LiteLLM **mesure et attribue** les coûts (par clé/user/team/org) sans s'intercaler dans la facturation. (Différence nette avec [OpenRouter](openrouter.md), qui revend des crédits.)

## À quoi ça sert
Standardiser tous ses appels LLM derrière une interface OpenAI unique, avec routing/fallback et — via le proxy — gouvernance d'accès (clés virtuelles, budgets) pour plusieurs équipes. Brique d'infra que d'autres outils d'observabilité (Langfuse, Arize Phoenix, OpenTelemetry) viennent instrumenter.

## Notes / à creuser
- **SDK vs Proxy** : le SDK gère une appli ; le proxy est un gateway mutualisé. On choisit selon l'échelle.
- Les fonctions Enterprise (SSO, RBAC fin, guardrails, audit) sont sous **licence commerciale**, pas MIT.
- Self-host obligatoire → coûts/opérations d'hébergement à ta charge.
- Alternatives : [OpenRouter](openrouter.md) (gateway hébergé, revend les tokens), [Portkey](portkey.md) (open-core + cloud), Cloudflare AI Gateway.

## Source
https://www.litellm.ai/ · https://www.litellm.ai/enterprise · https://github.com/BerriAI/litellm · LICENSE = **MIT** (Copyright (c) 2023 Berri AI). *(vérifié le 2026-06-16 ; tarifs Enterprise non publiés à la source)*
