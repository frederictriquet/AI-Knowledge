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
FICHES = os.path.join(ROOT, "fiches")
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


def texte_embedding(fm, txt):
    """Construit le texte représentatif d'une fiche pour l'embedding.

    Combine titre + thème + corps : le titre porte le concept, le corps le sens.
    """
    titre = fm.get("titre", "")
    theme = fm.get("theme", "")
    return f"{titre}. Thème : {theme}. {corps_fiche(txt)}"


def charger_fiches():
    """Charge toutes les fiches. Retourne une liste de dicts.

    Chaque dict : {slug, path, fm (frontmatter), txt (brut), texte_embed}.
    """
    out = []
    for path in sorted(glob.glob(os.path.join(FICHES, "*.md"))):
        txt = open(path, encoding="utf-8", errors="replace").read()
        fm = parse_frontmatter(txt)
        out.append({
            "slug": os.path.basename(path)[:-3],
            "path": path,
            "fm": fm,
            "txt": txt,
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
