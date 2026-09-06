# Ist-Zustand: Zoho Subscriptions als heutiges Kernsystem

Quelle: Anforderungsdokument „Umstellung Software deinPlatz v1" (06.09.2026, P. Allan) sowie
mündliche Angaben. Ersetzt die bisherigen `ANNAHME`-Aussagen zum Bestandssystem.

## 1. Systemlandschaft heute

| Baustein | System | Bemerkung |
| --- | --- | --- |
| Kundenverwaltung, Verträge, Fakturierung | **Zoho Subscriptions** (heute unter dem Namen Zoho Billing geführt) | Kein Self-Storage-Fachsystem. Zum Einrichtungszeitpunkt die am besten passende verfügbare Lösung – die Grenzen sind heute erreicht |
| Ergänzende Kundenverwaltung | Dateiablage in **OneDrive** | Parallelführung; soll mit der Umstellung entfallen (siehe Frage 2 im Benchmark) |
| Buchhaltung | Steuerberatung mit **RZL** | Schnittstelle zu RZL ist die wichtigste Einzelanforderung |
| Zahlungsabwicklung | **SEPA-Lastschrift über das eigene Bankkonto unter eigener Gläubiger-ID, ergänzt um Überweisungen; keine Kartenzahlung** (bestätigt 06.09.2026) | Mandate gehören deinPlatz und bleiben bei einem Softwarewechsel gültig |
| Zutrittskontrolle | ❓ Hersteller/Modell zu erheben | bestimmt die Integrationsmöglichkeit |
| Website | vorhanden (deinplatz.at) | Buchungsstrecke soll eingebunden, die Website nicht ersetzt werden |

> **Hinweis zum Zoho-Zugang in diesem Projekt:** Der in der Arbeitsumgebung verbundene
> Zoho-Zugang gehört zu den accilium-Mandanten, **nicht** zum Mandanten von deinPlatz.
> Für die Migrationsanalyse wird daher ein Export aus dem deinPlatz-Mandanten benötigt
> (oder ein lesender Zugang). Anzufordern in Woche 1.

## 2. Funktionale Lücken des heutigen Systems

Zoho Subscriptions ist ein Abrechnungssystem für wiederkehrende Leistungen, kein
Self-Storage-System. Daraus folgen die Lücken, die das neue System schließen soll:

| Lücke | Auswirkung heute |
| --- | --- |
| Kein Objekt-/Einheitenmodell | Belegung wird außerhalb des Systems geführt (OneDrive), Anlageplan fehlt |
| Kein Belegungs-/Verfügbarkeitsstatus | Verfügbarkeitsauskunft nur mit Nachschauen möglich |
| Keine Vertragsstrecke mit Unterschrift und Identitätsprüfung | Vertragsabschluss manuell |
| Keine Zutrittssteuerung | Zutritt getrennt gepflegt |
| Keine Buchungsstrecke auf der Website | Anfragen kommen telefonisch/per E-Mail, kein Abschluss außerhalb der Öffnungszeiten |
| Keine branchenübliche Interessentenverfolgung | Anfragen können verloren gehen |
| Buchhaltungsanbindung nicht auf RZL ausgerichtet | Übergabe an die Kanzlei aufwendig |
| Keine automatische Rückmeldung von Zahlungen und Rückläufern | Zahlungsabgleich erfolgt überwiegend manuell – Hauptziel der Automatisierung |
| Keine Kartenzahlung | Zahlungsarten für Neukunden eingeschränkt |

## 3. Anforderungsumfang laut Kundendokument

### Phase 1 (zum Go-Live)

| Nr. | Anforderung | Anforderungs-ID |
| --- | --- | --- |
| 1 | Schnittstelle zur Steuerberatung – **RZL** | BUH-01 |
| 2 | Vertrags-/Angebotserstellung online inklusive Ausweiskopie | VER-01, VER-02, VER-07 |
| 3 | Monatliche Rechnungserstellung und -versendung, nach Auswahl | ABR-01, ABR-07, ABR-13 |
| 4 | Zahlung wählbar: Lastschrift, Kreditkarte, Stripe o. Ä. | ABR-04, ABR-05, ABR-14 |
| 5 | Website integriert | BUC-02 |
| 6 | Automatisierte E-Mails | KOM-01 |

### Phase 2 (nach Stabilisierung)

| Nr. | Anforderung | Anforderungs-ID |
| --- | --- | --- |
| 7 | Buchungsportal | BUC-01 |
| 8 | Kundenportal – ausschließlich Aktualisierung der Zahlungsmethoden | BUC-03, BUC-05 |
| 9 | Anlageplan | OBJ-06 |

**Einordnung:** Beide Kandidaten der Shortlist liefern Phase 2 im Standard mit. Die Phasung ist
daher eine Frage der Einführungsreihenfolge, nicht des Produktumfangs – siehe
[`../30_markt/benchmark_kinnovis_stora.md`](../30_markt/benchmark_kinnovis_stora.md), Abschnitt 4.

## 4. Datenlage für die Migration (Angabe des Kunden)

| Datenobjekt | Verfügbarkeit in Zoho | Konsequenz |
| --- | --- | --- |
| Aktive Mieter | vorhanden | Basis der Migration |
| Name | vorhanden | – |
| Adresse | vorhanden | Formatprüfung |
| E-Mail | vorhanden | Voraussetzung für Portal und Rechnungsversand |
| Telefonnummer | **teilweise** | Nacherfassung beim nächsten Kundenkontakt, kein Blocker |
| **IBAN** | fehlt im Export | **kein Datenverlust** – vorhanden in Mandatsunterlagen und Electronic Banking, siehe [`../50_umsetzung/migration_zoho.md`](../50_umsetzung/migration_zoho.md) |
| Offene Posten | vorhanden | Stichtagsgenau zu übernehmen |
| Konto (Kundenkonto) | vorhanden | Saldo je Kunde |
| Kontoauszug (Statement) | vorhanden | als Archiv |
| Rechnungen | vorhanden | Archiv, keine Belegmigration |
| Kautionen | vorhanden | getrennt zu führen |
| **Zuordnung Kunde ↔ Lagerabteil** | ❓ vermutlich nicht strukturiert in Zoho | aus OneDrive-Liste zu rekonstruieren – **in Woche 1 prüfen** |

## 5. Offene Fragen aus dem Kundendokument

Beantwortet in [`../30_markt/benchmark_kinnovis_stora.md`](../30_markt/benchmark_kinnovis_stora.md), Abschnitt 9:

1. Wie funktioniert der Abgleich mit der Bank? → 9.1
2. Kann die Kundenverwaltung in OneDrive entfallen? → 9.2
3. Wie weit sind Pickerle bzw. Frau Tarmann einzubinden? → 9.3
4. Gibt es eine Interessentenverfolgung? → 9.4
5. Wie erfolgt die Evidenzhaltung gekündigter Verträge? → 9.5
6. Ist die Software cloudfähig? → 9.6

## 6. Was in Woche 1 zusätzlich zu erheben ist

- [x] Zahlungswege geklärt: SEPA über eigenes Bankkonto mit eigener Gläubiger-ID plus Überweisungen
- [ ] Mandatsliste mit IBAN, Mandatsreferenz, Erteilungsdatum und letztem Einzug aufbauen
- [ ] Anteil der Überweiser beziffern
- [ ] Anzahl aktiver Verträge und Einheiten, Belegungsgrad
- [ ] Hersteller und Modell der Zutrittsanlage
- [ ] Vertragslaufzeit und Kündigungsfrist des Zoho-Abonnements
- [ ] Umfang der Barzahlungen (bestimmt die Registrierkassenfrage, Prüfauftrag P1)
- [ ] Wie ist die Einheitenzuordnung heute dokumentiert (OneDrive-Struktur)?
- [ ] Aufbau der heutigen Rechnung und des Mietvertrags (Muster, anonymisiert)
