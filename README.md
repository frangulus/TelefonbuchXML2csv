# TelefonbuchXML2csv

Konvertiert die von einer Fritz!box per Telefonbuchexport erstellte XML-Datei in eine CSV-Datei   

# Beschreibung
Die Fritz!box kann angelegte Telefonbücher exportieren. Beim Export eines Telefonbuchs wird eine Datei im XML-Format erstellt. 

Zum Import der Daten in ein andere Software oder Anwendung ist diese Format jedoch ungeeignet. Mit xml2cslW kann man aus dem Fritz!box eigenen Format eine CSV-Datei erstellen.
Das CSV kann dann direct in MircoSIP importiert werden oder mit LibreOffice, Excel, etc. leicht weiterbearbeitet und angepasst werden. Das CSV Format ist als Dateiformat für den Im- und Export von Daten weit verbreitet.

# Anforderungen
+ Python3  
+ PyQt5 (GUI Version) 

# Versionen / Benutzung

## Komandozeile 
xml2csv.py ist die Version für die Nutzung im Terminal. 

    `python3 xml2csv.py XMLinputfile`

Als XMLinputfile ist die von der Fritz!Box erstellte XML-Datei anzugeben. Es wird eine CSV Datei mit dem Namen microSipImport.csv 
im aktuellen Verzeigchnis erzeugt. Diese kann dann zum Import in MicroSip verwendet werden oder weiterbearbeitet werden. 

## GUI-Versiom    
xml2csvW.py ist die Version mit graphischer Nutzeroberfläche. 
Der Auruf erfolgt per:

    `python3 xml2csvW`

Der Rest ist weitgehend selbsterklärend. Es kann Eingabe- und Ausgabedatei ausgewählt werden, dann die Konvertierung mit dem Start-Button anstossen. Nach erfolgter Erstellung der CSV Datei erscheint eine Statusmeldung.        