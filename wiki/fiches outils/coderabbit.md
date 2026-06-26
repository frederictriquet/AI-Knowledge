---
outil: "CodeRabbit"
titre: "CodeRabbit"
themes: [evaluation]
type: "Service web (app GitHub/GitLab) + IDE / CLI"
url: https://www.coderabbit.ai/
modele_economique: "Propriétaire (SaaS) — Freemium / Abonnement par seat"
cout_llm: "Inclus (l'éditeur fournit le LLM dans le prix)"
objectifs: [generer-code, fiabilite]
famille: "Revue de code par IA"
eco_icones: "🎁🔁💳"
cout_icones: "📦"
resume: "Reviewer IA de PR (GitHub/GitLab) : résumés, revue ligne à ligne, linters + SAST, fix en 1 clic. **Gratuit à vie pour repos publics** ; Pro 24 $, Pro Plus 48 $/user/mois, Enterprise (SSO, self-host). Meilleur **recall** au benchmark Martian (~49 % précision). LLM inclus"
---

# CodeRabbit

**En une phrase** — Reviewer de code IA qui s'installe sur tes PR GitHub/GitLab : résumés, revue ligne à ligne, intégration de linters et d'outils SAST, corrections en 1 clic ; aussi disponible en IDE et CLI.

## Type & intégration
Application à connecter au repo (GitHub/GitLab) qui commente automatiquement chaque PR ; agit aussi dans l'IDE et en CLI, plus un agent Slack. S'appuie sur des linters et des outils SAST en complément de l'analyse LLM. Dans le benchmark cité par Addy Osmani : ~49 % de précision, le **meilleur recall**, avec corrections en 1 clic.

## Modèle économique
Propriétaire, freemium (constaté le 2026-06-17) :
- **Free** : 0 $ — **gratuit à vie pour les repos publics**, essai Pro Plus 14 j, revues IDE/CLI.
- **Pro** : 24 $/utilisateur/mois (annuel) — revues PR complètes, linters, SAST, analytics.
- **Pro Plus** : 48 $/utilisateur/mois — checks pré-merge custom, finitions avancées.
- **Enterprise** : sur devis — SSO, RBAC, API, **self-hosting**, SLA.
- Add-on à l'usage (revues PR/CLI illimitées) ; agent Slack à 0,50 $/minute-agent.

## Coût LLM
**Inclus (📦)** : le LLM est fourni par CodeRabbit dans le prix de l'abonnement — pas de clé à apporter ni de tokens facturés à part. Coût prévisible (par seat / par usage), pas BYOK.

## À quoi ça sert
Automatiser la première passe de revue sur chaque PR : faire remonter bugs, smells et points de sécurité avant l'humain, et fluidifier les petites corrections. Gratuit pour l'open-source.

## Notes / à creuser
- Recall élevé = plus de findings à trier (bruit) ; à traiter comme capteur, pas comme verdict (cf. [revue de code agentique](../fiches/revue-de-code-agentique.md)).
- Combiner avec un reviewer de nature différente (faible recouvrement entre outils).

## Source
https://www.coderabbit.ai/pricing *(vérifié le 2026-06-17)*
