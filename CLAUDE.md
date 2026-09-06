# Arbeitsanweisungen für dieses Repository

## Sprache
- **Alles auf Deutsch**: Dokumente, Tabellenüberschriften, Commit-Messages, Antworten im Chat.
- Fachbegriffe, die im Markt englisch etabliert sind (z. B. „Self-Storage", „Cutover",
  „Delinquency Management"), dürfen englisch bleiben; erklärt wird auf Deutsch.
- Sie-Form in kundengerichteten Texten (RFP, Anschreiben), sachlich-neutral in internen Dokumenten.

## Inhaltliche Regeln
- **Fakten belegen.** Jede extern recherchierte Aussage (Anbieter, Preis, Rechtslage) bekommt
  eine Quelle in `90_quellen/recherchequellen.md`. Preise und Funktionsumfänge ändern sich –
  immer mit Stand-Datum versehen.
- **Annahmen kennzeichnen.** Nicht verifizierte Aussagen über deinPlatz beginnen mit `ANNAHME:`.
  Nach der Verifikation wird die Markierung entfernt und die Quelle (Workshop, Interview) genannt.
- **Keine Rechts- oder Steuerberatung.** Rechtliche Punkte (RKSV, Gebührenpflicht, DSGVO)
  werden als Prüfauftrag an Steuerberatung/Rechtsberatung formuliert, nicht als abschließendes Urteil.
- **Keine echten Kundendaten im Repository.** Migrationsanalysen nur mit anonymisierten
  Beispielen oder Feldbeschreibungen. Exporte gehören in `/vertraulich/` (gitignored).

## Struktur- und Formatkonventionen
- Nummerierte Ordner (`00_` … `90_`) geben die Projektlogik vor; neue Dokumente in den passenden Ordner.
- Dateinamen: klein, `snake_case`, deutsch, ohne Umlaute (`rechtliche_rahmenbedingungen_at.md`).
- Anforderungs-IDs: `<DOMÄNE>-<NR>`, z. B. `ABR-07`. IDs werden nie wiederverwendet oder umnummeriert.
- Tabellen in Markdown; strukturierte Daten zusätzlich als CSV (Semikolon-getrennt, UTF-8),
  damit sie in Excel/Sheets weiterverarbeitet werden können.
- Entscheidungen werden **immer** in `00_management/entscheidungslog.md` ergänzt, nicht nur im Fließtext.

## Commits
- Deutsche Commit-Messages im Imperativ, z. B. `Anforderungskatalog um Zutrittskontrolle ergaenzt`.
- Ein Commit = eine inhaltliche Änderung.

## Arbeitsstand aktuell
Phase 1 (Analyse & Anforderungen) läuft. Der Ist-Zustand ist noch nicht erhoben –
vor inhaltlichen Aussagen zum Bestandssystem immer `10_analyse/ist_aufnahme_leitfaden.md` prüfen.
