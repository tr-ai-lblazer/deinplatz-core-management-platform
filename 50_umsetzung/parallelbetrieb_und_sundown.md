# Parallelbetrieb, Abgleich und Sundown von Zoho

Beschluss aus dem Stakeholder-Termin vom 07.09.2026 (B2/B3): Das neue System geht am
**1. November 2026** live, Zoho läuft zunächst weiter; beide Systeme werden bis zum Jahreswechsel,
längstens bis in den Januar, nebeneinander geführt, um Abweichungen zu vergleichen.

Verantwortlich für die Ausarbeitung des Cutover-Szenarios einschließlich Archivierung: **Martina**.
Dieses Dokument ist die Arbeitsgrundlage dafür.

## 1. Die Grundsatzentscheidung: Schattenbetrieb statt Doppelpflege

| Variante | Was passiert | Aufwand | Risiko |
| --- | --- | --- | --- |
| **Schattenbetrieb (Empfehlung)** | Ab 1.11. ist das neue System führend. Zoho wird nicht mehr bespielt, bleibt lesend verfügbar und dient dem Abgleich und als Rückfallebene | gering | gering |
| Echter Parallelbetrieb | Beide Systeme werden gepflegt, beide fakturieren | doppelt | doppelte oder fehlende Rechnungen, widersprüchliche Stände |

**Begründung:** Der Zweck des Nebeneinanders ist Absicherung, nicht Redundanz. Sobald zwei Systeme
Rechnungen erzeugen, entstehen genau die Fehler, die der Parallelbetrieb verhindern soll.
Ein Vergleich ist auch möglich, wenn nur eines produktiv ist – der Abgleich erfolgt gegen den
eingefrorenen Stand von Zoho und gegen den Kontoauszug.

> Diese Präzisierung ist noch zu bestätigen (offene Frage O-14 im Entscheidungslog).

## 2. Rollen der beiden Systeme ab 1. November

| Vorgang | Neues System | Zoho |
| --- | --- | --- |
| Neuvertrag, Kündigung, Vertragsänderung | führend | keine Erfassung mehr |
| Monatliche Fakturierung | führend | keine Läufe mehr |
| Zahlungseinzug und Zuordnung | führend | – |
| Mahnwesen | führend | – |
| Auskunft über Altvorgänge und Belege bis 31.10. | lesend über Archiv | lesend |
| Abgleich und Rückfallebene | – | Vergleichsstand |

**Datenannahmestopp in Zoho: 30.10.2026.** Ab diesem Zeitpunkt keine neuen Buchungen, Verträge
oder Rechnungen mehr im Altsystem. Vorgänge des Cutover-Wochenendes werden auf einer Deltaliste
geführt und im neuen System nacherfasst.

## 3. Abgleichpunkte

Drei feste Termine, je mit Protokoll im Repository (ohne Kundendaten – nur Summen und Abweichungszahlen):

| Termin | Prüfung | Kriterium |
| --- | --- | --- |
| **05.11.2026** (nach dem ersten Lauf) | Anzahl und Summe der Novemberrechnungen gegen die Sollmieten aus Zoho | Abweichung 0,00 € oder erklärt |
| **30.11.2026** | Zahlungseingänge, Rückläufer, offene Posten gegen Kontoauszug | jede Abweichung dokumentiert und geklärt |
| **31.12.2026** | Jahresabschlussrelevante Summen, Kautionen, Guthaben, Buchhaltungsexport des Quartals | von der Steuerberatung bestätigt |

Erst wenn der Abgleich zum 31.12. sauber ist, wird der Sundown ausgelöst.

## 4. Sundown von Zoho

| Schritt | Inhalt | Termin |
| --- | --- | --- |
| S1 | Vollständige Datensicherung ziehen (Kunden, Abos, Rechnungen, Zahlungen, Gutschriften, Kontoauszüge) und Lesbarkeit prüfen | bis 15.01.2027 |
| S2 | Rechnungs- und Belegarchiv als PDF-Bestand aufbauen, nach Jahr und Kundennummer strukturiert | bis 15.01.2027 |
| S3 | Archiv an zwei getrennten Orten ablegen, Zugriff dokumentieren | bis 20.01.2027 |
| S4 | Stichprobe: 20 Belege aus verschiedenen Jahren aus dem Archiv wiederfinden und öffnen | bis 20.01.2027 |
| S5 | Freigabe durch Steuerberatung, dass das Archiv den Aufbewahrungspflichten genügt | bis 25.01.2027 |
| S6 | Zoho-Abonnement kündigen, Kündigungsbestätigung ablegen | bis 31.01.2027 |
| S7 | Löschung der Daten beim Anbieter beauftragen und bestätigen lassen | nach Ablauf der Aufbewahrungsfrist |

**Kündigungsfrist des Zoho-Abonnements vorher prüfen** – sie bestimmt den spätesten Zeitpunkt
für S6 und ist möglicherweise früher als der geplante Sundown.

## 5. Langzeitarchivierung – Anforderungen

Bücher, Aufzeichnungen und Belege sind grundsätzlich **sieben Jahre** aufzubewahren (§ 132 BAO)
und müssen in dieser Zeit **maschinell auswertbar** bleiben. Für ein abgeschaltetes SaaS-System
heißt das:

| Anforderung | Umsetzung |
| --- | --- |
| Vollständigkeit | Alle Ausgangsrechnungen, Gutschriften, Zahlungen und Kontoauszüge des Zeitraums |
| Lesbarkeit ohne das Altsystem | PDF für Belege, CSV für Datentabellen – kein proprietäres Format |
| Auffindbarkeit | Ordnerstruktur nach Jahr, darin nach Kundennummer; zusätzlich eine Indexdatei als CSV |
| Unveränderbarkeit | Ablage schreibgeschützt, Zugriff protokolliert |
| Datenschutz | Zugriff nur für berechtigte Personen; Löschung nach Fristablauf geplant und dokumentiert |
| Nachweis | Kurzes Archivprotokoll: was wurde wann gesichert, von wem geprüft |

Das Archiv gehört **nicht** in dieses Repository, sondern in die geschützte Ablage.
Hier wird nur das Archivprotokoll ohne personenbezogene Daten geführt.

## 6. Rückfallebene während des Parallelbetriebs

Falls im November gravierende Fehler auftreten (falsche Beträge, fehlgeschlagene Einzüge in
größerem Umfang):

1. Fakturierung des betroffenen Monats einmalig über den bisherigen Weg abwickeln.
2. Ursache klären, Korrekturlauf im neuen System.
3. Entscheidung der Geschäftsführung, ob der Sundown-Termin verschoben wird.

Der Rückfall ist möglich, solange Zoho nicht abgeschaltet ist – das ist der eigentliche Wert des
Nebeneinanders und der Grund, den Sundown nicht vor dem sauberen Abgleich zum 31.12. anzusetzen.

## 7. Zusammenspiel mit der Preisanpassung zum 1. Januar

Die für den 1. Januar 2027 vorgesehene Preiserhöhung fällt in den Parallelbetrieb. Reihenfolge:

1. Preise im neuen System zum Stichtag 01.01.2027 hinterlegen und in der Vorschau prüfen
   (Anforderung PRI-03).
2. Ankündigung an die Kundinnen und Kunden mit der vereinbarten Frist – als eigenes Schreiben,
   getrennt von der Umstellungsinformation (siehe offene Frage O-15).
3. Erster Lauf im Januar im Vier-Augen-Prinzip prüfen, bevor er versendet wird.
4. Sundown von Zoho **erst nach** dem ersten korrekten Januarlauf abschließen.
