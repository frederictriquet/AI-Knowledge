#!/usr/bin/env python3
"""Génère INDEX-THEMATIQUE.md et RAPPORT-CORPUS.md à partir du frontmatter des fiches.

Usage : python3 tools/build_index.py
Idempotent : régénère intégralement les deux fichiers à la racine du dépôt.
"""
import os
import re
import glob
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHES = os.path.join(ROOT, "fiches")

# Ordre de parcours pédagogique + libellé affiché par thème.
THEMES = [
    ("fondamentaux-agents", "🧱 Fondamentaux des agents"),
    ("raisonnement-planification", "🧠 Raisonnement & planification"),
    ("prompting", "✍️ Prompting"),
    ("outils-function-calling", "🔧 Outils & function-calling"),
    ("rag-contexte", "📚 RAG & contexte"),
    ("memoire", "💾 Mémoire"),
    ("multi-agents", "👥 Multi-agents"),
    ("protocoles-interop", "🔌 Protocoles & interopérabilité"),
    ("frameworks-outillage", "🛠️ Frameworks & outillage"),
    ("evaluation", "📊 Évaluation"),
    ("benchmarks", "🏁 Benchmarks"),
    ("securite", "🔐 Sécurité"),
    ("efficacite-cout", "⚡ Efficacité & coût"),
    ("gouvernance-alignement-ops", "⚖️ Gouvernance, alignement & ops"),
]
THEME_LABEL = dict(THEMES)
NIVEAU_RANG = {"🔴": 0, "🟡": 1, "🟢": 2}


def parse_frontmatter(path):
    """Retourne le dict du frontmatter YAML simple (clé: valeur), ou {} si absent."""
    txt = open(path, encoding="utf-8", errors="replace").read()
    if not txt.startswith("---"):
        return {}
    bloc = txt.split("---", 2)[1]
    d = {}
    for line in bloc.splitlines():
        m = re.match(r"([A-Za-z_]+):\s*(.*)", line)
        if m:
            d[m.group(1)] = m.group(2).strip().strip('"')
    return d


def charger():
    fiches = []
    for f in sorted(glob.glob(os.path.join(FICHES, "*.md"))):
        d = parse_frontmatter(f)
        d["_slug"] = os.path.basename(f)[:-3]
        fiches.append(d)
    return fiches


def ligne_fiche(d):
    titre = d.get("titre", d["_slug"])
    url = d.get("source_url", "").strip()
    src = f" → [source]({url})" if url else " → ⚠️ _source manquante_"
    prim = d.get("source_primaire", "").strip()
    prim = f"  ·  papier : {prim}" if prim else ""
    niv = d.get("niveau", "")
    prov = d.get("provenance", "")
    return f"- {niv} {prov} **[{titre}](fiches/{d['_slug']}.md)**{src}{prim}"


def build_index(fiches):
    par_theme = defaultdict(list)
    for d in fiches:
        par_theme[d.get("theme", "??")].append(d)
    out = ["# Index thématique du corpus IA\n",
           "> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.\n",
           f"{len(fiches)} fiches · provenance : ✅ IBM · ➕ hors-corpus · 🔗 source externe · "
           "niveau : 🔴 substance · 🟡 tradeoff · 🟢 survol\n",
           "## Sommaire\n"]
    for slug, label in THEMES:
        n = len(par_theme.get(slug, []))
        anc = label.split(" ", 1)[1].lower().replace(" ", "-").replace("&", "").replace("'", "")
        anc = re.sub(r"[^a-z0-9\-éèàûô]", "", anc)
        out.append(f"- [{label}](#{anc}) — {n}")
    out.append("")
    for slug, label in THEMES:
        items = par_theme.get(slug, [])
        if not items:
            continue
        items.sort(key=lambda d: (NIVEAU_RANG.get(d.get("niveau"), 9), d.get("titre", "")))
        out.append(f"\n## {label}\n")
        out += [ligne_fiche(d) for d in items]
    # thèmes inconnus éventuels
    autres = {k: v for k, v in par_theme.items() if k not in THEME_LABEL}
    for slug, items in autres.items():
        out.append(f"\n## ⚠️ {slug} (thème hors taxonomie)\n")
        out += [ligne_fiche(d) for d in items]
    open(os.path.join(ROOT, "INDEX-THEMATIQUE.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")


def build_rapport(fiches):
    par_theme = defaultdict(list)
    par_prov = defaultdict(int)
    sans_url = []
    for d in fiches:
        par_theme[d.get("theme", "??")].append(d)
        par_prov[d.get("provenance", "?")] += 1
        if not d.get("source_url", "").strip():
            sans_url.append(d["_slug"])
    out = ["# Rapport de complétude du corpus\n",
           "> ⚙️ **Fichier généré** par `tools/build_index.py`.\n",
           f"**{len(fiches)} fiches** au total.\n",
           "## Par provenance\n"]
    for p, n in sorted(par_prov.items(), key=lambda x: -x[1]):
        out.append(f"- {p} : {n}")
    out.append("\n## Par thème\n")
    for slug, label in THEMES:
        n = len(par_theme.get(slug, []))
        flag = "  ⚠️ _peu couvert_" if n < 3 else ""
        out.append(f"- {label} : {n}{flag}")
    out.append(f"\n## Fiches sans `source_url` ({len(sans_url)})\n")
    out += [f"- `{s}`" for s in sorted(sans_url)] or ["- (aucune)"]
    # doublons de titre éventuels
    par_titre = defaultdict(list)
    for d in fiches:
        par_titre[d.get("titre", "").lower()].append(d["_slug"])
    dups = {t: s for t, s in par_titre.items() if len(s) > 1}
    out.append(f"\n## Doublons de titre potentiels ({len(dups)})\n")
    out += [f"- « {t} » : {', '.join(s)}" for t, s in dups.items()] or ["- (aucun)"]
    open(os.path.join(ROOT, "RAPPORT-CORPUS.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")


def main():
    import sys
    fiches = charger()
    build_index(fiches)
    build_rapport(fiches)
    sys.stdout.write(f"OK — {len(fiches)} fiches indexées.\n")
    sys.stdout.write("→ INDEX-THEMATIQUE.md\n→ RAPPORT-CORPUS.md\n")


if __name__ == "__main__":
    main()
