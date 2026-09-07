# 8-Wochen-Plan: Auswahl und Einführung

Stand: 07.09.2026 · Version 0.3 · **Projektstart Mo 07.09.2026, Go-Live So 01.11.2026**

> **Geändert nach dem Stakeholder-Termin vom 07.09.2026 (Beschlüsse B2/B3):** Der Go-Live liegt
> auf dem **1. November**; danach folgt eine Absicherungsphase, in der Zoho als Vergleichs- und
> Rückfallstand verfügbar bleibt – bis zum Jahreswechsel, längstens bis Januar 2027.
> Regeln dazu: [`../50_umsetzung/parallelbetrieb_und_sundown.md`](../50_umsetzung/parallelbetrieb_und_sundown.md).

> **Ausführliche Fassung für die Geschäftsführung:** [`projektplan_umstellung_kernsystem.docx`](projektplan_umstellung_kernsystem.docx)
> – mit Meilensteinen samt spätesten Terminen, kritischem Pfad, Balkenplan, Rückwärtsrechnung,
> Ressourcen, Rückfallebenen und Cutover-Tagesplan.

## Kalenderzuordnung

| Woche | Kalenderwoche | Zeitraum | Meilenstein am Freitag |
| --- | --- | --- | --- |
| W1 | KW 37 | 07.–11.09.2026 | M1 Ist-Bild und Projektauftrag |
| W2 | KW 38 | 14.–18.09.2026 | M2 Anforderungen freigegeben, Anbieter angefragt |
| W3 | KW 39 | 21.–25.09.2026 | M3 Demos und RZL-Testimport |
| W4 | KW 40 | 28.09.–02.10.2026 | M4 Angebote bewertet |
| W5 | KW 41 | 05.–09.10.2026 | **M5 Anbieter beauftragt – kritischster Termin** |
| W6 | KW 42 | 12.–16.10.2026 | M6 Konfiguration und Migrationstest 1 |
| W7 | KW 43 | 19.–23.10.2026 | M7 Abnahme und Go-/No-Go |
| W8 | KW 44 | 26.–30.10.2026 | Datenübernahme und Freigabe |
| — | KW 45 | **01.11.2026** | **M8 Go-Live** (Stichtag Sonntag, operativer Start Mo 02.11.) |
| — | Nov/Dez | bis 31.12.2026 | M9 Parallelbetrieb, drei Abgleichtermine |
| — | Januar | bis 31.01.2027 | M10 Sundown Zoho und Langzeitarchivierung |

**Kalenderbesonderheiten:** Montag, 26.10.2026 ist Nationalfeiertag; Sonntag, 01.11.2026 ist
Allerheiligen. Der Cutover läuft daher Di 27.10. bis Fr 30.10. (Migration, Abgleich, Freigabe,
Datenannahmestopp in Zoho), der **Stichtag ist der 01.11.**, der operative Start Montag, 02.11.
Der erste Abrechnungslauf für November erfolgt in der Woche ab 02.11. im Vier-Augen-Prinzip.

## Phasenlogik

```
W1        W2        W3        W4        W5        W6        W7        W8
|--Analyse & Anforderungen--|--Markt & Demos--|-Entsch.-|--Konfiguration & Migration--|-Go-Live-|
```

Die Auswahl ist bewusst auf 5 Wochen komprimiert; parallelisiert wird, indem die
Anbieteransprache (RFP-Versand) bereits am Ende von Woche 2 startet, während der
Anforderungskatalog noch final abgestimmt wird.

## Woche 1 – Ist-Aufnahme und Zielbild

| # | Arbeitspaket | Ergebnis | Verantwortlich |
| --- | --- | --- | --- |
| 1.1 | Kick-off mit Geschäftsführung, Rollen und Entscheidungswege festlegen | Projektauftrag freigegeben | PL |
| 1.2 | Ist-Aufnahme Prozesse (Anfrage → Vertrag → Abrechnung → Kündigung) | `10_analyse/prozesslandkarte.md` gefüllt | Beratung |
| 1.3 | Ist-Aufnahme Systeme, Daten, Schnittstellen, Verträge/Kündigungsfristen Altsystem | Systemsteckbrief | Beratung |
| 1.4 | Datenqualitäts-Check auf Basis eines Testexports | Bewertung Migrationsaufwand | Beratung |
| 1.5 | Zielbild und Priorisierung (Was muss am Tag 1 laufen?) | Scope-Abgrenzung | PL + GF |

**Meilenstein M1 (Ende W1):** Ist-Bild und Zielbild abgestimmt.

## Woche 2 – Anforderungen und Marktansprache

| # | Arbeitspaket | Ergebnis | Verantwortlich |
| --- | --- | --- | --- |
| 2.1 | Anforderungskatalog finalisieren (MoSCoW, Gewichtung) | `20_anforderungen/anforderungskatalog.md` freigegeben | Beratung + GF |
| 2.2 | Rechts-/Steuerfragen an Steuerberatung übergeben (RKSV, Belege, Gebühren, Archivierung) | Klärungsliste beantwortet | PL |
| 2.3 | Longlist verdichten, Anbieter kontaktieren, RFP versenden | 5–7 Anbieter angeschrieben | Beratung |
| 2.4 | Bewertungsmodell und Gewichtung beschließen | `30_markt/bewertungsmodell.md` freigegeben | GF |

**Meilenstein M2 (Ende W2):** Anforderungskatalog freigegeben, RFP versendet.

## Woche 3 – Screening und erste Demos

| # | Arbeitspaket | Ergebnis | Verantwortlich |
| --- | --- | --- | --- |
| 3.1 | Rückläufer sichten, K.o.-Kriterien prüfen | Longlist → Shortlist (3–4) | Beratung |
| 3.2 | Demo-Termine terminieren, Demo-Skript versenden | Termine fixiert | PL |
| 3.3 | Demos Teil 1 (2 Anbieter) entlang `40_auswahl/demo_skript.md` | Bewertungsbögen | Team |
| 3.4 | Referenzkunden im DACH-Raum anfragen | 2 Referenzgespräche terminiert | Beratung |

**Meilenstein M3 (Ende W3):** Shortlist steht.

## Woche 4 – Demos, Referenzen, Angebote

| # | Arbeitspaket | Ergebnis | Verantwortlich |
| --- | --- | --- | --- |
| 4.1 | Demos Teil 2 (restliche Anbieter), immer mit echtem Testfall | Bewertungsbögen vollständig | Team |
| 4.2 | Referenzgespräche führen (Fokus: Migration, Support, versteckte Kosten) | Gesprächsnotizen | Beratung |
| 4.3 | Angebote inkl. TCO 3 Jahre einholen und normalisieren | `40_auswahl/bewertungsmatrix.csv` gefüllt | Beratung |
| 4.4 | Migrationsprobe: Testexport an favorisierte Anbieter geben | Machbarkeitsaussage je Anbieter | Beratung |

**Meilenstein M4 (Ende W4):** Bewertete Angebote liegen vor.

## Woche 5 – Entscheidung und Vertrag

| # | Arbeitspaket | Ergebnis | Verantwortlich |
| --- | --- | --- | --- |
| 5.1 | Bewertung konsolidieren, Empfehlung mit Begründung | Entscheidungsvorlage | Beratung |
| 5.2 | Entscheidung der Geschäftsführung | Eintrag im Entscheidungslog | GF |
| 5.3 | Verhandlung (Preis, Laufzeit, Kündigungsfrist, SLA, Datenexport, AVV nach Art. 28 DSGVO) | Vertrag unterschrieben | GF + Beratung |
| 5.4 | Kündigung/Auslaufplanung Altsystem prüfen (Fristen!) | Kündigungstermin gesetzt | PL |

**Meilenstein M5 (Ende W5):** Anbieter beauftragt. *Kritischster Termin des Projekts.*

## Woche 6 – Konfiguration und Datenmigration (Testlauf)

| # | Arbeitspaket | Ergebnis | Verantwortlich |
| --- | --- | --- | --- |
| 6.1 | System aufsetzen: Mandant, Standort, Flächenplan/Einheiten, Preisliste, Steuersätze | Konfigurierte Testumgebung | Anbieter + PL |
| 6.2 | Vorlagen: Mietvertrag, Rechnung, Mahnstufen, E-Mail-Texte | Dokumentvorlagen abgenommen | GF + Beratung |
| 6.3 | Zahlungsanbindung (SEPA-Lastschrift/Karte) einrichten und im Testmodus prüfen | Testzahlungen erfolgreich | PL |
| 6.4 | Migration Testlauf 1 inkl. Abgleichprotokoll | `50_umsetzung/datenmigration.md` Protokoll | Beratung |
| 6.5 | Schnittstellen Zutrittskontrolle und Buchhaltungsexport klären/anbinden | Integrationsstatus | Beratung |

**Meilenstein M6 (Ende W6):** Testumgebung fachlich vollständig, Migration technisch machbar.

## Woche 7 – Test, Abnahme, Schulung

| # | Arbeitspaket | Ergebnis | Verantwortlich |
| --- | --- | --- | --- |
| 7.1 | Testfälle durchspielen (`50_umsetzung/test_und_abnahme.md`) | Testprotokoll, Fehlerliste | Team |
| 7.2 | Fehlerbehebung mit Anbieter, Nachtest | Restpunkte klassifiziert | PL |
| 7.3 | Migration Testlauf 2 mit aktuellem Datenstand | Abgleich sauber | Beratung |
| 7.4 | Schulung des Teams (2 × 2 h) + Kurzanleitungen | Schulungsunterlagen | Beratung |
| 7.5 | Kundenkommunikation vorbereiten (neue Zahlungsart, Portal, SEPA-Mandate) | Anschreiben freigegeben | GF |

**Meilenstein M7 (Ende W7):** Abnahme erteilt, Go-/No-Go-Entscheidung.

## Woche 8 – Cutover, Go-Live, Hypercare

| # | Arbeitspaket | Ergebnis | Verantwortlich |
| --- | --- | --- | --- |
| 8.1 | Datenannahmestopp im Altsystem, finale Migration | Produktivdaten im Neusystem | Beratung |
| 8.2 | Go-Live: Verträge, Abrechnung und Zahlungen produktiv | Betrieb umgestellt | alle |
| 8.3 | Erster Abrechnungslauf begleitet, Ergebnis geprüft | Rechnungen versendet | PL |
| 8.4 | Hypercare (tägliches Kurz-Standup, Fehlerliste) | Stabiler Betrieb | alle |
| 8.5 | Projektabschluss: Doku, offene Punkte, Archivierung Altsystem | Abschlussbericht | Beratung |

**Meilenstein M8 (Ende W8):** Produktivbetrieb, Projektabschluss.

## Kritischer Pfad

`Ist-Aufnahme → Anforderungen → RFP → Demos → Entscheidung (W5) → Migration → Go-Live`

Jede Verzögerung der Entscheidung in Woche 5 verschiebt den Go-Live 1:1. Puffer existiert
praktisch nur in Woche 3/4 (Demo-Terminierung). Deshalb: Anbietertermine bereits in Woche 2
vorreservieren.

## Rückfallebene

Drei abgestufte Stufen, ausführlich in der Word-Fassung (Kapitel 12): Umfang reduzieren und
Termin halten · Cutover auf den Monatswechsel November/Dezember verschieben (Go-Live 25.11.) ·
Abrechnung eines Monats übergangsweise getrennt führen.

Wenn M5 nicht bis Ende Woche 5 (Fr 09.10.) erreicht wird, wird der Umfang für den Go-Live reduziert:
Zuerst gehen Kundenstamm, Verträge und Abrechnung produktiv; Online-Buchungsstrecke,
Zutrittskontroll-Integration und Reporting folgen in einer zweiten Welle
(Wochen 9–12). Diese Entscheidung trifft die Geschäftsführung, sie wird im Entscheidungslog dokumentiert.
