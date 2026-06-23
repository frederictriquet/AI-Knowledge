#!/usr/bin/env python3
"""Rappel court (one-liner) si des fiches outils sont à rafraîchir.

Pensé pour un hook **SessionStart** : n'imprime **rien** s'il n'y a rien à
signaler (sortie vide = pas de bruit). Réutilise la logique de `kb_staleness.py`
(pas de duplication) : périmé = « vérifié le » plus vieux que le seuil, ou absent.

Usage : python3 tools/kb_reminder.py   (seuil 90 j, fiches outils/ seulement)
"""
import os
import sys
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_staleness import extraire_date, cibles  # noqa: E402

SEUIL = 90


def main():
    today = datetime.date.today()
    perimes = non_dates = 0
    for path in cibles(False):  # fiches outils/ uniquement
        d = extraire_date(path)
        if d is None:
            non_dates += 1
        elif (today - d).days > SEUIL:
            perimes += 1
    n = perimes + non_dates
    if n:
        print(
            f"⚠️ KB — {n} fiche(s) outil à rafraîchir "
            f"({perimes} périmée(s) >{SEUIL} j, {non_dates} non datée(s)) "
            f"→ lance /kb:refresh"
        )


if __name__ == "__main__":
    main()
