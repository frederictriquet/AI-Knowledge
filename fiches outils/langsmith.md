---
outil: "LangSmith"
type: "Service web (SaaS) + SDK"
url: https://www.langchain.com/langsmith
modele_economique: "Propriétaire — Freemium / Abonnement par seat + usage"
cout_llm: "Intégré (observabilité) + BYOK (éval LLM-as-judge)"
---

# LangSmith

**En une phrase** — Plateforme LLMOps propriétaire de LangChain (tracing, évaluation, monitoring d'applis LLM/agents), très intégrée à LangChain/LangGraph mais utilisable sans aucun framework.

## Type & intégration
SaaS hébergé + SDK clients (Python, TS) pour instrumenter l'appli. Le **self-hosting** (Cloud / Hybrid / VPC) n'est disponible **que sur le plan Enterprise** ; Developer et Plus sont cloud uniquement (données hébergées chez LangChain, point d'attention RGPD). À ne pas confondre avec le **framework `langchain`** (lui, open-source MIT) : LangSmith, la plateforme, est propriétaire.

## Modèle économique
Propriétaire, freemium (constaté le 2026-06-15) :
- **Developer** : gratuit, 1 seat, jusqu'à 5k traces de base/mois puis à l'usage.
- **Plus** : 39 $/seat/mois, 10k traces/mois puis à l'usage ; seats illimités à 39 $ pièce.
- **Enterprise** : sur devis — seul à offrir self-host/hybrid/VPC, SSO, SLA.
- Usage au-delà des quotas : ~2,50 $/1k traces de base, runs de déploiement ~0,005 $ pièce.

## Coût LLM
- **Tracing / observabilité** : LangSmith enregistre les appels, **n'appelle pas de LLM** → pas de coût LLM séparé (🟢). Il facture l'ingestion/stockage des traces, pas les tokens.
- **Évaluation LLM-as-judge** : l'évaluateur utilise **ta** clé/modèle (BYOK 🔑) → tokens facturés par ton fournisseur.

## À quoi ça sert
Le choix « par défaut », à friction minimale, quand on travaille déjà avec **LangChain / LangGraph** : déboguer des chaînes/agents, monitorer coûts et latence en prod, rejouer des évals avant de merger.

## Notes / à creuser
- Facturation **à la trace** : peut grimper vite à fort volume en production (surveiller la rétention base vs extended).
- Self-host réservé à l'Enterprise : bloquant si la donnée ne peut pas sortir.
- Alternatives open-source self-hostables : **Langfuse**, **Arize Phoenix**.

## Source
https://www.langchain.com/pricing-langsmith · https://docs.smith.langchain.com *(vérifié le 2026-06-15)*
