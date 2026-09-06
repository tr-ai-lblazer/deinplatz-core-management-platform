# Longlist und Screening

Datenbasis: [`anbieter.csv`](anbieter.csv) (führende Quelle) · Stand 06.09.2026

## Vorgehen

1. **Longlist (13 Einträge, Woche 2):** Alle Kandidaten, die grundsätzlich in Frage kommen –
   Fachsysteme (Weg A), generische Stacks (Weg B) sowie der bewusst dokumentierte
   Ausschluss Eigenbau (Weg C).
2. **K.o.-Screening (Woche 3):** Prüfung der als K.o. markierten Anforderungen aus
   [`../20_anforderungen/anforderungskatalog.md`](../20_anforderungen/anforderungskatalog.md)
   anhand der RFP-Antworten. Wer eines nicht erfüllt, scheidet aus – dokumentiert mit Begründung.
3. **Shortlist (3–4 Anbieter, Ende Woche 3):** nur diese bekommen einen Demo-Termin;
   mehr ist im Zeitrahmen nicht seriös bewertbar.

## Empfohlene Ansprache in Woche 2

| Priorität | Anbieter | Begründung |
| --- | --- | --- |
| 1 | Storeganise (A1) | Belegter Einsatz im DACH-Raum, deutschsprachiger Ansprechpartner, offene API für Zutritt und Zahlung |
| 2 | Kinnovis (A2) | Europäischer Anbieter mit vollständiger Automatisierungskette Buchung → Vertrag → Abrechnung → Portal |
| 3 | selfstorage.team (A4) | DACH-Ausrichtung; interessant, weil ergänzende Dienstleistungen den Personalengpass eines Kleinbetriebs adressieren |
| 4 | Stora (A3) | Funktional stark und schnell einführbar; K.o.-Fragen zu Sprache/SEPA/AT-Rechnung vorab klären |
| 5 | 6Storage (A6) | Breite Zutrittsintegrationen, günstiger Einstieg; gleiche K.o.-Vorprüfung |
| 6 | Zoho One (B1) *oder* Odoo (B2) | Ein Vergleichsangebot aus Weg B, damit die Entscheidung nicht nur innerhalb einer Produktkategorie getroffen wird |

Nicht angesprochen werden zunächst A5, A7, A8 und B4 (Begründung in `anbieter.csv`).
Sie bleiben als Reserve, falls die Rückläufer zu dünn sind.

## K.o.-Screening-Bogen (je Anbieter auszufüllen)

| K.o.-Kriterium | Anforderung | erfüllt? | Beleg/Quelle |
| --- | --- | --- | --- |
| Deutschsprachige Oberfläche | ADM-07 | ⬜ | |
| Deutschsprachige Kundentexte und Vorlagen | KOM-03, BUC-04 | ⬜ | |
| Deutschsprachiger Support mit Reaktionszeiten | ADM-08 | ⬜ | |
| Ein Kunde mit mehreren Verträgen/Einheiten | KUN-02 | ⬜ | |
| Alle Einheitentypen und -größen abbildbar | OBJ-01 | ⬜ | |
| Vertragsvorlagen selbst pflegbar | VER-01 | ⬜ | |
| Statusgesteuerte Folgeprozesse | VER-03 | ⬜ | |
| Rabatt-/Aktionslogik mit automatischem Auslaufen | PRI-02 | ⬜ | |
| Automatischer wiederkehrender Abrechnungslauf | ABR-01 | ⬜ | |
| Taggenaue anteilige Abrechnung | ABR-02 | ⬜ | |
| Österreichkonforme Rechnung inkl. USt.-Ausweis | ABR-03 | ⬜ | |
| SEPA-Lastschrift inkl. Mandatsverwaltung und Rückläufern | ABR-04 | ⬜ | |
| Automatischer Zahlungsabgleich / offene Posten | ABR-06 | ⬜ | |
| Regelbasiertes Mahnwesen | MAH-01 | ⬜ | |
| Buchhaltungsexport im Format der Steuerberatung | BUH-01 | ⬜ | |
| Unveränderbarkeit versendeter Belege | BUH-03 | ⬜ | |
| AVV nach Art. 28 DSGVO, Hosting EU | ADM-03 | ⬜ | |
| Vollständiger Datenexport durch den Kunden | ADM-05 | ⬜ | |

**Ergebnis:** ⬜ Shortlist · ⬜ ausgeschieden – Begründung: ______________________

## Screening-Ergebnis (wird in Woche 3 ausgefüllt)

| Anbieter | K.o. erfüllt | Shortlist | Begründung |
| --- | --- | --- | --- |
| Storeganise | | | |
| Kinnovis | | | |
| selfstorage.team | | | |
| Stora | | | |
| 6Storage | | | |
| Weg B (Vergleichsangebot) | | | |
