# Hotel-Reservierungssystem

### Das ist ein Hotelreservierungssystem Projekt der Gruppe B2

## 👥 Team

Josip Jukic (GitHub: JJukic)

    • 	Grundstruktur und Grundgerüst mit Klassen und Modulen in Modul/Data_Access/Busniess_Logic Layer
    • 	Userstories 1-4 + Userstory 4 mit DB Schemaänderung 
    • 	Funktionen der jeweiligen Userstories 
    • 	Readme. & Dokumentation, Video zur Grundstruktur

Libin Manavalan (GitHub: Libin2001)

    • 	Userstories 8-10 + Userstory 1 mit DB Schemaänderung
    • 	Funktionen der jeweiligen Userstories 
    • 	Video zur Userstory

Janarthanan Ragunathan(GitHub: Janaragu)

    • 	Userstories 5-7 + Userstory mit Visualisierung
    • 	Funktionen der jeweiligen Userstories 
    • 	Video zur Userstory

Selma Kaviani (GitHub: selmakaviani)

    • 	Dokumentation über Basics von Python

## Projektbeschrieb
Das Hotelreservierungssystem umfasst einige Userstories aus der Aufgabenstellung die vorgegeben ist.
Das Modellierungskonzept wurde mittels Visual Paradigm erstellt. Die Datenbank wurd bereitgestellt und mit SQLite in Verbindung gebracht.
Die Projektstruktur wurde vorgegeben und wird auch n-Tier Struktur genannt. 

## Anleitung

    1. Öffnen des Notebooks 
![Bild1](images/anleitung_1.png)

    2. Auf den Button "Run" klicken um die Datenbank zu verbinden
![Bild2](images/anleitung_2.png)

    3. Beliebige Userstory anwählen und mit "Run" laufen lassen, danach Eingaben mit "OK" bestätigen
![Bild3](images/anleitung_3.png)


## N-Tier Struktur

Im Vordergrund steht der UI-Layer, der sich um die Präsentation kümmert und alle Eingaben und Ausgaben der Benutzer steuert. Darauf folgt der Business-Logic-Layer, in dem alle Anwendungsregeln, Validierungen und Workflows umgesetzt werden, zum Beispiel die Logik zur Reservierungsprüfung oder Preisberechnung. Der Data-Access-Layer abstrahiert die konkrete Datenbankanbindung, führt CRUD-Operationen aus und stellt die rohen Daten bereit. Unterhalb dieser drei Schichten liegt der Model-Layer, der die Objekte wie Hotel, Zimmer und Reservierung mit ihren Eigenschaften und Beziehungen definiert.

Durch diese klar getrennte Aufteilung können Änderungen an einer Schicht, etwa der Austausch der Datenbanktechnologie vorgenommen werden, ohne dass andere Schichten angepasst werden müssen. Außerdem erleichtert diese Architektur das isolierte Testen der Geschäftsregeln und verbessert die Wartbarkeit insgesamt. Typischerweise fließt eine Benutzeranfrage vom UI-Layer in den Business-Logic-Layer, wird dort verarbeitet und bei Bedarf an den Data-Access-Layer weitergegeben, der die Datenbank kontaktiert. Die Antwort wandert dann in umgekehrter Reihenfolge zurück an die Benutzeroberfläche.
![Projektstruktur](images/Project_Structure.png)

#### 1.  Datenbank-Layer
	•	Enthält die tatsächlichen SQLite-Dateien (DB-Storage).
	•	Schnittstelle: direktes Dateisystem, kein Python-Code hier.

#### 2. Model-Layer
	•	Zweck: Daten zwischen Schichten als Objekte transportieren.
	•	Klassen: Je Tabelle eine Datei <Entity>.py (z. B. Hotel.py, Booking.py).
	•	Inhalte: Properties und Getter/Setter für jedes Attribut der Tabelle.
	•	Wichtig: Neue Model-Klassen müssen in __init__.py importiert werden.

#### 3. Data-Access-Layer
	•	Zweck: CRUD-Operationen (INSERT, SELECT, UPDATE, DELETE) auf der DB ausführen.
	•	Klassen: Je Entity eine Datei <entity_name>_dal.py (z. B. hotel_dal.py).
	•	Inhalte: Sämtliche SQL-Statements und Datenbank-Verbindungen.
	•	Wichtig: Neue DAL-Klassen ebenfalls in __init__.py registrieren.

#### 4. Business-Logic-Layer
	•	Zweck: Anwendungs- bzw. Geschäftsregeln umsetzen (z. B. Preis-Berechnung, Validierungen).
	•	Klassen: Je Entity ein Manager <entity_name>_manager.py (z. B. booking_manager.py).
	•	Inhalte: Kombination und Vorbereitung von DAL-Aufrufen, Vor- und Nachbearbeitung von Daten für UI/DB.
	•	Wichtig: Auch hier neue Manager in __init__.py eintragen.

#### 5. UI-Layer
	•	Zweck: Nutzerinteraktion (Inputs abfragen, validieren, Ausgabe formatieren).
	•	Komponenten:
	•	Helper-Klasse für Input-Validierung.
	•	Deepnote-Notebooks für die finale Darstellung.
	
#### 6. •	Ablauf:
	1.	Eingaben entgegennehmen
	2.	Validieren (bei Fehlern Rückmeldung geben)
	3.	Über Business-Logic-Manager auf DAL zugreifen
	4.	Ergebnisse im Notebook anzeigen

