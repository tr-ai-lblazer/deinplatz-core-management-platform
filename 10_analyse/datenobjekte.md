# Datenobjekte und Feldübersicht

Grundlage für Migration (`50_umsetzung/datenmigration.md`), Anbieterbewertung (Datenmodell-Fit)
und DSGVO-Betrachtung. Feldlisten sind Soll-Vorgaben; die Zuordnung zu den Feldern des
Altsystems erfolgt im Mapping nach der Ist-Aufnahme.

## Übersicht

| Objekt | Beschreibung | Volumen (`ANNAHME`) | Migrationsrelevanz |
| --- | --- | --- | --- |
| Kunde/Kontakt | Privat- und Firmenkunden | 200–600 | zwingend |
| Einheit (Lagerabteil) | Vermietbare Fläche 2,5–50 m² | 100–400 | zwingend |
| Mietvertrag | Verknüpfung Kunde ↔ Einheit ↔ Preis ↔ Laufzeit | aktiv + Historie | zwingend |
| Preis/Tarif | Listenpreis je Größenklasse, Rabatte, Aktionen | 10–40 | zwingend |
| Rechnung/Beleg | Ausgangsrechnungen, Gutschriften | Historie | teilweise (Archiv) |
| Zahlung | Zahlungseingänge, Zuordnung zur Rechnung | Historie | offene Posten zwingend |
| Zahlungsmittel/Mandat | SEPA-Mandat, Karte (tokenisiert) | je aktiver Vertrag | zwingend, rechtlich sensibel |
| Zusatzleistung | Versicherung, Schloss, Kartons, Parkplatz | wenige | zwingend |
| Dokument | Vertrags-PDF, Ausweis, Korrespondenz | je Vertrag | selektiv |
| Zutrittsberechtigung | PIN/Karte/App je Kunde und Einheit | je aktiver Vertrag | zwingend (Neuanlage möglich) |
| Interessent/Lead | Anfragen ohne Vertrag | laufend | optional |
| Aktivität/Notiz | Gesprächsnotizen, Historie | laufend | optional |

## Kunde/Kontakt

| Feld | Pflicht | Anmerkung |
| --- | --- | --- |
| Kundennummer | ja | Nummernkreis im Neusystem festlegen; Altnummer als Zusatzfeld mitnehmen |
| Typ (Privat/Firma) | ja | steuert UID-Pflicht und Rechnungsanschrift |
| Firmenname / Vorname / Nachname | ja | |
| Rechnungsanschrift (Straße, PLZ, Ort, Land) | ja | |
| E-Mail, Telefon/Mobil | ja | E-Mail ist Voraussetzung für Portal und Rechnungsversand |
| UID-Nummer (ATU…) | bei Firmen | Rechnungsanforderung |
| Geburtsdatum, Ausweisdaten | optional | nur mit Zweckbindung erfassen (DSGVO), Löschfrist definieren |
| Bevorzugte Sprache / Kommunikationskanal | optional | |
| Marketing-Einwilligung | ja/nein | Nachweis mit Zeitstempel migrieren |
| Notizen | optional | Freitext prüfen: keine sensiblen Daten |

## Einheit (Lagerabteil)

| Feld | Pflicht | Anmerkung |
| --- | --- | --- |
| Einheitennummer | ja | wie vor Ort beschildert |
| Standort/Gebäude/Etage | ja | |
| Fläche m² / Volumen m³ | ja | Größenklassen für Preisliste und Reporting |
| Typ (Abteil, Container, Parkplatz, Regal) | ja | |
| Status (frei, reserviert, belegt, gesperrt/wartung) | ja | |
| Listenpreis | ja | |
| Merkmale (Erdgeschoss, Aufzug, Strom, Klima, Tordimension) | optional | verkaufsrelevant |

## Mietvertrag

| Feld | Pflicht | Anmerkung |
| --- | --- | --- |
| Vertragsnummer | ja | |
| Kunde, Einheit(en) | ja | ein Kunde kann mehrere Einheiten mieten |
| Beginn / vereinbarte Mindestlaufzeit / Kündigungsfrist | ja | Mindestmietdauer laut Angebot 1 Monat |
| Vereinbarter Preis, abweichend vom Listenpreis | ja | Rabattgrund dokumentieren |
| Rabatt/Aktion inkl. Gültigkeit | ja | z. B. Aktion „1 Monat gratis bei 12 Monaten" |
| Abrechnungsintervall, nächster Abrechnungstermin | ja | migrationskritisch: Stichtag muss exakt stimmen |
| Zahlungsart, Mandatsreferenz | ja | |
| Kaution (Betrag, Status) | ja | |
| Versicherung/Zusatzleistungen | ja | |
| Status (aktiv, gekündigt, beendet, im Verzug) | ja | |
| Kündigungsdatum, Auszugsdatum | bei Ende | |

## Offene Posten (Stichtagsdaten)

Kritischste Migrationsposition: Zum Cutover müssen **offene Rechnungen, Teilzahlungen,
Guthaben, Kautionen und der nächste Abrechnungsstichtag** exakt übernommen werden.
Empfehlung: Summenabgleich (Gesamtsumme offener Posten alt = neu) **und** Einzelabgleich
der 20 größten Posten, protokolliert im Migrationsprotokoll.

## Personenbezug und Löschfristen (DSGVO)

| Datenkategorie | Zweck | Aufbewahrung (Vorschlag, mit Steuerberatung/Recht abstimmen) |
| --- | --- | --- |
| Stammdaten Kunde | Vertragserfüllung | Vertragsende + gesetzliche Aufbewahrungsfrist |
| Rechnungen/Buchungsbelege | steuerliche Aufbewahrungspflicht | 7 Jahre (§ 132 BAO), teils länger bei laufenden Verfahren |
| SEPA-Mandate | Nachweis Einzugsermächtigung | 14 Monate nach letztem Einzug, danach nur bei Bedarf |
| Ausweiskopien | Identitätsprüfung | nur wenn wirklich erforderlich; enge Frist, sonst gar nicht speichern |
| Zutrittsprotokolle | Sicherheit/Beweiszwecke | kurze Frist (z. B. 30–90 Tage) |
| Videoaufzeichnungen | Objektschutz | üblich 72 Stunden, separate Anlage und Dokumentation |
| Marketing-Einwilligungen | Nachweis | bis Widerruf + Nachweisfrist |
