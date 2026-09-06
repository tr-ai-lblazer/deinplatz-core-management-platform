#!/usr/bin/env python3
"""Erzeugt die Markdown-Tabellen des Anforderungskatalogs aus anforderungen.csv.

Aufruf:  python3 werkzeuge/anforderungen_tabelle.py

Die CSV ist die fuehrende Quelle. Im Katalog werden die Bereiche zwischen
<!-- TABELLE:<DOMAENENKUERZEL> --> und <!-- ENDE --> ersetzt.
"""
import csv
import pathlib
import re
import sys

BASIS = pathlib.Path(__file__).resolve().parent.parent
CSV_PFAD = BASIS / "20_anforderungen" / "anforderungen.csv"
KATALOG = BASIS / "20_anforderungen" / "anforderungskatalog.md"


def lade_anforderungen():
    with CSV_PFAD.open(encoding="utf-8", newline="") as datei:
        return list(csv.DictReader(datei, delimiter=";"))


def tabelle(zeilen):
    kopf = "| ID | Anforderung | Prioritaet | K.o. | Prueffrage an den Anbieter |\n"
    kopf += "| --- | --- | --- | --- | --- |\n"
    zellen = []
    for z in zeilen:
        ko = "**ja**" if z["KO"].strip().lower() == "ja" else "–"
        zellen.append(
            f'| {z["ID"]} | {z["Anforderung"]} | {z["Prioritaet"]} | {ko} | {z["Prueffrage an den Anbieter"]} |'
        )
    return kopf + "\n".join(zellen) + "\n"


def main():
    anforderungen = lade_anforderungen()
    inhalt = KATALOG.read_text(encoding="utf-8")
    fehlend = []
    for kuerzel in sorted({a["ID"].split("-")[0] for a in anforderungen}):
        marker = f"<!-- TABELLE:{kuerzel} -->"
        if marker not in inhalt:
            fehlend.append(kuerzel)
            continue
        zeilen = [a for a in anforderungen if a["ID"].startswith(kuerzel + "-")]
        muster = re.compile(re.escape(marker) + r".*?<!-- ENDE -->", re.DOTALL)
        inhalt = muster.sub(marker + "\n" + tabelle(zeilen) + "<!-- ENDE -->", inhalt)
    KATALOG.write_text(inhalt, encoding="utf-8")
    print(f"{len(anforderungen)} Anforderungen in den Katalog geschrieben.")
    if fehlend:
        print("Kein Marker im Katalog fuer: " + ", ".join(fehlend), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
