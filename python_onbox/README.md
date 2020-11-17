# Der OnBox-Python-Interpreter
Unter NX-OS steht z. B. für die OnBox-Automatisierung ein lokaler Python-Interpreter zur Verfügung. Nach dem ssh-Login lässt sich dieser dort starten durch die Eingabe des Befehls:
```
python
```
Beachten Sie das sich der Prompt jetzt geändert hat zu:
```
>>>
```
(**Hinweis:** Bei Bedarf beenden Sie den Interpreter durch Eingabe von `exit()` oder die Tastenkombination `STRG+D`.)

Aus diesem Interpreter haben Sie Zugriff auf die lokalen Python-API des NX-OS:
```
import cisco
```
Über ein VLAN-Objekt lässt sich dort z. B. mit der Vlan-Konfiguration des NX-OS mit Pythons nativen Funktionen und Datenstrukturen interagieren.

## Aufgaben
- Testen Sie im On-Box-Python-Interpreter den folgenden Ablauf:
``` 
import cisco
vl = cisco.vlan.Vlan()
vlShow = vl.show_vlan()
existing_vlans =  vlShow.get_vlans()
type(existing_vlans)
```
- Versuchen sie das gesehene nachzuvollziehen. Was sind Variablen und wo verwenden Sie Funktionsaufrufe? In welchem Datentyp liefert der Switch Informationen zu existierenden Vlans?
- Mit den Funktionsaufrufen `vl.create_vlan(XXX)` und `vl.delete_vlan(XXX)` lassen sich Vlans anlegen wenn sie `XXX` durch die entsprechende Vlan-Nummer ersetzen. Legen sie mit deren Hilfe ein neues Vlan an. Verifizieren sie mit `vl.show_vlan().get_vlans()` das dieses erstellt wurde.
- Legen Sie auf gleichem Weg ein zweites Vlan an und löschen sie das erste. Verifizieren sie den erreichten Endzustand.
