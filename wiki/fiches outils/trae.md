---
outil: "Trae"
titre: "Trae"
themes: [frameworks-outillage]
type: "Application (IDE)"
url: https://www.trae.ai/
modele_economique: "Freemium + abonnements (Lite/Pro/Ultra)"
cout_llm: "Inclus dans l'abonnement (quotas / pool de tokens)"
objectifs: [generer-code]
famille: "Agents & IDE qui codent"
eco_icones: "🎁🔁"
cout_icones: "📦💸"
resume: "IDE IA de ByteDance basé sur VS Code ; modèles premium (Claude, GPT, DeepSeek) fournis via un système de **crédits** (tokens × tarif modèle, plafond par palier), abonnements Lite/Pro/Pro+/Ultra 3–100 $/mois"
---

# Trae

**En une phrase** — IDE IA autonome de ByteDance, basé sur VS Code, où les modèles premium (Claude, GPT, DeepSeek) sont fournis et facturés dans l'abonnement, sans clé API à apporter.

## Type & intégration
**Application IDE autonome** (et non une simple extension) : un fork de VS Code, disponible sur macOS et Windows, plus un Cloud IDE dans le navigateur. Lancé par ByteDance en janvier 2025. Deux modes phares : **Builder** (décrire un projet en langage naturel → génération du code) et **Chat** (questions, debug, optimisation). Existe en version internationale et version chinoise.

## Modèle économique
**Freemium + abonnements** :
- **Free** : 0 $ — autocomplétions + accès à des modèles premium (quotas / file d'attente).
- **Lite** : ~3 $/mois (≈ 5 $ de « Basic Usage »).
- **Pro** : ~10 $/mois (≈ 20 $ de crédits).
- **Pro+** : ~30 $/mois (≈ 90 $ de crédits).
- **Ultra** : ~100 $/mois (≈ 400 $ de crédits).

Le coût et les quotas exacts évoluent ; vérifier la page tarifs à jour.

## Coût LLM
**Inclus + revendu à l'usage** 📦💸 — pas de clé API à fournir : ByteDance **fournit les modèles** (Claude, GPT, DeepSeek…). Mais la facturation est en réalité un **système de crédits** : chaque palier donne une allocation mensuelle « Basic Usage » (en $), et la consommation = **tokens × tarif API du modèle**, débitée de cette allocation (puis « Bonus Usage » subventionné). Donc *inclus jusqu'au plafond de crédits*, avec une logique de **revente à l'usage** par l'éditeur. Coût plafonné par le plan tant qu'on reste dans l'allocation ; choix de modèles/limites dictés par l'éditeur. (Reste sans clé à gérer, contrairement au BYOK de [Kilo Code](kilo-code.md).)

Ordre de grandeur : de 0 $ (free, avec quotas serrés) à 100 $/mois (Ultra). Très bon rapport qualité/prix annoncé pour l'accès à des modèles haut de gamme.

## À quoi ça sert
Développer dans un IDE complet piloté par l'IA : génération de projet de bout en bout (Builder), assistance au code, debug, refactor. Cible les développeurs qui veulent un IDE « clé en main » avec modèles inclus, sans gérer de clés ni de coûts à l'usage.

## Notes / à creuser
- ⚠️ **Confidentialité** : produit ByteDance — la politique indique que des extraits de code et données d'interaction *peuvent* servir à l'entraînement/l'amélioration, avec transferts de données entre serveurs dans le monde. Point d'attention fort en contexte pro/sensible.
- Basé sur VS Code → écosystème d'extensions familier.
- Concurrents : Cursor, Windsurf, Trae se distingue par des prix agressifs et les modèles inclus.

## Source
- Site officiel : https://www.trae.ai/
- Revues 2026 (pricing, Builder Mode) : aibase, vibecoding.app, ohaiknow

*(vérifié le 2026-06-15 — site officiel + recherche web ; tarifs à reconfirmer car évolutifs)*
