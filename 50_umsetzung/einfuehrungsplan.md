# Einführungsplan (Wochen 6–8)

Voraussetzung: Anbieter beauftragt (Meilenstein M5). Der Plan ist bewusst auf drei Wochen
verdichtet und arbeitet mit zwei Migrationsdurchläufen vor dem produktiven Lauf.

## Arbeitsstränge

| Strang | Inhalt | Verantwortlich |
| --- | --- | --- |
| S1 Konfiguration | Mandant, Standort, Einheiten, Preise, Steuersätze, Vorlagen, Mahnstufen, Benutzer/Rollen | Anbieter + PL |
| S2 Daten | Extraktion, Bereinigung, Mapping, Testläufe, Abgleich | Beratung + Fachverantwortung |
| S3 Zahlungen | Payment-Provider, SEPA-Mandate, Gläubiger-ID, Testeinzüge | Fachverantwortung Finanzen |
| S4 Integrationen | Zutrittskontrolle, Website-Einbindung, Buchhaltungsexport | Beratung + Anbieter |
| S5 Menschen | Schulung, Kurzanleitungen, Kundenkommunikation | Beratung + GF |
| S6 Abnahme | Testfälle, Fehlerliste, Go-/No-Go | PL |

## Wochenübersicht

### Woche 6 – Aufbau

| Tag | S1 Konfiguration | S2 Daten | S3/S4 | S5/S6 |
| --- | --- | --- | --- | --- |
| Mo | Kick-off mit Anbieter, Zugänge, Grundeinstellungen | Vollexport aus dem Altsystem | Payment-Konto beantragen | Schulungstermine fixieren |
| Di | Standort und Einheiten anlegen | Feldmapping erstellen | Gläubiger-ID/Mandatsfrage klären | – |
| Mi | Preisliste, Rabatte, Steuersätze | Bereinigung Dubletten/Adressen | Zutrittssystem: Integrationsgespräch | – |
| Do | Vertrags- und Rechnungsvorlagen | **Migrationstestlauf 1** | Website-Einbindung vorbereiten | – |
| Fr | Mahnstufen, E-Mail-Vorlagen, Benutzer/Rollen | Abgleichprotokoll, Fehlerliste | Buchhaltungsexport testen | Statusbericht, Go-/No-Go für W7 |

**Ergebnis Woche 6:** Testumgebung fachlich vollständig, ein Migrationsdurchlauf dokumentiert.

### Woche 7 – Prüfen und Üben

| Tag | Inhalt |
| --- | --- |
| Mo | Testfälle Teil 1 (Stammdaten, Vertrag, Zutritt) durch das Fachteam |
| Di | Testfälle Teil 2 (Abrechnungslauf, Zahlungen, Mahnwesen) inkl. Testeinzug |
| Mi | Fehlerbehebung mit Anbieter; Nachtest der Fehler der Klasse A |
| Do | **Migrationstestlauf 2** mit aktuellem Datenstand + Vollabgleich |
| Fr | Schulung (2 × 2 h), Kurzanleitungen verteilt, **Abnahmeentscheidung (M7)** |

Parallel: Kundenanschreiben zur Umstellung final freigegeben und versandfertig.

### Woche 8 – Umstellen

| Tag | Inhalt |
| --- | --- |
| Mo | Datenannahmestopp im Altsystem (nur noch lesend), Deltaerfassung auf Papier/Liste |
| Di | **Produktive Migration**, Abgleich, Freigabe durch Fachverantwortung Finanzen |
| Mi | **Go-Live**: alle Neuvorgänge im neuen System; Kundeninformation versendet |
| Do | Erster produktiver Abrechnungslauf im Vier-Augen-Prinzip, Versand nach Prüfung |
| Fr | Erster Lastschrifteinzug, Hypercare, Projektabschluss-Termin |

## Konfigurationsliste (Abhaken in Woche 6)

- [ ] Firmendaten, Logo, UID, Bankverbindung, Rechnungsnummernkreis
- [ ] Standort und alle Einheiten inkl. Größe, Typ, Merkmalen, Status
- [ ] Preisliste je Größenklasse, Aktionen und Rabattregeln
- [ ] Steuersätze und Erlöskonten laut Steuerberatung (Prüfauftrag P2)
- [ ] Vertragsvorlage, AGB, Hausordnung, Widerrufsbelehrung (Prüfauftrag P4)
- [ ] Rechnungs-, Mahn- und E-Mail-Vorlagen in deutscher Sprache
- [ ] Mahnstufen mit Fristen, Spesen und Sperrlogik
- [ ] Benutzer und Rollen inkl. lesendem Zugang für die Steuerberatung
- [ ] Zahlungsarten, SEPA-Gläubiger-ID, Vorabinformationsfrist
- [ ] Buchhaltungsexport konfiguriert und von der Steuerberatung geprüft
- [ ] Zutrittsintegration oder dokumentierter manueller Übergangsprozess
- [ ] Buchungsstrecke auf der Website (falls im Go-Live-Umfang)
- [ ] Backup-/Exportroutine dokumentiert

## Grundsatz für die Einführung

**Standard vor Sonderwunsch.** Jede Abweichung vom Systemstandard kostet in dieser Projektlaufzeit
mehr, als sie bringt. Sonderwünsche werden gesammelt und nach 8 Wochen im Betrieb neu bewertet –
erfahrungsgemäß erledigt sich ein Teil davon von selbst.
