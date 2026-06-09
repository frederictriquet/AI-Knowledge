# Référentiels de sécurité IA — base de connaissances (sources externes)

Référentiels de sécurité (pas des papiers arXiv) ingérés pour situer les garde-fous du corpus IBM face à des taxonomies de menaces officielles et communautaires.

## Sources

| # | Référentiel | Organisme / année | Source brute | Lien officiel |
|---|---|---|---|---|
| 1 | OWASP Top 10 for LLM Applications | OWASP GenAI Security Project, 2025 | [html](html/owasp-llm-top-10.html), [html (Foundation)](html/owasp-llm-top-10-alt.html) | [genai.owasp.org](https://genai.owasp.org/llm-top-10/) |
| 2 | MITRE ATLAS | MITRE, données v5.6.0 (2025) | [ATLAS.yaml](md/ATLAS.yaml) | [atlas.mitre.org](https://atlas.mitre.org/) |
| 3 | NIST AI 100-2 — Adversarial ML | NIST, mars 2025 | [texte](md/NIST.plain.txt) | [csrc.nist.gov](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) |

## Fiches de synthèse

- 🔴 [OWASP Top 10 for LLM Applications](../../fiches/owasp-llm-top-10.md) — les 10 risques `LLM0x:2025` + volet Agentic AI.
- 🔴 [MITRE ATLAS](../../fiches/mitre-atlas.md) — matrice de 16 tactiques / 101 techniques / 57 études de cas adverses contre l'IA.
- 🔴 [NIST AI 100-2 : taxonomie de l'adversarial ML](../../fiches/nist-ai-100-2.md) — taxonomie officielle PredAI / GenAI (évasion, empoisonnement, privacy, prompt injection directe/indirecte).

## Fidélité des sources

- **OWASP** : liste 2025 (codes + titres) récupérée verbatim via WebFetch sur la page officielle ; liste 2023/24 (v1.1) récupérée verbatim dans le HTML de l'OWASP Foundation. Détails du volet *Agentic AI* marqués « (à vérifier) ».
- **MITRE ATLAS** : le site est entièrement rendu en JS (HTML vide) ; données extraites du fichier canonique `ATLAS.yaml` v5.6.0 (GitHub `mitre-atlas/atlas-data`) — tactiques, descriptions et comptes verbatim.
- **NIST AI 100-2** : abstract verbatim de la page CSRC ; structure de la taxonomie et axes de classification extraits verbatim du PDF officiel (table des matières + Executive Summary). Définitions fines white/black/gray-box marquées « (à vérifier) ».
