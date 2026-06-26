#!/usr/bin/env python3
"""Signale les fiches-outils dont la date de vérification de source est ancienne ou absente.

Chaque fiche-outil (`fiches outils/*.md`) se termine par une section « ## Source »
dont une ligne porte une date du type *(vérifié le AAAA-MM-JJ)*. Cet outil :
  - extrait cette date par regex `vérifié le (\\d{4}-\\d{2}-\\d{2})` ;
  - calcule son âge en jours par rapport à aujourd'hui (ou `--today` pour des runs
    reproductibles) ;
  - range chaque fiche dans trois catégories :
      PÉRIMÉ   — date plus ancienne que le seuil (`--days`, défaut 90) ;
      NON DATÉ — aucune date de vérification trouvée ;
      OK       — date présente et récente (compté seulement).

Outil purement informatif : code de sortie toujours 0.

Usage :
    python3 tools/kb_staleness.py                          # seuil 90 j, date du jour
    python3 tools/kb_staleness.py --days 30                # seuil personnalisé
    python3 tools/kb_staleness.py --today 2026-06-17       # date de référence figée
    python3 tools/kb_staleness.py --all                    # inclut aussi fiches/
"""
import os
import re
import glob
import argparse
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
FICHES_OUTILS = os.path.join(WIKI, "fiches outils")
FICHES = os.path.join(WIKI, "fiches")

DATE_RE = re.compile(r"vérifié le (\d{4}-\d{2}-\d{2})")


def extraire_date(path):
    """Retourne la date de vérification (datetime.date) ou None si absente/illisible."""
    txt = open(path, encoding="utf-8", errors="replace").read()
    m = DATE_RE.search(txt)
    if not m:
        return None
    try:
        return datetime.date.fromisoformat(m.group(1))
    except ValueError:
        return None


def cibles(inclure_concepts):
    """Liste des fiches à analyser, hors _TEMPLATE.md."""
    paths = glob.glob(os.path.join(FICHES_OUTILS, "*.md"))
    if inclure_concepts:
        paths += glob.glob(os.path.join(FICHES, "*.md"))
    return sorted(p for p in paths if os.path.basename(p) != "_TEMPLATE.md")


def main():
    ap = argparse.ArgumentParser(
        description="Signale les fiches dont la vérification de source est ancienne ou absente."
    )
    ap.add_argument("--days", type=int, default=90,
                    help="Seuil de péremption en jours (défaut : 90).")
    ap.add_argument("--today", metavar="AAAA-MM-JJ",
                    help="Date de référence figée (pour des runs reproductibles).")
    ap.add_argument("--all", action="store_true",
                    help="Analyser aussi les fiches concepts (fiches/).")
    args = ap.parse_args()

    if args.today:
        try:
            aujourdhui = datetime.date.fromisoformat(args.today)
        except ValueError:
            ap.error(f"--today mal formé : « {args.today} » (attendu AAAA-MM-JJ).")
    else:
        aujourdhui = datetime.date.today()

    perimes = []      # (chemin, date, age_jours)
    non_dates = []    # chemins
    nb_ok = 0

    for path in cibles(args.all):
        d = extraire_date(path)
        if d is None:
            non_dates.append(path)
            continue
        age = (aujourdhui - d).days
        if age > args.days:
            perimes.append((path, d, age))
        else:
            nb_ok += 1

    total = len(perimes) + len(non_dates) + nb_ok

    print(f"Vérification de fraîcheur — référence {aujourdhui.isoformat()}, "
          f"seuil {args.days} j, {total} fiche(s) analysée(s).\n")

    perimes.sort(key=lambda t: t[1])  # plus anciennes d'abord
    if perimes:
        print(f"PÉRIMÉ ({len(perimes)}) — plus vieux que {args.days} j :")
        for path, d, age in perimes:
            print(f"  {os.path.relpath(path, ROOT)} — {d.isoformat()} — {age} j")
        print()

    if non_dates:
        print(f"NON DATÉ ({len(non_dates)}) — aucune date « vérifié le » trouvée :")
        for path in sorted(non_dates):
            print(f"  {os.path.relpath(path, ROOT)}")
        print()

    print(f"Résumé : {nb_ok} OK · {len(perimes)} périmé(s) · "
          f"{len(non_dates)} non daté(s) sur {total} fiche(s).")


if __name__ == "__main__":
    main()
