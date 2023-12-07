# 2 - DIS07 Informationserschließung - Strukturierte Dokumentbeschreibung [SS 2023]

## 28-03-23

Abstracts sind immer dabei, man könnte Original auch recherchieren.  
Ziel: Egal wie, Herstellung von Einheitlichkeit  
17 PDFs --> Zeit af   
Für Aufsätze innerhalb eines Buches müssen eigene Datensätz angelegt werden. Der Fall taucht zweimal auf. Für ein Buch mit zwei Vorträgen von anderen Autoren sind drei Datensätzen anzulegen.  
***Semantische Interoperabilität***  
Bei den PDFs nicht alphabetisch vorgehen, mit einfachen anfangen.

## 04-04-23

Titelblätter sind maßgeblich zum Befüllen der Metadaten, was da steht ist Gesetz, das glauben wir! Keine weitere Recherche zur Überprüfung nötig.  
Namen invertieren und mit Pipes trennen (?) kein Semikolon  
Nicht vorhandene Metadaten werden nicht befüllt.  
Titelblatt Rückseite ist häufig irrelevant und kann verwirren, Beispiel:  
`Es ist komplett egal wer genau das Buch gedruckt hat.`  
Datenbank befragen, vorallem beim Ausgabeformat.  
Sammelwerke haben nur Herausgeber und keine Verfasser.  
Sobald was bei "Herausgeber" steht ist es klar, dass es ein Sammelwerk ist und es darf nichts bei "Verfasser" stehen!  
"Inhalt" handelt vom Inhalt des Inhaltsverzeichnis, das ist der Unterschied zu "Abstract", Abstract ist der eigentlich Inhalt des Buches / Aufsatzes / whatever  
Index oder sowas in normale Groß- und Kleinschreibung umwandeln. (?)  
*ISSN ist irrelevant!!!*  
Pipes != semicolon  
Pipes werden im Ausgabeformat mit Semicolon angezeigt (warum auch immer)  

## 11-04-23

Vergleich zur vorherigen Bilddatenbank nicht strapazieren, vieles geht nicht so intuitiv wie damamls.

## 18-04-23

Vorlesungsskript ~24 - Erich Kästner  
eigenen Datensatz zum Verfasser  
Teil der Schriftenreihe  
Auch eigener Datensatz  

S.24  
Wenn man sich die XML anschaut, steht oft gar nicht drin was wir sehen, sondern nur eine Nummer. Über die Nummer des Datensatzes können wir den Titel anzeigen.  
s.22  
datensatz des werks, bläuliche Stelle enthalten nicht wirklich erich kästner, sondern die NUMMER des Datesatzes wo Erich Kästner steht  
Dieses Verknüpfungssystem ist typisch für bibliograpihsches Daten.  
Verknüpfungssystem ist sehr aufwendig, ist aber nur bestimmten System vorbehalten und SEHR NERVIG, weil es händisch passiere muss (beispielsweise bei generischen Namen).  
Midos kann das nicht.  
`In Midos ist die Datenstruktur flach.`

`GND = Gemeinsame Normdatei`

### FRBR
S.32  
Werk (work) ist Gesamtidee wie der Textaussehen soll, nicht die physische Einheit! [Das WERK Harry Potter bestand bevor das erste Buch verkauft wurde.]  
**Expression** --> Erscheinungsform  
**Manifestation** --> Man hat was in der Hand! Physisches Buch, Film, Hörbuch, was auch immer.  
Erst auf Exemplarebene gibt es Daten zu diesem komkreten Exemplar was vor einem liegt!!  
Dies ist nur ein Model und von relation~ durchseucht. Lepsky ist nicht unbedingt Fan davon.  
Gruppe 3: Inhalt ist aspektiert.  
weitere Abstraktion auf s.34  
Niemand benutzt das.  

### Nächster Schritt

21 zugefügte Dokumente müssen inhaltlich erschlossen werden.  Koextensiv - so spezifisch wie möglich.  
Unselbstständig erschienene Dokumente (Aufsätze) sind besonders spezifisch  
So reichhaltig wie möglich erschließen.  
*Screenshots ab Seite 36 entsprechen nicht unserer Datenbank - beispielsweise Themenfeld ist anders*  
Welche Aspekte wir wie berücksichtigen sollen steht im Tutorial. Die ersten 4 bis Geografika mit bestehendem Thesauri, die anderen mit Wortlisten.  
Nur wenn eindeutig!

Form nur dann, wenn ausdrücklich mit Bezug zum Inhalt genannt. Es ist normal, dass die allermeisten keine Sparte- oder Formeintrag haben. Kann sogar sein dass das gar nicht vorkommt. Nicht in Erfindungen übergehen. Fälschliches Zuweise ist schlimmer als fehlendes Zuweisen.  
Wissenschaftsfach nur wenn ausdrücklich genannt. Nicht jedes mal *Informationswissenschaft*!  
Ort nur mit inhaltlichem Bezug. Tagungsorte, Verlagsorte etc... sind IRRELEVANT für den Inhalt!!!!!  
Bei Thesaurus mit Gegebenem zufrieden geben, **nicht erweitern**.  
Nur spezifischsten Deskriptor nehmen, nicht einen allgemeinen - trotzdem nicht zu wenige! Falls mehrere, dann müssen die zueinander hierarchisch sein, was hier besonders schwierig ist, weil umfrangreich und tief geschachtelt. Also falls zwei Begriffe Deskiptoren sind, darf keiner von beiden unter dem anderen stehen. Falls doch --> allgemeineren Streichen.  
Standardfehler:  
Geografika-Thesaurus NICHT für Verlagsort etc verwenden, es geht um den INHALT!  
Wissenschaftsfach ist nicht das fach woher das Werk kommt, INHALTTTTT!

## 25-04-23

Sammelwerk versammelt Aufsätze  
*Journal of the Association for Information Science and Technology (JASIST)*
Übersetzer in Fußnote

### Automatische Schlagwortvergabe

Titel, Titelzusatz und Extract (Inhaltskategorie würde auch Sinn machen, ist aber häufig leer.) sagen was über Inhalt aus (zumindest in Fachliteratur), diese beiden Kategorien betrachten wir als Rohmaterial für die automatische Schlagwortvergabe mit Hilfe von Wortlisten (eine andere Wortliste als die die wir kennen [Export: Wortlisten/auto-sw.txt]  
In diese Wortliste werden alle Deskiprotren und Synonyme exportiert.  
(im auto-sw.txt) In einer Zeile ist mindestens ein Deskriptore, oder ein Synonym durch Smikolon getrennt.  

Es wird geschaut ob ein Begriff aus dem Rohmaterial als Allgemeindeskiptor auftaucht (oder als Synonym) und dieser Deskiprotren werden in der Kategorie auto-sw eingefügt. In der auto-sw stehen also nur noch Deskiptoren und keine Synonyme.  
Es kann vorkommen dass einige Einräge in auto-sw komisch sind. In der auto-sw.txt kann man herausfinden warum das passiert ist. Falls es dadurch trotzdem nicht passt, liegt es an unsauberer Arbeit.
`Jede Zuteilung hat einen Grund, welcher sich in der auto-sw.txt finden lässt.`

Vorbereitung im Datenbankeditor.  
Optionen --> Schlagwörter (**NICHT** *freie Schlagwörter*)  
Danach ist er Button im Datenbankeditor nicht ausgegraut.  
Nur für selbstgemachte Elemente machen, nicht die millionen die schon drin sind. 
die drei Punkte nutzen um Fehler zu vermeiden.  
Positivliste1 ist vorbereitet. [wortlisten --> auto-sw.wtx]  
WTX = Midos-Index-Datei  
Da ist ein Mechanismus drübergelaufen, welcher aus txts eine Index Datei gemacht hat. Erhöht Geschwindigkeit.  
Man kann sie sich auch anschauen lassen.  
	"=>" bedeutet Synonym
	In dieser Sicht kann man genau sehen warum ein bestimmtes Schlagwort automatisch vergeben werde.  
	Wir sollen in der Prüfung nicht nur die Terme vergeben lassen, sondern auch darüber reflektieren, analysieren und wissen, warum ein Term zugewiesen wurde. Das liegt daran, dass Midos ein bisschen trickst um in der deutschen Sprache trotzdem Übereinstimmungen zu finden. [Erwartung: Mindestens eine begründete Vermutung.]
Positivliste 2 gibt es nicht.  
Wortlängenänderungen hilft minimale grammatikalische Unterschiede auszugleichen, beispielsweise Wortendungen oder sowas. Am besten mit verschiedenen Längen testen.  
Mindestwortlänge ignoriert Worte welche kürzer sind. Kann mn auch lassen, da es ja auch sinnvolle aber kurze Akronyme gibt.  
"Deutsche Text" --> Er versteht Komposita.  
`**Böden** Verumlautung im Wortstamm`  
Wortgruppen anschalten.  
Im Editor --> Schlagwörter gilt nur für das eine Dokument, muss für jedes einzelnd gemacht werden. Es gibt auch irgendwo eine Funktion die das für alle macht, aber lohnt sich eventuell nicht und es soll interaktiv sein. (?)  
Prozess ist ableitbar durch Stichwort in Titel, Abstract oder Titelzusatz.  
Typische Aufgabe: "Analysieren sie das Ergebnis und erklären Sie, wie es Zustande gekommen ist."
in der auto-sw.txt  
Das Durchsuchen der auto-sw.txt ist in sowas wie notepadd++ sehr viel angenehmer. (beispielsweise nur alle Zeilen mit Treffern anzeigen.)  
Zur Übung am besten die Schlagwortvergabe für alle 21 Dokumente machen und vielleicht für eine Analyse.  

### Import von Fremddaten

Das Problem ist, dass die Kategorien der zu importierenden Daten anders sind (oder anders heißen) als in der WOHIN wir das importieren. Hinzu kommt, dass Kategorien vielleicht auch anders zusammengesetzt sind. (Beispiel: Titel und Titelzusatz in einer oder mehreren Kategorien.)  
weitere Problem auf Folie 54  
Häufiger Fehler sind die unterschiedlichen Zeichensätze, lässt sich leicht mit notepadd++ lösen (kommt noch)
schlechte Zeichensätze --> Inhaltsreduktion! (Beispiel: Goethe!!!!!)  
	- Deswegen nicht einfach OE durch Ö ersetzen oder andersherum.  
Die Daten in der Prüfung sind natürlich besonders anfällig für diese Probleme.  
RIS ist ein neutrale Standardformat für die Übergabe von Daten, sehr weit verbreitet.  
Wir bekommen in der Prüfung Daten im BibTex Format und wir wollen zum internen Midos Speicherformat kommen. [S. 57]  Dit ist deutlich mehr als ein Knopfdruck.  
mit hilfe von such und ersetzen und regular expressions; es soll nicht zu Fuß passieren, dafür ist es zu lang.  
WIE GENAU wir das machen ist ihm komplett egal. Frage nach Automatisieung durch Python: Man könnte es algorithmisieren, aber das dauert häufig doch länger. Vielleicht zur Überprüfung falls Zeit bleibt?  
Es sind ungefähr 400 Datensätze (GOTT SEI DANK IN EINER TXT)  
BibTech Datei ist eine Fälschung, Tools die bei Entschlüsselung helfen HELFEN NICHT HIER!!   
eigentlich wird schwieriges mit regular expression nicht nötig sein.  


### 02-05

"Analyse der Ergebnisse" im NEUEN Tutorial  
Musteraufgabenstellung im Moodle  
eventuell Codierung verändern  
Midos möchte Ansii haben?  
Sure maken dass Umlaute funktionieren und der Bumms Midos-Tauglich ist, lässt sich später nicht mehr reparieren.  
Wenn man Abstracts aus dem Web klaut, auch drauf achten, dass sie nicht kaputtgehen.  
Grundlegende Daten kriegt man mit Austauchformaten übertragen, Schnick-Schnack nicht. Nur weil Excel XML als Austauschformat akzeptiert, heißt es nicht, dass es damit komplett zufrieden ist.  
Trotzdem sidn Austauschformate relative geil.  
Midos hat keine Inputformat für BibTex. Es kann CSV, hilft uns hier aber nicht. Wir müssen umwandeln / händisch filtern.  
notepad symbole anzeigen, zeilenenden anzeigen!  
In Notepad++ auf Regular Expressions umstellen sonst rafft der das nicht.  
Notepadd++ hat sich bezogen auf die Regular Expression etwas verändert, deswegen ist die Darstellung im Buch nicht unbedingt aktuell!  
Bei Erschließung von Sammelwerk allgemein zurückhalten, nicht zwingend auf Suche gehen.  


### 16-05

Es darf alles fehlen, aber einen Titel braucht man immer.  
Wenn Suchprozess mit mehrere Verfassern, dann mit größter Menge arbeiten (die wissen wir nicht)  


### 23-05-2023

notepad++ erweiterete Suche --> ~**findet /r und /n**, falls irgendwas nicht funktioniert, dann den Haken wegmachen!!!!!!!!!  

#### Leitfaden zum Anfertigen wissenschaftlicher Arbeiten  
(pdf auf der Seite der Fakultät)	
Zotoro ist Lepsky's favourite als Zitier Programm Gedöns, es hat die beste Web Integration, Datenbank selber ist sehr einfach. 
Gutes Tool: Overleaf  
Literaturverwaltungen sind sinnvoll und machen das Leben leichter, GEHT aber auch ohne.  
Es gibt über Textverarbeitung in WORD hinaus Tools zur Textverarbeitung.  

### 30-05

Ausgabeformat wie die Zitierdinger von Harvard usw. wir müssen verschiedene Fälle unterscheiden, nämlich zwischen Buch, Aufsatz, etc...  
Das ist möglich mit "Kommandos" rechts oben.  
Bei dieser Fallunterscheidung ist die Abkürzung (b, in usw.) nicht gut, weil einiger der Dokumente, welche schon in der Datenbank sind, eventuell zwei haben. Man muss es an anderen Kriterien herausfinden.  
Beispiel: Quellen haben nur Aufsätze.  

if KONDITION go to buch:  
inhalt  
exit  
!buch  
anderer Inhalt  

---
Im Buch gibt es ein unvollständiges Ausgabeformat, was man vielleicht copy-pasten kann.  
Dokument ohne Verfasser muss ja Herausgeber haben.  
Statt Exit ein GOTO X1 und am Ende (:X1) irgendwas ausgeben, was sowieso überall hinmuss?  
nur unterscheiden zwischen Buch, aufsatz in Buch und Aufsatz in Zeitschrift ( ez af? )  

# Bibliografie

Funktionen --> Bibliografie erstellen 

Folien als Vorlage, aber nicht nur abschauen, sondern für den eigenen Fall anpassen.  
Verschachtelte Sortierung für den Fall, dass Felder gleich oder leer sind.  
PDF manuell nach Sortierungsfehlern durchsuchen.  
Sinntragende Überschrift und Dateinahme, mit Bezug zum Namen.  
Suchanfrage noooo (*, alle)  
Ausgabeformat: Keine kategorisierte Vollanzeige! Natürlich das Zitierformat auswählen!  
Mit Register und Mit Sortierung!  
Suchwortmark aus.   
Registerfelder stehen fest.  
Wortgruppen!  
Bezeichnungen sollen auch Sinntragend sein.  
als RTF-Datei  
Kleine Formatierungsfehler im Register braucht man nicht korrigieren, vielleicht aber einspaltiges Register?  
Eigenes Register für automatische Schlagworte (wird immer vergessen)  
bevor man was verbessert und pdf überschreibt, muss man die zu überschreibene PDF schließen.  
PDF ist mit kleinen Zusätzen die Basis für die Abgabe.  
Insgesamt 3 Register; Deskriptoren, Personen und Schlagwörter. Wird aber in der Prüfung stehen.   

## Modulprüfung

(modulprüfungspdf von moodle)
Lepsky verschickt eine Mail zur Prüfung oder Kursraum für Wiederholer, nicht wundern  
aspektdifferenziertes Erschließungskonzepts.  
Koextensive Erschließung.   
alles ist in den ZIPS gegeben, also Thesauri, auto-sw, fremdaten und so  

fremdaten: 
1. stammen aus Datenbankliteratur zur Informationserschließung  
2. Format und Struktur erklärt  

10 pdfs 
Matrikelnummer ist ohne Prüfungsid oder sowas, achtstellig!  
Falscher ZIP bearbeiten ist komplett schlimm und man kann sich sofort das Leben nehmen.  
Es könnte sinnvoll sein die literatur.dbm als Basis nutzen, natürlich leer machen. Man könnte auch eine sich aber auch eine komplett neue Midos Datenbankstruktur ausdenken.  
Lepsky sieht ja nur das Ergebnis und nicht die Datenbank oder den ganzen Weg dorthin!!  
Es gibt nur "einfache" Bücher und Aufsätze [Zeitschriftenaufsatz und Aufsatz im Buch]  
Nur selbsterfasten Einträge intellektuell erschließen und automatische Schlagwortvergabe durchführen.  
Jedem mindestens EINEN Sachdeskriptor zuordnen.  
GEO und sowas bleibt natürlich häufig leer.  
zu analysierende Schlagwörter wählen, zu denen man natürlich viel sagen kann! Hier kann man sich gute raussuchen.  
**Gründe für deren Erzeugung**  
Schlagwörter ausgeben und abstracts auch und so nicht vergessen!!!!!!!!!!!1  
keine kategorisierte Vollanzeige  
durchgehende Sortierung ist genau das, ein Fehler ruiniert das und für alle Titel einheitlich 
Bibiliogrpahie braucht 3 register
- Gemischt (alle Deskriptoren auf einmal (geo, objekt, sach))
- automatische schlagworte
- personen  

übereinstimmendes Ausgabeformat mit gleichen Fehlern ist **TÄUSCHUNGSVERSUCH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**  
aus rtf PDF machen und EINE PDF abgeben.  
Bewertungsbogen wird mit Aufgabenstellung veröffentlicht.  
Schreibfehler werden nicht toleriert!!

# Codierungstabelle 

|normal|utf-8|Ansi|
|:---:|:---:|:---:|
|Ü|||
|ü|||
|Ö|||
|ö|||
|Ä|||
|ä|||
||||
||||
||||