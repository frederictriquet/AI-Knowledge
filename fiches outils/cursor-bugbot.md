---
outil: "Cursor BugBot"
type: "Service web (app GitHub)"
url: https://cursor.com/bugbot
modele_economique: "Propriétaire (Anysphere) — abonnement → bascule à l'usage"
cout_llm: "Inclus (modèles frontier + maison fournis dans le prix)"
---

# Cursor BugBot

**En une phrase** — Reviewer de PR IA d'Anysphere (Cursor) qui cible les **bugs de logique difficiles** avec un faible taux de faux positifs, et commente directement dans GitHub.

## Type & intégration
Application connectée à GitHub : revue automatique des PR, commentaires sur les problèmes potentiels et suggestions de correctif. Rattaché à l'écosystème Cursor (compte Cursor requis). Utilise « une combinaison de modèles frontier et de modèles maison ». Privilégie la **précision** (peu de faux positifs) plutôt que le volume de findings.

## Modèle économique
Propriétaire (Anysphere), en transition tarifaire (constaté le 2026-06-17) :
- **Historique** : 40 $/utilisateur/mois (32 $ en annuel), 200 PR/mois, revues illimitées.
- **Nouveau modèle** : **facturation à l'usage** (Teams et Individus, dès le renouvellement après le 8 juin 2026) — suppression des frais de siège ; un run coûte en moyenne ~1,00–1,50 $ selon la taille/complexité de la PR. Facturé par auteur de PR revue (contributeurs externes inclus).
- Essai 14 j.

## Coût LLM
**Inclus (📦)** : les modèles (frontier + maison) sont fournis par Cursor dans le prix — pas de BYOK, pas de tokens facturés à part. Le prix « à l'usage » reste une facturation produit (par run), pas une revente de tokens bruts.

## À quoi ça sert
Une passe de revue IA orientée **précision** sur GitHub : faire remonter les bugs de logique réels avec peu de bruit, en complément d'un outil plus orienté recall (architecture/contexte).

## Notes / à creuser
- Pricing en mouvement : vérifier le modèle en vigueur au moment de l'adoption (siège vs usage).
- Faible recouvrement avec les autres reviewers → bon candidat pour une stratégie multi-outils.

## Source
https://cursor.com/bugbot · https://cursor.com/blog/may-2026-bugbot-changes *(vérifié le 2026-06-17)*
