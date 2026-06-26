---
outil: "Langfuse"
titre: "Langfuse"
themes: [evaluation, gouvernance-alignement-ops]
type: "Service web (cloud) + self-host open-source"
url: https://langfuse.com/
modele_economique: "Open-source (cœur MIT) + Freemium / Abonnement (cloud)"
cout_llm: "Intégré (observabilité) + BYOK (éval LLM-as-judge)"
objectifs: [fiabilite, mise-en-prod]
famille: "LLMOps — évaluation & observabilité"
eco_icones: "🔓🎁🔁"
cout_icones: "🟢🔑"
resume: "Plateforme LLMOps open-source (cœur **MIT**, dossiers `ee` commerciaux) : tracing, évaluation, prompt management, datasets. Self-host gratuit ou cloud (Hobby gratuit 50k unités/mois → Core 29 $, Pro 199 $, Enterprise 2 499 $/mois). Obs sans coût LLM (🟢) ; éval LLM-as-judge en BYOK. Alternative OSS à LangSmith"
---

# Langfuse

**En une phrase** — Plateforme LLMOps open-source (tracing, évaluation, prompt management, datasets) pour déboguer, mesurer et monitorer une application LLM ; l'alternative open-source de référence à LangSmith.

## Type & intégration
Service web hébergé (Langfuse Cloud) **ou** auto-hébergeable gratuitement (Docker, k8s). On instrumente son appli via SDK (Python, JS/TS), des intégrations (LangChain, LlamaIndex, OpenAI SDK…) ou l'API/OpenTelemetry. Couvre les trois piliers : **tracing** (détail d'une exécution), **évaluation** (datasets, scores, LLM-as-judge), **observabilité** (coûts, latence, volumes) + gestion des prompts.

## Modèle économique
Open-source : le cœur du dépôt est sous **licence MIT**, **sauf les dossiers `ee`** (Enterprise Edition) qui relèvent d'une licence commerciale. Self-hosting **gratuit**. Cloud (constaté le 2026-06-15) :
- **Hobby** : gratuit, 50k unités/mois, 2 utilisateurs, 30 j de rétention.
- **Core** : 29 $/mois, 100k unités incluses puis 8 $/100k, 90 j, utilisateurs illimités.
- **Pro** : 199 $/mois, rétention 3 ans (option Teams +300 $/mois).
- **Enterprise** : 2 499 $/mois, rate limits custom, support dédié.
- Dégressif au volume : 8 → 6 $/100k unités selon les paliers.

## Coût LLM
- **Observabilité / tracing** : Langfuse **n'appelle pas de LLM** — il enregistre tes appels et leurs tokens/coûts → pas de coût LLM séparé (🟢).
- **Évaluation LLM-as-judge** : les évaluateurs peuvent invoquer un LLM ; c'est alors **ta** clé/modèle (BYOK 🔑) → tokens facturés par ton fournisseur LLM, pas par Langfuse.

## À quoi ça sert
Maîtriser une appli LLM en prod : déboguer une réponse via sa trace, suivre coûts/latence, tester la qualité sur des datasets, versionner les prompts. Choix naturel quand on veut de l'**open-source self-hostable** (données chez soi, pas de vendor lock-in).

## Notes / à creuser
- Distinguer le cœur MIT des features `ee` (SSO entreprise, etc.) sous licence commerciale.
- Concurrents directs : LangSmith (propriétaire, intégré LangChain), Braintrust (centré éval), Arize Phoenix (OTel).

## Source
https://langfuse.com/pricing · dépôt https://github.com/langfuse/langfuse (README : « This repository is MIT licensed, except for the `ee` folders »). *(vérifié le 2026-06-15)*
