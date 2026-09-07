# Arbeitsweise im Projekt

Das gesamte Projektmanagement läuft über dieses GitHub-Repository. Es gibt keine zweite
Aufgabenliste, keinen parallelen Aufgabenversand per E-Mail und keine Aufgaben, die nur in
einem Meeting-Protokoll stehen.

## 1. Die zwei Quellen der Wahrheit

| Was | Wo | Bedeutung |
| --- | --- | --- |
| **Arbeitsstand** – wer macht was bis wann, was ist offen | **GitHub Issues** | Wenn es keine Issue gibt, passiert es nicht |
| **Inhalte** – Anforderungen, Analysen, Pläne, Entscheidungen | **Dateien im Repository** | Ergebnisse werden ins Repository geschrieben, nicht in Issue-Kommentare |

Faustregel: Eine Issue beschreibt die **Arbeit**, das Repository enthält das **Ergebnis**.
Eine Issue wird geschlossen, wenn das Ergebnis im Repository liegt.

## 2. Team und Rollen

| Person | Rolle | Schwerpunkt |
| --- | --- | --- |
| Peter | Projektleitung, Auftraggeberseite | Steuerung, Entscheidungen, Steuerberatung und Bank |
| Martin | Umsetzung | Repository, Migration, Anbieterkoordination |
| Martina | Fachverantwortung Betrieb | Cutover-Szenario, Archivierung, Tagesgeschäft |
| Geschäftsführung | Auftraggeber | Freigaben, Anbieterentscheidung, Go-/No-Go |
| accilium | Beratung | Analyse, Auswahl, Migrationssteuerung, Dokumentation |
| Pickerle / Frau Tarmann | Steuerberatung (extern) | RZL-Schnittstelle, Kontenrahmen, SEPA-Fragen |
| Sepp | Buchhaltung (extern) | Spezifikation des Datenaustauschs |

Namen bitte ergänzen oder korrigieren, sobald die GitHub-Benutzernamen feststehen – dann auch
in `.github/CODEOWNERS` eintragen.

## 3. Issues

**Für jede Aufgabe eine Issue.** Vorlagen liegen bereit und werden beim Anlegen angeboten:

| Vorlage | Wofür |
| --- | --- |
| Aufgabe / Arbeitspaket | konkrete Arbeit mit Ergebnis und Termin |
| Entscheidungsbedarf | eine Frage, die entschieden werden muss |
| Risiko | etwas, das Termin, Kosten oder Qualität gefährdet |
| Frage an einen Anbieter | Punkte für RFP und Demo |

Pflichtangaben in jeder Issue: **Ergebnis**, **verantwortliche Person** (auch als Assignee),
**Termin**. Ohne diese drei ist eine Issue unvollständig.

## 4. Labels

Drei Ebenen, kombinierbar. Das vollständige Schema mit Farben steht in
[`.github/labels.md`](.github/labels.md).

| Ebene | Beispiele |
| --- | --- |
| Typ | `aufgabe`, `entscheidung`, `risiko`, `anbieterfrage`, `dokumentation` |
| Bereich | `bereich:zahlungen`, `bereich:buchhaltung`, `bereich:migration`, `bereich:anforderungen`, `bereich:auswahl`, `bereich:betrieb`, `bereich:kommunikation`, `bereich:recht` |
| Steuerung | `kritischer-pfad`, `blockiert`, `prio:hoch`, `prio:mittel`, `prio:niedrig` |
| Anbieter | `anbieter:kinnovis`, `anbieter:stora`, `anbieter:store365` |

`kritischer-pfad` ist kein Schmuck: Diese Issues werden im Jour fixe zuerst durchgegangen.

> **Noch zu erledigen:** Die Labels und die Meilensteine sind im Repository noch nicht angelegt.
> Die Befehle dafür stehen in [`.github/labels.md`](.github/labels.md) und sind einmalig
> auszuführen. Die bereits angelegten Issues nennen die vorgesehenen Labels im Text; sie können
> danach in einem Durchgang gesetzt werden.

## 5. Meilensteine

Jede Issue gehört zu einem Meilenstein. Die Meilensteine bilden den Projektplan ab
(siehe [`00_management/projektplan_8_wochen.md`](00_management/projektplan_8_wochen.md)):

| Meilenstein | Fällig | Inhalt |
| --- | --- | --- |
| M1 Ist-Bild und Projektauftrag | 11.09.2026 | Prozesse, Daten, Mandate erhoben |
| M2 Anforderungen und Anbieteransprache | 18.09.2026 | Katalog freigegeben, Fragen versendet |
| M3 Demos und RZL-Test | 25.09.2026 | Demo Kinnovis, Testimport in RZL |
| M4 Angebote bewertet | 02.10.2026 | Lizenzmodell, Preise, Bindungsdauer geklärt |
| M5 Anbieter beauftragt | 09.10.2026 | Entscheidung und Vertrag – kritischster Termin |
| M6 Konfiguration und Migrationstest 1 | 16.10.2026 | Testumgebung steht |
| M7 Abnahme und Go-/No-Go | 23.10.2026 | Testprotokoll, Schulung |
| M8 Go-Live | 01.11.2026 | Neues System produktiv |
| M9 Parallelbetrieb und Abgleich | 31.12.2026 | Zoho läuft mit, Abweichungen geklärt |
| M10 Sundown Zoho und Archivierung | 31.01.2027 | Altsystem abgeschaltet, Archiv gesichert |

## 6. Projektboard

Ein Board („deinPlatz Kernsystem") mit fünf Spalten:

`Backlog` → `Diese Woche` → `In Arbeit` → `Wartet auf Dritte` → `Erledigt`

Die Spalte **Wartet auf Dritte** ist wichtig: Anbieter, Bank und Steuerberatung bestimmen in
diesem Projekt einen großen Teil des Takts. Was dort liegt, braucht ein Nachfassdatum im Issue-Text.

## 7. Branches und Pull Requests

- `main` ist immer der gültige Projektstand.
- Gearbeitet wird auf Zweigen: `doku/<kurzbeschreibung>`, `plan/<kurzbeschreibung>`,
  `anforderung/<id>` – zum Beispiel `doku/mandatsliste` oder `anforderung/abr-18`.
- Ein Pull Request je inhaltlicher Änderung, mit Verweis auf die Issue (`Fixes #12`).
- Mindestens eine prüfende Person. Bei Änderungen an Anforderungen, Terminen oder
  Entscheidungen prüft die Projektleitung.
- Die Vorlage in [`.github/pull_request_template.md`](.github/pull_request_template.md) enthält
  die Prüfliste; sie ist ernst gemeint.

Kleine Korrekturen (Tippfehler, tote Verweise) dürfen direkt auf `main`.

## 8. Konventionen für Inhalte

Die inhaltlichen Regeln stehen in [`CLAUDE.md`](CLAUDE.md) und gelten für alle:

- Alles auf Deutsch, Commit-Messages im Imperativ.
- Dateinamen klein, `snake_case`, ohne Umlaute.
- Anforderungen werden in `20_anforderungen/anforderungen.csv` gepflegt; danach
  `python3 werkzeuge/anforderungen_tabelle.py` ausführen, damit der Katalog dazu passt.
- Entscheidungen **immer** in `00_management/entscheidungslog.md`, nicht nur in der Issue.
- Externe Aussagen mit Quelle in `90_quellen/recherchequellen.md`.
- Unverifizierte Aussagen mit `ANNAHME:` kennzeichnen.

## 9. Vertraulichkeit

**Niemals im Repository:** Kundendaten, Exporte aus Zoho, IBAN oder Mandatsreferenzen,
Ausweiskopien, unterschriebene Verträge, Angebote mit Preisen.
Diese Unterlagen gehören in die vereinbarte geschützte Ablage; im Repository steht nur der Verweis.
Die `.gitignore` fängt die häufigsten Fälle ab, ersetzt aber kein Nachdenken.

## 10. Rhythmus

| Termin | Wann | Inhalt |
| --- | --- | --- |
| Jour fixe | wöchentlich | Board durchgehen, beginnend bei `kritischer-pfad` |
| Kurz-Standup | täglich in der Umsetzungsphase | Blockaden |
| Meilensteintermin | zu M1 bis M10 | Freigabe oder Eskalation |

Verzug von mehr als drei Tagen auf dem kritischen Pfad wird sofort an die Projektleitung
gemeldet – über einen Kommentar in der Issue und mit dem Label `blockiert`.
