#!/usr/bin/env python3
"""Génère INDEX-THEMATIQUE.md et RAPPORT-CORPUS.md à partir du frontmatter des fiches.

Usage : python3 tools/build_index.py
Idempotent : régénère intégralement les deux fichiers à la racine du dépôt.
"""
import os
import glob
from collections import defaultdict

# kb_common est un module frère (tools/), importable en python3 nu : ses imports
# de tête (os/re/glob) sont légers ; numpy n'est chargé que dans cosine().
# pyright: reportMissingImports=false
from kb_common import parse_frontmatter, themes_fiche

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
FICHES = os.path.join(WIKI, "fiches")
FICHES_OUTILS = os.path.join(WIKI, "fiches outils")
MOC_DIR = os.path.join(WIKI, "MOC")

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


def charger():
    fiches = []
    for f in sorted(glob.glob(os.path.join(FICHES, "*.md"))):
        d = parse_frontmatter(f)
        d["_slug"] = os.path.basename(f)[:-3]
        fiches.append(d)
    return fiches


def charger_outils():
    """Charge le frontmatter des fiches outils (hors gabarits `_*.md`)."""
    outils = []
    for f in sorted(glob.glob(os.path.join(FICHES_OUTILS, "*.md"))):
        if os.path.basename(f).startswith("_"):
            continue
        d = parse_frontmatter(f)
        d["_slug"] = os.path.basename(f)[:-3]
        d["_themes"] = themes_fiche(d)
        outils.append(d)
    return outils


def ligne_fiche(d, base="fiches/"):
    titre = d.get("titre", d["_slug"])
    url = d.get("source_url", "").strip()
    src = f" → [source]({url})" if url else " → ⚠️ _source manquante_"
    prim = d.get("source_primaire", "").strip()
    prim = f"  ·  papier : {prim}" if prim else ""
    niv = d.get("niveau", "")
    return f"- {niv} **[{titre}]({base}{d['_slug']}.md)**{src}{prim}"


def ligne_outil(d, base="../fiches outils/"):
    titre = d.get("titre", d.get("outil", d["_slug"]))
    typ = d.get("type", "").strip()
    typ = f" — _{typ}_" if typ else ""
    cible = (base + d["_slug"] + ".md").replace(" ", "%20")
    return f"- **[{titre}]({cible})**{typ}"


def build_moc(fiches, outils):
    """Génère une page-hub MOC par thème : concepts + outils du même sujet.

    Les liens vers `fiches/` et `fiches outils/` créent dans le graphe Obsidian
    les arêtes qui relient les deux corpus à travers chaque thème.
    """
    os.makedirs(MOC_DIR, exist_ok=True)
    concepts_par_theme = defaultdict(list)
    for d in fiches:
        concepts_par_theme[d.get("theme", "??")].append(d)
    outils_par_theme = defaultdict(list)
    for d in outils:
        for th in d["_themes"]:
            outils_par_theme[th].append(d)

    generes = []
    for slug, label in THEMES:
        concepts = concepts_par_theme.get(slug, [])
        tools = outils_par_theme.get(slug, [])
        concepts.sort(key=lambda d: (NIVEAU_RANG.get(d.get("niveau"), 9), d.get("titre", "")))
        tools.sort(key=lambda d: d.get("titre", d["_slug"]).lower())
        nom = label.split(" ", 1)[1]
        out = [
            "---", "type: index", f'titre: "MOC — {nom}"', f"theme: {slug}", "---", "",
            f"# {label}", "",
            "> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.", "",
            f"## Concepts ({len(concepts)})", "",
        ]
        out += [ligne_fiche(d, base="../fiches/") for d in concepts] or ["- _(aucun)_"]
        out += ["", f"## Outils ({len(tools)})", ""]
        out += [ligne_outil(d) for d in tools] or ["- _(aucun)_"]
        open(os.path.join(MOC_DIR, f"{slug}.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
        generes.append(slug)
    return generes


def build_index(fiches, outils):
    """INDEX-THEMATIQUE.md : sommaire léger renvoyant vers les MOC par thème."""
    concepts_par_theme = defaultdict(list)
    for d in fiches:
        concepts_par_theme[d.get("theme", "??")].append(d)
    outils_par_theme = defaultdict(list)
    for d in outils:
        for th in d["_themes"]:
            outils_par_theme[th].append(d)
    out = ["# Index thématique du corpus IA\n",
           "> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.\n",
           f"{len(fiches)} concepts · {len(outils)} outils · "
           "chaque thème ouvre une page-hub (concepts + outils).\n",
           "| Thème | Concepts | Outils |",
           "|---|---:|---:|"]
    for slug, label in THEMES:
        nc = len(concepts_par_theme.get(slug, []))
        no = len(outils_par_theme.get(slug, []))
        out.append(f"| [{label}](MOC/{slug}.md) | {nc} | {no} |")
    autres = sorted(k for k in concepts_par_theme if k not in THEME_LABEL)
    if autres:
        out.append("")
        for slug in autres:
            items = concepts_par_theme[slug]
            out.append(f"\n## ⚠️ {slug} (thème hors taxonomie)\n")
            out += [ligne_fiche(d) for d in items]
    open(os.path.join(WIKI, "INDEX-THEMATIQUE.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")


def build_rapport(fiches, outils):
    par_theme = defaultdict(list)
    sans_url = []
    for d in fiches:
        par_theme[d.get("theme", "??")].append(d)
        if not d.get("source_url", "").strip():
            sans_url.append(d["_slug"])
    out = ["# Rapport de complétude du corpus\n",
           "> ⚙️ **Fichier généré** par `tools/build_index.py`.\n",
           f"**{len(fiches)} fiches** au total.\n",
           "## Par thème\n"]
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

    sans, hors = valider_themes_outils(outils)
    out.append(f"\n## Outils sans `themes` ({len(sans)})\n")
    out += [f"- `{s}`" for s in sorted(sans)] or ["- (aucun)"]
    out.append(f"\n## Outils avec un thème hors taxonomie ({len(hors)})\n")
    out += [f"- `{s}` : {', '.join(t)}" for s, t in sorted(hors.items())] or ["- (aucun)"]
    open(os.path.join(WIKI, "RAPPORT-CORPUS.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")


def valider_themes_outils(outils):
    """Liste les outils dont `themes` est vide ou contient un thème hors taxonomie."""
    valides = set(THEME_LABEL)
    sans = [d["_slug"] for d in outils if not d["_themes"]]
    hors = {d["_slug"]: [t for t in d["_themes"] if t not in valides]
            for d in outils}
    hors = {s: t for s, t in hors.items() if t}
    return sans, hors


def build_okf_index(fiches):
    """Génère index.md à la racine : point d'entrée OKF (progressive disclosure).

    Ne duplique pas le contenu — renvoie vers les index/tableaux/hub existants.
    """
    n_concepts = len(fiches)
    n_outils = len(glob.glob(os.path.join(WIKI, "fiches outils", "*.md")))
    n_outils = max(0, n_outils - len(glob.glob(os.path.join(WIKI, "fiches outils", "_*.md"))))
    out = [
        "---",
        'type: index',
        'title: "Corpus IA — Knowledge Base"',
        'description: "Point d\'entrée OKF du wiki : concepts (fiches/) + recensement d\'outils (fiches outils/)."',
        "---",
        "",
        "# Corpus IA — point d'entrée",
        "",
        "> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.",
        "> Bundle conforme [Open Knowledge Format](https://okf.md/spec/) ; le schéma faisant foi est `process/SCHEMA.md` (sur-ensemble strict).",
        "",
        "## Contenu",
        "",
        f"- **Concepts** ({n_concepts}) → [`fiches/`](fiches/) · index : [INDEX-THEMATIQUE.md](INDEX-THEMATIQUE.md)",
        f"- **Outils** ({n_outils}) → [`fiches outils/`](fiches%20outils/) · hub & légende : [outils IA.md](outils%20IA.md)",
        "  - par question : [Q1 — produire du code](Q1%20-%20produire%20du%20code.md) · "
        "[Q2 — IA dans un produit](Q2%20-%20IA%20dans%20un%20produit.md) · "
        "[Q3 — autres métiers](Q3%20-%20IA%20dans%20les%20autres%20m%C3%A9tiers.md)",
        "",
        "## Fichiers réservés (OKF)",
        "",
        "- [index.md](index.md) — ce fichier (listing du bundle)",
        "- [log.md](log.md) — journal append-only, plus récent en bas",
        "",
        "## Dérivés générés",
        "",
        "- [INDEX-THEMATIQUE.md](INDEX-THEMATIQUE.md) — sommaire des thèmes (concepts + outils)",
        "- [`MOC/`](MOC/) — une page-hub par thème, reliant concepts et outils",
        "- [RAPPORT-CORPUS.md](RAPPORT-CORPUS.md) — complétude / doublons / thèmes d'outils",
    ]
    open(os.path.join(WIKI, "index.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")


def main():
    import sys
    fiches = charger()
    outils = charger_outils()
    mocs = build_moc(fiches, outils)
    build_index(fiches, outils)
    build_rapport(fiches, outils)
    build_okf_index(fiches)
    sys.stdout.write(f"OK — {len(fiches)} concepts + {len(outils)} outils indexés.\n")
    sys.stdout.write(f"→ {len(mocs)} MOC/*.md\n→ INDEX-THEMATIQUE.md\n"
                     "→ RAPPORT-CORPUS.md\n→ index.md (OKF)\n")


if __name__ == "__main__":
    main()
