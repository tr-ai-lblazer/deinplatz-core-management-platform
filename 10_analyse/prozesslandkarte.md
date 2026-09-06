# Prozesslandkarte (Soll-Sicht Self-Storage)

Die Landkarte beschreibt die Prozesse, die das neue Kernsystem abdecken muss. Sie dient in
Woche 1 als Raster für die Ist-Aufnahme und in Woche 3/4 als Drehbuch für die Anbieterdemos.
Die Kürzel in Klammern verweisen auf die Anforderungsdomänen in `20_anforderungen/anforderungskatalog.md`.

## Kernprozess: Vom Interessenten zum zahlenden Mieter

```
Anfrage ──► Verfügbarkeit ──► Angebot/Reservierung ──► Vertrag ──► Zutritt ──► Abrechnung
 (KOM)        (OBJ)              (BUC)                  (VER)      (ZUT)       (ABR)
                                                                                 │
                              Kündigung ◄── Vertragsänderung ◄── Zahlung/Mahnung ┘
                                (VER)          (VER/PRI)            (ABR/MAH)
```

## 1. Anfrage und Beratung (KOM, KUN)
Kanäle: Telefon, E-Mail, Formular, Laufkundschaft. Erwartung an das System: Lead wird mit
Bedarf (Größe, Zeitraum) erfasst, Wiedervorlage automatisch, keine verlorenen Anfragen,
Herkunft der Anfrage auswertbar.

## 2. Verfügbarkeit und Reservierung (OBJ, BUC)
Belegungsplan in Echtzeit, freie Einheiten nach Größe/Preis, Reservierung mit Ablaufdatum,
optional Online-Buchung 24/7 mit sofortiger Zahlung.

## 3. Vertragsabschluss (VER)
Vertragsdokument aus Vorlage, digitale Unterschrift, Identitätsnachweis, Kaution,
Zahlungsart und SEPA-Mandat, automatische Zutrittsberechtigung, Willkommensmail mit
Portalzugang und Vertrags-PDF.

## 4. Zutritt (ZUT)
Berechtigung folgt dem Vertragsstatus: aktiv = Zutritt, gekündigt/geräumt = Entzug,
Zahlungsverzug = optional Sperre. Zutrittsprotokoll für Sicherheitsfragen.

## 5. Wiederkehrende Abrechnung (ABR, PRI)
Monatlicher Lauf, taggenaue Abrechnung bei Ein-/Auszug, Zusatzleistungen (Versicherung,
Ware), korrekte USt., automatischer Rechnungsversand, Einzug per Lastschrift/Karte,
Zahlungsabgleich, Buchhaltungsexport.

## 6. Zahlungsverzug (MAH)
Automatische Erinnerung und Mahnstufen mit Fristen, Sperre des Zutritts nach definierter
Stufe, Eskalation bis Verwertung; jederzeit ersichtlich, welche Kundin/welcher Kunde in
welcher Stufe steht.

## 7. Vertragsänderungen (VER, PRI)
Umzug in eine andere Einheit, Größenwechsel, Preisanpassung/Indexierung mit Ankündigungsfrist,
Rabatte und Aktionen (z. B. „1 Monat gratis bei 12 Monaten Bindung"), Zahlungsartwechsel.

## 8. Kündigung und Auszug (VER, ABR)
Kündigung mit Frist, Endabrechnung inkl. anteiliger Miete, Kautionsrückzahlung,
Zutrittsentzug, Freigabe der Einheit für die Neuvermietung, Nachbetreuung/Feedback.

## 9. Steuerung und Auswertung (REP)
Belegungsgrad je Größenklasse, Umsatz je m² und Monat, Außenstände nach Alter,
Neuzugänge/Kündigungen, Herkunft der Anfragen, Prognose freier Flächen.

## 10. Administration und Datenschutz (ADM)
Benutzer und Rollen, Protokollierung, Löschkonzept und Aufbewahrungsfristen,
Auftragsverarbeitung, Datenexport.

## Automatisierungspotenzial (Grundlage der Nutzenargumentation)

| Prozess | heute (`ANNAHME`) | Ziel |
| --- | --- | --- |
| Monatliche Fakturierung | manuell je Vertrag | automatischer Lauf, Kontrolle statt Erstellung |
| Zahlungsabgleich | manueller Kontoabgleich | automatischer Abgleich über Lastschrift/Provider |
| Mahnwesen | anlassbezogen, uneinheitlich | regelbasiert, mit definierten Stufen |
| Vertragserstellung | Word-Vorlage + Ausdruck | Vorlage + digitale Signatur |
| Zutrittsberechtigung | manuell im Zutrittssystem | statusgesteuert aus dem Kernsystem |
| Belegungsübersicht | Tabelle | Echtzeit-Belegungsplan |
