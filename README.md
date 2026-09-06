# deinPlatz – Ablöse des Kernsystems (Kundenverwaltung & Transaktionen)

Arbeits- und Steuerungs-Repository für die Auswahl und Einführung eines neuen
Kernsystems für Kundenverwaltung, Mietverträge, Abrechnung und Zahlungen bei
**deinPlatz.at** (Self-Storage, Reitschulgasse 16, 9500 Villach).

> **Projektsprache: Deutsch.** Alle Dokumente, Commits und Auswertungen in diesem
> Repository werden auf Deutsch geführt.

## Zielsetzung

Innerhalb von **8 Wochen** wird das bestehende Kernsystem abgelöst:
Systemauswahl, Vertrag, Konfiguration, Datenmigration und Go-Live.
Leitprinzip: **Standard-SaaS statt Eigenentwicklung** – nur so ist der Zeitrahmen
realistisch (siehe [Projektauftrag](00_management/projektauftrag.md), Abschnitt „Leitplanken").

## Navigation

| Ordner | Inhalt |
| --- | --- |
| [`00_management/`](00_management/) | Projektauftrag, 8-Wochen-Plan, Governance, Risiken, Entscheidungen, Statusbericht |
| [`10_analyse/`](10_analyse/) | Ist-Aufnahme, Prozesslandkarte, Datenobjekte |
| [`20_anforderungen/`](20_anforderungen/) | Anforderungskatalog (MoSCoW), NFA, Rechtsrahmen Österreich |
| [`30_markt/`](30_markt/) | Marktüberblick, Longlist, Bewertungsmodell |
| [`40_auswahl/`](40_auswahl/) | RFP-Unterlagen, Demo-Skript, Bewertungsmatrix, Vertrags-Checkliste |
| [`50_umsetzung/`](50_umsetzung/) | Einführungsplan, Datenmigration, Test & Abnahme, Cutover, Schulung |
| [`90_quellen/`](90_quellen/) | Rechercheprotokoll und Quellenverzeichnis |
| [`werkzeuge/`](werkzeuge/) | Hilfsskripte (z. B. Erzeugung der Anforderungstabellen aus der CSV) |

## Aktueller Stand

| Punkt | Status |
| --- | --- |
| Repository initialisiert | ✅ erledigt |
| Marktrecherche (Desk Research) | ✅ Erstfassung, siehe [`30_markt/marktueberblick.md`](30_markt/marktueberblick.md) |
| Ist-Aufnahme beim Kunden | ⬜ offen – Workshop Woche 1 |
| Anforderungskatalog freigegeben | ⬜ Entwurf liegt vor, Freigabe Woche 2 |
| Anbieterentscheidung | ⬜ geplant Ende Woche 5 |
| Go-Live | ⬜ geplant Woche 8 |

## Wichtiger Hinweis zu den Annahmen

Alle Angaben zum Ist-Zustand von deinPlatz (bestehendes System, Anzahl Einheiten,
Kundenanzahl, Prozesse) sind bis zur Ist-Aufnahme **Annahmen**. Sie sind in den
Dokumenten mit `ANNAHME` gekennzeichnet und in Woche 1 zu verifizieren.
Öffentlich recherchierte Angaben sind in [`90_quellen/recherchequellen.md`](90_quellen/recherchequellen.md)
belegt.
