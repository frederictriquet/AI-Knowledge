#!/usr/bin/env python3
"""Génère INDEX-THEMATIQUE.md et RAPPORT-CORPUS.md à partir du frontmatter des fiches.

Usage : python3 tools/build_index.py
Idempotent : régénère intégralement les deux fichiers à la racine du dépôt.
"""
import os
import re
import glob
import unicodedata
from collections import defaultdict

# kb_common est un module frère (tools/), importable en python3 nu : ses imports
# de tête (os/re/glob) sont légers ; numpy n'est chargé que dans cosine().
# pyright: reportMissingImports=false
from kb_common import parse_frontmatter, themes_fiche, objectifs_fiche, OBJECTIFS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
FICHES = os.path.join(WIKI, "fiches")
FICHES_OUTILS = os.path.join(WIKI, "fiches outils")
THEME_DIR = os.path.join(WIKI, "themes")
GUIDES_DIR = os.path.join(WIKI, "guides")

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
NIVEAU_LABEL = [("🔴", "Substance / cœur"), ("🟡", "Tradeoff / intermédiaire"), ("🟢", "Survol / introductif")]

# Intro d'une ligne par thème, affichée en tête de chaque page de thème (L2).
THEME_INTRO = {
    "fondamentaux-agents": "Ce qu'est un agent, ses composants et ses limites structurelles.",
    "raisonnement-planification": "Faire raisonner, planifier et s'auto-corriger un modèle.",
    "prompting": "Formuler et optimiser les prompts (techniques, in-context learning).",
    "outils-function-calling": "Donner des outils à un agent et soigner l'interface agent-ordinateur.",
    "rag-contexte": "Augmenter le modèle par récupération et gérer le contexte.",
    "memoire": "Mémoire court/long terme et persistance entre sessions.",
    "multi-agents": "Orchestrer et structurer plusieurs agents.",
    "protocoles-interop": "Standards d'interopérabilité (MCP, A2A…).",
    "frameworks-outillage": "Frameworks et bibliothèques pour construire des agents.",
    "evaluation": "Mesurer la qualité : évals, juges LLM, analyse d'erreurs.",
    "benchmarks": "Jeux de test et métriques standardisées.",
    "securite": "Menaces, injections et défense des systèmes LLM.",
    "efficacite-cout": "Réduire coût et latence (routing, caching, décodage).",
    "gouvernance-alignement-ops": "Piloter, observer et gouverner les systèmes en production.",
}


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


def accroche_fiche(slug):
    """Extrait l'accroche « En une phrase » du corps d'une fiche concept. '' si absente."""
    try:
        txt = open(os.path.join(FICHES, slug + ".md"), encoding="utf-8", errors="replace").read()
    except OSError:
        return ""
    m = re.search(r"\*\*En une phrase\*\*\s*[—–-]\s*(.+)", txt)
    return m.group(1).strip() if m else ""


def rendu_bloc_guide(obj, items):
    """Rend l'index (groupé par thème) des fiches taguées d'un objectif donné."""
    par_theme = defaultdict(list)
    for d in items:
        par_theme[d.get("theme", "??")].append(d)
    lignes = [
        f"> ⚙️ **Index généré** — {len(items)} fiche(s) taguée(s) `objectifs: [{obj}]`, "
        "régénéré par `tools/build_index.py`. La prose ci-dessus est curée à la main.",
    ]
    for slug, label in THEMES:
        grp = par_theme.get(slug, [])
        if not grp:
            continue
        grp.sort(key=lambda d: (NIVEAU_RANG.get(d.get("niveau"), 9), d.get("titre", "")))
        lignes.append(f"\n### {label}")
        for d in grp:
            acc = accroche_fiche(d["_slug"])
            acc = f" — {acc}" if acc else ""
            niv = d.get("niveau", "")
            lignes.append(f"- {niv} **[{d.get('titre', d['_slug'])}](../fiches/{d['_slug']}.md)**{acc}")
    return "\n".join(lignes)


def slug_ascii(s):
    """Slug ASCII kebab (pour les ancres de famille), accents retirés."""
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()


def ligne_outil_table(d):
    """Ligne de tableau d'un outil, reconstruite depuis son frontmatter."""
    titre = d.get("titre", d.get("outil", d["_slug"]))
    url = d.get("url", "").strip()
    nom = f"**[{titre}]({url})**" if url else f"**{titre}**"
    fiche = f'[📄](../fiches%20outils/{d["_slug"]}.md)'
    return (f"| {nom} · {fiche} | {d.get('type', '')} | {d.get('eco_icones', '')} "
            f"| {d.get('cout_icones', '')} | {d.get('resume', '')} |")


_FAMILLES_META = None


def familles_meta():
    """Prose curée par famille (intro + notes), source `tools/familles.json`."""
    global _FAMILLES_META
    if _FAMILLES_META is None:
        import json
        p = os.path.join(ROOT, "tools", "familles.json")
        _FAMILLES_META = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
    return _FAMILLES_META


def rendu_bloc_outils(obj, outils):
    """Rend les outils d'un objectif, groupés par famille (tables), depuis le frontmatter.

    La prose curée de chaque famille (intro + « clés de lecture ») est réinjectée
    depuis `tools/familles.json` — préservée, pas perdue avec les recensements.
    """
    meta = familles_meta()
    par_fam = defaultdict(list)
    for d in outils:
        if obj in objectifs_fiche(d):
            par_fam[d.get("famille", "(sans famille)")].append(d)
    if not par_fam:
        return "> _(aucun outil rattaché à cet objectif pour l'instant)_"
    total = sum(len(v) for v in par_fam.values())
    lignes = [f"> ⚙️ **Outils générés** — {total} outil(s) `objectifs: [{obj}]`, groupés par famille. "
              "Régénéré par `tools/build_index.py` depuis le frontmatter des fiches outils."]
    for fam in sorted(par_fam):
        lignes.append(f'\n<a id="fam-{slug_ascii(fam)}"></a>')
        lignes.append(f"### {fam}\n")
        if meta.get(fam):
            lignes.append(meta[fam] + "\n")
        lignes.append("| Outil | Type | Éco | Coût LLM | En bref |")
        lignes.append("|---|---|:--:|:--:|---|")
        for d in sorted(par_fam[fam], key=lambda d: d.get("titre", d["_slug"]).lower()):
            lignes.append(ligne_outil_table(d))
    return "\n".join(lignes)


def _injecter_bloc(txt, marqueur, bloc):
    """Remplace le contenu entre `<!-- marqueur -->` et `<!-- /marqueur -->` (ajoute si absent)."""
    debut, fin = f"<!-- {marqueur} -->", f"<!-- /{marqueur.split(':')[0]} -->"
    remplacement = f"{debut}\n{bloc}\n{fin}"
    motif = re.compile(re.escape(debut) + r".*?" + re.escape(fin), re.DOTALL)
    return motif.sub(remplacement, txt) if motif.search(txt) else txt.rstrip() + "\n\n" + remplacement + "\n"


def build_guides(fiches, outils):
    """Remplit les blocs générés de chaque page-sujet : concepts (`AUTO:objectif=X`)
    ET outils (`AUTO-OUTILS:objectif=X`). La prose curée est préservée.
    """
    if not os.path.isdir(GUIDES_DIR):
        return []
    fiches_par_obj = defaultdict(list)
    for d in fiches:
        for o in objectifs_fiche(d):
            fiches_par_obj[o].append(d)
    generes = []
    for path in sorted(glob.glob(os.path.join(GUIDES_DIR, "*.md"))):
        txt = open(path, encoding="utf-8", errors="replace").read()
        obj = parse_frontmatter(txt).get("objectif", "").strip()
        if not obj:
            continue
        if obj not in OBJECTIFS:
            sys_warn(f"⚠️  guide {os.path.basename(path)} : objectif « {obj} » hors vocabulaire OBJECTIFS")
        txt = _injecter_bloc(txt, f"AUTO:objectif={obj}", rendu_bloc_guide(obj, fiches_par_obj.get(obj, [])))
        txt = _injecter_bloc(txt, f"AUTO-OUTILS:objectif={obj}", rendu_bloc_outils(obj, outils))
        open(path, "w", encoding="utf-8").write(txt)
        generes.append(os.path.basename(path)[:-3])
    return generes


def lister_guides():
    """[(slug, titre)] des guides L3 présents, pour le sommaire INDEX-THEMATIQUE."""
    res = []
    for path in sorted(glob.glob(os.path.join(GUIDES_DIR, "*.md"))):
        fm = parse_frontmatter(path)
        res.append((os.path.basename(path)[:-3], fm.get("titre", os.path.basename(path)[:-3])))
    return res


def sys_warn(msg):
    import sys
    sys.stderr.write(msg + "\n")


def bloc_concepts_moc(concepts):
    """Rend les concepts d'un thème groupés par niveau, avec accroche (L2 enrichi)."""
    par_niv = defaultdict(list)
    for d in concepts:
        par_niv[d.get("niveau", "")].append(d)
    out = []
    for niv, lab in NIVEAU_LABEL:
        grp = sorted(par_niv.get(niv, []), key=lambda d: d.get("titre", ""))
        if not grp:
            continue
        out.append(f"### {niv} {lab}")
        for d in grp:
            acc = accroche_fiche(d["_slug"])
            acc = f" — {acc}" if acc else ""
            out.append(f"- **[{d.get('titre', d['_slug'])}](../fiches/{d['_slug']}.md)**{acc}")
        out.append("")
    return out or ["- _(aucun)_", ""]


def build_moc(fiches, outils):
    """Génère une page-hub par thème : concepts + outils du même sujet.

    Les liens vers `fiches/` et `fiches outils/` créent dans le graphe Obsidian
    les arêtes qui relient les deux corpus à travers chaque thème.
    """
    os.makedirs(THEME_DIR, exist_ok=True)
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
        tools.sort(key=lambda d: d.get("titre", d["_slug"]).lower())
        nom = label.split(" ", 1)[1]
        out = [
            "---", "type: index", f'titre: "Thème — {nom}"', f"theme: {slug}", "---", "",
            f"# {label}", "",
            "> ⚙️ **Fichier généré** par `tools/build_index.py` — ne pas éditer à la main.", "",
        ]
        intro = THEME_INTRO.get(slug)
        if intro:
            out += [f"_{intro}_", ""]
        out += [f"## Concepts ({len(concepts)})", ""]
        out += bloc_concepts_moc(concepts)
        out += [f"## Outils ({len(tools)})", ""]
        out += [ligne_outil(d) for d in tools] or ["- _(aucun)_"]
        open(os.path.join(THEME_DIR, f"{slug}.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
        generes.append(slug)
    return generes


def build_index(fiches, outils):
    """INDEX-THEMATIQUE.md : sommaire léger renvoyant vers les pages par thème."""
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
           "chaque thème ouvre une page-hub (concepts + outils).\n"]
    guides = lister_guides()
    if guides:
        out.append("## Guides par objectif (transverses)\n")
        out += [f"- **[{titre}](guides/{slug}.md)**" for slug, titre in guides]
        out.append("")
    out += ["## Par thème\n",
            "| Thème | Concepts | Outils |",
            "|---|---:|---:|"]
    for slug, label in THEMES:
        nc = len(concepts_par_theme.get(slug, []))
        no = len(outils_par_theme.get(slug, []))
        out.append(f"| [{label}](themes/{slug}.md) | {nc} | {no} |")
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
        *([f"- **Guides par objectif** ({len(lister_guides())}) → [`guides/`](guides/) "
           "· parcours transverses orientés tâche"] if lister_guides() else []),
        f"- **Concepts** ({n_concepts}) → [`fiches/`](fiches/) · index : [INDEX-THEMATIQUE.md](INDEX-THEMATIQUE.md)",
        f"- **Outils** ({n_outils}) → [`fiches outils/`](fiches%20outils/) · hub & légende : [outils IA.md](outils%20IA.md)",
        "  - par sujet : [produire du code](guides/generer-du-code-avec-l-ia.md) · "
        "[IA dans un produit](guides/mettre-de-l-ia-en-production.md) · "
        "[pour ceux qui ne codent pas](guides/ia-pour-ceux-qui-ne-codent-pas.md)",
        "",
        "## Fichiers réservés (OKF)",
        "",
        "- [index.md](index.md) — ce fichier (listing du bundle)",
        "- [log.md](log.md) — journal append-only, plus récent en bas",
        "",
        "## Dérivés générés",
        "",
        "- [INDEX-THEMATIQUE.md](INDEX-THEMATIQUE.md) — sommaire des thèmes (concepts + outils)",
        "- [`themes/`](themes/) — une page-hub par thème, reliant concepts et outils",
        "- [RAPPORT-CORPUS.md](RAPPORT-CORPUS.md) — complétude / doublons / thèmes d'outils",
    ]
    open(os.path.join(WIKI, "index.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")


def main():
    import sys
    fiches = charger()
    outils = charger_outils()
    mocs = build_moc(fiches, outils)
    guides = build_guides(fiches, outils)
    build_index(fiches, outils)
    build_rapport(fiches, outils)
    build_okf_index(fiches)
    sys.stdout.write(f"OK — {len(fiches)} concepts + {len(outils)} outils indexés.\n")
    sys.stdout.write(f"→ {len(mocs)} themes/*.md\n→ {len(guides)} guide(s) L3\n→ INDEX-THEMATIQUE.md\n"
                     "→ RAPPORT-CORPUS.md\n→ index.md (OKF)\n")


if __name__ == "__main__":
    main()
