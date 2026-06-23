---
outil: "Arize Phoenix / Arize AX"
titre: "Arize Phoenix / Arize AX"
type: "Bibliothèque/app open-source (Phoenix) + Service web SaaS (Arize AX)"
url: https://phoenix.arize.com/
modele_economique: "Open-source (Phoenix, Elastic License 2.0) + Freemium / Abonnement + usage (Arize AX)"
cout_llm: "Intégré (tracing) + BYOK (éval LLM-as-judge)"
---

# Arize Phoenix / Arize AX

**En une phrase** — Deux produits liés d'Arize AI : **Phoenix**, plateforme open-source d'observabilité/évaluation LLM bâtie sur **OpenTelemetry/OpenInference** (framework-agnostique, self-host gratuit) ; et **Arize AX**, le SaaS de monitoring ML/LLM en production à l'échelle.

## Type & intégration
- **Phoenix** : bibliothèque + app (Python en tête), exécutable en local/notebook ou self-hosted. S'appuie sur **OpenTelemetry** et les conventions **OpenInference** → instrumentation standard, indépendante du framework (vs LangSmith centré LangChain). Tracing, évals, expérimentation, itération de prompts.
- **Arize AX** : plateforme cloud pour monitorer en prod (dérive, qualité, volumes), avec gouvernance, conformité et passage à l'échelle.

## Modèle économique
- **Phoenix** : open-source sous **Elastic License 2.0 (ELv2)** — gratuit, self-hostable. (ELv2 = source-available, restreint la revente en SaaS concurrent ; ce n'est pas une licence OSI classique.)
- **Arize AX** (constaté le 2026-06-15) : **Free** (25k trace spans/mois, 1 Go ingestion, rétention 15 j) → **Pro** 50 $/mois (50k spans, 10 Go, 30 j ; +0,0008 $/span, +3 $/Go) → **Enterprise** sur devis (self-host, SLA, SOC2/HIPAA, multi-région). Programme startup à tarif réduit.

## Coût LLM
- **Tracing / observabilité** : n'appelle pas de LLM → pas de coût séparé (🟢).
- **Évaluation** : la lib `arize-phoenix-evals` fait du **LLM-as-judge** avec **ta** clé/modèle (BYOK 🔑) → tokens facturés par ton fournisseur.

## À quoi ça sert
Quand on veut des **standards ouverts (OpenTelemetry)** et de l'éval/tracing **local et gratuit** (Phoenix), avec une montée en gamme possible vers le **monitoring en prod à l'échelle** (Arize AX). Phoenix est aussi un bon point d'entrée framework-agnostique.

## Notes / à creuser
- Attention à la licence **ELv2** de Phoenix (source-available ≠ open-source OSI) : OK pour usage interne/self-host, restrictions sur la revente managée.
- Les packages d'instrumentation OpenInference (Python/TS/Java) sont réutilisables avec d'autres backends OTel.

## Source
https://phoenix.arize.com/ · https://arize.com/pricing/ · dépôt https://github.com/Arize-ai/phoenix (README : « licensed under the terms of the Elastic License 2.0 (ELv2) »). *(vérifié le 2026-06-15)*
