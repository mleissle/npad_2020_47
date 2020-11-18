# REST
## NXAPI-CLI
Das Aufrufen der Device-IP im Webbrowserliefert über die NXAPI-Sandbox einen einfachen Zugang zur NXAPI-CLI.

## NXAPI-Rest
Cisco's NX-OS Plattform verfügt in aktuellen Releases über eine REST-API für Nexus 3000/9000. Die Dokumentation findet sich z. B. für den 9.2 Release unter https://developer.cisco.com/docs/cisco-nexus-3000-and-9000-series-nx-api-rest-sdk-user-guide-and-api-reference-release-9-2x/ .

## Postman
Postman ist ein weitverbreitetes Werkzeug zum Test von REST-APIs. Hervorgegangen aus einer Erweiterung für Chrome, handelt es sich nun um eine eigenständige App, zu finden unter https://www.postman.com/ .

Unter anderem erlaubt postman das Zusammenstellen/Teilen/Importieren/etc. von Request-Collections.

Im Labor lässt sich Postman am einfachsten über das Terminal mit dem folgenden Befehl installieren:
```
sudo snap install postman
```

## Übung
Nutzen Sie Postman und die API-Dokumentation um einen BGP-Nachbarn zu konfigurieren. Dazu muss eventuell erst über die API ein BGP-Router konfiguriert werden. Beispiele für sinnvolle Requests finden die in der bereitgestellten Postman-Collection.

# RESTCONF + Python
## Übung
- Legen sie mit einem Texteditor, z. B. im Heimatverzeichnis, eine Datei mit dem Namen `restconf.py` an.
- Generieren Sie mit, Hilfe von Postman und der bereitgestellten Collection, Python-Code für einen RESTCONF-Request.
- Führen Sie das Skript aus, indem ie auf der Kommandozeile, in dem Verzeichnis in dem sich die Datei befindet, den Befehl `python3 restconf.py` verwenden.