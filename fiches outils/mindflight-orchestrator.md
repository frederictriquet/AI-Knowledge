---
outil: "MindFlight Orchestrator (MFO)"
titre: "MindFlight Orchestrator (MFO)"
type: "Plateforme (orchestration d'agents IA / automatisation d'entreprise)"
url: https://www.mindflight.be/
modele_economique: "Propriétaire, B2B — pas de tarif public (vente sur devis / diagnostic CEO)"
cout_llm: "❓ Non vérifié — l'éditeur évoque l'intégration de tes propres fournisseurs (OpenAI/Anthropic/… ou local), ce qui suggère du BYOK, mais le mécanisme de facturation LLM n'est pas documenté publiquement"
---

# MindFlight Orchestrator (MFO)

**En une phrase** — plateforme d'orchestration d'agents IA pour l'entreprise, présentée comme un « AI Operating System » : une couche transparente qui connecte les silos (CRM, ERP, email, Slack…), structure les flux de données et coordonne des agents IA à travers les départements.

> Contexte : produit de l'éditeur belge MindFlight (mindflight.be). Positionnement B2B/entreprise, pas un outil de codage — d'où sa famille dédiée (orchestration & automatisation).

## Type & intégration
**Plateforme** (pas une simple app), architecture en trois parties :
- **MFO Client** — intelligence locale : capte les événements là où ils surviennent (emails, mises à jour CRM, interactions client) et déclenche les workflows.
- **MFO Server** — le moteur : APIs, mémoire, outils IA ; sécurisé, stateless, extensible.
- **MFO Providers** — modules spécialisés : chaque système de l'entreprise (CRM, ERP, documents, modèles IA) devient un module augmenté.

Les agents y sont des **workflows dynamiques** (en équipe) ou des **task flows** (solo) : au lieu de suivre une séquence figée, l'agent s'adapte dans un cadre. Ils comprennent le langage naturel, décident sous incertitude, mémorisent le contexte et collaborent entre eux.

## Modèle économique
**Propriétaire, vente B2B.** Aucun tarif public : le parcours pousse vers un « Book My 25-Minute CEO Diagnostic » et un ebook gratuit → modèle **contact commercial / devis** typique des plateformes entreprise. Mises en avant : gouvernance (sécurité, conformité, auditabilité), scalabilité modulaire, ROI mesurable (dashboard par agent : heures économisées, revenus générés).

## Coût LLM
**❓ Non vérifié.** Le discours marketing de MindFlight indique que l'IA s'intègre via **n'importe quel fournisseur** (OpenAI, Anthropic, Grok, Groq, Mistral, DeepSeek…) ou des **modèles locaux**, combinables dans un même workflow — ce qui **suggère** un modèle **BYOK** (tu branches tes propres providers). **Mais** : pas de page tarifs (/pricing en 404), et le mécanisme exact de facturation LLM (tes clés vs inclus dans l'abonnement entreprise) **n'est documenté nulle part**. Je ne l'affirme donc pas. La plateforme elle-même est sur devis (B2B). → à confirmer auprès de l'éditeur.

## À quoi ça sert
Industrialiser l'IA dans une entreprise au-delà des pilotes isolés : chatbots clients/employés, équipes d'assistants en coulisses, agents métier (assistant CEO produisant des briefs avant réunion, agent data qui nettoie/enrichit/route les données client, agent support reliant emails et base de connaissances). Cible : directions d'entreprise cherchant à connecter leurs systèmes et automatiser des processus.

## Notes / à creuser
- Seul outil **non orienté codage** du recensement à ce stade : famille « orchestration / automatisation d'entreprise », distincte des outils dev.
- Concurrents/voisins conceptuels : n8n (+ IA), Make, Zapier AI, watsonx Orchestrate (IBM), Microsoft Copilot Studio.
- À creuser : tarification réelle, déploiement (cloud/on-prem), portée de l'auto-hébergement.

## Source
- Site officiel : https://www.mindflight.be/ (et /how-it-works/, /core-components/, docs) — fetch automatisé bloqué (403), contenu récupéré via curl le 2026-06-15

*(vérifié le 2026-06-15 — pages officielles via curl + recherche web ; tarification non publique)*
