Erstelle ein Programm, das die Daten aus der CSV-Datei einliest und über einen REST-Endpoint zur Verfügung
stellt. Der Endpunkt soll mit der Abkürzung einer Betriebsstelle angefragt werden und die Daten der
Betriebsstelle als JSON-Objekt zurück liefern.

Beispiel-Request:
.../betriebsstelle/aamp

Beispiel-Response:

HTTP-STATUS: 200
{
  Name: Hamburg Anckelmannsplatz
  Kurzname: Anckelmannsplatz
  Typ: Üst
}