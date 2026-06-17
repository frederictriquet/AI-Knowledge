---
outil: "Sculptor"
type: "Application desktop Mac — orchestrateur d'agents"
url: https://imbue.com/sculptor/
modele_economique: "Propriétaire — gratuit en beta"
cout_llm: "Intégré (BYO Anthropic : clé API ou abonnement Claude Pro/Max)"
---

# Sculptor

**En une phrase** — « UI manquante pour les agents de codage » (Imbue) : app Mac qui lance **plusieurs agents Claude Code en parallèle dans des conteneurs Docker isolés**, avec preview instantané des changements.

## Type & intégration
App desktop macOS. Chaque agent tourne dans un **conteneur isolé** (il peut installer des paquets et exécuter du code sans risque pour ta machine). **Pairing Mode** : basculer instantanément vers l'environnement d'un agent pour tester ses changements en local. Support des **dev containers** (dépendances pré-installées dans l'image → démarrage d'agent en secondes au lieu de minutes). Tourne entièrement en local ; tu contrôles ce qui est renvoyé à Imbue.

## Modèle économique
Propriétaire, **gratuit pendant la beta**. Pas de pricing public à ce stade.

## Coût LLM
**🟢🔑 BYO Anthropic** : nécessite un accès Anthropic — soit ta **clé API** (🔑), soit ton abonnement **Claude Pro/Max** (🟢). Sculptor n'ajoute pas de coût LLM propre.

## À quoi ça sert
Faire tourner et comparer plusieurs agents de codage **en sécurité** (isolation conteneur), avec un aller-retour rapide pour tester leurs résultats. Se distingue par l'isolation Docker et le démarrage accéléré.

## Notes / à creuser
- Édité par **Imbue** (labo de recherche IA) ; beta → maturité et modèle éco à surveiller.
- macOS uniquement ; même famille que Conductor / Sculptor / Crystal (orchestrateurs desktop).

## Source
https://imbue.com/sculptor/ · https://imbue.com/blog/sculptor-announce · https://imbue.com/blog/containers. *(vérifié le 2026-06-17 ; gratuit en beta, pricing futur non publié)*
