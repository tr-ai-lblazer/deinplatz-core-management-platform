# Benchmark: Kinnovis vs. Stora

Stand: 06.09.2026 · Bezug: Anforderungsdokument „Umstellung Software deinPlatz v1" (Phase 1/2)

> **Ergänzender Report:** Die Zahlungsabwicklung ist in einem eigenen Report für die
> Geschäftsführung vertieft: [`benchmark_kinnovis_stora_zahlungsabwicklung.docx`](benchmark_kinnovis_stora_zahlungsabwicklung.docx)
> – Betriebsmodelle, Einbindung der Bestandskunden, Automatisierungsgrad und Kosten.
Quellen: [`../90_quellen/recherchequellen.md`](../90_quellen/recherchequellen.md)

## 0. Auf einen Blick

**Empfehlung (vorläufig, bis zu den Demos): Kinnovis liegt für deinPlatz vorn.**

Der Grund ist nicht der Funktionsumfang – der ist bei beiden Produkten für einen Standort mehr
als ausreichend – sondern der Rechts- und Sprachraum:

1. **Kinnovis kommt aus Österreich.** Das Produkt ist aus dem Betrieb der Marke STORE ROOM
   (Muttergesellschaft Zinkpower) entstanden, deren Flaggschiff mit 9.000 m² als größte
   Self-Storage-Anlage Österreichs auftritt. Kinnovis GmbH ist Mitglied im
   Self-Storage-Verband – demselben Verband, in dem auch deinPlatz gelistet ist.
2. **Buchhaltung:** Kinnovis führt einen **DATEV-Report** als Integration. RZL kann DATEV-Format
   im CSV importieren – damit existiert ein realistischer Weg zur RZL-Schnittstelle
   (Ihr wichtigster Punkt). Für Stora ist bisher nur Xero/QuickBooks belegt; das hilft in
   Österreich nicht.
3. **Zahlung:** Kinnovis unterstützt neben Stripe auch einen **SEPA-Lastschrift-XML-Export**,
   also Einzug über die Hausbank ohne Kartengebühren. Stora wickelt Zahlungen ausschließlich
   über Stripe ab (Karte, SEPA, Link).
4. **Stora ist dafür kaufmännisch transparenter** (öffentliche Preise ab 99 GBP/Monat, keine
   Mindestlaufzeit) und beim Thema Ertragssteuerung/dynamische Preise weiter.

**Aber:** Kein Punkt in diesem Dokument ersetzt die Demo. Die drei Fragen, die die Entscheidung
tatsächlich kippen können – RZL-Import in der Praxis, deutschsprachige Kundendokumente,
Übernahme der Zahlungsdaten aus Zoho – sind bei **beiden** Anbietern noch offen und in
Abschnitt 10 als Fragenkatalog vorbereitet.

## 1. Belastbarkeit dieser Analyse

| Kennzeichnung | Bedeutung |
| --- | --- |
| ✅ | Aus öffentlicher Quelle belegt (Quellenverzeichnis) |
| 🟡 | Plausibel, aber nicht belegt – in der Demo zu prüfen |
| ❓ | Offen, muss vom Anbieter beantwortet werden |
| ❌ | Nach aktuellem Stand nicht gegeben |

> **Einschränkung:** Die Websites `kinnovis.com` und `stora.co` sind aus dieser Arbeitsumgebung
> netzwerkseitig nicht direkt abrufbar. Die Angaben stammen aus Suchergebnissen, Fach- und
> Vergleichsportalen sowie Verbandsverzeichnissen. Produktangaben von Anbieterseiten sind
> Marketingaussagen – verbindlich werden sie erst durch Demo und Angebot.

## 2. Anbietersteckbriefe

| Merkmal | **Kinnovis** | **Stora** |
| --- | --- | --- |
| Unternehmen | Kinnovis GmbH ✅ | Stora (UK/Irland) ✅ |
| Herkunft | Aus dem eigenen Self-Storage-Betrieb in **Österreich** entstanden (Zinkpower / STORE ROOM, seit 2018) ✅ | Aus dem UK-Markt für unabhängige Betreiber ✅ |
| Marktpräsenz | Betreiber in 19 europäischen Ländern ✅; DACH-Kunden u. a. CoStore (Leipzig, Brandenburg a. d. H.), Zweitbox ✅ | Betreiber in 19 Ländern ✅, Schwerpunkt UK/Irland 🟡 |
| Verbandsmitgliedschaft | Self-Storage-Verband (DACH) ✅ | ❓ |
| Deutschsprachige Website | ja (`kinnovis.com/de`) ✅ | deutschsprachige Produktbeschreibung vorhanden ✅, Produktoberfläche ❓ |
| Positionierung | „AI-powered" Verwaltungsplattform, von Betreibern für Betreiber ✅ | Automatisierungs- und Wachstumsplattform für unabhängige Betreiber ✅ |
| Preismodell | nicht öffentlich, Angebot nach Standort/Einheiten ✅ | öffentlich: Essentials 99 GBP, Advanced 149 GBP, Premium 299 GBP pro Monat; keine Setup-Gebühr, keine Mindestlaufzeit ✅ (EUR-Preisliste separat, zu prüfen) |
| Eigene Zutritts-Hardware | ja („Kinnovis Access": Tür-/Torsteuerung, Mieter-App, Buchung-bis-Zutritt) ✅ | nein, „Smart Access" über Integrationen ✅ |
| Offene Schnittstelle | „Kinnovis Connect" (öffentliche API) ✅ | Zapier mit 8.000+ Apps ✅, API ❓ |

## 3. Bewertung entlang **Phase 1** (Ihr Anforderungsdokument)

| Ihre Anforderung | Kinnovis | Stora | Bewertung |
| --- | --- | --- | --- |
| **Schnittstelle Steuerberater – RZL** | **DATEV-Report** als Integration ✅; RZL importiert DATEV-CSV ✅ → Brücke plausibel 🟡 | Export „formatiert für Xero" ✅; RZL-tauglicher Export ❓ | **Vorteil Kinnovis.** In beiden Fällen ist der Weg über eine Buchungsstapel-CSV zu bestätigen – mit RZL und mit der Steuerberatung |
| **Vertrag/Angebot online inkl. Ausweiskopie** | E-Signatur im Online-Buchungsprozess ✅, Signable-Integration ✅, Identitätsprüfung über Stripe Identity (Pass/Fail) ✅ | Online-Buchung mit Vertragsabschluss ✅, E-Signatur 🟡, Ausweisprüfung ❓ | **Vorteil Kinnovis** – mit Einschränkung: Stripe Identity liefert *Prüfergebnis*, nicht zwingend eine *gespeicherte Ausweiskopie*. Falls Sie die Kopie ablegen wollen, ist das eine eigene Frage (auch datenschutzrechtlich, siehe 6.4) |
| **Monatliche Rechnungserstellung und -versand, nach Auswahl** | automatisierte Rechnungsstellung über Stripe Billing ✅, automatisierte E-Mails mit Triggern ✅ | automatisierte Rechnungsstellung und Zahlungsabwicklung ✅ | **Gleichstand.** Prüfpunkt: „nach Auswahl" – also selektiver Lauf für einzelne Kunden/Gruppen – ist in der Demo zu zeigen |
| **Zahlung wählbar: Lastschrift, Kreditkarte, Stripe o. ä.** | Stripe (Karte) ✅ **und** SEPA-Lastschrift-XML-Export für die Hausbank ✅ | Stripe: Karte, SEPA-Lastschrift, Link ✅; Kunde wählt beim Buchen die Methode ✅ | **Vorteil Kinnovis** bei der Wahlfreiheit (Bank-Lastschrift ohne Stripe möglich), **Vorteil Stora** bei der Bequemlichkeit im Buchungsprozess |
| **Website integriert** | kostenlose Website im Produkt enthalten ✅, Buchungsportal ✅ | „Storefront" mit Buchungsstrecke, Website im Produkt ✅ | **Gleichstand.** Prüfpunkt für beide: Einbindung in die **bestehende** deinPlatz-Website statt Ersatz durch eine Anbieter-Website |
| **Automatisierte E-Mails** | Vorlagen, Merge-Tags, Trigger (Zahlungserinnerung, Willkommen, Verlängerung) ✅ | automatisierte Kommunikation entlang Buchung/Zahlung ✅ | **Gleichstand.** Prüfpunkt: alle Texte deutsch und selbst pflegbar |

## 4. Bewertung entlang **Phase 2**

| Ihre Anforderung | Kinnovis | Stora | Bewertung |
| --- | --- | --- | --- |
| **Buchungsportal** | 24/7-Buchungsportal im Standard ✅ | Storefront/Online-Buchung im Standard ✅ | Gleichstand – bei Stora traditionell der Produktkern |
| **Kundenportal (nur Zahlungsmethode aktualisieren)** | Kundenportal für Einheiten, Zahlungen, Zutritt, Kontaktdaten ✅ | Kundenkonto zur Selbstverwaltung ✅ | Gleichstand. Prüfpunkt: Lässt sich der Umfang **einschränken** (nur Zahlungsdaten), oder kann der Kunde auch kündigen/ändern? |
| **Anlageplan** | interaktive Facility Map im Standard ✅ | „Facility Maps" als neu eingeführtes Produkt ✅ 🟡 (Reifegrad/Plan-Zugehörigkeit prüfen) | **Leichter Vorteil Kinnovis** (länger im Produkt); bei Stora klären, ob Facility Maps im gewählten Tarif enthalten ist |

Beide Anbieter liefern Phase 2 im Standard mit. **Konsequenz:** Die Aufteilung in Phase 1 und 2
ist bei diesen zwei Kandidaten weniger eine Produkt- als eine Einführungsfrage – Sie können
entscheiden, ob Buchungsportal und Kundenportal am Tag 1 aktiviert werden oder erst nach
Stabilisierung des Kerngeschäfts. Meine Empfehlung: **Kernbetrieb zuerst, Portale zwei bis
vier Wochen später** – aber im selben System, ohne zweites Projekt.

## 5. Funktionaler Detailvergleich (Domänen des Anforderungskatalogs)

| Domäne | Kinnovis | Stora | Anmerkung |
| --- | --- | --- | --- |
| Kunden & Kontakte (KUN) | ✅ | ✅ | Interessentenverfolgung bei beiden ❓ (siehe 9.4) |
| Einheiten & Belegung (OBJ) | ✅ Facility Map | ✅ Facility Maps (neu) | – |
| Online-Buchung & Portal (BUC) | ✅ | ✅ | Storefront von Stora gilt als besonders ausgereift 🟡 |
| Vertragsmanagement (VER) | ✅ E-Signatur, Signable | 🟡 | Vertragsvorlagen in deutscher Sprache: bei beiden ❓ |
| Preise & Rabatte (PRI) | ✅ | ✅ + dynamisches Revenue Management ✅ | **Vorteil Stora** bei automatischer Preissteuerung |
| Abrechnung & Zahlung (ABR) | ✅ Stripe Billing + SEPA-XML | ✅ Stripe (Karte/SEPA/Link) | Österreichische USt.- und Rechnungslogik: bei beiden ❓ – **K.o.-Kriterium** |
| Mahnwesen (MAH) | ✅ automatisierte Erinnerungen | ✅ automatisiertes Handling fehlgeschlagener Zahlungen | Mahnstufen, Spesen, Verzugszinsen nach AT-Praxis: ❓ |
| Zutrittskontrolle (ZUT) | ✅ eigene Lösung + Sensorberg, Tapkey, JANUS/Nokē | ✅ Integrationen | **Vorteil Kinnovis** im DACH-Raum (Sensorberg, Tapkey sind hier verbreitet) |
| Buchhaltung (BUH) | ✅ DATEV-Report, Xero | ✅ Xero, QuickBooks | **Vorteil Kinnovis** – siehe 6.1 |
| Reporting (REP) | ✅ Analytics mit Filtern | ✅ Echtzeit-Kennzahlen | Nutzerkritik an Stora-Reporting bei Mehrstandort ✅ (für Sie irrelevant) |
| Kommunikation (KOM) | ✅ | ✅ | Deutschsprachigkeit der Vorlagen: ❓ bei beiden |
| Administration/DSGVO (ADM) | ❓ AVV/Hosting | ❓ AVV/Hosting | Bei beiden im RFP anzufordern |

## 6. Die vier kritischen Punkte

### 6.1 RZL-Schnittstelle (Ihr wichtigster Punkt)

Weder Kinnovis noch Stora hat eine native RZL-Integration – das hat kein Anbieter dieser
Produktklasse. Realistisch sind drei Wege:

| Weg | Beschreibung | Kinnovis | Stora |
| --- | --- | --- | --- |
| **A: DATEV-Format** | RZL importiert Buchungsstapel im DATEV-CSV-Format (nach DATEV-Leitfaden 1.4 inkl. Erweiterungen 2015) ✅ | DATEV-Report vorhanden ✅ → direkter Kandidat | ❌ nicht belegt |
| **B: RZL-eigenes CSV** | RZL-Format mit getrennten Soll-/Haben-Spalten, positivem Betrag, numerischem USt.-Schlüssel ✅ | aus Standard-CSV-Export per Mapping erzeugbar 🟡 | aus Standard-CSV-Export per Mapping erzeugbar 🟡 |
| **C: Belegweise** | Monatlicher Sammelbeleg/Umsatzliste plus Belegablage; Buchung durch die Kanzlei | bei beiden möglich, aber Rückschritt gegenüber heute | dito |

**Wichtige Einschränkung:** Ein „DATEV-Report" ist auf den **deutschen** Kontenrahmen ausgelegt.
Österreichische Kontenrahmen und USt.-Schlüssel weichen ab. Der Report muss also entweder
konfigurierbar sein (Konten und Steuerschlüssel frei zuordenbar) oder es braucht eine
Mapping-Datei zwischen Export und RZL. Das ist Aufwand von Stunden bis wenigen Tagen, kein
Projektrisiko – **aber es muss vor der Entscheidung geklärt sein.**

**Vorgehen:** Musterexport beider Anbieter anfordern (ein voller Monat, echte Struktur) und
**vor der Entscheidung** von der Steuerberatung testweise in RZL importieren lassen. Das ist
die einzige belastbare Prüfung. Ein „ja, wir haben eine Buchhaltungsschnittstelle" im
Vertriebsgespräch ist keine.

### 6.2 Zahlungen: Betriebsmodell, Mandate und Kostenwirkung

**Ist-Zustand (bestätigt 06.09.2026):** SEPA-Lastschrift über das **eigene Bankkonto** unter
**eigener Gläubiger-ID**, ergänzt um Überweisungen; der Abgleich erfolgt weitgehend manuell.

Damit ist die entscheidende Frage nicht „Stripe ja oder nein", sondern welches Betriebsmodell
gefahren wird:

| Modell | Einzug durch | Mandate | Verfügbar bei |
| --- | --- | --- | --- |
| **A – eigene Bank** | Hausbank über SEPA-Datei (pain.008) aus dem System | bleiben unverändert gültig | Kinnovis (SEPA-XML-Export belegt); Stora: nicht vorgesehen |
| **B – Stripe** | Stripe, mit voller Rückmeldung ins System | portierbar, **wenn** die eigene Gläubiger-ID vor der ersten Live-Zahlung hinterlegt wird | Kinnovis und Stora |
| **C – Hybrid (Empfehlung)** | Bestand über die Bank, Neuverträge über Stripe | keine Kundenaktion nötig | nur mit SEPA-XML, also Kinnovis |

**Kritischer Konfigurationspunkt:** Bei Stripe ist die Gläubiger-ID **nach der ersten Live-Zahlung
nicht mehr änderbar** ✅. Wird versehentlich die Stripe-Gläubiger-ID verwendet, müssen alle Mandate
neu eingeholt werden.

**Überweisungen:** Für Stora ist belegt, dass Zahlungen mit manueller Zahlungsart (Überweisung,
Bar, Scheck) im System **von Hand als bezahlt markiert** werden ✅ – für diesen Teil der Kunden
entsteht kein Automatisierungsgewinn. Ob eines der Systeme einen Kontoauszug (CAMT.053/MT940)
einlesen kann, ist bei beiden offen ❓ und in den Demos zu klären (Anforderung BUH-04).

Rechenbeispiel (`ANNAHME`: 120 aktive Verträge, Ø 100 € Monatsmiete, 12.000 € Monatsumsatz;
Stripe-Listenpreise Österreich: europäische Karten 1,5 % + 0,25 €, SEPA-Lastschrift 0,35 € pauschal ✅):

| Szenario | Kosten je Monat | Kosten je Jahr |
| --- | --- | --- |
| Alles über Karte | 12.000 × 1,5 % + 120 × 0,25 € = **210 €** | **2.520 €** |
| Alles über SEPA-Lastschrift (Stripe) | 120 × 0,35 € = **42 €** | **504 €** |
| Alles über Bank-Lastschrift (SEPA-XML, nur Kinnovis) | Bankentgelt, meist unter 20 € | **~240 €** |

Die Zahlungsentgelte übersteigen bei Kartendominanz die Softwarekosten. **Konsequenz für die
Konfiguration – unabhängig vom Anbieter: SEPA-Lastschrift als Standard, Karte als Ausweichoption.**
Das deckt sich mit Ihrer Anforderung „Zahlung auswählbar", verschiebt aber die Voreinstellung.

### 6.3 Sprache und österreichische Rechnungslogik

Für Kinnovis ist deutschsprachiger Marktauftritt belegt, für Stora bisher nur deutschsprachiges
Marketingmaterial. Entscheidend sind aber nicht die Websites, sondern:

1. Oberfläche für Ihr Team auf Deutsch,
2. **Kundendokumente** (Vertrag, Rechnung, Mahnung, E-Mails) auf Deutsch und selbst pflegbar,
3. Rechnung nach § 11 UStG mit korrektem USt.-Ausweis und lückenloser Nummerierung,
4. Handhabung von Kautionen (durchlaufender Posten, nicht Erlös).

Punkte 2 bis 4 sind bei **beiden** Anbietern offen und in der Demo an einer echten Musterrechnung
zu prüfen – nicht als Zusage entgegenzunehmen.

### 6.4 Ausweiskopie – bitte bewusst entscheiden

Ihr Dokument fordert „Vertrag/Angebot Erstellung online einschließlich Kopie Ausweis".
Kinnovis löst Identität über Stripe Identity als **Prüfung** (bestanden/nicht bestanden) –
das ist datenschutzrechtlich die sauberere Variante, weil keine Ausweiskopie dauerhaft bei
Ihnen liegt. Wenn Sie die Kopie zusätzlich speichern wollen, brauchen Sie Zweck,
Rechtsgrundlage und Löschfrist (siehe [`../10_analyse/datenobjekte.md`](../10_analyse/datenobjekte.md)).

**Empfehlung:** Identitätsprüfung ja, dauerhafte Ausweiskopie nur, wenn ein konkreter Zweck sie
verlangt – etwa die Durchsetzung des Zurückbehaltungsrechts bei Zahlungsverzug. Diesen Zweck mit
der Rechtsberatung abstimmen (Prüfauftrag P7 in
[`../20_anforderungen/rechtliche_rahmenbedingungen_at.md`](../20_anforderungen/rechtliche_rahmenbedingungen_at.md)).

## 7. Kosten

| Position | Kinnovis | Stora |
| --- | --- | --- |
| Software je Monat | ❓ nicht öffentlich, Angebot erforderlich | 99 / 149 / 299 GBP je nach Tarif ✅ (EUR-Preise separat prüfen) |
| Einrichtung/Onboarding | ❓ | keine Setup-Gebühr ✅ |
| Vertragsbindung | ❓ | keine Mindestlaufzeit ✅ |
| Zahlungsentgelte | Stripe-Konditionen bzw. Bankentgelt bei SEPA-XML | Stripe-Konditionen |
| Migrationsunterstützung | ❓ | ❓ |

**Für den TCO-Vergleich anzufordern (36 Monate):** Lizenz inkl. angekündigter Preissteigerung,
Onboarding, Migration, alle Zusatzmodule (Facility Map, Kundenportal, Zutrittsintegration,
E-Signatur), Zahlungsentgelte, Kosten für einen möglichen zweiten Standort.
Erfassung in [`../40_auswahl/bewertungsmatrix.csv`](../40_auswahl/bewertungsmatrix.csv).

**Achtung Tarifgrenzen bei Stora:** Bei drei Tarifstufen liegt der Preisvorteil des
Einstiegstarifs nur dann vor, wenn die benötigten Funktionen (Facility Maps, erweiterte
Automatisierung, Reporting) darin enthalten sind. Die Zuordnung Ihrer Anforderungen zu einem
konkreten Tarif ist Teil der Angebotsanfrage.

## 8. Migration aus Zoho Subscriptions

Ausführlich in [`../50_umsetzung/migration_zoho.md`](../50_umsetzung/migration_zoho.md).
Für den Anbietervergleich zählt:

| Aspekt | Kinnovis | Stora |
| --- | --- | --- |
| Import von Kunden, Einheiten, Verträgen | ❓ Importvorlagen anfordern | ❓ Importvorlagen anfordern |
| Übernahme offener Posten | ❓ | ❓ |
| **Übernahme der Zahlungsdaten/Mandate** | wenn beide Seiten Stripe nutzen, ist ein Übertrag zwischen Stripe-Konten grundsätzlich möglich – jedoch **nur bei identischer Gläubiger-ID** und nur für als PaymentMethod gespeicherte Mandate ✅ | dieselbe Bedingung ✅ |
| Kautionen | ❓ eigenes Feld/Position nötig | ❓ |
| Rechnungshistorie | Archivweg klären ❓ | Archivweg klären ❓ |

**Nachtrag zur Mandatsfrage (geklärt am 06.09.2026):** Da die Einzüge über das eigene Bankkonto
unter eigener Gläubiger-ID laufen, ist deinPlatz selbst Gläubiger der Mandate. Sie bleiben bei
einem Softwarewechsel gültig; eine Neueinholung ist nicht erforderlich. Die im Zoho-Export
fehlenden IBANs sind aus den Mandatsunterlagen und dem Electronic Banking zu beschaffen.
Zu prüfen bleiben Mandate ohne Einzug in den letzten 36 Monaten (Verfall) sowie Verträge ohne
gültiges Mandat. Details: [`../50_umsetzung/migration_zoho.md`](../50_umsetzung/migration_zoho.md).

## 9. Antworten auf Ihre sechs Fragen

### 9.1 Wie funktioniert das mit dem Abgleich Bank?

Drei Modelle, je nach Zahlungsweg:

- **Stripe (Karte/SEPA):** Der Abgleich passiert im System automatisch – die Zahlung ist der
  Rechnung zugeordnet, bevor das Geld auf dem Konto ist. Auf dem Bankkonto erscheint eine
  **Sammelauszahlung** von Stripe, nicht die Einzelzahlung. Für die Buchhaltung heißt das:
  Auszahlung gegen Forderungskonto plus Gebührenbuchung – die Kanzlei muss das einmalig einrichten.
- **SEPA-XML über die Hausbank (nur Kinnovis):** Sie erzeugen die Einzugsdatei, die Bank zieht
  ein, Rückläufer kommen als Einzelposten zurück. Der Abgleich erfolgt über den Kontoauszug
  (CAMT/MT940) oder manuell.
- **Überweisung:** immer Abgleich über Kontoauszug – hier ist ein Bankimport im System das
  entscheidende Komfortmerkmal (Anforderung BUH-04).

**Frage an beide Anbieter:** Gibt es einen Bankkontoimport (CAMT.053/MT940) oder eine
Bankanbindung, und wie werden Stripe-Sammelauszahlungen aufgelöst?

### 9.2 Kann die Kundenverwaltung in OneDrive künftig entfallen?

**Ja – das ist sogar der eigentliche Zweck der Umstellung.** Kundenstamm, Verträge, Rechnungen,
Zahlungen und Kommunikation gehören in ein System. Zwei Einschränkungen:

1. **Dokumente:** Beide Systeme legen Vertrags- und Rechnungs-PDFs ab. Prüfen Sie in der Demo,
   ob auch **eigene** Dokumente je Kunde hinterlegbar sind (Schriftverkehr, Übergabeprotokoll).
   Wenn nicht, bleibt eine schlanke Dokumentablage nötig – dann aber ohne parallele Datenpflege.
2. **Archiv:** Der Bestand aus OneDrive wird nicht vollständig migriert. Er bleibt als Archiv
   erhalten (Aufbewahrungspflicht sieben Jahre), wird aber „eingefroren": ab Go-Live keine
   Neuablage mehr.

Erfolgskriterium nach vier Wochen: **null parallel geführte Listen.** Erfahrungsgemäß ist genau
das der Punkt, an dem Umstellungen scheitern – nicht an der Software.

### 9.3 Wie weit sollen Pickerle bzw. Frau Tarmann eingebunden werden?

Die Steuerberatung ist an **drei** Punkten einzubinden, sonst nirgends:

| Zeitpunkt | Beitrag | Aufwand |
| --- | --- | --- |
| **Vor der Entscheidung** (Woche 2–4) | Testimport eines Musterexports beider Anbieter in RZL; Vorgabe von Kontenrahmen und USt.-Schlüsseln | ca. 2–3 Stunden |
| **Bei der Konfiguration** (Woche 6) | Freigabe der Konten-/Steuerzuordnung, Behandlung von Kautionen und Stripe-Sammelauszahlungen | ca. 2 Stunden |
| **Beim ersten Monatsabschluss** (Woche 8/9) | Prüfung des ersten echten Exports, Bestätigung der Verbuchung | ca. 2 Stunden |

Die Buchhaltung sollte zusätzlich einen **lesenden Systemzugang** bekommen (Anforderung ADM-01) –
das erspart dauerhaft Rückfragen. Nicht einbinden würde ich sie in Auswahlgespräche zu Funktionen
außerhalb der Buchhaltung; das verlängert nur die Entscheidung.

### 9.4 Hat die neue Software eine Interessentenverfolgung?

Beide Systeme erfassen Online-Anfragen und abgebrochene Buchungen und verschicken automatisierte
Nachfass-Mails – das ist Standard in dieser Produktklasse. Was diese Systeme **nicht** sind:
ein vollwertiges CRM mit Vertriebspipeline. Für einen Standort ist das in aller Regel ausreichend.

**Prüffragen für die Demo:** Wo landet ein *telefonischer* Interessent? Gibt es eine
Wiedervorlage mit Aufgabe? Wird die Anfragequelle erfasst (damit Sie sehen, was Ihre
Werbung bringt)? Wird eine unvollständig gebliebene Online-Buchung automatisch nachgefasst?
Kinnovis hat dafür ein Aufgaben-Dashboard mit Zuweisung an die zuständige Person ✅ – prüfen Sie,
ob das den telefonischen Erstkontakt abdeckt.

### 9.5 Wie erfolgt die Evidenzhaltung gekündigter Verträge (Kündigungsfrist, förmliche Rückgabe)?

Das ist die Frage, die Standardsoftware am häufigsten nur halb beantwortet, und sie gehört
deshalb ausdrücklich ins Demo-Drehbuch. Fachlich brauchen Sie vier Dinge:

1. **Kündigungseingang** mit Datum, Kanal und Person – dokumentiert, nicht als Notiz.
2. **Fristenrechnung**: Kündigungsdatum + vereinbarte Frist = Vertragsende; das System muss das
   Ende berechnen, nicht Sie.
3. **Aufgabenliste bis zur Rückgabe**: Termin der Räumung, Zustandsprüfung, Schlüssel/Zutritt
   entzogen, Endabrechnung, Kautionsrückzahlung – idealerweise als Checkliste am Vertrag.
4. **Statuskette**: aktiv → gekündigt → geräumt → abgerechnet → abgeschlossen. Erst der letzte
   Status gibt die Einheit endgültig frei; „gekündigt" darf nicht schon als frei vermietbar gelten,
   sondern als „ab Datum X verfügbar" (das ist gleichzeitig Ihr wichtigstes Vertriebsinstrument).

**Prüffrage an beide Anbieter:** Bitte eine Kündigung mit vierwöchiger Frist zum Monatsende
anlegen und zeigen: berechnetes Vertragsende, Anzeige der Einheit als „ab … verfügbar",
Aufgabenliste bis zur Rückgabe, Endabrechnung, Zutrittsentzug, Kautionsrückzahlung.
Falls die Checkliste fehlt: ist eine Aufgabe/Erinnerung am Vertrag hinterlegbar?

### 9.6 Ist die neue Software cloudfähig?

Beide Produkte sind reine Cloud-Lösungen (SaaS) – es gibt gar keine lokale Installation.
Damit sind sie von jedem Gerät und Standort nutzbar, inklusive Tablet vor Ort. Die relevanten
Folgefragen sind nicht „cloudfähig ja/nein", sondern:

- **Wo liegen die Daten?** EU/EWR-Hosting und Auftragsverarbeitungsvertrag nach Art. 28 DSGVO
  sind K.o.-Kriterien (ADM-03).
- **Was passiert bei Internetausfall vor Ort?** Ohne Verbindung kein Systemzugriff – Zutritt und
  Notfallprozess müssen davon unabhängig funktionieren.
- **Wie kommen Sie wieder heraus?** Vollständiger Datenexport jederzeit und kostenfrei (ADM-05).
- **Wer beim Anbieter kann auf Ihre Produktivdaten zugreifen** und wird das protokolliert?

## 10. Fragenkatalog für die Demos (identisch an beide)

Diese Fragen entscheiden – nicht der Funktionsumfang. Bitte in dieser Reihenfolge stellen:

| Nr. | Frage | Warum |
| --- | --- | --- |
| F1 | Bitte einen echten Buchhaltungsexport eines Monats erzeugen und die Datei zeigen. Ist das Format konfigurierbar (Konten, Steuerschlüssel, österreichischer Kontenrahmen)? | RZL-Tauglichkeit ist Ihr wichtigstes Kriterium |
| F2 | Bitte eine Musterrechnung für einen österreichischen Firmenkunden zeigen – mit UID, USt.-Ausweis, fortlaufender Nummer. | § 11 UStG |
| F3 | Sind Vertrag, Rechnung, Mahnung und alle Kunden-E-Mails auf Deutsch und von uns selbst änderbar? Bitte einen Text live ändern. | Sprache ist K.o. |
| F4 | Können wir unter **unserer eigenen Gläubiger-ID** einziehen, und können wir die bestehenden Mandate mit IBAN, Referenz und Erteilungsdatum importieren? | Erhalt der Bestandsmandate |
| F4b | Erzeugt das System eine SEPA-Einzugsdatei (pain.008) für unser Electronic Banking, und können Bank- und Stripe-Einzug dauerhaft parallel laufen? | Voraussetzung für Modell A und C |
| F4c | Kann ein Bankkontoauszug (CAMT.053/MT940) eingelesen und automatisch zugeordnet werden? | einziger Weg, Überweisungen zu automatisieren |
| F5 | Wie werden Kautionen abgebildet – als Erlös oder als durchlaufender Posten? | steuerlich relevant |
| F6 | Bitte eine Kündigung mit Frist inklusive Rückgabeprozess vorführen (siehe 9.5). | Ihre Frage 5 |
| F7 | Wie wird ein telefonischer Interessent erfasst und nachverfolgt? | Ihre Frage 4 |
| F8 | Kann die Buchungsstrecke in unsere **bestehende** Website eingebunden werden, ohne sie zu ersetzen? | Sie haben eine Website |
| F9 | Wie erfolgt der Bankabgleich, und wie lösen Sie Stripe-Sammelauszahlungen für die Buchhaltung auf? | Ihre Frage 1 |
| F10 | Welche Zutrittssysteme sind integriert? *(Hersteller Ihrer Anlage einsetzen)* | Automatisierungsgrad |
| F11 | Wo liegen die Daten, gibt es einen AVV, und wie exportieren wir alles wieder? | DSGVO und Ausstieg |
| F12 | Was kostet die Lösung in 36 Monaten – inklusive aller Module und Zahlungsentgelte? | TCO |

## 11. Vorläufige Bewertung

Punkte 0–5 je Kriterium, gewichtet nach [`bewertungsmodell.md`](bewertungsmodell.md).
**D2 (Kosten) und D3 (Einführbarkeit) sind noch nicht bewertbar** – dafür fehlen die Angebote.

| Kriterium | Gewicht | Kinnovis | Stora | Begründung |
| --- | --- | --- | --- | --- |
| Zahlungswege und Mandatserhalt | **hoch** | 5 | 3 | SEPA-XML erhält Bestandsmandate ohne Kundenaktion; Stora erfordert die Umstellung auf Stripe |
| Funktionale Abdeckung Phase 1 | hoch | 4 | 4 | beide decken den Kern ab |
| Funktionale Abdeckung Phase 2 | mittel | 4 | 4 | beide im Standard |
| Buchhaltung/RZL | **hoch** | 4 | 2 | DATEV-Report vs. nur Xero |
| Sprache und AT-Rechtsraum | **hoch** | 4 | 2 | Herkunft Österreich, deutschsprachiger Auftritt |
| Zahlungsarten und -kosten | hoch | 4 | 3 | zusätzlich SEPA-XML ohne Provider |
| Zutrittskontrolle DACH | mittel | 5 | 3 | Sensorberg, Tapkey, eigene Lösung |
| Preistransparenz | mittel | 2 | 5 | öffentliche Preise, keine Bindung |
| Ertragssteuerung/dynamische Preise | niedrig | 3 | 5 | Revenue Management bei Stora stärker |
| Ausgereiftheit Buchungsstrecke | mittel | 4 | 5 | Produktkern von Stora |
| **Tendenz** | | **stärker** | | Vorsprung im Rechts- und Buchhaltungsteil, der für Sie am schwersten wiegt |

## 12. Empfehlung und nächste Schritte

1. **Beide Anbieter zur Demo einladen** – die Entscheidung nicht vorwegnehmen. Stora kann über
   Preis, Bedienung und Buchungsstrecke gewinnen, wenn die AT-Punkte belegbar erfüllt sind.
2. **Vor den Demos**: Musterexport für die Buchhaltung anfordern (F1) und an die Steuerberatung
   zum Testimport in RZL geben. Das ist das schnellste Ausschlusskriterium.
3. **Parallel und sofort**: Klären, ob die Zahlungsdaten aus dem heutigen Zoho-Setup übernehmbar
   sind (Abschnitt 8). Falls nein, startet die Mandatsneueinholung sofort – sie ist der längste
   Vorlauf im ganzen Projekt.
4. **Angebote über 36 Monate** anfordern, bei Stora mit ausdrücklicher Tarifzuordnung.
5. **Entscheidung** in der Woche nach den Demos, dokumentiert im Entscheidungslog.

> Wenn sich in den Demos herausstellt, dass **beide** Anbieter die österreichische
> Rechnungs- und Buchhaltungslogik nicht sauber abbilden, ist die Kombination
> „Fachsystem für Betrieb + österreichisches Fakturierungs-/Buchhaltungssystem" der
> nächste Prüfschritt – nicht die Aufgabe des Projektziels. Das ist in der Longlist
> als Weg B bereits vorbereitet.
