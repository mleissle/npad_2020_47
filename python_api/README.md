# Python + APIs
## Netconf
- Zur Vorbereitung installieren Sie ggf. `pip`:
```
sudo apt install python3-pip
```
Danach nutzen Sie pip um das Python-Paket für die Netconf-API zu installieren:
```
pip3 install ncclient
```

- Testen Sie die bereitgestellten `n9kv_netconf_get_int_*.py`-Skripte, z. B.:
```
python3 n9kv_netconf_get_int_*.py
```
Achten Sie dabei auf die verwendeten Filter in den Skripten, die den Output einschränken.

- Anschließend passen sie den Filter in `n9kv_netconf_edit_int_1.py` an, um jetzt eine eigene Interface-Beschreibung, auf Basis das Openconfig-Yang-Modells, per Netconf zu konfigurieren. Vergessen Sie nicht die IP-Addresse des Switches ggf. zu ändern.

Mit `n9kv_netconf_edit_int_1.py` können Sie das Resultat beobachten.

## Restconf
- Legen sie mit einem Texteditor, z. B. im Heimatverzeichnis, eine Datei mit dem Namen `restconf.py` an.
- Generieren Sie mit, Hilfe von Postman und der bereitgestellten Collection, Python-Code für einen RESTCONF-Request.
- Führen Sie das Skript aus, indem ie auf der Kommandozeile, in dem Verzeichnis in dem sich die Datei befindet, den Befehl `python3 restconf.py` verwenden.