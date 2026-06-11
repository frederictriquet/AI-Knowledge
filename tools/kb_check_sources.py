#!/usr/bin/env python3
"""Vérification factuelle des sources d'une fiche (gate qualité « sources »).

Pour chaque fiche :
  - `source_url` : la page répond-elle (HTTP < 400) ?
  - identifiant arXiv cité (frontmatter ou corps, ex. arXiv:2210.03629) : la page
    https://arxiv.org/abs/<id> existe-t-elle, et son titre est-il cohérent avec
    le titre de papier cité dans la fiche ? (même logique que SOURCES-PRIMAIRES.md)

Réseau requis. Les requêtes ont un timeout ; un échec réseau est signalé sans
masquer le résultat (jamais d'except silencieux).

Usage :
    python3 tools/kb_check_sources.py fiches/react.md
    python3 tools/kb_check_sources.py --all --json
"""
# kb_common est un module frère ; requests vit dans tools/.venv. Invisibles au hook.
# pyright: reportMissingImports=false
import os
import re
import sys
import glob
import json
import html
import argparse

import requests

from kb_common import FICHES, parse_frontmatter

TIMEOUT = 12
HEADERS = {"User-Agent": "AI-Knowledge-source-checker/1.0"}
ARXIV_RE = re.compile(r"arxiv[:/]?\s*(\d{4}\.\d{4,5})", re.IGNORECASE)


def _norm(s):
    """Normalise un titre pour comparaison souple (minuscules, espaces compactés)."""
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s.lower())).strip()


def verifier_url(url):
    """Retourne (ok: bool, detail: str). Tente HEAD puis GET en repli."""
    try:
        r = requests.head(url, timeout=TIMEOUT, headers=HEADERS, allow_redirects=True)
        if r.status_code >= 400:  # certains serveurs refusent HEAD → repli GET
            r = requests.get(url, timeout=TIMEOUT, headers=HEADERS, allow_redirects=True)
        return (r.status_code < 400, f"HTTP {r.status_code}")
    except requests.RequestException as e:
        return (False, f"réseau : {type(e).__name__}")


def titre_arxiv(arxiv_id):
    """Retourne (ok, titre_ou_erreur) pour un identifiant arXiv via l'API officielle."""
    api = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        r = requests.get(api, timeout=TIMEOUT, headers=HEADERS)
    except requests.RequestException as e:
        return (False, f"réseau : {type(e).__name__}")
    if r.status_code >= 400:
        return (False, f"HTTP {r.status_code}")
    m = re.search(r"<entry>.*?<title>(.*?)</title>", r.text, re.DOTALL)
    if not m:
        return (False, "id introuvable sur arXiv")
    return (True, html.unescape(m.group(1).strip()))


def verifier_fiche(path):
    """Vérifie source_url + arXiv d'une fiche. Retourne un dict de résultats."""
    txt = open(path, encoding="utf-8", errors="replace").read()
    fm = parse_frontmatter(txt)
    res = {"slug": os.path.basename(path)[:-3], "checks": []}

    url = fm.get("source_url", "").strip()
    if url:
        ok, detail = verifier_url(url)
        res["checks"].append({"type": "source_url", "ok": ok, "detail": detail, "ref": url})
    else:
        res["checks"].append({"type": "source_url", "ok": False, "detail": "absent", "ref": ""})

    # arXiv : on prend le 1er id trouvé (frontmatter source_primaire ou corps).
    m = ARXIV_RE.search(txt)
    if m:
        arxiv_id = m.group(1)
        ok, titre = titre_arxiv(arxiv_id)
        check = {"type": "arxiv", "ok": ok, "detail": titre, "ref": arxiv_id}
        # Cohérence titre : le titre arXiv réel apparaît-il dans la fiche ?
        if ok:
            titre_norm = _norm(titre)
            # On compare aux mots significatifs du titre arXiv présents dans la fiche.
            mots = [w for w in titre_norm.split() if len(w) > 4]
            presents = sum(1 for w in mots if w in _norm(txt))
            ratio = presents / len(mots) if mots else 0
            check["coherence"] = round(ratio, 2)
            if ratio < 0.5:
                check["ok"] = False
                check["detail"] = f"titre arXiv « {titre} » peu cohérent avec la fiche (couverture {ratio:.0%})"
        res["checks"].append(check)

    res["ok"] = all(c["ok"] for c in res["checks"])
    return res


def main():
    ap = argparse.ArgumentParser(description="Vérification factuelle des sources.")
    ap.add_argument("paths", nargs="*", help="Fiches à vérifier.")
    ap.add_argument("--all", action="store_true", help="Vérifier tout le corpus.")
    ap.add_argument("--json", action="store_true", help="Sortie JSON.")
    args = ap.parse_args()

    if args.all:
        cibles = sorted(glob.glob(os.path.join(FICHES, "*.md")))
    elif args.paths:
        cibles = args.paths
    else:
        ap.error("fournir des fiches ou --all.")

    rapport = [verifier_fiche(p) for p in cibles]
    nb_ko = sum(1 for r in rapport if not r["ok"])

    if args.json:
        json.dump(rapport, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        for r in rapport:
            mark = "✅" if r["ok"] else "❌"
            sys.stdout.write(f"{mark} {r['slug']}\n")
            for c in r["checks"]:
                cm = "✅" if c["ok"] else "❌"
                sys.stdout.write(f"    {cm} {c['type']}: {c['detail']} [{c['ref']}]\n")
        sys.stdout.write(f"\n{nb_ko} fiche(s) en échec sur {len(cibles)}.\n")

    sys.exit(1 if nb_ko else 0)


if __name__ == "__main__":
    main()
