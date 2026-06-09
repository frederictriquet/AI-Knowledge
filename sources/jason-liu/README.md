# Source externe — Jason Liu (jxnl.co)

Auteur de la librairie **instructor** (structured outputs / Pydantic), consultant RAG.
Ingestion pour la base de connaissances française : posts du blog + doc *instructor*,
sélectionnés pour la vue « améliorer un RAG en production » et « sorties structurées »
absente du corpus IBM.

## Arborescence
- `html/` — pages brutes téléchargées (curl).
- `md/` — extraits Markdown (via `sources/extract_generic.py`, pandoc).
- `concepts/` — fiches de synthèse françaises (gabarit projet).

## Posts ingérés
| md | titre | mots | URL |
|----|-------|------|-----|
| `ameliorer-rag-systematiquement.md` | Systematically Improving Your RAG | ~2619 | https://jxnl.co/writing/2024/05/22/systematically-improving-your-rag/ |
| `predictions-future-rag.md` | Predictions for the Future of RAG | ~1068 | https://jxnl.co/writing/2024/06/05/predictions-for-the-future-of-rag/ |
| `instructor-home.md` | Instructor — Structured LLM Outputs (doc) | ~1771 | https://python.useinstructor.com/ |

## Fiches
- `concepts/ameliorer-rag-systematiquement.md` — 🔴 substance : RAG mesurable (recall/precision, feedback, clustering).
- `concepts/sorties-structurees-instructor.md` — 🟡 tradeoff : sorties typées Pydantic, validation + retries.
- `concepts/rapports-plutot-que-rag.md` — 🟢 vision : du Q&A vers la génération de rapports (SOP/templates).

## Découverte
Index `/writing/` rendu en JS (aucun lien exploitable dans le HTML). URLs de posts
extraites du **sitemap** `https://jxnl.co/sitemap.xml`. UA Firefox sans parenthèses.

## Notes
- Le post keynote « Pydantic is all you need » a été écarté (page = vidéo, ~108 mots) ;
  remplacé par la page d'accueil de la doc *instructor* (plus substantielle) pour la
  fiche sorties structurées.
