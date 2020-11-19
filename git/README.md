![git](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/512px-Git-logo.svg.png)
# Git
Ein Versionsverwaltungssystem ist der zentrale Ausgangspunkt einer CI/CD-Pipeline. Es ist jedoch auch jenseits solcher komplexerer Prozesse ein sehr hilfreiches Werkzeug, sobald mehrere Personen ihre Arbeit an primär textbasierten Dateien verwalten wollen. Bereits für eine einzelne Person kann es wertvoll sein, um über längere Zeit die Arbeit an einem Projekt zu organisieren.

Das aktuell vermutlich verbreiteteste VCS ist git. Grundlage von git ist der Command-Line-Client der mit `git` aufgerufen wird. Auf vielen Systemen ist dieser bereits vorhanden. Aktuelle Versionen für gängige Betriebssystem sind jedoch jederzeit bei Bedarf unter https://git-scm.com/ verfügbar. Unter Ubuntu ist es einfach installierbar mit:
```
sudo apt install git
```

Um die Einstiegshürde die damit verbunden ist leichter überwinden zu können, sind im folgenden einige der wesentlichsten Konzepte erläutert.

---
## Basis-Setup
Um die Änderungen aussagekräftig zu dokumentieren erwartet git von seinen Nutzern einige grundlegende Informationen um z. B. festzuhalten wer zu welchem Zeitpunkt welche Änderung vorgenommen hat.
```
git config --global user.name "Nutzername"
git config --global user.email "nutzer@beispiel.de"
```
Die beiden obigen Befehle nutzen `git config` um global Nutzernamen und E-Mail festzulegen. Für das Basis-Setup sind diese beiden Informationen ausreichend. Das Kommando erlaubt allerdings auch noch viele weitere, für git relevante Variablen zu beeinflussen.

---
## Der Anfang
Auch wenn für git zahlreiche GUIs und Integrationsmöglichkeiten in Editoren und Plattformen existieren, werden die unterliegenden Konzepte am deutlichsten wenn man auf der Kommandozeile beginnt.
```
git init projectName
cd projectName
```
Der erste Befehl für dazu das in einem Verzeichnis `projectName` ein neues git-Projekt angelegt wird. Der zweite Befehl wechselt in das angelegt Verzeichnis. Innehalb dieses Projekts überwacht git nun alle Änderungen.

---
## Arbeit mit Dateien
Sobald sich diesem Verzeichnis jetzt Datein auftauchen wird git dieses registrieren. Ein gängiges Beispiel wäre eine `README.md` für die spätere Verwendung auf Plattformen wie GitLab oder GitHub. Mit `touch README.md` lässt sich diese schnell anlegen um päter in einem geeigneten Texteditor mit sinvollem Inhalt befüllt zu werden. Damit git neue Dateien allerdings nicht nur erkennt, sondern sich auch für diese zuständig sieht, ist ein weiterer Schritt notwendig.
```
git add .
```
Dieser Befehl fügt alle Dateien im aktuellen Verzeichnis (und ggf. dessen Unterverzeichnissen) zur Staging-Area hinzu. Es lassen sich alternativ z. B.  auch einzelne Dateien oder Verzeichnisse aufnehmen.

Die Änderungen sind allerdings immer noch nicht Bestandteil des Repositories. Dazu ist ein weiter Schritt notwendig, der eigentliche Commit.
```
git commit -m "Commit-Nachricht"
```
Das zugehörige Kommando `git commit` erwartet jetzt keine Dateinamen oder Ähnliches. Es nimmt alle Änderungen, die in der Staging-Area angesammelt sind, in den Commit in das Repository auf. Stattdessen wird hier der Parameter `-m` verwendet um die Commit-Nachricht (Commit-Message) festzulegen. Diese sollte beispielsweise eine sinnvolle Kurzbeschreibung des durchgeführen Commit beinhalten.

Es existieren noch viele weitere Parameter. Eine hilfreiche Abkürzung ist später z. B. `git commit -a -m 'Nachricht'` um in einem Schritt alle aktuellen Änderungen in die Staging-Area aufzunehmen und direkt zu commiten. 

---
## Kollaboration
Git bietet viele weitere Features, die insbesondere die Kollaboration von mehreren beteiligten am gleichen Projekt erleichtern sollen. Dazu gehört unterandererem, dass diese auch parallel an ihren Teilen arbeiten können ohne von den Änderungen der Anderen unterbrochen oder gestört zu werden.
### Branch
Git erlaubt es dazu ein Projekt zu verzweigen und auch (optional) wieder zusammenwachsen zu lassen. In der Analogie eines Baumes spricht man dort von "Branches" in die sich der "Tree" verzweigen kann.
```
git branch -c mein-branch
```
### Checkout
```
git checkout mein-branch
```
### Merge
```
git merge mein-branch
```

---
## Remote Repositories
Git erleichtert auch das organisierte Arbeiten an lokalen Projekten. Bisher bezogen sich acuh alle verwendeten Befehle rein auf ein lokales Repository. Es ist nicht zwingend notwendig eine weiteres Repository zu verknüpend und die Informationen zwischen diesen abzugleichen.

Um jedoch auch das verteilte Arbeiten zu ermöglichen, kennt git das Konzept des "Remote-Repository". Häufig befindet sich dieses auf einen externen Server. Dieser kann natürlich selbst betriebenm werden, häufig kommen jedoch auch externe Platformen wie GitHub oder GitLab zur Anwendung.
### Clone
Der Einfachste WEg eine solche Verknüpfung herzustellen ist das s. g. "Clonen" eines bereits vorhandenen Projekts.
```
git clone https://github.com/dpidt/public.git
```
Das entsprehcnende Kommando `git clone` erstellt auf Basis des angegebenen Remote-Repositry ein lokales Repository des gleichen Namens an kopiert alle Branches und checkt lokal aus in den dort festgelegten Main-Branch (typischerweise "master").
### Remote
```
git remote
```
Die allgemeine Verweltung von Remote-Repositories erfolgt mit `git remote`. Ohne weitere Parameter listet der Befewhl z. B. alle bekannten Remotes und deren Namen auf. Sol stellt man auch fest, dass ein evtl. vorher durchgeführtes `git clone` implizit den Namen "origin" wählt.

Ein Remote lässt sich natürlich auch explizit und unter Verwendung eines selbst festlegbaren Namens hinzufügen.
```
git remote add yang https://github.com/dpidt/public.git
```
### Push & Pull
Um auf Daten in einem Remote zuzugreifen kommen hauptsächlich drei Kommandos zur Anwendung 
```
git fetch
```
Dieser Befehl holt alle Informationen aus einem Remote (Änderungen, Branches, etc.). Wird kein Name explizit angegeben wird implizit "origin" verwendet. Um diese mit den lokalen Informationen, im aktuellen Branchzu kombinieren ist jetzt noch ein `git merge` notwendig. Da die Kombination dieser beiden Befehle häufig verwendet wird exisitiert dazu eine Abkürzung:
```
git pull
```

Was bisher noch fehlt, ist die umgekehrte Richtung, lokale Änderungen in das Remote schreiben. Git nent dieses einen "Push" und das Kommando lautet dementsprechend `git push`.
```
git push origin master
```
Hier kommen zwei Argumente zur Anwendung, das erste ist der Name des Remotes und der zweite der Branch auf den gepusht werden soll.
---
## Informationen
Git speichert nicht nur den Inhalt der eigentlichen Details sondern noch eine Vielzahl an weiteren Informationen. Diese sind natürlich auch für die Nutzer relevant und über unterschiedliche Befehle zugänglich. 

Einen `git status` liefert einen ersten Überblick über den Zustand des aktuellen Repository. 
```
git status
```
Dieser Verrät z. B. welche Dateien aktuell Änderungen aufweisen, welche vorgenommenen Änderungen für den nächsten Commit in die Staging-Area aufgenommen sind, usw..

Informationen über die History aller vorgenommenen Änderungen und Commits erhält man hingegen mit `git log`, welches z.B. neben einer Auflistung aller Commits die zugehörigen Commit-IDs aufzeigt.
```
git log
```
Das Log kann im Laufe der Zeit sehr lang und komplex werden insbesondere sobald mehrere Branches ins Spiel kommen. `git log` besitzt demensprechend sehr umfangreiche Optionen das Log zu filtern und darstellbar zu machen.

An Hand der Commit-ID lässt sich jetzt beispielsweise die Differenz eines Commits zum aktuellen Zustand des Verteichnisses in Erfahrung bringen:
```
git diff mein-branch
```
Der Befehl `git diff` wird  auch von diversen GUIs und Tools verwendet.


Da Commit-IDs für Menschen nur schwer zuzuordnen sind erlaubt `git tag` das festlegen von eigenen Tags, um z. B. bestimmte besonders relevante Zustände einfacher identifizieren zu können.
```
git tag mein-tag
```
Der obige Befehl identifiziert z. B. den aktuellen Zustand mit dem Tag "mein-tag". Es lassen sich aber natürlich auch vergangene Commits taggen.

---
## Reset & Revert
Beim Arbeiten mit git wird es immer wieder auftreten das Änderungen zurückgenommen werden sollen, die mit Gits funktionalitäten selbst zusammenhängen. Einen vorherigen Zustand (wieder-)herstellen ermöglicht `git reset`, der auch ohne Parameter verwendet werden kann.
```
git reset
```
Mit diesem Befehl nimmt man z. B. auch alle aktuellen Änderungen zurück die bereits als Staged markiert sind. Optionen und Parameter erlauben aber natürlich noch Eingrenzungen oder das addressieren eines Commits durch seine ID. 

Sollen allerdins nicht nur zu einem vorherigen Zustand zurück gesprungen werden, sondern der aktuelle Zustand in einen vergangenen überführt werden ist dafür ein anderer Befehl notwendig.
```
git revert 2c35f516abf7dcb794f6104c7839c9e1a6f0e459
```
Leitet den notewendigen Prozess ein und führt durch evtl. auftretende Konflikte. Wichtig ist dabei im Hinterkopf zu behalten, dass das Kommando neue Commits erstellt.


---
## Hilfe
Git stellt dem Nutzer auch Informationen zu sich selbt und seinen Kommandos zur Verfügung.
```
git help
```
Dieser Befehlt ist die Ausgangsposition. Ohne weitere Parameter wird die allgemeine Hilfe angezeigt. Ein einfaches `git help <COMMAND>` liefert aber auch deutlich detailliertere Informationen zu den einzelnen git befehlen, den vorhandenen Optionen, etc. zu allen Kommandos die bisher in dieser kurzen Einführung verwendet wurden.