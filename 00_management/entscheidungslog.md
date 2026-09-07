# Entscheidungslog

Jede Festlegung mit Auswirkung auf Umfang, Kosten, Termine oder Architektur wird hier
dokumentiert – auch, wenn sie mündlich getroffen wurde. Format: fortlaufende ID, kein Löschen;
revidierte Entscheidungen werden als „ersetzt durch E-xx" markiert.

| ID | Datum | Thema | Entscheidung | Begründung | Entschieden von | Status |
| --- | --- | --- | --- | --- | --- | --- |
| E-01 | 06.09.2026 | Projektsprache | Das gesamte Projekt inklusive Repository wird auf Deutsch geführt | Anforderung des Auftraggebers, Team- und Kundenkommunikation in Deutsch | Auftraggeber | gültig |
| E-02 | 06.09.2026 | Lösungsstrategie | Standard-SaaS wird gegenüber Individualentwicklung und Low-Code-Eigenbau bevorzugt | 8-Wochen-Zeitrahmen, Kleinbetrieb ohne eigene IT, Wartbarkeit | Beratung (Vorschlag), GF bestätigt noch | vorläufig |
| E-03 | 06.09.2026 | Repository-Struktur | Nummerierte Ordner entlang der Projektphasen, Anforderungen zusätzlich als CSV | Nachvollziehbarkeit, Weiterverarbeitung in Excel | Beratung | gültig |
| E-04 | 06.09.2026 | Shortlist | Die Auswahl wird auf **Kinnovis** und **Stora** eingegrenzt | Vorgabe des Auftraggebers | Auftraggeber | ersetzt durch E-09 |
| E-05 | 06.09.2026 | Umfang Go-Live | Phasung laut Kundendokument: Phase 1 = RZL-Schnittstelle, Online-Vertrag inkl. Identitätsprüfung, monatliche Fakturierung, wählbare Zahlungsart, Website-Einbindung, automatisierte E-Mails; Phase 2 = Buchungsportal, Kundenportal, Anlageplan | Fokus auf den Kernbetrieb, Portale nach Stabilisierung | Auftraggeber | gültig |
| E-06 | 06.09.2026 | Buchhaltungsformat | Zielformat ist **RZL** (Steuerberatung); DATEV-CSV gilt als zulässiger Zwischenweg, sofern der Import in RZL nachgewiesen ist | RZL ist gesetzt, Anbieter liefern kein natives RZL-Format | Auftraggeber / Beratung | gültig |
| E-07 | 06.09.2026 | Zahlungsstrategie (Empfehlung) | SEPA-Lastschrift als Standardzahlungsart, Karte als Ausweichoption | Kostenwirkung: bei Kartendominanz übersteigen die Zahlungsentgelte die Softwarekosten | Beratung (Vorschlag), GF offen | vorläufig |
| E-13 | 07.09.2026 | Kundenkommunikation | Die rund 250 Kundinnen und Kunden werden **einmal** informiert, als reine Info-Mail ohne neue Unterschrift | Doppelte Ansprache wegen System- und Gesellschaftswechsel vermeiden, keine Verlängerungs- oder Kündigungsentscheidungen auslösen | Stakeholder-Termin | gültig |
| E-12 | 07.09.2026 | Zahlungsabwicklung | Stripe wird **zunächst nur für künftige Kunden** eingesetzt, der Bestand bleibt beim Einzug über die eigene Bank | Bestätigt das Hybridmodell (E-08); Kostenwirkung rund 2.000–2.800 € pro Jahr, Mandate bleiben unangetastet | Stakeholder-Termin | gültig |
| E-11 | 07.09.2026 | Go-Live und Übergang | **Go-Live am 01.11.2026.** Zoho läuft zunächst weiter; Nebeneinander bis zum Jahreswechsel, längstens bis Januar 2027 | Schrittweise Absicherung des Übergangs, Vergleich von Abweichungen | Stakeholder-Termin | gültig |
| E-10 | 07.09.2026 | Auswahlfokus | **Kinnovis wird als erster Kandidat in die Demo geführt**; Lizenzmodell, Preise und Bindungsdauer sind dort zu klären | Ergebnis des Benchmarks und Vorgabe aus dem Termin; Stora und Store365 bleiben als Alternativen bestehen | Stakeholder-Termin | gültig |
| E-09 | 06.09.2026 | Shortlist erweitert | **Store365 (Store-IT B.V.)** wird als dritter Kandidat in den Benchmark aufgenommen; Shortlist damit Kinnovis, Stora, Store365 | Vorgabe des Auftraggebers; Store365 ist seit 2000 am Markt, deutschsprachig betreut und ISO 27001 zertifiziert | Auftraggeber | gültig |
| E-08 | 06.09.2026 | Betriebsmodell Zahlungsabwicklung (Empfehlung) | **Hybrid:** Bestand weiter über die eigene Bank (SEPA-XML, eigene Gläubiger-ID), Neuverträge und Online-Buchungen über Stripe | Bestandsmandate bleiben unverändert gültig, Automatisierungsgrad wächst ohne Umstellungsaktion; setzt SEPA-XML-Export voraus (ABR-15) | Beratung (Vorschlag), GF offen | vorläufig |

## Offene Entscheidungen (Entscheidungsbedarf)

| Nr. | Frage | Benötigt bis | Entscheidet |
| --- | --- | --- | --- |
| O-01 | ~~Fachsystem oder generischer Stack?~~ **Beantwortet:** Fachsystem, Shortlist Kinnovis/Stora (E-04) | – | erledigt |
| O-02 | ~~Buchungsstrecke zum Go-Live?~~ **Beantwortet:** Phase 2 (E-05) | – | erledigt |
| O-03 | ~~Exportformat der Steuerberatung?~~ **Beantwortet:** RZL (E-06). Offen bleibt der **Nachweis des Importwegs** – Musterexport beider Anbieter testweise in RZL importieren | vor der Entscheidung | Steuerberatung |
| O-04 | Bleiben Barzahlungen am Standort möglich? (bestimmt Registrierkassen-Thematik) | Ende W2 | GF + Steuerberatung |
| O-05 | ~~Zahlungsdienstleister und Gläubiger-ID?~~ **Beantwortet:** SEPA über eigenes Bankkonto mit eigener Gläubiger-ID plus Überweisungen | – | erledigt |
| O-06 | ~~Mandate übernehmbar?~~ **Weitgehend beantwortet:** deinPlatz ist selbst Gläubiger, die Mandate bleiben gültig. Offen bleibt die Beschaffung von IBAN und Mandatsreferenz aus den eigenen Unterlagen | Woche 1 | Finanzen |
| O-10 | Wird Stripe eingesetzt: eigene oder Stripe-Gläubiger-ID? Die Entscheidung ist nach der ersten Live-Zahlung **nicht mehr änderbar** | vor Go-Live | GF + Anbieter |
| O-11 | Bietet das System einen Kontoauszugsimport (CAMT.053/MT940)? Davon hängt ab, ob Überweisungen automatisiert abgeglichen werden können | Demo | Beratung |
| O-12 | **Gehen die bestehenden SEPA-Mandate und die Gläubiger-ID beim Wechsel vom Einzelunternehmen zur GmbH über, oder müssen sie neu eingerichtet werden?** | **KW 38** | Peter mit Bank und Steuerberatung |
| O-13 | Lizenzmodell von Kinnovis: Wie hoch ist der umsatzabhängige Anteil (im Termin genannt: 0,7 % des Plattformumsatzes), und wofür fällt er an? | mit der Demo | Martin |
| O-14 | Was bedeutet „Parallelbetrieb" konkret – Schattenbetrieb mit einem führenden System (Empfehlung) oder echte Doppelpflege? | vor dem Go-Live | GF |
| O-15 | Wird die Preisanpassung zum 01.01.2027 gemeinsam mit der Umstellungsinformation kommuniziert oder getrennt? | KW 40 | GF |
| O-16 | Zu welchem Stichtag wird der Rechtsformwechsel wirksam? Er bestimmt die Reihenfolge von System- und Gläubigerwechsel | KW 39 | Peter |
| O-08 | Wo ist die Zuordnung Kunde ↔ Lagerabteil heute dokumentiert, und stimmt sie mit der Realität überein? | Woche 1 | Fachverantwortung Betrieb |
| O-09 | Wird die Ausweiskopie dauerhaft gespeichert – und mit welcher Rechtsgrundlage? | Ende W2 | GF + Rechtsberatung |
| O-07 | Budgetrahmen verbindlich | Ende W2 | GF |
