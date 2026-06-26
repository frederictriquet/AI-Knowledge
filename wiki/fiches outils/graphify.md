---
outil: "Graphify"
titre: "Graphify"
themes: [rag-contexte]
type: "Skill (assistants de codage IA / Claude Code)"
url: https://graphify.net/
modele_economique: "Open-source (MIT), gratuit"
cout_llm: "Intégré (tourne dans Claude Code) — mais consomme des tokens à l'indexation (extraction sémantique LLM)"
---

# Graphify

**En une phrase** — skill open-source qui transforme un dépôt entier (code, docs, articles, diagrammes) en graphe de connaissances multi-modal et interrogeable, pour aider les assistants de codage IA à comprendre *ce que fait* le code et *pourquoi* il est conçu ainsi.

> ⚠️ Homonymie : plusieurs produits s'appellent « Graphify » (graphify.ai, getgraphify.com, graphy.app…). Cette fiche concerne **graphify.net**, le skill open-source de Safi Shamsi.

## Type & intégration
**Skill** pour assistants de codage IA (Claude Code en cible principale). Combine **tree-sitter** (analyse statique : AST, call graphs, docstrings) avec une **extraction sémantique pilotée par LLM**. Multi-modal : parse code (.py, .js, .go, .java…), Markdown, **PDF** et **images**. Produit en sortie un `graph.html` interactif, un `graph.json` interrogeable et un `GRAPH_REPORT.md` lisible (rapport d'audit).

## Modèle économique
**Open-source, licence MIT**, gratuit. Maintenu par Safi Shamsi.

## Coût LLM
**Intégré** 🟢 — le skill tourne dans Claude Code et utilise le LLM de l'agent, pas de clé API séparée. **Nuance importante vs [CodeGraph](codegraph.md)** : Graphify fait de l'**extraction sémantique par LLM** lors de la construction du graphe → l'indexation **consomme des tokens** (à la différence de CodeGraph, 100 % déterministe et gratuit). Le pari : ce coût d'indexation ponctuel est largement amorti ensuite (la communication marketing évoque jusqu'à « 70× » de réduction de coût sur de gros codebases, le graphe évitant de relire le repo à chaque requête).

Ordre de grandeur : coût LLM dépend du volume indexé et du modèle, à l'usage de Claude Code (pas de facture séparée). Indexation = pic de tokens ; requêtes ensuite = économies.

## À quoi ça sert
Donner à un agent une compréhension riche et multi-modale d'un projet (pas seulement le code, mais aussi docs/PDF/diagrammes — le « pourquoi »). Utile sur de gros dépôts où relire les fichiers est coûteux. Inspiré d'idées façon Karpathy sur les graphes de connaissances pour le code.

## Notes / à creuser
- Différence clé avec [CodeGraph](codegraph.md) : Graphify = static **+ sémantique LLM** + multi-modal (consomme des tokens) ; CodeGraph = purement déterministe/AST, local, zéro LLM. À choisir selon qu'on veut le « quoi » brut (CodeGraph) ou le « pourquoi » enrichi (Graphify).
- Sorties exportables (html/json/md) → exploitables hors agent.
- ⚠️ Le « 70× de réduction de coût » est un chiffre **marketing (MindStudio) non vérifié** ; sur un gros monorepo, l'indexation par LLM peut coûter cher avant tout amortissement — préférer [CodeGraph](codegraph.md) (déterministe, zéro token LLM) si le « pourquoi » sémantique n'est pas indispensable.

## Source
- Site officiel : https://graphify.net/ (HTTP 403 au fetch automatisé le 2026-06-15 ; infos via recherche web)
- Analyse tierce : MindStudio (« Karpathy-Inspired Knowledge Graph … 70x »)

*(vérifié le 2026-06-15 — recherche web ; landing officielle non récupérable automatiquement, à reconfirmer en visite directe)*
