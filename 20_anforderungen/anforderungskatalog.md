# Anforderungskatalog

Version 0.1 (Entwurf, Stand 06.09.2026) · Freigabe geplant Ende Woche 2

## Lesehinweis

- **Führende Quelle ist [`anforderungen.csv`](anforderungen.csv)**. Die Tabellen unten werden daraus
  erzeugt: `python3 werkzeuge/anforderungen_tabelle.py`. Änderungen bitte in der CSV vornehmen.
- **Priorität** nach MoSCoW: `Muss` (ohne diese Funktion ist der Betrieb nicht möglich),
  `Soll` (wichtig, Workaround kurzfristig denkbar), `Kann` (Zusatznutzen),
  `Nicht` (bewusst ausgeschlossen).
- **K.o.** kennzeichnet Ausschlusskriterien: Erfüllt ein Anbieter eines davon nicht,
  scheidet er unabhängig von der Gesamtpunktzahl aus.
- Die **Prüffrage** ist die Formulierung, mit der die Anforderung in RFP und Demo
  verifiziert wird – nicht die Selbstauskunft des Anbieters zählt, sondern das Gezeigte.

## Domänen

| Kürzel | Domäne | Gewicht in der Bewertung |
| --- | --- | --- |
| KUN | Kunden & Kontakte | 10 % |
| OBJ | Einheiten & Belegung | 10 % |
| BUC | Online-Buchung & Kundenportal | 10 % |
| VER | Vertragsmanagement | 15 % |
| PRI | Preise & Rabatte | 5 % |
| ABR | Abrechnung & Zahlung | 20 % |
| MAH | Mahnwesen | 10 % |
| ZUT | Zutrittskontrolle | 5 % |
| BUH | Buchhaltung & Schnittstellen | 5 % |
| REP | Reporting | 5 % |
| KOM | Kommunikation | 3 % |
| ADM | Administration, Sicherheit, Datenschutz | 2 % |

Die Gewichte gelten für die Dimension „Funktionale Abdeckung"; wie diese mit Kosten,
Anbieterreife und Einführbarkeit verrechnet wird, steht in
[`../30_markt/bewertungsmodell.md`](../30_markt/bewertungsmodell.md).

## 1. Kunden & Kontakte (KUN)

<!-- TABELLE:KUN -->
| ID | Anforderung | Prioritaet | K.o. | Prueffrage an den Anbieter |
| --- | --- | --- | --- | --- |
| KUN-01 | Verwaltung von Privat- und Firmenkunden mit getrennten Pflichtfeldern (UID, Firmenwortlaut) | Muss | – | Wie werden Firmenkunden mit abweichender Rechnungsanschrift abgebildet? |
| KUN-02 | Ein Kunde kann mehrere Einheiten und mehrere Vertraege gleichzeitig halten | Muss | **ja** | Wie sieht die Kundenakte bei 3 Vertraegen aus? |
| KUN-03 | Vollstaendige Kundenhistorie (Vertraege, Rechnungen, Zahlungen, Kommunikation, Notizen) auf einen Blick | Muss | – | Zeigen Sie die Kundenakte in der Demo. |
| KUN-04 | Dublettenpruefung bei Neuanlage | Soll | – | Woran wird eine Dublette erkannt? |
| KUN-05 | Lead-/Interessentenverwaltung inkl. Quelle und Wiedervorlage | Soll | – | Wie wird eine telefonische Anfrage erfasst und nachverfolgt? |
| KUN-06 | Dokumentenablage je Kunde (Vertrag, Korrespondenz) mit Berechtigungssteuerung | Muss | – | Wo liegen die Dokumente und wer darf sie sehen? |
<!-- ENDE -->

## 2. Einheiten & Belegung (OBJ)

<!-- TABELLE:OBJ -->
| ID | Anforderung | Prioritaet | K.o. | Prueffrage an den Anbieter |
| --- | --- | --- | --- | --- |
| OBJ-01 | Abbildung aller Einheiten mit Groesse, Typ, Merkmalen und Standort | Muss | **ja** | Wie werden 2,5 bis 50 m2 sowie Sonderflaechen abgebildet? |
| OBJ-02 | Grafischer oder listenbasierter Belegungsplan in Echtzeit | Muss | – | Wie schnell sieht der Mitarbeiter freie Einheiten je Groessenklasse? |
| OBJ-03 | Statusverwaltung frei/reserviert/belegt/gesperrt inkl. Wartung | Muss | – | Wie wird eine Einheit wegen Schaden gesperrt? |
| OBJ-04 | Reservierung mit Ablaufdatum und automatischer Freigabe | Soll | – | Was passiert mit einer nicht abgeholten Reservierung? |
| OBJ-05 | Mehrere Standorte/Mandanten ohne Systemwechsel (Skalierung) | Soll | – | Wie wuerde ein zweiter Standort ergaenzt und was kostet er? |
<!-- ENDE -->

## 3. Online-Buchung & Kundenportal (BUC)

<!-- TABELLE:BUC -->
| ID | Anforderung | Prioritaet | K.o. | Prueffrage an den Anbieter |
| --- | --- | --- | --- | --- |
| BUC-01 | Online-Verfuegbarkeitsanzeige und Buchung 24/7 mit Sofortzahlung | Soll | – | Bitte den kompletten Online-Abschluss live vorfuehren. |
| BUC-02 | Einbindung in die bestehende Website (Widget/Seite) ohne Website-Neubau | Muss | – | Wie erfolgt die technische Einbindung in unsere Website? |
| BUC-03 | Kundenportal zur Selbstverwaltung (Rechnungen, Zahlungsart, Kuendigung, Daten) | Soll | – | Was kann der Kunde selbst erledigen, was nicht? |
| BUC-04 | Buchungsstrecke vollstaendig in deutscher Sprache und rechtssicher (AGB, Widerruf, Datenschutz) | Muss | **ja** | Sind alle Kundentexte deutschsprachig und anpassbar? |
<!-- ENDE -->

## 4. Vertragsmanagement (VER)

<!-- TABELLE:VER -->
| ID | Anforderung | Prioritaet | K.o. | Prueffrage an den Anbieter |
| --- | --- | --- | --- | --- |
| VER-01 | Mietvertrag aus Vorlage mit Serienfeldern erzeugen, Vorlagen selbst pflegbar | Muss | **ja** | Wie aendern wir eine Vertragsklausel ohne Anbieter? |
| VER-02 | Digitale Unterschrift rechtswirksam (vor Ort auf Tablet und per Fernsignatur) | Soll | – | Welches Signaturverfahren wird eingesetzt und wie wird es nachgewiesen? |
| VER-03 | Vertragsstatus steuert Folgeprozesse (Abrechnung, Zutritt, Mahnung) automatisch | Muss | **ja** | Was passiert systemseitig bei Statuswechsel auf gekuendigt? |
| VER-04 | Vertragsaenderungen: Umzug in andere Einheit, Preisaenderung, Zahlungsartwechsel mit Historie | Muss | – | Wie wird ein Umzug in eine groessere Einheit abgebildet? |
| VER-05 | Kuendigung mit Fristenlogik, Endabrechnung und Kautionsabwicklung | Muss | – | Bitte eine Kuendigung inkl. anteiliger Abrechnung zeigen. |
| VER-06 | Mindestmietdauer, unbefristete Vertraege und Aktionsbindung (z. B. 12 Monate) abbildbar | Muss | – | Wie wird eine 12-Monats-Bindung mit Gratismonat hinterlegt? |
<!-- ENDE -->

## 5. Preise & Rabatte (PRI)

<!-- TABELLE:PRI -->
| ID | Anforderung | Prioritaet | K.o. | Prueffrage an den Anbieter |
| --- | --- | --- | --- | --- |
| PRI-01 | Preisliste je Groessenklasse und Standort, mit Gueltigkeitszeitraum | Muss | – | Wie wird eine Preiserhoehung zum Stichtag geplant? |
| PRI-02 | Rabatte und Aktionen (Prozent, Betrag, Freimonate) mit Automatik nach Ablauf | Muss | **ja** | Was passiert nach Ende des Gratismonats automatisch? |
| PRI-03 | Preisanpassung bestehender Vertraege mit Ankuendigungsschreiben und Wirksamkeitsdatum | Soll | – | Wie werden Bestandskunden ueber eine Erhoehung informiert? |
| PRI-04 | Dynamische Preise nach Belegungsgrad (Revenue Management) | Kann | – | Gibt es Preisautomatik nach Auslastung? |
<!-- ENDE -->

## 6. Abrechnung & Zahlung (ABR)

Kernstück des Projekts: Hier entsteht der größte Teil des heutigen manuellen Aufwands
und hier liegt das größte Fehlerrisiko bei der Migration (Stichtage, offene Posten, Mandate).

<!-- TABELLE:ABR -->
| ID | Anforderung | Prioritaet | K.o. | Prueffrage an den Anbieter |
| --- | --- | --- | --- | --- |
| ABR-01 | Automatischer wiederkehrender Abrechnungslauf (monatlich) fuer alle aktiven Vertraege | Muss | **ja** | Wie viele Klicks braucht der Monatslauf? |
| ABR-02 | Taggenaue anteilige Abrechnung bei Ein- und Auszug | Muss | **ja** | Rechnen Sie einen Einzug am 17. des Monats vor. |
| ABR-03 | Rechnungen nach oesterreichischem Recht (Pflichtangaben, USt.-Ausweis, fortlaufende Nummer) | Muss | **ja** | Bitte eine Musterrechnung fuer AT zeigen. |
| ABR-04 | SEPA-Lastschrift inkl. Mandatsverwaltung, Vorabinformation und Ruecklaeuferbearbeitung | Muss | **ja** | Wie werden Ruecklastschriften (R-Transaktionen) verarbeitet? |
| ABR-05 | Kartenzahlung wiederkehrend (tokenisiert) als Alternative zur Lastschrift | Soll | – | Welche Zahlungsdienstleister sind angebunden und zu welchen Gebuehren? |
| ABR-06 | Automatischer Zahlungsabgleich und offene-Posten-Liste | Muss | **ja** | Wie wird eine Teilzahlung zugeordnet? |
| ABR-07 | Rechnungsversand per E-Mail als PDF, optional Post/Portal-Abruf | Muss | – | Wie sieht der Versandprozess und das Fehlerhandling aus? |
| ABR-08 | Gutschriften, Storni und Guthabenverrechnung | Muss | – | Wie wird eine falsch gestellte Rechnung korrigiert? |
| ABR-09 | Kautionen und Depots getrennt fuehren und rueckzahlen | Soll | – | Wo sieht man offene Kautionen? |
| ABR-10 | Barzahlung mit Belegausgabe am Standort (Registrierkassenanbindung falls erforderlich) | Soll | – | Wie wird eine Barzahlung RKSV-konform erfasst? |
| ABR-11 | Zusatzleistungen (Versicherung, Schloss, Kartons, Parkplatz) mit korrektem Steuersatz abrechnen | Muss | – | Wie werden Waren und Mieten auf einer Rechnung getrennt? |
| ABR-12 | E-Rechnung im strukturierten Format (ebInterface/Peppol) fuer Firmenkunden und oeffentliche Auftraggeber | Kann | – | Welche E-Rechnungsformate werden unterstuetzt? |
<!-- ENDE -->

## 7. Mahnwesen (MAH)

<!-- TABELLE:MAH -->
| ID | Anforderung | Prioritaet | K.o. | Prueffrage an den Anbieter |
| --- | --- | --- | --- | --- |
| MAH-01 | Regelbasierte Mahnstufen mit Fristen, Textvorlagen und automatischem Versand | Muss | **ja** | Bitte den konfigurierten Mahnlauf zeigen. |
| MAH-02 | Mahnspesen und Verzugszinsen automatisch berechnen | Soll | – | Wie werden Mahnspesen hinterlegt? |
| MAH-03 | Automatische Zutrittssperre ab definierter Mahnstufe (ueber Zutrittsschnittstelle) | Soll | – | Wie wird die Sperre technisch ausgeloest und wieder aufgehoben? |
| MAH-04 | Uebersicht Aussenstaende nach Alter und Mahnstufe | Muss | – | Zeigen Sie das Debitorenreporting. |
<!-- ENDE -->

## 8. Zutrittskontrolle (ZUT)

Der konkrete Hersteller der bestehenden Zutrittsanlage ist in Woche 1 zu erheben; davon hängt ab,
ob ZUT-01/ZUT-02 zum Go-Live oder erst in Phase 2 realisierbar sind.

<!-- TABELLE:ZUT -->
| ID | Anforderung | Prioritaet | K.o. | Prueffrage an den Anbieter |
| --- | --- | --- | --- | --- |
| ZUT-01 | Schnittstelle zum bestehenden Zutrittssystem (Hersteller in W1 zu erheben) | Soll | – | Welche Zutrittssysteme sind nativ integriert, welche per API? |
| ZUT-02 | Zutrittsberechtigung folgt automatisch dem Vertragsstatus | Soll | – | Wie schnell wirkt eine Sperre nach Statuswechsel? |
| ZUT-03 | Zutrittsprotokoll im System einsehbar und auswertbar | Kann | – | Wo sieht man, wer wann Zutritt hatte? |
<!-- ENDE -->

## 9. Buchhaltung & Schnittstellen (BUH)

<!-- TABELLE:BUH -->
| ID | Anforderung | Prioritaet | K.o. | Prueffrage an den Anbieter |
| --- | --- | --- | --- | --- |
| BUH-01 | Export der Buchungsdaten im Format der Steuerberatung (BMD, RZL, DATEV oder definiertes CSV) | Muss | **ja** | Welche Exportformate liefern Sie standardmaessig? |
| BUH-02 | Konten- und Steuerschluesselzuordnung konfigurierbar | Muss | – | Wie werden Erloeskonten je Leistungsart zugeordnet? |
| BUH-03 | Unveraenderbarkeit und Nachvollziehbarkeit der Belege (keine stille Aenderung nach Versand) | Muss | **ja** | Wie wird eine bereits versendete Rechnung technisch geschuetzt? |
| BUH-04 | Bankkontoabgleich (CAMT/MT940-Import oder Provider-Abgleich) | Soll | – | Wie kommen Ueberweisungen ins System? |
<!-- ENDE -->

## 10. Reporting (REP)

<!-- TABELLE:REP -->
| ID | Anforderung | Prioritaet | K.o. | Prueffrage an den Anbieter |
| --- | --- | --- | --- | --- |
| REP-01 | Standardberichte: Belegungsgrad, Umsatz je m2, Neuzugaenge/Kuendigungen, Aussenstaende | Muss | – | Welche Berichte gibt es ohne Zusatzkosten? |
| REP-02 | Export aller Berichte nach Excel/CSV | Muss | – | Bitte Export live zeigen. |
| REP-03 | Eigene Auswertungen ohne Anbieterunterstuetzung erstellbar | Soll | – | Wie baut man einen eigenen Bericht? |
| REP-04 | Kennzahlen-Dashboard fuer die Geschaeftsfuehrung | Kann | – | Gibt es ein Startseiten-Dashboard? |
<!-- ENDE -->

## 11. Kommunikation (KOM)

<!-- TABELLE:KOM -->
| ID | Anforderung | Prioritaet | K.o. | Prueffrage an den Anbieter |
| --- | --- | --- | --- | --- |
| KOM-01 | Automatisierte E-Mails (Willkommen, Rechnung, Zahlungserinnerung, Vertragsende) mit eigenen Vorlagen | Muss | – | Wie pflegen wir Texte und Logo selbst? |
| KOM-02 | SMS- oder WhatsApp-Benachrichtigung bei Zahlungsverzug oder Zutrittsthemen | Kann | – | Welche Kanaele sind integriert und was kosten sie? |
| KOM-03 | Alle Kundentexte in deutscher Sprache, Duzen/Siezen frei waehlbar | Muss | **ja** | Sind saemtliche Systemtexte deutsch anpassbar? |
| KOM-04 | Dokumentierte Kommunikationshistorie je Kunde | Soll | – | Wo sieht man versendete Mails? |
<!-- ENDE -->

## 12. Administration, Sicherheit, Datenschutz (ADM)

<!-- TABELLE:ADM -->
| ID | Anforderung | Prioritaet | K.o. | Prueffrage an den Anbieter |
| --- | --- | --- | --- | --- |
| ADM-01 | Rollen- und Rechtekonzept (GF, Buero, Facility Manager, Steuerberatung lesend) | Muss | – | Welche Rollen sind vorkonfiguriert? |
| ADM-02 | Protokollierung von Aenderungen (wer hat wann was geaendert) | Muss | – | Zeigen Sie das Aenderungsprotokoll eines Vertrags. |
| ADM-03 | Auftragsverarbeitungsvertrag nach Art. 28 DSGVO und Hosting in der EU | Muss | **ja** | Wo liegen die Daten und liegt ein AVV vor? |
| ADM-04 | Loeschkonzept und Aufbewahrungsfristen konfigurierbar | Soll | – | Wie werden Daten nach Fristablauf geloescht? |
| ADM-05 | Vollstaendiger Datenexport aller Objekte jederzeit selbststaendig moeglich | Muss | **ja** | Bitte den Gesamtexport demonstrieren. |
| ADM-06 | Zwei-Faktor-Authentifizierung fuer Benutzerkonten | Soll | – | Ist 2FA verfuegbar und erzwingbar? |
| ADM-07 | Benutzeroberflaeche deutschsprachig | Muss | **ja** | Ist die Oberflaeche vollstaendig auf Deutsch? |
| ADM-08 | Deutschsprachiger Support mit definierten Reaktionszeiten | Muss | **ja** | Wie sind Supportzeiten, Kanaele und Reaktionszeiten geregelt? |
<!-- ENDE -->

## Zusammenfassung der K.o.-Kriterien

Ein Anbieter kommt nur in die Shortlist, wenn er **alle** als K.o. markierten Anforderungen
erfüllt. Die vollständige Liste wird beim Screening (Woche 3) abgehakt und im Protokoll
dokumentiert.

## Änderungshistorie

| Version | Datum | Änderung | Autor |
| --- | --- | --- | --- |
| 0.1 | 06.09.2026 | Erstentwurf auf Basis Marktrecherche und Branchenstandard | Beratung |
