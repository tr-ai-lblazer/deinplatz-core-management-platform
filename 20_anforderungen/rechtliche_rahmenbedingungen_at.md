# Rechtliche Rahmenbedingungen Österreich (Systemanforderungen)

Stand der Recherche: 06.09.2026 · Quellen: [`../90_quellen/recherchequellen.md`](../90_quellen/recherchequellen.md)

> **Kein Ersatz für Rechts- oder Steuerberatung.** Dieses Dokument übersetzt die
> Rechtslage in Anforderungen an das System und benennt offene Prüfaufträge an
> Steuerberatung bzw. Rechtsberatung. Verbindliche Aussagen trifft die jeweilige Beratung.

## 1. Registrierkassen- und Belegerteilungspflicht (RKSV)

**Sachlage:** Registrierkassenpflicht besteht ab einem Jahresumsatz von 15.000 € je Betrieb,
sofern die **Barumsätze** dieses Betriebs 7.500 € im Jahr überschreiten – beide Werte müssen
zusammentreffen. Als Barumsatz gelten auch Zahlungen mit Bankomat- oder Kreditkarte **vor Ort**,
Barschecks sowie eingelöste Gutscheine. **Nicht** als Barumsatz gelten Online-Überweisungen,
PayPal und Einziehungsaufträge (Lastschrift). Die Belegerteilungspflicht gilt unabhängig davon
für jeden Barumsatz. Ab 1. Oktober 2026 darf der Beleg elektronisch zum Auslesen bereitgestellt
werden (z. B. QR-Code am Display); auf Wunsch bleibt der Papierbeleg verpflichtend.

**Bedeutung für deinPlatz:** Werden Mieten überwiegend per SEPA-Lastschrift oder Überweisung
bezahlt, fällt der Großteil des Umsatzes **nicht** unter „Barumsatz". Entscheidend ist,
wie viel bar bzw. per Karte vor Ort kassiert wird (Mieten, Kaution, Schlösser, Kartons).

**Anforderungen an das System:**
- Wenn Barumsätze über der Grenze liegen: RKSV-konforme Kassenlösung mit Signatureinrichtung,
  Datenerfassungsprotokoll, Startbeleg/Monats-/Jahresbeleg und FinanzOnline-Registrierung –
  entweder im Kernsystem enthalten oder als angebundenes Kassensystem (siehe ABR-10).
- In jedem Fall: Belegausgabe bei Barzahlung, elektronisch oder auf Papier.

**Prüfauftrag P1 (Steuerberatung):** Höhe der tatsächlichen Barumsätze und daraus folgende
Registrierkassenpflicht; falls einschlägig, empfohlene Kassenlösung und deren Zusammenspiel
mit dem neuen Kernsystem. → Ergebnis in `00_management/entscheidungslog.md` (O-04).

## 2. Rechnungslegung und Umsatzsteuer

**Anforderungen an das System:**
- Pflichtangaben der Rechnung nach § 11 UStG (Name/Anschrift beider Seiten, Menge/Bezeichnung
  der Leistung, Leistungszeitraum, Entgelt, Steuersatz und Steuerbetrag, fortlaufende Nummer,
  Ausstellungsdatum, UID des Leistenden; UID des Empfängers ab 10.000 € Rechnungsbetrag).
- Korrekte Steuersätze je Leistungsart: Vermietung von Lagerflächen, Warenverkauf und
  Versicherungsleistungen können unterschiedlich zu behandeln sein → siehe Prüfauftrag P2.
- Kleinbetragsrechnungen, Gutschriften und Storni müssen sauber abbildbar sein (ABR-08).
- Rechnungsnummernkreis lückenlos, nachträgliche Änderung versendeter Belege ausgeschlossen (BUH-03).

**Prüfauftrag P2 (Steuerberatung):** Umsatzsteuerliche Behandlung von Lagerabteilmiete,
Zusatzleistungen (Versicherung, Schlösser, Kartons), Kaution und Mahnspesen; Vorgabe der
Erlöskonten und Steuerschlüssel für die Systemkonfiguration.

## 3. E-Rechnung

**Sachlage:** Gegenüber Bundesdienststellen ist die elektronische Rechnung seit 2014 verpflichtend,
akzeptiert werden ebInterface (ab Version 4.3) und Peppol BIS Billing 3.0. Eine allgemeine
B2B-E-Rechnungspflicht besteht in Österreich mit Stand 2026 **nicht**; ein konkretes Datum ist
nicht beschlossen. Auf EU-Ebene bringt die ViDA-Richtlinie (EU) 2025/516 ab 1. Juli 2030
Verpflichtungen für innergemeinschaftliche B2B-Umsätze; rein inländische Umsätze sind davon
nicht unmittelbar betroffen.

**Bedeutung:** Für deinPlatz derzeit kein Muss, aber ein Zukunftskriterium. Deshalb ist
ABR-12 (Unterstützung strukturierter E-Rechnungsformate) als „Kann" eingestuft; die
Roadmap-Aussage des Anbieters wird trotzdem abgefragt.

## 4. SEPA-Lastschrift

**Anforderungen an das System:**
- Verwaltung von SEPA-Mandaten inkl. eindeutiger Mandatsreferenz, Gläubiger-ID (Creditor
  Identifier, in Österreich über die OeNB zu beziehen), Datum der Mandatserteilung und Nachweis.
- Vorabinformation (Pre-Notification) an die Kundin/den Kunden vor dem Einzug mit Betrag und
  Fälligkeitsdatum; die Frist ist vertraglich vereinbar und in den Mietvertrag aufzunehmen.
- Verarbeitung von Rücklastschriften inkl. Entgelten und automatischer Übergabe ins Mahnwesen (ABR-04).
- Beim Wechsel des Zahlungsdienstleisters ist zu klären, ob bestehende Mandate weiter genutzt
  werden können oder neu einzuholen sind (Risiko R03, Entscheidung O-06).

## 5. Datenschutz (DSGVO)

**Anforderungen an das System:**
- Auftragsverarbeitungsvertrag nach Art. 28 DSGVO mit dem Anbieter, Liste der
  Unterauftragsverarbeiter, Hosting vorzugsweise in der EU/EWR (ADM-03, NFA-11/12).
- Rollen- und Rechtekonzept, Protokollierung von Zugriffen und Änderungen (ADM-01/02).
- Umsetzung von Betroffenenrechten: Auskunft, Berichtigung, Löschung, Datenübertragbarkeit –
  praktisch heißt das: Kundendaten müssen exportier- und löschbar sein (ADM-04/05).
- Löschkonzept mit Fristen je Datenkategorie (siehe `10_analyse/datenobjekte.md`).
- Verzeichnis der Verarbeitungstätigkeiten ist um das neue System zu ergänzen.
- Videoüberwachung am Standort ist datenschutzrechtlich getrennt zu betrachten
  (Zweckbindung, kurze Speicherdauer, Hinweisbeschilderung) und nicht Teil des Kernsystems.

**Prüfauftrag P3 (Datenschutz/Recht):** Aktualisierung von Verarbeitungsverzeichnis,
Datenschutzerklärung und Informationspflichten (Art. 13) zum Go-Live, insbesondere für
Online-Buchung und Kundenportal.

## 6. Aufbewahrungspflichten und Unveränderbarkeit

- Bücher, Aufzeichnungen und Belege sind grundsätzlich **sieben Jahre** aufzubewahren
  (§ 132 BAO); bei anhängigen Verfahren länger. Die Aufbewahrung muss die Daten
  **maschinell auswertbar** halten.
- Konsequenz für die Systemauswahl: Der Anbieter muss entweder die Belege über die gesamte
  Frist vorhalten **oder** einen vollständigen, dauerhaft lesbaren Export ermöglichen
  (NFA-18 bis NFA-21). Das gilt auch für das **Altsystem** – vor dessen Abschaltung ist ein
  revisionssicheres Archiv zu erstellen (siehe `50_umsetzung/cutover_go_live.md`).

## 7. Verbraucherrecht bei Online-Buchung

Sobald Verträge online mit Verbraucherinnen und Verbrauchern geschlossen werden, greifen
Fernabsatzregeln (FAGG/KSchG) und das E-Commerce-Gesetz:
Informationspflichten vor Vertragsabschluss, Button-Lösung („zahlungspflichtig bestellen"),
Widerrufsbelehrung samt Musterformular, AGB-Einbindung, Impressum.

**Anforderung:** Die Buchungsstrecke muss diese Elemente in deutscher Sprache abbilden
und die Texte müssen selbst pflegbar sein (BUC-04).

**Prüfauftrag P4 (Rechtsberatung):** Prüfung von Mietvertragsmuster, AGB, Widerrufsbelehrung
und Hausordnung für den Online-Abschluss.

## 8. Weitere Klärungspunkte

| Nr. | Thema | Frage | Adressat |
| --- | --- | --- | --- |
| P5 | Rechtsgeschäftsgebühr auf Bestandverträge (§ 33 TP 5 GebG) | Unterliegen die Mietverträge über Lagerabteile der Bestandvertragsgebühr, und muss das System die Bemessungsgrundlage liefern? | Steuerberatung |
| P6 | Vertragstyp | Sind die Verträge als Bestandverträge oder als Verwahrungsverträge ausgestaltet – mit Folgen für Kündigungsfristen und Verwertungsrecht bei Zahlungsverzug? | Rechtsberatung |
| P7 | Verwertung bei Zahlungsverzug | Zulässiger Ablauf von Sperre, Zurückbehaltung und Verwertung des Lagerguts inkl. Fristen und Dokumentation im System | Rechtsberatung |
| P8 | Versicherung des Lagerguts | Vermittlung/Weiterverrechnung von Versicherungen: gewerberechtliche und steuerliche Behandlung | Steuer-/Rechtsberatung |

Alle Prüfaufträge sind bis Ende Woche 2 zu adressieren, da sie K.o.-Kriterien im RFP beeinflussen.
