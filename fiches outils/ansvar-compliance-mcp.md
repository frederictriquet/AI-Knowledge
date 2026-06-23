---
outil: "Ansvar Compliance MCP (suite)"
titre: "Ansvar Compliance MCP (suite)"
type: "Suite de serveurs MCP (sources de données réglementaires / juridiques)"
url: https://github.com/Ansvar-Systems
modele_economique: "Connecteurs open-source (Apache 2.0) self-host gratuit + Ansvar Gateway hébergée (Free 100 recherches/j/siège ; Premium 249 €/siège/mois ou 2490 €/an ; Team/Company sur devis). Éditeur : Ansvar Systems AB (Suède)"
cout_llm: "Aucun LLM — récupération de texte officiel verbatim ; BYO client (Claude, Cursor…)"
---

# Ansvar Compliance MCP (suite)

**En une phrase** — une famille de ~150 serveurs MCP open-source (par **Ansvar AI**, Stockholm) qui donnent aux agents IA un accès *structuré et verbatim* aux textes réglementaires et juridiques officiels — on demande en langage naturel, on reçoit le **texte officiel exact**, pas un résumé généré par LLM.

> Cette fiche couvre l'**ensemble de la suite**. Le point d'entrée le plus connu est `EU_compliance_MCP` (le premier recensé), mais l'org publie en réalité une centaine de serveurs analogues.

## Type & intégration
**Serveurs MCP** (read-only) interrogeables depuis Claude Code, Claude Desktop, Cursor, Cline, et tout client compatible MCP. Deux architectures de données selon le serveur :
- **Base embarquée** (SQLite FTS5) contenant le texte verbatim (ex. l'EU, basé sur EUR-Lex), avec vérification de fraîcheur quotidienne.
- **APIs gouvernementales live** pour certains volets (ex. le volet US s'appuyait sur eCFR.gov, California LegInfo, regulations.gov).

Principe commun : **zéro résumé / paraphrase LLM**, on sert le texte officiel citable. Écrit majoritairement en TypeScript. Org GitHub : `Ansvar-Systems` (**150 dépôts publics**), éditeur **Ansvar AI** (ansvar.eu — « cited answers for compliance, legal, and security teams »).

## Couverture (extraits du catalogue)
- **UE — `EU_compliance_MCP`** (vaisseau amiral) : ~49–61 réglementations (GDPR, **AI Act**, DORA, NIS2, MiFID II, eIDAS, MDR, Chips Act…), milliers d'articles/considérants/définitions + mappings **ISO 27001 / NIST CSF**.
- **Droit national par pays** : UK (`UK-law-mcp`, 3 243 actes), Luxembourg (4 551), Irlande (3 972), France (Code civil/pénal/travail), Allemagne, Italie, Espagne, Pays-Bas, Suède, Finlande, Danemark, etc.
- **Protection des données par autorité** : CNIL-like par pays — ICO (UK), AEPD (ES), Garante (IT), BfDI/BfD (DE), CNPD, IMY (SE), DPC (IE), FDPIC (CH)…
- **Cybersécurité par autorité** : BSI (DE), NCSC (UK/IE/FI), CCN-CERT (ES), MSB (SE), CIRCL (LU)…
- **Concurrence**, **régulation financière** (BaFin, CNMV, FI, MFSA…) et **énergie** par pays.

## Modèle économique
- **Connecteurs MCP open-source, licence Apache 2.0** (quelques dépôts en `NOASSERTION`) — self-hosting gratuit. Gateway + données licenciées = propriétaire.
- **Ansvar Gateway** (hébergée, 100 % UE/Hetzner, OAuth) : **Free 0 € = 100 recherches/jour par siège** (concurrency 1, compte B2B + VAT requis) ; **Premium 249 €/siège/mois** (ou 2490 €/an, ~5000 recherches/j/siège) ; **Team/Company** sur devis (waitlist). Conseil dès 2000 €.
- ✅ Correction : le « free tier 50 req/j » précédemment indiqué était **faux** (vérifié sur ansvar.eu/limits = 100/jour par siège).

## Coût LLM
**Aucun LLM** 🟢 — pas d'inférence : les serveurs récupèrent et présentent le texte officiel. Tu apportes ton client (BYO abonnement Claude/Cursor) ; le coût LLM est celui de ce client, pas des serveurs. La valeur = **fidélité** (texte exact, citable), pas génération.

## À quoi ça sert
Référence de conformité/juridique « AI-readable » pour qui construit des produits pour les marchés européens (et au-delà) : recherche, recoupement et citation de réglementations directement dans l'agent. Mappings vers référentiels (ISO/NIST), artefacts d'audit, règles d'applicabilité par secteur.

## Notes / à creuser
- **Famille 8 (sources de connaissances via MCP)** : archétype de la catégorie. Cousin technique de [Polaris (polarismcp.com)](polaris.md)/[Cavemem](cavemem.md) (SQLite FTS5 + MCP local) mais sur des **domaines métier** (droit/réglementation) au lieu du code.
- ⚠️ **Avertissement de l'éditeur** : les *control mappings* sont des « aides interprétatives, pas une guidance officielle » — vérifier les sources officielles, consulter un juriste. Outil d'aide, **pas de conseil juridique**.
- ⚠️ **Volet US retiré** : `US_Compliance_MCP` et `US-law-mcp` (HIPAA, CCPA, GLBA, FERPA, COPPA, SOX, FDA 21 CFR Part 11) sont référencés par les moteurs mais renvoient **HTTP 404** (supprimés/renommés/privés au 2026-06-15). À surveiller s'ils réapparaissent.
- Catalogue en croissance rapide (150 dépôts, beaucoup poussés en juin 2026) — la couverture évolue.

## Source
- Org GitHub : https://github.com/Ansvar-Systems (150 dépôts publics) · vaisseau amiral : https://github.com/Ansvar-Systems/EU_compliance_MCP · npm : `@ansvar/eu-regulations-mcp`
- Éditeur : https://ansvar.eu/ (Ansvar AI, Stockholm)
- Annuaires MCP : mcpservers.org, lobehub, pulsemcp

*(vérifié le 2026-06-15 — API GitHub de l'org [150 repos publics confirmés] + README EU + recherche web ; volet US confirmé 404 via API GitHub)*
