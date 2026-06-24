---
outil: "Kilo Code"
titre: "Kilo Code"
themes: [frameworks-outillage]
type: "Extension IDE / CLI"
url: https://kilo.ai/
modele_economique: "Open-source + paiement à l'usage (gateway sans marge) + abonnements optionnels"
cout_llm: "BYOK ou Revendu à l'usage (prix coûtant, sans marge)"
---

# Kilo Code

**En une phrase** — agent de codage IA open-source (extension VS Code/JetBrains, CLI, Slack, cloud) qui donne accès à 500+ modèles, soit avec tes propres clés API, soit via un gateway qui facture les tokens au prix coûtant.

## Type & intégration
Plateforme d'« agentic engineering » open-source, principalement une **extension IDE** (VS Code, aussi dispo sur l'Open VSX Registry, et JetBrains), avec également une **CLI**, une intégration Slack et une offre cloud. Licences : Apache 2.0 pour les extensions, MIT pour la CLI → auditable et auto-hébergeable. Issu de la lignée des agents type Roo Code / Cline.

## Modèle économique
- **Logiciel gratuit et open-source** : l'extension/CLI ne coûte rien à installer et utiliser.
- **Monétisation via le Kilo Gateway** (paiement à l'usage) et des forfaits **Kilo Pass** optionnels pour lisser la dépense mensuelle :
  - Starter ~19 $/mois, Pro ~49 $/mois, Expert ~199 $/mois (crédits bonifiés vs le prix, bonus annuel/fidélité).
  - Offres Team/Enterprise à partir de ~15 $/utilisateur/mois (facturation centralisée, SSO, audit logs).
- 20 $ de crédits offerts à l'inscription.

## Coût LLM
Le LLM n'est pas inclus — deux voies, au choix :
- **BYOK** 🔑 — tu branches tes clés Anthropic, OpenAI, Google, Azure, AWS Bedrock… ou des modèles **locaux** via Ollama / LM Studio (coût nul). Tu paies alors directement le fournisseur.
- **Revendu à l'usage** 💸 via le Kilo Gateway — **au prix coûtant, sans marge** (argument commercial central : les tarifs correspondent exactement à ceux des fournisseurs).

Ordre de grandeur : entièrement dépendant du modèle choisi. Gratuit avec des modèles locaux/gratuits ; pour les gros modèles (Claude Opus, GPT-5.5…) le coût suit le tarif token du fournisseur, potentiellement élevé sur de gros volumes — mais sans surcoût Kilo.

## À quoi ça sert
Coder en mode agent dans l'IDE : génération, refactor, autocomplétion, exécution de tâches multi-étapes, le tout en gardant le choix du modèle et la maîtrise des coûts (pas de markup, BYOK possible). Alternative open-source aux agents propriétaires, avec accès à un large catalogue de modèles.

## Notes / à creuser
- 500+ modèles annoncés (GPT-5.5, Claude Opus 4.7, Sonnet 4.6, Gemini 3.1 Pro…).
- Le « sans marge » est l'argument différenciant face aux concurrents qui prennent une commission sur les tokens.
- Auto-hébergeable / auditable grâce aux licences ouvertes — pertinent en contexte entreprise.
- Concurrents proches : Cline, Roo Code, Cursor, Continue.

## Source
- Site officiel : https://kilo.ai/ (`kilocode.ai` redirige vers ce domaine) — page tarifs https://kilo.ai/pricing
- Dépôt : https://github.com/Kilo-Org/kilocode

*(vérifié le 2026-06-15 — site officiel + page pricing + GitHub)*
