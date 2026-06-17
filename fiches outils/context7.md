---
outil: "Context7"
type: "Serveur MCP (doc de librairies) — open-source + hébergé"
url: https://context7.com/
modele_economique: "Open-source (MIT) + service hébergé gratuit (clé API pour + de quota)"
cout_llm: "Intégré (source de doc ; ne génère pas de LLM)"
---

# Context7

**En une phrase** — Serveur MCP (Upstash) qui injecte dans le prompt la **doc à jour et spécifique à la version** des librairies + des exemples de code, pour que l'agent ne se trompe pas d'API.

## Type & intégration
Serveur MCP, en remote hébergé (`https://mcp.context7.com/mcp`) ou en local. Outils : `resolve-library-id` (résout un nom de lib en ID, ex. `/supabase/supabase`) puis `query-docs`. CLI `ctx7` aussi. Compatible Claude Code, Cursor et 30+ agents. **Déjà connecté dans cette session Claude Code.**

## Modèle économique
**Open-source — MIT.** Service hébergé **gratuit** sans authentification ; une **clé API gratuite** (context7.com/dashboard) débloque des limites de débit plus élevées. Pas de tier payant clairement documenté à ce jour.

## Coût LLM
**🟢 Intégré** : source de documentation — ne génère pas de complétion, tourne dans ton agent (coût LLM = celui de l'agent). Vise à *réduire* les hallucinations d'API et le contexte chargé.

## À quoi ça sert
Servir à l'agent la **bonne doc de librairie, à jour**, au moment où il code — créneau identique à Ref. Très répandu, intégration triviale (MCP).

## Notes / à creuser
- Voisins directs : [Ref](ref.md) (doc + repos/PDF privés, freemium) et [GitMCP](gitmcp.md) (repo GitHub → MCP).
- Édité par **Upstash** (Redis/Kafka serverless) ; bonne traction communautaire.

## Source
https://context7.com/ · https://github.com/upstash/context7 (LICENSE = MIT). *(vérifié le 2026-06-17)*
