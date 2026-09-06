# Test und Abnahme (Woche 7)

Getestet wird durch die Personen, die später damit arbeiten – nicht durch den Anbieter und nicht
durch die Beratung allein. Jeder Testfall wird mit echten, aber unkritischen Daten in der
Testumgebung durchgespielt.

## Fehlerklassen

| Klasse | Definition | Wirkung auf den Go-Live |
| --- | --- | --- |
| A | Betrieb nicht möglich (keine Abrechnung, kein Vertrag, kein Zutritt, falsche Beträge) | Go-Live blockiert |
| B | Erhebliche Einschränkung, Workaround aufwendig | Go-Live nur mit dokumentiertem Workaround und Termin zur Behebung |
| C | Schönheitsfehler, Komfortfunktion | Nachlaufliste |

## Testfälle

| Nr. | Testfall | Erwartetes Ergebnis | Klasse bei Fehler | Status |
| --- | --- | --- | --- | --- |
| T01 | Neuen Privatkunden anlegen und Vertrag über 12 m² ab dem 1. des Folgemonats abschließen | Vertrag, PDF, Willkommensmail, Zutritt aktiv | A | ⬜ |
| T02 | Firmenkunde mit UID, abweichender Rechnungsanschrift, zwei Einheiten | Eine Rechnung mit zwei Positionen, korrekte UID-Angaben | A | ⬜ |
| T03 | Einzug am 17. des Monats | Anteilige Miete taggenau korrekt berechnet | A | ⬜ |
| T04 | Aktion „1 Monat gratis bei 12 Monaten Bindung" | Monat 1 = 0 €, ab Monat 2 voller Preis, Aktion endet automatisch | A | ⬜ |
| T05 | Monatlicher Abrechnungslauf für alle aktiven Verträge | Alle Rechnungen korrekt, fortlaufende Nummerierung, Versand protokolliert | A | ⬜ |
| T06 | SEPA-Einzug im Testmodus | Einzugsdatei/Provider-Auftrag korrekt, Vorabinformation versendet | A | ⬜ |
| T07 | Rücklastschrift | Zahlung storniert, Spesen verrechnet, Mahnstufe ausgelöst | A | ⬜ |
| T08 | Mahnlauf Stufe 1 bis 3 | Fristen, Texte und Spesen korrekt; Zutrittssperre bei definierter Stufe | A | ⬜ |
| T09 | Zahlungseingang nach Mahnung | Offener Posten ausgeglichen, Sperre aufgehoben | A | ⬜ |
| T10 | Teilzahlung | Korrekte Zuordnung, Restforderung sichtbar | B | ⬜ |
| T11 | Umzug in eine größere Einheit zum Monatswechsel | Alter Vertrag beendet, neuer Vertrag aktiv, Abrechnung stimmig | B | ⬜ |
| T12 | Kündigung zum Monatsende inkl. Endabrechnung und Kautionsrückzahlung | Endabrechnung korrekt, Einheit wieder frei, Zutritt entzogen | A | ⬜ |
| T13 | Rechnungskorrektur (Storno und Gutschrift) | Ursprungsbeleg unverändert, Gutschrift korrekt nummeriert | A | ⬜ |
| T14 | Zusatzleistung Versicherung und Warenverkauf (Schloss) auf einer Rechnung | Korrekte Steuersätze und Erlöskonten | A | ⬜ |
| T15 | Barzahlung mit Belegausgabe (falls einschlägig) | Beleg korrekt, Kassenlogik entsprechend Prüfauftrag P1 | A | ⬜ |
| T16 | Buchhaltungsexport eines Monats | Von der Steuerberatung geprüft und akzeptiert | A | ⬜ |
| T17 | Berichte: Belegung, Umsatz je m², offene Posten | Werte stimmen mit Stichprobe überein, Export nach Excel funktioniert | B | ⬜ |
| T18 | Online-Buchung inkl. Zahlung (falls im Go-Live-Umfang) | Vertrag entsteht vollständig ohne manuelles Zutun | B | ⬜ |
| T19 | Kundenportal: Rechnung einsehen, Zahlungsart ändern | Funktioniert und ist deutschsprachig | C | ⬜ |
| T20 | Rolle „Facility Manager" | Sieht Verträge und Zutritt, keine Umsatzauswertungen | B | ⬜ |
| T21 | Änderungsprotokoll eines Vertrags | Änderung mit Benutzer und Zeitstempel nachvollziehbar | B | ⬜ |
| T22 | Vollständiger Datenexport | Alle Objekte exportierbar, Datei lesbar | B | ⬜ |
| T23 | Bedienung auf dem Tablet vor Ort | Vertragsabschluss mobil möglich | B | ⬜ |
| T24 | Migrationsabgleich nach Testlauf 2 | Alle Kriterien aus `datenmigration.md` erfüllt | A | ⬜ |

## Fehlerliste (laufend)

| Nr. | Testfall | Beschreibung | Klasse | Gemeldet am | Anbieter-Status | Behoben am |
| --- | --- | --- | --- | --- | --- | --- |

## Abnahmeerklärung (Meilenstein M7)

Die Abnahme wird erteilt, wenn:

- [ ] alle Testfälle der Klasse A fehlerfrei durchlaufen sind,
- [ ] alle Fehler der Klasse B entweder behoben oder mit dokumentiertem Workaround und
      verbindlichem Behebungstermin akzeptiert sind,
- [ ] die Migrationskriterien erfüllt sind,
- [ ] der Buchhaltungsexport von der Steuerberatung akzeptiert wurde,
- [ ] das Team geschult ist und die Kurzanleitungen vorliegen.

| Rolle | Name | Datum | Abnahme |
| --- | --- | --- | --- |
| Fachverantwortung Betrieb | | | ⬜ |
| Fachverantwortung Finanzen | | | ⬜ |
| Projektleitung | | | ⬜ |
| Geschäftsführung (Go-/No-Go) | | | ⬜ |
