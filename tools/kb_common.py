#!/usr/bin/env python3
"""Helpers partagés du process d'enrichissement de la base de connaissances.

Centralise : la taxonomie des thèmes, le parsing du frontmatter, le chargement
des fiches, la préparation du texte pour les embeddings et la similarité cosinus.
Importé par kb_embed.py, kb_dedup.py, kb_lint.py et kb_check_sources.py.
"""
# numpy vit dans tools/.venv, invisible au type-checker isolé du hook.
# pyright: reportMissingImports=false
import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
FICHES = os.path.join(WIKI, "fiches")
FICHES_OUTILS = os.path.join(WIKI, "fiches outils")
CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".cache")

# Les 14 thèmes valides (slug). Source de vérité unique, alignée sur build_index.py.
THEMES = [
    "fondamentaux-agents",
    "raisonnement-planification",
    "prompting",
    "outils-function-calling",
    "rag-contexte",
    "memoire",
    "multi-agents",
    "protocoles-interop",
    "frameworks-outillage",
    "evaluation",
    "benchmarks",
    "securite",
    "efficacite-cout",
    "gouvernance-alignement-ops",
]
NIVEAUX = {"🔴", "🟡", "🟢"}

# Axe « objectif » (L3 — guides par objectif). Optionnel, multi-valué sur les
# concepts : slug → libellé humain. Sert à générer les guides wiki/guides/.
# Orthogonal au thème (thème = à propos de quoi ; objectif = pour quel but).
OBJECTIFS = {
    "generer-code": "Générer du code avec l'IA",
    "fiabilite": "Fiabiliser & évaluer un système LLM",
    "couts": "Maîtriser le coût en tokens",
    "mise-en-prod": "Mettre de l'IA en production",
}


def split_fiche(txt):
    """Sépare une fiche en (frontmatter_brut, corps). Frontmatter vide si absent."""
    if not txt.startswith("---"):
        return "", txt
    parts = txt.split("---", 2)
    if len(parts) < 3:
        return "", txt
    return parts[1], parts[2]


def parse_frontmatter(txt_ou_path):
    """Parse le frontmatter YAML simple. Accepte un chemin de fichier ou un texte.

    Gère les valeurs scalaires (`clé: valeur`) et les listes en ligne
    (`tags: [a, b]`). Retourne un dict ; {} si pas de frontmatter.
    """
    if "\n" not in txt_ou_path and txt_ou_path.endswith(".md"):
        txt = open(txt_ou_path, encoding="utf-8", errors="replace").read()
    else:
        txt = txt_ou_path
    bloc, _ = split_fiche(txt)
    if not bloc:
        return {}
    d = {}
    for line in bloc.splitlines():
        m = re.match(r"([A-Za-z_]+):\s*(.*)", line)
        if not m:
            continue
        cle, val = m.group(1), m.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            d[cle] = [x.strip().strip('"') for x in val[1:-1].split(",") if x.strip()]
        else:
            d[cle] = val.strip('"')
    return d


def corps_fiche(txt):
    """Retourne le corps Markdown (sans frontmatter), nettoyé pour l'embedding.

    Retire les marqueurs Markdown structurels (titres, gras, listes, liens)
    afin de ne garder que le sens, sans le bruit de mise en forme.
    """
    _, corps = split_fiche(txt)
    corps = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", corps)  # liens → texte seul
    corps = re.sub(r"[#*`>_]", " ", corps)                  # marqueurs MD
    corps = re.sub(r"\s+", " ", corps)
    return corps.strip()


def themes_fiche(fm):
    """Retourne la liste des thèmes d'une fiche, qu'elle porte `theme` ou `themes`.

    Concepts : `theme` (slug unique). Outils : `themes` (liste multi-valuée).
    """
    th = fm.get("themes")
    if isinstance(th, list):
        return [t for t in th if t]
    if isinstance(th, str) and th:
        return [th]
    t = fm.get("theme", "")
    return [t] if t else []


def objectifs_fiche(fm):
    """Retourne la liste des objectifs (axe L3) d'une fiche concept. [] si absent."""
    o = fm.get("objectifs")
    if isinstance(o, list):
        return [x for x in o if x]
    if isinstance(o, str) and o:
        return [o]
    return []


def texte_embedding(fm, txt):
    """Construit le texte représentatif d'une fiche pour l'embedding.

    Combine titre + thème(s) + corps : le titre porte le concept, le corps le sens.
    Lit `theme` (concepts) comme `themes` (outils) via themes_fiche().
    """
    titre = fm.get("titre", "")
    themes = ", ".join(themes_fiche(fm))
    return f"{titre}. Thème : {themes}. {corps_fiche(txt)}"


def charger_fiches(dirs=None):
    """Charge toutes les fiches. Retourne une liste de dicts.

    Chaque dict : {slug, path, fm (frontmatter), txt (brut), texte_embed}.

    `dirs` : itérable de répertoires à scanner. Par défaut, seul ``fiches/``
    (comportement historique des scripts d'enrichissement). Les fiches sont
    dédupliquées par slug — le 1er répertoire de la liste l'emporte.
    """
    if dirs is None:
        dirs = [FICHES]
    out = []
    vus = set()
    for d in dirs:
        corpus = "outil" if os.path.abspath(d) == os.path.abspath(FICHES_OUTILS) else "concept"
        for path in sorted(glob.glob(os.path.join(d, "*.md"))):
            slug = os.path.basename(path)[:-3]
            if slug in vus:
                continue
            vus.add(slug)
            txt = open(path, encoding="utf-8", errors="replace").read()
            fm = parse_frontmatter(txt)
            out.append({
                "slug": slug,
                "path": path,
                "fm": fm,
                "txt": txt,
                "corpus": corpus,
                "themes": themes_fiche(fm),
                "texte_embed": texte_embedding(fm, txt),
            })
    return out


def contenu_hash(texte):
    """Hash stable du texte d'embedding, pour invalider le cache au changement."""
    import hashlib
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()[:16]


def cosine(a, b):
    """Similarité cosinus entre deux vecteurs (listes ou np.ndarray)."""
    import numpy as np
    a, b = np.asarray(a, dtype="float32"), np.asarray(b, dtype="float32")
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(np.dot(a, b) / (na * nb))
