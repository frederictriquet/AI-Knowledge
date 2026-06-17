---
outil: "Mastra"
type: "Framework d'agents TypeScript/JS + Mastra Cloud (déploiement)"
url: https://mastra.ai/
modele_economique: "Open-source (Apache 2.0, cœur ; ee/ sous licence Enterprise) + Mastra Cloud (freemium)"
cout_llm: "🔑 BYOK, model-agnostic (via Vercel AI SDK) — ne facture pas les tokens"
---

# Mastra

**En une phrase** — Framework d'agents **TypeScript-natif** (par l'équipe derrière Gatsby) : agents, workflows, RAG, mémoire, evals et observabilité — pensé pour combler le vide d'un écosystème agentique jusque-là dominé par Python.

## Type & intégration
Framework open-source **TypeScript/JS** (pas un portage Python), bâti pour l'écosystème JS et s'appuyant sur le **Vercel AI SDK**. Primitives : agents, **workflows**, RAG, mémoire persistante, tools (schémas **Zod**), evals/scorers, guardrails, tracing (tokens/latence/coûts). Déployable sur tout runtime Node.js (deployers Vercel/Netlify/Cloudflare) ou via **Mastra Cloud** (public beta). 1.0 stable le 21 janv. 2026, ~25k★.

## Modèle économique
- **Cœur : open-source Apache 2.0.** Le répertoire `ee/` (Enterprise Edition) est **source-available sous « Mastra Enterprise License »** (dual-license).
- **Mastra Cloud** (déploiement/monitoring, public beta) : **Starter** 0 $/mois (100k events obs., 24 CPU-h, 15 j) → **Teams** 250 $/mois (1M events, SSO, SOC 2) → **Enterprise** sur devis (RBAC, audit, SLA).

## Coût LLM
**🔑 BYOK, model-agnostic** via le **model routing** (40+ fournisseurs : OpenAI, Anthropic, Gemini…). Le framework open-source **ne facture pas de tokens**. Seule exception **optionnelle** : le « Memory Gateway » de Mastra Cloud, facturé **Market Rate + 5,5 %** si on passe par lui.

## À quoi ça sert
Le choix quand on bâtit un produit IA **en TypeScript** (front et back JS) et qu'on ne veut pas basculer sur Python. Stack complète (agents → workflows → RAG → mémoire → evals → obs) idiomatique JS.

## Notes / à creuser
- **Jeune mais forte traction** : lancé oct. 2024, 1.0 en janv. 2026, 300k+ downloads npm/semaine, YC W25, seed 13 M$ (oct. 2025, YC + Gradient Ventures, avec G. Rauch / A. Masad / S. Banon parmi les angels). Compteurs et statut « beta » évoluent vite.
- Positionnement : alternative TS-first à **LangGraph.js** et à l'écosystème Python ([CrewAI](crewai.md), [LangGraph](langgraph.md), [Pydantic AI](pydantic-ai.md)).
- Logos clients (Replit, PayPal, SoftBank…) = communication Mastra, non audités.

## Source
https://mastra.ai/ · https://mastra.ai/pricing · https://mastra.ai/blog/apache-license · github.com/mastra-ai/mastra (LICENSE.md Apache 2.0 + ee/LICENSE) · https://mastra.ai/blog/seed-round. *(vérifié le 2026-06-16 ; statut beta/compteurs volatils)*
