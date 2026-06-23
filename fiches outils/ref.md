---
outil: "Ref (ref.tools)"
titre: "Ref (ref.tools)"
type: "Serveur MCP (documentation technique à jour)"
url: https://ref.tools/
modele_economique: "Freemium / Abonnement (client MCP open-source)"
cout_llm: "Intégré (source de doc ; ne génère pas de LLM)"
---

# Ref (ref.tools)

**En une phrase** — Serveur MCP qui donne aux agents de codage un accès **token-efficient** à un index de **documentation technique à jour** (libs/APIs publiques + repos/PDF privés), pour éviter les hallucinations d'API sans gaspiller le contexte.

## Type & intégration
Serveur MCP (`ref-tools-mcp`) exposant deux outils : `ref_search_documentation(query)` et `ref_read_url(url)`. Index pré-**chunké intelligemment** → l'agent reçoit *juste les tokens utiles* plutôt que des pages entières (réduction du « context rot »). Couvre les repos GitHub et sites de doc des principales plateformes/libs, plus tes sources privées.

## Modèle économique
Le **serveur MCP est open-source** (repo `ref-tools/ref-tools-mcp`) ; le service hébergé (l'index) est **freemium + abonnement** (constaté le 2026-06-17) :
- **Free** : 0 $, 200 crédits one-shot (sans expiration), 3 petits repos + 1 gros.
- **Basic** : 19 $/mois, 2 000 crédits, 10 petits repos.
- **Pro** : 50 $/mois, 6 000 crédits, 50 petits repos.
- **Max** : 200 $/mois, 30 000 crédits.
- **Enterprise** : sur devis (SSO, limites custom).

## Coût LLM
**🟢 Intégré** : Ref est une **source de connaissances** — il ne génère pas de complétion. Il tourne dans ton agent (coût LLM = celui de ton agent) et vise au contraire à **réduire** les tokens consommés en ne renvoyant que le contexte pertinent.

## À quoi ça sert
Empêcher l'agent de se tromper sur les APIs de librairies (versions, signatures) en lui servant la **bonne doc, à jour, de façon économe en tokens**. Même créneau que Context7.

## Notes / à creuser
- ⚠️ **Classement** : rangé ici comme aide à la production de code (doc externe pour l'agent). Voisins : Context7, GitMCP (mêmes « sources de connaissances MCP » pour coder).
- Le pricing en crédits dépend du volume de recherches/repos indexés.

## Source
https://ref.tools/ · https://docs.ref.tools/usage/pricing · https://github.com/ref-tools/ref-tools-mcp. *(vérifié le 2026-06-17)*
