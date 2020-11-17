# Netconf
Für die Interaktion via Netconf-API initialisiert der Client die SSH-Session zum Server und signalisiert das auf Basis von Netconf kommuniziert werden soll. Auf der CLI im Labor ist ein entsprechender Befehl:
```
ssh <USER>@<DEVICE_IP> -p 830 -s netconf
```
Die genauen Parameter könner allerdings je nach Server-Implementierung und Konfiguration auch andere sein.

## Übungen
### Teil 1
Nutzen sie die bereitgestellten XML-Snippets um einen ersten Eindruck für die Interaktion mittels Netconf zu erhalten.
Die Session öffnen Sie durch den jeweiligen Befehl:
```
ssh -l admin 192.168.181.21 -s netconf
ssh -l admin 192.168.181.22 -s netconf
ssh -l admin 192.168.181.23 -s netconf
ssh -l admin 192.168.181.24 -s netconf
```
### Teil 2
- Öffnen sie zusätzlich zu einer Netconf-Session, z. B. in einem zweiten Terminal, eine klassische CLI Verbindung.
- Wechseln Sie dort mit `xmlin` in den XML-Config-Modus und generieren sie mittels der Befehle `configure terminal`, `interface ethernet 1/XX`, `description MeinName`, `exit`, `exit` einen XML-String für Netconf. Ersetzen Sie dabei XX durch eine beliebige Interface-Nummer.
- Nutzen Sie diesen um, über die Netconf-Session die Interface-Beschreibung zu konfigurieren.