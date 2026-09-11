# Anschreiben an die Buchhaltung: Spezifikation des Datenaustauschs

Entwurf vom 11.09.2026 · Aufgabe A4 aus dem Stakeholder-Termin, Issue
[#5](https://github.com/tr-ai-lblazer/deinplatz-core-management-platform/issues/5)
· Empfänger: Sepp, in Kopie Pickerle bzw. Frau Tarmann

**Zweck:** Die Antworten sind die Vorgabe für die Konfiguration des Buchhaltungsexports
(Anforderungen BUH-01, BUH-02, BUH-05) und die Grundlage für den Testimport des Musterexports
in RZL vor der Kinnovis-Demo.

---

**Betreff:** Neues Verwaltungssystem ab 1. November – wie soll die Übergabe an die Buchhaltung aussehen?

Hallo Sepp,

wir lösen bei deinPlatz unser bisheriges System (Zoho) ab und stellen zum 1. November auf eine
Self-Storage-Software um. Das neue System soll die monatliche Übergabe an die Buchhaltung
möglichst automatisch erledigen – idealerweise als Datei, die du direkt in RZL einliest.

Damit wir das richtig einrichten und nicht raten, bräuchte ich von dir kurz folgende Angaben.
Stichworte genügen:

1. **Format:** Welches Importformat sollen wir liefern – das RZL-eigene CSV oder das
   DATEV-Format? Gibt es dazu eine Feldbeschreibung?
2. **Musterdatei:** Kannst du mir eine Datei schicken, die schon einmal sauber in RZL eingelesen
   wurde? Das ist für uns die verlässlichste Vorlage.
3. **Konten:** Welche Erlöskonten sollen wir verwenden – für die Lagermiete, für Zusatzleistungen
   (Versicherung, Schlösser, Kartons) und für Mahnspesen?
4. **Umsatzsteuer:** Welche Steuersätze und Steuerschlüssel gehören zu diesen Positionen?
5. **Kautionen:** Wir gehen davon aus, dass sie als durchlaufender Posten geführt werden – auf
   welchem Konto?
6. **Zahlungsdienstleister:** Falls wir künftig Kartenzahlung anbieten, kommt das Geld nicht
   einzeln, sondern etwa alle sieben Tage als Sammelüberweisung abzüglich Gebühren auf das Konto.
   Wie sollen wir Auszahlung und Gebühren buchen, damit es für dich stimmt?
7. **Ablauf:** Monatlich reicht vermutlich – auf welchem Weg bekommst du die Datei am liebsten,
   und brauchst du die Rechnungs-PDFs zusätzlich oder genügt der Buchungsstapel?

Und eine Bitte mit etwas Zeitdruck: Wir bekommen vom Softwareanbieter demnächst einen
Musterexport. **Könntest du den testweise in RZL einlesen**, bevor wir uns endgültig entscheiden?
Wenn das nicht funktioniert, ist das für uns ein Ausschlusskriterium – und das wollen wir vorher
wissen, nicht nachher.

Wenn es dir schneller geht, telefonieren wir kurz; ich schreibe die Antworten dann mit.

Danke dir und beste Grüße
Peter

---

## Hinweise für uns (nicht Teil der E-Mail)

- **Warum die Musterdatei so wichtig ist:** RZL kann Buchungsstapel sowohl über die integrierte
  DATEV-Schnittstelle im CSV-Format als auch über ein RZL-eigenes CSV einlesen. Die Formate
  unterscheiden sich unter anderem darin, dass RZL Soll- und Habenkonto in getrennten Spalten
  führt und den Betrag positiv trägt. Eine funktionierende Beispieldatei erspart uns die
  Formatdiskussion vollständig.
- **Wenn Sepp das DATEV-Format nennt:** in der Demo prüfen, ob der DATEV-Report des Anbieters auf
  den österreichischen Kontenrahmen umkonfiguriert werden kann (Frage E3 im Fragenkatalog).
- **Nach der Antwort:** Vorgaben in `20_anforderungen/rechtliche_rahmenbedingungen_at.md`
  (Prüfauftrag P2) eintragen und Issue #5 schließen.
