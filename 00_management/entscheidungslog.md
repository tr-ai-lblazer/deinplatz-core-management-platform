# Entscheidungslog

Jede Festlegung mit Auswirkung auf Umfang, Kosten, Termine oder Architektur wird hier
dokumentiert – auch, wenn sie mündlich getroffen wurde. Format: fortlaufende ID, kein Löschen;
revidierte Entscheidungen werden als „ersetzt durch E-xx" markiert.

| ID | Datum | Thema | Entscheidung | Begründung | Entschieden von | Status |
| --- | --- | --- | --- | --- | --- | --- |
| E-01 | 06.09.2026 | Projektsprache | Das gesamte Projekt inklusive Repository wird auf Deutsch geführt | Anforderung des Auftraggebers, Team- und Kundenkommunikation in Deutsch | Auftraggeber | gültig |
| E-02 | 06.09.2026 | Lösungsstrategie | Standard-SaaS wird gegenüber Individualentwicklung und Low-Code-Eigenbau bevorzugt | 8-Wochen-Zeitrahmen, Kleinbetrieb ohne eigene IT, Wartbarkeit | Beratung (Vorschlag), GF bestätigt noch | vorläufig |
| E-03 | 06.09.2026 | Repository-Struktur | Nummerierte Ordner entlang der Projektphasen, Anforderungen zusätzlich als CSV | Nachvollziehbarkeit, Weiterverarbeitung in Excel | Beratung | gültig |
| E-04 | 06.09.2026 | Shortlist | Die Auswahl wird auf **Kinnovis** und **Stora** eingegrenzt | Vorgabe des Auftraggebers; beide sind Fachsysteme mit europäischer Ausrichtung | Auftraggeber | gültig |
| E-05 | 06.09.2026 | Umfang Go-Live | Phasung laut Kundendokument: Phase 1 = RZL-Schnittstelle, Online-Vertrag inkl. Identitätsprüfung, monatliche Fakturierung, wählbare Zahlungsart, Website-Einbindung, automatisierte E-Mails; Phase 2 = Buchungsportal, Kundenportal, Anlageplan | Fokus auf den Kernbetrieb, Portale nach Stabilisierung | Auftraggeber | gültig |
| E-06 | 06.09.2026 | Buchhaltungsformat | Zielformat ist **RZL** (Steuerberatung); DATEV-CSV gilt als zulässiger Zwischenweg, sofern der Import in RZL nachgewiesen ist | RZL ist gesetzt, Anbieter liefern kein natives RZL-Format | Auftraggeber / Beratung | gültig |
| E-07 | 06.09.2026 | Zahlungsstrategie (Empfehlung) | SEPA-Lastschrift als Standardzahlungsart, Karte als Ausweichoption | Kostenwirkung: bei Kartendominanz übersteigen die Zahlungsentgelte die Softwarekosten (Benchmark, Abschnitt 6.2) | Beratung (Vorschlag), GF offen | vorläufig |

## Offene Entscheidungen (Entscheidungsbedarf)

| Nr. | Frage | Benötigt bis | Entscheidet |
| --- | --- | --- | --- |
| O-01 | ~~Fachsystem oder generischer Stack?~~ **Beantwortet:** Fachsystem, Shortlist Kinnovis/Stora (E-04) | – | erledigt |
| O-02 | ~~Buchungsstrecke zum Go-Live?~~ **Beantwortet:** Phase 2 (E-05) | – | erledigt |
| O-03 | ~~Exportformat der Steuerberatung?~~ **Beantwortet:** RZL (E-06). Offen bleibt der **Nachweis des Importwegs** – Musterexport beider Anbieter testweise in RZL importieren | vor der Entscheidung | Steuerberatung |
| O-04 | Bleiben Barzahlungen am Standort möglich? (bestimmt Registrierkassen-Thematik) | Ende W2 | GF + Steuerberatung |
| O-05 | Welcher Zahlungsdienstleister steht heute hinter Zoho, wem gehört das Konto, gibt es eine eigene SEPA-Gläubiger-ID? | **Woche 1** | PL |
| O-06 | Können die bestehenden Mandate übernommen werden oder müssen sie neu eingeholt werden? (IBAN fehlt im Zoho-Export) | **Woche 1–2** | GF + Zahlungsdienstleister |
| O-08 | Wo ist die Zuordnung Kunde ↔ Lagerabteil heute dokumentiert, und stimmt sie mit der Realität überein? | Woche 1 | Fachverantwortung Betrieb |
| O-09 | Wird die Ausweiskopie dauerhaft gespeichert – und mit welcher Rechtsgrundlage? | Ende W2 | GF + Rechtsberatung |
| O-07 | Budgetrahmen verbindlich | Ende W2 | GF |
