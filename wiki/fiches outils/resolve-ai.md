---
outil: "Resolve.ai"
titre: "Resolve.ai"
themes: [gouvernance-alignement-ops]
type: "Plateforme SaaS — AI SRE / ingénierie de production"
url: https://resolve.ai/
modele_economique: "Propriétaire SaaS, enterprise — pas de prix public (contact direct)"
cout_llm: "Inclus (📦) — l'éditeur fournit le LLM dans son service (enterprise) ; pas de BYOK affiché"
objectifs: [generer-code, mise-en-prod]
famille: "CI/CD, livraison & opérations assistés par IA"
eco_icones: "🔒"
cout_icones: "📦"
resume: "Agents IA d'astreinte/incident/prod (objectif ~80 % d'auto-résolution, garde-fous) ; sécurité entreprise (SSO/RBAC, pas d'entraînement sur tes données). Clients Coinbase/DoorDash… Enterprise / sur devis"
---

# Resolve.ai

**En une phrase** — plateforme d'**agents IA de production / on-call** : des agents prennent en charge l'astreinte, les incidents et le travail de prod quotidien, l'ingénieur dirigeant et validant les actions.

## Type & intégration
**SaaS propriétaire, orienté entreprise.** Des équipes d'agents enquêtent **avec** tes ingénieurs (triage, RCA de problèmes complexes). Sécurité entreprise : SAML SSO, RBAC, redaction/chiffrement, isolation par org, logs d'activité, **pas d'entraînement** de modèle sur tes données. Clients cités : Coinbase, DoorDash, Expedia, Snowflake, MongoDB. Valorisée ~1 Md$ (déc. 2025), pedigree fondateur Splunk.

## Modèle économique
**Propriétaire, enterprise** — pas de prix public, **sur devis**. *(constaté 2026-06-18)*

## Coût LLM
**Inclus (📦)** — l'inférence est **fournie par Resolve.ai** dans le cadre du contrat enterprise ; pas de BYOK ni de facturation token affichés côté client.

## À quoi ça sert
Automatiser fortement l'astreinte et la réponse à incident (objectif annoncé : jusqu'à ~80 % d'auto-résolution, avec garde-fous). L'humain « step in » pour diriger/agir. Cible : grandes organisations à forte charge d'incidents.

## Notes / à creuser
- **Famille [CI/CD, livraison & ops](../guides/generer-du-code-avec-l-ia.md#fam-ci-cd-livraison-operations-assistes-par-ia)**, sous-espace **AI SRE** ; la plus **agressive en autonomie** du trio ([Cleric](cleric.md) = prudent/read-only, [Traversal](traversal.md) = précision/ML). 
- ⚠️ **Exploitation de prod** (frontière entre *produire du code* et *embarquer l'IA dans un produit*). Degré réel d'auto-résolution et garde-fous à valider.

## Source
- Site : https://resolve.ai/

*(vérifié le 2026-06-18 — site officiel + recherche web)*
