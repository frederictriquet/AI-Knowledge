---
outil: "Mergify"
titre: "Mergify"
themes: [gouvernance-alignement-ops]
type: "Plateforme SaaS — merge queue & CI (détection de tests flaky)"
url: https://mergify.com/
modele_economique: "Propriétaire SaaS, freemium (gratuit pour l'open-source ; payant par contributeur — prix exacts à vérifier)"
cout_llm: "Inclus (📦) — cœur surtout déterministe ; l'IA éventuelle (détection/fix flaky) est bundlée, pas de clé/BYOK"
---

# Mergify

**En une phrase** — plateforme de **merge et CI** : merge queue (« keep main green »), CI Insights (observabilité + auto-retry), Test Insights (détecte, met en quarantaine et corrige les **tests flaky**), Merge Protections et Stacks.

## Type & intégration
**SaaS propriétaire**, branché sur tes CI existants (35+ intégrations) **sans réécrire les tests**. Composants : **Merge Queue** (évite de casser `main`), **CI Insights** (auto-retry des échecs transitoires), **Test Insights** (quarantaine/correction des flaky), **Merge Protections** (gouvernance), **Stacks** (découper de grosses PR). Échelle : 2k+ orgs, 25k+ users, 75k+ PR/mois.

## Modèle économique
**Propriétaire, freemium** : historiquement **gratuit pour l'open-source / repos publics**, offres payantes **par contributeur** au-delà. ⚠️ Prix exacts **non vérifiés** ici (page `/pricing` non détaillée). *(constaté 2026-06-18)*

## Coût LLM
**Inclus (📦)** — Mergify est **surtout une automatisation déterministe** (règles de merge queue, retry, quarantaine flaky) ; le volet « détection/fix de flaky » peut mobiliser de l'IA, **bundlée dans le service**. Tu n'apportes ni ne paies de LLM séparé. *(Donc « IA » au sens large, pas un agent LLM gourmand en tokens.)*

## À quoi ça sert
Fluidifier la **livraison** : garder `main` vert, éviter que les tests flaky ne bloquent les merges (moins de reruns → CI moins chère), gouverner les merges. Se situe entre **tester** et **déployer** dans le SDLC.

## Notes / à creuser
- **Famille [CI/CD, livraison & ops](../produire-du-code.md#fam-9)**, sous-espace **CI / merge / flaky** — vs les **AI SRE** [Cleric](cleric.md)/[Resolve.ai](resolve-ai.md)/[Traversal](traversal.md) (run/incident).
- Voisins plus « AI-natifs » côté CI (candidats, non vérifiés) : **Datadog Bits AI Dev Agent** (fix autonome de flaky → draft PR), **Aviator**, **Trunk** (flaky tests).
- À vérifier : grille de prix exacte, profondeur réelle de l'« IA » (vs automatisation par règles).
- ⚠️ Chiffres d'adoption (« 2k+ orgs, 25k+ users, 75k+ PR/mois ») = communication éditeur non vérifiée ; le cœur est **déterministe** (merge queue/CI), le volet « IA » reste marginal — n'en attends pas un agent.

## Source
- Site : https://mergify.com/ (et /pricing)

*(vérifié le 2026-06-18 — site officiel + curl ; prix exacts à confirmer)*
