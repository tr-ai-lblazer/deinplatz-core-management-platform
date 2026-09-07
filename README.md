# deinPlatz – Ablöse des Kernsystems (Kundenverwaltung & Transaktionen)

Arbeits- und Steuerungs-Repository für die Auswahl und Einführung eines neuen
Kernsystems für Kundenverwaltung, Mietverträge, Abrechnung und Zahlungen bei
**deinPlatz.at** (Self-Storage, Reitschulgasse 16, 9500 Villach).

> **Projektsprache: Deutsch.** Alle Dokumente, Commits und Auswertungen in diesem
> Repository werden auf Deutsch geführt.

## Zielsetzung

Auswahl, Vertrag, Konfiguration und Datenmigration in acht Wochen, **Go-Live am 1. November 2026**;
danach eine Absicherungsphase, in der Zoho bis zum Jahreswechsel als Vergleichs- und Rückfallstand
verfügbar bleibt, und der Sundown des Altsystems im Januar 2027.
Leitprinzip: **Standard-SaaS statt Eigenentwicklung** – nur so ist der Zeitrahmen
realistisch (siehe [Projektauftrag](00_management/projektauftrag.md), Abschnitt „Leitplanken").

## Projektmanagement über GitHub

Das gesamte Projektmanagement läuft über dieses Repository: **Aufgaben, Entscheidungsbedarf,
Risiken und Anbieterfragen werden als GitHub-Issues geführt**, Ergebnisse als Dateien abgelegt.
Wie wir arbeiten – Issues, Labels, Meilensteine, Board, Branches, Pull Requests – steht in
[`CONTRIBUTING.md`](CONTRIBUTING.md).

| Person | Rolle |
| --- | --- |
| Peter | Projektleitung, Steuerberatung und Bank |
| Martin | Umsetzung, Repository, Anbieterkoordination |
| Martina | Fachverantwortung Betrieb, Cutover und Archivierung |
| accilium | Beratung |

Einstiegspunkte: [Issue-Vorlagen](.github/ISSUE_TEMPLATE) · [Labelschema](.github/labels.md) ·
[Protokolle](00_management/protokolle/)

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
| [`.github/`](.github/) | Issue- und PR-Vorlagen, Labelschema, CODEOWNERS |

## Aktueller Stand

| Punkt | Status |
| --- | --- |
| Repository initialisiert | ✅ erledigt |
| Marktrecherche (Desk Research) | ✅ Erstfassung, siehe [`30_markt/marktueberblick.md`](30_markt/marktueberblick.md) |
| Ist-Zustand Bestandssystem | ✅ Zoho Subscriptions dokumentiert ([`10_analyse/ist_zustand_zoho.md`](10_analyse/ist_zustand_zoho.md)), Detailerhebung Woche 1 offen |
| Anforderungskatalog | ✅ Version 0.2 mit Phasen 1/2 aus dem Kundendokument, Freigabe Woche 2 |
| Shortlist | ✅ Kinnovis, Stora und Store365 (Store-IT), Benchmark liegt vor ([`30_markt/benchmark_kinnovis_stora_store365.md`](30_markt/benchmark_kinnovis_stora_store365.md)) |
| Migrationskonzept Zoho | ✅ Entwurf ([`50_umsetzung/migration_zoho.md`](50_umsetzung/migration_zoho.md)); Mandatsfrage offen |
| Projektplan mit Terminen | ✅ Go-Live **So 01.11.2026**, danach Parallelbetrieb bis Jahreswechsel; Word-Fassung in [`00_management/projektplan_umstellung_kernsystem.docx`](00_management/projektplan_umstellung_kernsystem.docx) |
| Stakeholder-Termin 07.09.2026 | ✅ [Protokoll](00_management/protokolle/2026-09-07_stakeholder_termin.md) mit Beschlüssen B1–B6 |
| Anbieterentscheidung | ⬜ **spätestens Fr 09.10.2026** (M5); Kinnovis ist erster Demo-Kandidat (E-10) |
| Offen und terminkritisch | ⬜ Übergang der SEPA-Mandate und der Gläubiger-ID auf die GmbH (O-12, KW 38) |
| Go-Live | ⬜ geplant Woche 8 |

## Wichtiger Hinweis zu den Annahmen

Bestätigt sind inzwischen: Zoho Subscriptions als Bestandssystem, SEPA-Einzug über das eigene
Bankkonto mit eigener Gläubiger-ID, rund 250 aktive Kundinnen und Kunden, RZL bei der
Steuerberatung sowie der geplante Wechsel zur GmbH. Weitere Angaben zum Ist-Zustand
(Anzahl Einheiten, Belegung, Zutrittsanlage) sind bis zur Ist-Aufnahme **Annahmen**. Sie sind in den
Dokumenten mit `ANNAHME` gekennzeichnet und in Woche 1 zu verifizieren.
Öffentlich recherchierte Angaben sind in [`90_quellen/recherchequellen.md`](90_quellen/recherchequellen.md)
belegt.
