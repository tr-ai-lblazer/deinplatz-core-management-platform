# Projektauftrag: Ablöse Kernsystem deinPlatz

| Feld | Inhalt |
| --- | --- |
| Projektname | Ablöse Kernsystem Kundenverwaltung & Transaktionen |
| Auftraggeber | Geschäftsführung deinPlatz.at, Villach |
| Projektleitung | *(zu benennen)* |
| Beratung/Umsetzung | accilium |
| Laufzeit | 8 Wochen ab Kick-off |
| Version | 0.1 (Entwurf, Stand 06.09.2026) |

## 1. Ausgangslage

deinPlatz.at betreibt einen Self-Storage-Standort in Villach (Reitschulgasse 16, Gewerbegebiet
Seebach) mit Lagerabteilen von rund 2,5 bis 50 m², 24/7-Zutritt, Videoüberwachung,
Zutrittskontrolle und Facility Manager vor Ort. Die Mindestmietdauer beträgt einen Monat,
die Konditionen sind bewusst flexibel gehalten
(Quelle: öffentliche Unternehmensangaben, siehe `90_quellen/recherchequellen.md`).

Das heute eingesetzte Kernsystem für Kundenverwaltung und Transaktionen (Verträge, Rechnungen,
Zahlungen, Mahnwesen) soll abgelöst werden.

> `ANNAHME:` Heute wird eine Kombination aus Insellösungen genutzt (Tabellenkalkulation für
> Belegung/Kundenliste, separates Fakturierungs- oder Kassensystem, manuelle Bankabgleiche,
> eigenständige Zutrittskontrolle). Der konkrete Ist-Zustand ist in Woche 1 zu erheben
> (siehe `10_analyse/ist_aufnahme_leitfaden.md`).

## 2. Projektziele

1. **Ein führendes System** für Kunden, Einheiten, Verträge, Abrechnung und Zahlungen –
   Ende der Doppelerfassung.
2. **Automatisierte wiederkehrende Abrechnung** inklusive SEPA-Lastschrift/Kartenzahlung,
   automatischer Rechnungslegung und automatisiertem Mahnwesen.
3. **Digitale Kundenstrecke**: Online-Reservierung/-Buchung, digitale Vertragsunterzeichnung,
   Selbstbedienungsportal für Kundinnen und Kunden.
4. **Rechtssichere Abwicklung in Österreich** (RKSV/Belegerteilung soweit einschlägig, DSGVO,
   Aufbewahrungspflichten, saubere Übergabe an die Steuerberatung).
5. **Verwertbare Kennzahlen**: Belegungsgrad, Umsatz je m², Kündigungsquote, Außenstände.
6. **Go-Live innerhalb von 8 Wochen** ohne Unterbrechung des laufenden Betriebs.

## 3. Nicht-Ziele (bewusst außerhalb des Projektumfangs)

- Neubau der Unternehmenswebsite über die Buchungsstrecke des neuen Systems hinaus.
- Austausch der physischen Zutrittskontroll-Hardware (nur Anbindung wird betrachtet).
- Ablöse der Finanzbuchhaltung bei der Steuerberatung.
- Individualentwicklung eines eigenen Systems.
- Standortexpansion/Mandantenaufbau – wird nur als Skalierungsanforderung berücksichtigt.

## 4. Leitplanken für die Lösungsauswahl

| Nr. | Leitplanke | Begründung |
| --- | --- | --- |
| L1 | Standard-SaaS, Konfiguration statt Programmierung | 8 Wochen lassen keine Entwicklung zu |
| L2 | Deutschsprachige Bedienoberfläche und deutschsprachiger Support | Team- und Kundenakzeptanz in Kärnten |
| L3 | Euro, österreichische USt., SEPA-Lastschrift, AT-Rechnungsanforderungen | Betrieb in Österreich |
| L4 | Offene Schnittstellen (API/Webhooks) zu Zutrittskontrolle, Payment, Buchhaltung | Automatisierungsgrad ist der eigentliche Nutzen |
| L5 | Datenexport jederzeit vollständig möglich | Vermeidung eines neuen Lock-ins |
| L6 | Gesamtkosten (TCO) über 3 Jahre transparent bewertet | Kleinbetrieb, Fixkostensensibilität |

## 5. Erfolgskriterien (messbar)

| Kriterium | Zielwert | Messung |
| --- | --- | --- |
| Go-Live | Ende Woche 8 | Produktivsetzung abgenommen |
| Migrierte aktive Verträge | 100 % | Abgleich Altsystem ↔ Neusystem |
| Migrationsfehlerquote nach Abnahme | < 1 % der Datensätze | Stichprobe 50 Verträge + Summenabgleich |
| Anteil automatisch eingezogener Mieten | ≥ 80 % innerhalb 4 Wochen nach Go-Live | Zahlungsreport |
| Manueller Aufwand Monatsfakturierung | < 1 Stunde/Monat (vorher: `ANNAHME` 1 Tag) | Zeitmessung |
| Erstellte Rechnungen ohne Nacharbeit | ≥ 95 % | Reklamationsquote |

## 6. Budgetrahmen

`ANNAHME:` noch nicht freigegeben. Kalkulationsbasis für die Marktansprache:

| Position | Bandbreite (indikativ) |
| --- | --- |
| Software-Lizenz/SaaS p. a. | 1.500 – 6.000 € |
| Einmalige Einrichtung/Setup durch Anbieter | 0 – 3.000 € |
| Datenmigration (extern/intern) | 1.000 – 5.000 € |
| Zahlungsdienstleister (transaktionsabhängig) | ca. 0,35 – 1,5 % vom Umsatz |
| Projektbegleitung/Beratung | nach Aufwand |

Verbindliche Zahlen entstehen erst mit den Angeboten (Woche 4/5) und werden in
`40_auswahl/bewertungsmatrix.csv` geführt.

## 7. Freigabe

| Rolle | Name | Datum | Freigabe |
| --- | --- | --- | --- |
| Auftraggeber (GF) | | | ⬜ |
| Projektleitung | | | ⬜ |
| Beratung | | | ⬜ |
