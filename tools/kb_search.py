#!/usr/bin/env python3
"""Recherche hybride locale dans le corpus (concepts + outils), sans LLM.

Combine deux signaux normalisés (max→1) puis sommés, 100 % local, aucune clé :
  - lexical : TF-IDF maison sur titre (survalorisé) + corps ;
  - sémantique : cosinus requête↔fiche via l'index fastembed (kb_embed).
Un léger bonus s'ajoute si la requête recoupe le slug d'un thème de la fiche.
L'index couvre les deux corpus (cf. kb_embed).

Usage :
    python3 tools/kb_search.py "comment limiter la consommation de tokens"
    python3 tools/kb_search.py "base vectorielle agent" --k 8
    python3 tools/kb_search.py "revue de code" --only outil --json
"""
# kb_embed/kb_common dépendent du venv et d'imports frères, invisibles au hook.
# pyright: reportMissingImports=false
import re
import sys
import json
import math
import argparse
import unicodedata
from collections import defaultdict

import numpy as np
from kb_common import FICHES, FICHES_OUTILS, charger_fiches, corps_fiche, cosine
from kb_embed import maj_index, embed_texts

# Poids de fusion (scores déjà normalisés à [0,1] avant pondération).
W_SEMANTIQUE = 0.55
W_LEXICAL = 0.45
W_THEME = 0.10          # petit bonus de thème, départage à la marge
POIDS_TITRE = 3.0       # une occurrence dans le titre vaut 3 dans le corps

# Mots-outils français/anglais sans valeur discriminante pour le lexical.
STOPWORDS = {
    "le", "la", "les", "un", "une", "des", "de", "du", "d", "l", "et", "ou", "a",
    "à", "au", "aux", "en", "dans", "sur", "pour", "par", "avec", "sans", "se",
    "sa", "son", "ses", "ce", "cet", "cette", "que", "qui", "quoi", "comment",
    "est", "sont", "the", "of", "to", "for", "and", "or", "in", "on", "is", "how",
    "my", "i", "it", "ma", "mon", "mes", "plus", "moins", "comme", "quel", "quelle",
}


def normaliser(texte):
    """Minuscule + suppression des accents (comparaison robuste FR)."""
    texte = unicodedata.normalize("NFKD", texte.lower())
    return "".join(c for c in texte if not unicodedata.combining(c))


def desuffixer(mot):
    """Stemming minimal : unifie singulier/pluriel FR/EN (token/tokens, agents/agent).

    Replie quelques suffixes fréquents pour améliorer le rappel sans dépendance.
    """
    for suf in ("aux", "es", "s", "x"):
        if len(mot) - len(suf) >= 3 and mot.endswith(suf):
            return mot[: -len(suf)]
    return mot


def tokens(texte):
    """Tokenise en mots alphanumériques significatifs (sans stopwords, désuffixés)."""
    bruts = re.findall(r"[a-z0-9]+", normaliser(texte))
    return [desuffixer(t) for t in bruts if t not in STOPWORDS and len(t) > 1]


def construire_lexical(fiches):
    """Pré-calcule, par fiche, les comptes de tokens (titre, corps) + l'IDF global."""
    docs = {}
    df = {}
    for f in fiches:
        titre = f["fm"].get("title", f["slug"])
        corps = corps_fiche(f["txt"])
        ct_titre, ct_corps = {}, {}
        for t in tokens(titre):
            ct_titre[t] = ct_titre.get(t, 0) + 1
        for t in tokens(corps):
            ct_corps[t] = ct_corps.get(t, 0) + 1
        docs[f["slug"]] = (ct_titre, ct_corps)
        for t in set(ct_titre) | set(ct_corps):
            df[t] = df.get(t, 0) + 1
    n = len(fiches) or 1
    idf = {t: math.log(1 + n / c) for t, c in df.items()}
    return docs, idf


def score_lexical(qtok, ct_titre, ct_corps, idf):
    """Score lexical TF-IDF d'une fiche pour les tokens de requête (titre survalorisé)."""
    s = 0.0
    for t in qtok:
        poids = idf.get(t)
        if not poids:
            continue
        tf = ct_titre.get(t, 0) * POIDS_TITRE + ct_corps.get(t, 0)
        if tf:
            s += poids * (1 + math.log(tf))      # saturation logarithmique du TF
    return s


def centroides_themes(index):
    """Centroïde (vecteur moyen) de chaque thème, sur l'ensemble des fiches indexées."""
    par_theme = defaultdict(list)
    for meta in index.values():
        v = meta.get("vector")
        if v:
            for th in meta.get("themes", []):
                par_theme[th].append(v)
    return {th: np.mean(vs, axis=0) for th, vs in par_theme.items() if vs}


def rechercher(requete, only=None):
    """Retourne toutes les fiches porteuses d'un signal, classées par score hybride."""
    fiches = charger_fiches([FICHES, FICHES_OUTILS])
    index, _, _ = maj_index()
    qtok = tokens(requete)
    qvec = embed_texts([requete])[0]
    docs, idf = construire_lexical(fiches)
    # Proximité sémantique requête↔thème : booste les fiches d'un thème proche du sujet.
    theme_qsim = {th: cosine(qvec, c) for th, c in centroides_themes(index).items()}

    brut = []
    for f in fiches:
        if only and f["corpus"] != only:
            continue
        meta = index.get(f["slug"])
        sem = cosine(qvec, meta["vector"]) if meta and meta.get("vector") else 0.0
        ct_titre, ct_corps = docs[f["slug"]]
        lex = score_lexical(qtok, ct_titre, ct_corps, idf)
        thm = max((theme_qsim.get(t, 0.0) for t in f["themes"]), default=0.0)
        brut.append({
            "slug": f["slug"], "corpus": f["corpus"], "themes": f["themes"],
            "titre": f["fm"].get("title", f["slug"]),
            "_sem": sem, "_lex": lex, "_thm": thm,
        })

    # Normalisation max→1 par signal, puis fusion pondérée.
    max_sem = max((b["_sem"] for b in brut), default=0.0) or 1.0
    max_lex = max((b["_lex"] for b in brut), default=0.0) or 1.0
    max_thm = max((b["_thm"] for b in brut), default=0.0) or 1.0
    for b in brut:
        b["score"] = round(
            W_SEMANTIQUE * (b["_sem"] / max_sem)
            + W_LEXICAL * (b["_lex"] / max_lex)
            + W_THEME * (b["_thm"] / max_thm), 4)
    brut.sort(key=lambda b: b["score"], reverse=True)
    # Ne garde que les fiches porteuses d'un signal (évite de lister tout le corpus à 0).
    resultats = [b for b in brut if b["_lex"] > 0 or b["_sem"] > 0]
    for b in resultats:
        for cle in ("_sem", "_lex", "_thm"):
            b.pop(cle, None)
    return resultats


def main():
    ap = argparse.ArgumentParser(description="Local hybrid search (concepts + tools, 0 LLM).")
    ap.add_argument("requete", nargs="?", help="Free-form query.")
    ap.add_argument("--k", type=int, default=8, help="Number of results per section (default 8).")
    ap.add_argument("--only", choices=["concept", "outil"], help="Restrict to one corpus (single list).")
    ap.add_argument("--json", action="store_true", help="Raw JSON output (merged list).")
    args = ap.parse_args()

    if args.requete:
        requete = args.requete
    elif not sys.stdin.isatty():
        requete = sys.stdin.read()
    else:
        ap.error("provide a query (argument or stdin).")
    requete = requete.strip()
    if not requete:
        ap.error("empty query.")

    res = rechercher(requete, only=args.only)

    if args.json:
        json.dump(res[: args.k] if args.only else res, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return

    if not res:
        sys.stdout.write("No results.\n")
        return

    def ligne(b):
        th = (" · " + ", ".join(b["themes"])) if b["themes"] else ""
        return f"  {b['score']:.3f}  {b['titre']}  ({b['slug']}){th}\n"

    sys.stdout.write(f"Search: « {requete} »\n")
    if args.only:
        sys.stdout.write("\n")
        for b in res[: args.k]:
            sys.stdout.write(ligne(b))
        return
    # Deux sections : garantit la présence des concepts ET des outils.
    concepts = [b for b in res if b["corpus"] == "concept"][: args.k]
    outils = [b for b in res if b["corpus"] == "outil"][: args.k]
    sys.stdout.write(f"\n📄 Concepts ({len(concepts)})\n")
    for b in concepts:
        sys.stdout.write(ligne(b))
    sys.stdout.write(f"\n🛠️  Tools ({len(outils)})\n")
    for b in outils:
        sys.stdout.write(ligne(b))


if __name__ == "__main__":
    main()
