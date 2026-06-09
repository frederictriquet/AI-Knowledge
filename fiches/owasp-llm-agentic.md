---
titre: "OWASP Top 10 LLM & menaces agentiques"
theme: securite
niveau: 🟡
provenance: ➕
base: ibm-guide-agents-ia/hors-corpus
source_url: https://genai.owasp.org/llm-top-10/
---

# OWASP Top 10 LLM & menaces agentiques

> Fiche **hors-corpus** (➕) — absente du guide IBM, ajoutée depuis l'état de l'art. Glossaire · Pertinence 🟡 tradeoff

**En une phrase** — le référentiel de sécurité standard dont s'inspire le corpus IBM sans le nommer : une taxonomie partagée des risques LLM, prolongée par un volet spécifique aux menaces agentiques.

## L'idée
L'OWASP Top 10 for LLM Applications fournit une nomenclature commune des risques : **prompt injection**, fuite d'informations sensibles, empoisonnement des données d'entraînement, gestion non sécurisée des sorties (insecure output handling), consommation excessive, vulnérabilités de la chaîne d'approvisionnement, etc. Le document *Agentic AI – Threats and Mitigations* étend cette grille aux propriétés propres aux agents : mémoire persistante empoisonnée, abus d'outils, cascades d'agents, autonomie excessive et défaut de traçabilité. C'est un langage de revue, pas une implémentation.

## Tradeoff / quand l'utiliser
À utiliser comme checklist de threat modeling et pour aligner le vocabulaire entre équipes sécurité et IA ; il situe chaque garde-fou du corpus face à une menace nommée. Limite : c'est un cadre générique de sensibilisation, non prescriptif sur les contre-mesures techniques précises, qui doivent être conçues au cas par cas.

## Source primaire
OWASP, *Top 10 for LLM Applications* (2023/2025) et *OWASP Agentic AI – Threats and Mitigations* (2025) — référentiels OWASP (owasp.org), pas d'arXiv.

## Voir aussi
- [spotlighting](spotlighting.md) (hors-corpus sœur)
- [ethique-gouvernance](ethique-gouvernance.md) (corpus)
